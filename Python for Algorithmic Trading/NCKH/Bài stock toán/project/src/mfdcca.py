from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

try:
    from .dcca_core import cumulative_profile, _detrend_projector, _split_boxes, scale_range
except ImportError:
    from dcca_core import cumulative_profile, _detrend_projector, _split_boxes, scale_range

Q_DEFAULT = np.array([q for q in range(-5, 6) if q != 0], dtype=float)


def _local_fluctuations(x: np.ndarray, y: np.ndarray, s: int, order: int,
                         profile_x: np.ndarray | None = None,
                         profile_y: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    px = profile_x if profile_x is not None else cumulative_profile(x)
    py = profile_y if profile_y is not None else cumulative_profile(y)
    boxes_x = _split_boxes(px, s)
    boxes_y = _split_boxes(py, s)
    if boxes_x.shape[0] == 0:
        empty = np.empty(0)
        return empty, empty, empty
    R = _detrend_projector(s, order)
    resid_x = boxes_x @ R
    resid_y = boxes_y @ R
    f_dcca2 = (resid_x * resid_y).sum(axis=1) / s
    f_dfa_x2 = (resid_x ** 2).sum(axis=1) / s
    f_dfa_y2 = (resid_y ** 2).sum(axis=1) / s
    return f_dcca2, f_dfa_x2, f_dfa_y2


def _q_average(values_nonneg: np.ndarray, q: float) -> float:
    v = values_nonneg[values_nonneg > 0]
    if len(v) == 0:
        return np.nan
    if q == 0:
        return float(np.exp(0.5 * np.mean(np.log(v))))
    return float(np.mean(v ** (q / 2.0)) ** (1.0 / q))


def _q_average_signed_abs(values_signed: np.ndarray, q: float) -> float:
    v = np.abs(values_signed)
    v = v[v > 0]
    if len(v) == 0:
        return np.nan
    if q == 0:
        return float(np.exp(0.25 * np.mean(np.log(v))))
    return float(np.mean(v ** (q / 2.0)) ** (1.0 / q))


@dataclass
class MFDCCAResult:
    s_values: np.ndarray
    q_values: np.ndarray
    Fxy: np.ndarray
    Fxx: np.ndarray
    Fyy: np.ndarray

    def rho(self) -> np.ndarray:
        with np.errstate(divide="ignore", invalid="ignore"):
            return (self.Fxy ** 2) / (self.Fxx * self.Fyy)

    def lambda_q(self) -> pd.DataFrame:
        rows = []
        log_s = np.log(self.s_values)
        for j, q in enumerate(self.q_values):
            row = {"q": q}
            for name, F in [("lambda_xy", self.Fxy), ("h_x", self.Fxx), ("h_y", self.Fyy)]:
                col = F[:, j]
                mask = np.isfinite(col) & (col > 0)
                if mask.sum() >= 3:
                    slope, intercept = np.polyfit(log_s[mask], np.log(col[mask]), 1)
                else:
                    slope = np.nan
                row[name] = slope
            rows.append(row)
        return pd.DataFrame(rows).set_index("q")

    def rho_frame(self) -> pd.DataFrame:
        return pd.DataFrame(self.rho(), index=self.s_values, columns=self.q_values)


def compute_mfdcca(x: np.ndarray, y: np.ndarray, s_values: np.ndarray | None = None,
                    q_values: np.ndarray | None = None, order: int = 1,
                    n_scales: int = 24) -> MFDCCAResult:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    if s_values is None:
        s_values = scale_range(n, order=order, n_scales=n_scales)
    if q_values is None:
        q_values = Q_DEFAULT

    px = cumulative_profile(x)
    py = cumulative_profile(y)

    Fxy = np.full((len(s_values), len(q_values)), np.nan)
    Fxx = np.full((len(s_values), len(q_values)), np.nan)
    Fyy = np.full((len(s_values), len(q_values)), np.nan)

    for i, s in enumerate(s_values):
        f_dcca2, f_dfa_x2, f_dfa_y2 = _local_fluctuations(x, y, int(s), order, px, py)
        if len(f_dcca2) == 0:
            continue
        for j, q in enumerate(q_values):
            Fxy[i, j] = _q_average_signed_abs(f_dcca2, q)
            Fxx[i, j] = _q_average(f_dfa_x2, q)
            Fyy[i, j] = _q_average(f_dfa_y2, q)

    return MFDCCAResult(s_values=np.asarray(s_values), q_values=np.asarray(q_values),
                         Fxy=Fxy, Fxx=Fxx, Fyy=Fyy)


def multifractal_spectrum(h_q: pd.Series) -> pd.DataFrame:
    q = h_q.index.values.astype(float)
    h = h_q.values.astype(float)
    tau = q * h - 1.0
    alpha = np.gradient(tau, q)
    f_alpha = q * alpha - tau
    return pd.DataFrame({"q": q, "h": h, "tau": tau, "alpha": alpha, "f_alpha": f_alpha}).set_index("q")


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
    from src.data_loader import load_all_timeframes

    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/vn_indices_merged_filled.csv"
    ls = load_all_timeframes(data_path)["1D"]
    x = ls.returns["VN30"].values
    y = ls.returns["VNINDEX"].values

    res = compute_mfdcca(x, y, order=1, n_scales=15)
    print("F_xy(s,q) shape:", res.Fxy.shape)
    lam = res.lambda_q()
    print(lam)
    print("\nMultifractal spectrum of VN30 (h_x):")
    print(multifractal_spectrum(lam["h_x"]))
