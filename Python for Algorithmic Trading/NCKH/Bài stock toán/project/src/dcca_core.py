from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


def _detrend_projector(box_len: int, order: int) -> np.ndarray:
    k = np.arange(box_len, dtype=float)
    if box_len > 1:
        k = 2.0 * (k / (box_len - 1)) - 1.0
    A = np.vander(k, N=order + 1, increasing=True)
    H = A @ np.linalg.pinv(A.T @ A) @ A.T
    R = np.eye(box_len) - H
    return R


def cumulative_profile(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    return np.cumsum(x - x.mean())


def _split_boxes(profile: np.ndarray, s: int) -> np.ndarray:
    n = len(profile)
    ns = n // s
    if ns < 1:
        return np.empty((0, s))
    fwd = profile[: ns * s].reshape(ns, s)
    bwd = profile[n - ns * s :].reshape(ns, s)
    return np.vstack([fwd, bwd])


@dataclass
class DCCAScaleResult:
    s_values: np.ndarray
    n_boxes: np.ndarray
    Fxy2: np.ndarray
    Fxx: np.ndarray
    Fyy: np.ndarray
    rho: np.ndarray

    def to_frame(self) -> pd.DataFrame:
        return pd.DataFrame({
            "s": self.s_values,
            "n_boxes": self.n_boxes,
            "F_xy2": self.Fxy2,
            "F_xx": self.Fxx,
            "F_yy": self.Fyy,
            "rho_dcca": self.rho,
        })


def dcca_at_scale(x: np.ndarray, y: np.ndarray, s: int, order: int = 1,
                   profile_x: np.ndarray | None = None,
                   profile_y: np.ndarray | None = None) -> tuple[float, float, float, int]:
    px = profile_x if profile_x is not None else cumulative_profile(x)
    py = profile_y if profile_y is not None else cumulative_profile(y)
    if s < order + 2:
        raise ValueError(f"s={s} is too small for detrend order={order} (need s >= order+2)")

    boxes_x = _split_boxes(px, s)
    boxes_y = _split_boxes(py, s)
    n_boxes = boxes_x.shape[0]
    if n_boxes == 0:
        return np.nan, np.nan, np.nan, 0

    R = _detrend_projector(s, order)
    resid_x = boxes_x @ R
    resid_y = boxes_y @ R

    f_dcca2 = (resid_x * resid_y).sum(axis=1) / s
    f_dfa_x2 = (resid_x ** 2).sum(axis=1) / s
    f_dfa_y2 = (resid_y ** 2).sum(axis=1) / s

    Fxy2 = f_dcca2.mean()
    Fxx = np.sqrt(f_dfa_x2.mean())
    Fyy = np.sqrt(f_dfa_y2.mean())
    return Fxy2, Fxx, Fyy, n_boxes


def scale_range(n: int, order: int = 1, n_scales: int = 30,
                 s_min: int | None = None, s_max: int | None = None) -> np.ndarray:
    s_min = s_min or max(order + 2, 5)
    s_max = s_max or max(s_min + 1, n // 4)
    raw = np.unique(np.round(np.logspace(np.log10(s_min), np.log10(s_max), n_scales)).astype(int))
    return raw[(raw >= s_min) & (raw <= s_max)]


def compute_dcca_curve(x: pd.Series | np.ndarray, y: pd.Series | np.ndarray,
                        s_values: np.ndarray | None = None, order: int = 1,
                        n_scales: int = 30) -> DCCAScaleResult:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if len(x) != len(y):
        raise ValueError("x and y must have the same length (already time-aligned)")
    n = len(x)

    if s_values is None:
        s_values = scale_range(n, order=order, n_scales=n_scales)

    px = cumulative_profile(x)
    py = cumulative_profile(y)

    Fxy2_list, Fxx_list, Fyy_list, nb_list, rho_list = [], [], [], [], []
    for s in s_values:
        Fxy2, Fxx, Fyy, nb = dcca_at_scale(x, y, int(s), order=order, profile_x=px, profile_y=py)
        rho = Fxy2 / (Fxx * Fyy) if (Fxx > 0 and Fyy > 0) else np.nan
        Fxy2_list.append(Fxy2); Fxx_list.append(Fxx); Fyy_list.append(Fyy)
        nb_list.append(nb); rho_list.append(rho)

    return DCCAScaleResult(
        s_values=np.asarray(s_values),
        n_boxes=np.asarray(nb_list),
        Fxy2=np.asarray(Fxy2_list),
        Fxx=np.asarray(Fxx_list),
        Fyy=np.asarray(Fyy_list),
        rho=np.asarray(rho_list),
    )


def compare_dcca_large_s_to_pearson(x: np.ndarray, y: np.ndarray, order: int = 0) -> dict:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    Fxy2, Fxx, Fyy, nb = dcca_at_scale(x, y, s=n, order=order)
    rho_dcca = Fxy2 / (Fxx * Fyy)
    rho_pearson = np.corrcoef(x, y)[0, 1]
    return {"rho_dcca_s_eq_N": rho_dcca, "rho_pearson": rho_pearson,
            "abs_diff": abs(rho_dcca - rho_pearson)}


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
    from src.data_loader import load_all_timeframes

    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/vn_indices_merged_filled.csv"
    all_tf = load_all_timeframes(data_path)
    ls = all_tf["1D"]
    x = ls.returns["VN30"].values
    y = ls.returns["VNINDEX"].values

    check = compare_dcca_large_s_to_pearson(x, y, order=0)
    print("Qualitative comparison (order=0, s=N) vs Pearson:", check)

    result = compute_dcca_curve(x, y, order=1, n_scales=20)
    print(result.to_frame())
