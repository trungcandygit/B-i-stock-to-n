from __future__ import annotations

import numpy as np
import pandas as pd

try:
    from .robustness import validate_against_synthetic_white_noise
    from .dcca_core import scale_range
except ImportError:
    from robustness import validate_against_synthetic_white_noise
    from dcca_core import scale_range

DEFAULT_RHO0_GRID = (-0.3, 0.0, 0.3, 0.5, 0.7, 0.9)


def worst_case_error_curve(n: int, order: int = 1, n_scales: int = 40,
                            rho0_values=DEFAULT_RHO0_GRID, n_repeats: int = 8,
                            random_state: int = 42) -> pd.DataFrame:
    s_vals = scale_range(n, order=order, n_scales=n_scales)
    frames = []
    for i, rho0 in enumerate(rho0_values):
        reps = []
        for r in range(n_repeats):
            df = validate_against_synthetic_white_noise(
                rho0=rho0, n=n, order=order, n_scales=n_scales,
                random_state=random_state + 1000 * i + r,
            )
            reps.append(df.set_index("s")["abs_error"])
        mean_curve = pd.concat(reps, axis=1).mean(axis=1).reset_index()
        mean_curve.columns = ["s", "abs_error"]
        frames.append(mean_curve)
    all_df = pd.concat(frames, ignore_index=True)
    worst = all_df.groupby("s")["abs_error"].max().reset_index()
    worst = worst.rename(columns={"abs_error": "worst_case_abs_error"}).sort_values("s")
    return worst


def determine_reliable_smax(n: int, threshold: float = 0.05, order: int = 1, n_scales: int = 40,
                             rho0_values=DEFAULT_RHO0_GRID, n_repeats: int = 8,
                             random_state: int = 42) -> dict:
    worst = worst_case_error_curve(n, order=order, n_scales=n_scales, rho0_values=rho0_values,
                                    n_repeats=n_repeats, random_state=random_state)
    violation = worst[worst.worst_case_abs_error > threshold]
    if violation.empty:
        s_max = int(worst.s.max())
        note = "No threshold violation across the scanned s range - s_max = largest s tried."
    else:
        first_violation_s = violation.s.min()
        below = worst[worst.s < first_violation_s]
        s_max = int(below.s.max()) if not below.empty else int(worst.s.min())
        note = f"First violation of threshold {threshold} at s={int(first_violation_s)}."
    return {"n": n, "threshold": threshold, "s_max": s_max, "note": note,
            "s_min_scanned": int(worst.s.min()), "s_max_scanned": int(worst.s.max()),
            "curve": worst}


def add_reliable_column(df: pd.DataFrame, smax_by_timeframe: dict[str, int],
                         s_col: str = "s", tf_col: str = "timeframe") -> pd.DataFrame:
    df = df.copy()
    df["reliable"] = df.apply(lambda r: r[s_col] <= smax_by_timeframe.get(r[tf_col], np.inf), axis=1)
    return df


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
    from src.data_loader import load_all_timeframes

    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 200)

    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/vn_indices_merged_filled.csv"
    all_tf = load_all_timeframes(data_path)
    for tf, ls in all_tf.items():
        n = len(ls.returns)
        result = determine_reliable_smax(n, threshold=0.05, order=1, n_scales=40)
        print(f"{tf} (N={n}): s_max = {result['s_max']}  |  {result['note']}")
