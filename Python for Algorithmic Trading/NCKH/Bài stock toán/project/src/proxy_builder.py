from __future__ import annotations

import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss


def residual_proxy(ret_vn30: pd.Series, ret_vn100: pd.Series) -> tuple[pd.Series, dict]:
    df = pd.concat([ret_vn30.rename("x"), ret_vn100.rename("y")], axis=1).dropna()
    x = df["x"].values
    y = df["y"].values
    X = np.column_stack([np.ones_like(x), x])
    beta_hat, *_ = np.linalg.lstsq(X, y, rcond=None)
    alpha, beta = beta_hat
    fitted = X @ beta_hat
    resid = y - fitted
    ss_res = np.sum(resid ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else np.nan
    info = {"alpha": alpha, "beta": beta, "r_squared": r2, "n": len(df)}
    return pd.Series(resid, index=df.index, name="MID_CAP_PROXY_residual"), info


def ratio_proxy(price_vn30: pd.Series, price_vn100: pd.Series) -> pd.Series:
    df = pd.concat([price_vn30.rename("p30"), price_vn100.rename("p100")], axis=1).dropna()
    log_ratio = np.log(df["p100"] / df["p30"])
    r = log_ratio.diff().dropna()
    r.name = "MID_CAP_PROXY_ratio"
    return r


def compare_proxies(resid: pd.Series, ratio: pd.Series) -> dict:
    df = pd.concat([resid, ratio], axis=1).dropna()
    corr = df.iloc[:, 0].corr(df.iloc[:, 1])
    return {
        "n_overlap": len(df),
        "pearson_corr_between_proxies": corr,
        "std_residual": df.iloc[:, 0].std(ddof=1),
        "std_ratio": df.iloc[:, 1].std(ddof=1),
    }


def stationarity_tests(series: pd.Series, name: str | None = None) -> dict:
    s = series.dropna().values
    name = name or series.name or "series"
    adf_stat, adf_p, adf_lags, adf_nobs, adf_crit, _ = adfuller(s, autolag="AIC")
    with np.errstate(all="ignore"):
        try:
            kpss_stat, kpss_p, kpss_lags, kpss_crit = kpss(s, regression="c", nlags="auto")
        except Exception:
            kpss_stat, kpss_p, kpss_lags = np.nan, np.nan, np.nan
    conclusion = "stationary" if (adf_p < 0.05 and (np.isnan(kpss_p) or kpss_p > 0.05)) else "inconclusive"
    return {
        "series": name,
        "n": len(s),
        "adf_stat": adf_stat,
        "adf_pvalue": adf_p,
        "adf_lags": adf_lags,
        "kpss_stat": kpss_stat,
        "kpss_pvalue": kpss_p,
        "conclusion": conclusion,
    }


def build_all_proxies(loaded_series) -> dict:
    ret = loaded_series.returns
    px = loaded_series.prices

    resid, reg_info = residual_proxy(ret["VN30"], ret["VN100"])
    ratio = ratio_proxy(px["VN30"], px["VN100"])
    comparison = compare_proxies(resid, ratio)

    stat_tests = pd.DataFrame([
        stationarity_tests(ret["VN30"], "VN30_return"),
        stationarity_tests(ret["VN100"], "VN100_return"),
        stationarity_tests(ret["VNINDEX"], "VNINDEX_return"),
        stationarity_tests(resid, "MID_CAP_PROXY_residual"),
        stationarity_tests(ratio, "MID_CAP_PROXY_ratio"),
    ]).set_index("series")

    return {
        "residual_proxy": resid,
        "ratio_proxy": ratio,
        "regression_info": reg_info,
        "proxy_comparison": comparison,
        "stationarity_tests": stat_tests,
    }


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
    from src.data_loader import load_all_timeframes

    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/vn_indices_merged_filled.csv"
    all_tf = load_all_timeframes(data_path)
    for tf, ls in all_tf.items():
        print(f"\n=== Timeframe {tf} ===")
        result = build_all_proxies(ls)
        print("VN100~VN30 regression:", result["regression_info"])
        print("Proxy comparison:", result["proxy_comparison"])
        print(result["stationarity_tests"])
