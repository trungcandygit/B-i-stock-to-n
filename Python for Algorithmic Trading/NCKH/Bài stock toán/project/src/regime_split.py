from __future__ import annotations

import numpy as np
import pandas as pd

KNOWN_EVENTS = {
    "2018 Correction": ("2018-02-01", "2018-07-31"),
    "COVID-19 2020": ("2020-01-15", "2020-04-30"),
    "2022 Corporate Bond/Liquidity Crisis": ("2022-04-01", "2022-11-30"),
}


def bars_per_trading_day(index: pd.DatetimeIndex) -> float:
    counts = pd.Series(1, index=index).groupby(index.normalize()).sum()
    return float(counts.median())


def equivalent_window(index: pd.DatetimeIndex, base_window_1d: int = 20) -> int:
    bpd = bars_per_trading_day(index)
    return max(5, int(round(base_window_1d * bpd)))


def realized_volatility(returns: pd.Series, window: int) -> pd.Series:
    return returns.rolling(window, min_periods=max(5, window // 2)).std(ddof=1)


def split_regimes(returns: pd.Series, window: int | None = None,
                   low_pct: float = 25, high_pct: float = 75) -> pd.DataFrame:
    if window is None:
        window = equivalent_window(returns.index)
    rv = realized_volatility(returns, window)
    lo_thr = rv.quantile(low_pct / 100)
    hi_thr = rv.quantile(high_pct / 100)
    regime = pd.Series("mid", index=rv.index)
    regime[rv < lo_thr] = "low"
    regime[rv > hi_thr] = "high"
    regime[rv.isna()] = np.nan
    return pd.DataFrame({"rv": rv, "regime": regime, "low_threshold": lo_thr,
                          "high_threshold": hi_thr})


def detect_peak_volatility_window(returns: pd.Series, window: int, year: int,
                                   top_n_days: int = 1) -> dict:
    rv = realized_volatility(returns, window)
    rv_year = rv[rv.index.year == year].dropna()
    if rv_year.empty:
        return {"year": year, "found": False}
    peak_date = rv_year.idxmax()
    peak_value = rv_year.max()
    window_start = peak_date - pd.Timedelta(days=int(window * 1.5))
    return {
        "year": year, "found": True,
        "peak_date": peak_date, "peak_rv": peak_value,
        "approx_window_start": max(window_start, rv_year.index.min()),
        "approx_window_end": min(peak_date + pd.Timedelta(days=5), rv_year.index.max()),
        "sample_high_pct_rank": float((rv < peak_value).mean() * 100),
    }


def label_known_events(index: pd.DatetimeIndex) -> pd.Series:
    label = pd.Series("normal", index=index)
    for name, (start, end) in KNOWN_EVENTS.items():
        mask = (index >= pd.Timestamp(start)) & (index <= pd.Timestamp(end))
        label[mask] = name
    return label


def build_regime_report(loaded_series, column: str = "VNINDEX") -> dict:
    returns = loaded_series.returns[column]
    window = equivalent_window(returns.index)
    reg = split_regimes(returns, window=window)
    reg["known_event"] = label_known_events(reg.index)
    years_present = sorted(returns.index.year.unique())
    peak_2025 = detect_peak_volatility_window(returns, window, 2025) if 2025 in years_present else {"found": False}
    return {"window": window, "regime_table": reg, "peak_2025": peak_2025}


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
    from src.data_loader import load_all_timeframes

    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/vn_indices_merged_filled.csv"
    all_tf = load_all_timeframes(data_path)
    for tf, ls in all_tf.items():
        result = build_regime_report(ls)
        print(f"\n=== {tf}: equivalent window = {result['window']} bars ===")
        print(result["regime_table"]["regime"].value_counts())
        print("2025 volatility peak (if any):", result["peak_2025"])
