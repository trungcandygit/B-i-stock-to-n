from __future__ import annotations

import numpy as np
import pandas as pd

try:
    from .dcca_core import compute_dcca_curve, scale_range
    from .stats_tests import placebo_shuffle_test
    from .proxy_builder import stationarity_tests
except ImportError:
    from dcca_core import compute_dcca_curve, scale_range
    from stats_tests import placebo_shuffle_test
    from proxy_builder import stationarity_tests


def compare_pearson_rolling_dcca(x: pd.Series, y: pd.Series, s_values: np.ndarray,
                                  order: int = 1) -> pd.DataFrame:
    rho_pearson_static = x.corr(y)
    curve = compute_dcca_curve(x.values, y.values, s_values=s_values, order=order).to_frame()
    rolling_mean = []
    for s in s_values:
        rc = x.rolling(int(s)).corr(y)
        rolling_mean.append(rc.mean())
    curve["rho_pearson_static"] = rho_pearson_static
    curve["rho_rolling_mean"] = rolling_mean
    return curve


def sensitivity_to_detrend_order(x: np.ndarray, y: np.ndarray, s_values: np.ndarray,
                                  orders: tuple[int, ...] = (1, 2, 3)) -> pd.DataFrame:
    frames = []
    for m in orders:
        valid_s = s_values[s_values >= m + 2]
        curve = compute_dcca_curve(x, y, s_values=valid_s, order=m).to_frame()
        curve["order"] = m
        frames.append(curve[["s", "order", "rho_dcca"]])
    return pd.concat(frames, ignore_index=True).pivot(index="s", columns="order", values="rho_dcca")


def sensitivity_to_scale_range(x: np.ndarray, y: np.ndarray, n: int, order: int = 1) -> dict:
    ranges = {
        "range_narrow_small_s": scale_range(n, order=order, n_scales=15, s_max=max(order + 5, n // 20)),
        "range_default": scale_range(n, order=order, n_scales=30),
        "range_wide_large_s": scale_range(n, order=order, n_scales=15, s_min=max(order + 2, n // 40), s_max=n // 3),
    }
    out = {}
    for name, s_vals in ranges.items():
        out[name] = compute_dcca_curve(x, y, s_values=s_vals, order=order).to_frame()
    return out


def cross_timeframe_comparison(returns_by_tf: dict[str, pd.DataFrame], col_x: str, col_y: str,
                                order: int = 1, n_scales: int = 20) -> pd.DataFrame:
    frames = []
    for tf, ret in returns_by_tf.items():
        df = ret[[col_x, col_y]].dropna()
        curve = compute_dcca_curve(df[col_x].values, df[col_y].values, order=order,
                                    n_scales=n_scales).to_frame()
        curve["timeframe"] = tf
        curve["n_obs"] = len(df)
        curve["date_min"] = df.index.min()
        curve["date_max"] = df.index.max()
        frames.append(curve)
    return pd.concat(frames, ignore_index=True)


def out_of_sample_split(x: pd.Series, y: pd.Series, split_date: str = "2023-01-01",
                         order: int = 1, n_scales: int = 20) -> dict:
    df = pd.concat([x, y], axis=1).dropna()
    df.columns = ["x", "y"]
    train = df[df.index < split_date]
    test = df[df.index >= split_date]
    result = {}
    for name, sub in [("train", train), ("test", test)]:
        if len(sub) < 50:
            result[name] = {"n_obs": len(sub), "curve": pd.DataFrame()}
            continue
        curve = compute_dcca_curve(sub["x"].values, sub["y"].values, order=order,
                                    n_scales=n_scales).to_frame()
        result[name] = {"n_obs": len(sub), "date_min": sub.index.min(),
                         "date_max": sub.index.max(), "curve": curve}
    return result


def validate_against_synthetic_white_noise(rho0: float = 0.5, n: int = 3000,
                                            order: int = 1, n_scales: int = 15,
                                            random_state: int = 123) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)
    cov = np.array([[1.0, rho0], [rho0, 1.0]])
    L = np.linalg.cholesky(cov)
    z = rng.standard_normal((n, 2))
    xy = z @ L.T
    x, y = xy[:, 0], xy[:, 1]

    curve = compute_dcca_curve(x, y, order=order, n_scales=n_scales).to_frame()
    curve["rho0_true"] = rho0
    curve["abs_error"] = (curve["rho_dcca"] - rho0).abs()
    return curve


def validate_against_mfdfa_package(x: np.ndarray, s_values: np.ndarray, order: int = 1) -> pd.DataFrame:
    try:
        from MFDFA import MFDFA as mfdfa_func
    except ImportError:
        return pd.DataFrame({"note": ["MFDFA not installed, skipping cross-check"]})

    lag, f = mfdfa_func(x, lag=s_values.astype(int), order=order, q=2)
    f = f.flatten()
    curve = compute_dcca_curve(x, x, s_values=s_values, order=order).to_frame()
    out = pd.DataFrame({"s": lag, "F_MFDFA_package": f})
    out = out.merge(curve[["s", "F_xx"]].rename(columns={"F_xx": "F_ours"}), on="s")
    out["rel_diff_pct"] = 100 * (out["F_ours"] - out["F_MFDFA_package"]).abs() / out["F_MFDFA_package"]
    return out


if __name__ == "__main__":
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 200)

    import sys

    sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
    from src.data_loader import load_all_timeframes

    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/vn_indices_merged_filled.csv"
    all_tf = load_all_timeframes(data_path)
    ls = all_tf["1D"]
    x, y = ls.returns["VN30"], ls.returns["VNINDEX"]
    s_vals = scale_range(len(x), order=1, n_scales=15)

    print("\n=== [9] Synthetic white-noise validation (rho0=0.5) ===")
    print(validate_against_synthetic_white_noise(rho0=0.5).round(4))

    print("\n=== [8] MFDFA package cross-check (F_xx VN30) ===")
    print(validate_against_mfdfa_package(x.values, s_vals, order=1).round(6))

    print("\n=== [1] Pearson vs rolling vs DCCA ===")
    print(compare_pearson_rolling_dcca(x, y, s_vals).round(4))

    print("\n=== [2] Sensitivity to detrend order m ===")
    print(sensitivity_to_detrend_order(x.values, y.values, s_vals).round(4))
