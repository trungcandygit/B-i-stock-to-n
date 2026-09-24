from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

PRICE_COLS = ["VN30", "VN100", "VNINDEX", "USDVND"]
VALID_TIMEFRAMES = ("1D", "M30", "H1", "H4")


@dataclass
class LoadedSeries:
    timeframe: str
    prices: pd.DataFrame
    returns: pd.DataFrame
    outlier_report: pd.DataFrame = field(default_factory=pd.DataFrame)


def load_merged_csv(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["datetime"] = pd.to_datetime(df["time"], unit="s")
    df["timeframe"] = df["timeframe"].astype(str)
    for c in PRICE_COLS:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def filter_timeframe(df: pd.DataFrame, timeframe: str) -> pd.DataFrame:
    if timeframe not in VALID_TIMEFRAMES:
        raise ValueError(f"timeframe must be one of {VALID_TIMEFRAMES}, got '{timeframe}'")
    sub = df[df["timeframe"] == timeframe].copy()
    sub = sub.sort_values("datetime").drop_duplicates(subset="datetime")
    sub = sub.set_index("datetime")
    return sub[PRICE_COLS]


def compute_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    log_p = np.log(prices.where(prices > 0))
    rets = log_p.diff().iloc[1:]
    rets = rets.replace([np.inf, -np.inf], np.nan)
    return rets


def detect_outliers(returns: pd.DataFrame, k: float = 5.0) -> pd.DataFrame:
    rows = []
    for col in returns.columns:
        s = returns[col].dropna()
        if len(s) == 0:
            rows.append({"series": col, "n_obs": 0, "n_outliers": 0,
                         "pct_outliers": np.nan, "threshold": np.nan})
            continue
        thr = k * s.std(ddof=1)
        n_out = int((s.abs() > thr).sum())
        rows.append({
            "series": col,
            "n_obs": len(s),
            "n_outliers": n_out,
            "pct_outliers": 100.0 * n_out / len(s),
            "threshold": thr,
        })
    return pd.DataFrame(rows).set_index("series")


def descriptive_stats(returns: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for col in returns.columns:
        s = returns[col].dropna().values
        if len(s) < 8:
            continue
        jb_stat, jb_p = stats.jarque_bera(s)
        rows.append({
            "series": col,
            "n": len(s),
            "mean": s.mean(),
            "std": s.std(ddof=1),
            "annualized_vol_proxy": s.std(ddof=1) * np.sqrt(252),
            "skewness": stats.skew(s),
            "excess_kurtosis": stats.kurtosis(s, fisher=True),
            "jarque_bera_stat": jb_stat,
            "jarque_bera_pvalue": jb_p,
            "reject_normality_5pct": bool(jb_p < 0.05),
        })
    return pd.DataFrame(rows).set_index("series")


def load_timeframe(path: str | Path, timeframe: str, outlier_k: float = 5.0) -> LoadedSeries:
    raw = load_merged_csv(path)
    prices = filter_timeframe(raw, timeframe)
    returns = compute_log_returns(prices)
    outlier_report = detect_outliers(returns, k=outlier_k)
    return LoadedSeries(timeframe=timeframe, prices=prices, returns=returns,
                         outlier_report=outlier_report)


def load_all_timeframes(path: str | Path, outlier_k: float = 5.0) -> dict[str, LoadedSeries]:
    raw = load_merged_csv(path)
    out = {}
    for tf in VALID_TIMEFRAMES:
        if (raw["timeframe"] == tf).sum() == 0:
            continue
        prices = filter_timeframe(raw, tf)
        returns = compute_log_returns(prices)
        outlier_report = detect_outliers(returns, k=outlier_k)
        out[tf] = LoadedSeries(timeframe=tf, prices=prices, returns=returns,
                                outlier_report=outlier_report)
    return out


if __name__ == "__main__":
    import sys

    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/vn_indices_merged_filled.csv"
    all_tf = load_all_timeframes(data_path)
    for tf, ls in all_tf.items():
        print(f"\n=== Timeframe {tf} ({len(ls.prices)} price rows, {len(ls.returns)} return rows) ===")
        print(ls.outlier_report)
        print(descriptive_stats(ls.returns))
