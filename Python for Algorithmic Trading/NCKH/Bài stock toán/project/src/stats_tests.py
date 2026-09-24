from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import stats

try:
    from .dcca_core import compute_dcca_curve, dcca_at_scale, cumulative_profile
except ImportError:
    from dcca_core import compute_dcca_curve, dcca_at_scale, cumulative_profile


def podobnik_significance_test(rho: np.ndarray, s_values: np.ndarray, n: int) -> pd.DataFrame:
    rows = []
    for s, r in zip(s_values, rho):
        n_s = n / s - 2.0
        if not np.isfinite(r) or n_s <= 0 or abs(r) >= 1:
            rows.append({"s": s, "n_s": n_s, "t_stat": np.nan, "p_value": np.nan,
                         "significant_5pct": False})
            continue
        t_stat = r * np.sqrt(n_s / (1 - r ** 2))
        p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df=n_s))
        rows.append({"s": s, "n_s": n_s, "t_stat": t_stat, "p_value": p_val,
                     "significant_5pct": bool(p_val < 0.05)})
    return pd.DataFrame(rows).set_index("s")


def moving_block_bootstrap_ci(x: np.ndarray, y: np.ndarray, s_values: np.ndarray,
                               order: int = 1, n_boot: int = 200,
                               block_len: int | None = None,
                               ci: float = 0.95, random_state: int | None = 42) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)
    n = len(x)
    if block_len is None:
        block_len = max(20, int(3 * max(s_values)))
    block_len = min(block_len, n // 2)
    n_blocks_needed = int(np.ceil(n / block_len))
    max_start = n - block_len

    boot_rho = np.full((n_boot, len(s_values)), np.nan)
    for b in range(n_boot):
        starts = rng.integers(0, max_start + 1, size=n_blocks_needed)
        idx = np.concatenate([np.arange(st, st + block_len) for st in starts])[:n]
        xb, yb = x[idx], y[idx]
        px, py = cumulative_profile(xb), cumulative_profile(yb)
        for j, s in enumerate(s_values):
            try:
                Fxy2, Fxx, Fyy, nb = dcca_at_scale(xb, yb, int(s), order=order,
                                                    profile_x=px, profile_y=py)
                boot_rho[b, j] = Fxy2 / (Fxx * Fyy) if (Fxx > 0 and Fyy > 0) else np.nan
            except ValueError:
                boot_rho[b, j] = np.nan

    alpha = 1 - ci
    lo = np.nanpercentile(boot_rho, 100 * alpha / 2, axis=0)
    hi = np.nanpercentile(boot_rho, 100 * (1 - alpha / 2), axis=0)
    mean_boot = np.nanmean(boot_rho, axis=0)
    std_boot = np.nanstd(boot_rho, axis=0)
    return pd.DataFrame({"s": s_values, "boot_mean": mean_boot, "boot_std": std_boot,
                          "ci_lower": lo, "ci_upper": hi}).set_index("s")


def placebo_shuffle_test(x: np.ndarray, y: np.ndarray, s_values: np.ndarray, order: int = 1,
                          n_repeats: int = 30, random_state: int | None = 42) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)
    n = len(x)
    placebo_rho = np.full((n_repeats, len(s_values)), np.nan)
    for r in range(n_repeats):
        y_shuffled = rng.permutation(y)
        px = cumulative_profile(x)
        py = cumulative_profile(y_shuffled)
        for j, s in enumerate(s_values):
            Fxy2, Fxx, Fyy, nb = dcca_at_scale(x, y_shuffled, int(s), order=order,
                                                profile_x=px, profile_y=py)
            placebo_rho[r, j] = Fxy2 / (Fxx * Fyy) if (Fxx > 0 and Fyy > 0) else np.nan
    return pd.DataFrame({
        "s": s_values,
        "placebo_mean": np.nanmean(placebo_rho, axis=0),
        "placebo_std": np.nanstd(placebo_rho, axis=0),
        "placebo_abs_mean": np.nanmean(np.abs(placebo_rho), axis=0),
    }).set_index("s")


@dataclass
class DCCAInferenceReport:
    curve: pd.DataFrame
    significance: pd.DataFrame
    bootstrap_ci: pd.DataFrame
    placebo: pd.DataFrame

    def combined(self) -> pd.DataFrame:
        out = self.curve.set_index("s").join(self.significance).join(self.bootstrap_ci,
                                                                        rsuffix="_boot")
        out = out.join(self.placebo, rsuffix="_placebo")
        return out


def full_inference(x: np.ndarray, y: np.ndarray, s_values: np.ndarray | None = None,
                    order: int = 1, n_boot: int = 200, n_placebo: int = 30,
                    random_state: int | None = 42) -> DCCAInferenceReport:
    curve = compute_dcca_curve(x, y, s_values=s_values, order=order)
    s_vals = curve.s_values
    sig = podobnik_significance_test(curve.rho, s_vals, n=len(x))
    boot = moving_block_bootstrap_ci(x, y, s_vals, order=order, n_boot=n_boot,
                                      random_state=random_state)
    placebo = placebo_shuffle_test(x, y, s_vals, order=order, n_repeats=n_placebo,
                                    random_state=random_state)
    return DCCAInferenceReport(curve=curve.to_frame(), significance=sig,
                                bootstrap_ci=boot, placebo=placebo)


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
    from src.data_loader import load_all_timeframes

    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/vn_indices_merged_filled.csv"
    ls = load_all_timeframes(data_path)["1D"]
    x = ls.returns["VN30"].values
    y = ls.returns["VNINDEX"].values

    report = full_inference(x, y, order=1, n_boot=100, n_placebo=20)
    print(report.combined().round(4))
