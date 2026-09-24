from __future__ import annotations

import numpy as np
import pandas as pd

try:
    from .proxy_builder import residual_proxy, ratio_proxy, stationarity_tests
except ImportError:
    from proxy_builder import residual_proxy, ratio_proxy, stationarity_tests

HOSE_SNAPSHOT_DATE = "2024-05-31"
HOSE_SNAPSHOT_SOURCE = ("static2.vietstock.vn/vietstock/2024/6/12/"
                        "20240612_form_factsheet_mcindices_eng_t06_2024.pdf")
HOSE_VN30_FREEFLOAT_CAP_BVND = 1_316_288.0
HOSE_VN100_FREEFLOAT_CAP_BVND = 1_928_303.0
HOSE_VNMIDCAP_FREEFLOAT_CAP_BVND = 612_014.0
W_REAL = HOSE_VN30_FREEFLOAT_CAP_BVND / HOSE_VN100_FREEFLOAT_CAP_BVND


def weighted_decomposition_proxy(ret_vn30: pd.Series, ret_vn100: pd.Series, w: float,
                                  label: str) -> tuple[pd.Series, dict]:
    df = pd.concat([ret_vn30.rename("x"), ret_vn100.rename("y")], axis=1).dropna()
    one_minus_w = 1.0 - w
    unstable = abs(one_minus_w) < 0.05
    r_mid = (df["y"] - w * df["x"]) / one_minus_w
    r_mid.name = f"MID_CAP_PROXY_{label}"
    info = {
        "label": label, "w": w, "one_minus_w": one_minus_w,
        "amplification_factor": 1.0 / one_minus_w if one_minus_w != 0 else np.inf,
        "std_input_VN100": df["y"].std(ddof=1),
        "std_output_proxy": r_mid.std(ddof=1),
        "numerically_unstable_flag": unstable,
        "n": len(df),
    }
    return r_mid, info


def heuristic_weight_from_vol_ratio(ret_vn30: pd.Series, ret_vn100: pd.Series, beta: float) -> float:
    df = pd.concat([ret_vn30.rename("x"), ret_vn100.rename("y")], axis=1).dropna()
    return float(df["x"].std(ddof=1) * beta / df["y"].std(ddof=1))


def build_all_proxies_v2(loaded_series) -> dict:
    ret = loaded_series.returns
    px = loaded_series.prices

    resid_deprecated, reg_info = residual_proxy(ret["VN30"], ret["VN100"])
    beta = reg_info["beta"]

    w_heuristic = heuristic_weight_from_vol_ratio(ret["VN30"], ret["VN100"], beta)
    proxy_real, info_real = weighted_decomposition_proxy(ret["VN30"], ret["VN100"], W_REAL, "weighted_real")
    proxy_heur, info_heur = weighted_decomposition_proxy(ret["VN30"], ret["VN100"], w_heuristic, "weighted_heuristic")
    proxy_ratio = ratio_proxy(px["VN30"], px["VN100"])
    resid_deprecated.name = "MID_CAP_PROXY_residual_DEPRECATED"

    stat_tests = pd.DataFrame([
        stationarity_tests(proxy_real, "MID_CAP_PROXY_weighted_real"),
        stationarity_tests(proxy_heur, "MID_CAP_PROXY_weighted_heuristic"),
        stationarity_tests(proxy_ratio, "MID_CAP_PROXY_ratio"),
        stationarity_tests(resid_deprecated, "MID_CAP_PROXY_residual_DEPRECATED"),
    ]).set_index("series")

    return {
        "proxy_weighted_real": proxy_real,
        "proxy_weighted_heuristic": proxy_heur,
        "proxy_ratio": proxy_ratio,
        "proxy_residual_deprecated": resid_deprecated,
        "regression_info": reg_info,
        "weight_info_real": info_real,
        "weight_info_heuristic": info_heur,
        "w_real": W_REAL,
        "w_heuristic": w_heuristic,
        "stationarity_tests": stat_tests,
    }


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
    from src.data_loader import load_all_timeframes

    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 200)

    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/vn_indices_merged_filled.csv"
    all_tf = load_all_timeframes(data_path)
    print(f"W_REAL (from HOSE factsheet {HOSE_SNAPSHOT_DATE}) = {W_REAL:.4f}\n")
    for tf, ls in all_tf.items():
        result = build_all_proxies_v2(ls)
        print(f"=== {tf} ===")
        print("w_heuristic (=corr(r30,r100)):", f"{result['w_heuristic']:.4f}")
        print("Info A1 (real):", result["weight_info_real"])
        print("Info A2 (heuristic):", result["weight_info_heuristic"])
        print(result["stationarity_tests"])
        print()
