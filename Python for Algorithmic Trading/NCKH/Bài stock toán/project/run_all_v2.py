#!/usr/bin/env python
from __future__ import annotations

import sys
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", category=UserWarning)

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from src.data_loader import load_all_timeframes, descriptive_stats
from src.proxy_builder_v2 import build_all_proxies_v2, W_REAL, HOSE_SNAPSHOT_DATE
from src.dcca_core import compute_dcca_curve, scale_range
from src.mfdcca import compute_mfdcca, multifractal_spectrum
from src.stats_tests import full_inference
from src.regime_split import build_regime_report
from src.portfolio_risk import risk_table_over_scales, compare_static_vs_dcca, min_variance_weights
from src.robustness import (
    compare_pearson_rolling_dcca, sensitivity_to_scale_range, out_of_sample_split,
    validate_against_synthetic_white_noise, validate_against_mfdfa_package,
)
from src.scale_dependence import slope_regression_table
from src.reliability import determine_reliable_smax, add_reliable_column

DATA_PATH = ROOT / "data" / "vn_indices_merged_filled.csv"
TABLES_DIR = ROOT / "outputs_v2" / "tables"
TABLES_DIR.mkdir(parents=True, exist_ok=True)
(ROOT / "outputs_v2" / "figures").mkdir(parents=True, exist_ok=True)

TIMEFRAMES = ["1D", "M30", "H1", "H4"]
RAW_PAIRS = [("VN30", "VNINDEX"), ("VN30", "VN100"), ("VN100", "VNINDEX")]
PROXY_PAIRS_V2 = [
    ("MID_CAP_PROXY_weighted_real", "VN30"),
    ("MID_CAP_PROXY_weighted_heuristic", "VN30"),
    ("MID_CAP_PROXY_ratio", "VN30"),
    ("MID_CAP_PROXY_residual_DEPRECATED", "VN30"),
]
ALL_PAIRS = RAW_PAIRS + PROXY_PAIRS_V2
RELIABILITY_THRESHOLD = 0.05


def log(msg: str):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def save(df: pd.DataFrame, name: str):
    path = TABLES_DIR / name
    df.to_csv(path, index=False)
    log(f"  -> saved {path} ({len(df)} rows, {len(df.columns)} columns)")


def main():
    t_start = time.time()
    log(f"Reading data from {DATA_PATH}")
    all_tf = load_all_timeframes(str(DATA_PATH))

    log("=== [0/9] Determine reliability threshold s_max (white noise, real N per timeframe) ===")
    smax_rows, smax_curve_rows = [], []
    smax_by_timeframe = {}
    for tf in TIMEFRAMES:
        n = len(all_tf[tf].returns)
        res = determine_reliable_smax(n, threshold=RELIABILITY_THRESHOLD, order=1, n_scales=40, n_repeats=8)
        smax_by_timeframe[tf] = res["s_max"]
        smax_rows.append({"timeframe": tf, "n": n, "threshold": RELIABILITY_THRESHOLD,
                           "s_max": res["s_max"], "s_min_scanned": res["s_min_scanned"],
                           "s_max_scanned": res["s_max_scanned"], "note": res["note"]})
        cdf = res["curve"].copy()
        cdf.insert(0, "timeframe", tf)
        smax_curve_rows.append(cdf)
        log(f"  {tf}: N={n} -> s_max={res['s_max']} ({res['note']})")
    save(pd.DataFrame(smax_rows), "21_reliability_smax_v2.csv")
    smax_curve_df = pd.concat(smax_curve_rows, ignore_index=True)

    log("=== [1/9] Descriptive stats, outliers, NEW proxies (Issue 1), stationarity tests ===")
    extended_returns = {}
    desc_frames, outlier_frames, stat_frames = [], [], []
    reg_info_rows, proxy_cmp_rows = [], []

    for tf in TIMEFRAMES:
        ls = all_tf[tf]
        desc = descriptive_stats(ls.returns).reset_index()
        desc.insert(0, "timeframe", tf)
        desc_frames.append(desc)

        out = ls.outlier_report.reset_index()
        out.insert(0, "timeframe", tf)
        outlier_frames.append(out)

        proxies = build_all_proxies_v2(ls)
        stat = proxies["stationarity_tests"].reset_index()
        stat.insert(0, "timeframe", tf)
        stat_frames.append(stat)

        reg_info = dict(proxies["regression_info"])
        reg_info["timeframe"] = tf
        reg_info["w_real"] = proxies["w_real"]
        reg_info["w_heuristic"] = proxies["w_heuristic"]
        reg_info["one_minus_w_real"] = proxies["weight_info_real"]["one_minus_w"]
        reg_info["one_minus_w_heuristic"] = proxies["weight_info_heuristic"]["one_minus_w"]
        reg_info["amplification_real"] = proxies["weight_info_real"]["amplification_factor"]
        reg_info["amplification_heuristic"] = proxies["weight_info_heuristic"]["amplification_factor"]
        reg_info["heuristic_numerically_unstable"] = proxies["weight_info_heuristic"]["numerically_unstable_flag"]
        reg_info_rows.append(reg_info)

        ext = ls.returns.join(proxies["proxy_weighted_real"]).join(proxies["proxy_weighted_heuristic"]) \
                          .join(proxies["proxy_ratio"]).join(proxies["proxy_residual_deprecated"])
        extended_returns[tf] = ext

        proxy_cols = ["MID_CAP_PROXY_weighted_real", "MID_CAP_PROXY_weighted_heuristic",
                      "MID_CAP_PROXY_ratio", "MID_CAP_PROXY_residual_DEPRECATED"]
        corr_mat = ext[proxy_cols].corr()
        for a in proxy_cols:
            for b in proxy_cols:
                if a >= b:
                    continue
                proxy_cmp_rows.append({"timeframe": tf, "proxy_a": a, "proxy_b": b,
                                        "pearson_corr": corr_mat.loc[a, b],
                                        "std_a": ext[a].std(ddof=1), "std_b": ext[b].std(ddof=1)})

    save(pd.concat(desc_frames, ignore_index=True), "01_descriptive_stats_v2.csv")
    save(pd.concat(outlier_frames, ignore_index=True), "02_outlier_report_v2.csv")
    save(pd.concat(stat_frames, ignore_index=True), "03_stationarity_tests_v2.csv")
    save(pd.DataFrame(reg_info_rows), "04_proxy_regression_info_v2.csv")
    save(pd.DataFrame(proxy_cmp_rows), "05_proxy_comparison_v2.csv")

    log("=== [2/9] DCCA curves (m=1,2,3), all pairs x all timeframes ===")
    dcca_rows = []
    dcca_curve_cache = {}
    for tf in TIMEFRAMES:
        ext = extended_returns[tf]
        for (cx, cy) in ALL_PAIRS:
            sub = ext[[cx, cy]].dropna()
            x, y = sub[cx].values, sub[cy].values
            for order in (1, 2, 3):
                curve = compute_dcca_curve(x, y, order=order, n_scales=30).to_frame()
                curve.insert(0, "order", order)
                curve.insert(0, "pair_y", cy)
                curve.insert(0, "pair_x", cx)
                curve.insert(0, "timeframe", tf)
                curve["n_obs"] = len(sub)
                dcca_rows.append(curve)
                if order == 1:
                    dcca_curve_cache[(tf, cx, cy)] = curve.copy()
        log(f"  timeframe {tf} done ({len(ALL_PAIRS)} pairs x 3 detrend orders)")
    dcca_all = pd.concat(dcca_rows, ignore_index=True)
    dcca_all = add_reliable_column(dcca_all, smax_by_timeframe)
    save(dcca_all, "06_dcca_curves_v2.csv")

    log("=== [3/9] MF-DCCA: sweep over q, generalized Hurst, multifractal spectrum ===")
    mfdcca_grid_rows, lambda_q_rows, spectrum_rows = [], [], []
    for tf in TIMEFRAMES:
        ext = extended_returns[tf]
        for (cx, cy) in ALL_PAIRS:
            sub = ext[[cx, cy]].dropna()
            x, y = sub[cx].values, sub[cy].values
            res = compute_mfdcca(x, y, order=1, n_scales=24)
            rho_sq = res.rho()
            for i, s in enumerate(res.s_values):
                for j, q in enumerate(res.q_values):
                    mfdcca_grid_rows.append({
                        "timeframe": tf, "pair_x": cx, "pair_y": cy, "s": s, "q": q,
                        "Fxy": res.Fxy[i, j], "Fxx": res.Fxx[i, j], "Fyy": res.Fyy[i, j],
                        "rho_dcca_sq": rho_sq[i, j],
                    })
            lam = res.lambda_q().reset_index()
            lam.insert(0, "pair_y", cy); lam.insert(0, "pair_x", cx); lam.insert(0, "timeframe", tf)
            lambda_q_rows.append(lam)

            spec_x = multifractal_spectrum(lam.set_index("q")["h_x"]).reset_index()
            spec_x.insert(0, "series_role", "x=" + cx)
            spec_y = multifractal_spectrum(lam.set_index("q")["h_y"]).reset_index()
            spec_y.insert(0, "series_role", "y=" + cy)
            for spec in (spec_x, spec_y):
                spec.insert(0, "pair_y", cy); spec.insert(0, "pair_x", cx); spec.insert(0, "timeframe", tf)
                spectrum_rows.append(spec)
        log(f"  timeframe {tf} MF-DCCA done")
    save(pd.DataFrame(mfdcca_grid_rows), "07_mfdcca_Fxy_grid_v2.csv")
    save(pd.concat(lambda_q_rows, ignore_index=True), "08_mfdcca_lambda_q_v2.csv")
    save(pd.concat(spectrum_rows, ignore_index=True), "09_mfdcca_multifractal_spectrum_v2.csv")

    log("=== [4/9] Statistical inference: Podobnik t-test + bootstrap CI + placebo (may take a few minutes) ===")
    inference_rows = []
    for tf in TIMEFRAMES:
        ext = extended_returns[tf]
        for (cx, cy) in ALL_PAIRS:
            sub = ext[[cx, cy]].dropna()
            x, y = sub[cx].values, sub[cy].values
            t0 = time.time()
            rep = full_inference(x, y, order=1, n_boot=200, n_placebo=30)
            combined = rep.combined().reset_index()
            combined.insert(0, "pair_y", cy); combined.insert(0, "pair_x", cx); combined.insert(0, "timeframe", tf)
            inference_rows.append(combined)
            log(f"  {tf} {cx}-{cy}: {time.time()-t0:.1f}s")
    infer_all = pd.concat(inference_rows, ignore_index=True)
    infer_all = add_reliable_column(infer_all, smax_by_timeframe)
    save(infer_all, "10_stats_inference_v2.csv")

    log("=== [5/9] Volatility regime split (based on VNINDEX) + DCCA by regime ===")
    regime_table_rows, regime_dcca_rows = [], []
    regime_windows = {}
    for tf in TIMEFRAMES:
        ls = all_tf[tf]
        rep = build_regime_report(ls, column="VNINDEX")
        regime_windows[tf] = rep["window"]
        rt = rep["regime_table"].reset_index().rename(columns={"index": "datetime"})
        rt.insert(0, "timeframe", tf)
        regime_table_rows.append(rt)
        log(f"  {tf}: equivalent realized-vol window = {rep['window']} bars")

        ext = extended_returns[tf]
        regime_series = rep["regime_table"]["regime"]
        for (cx, cy) in ALL_PAIRS:
            sub = ext[[cx, cy]].dropna()
            for regime in ("low", "mid", "high"):
                mask = regime_series.reindex(sub.index) == regime
                sub_r = sub[mask.values]
                if len(sub_r) < 4 * (5 + 2):
                    continue
                curve = compute_dcca_curve(sub_r[cx].values, sub_r[cy].values, order=1,
                                            n_scales=15).to_frame()
                curve["n_obs_regime"] = len(sub_r)
                curve.insert(0, "regime", regime)
                curve.insert(0, "pair_y", cy); curve.insert(0, "pair_x", cx); curve.insert(0, "timeframe", tf)
                regime_dcca_rows.append(curve)
    save(pd.concat(regime_table_rows, ignore_index=True), "11_regime_table_v2.csv")
    regime_dcca_df = pd.concat(regime_dcca_rows, ignore_index=True)
    regime_dcca_df = add_reliable_column(regime_dcca_df, smax_by_timeframe)
    save(regime_dcca_df, "12_regime_dcca_curves_v2.csv")

    log("=== [6/9] Portfolio risk: static rho (full-sample 1D) vs rho_DCCA(s) ===")
    rho_static_1d = {}
    ext_1d = extended_returns["1D"]
    for (cx, cy) in ALL_PAIRS:
        sub = ext_1d[[cx, cy]].dropna()
        rho_static_1d[(cx, cy)] = sub[cx].corr(sub[cy])

    risk_scale_rows = []
    for tf in TIMEFRAMES:
        ext = extended_returns[tf]
        for (cx, cy) in ALL_PAIRS:
            sub = ext[[cx, cy]].dropna()
            sigma1, sigma2 = sub[cx].std(ddof=1), sub[cy].std(ddof=1)
            curve = dcca_curve_cache[(tf, cx, cy)]
            table = risk_table_over_scales(curve, sigma1, sigma2, rho_static_1d[(cx, cy)])
            table.insert(0, "pair_y", cy); table.insert(0, "pair_x", cx); table.insert(0, "timeframe", tf)
            risk_scale_rows.append(table)
    risk_scales_df = pd.concat(risk_scale_rows, ignore_index=True)
    risk_scales_df = add_reliable_column(risk_scales_df, smax_by_timeframe)
    save(risk_scales_df, "13_portfolio_risk_scales_v2.csv")

    regime_risk_rows = []
    regime_table_all_df = pd.concat(regime_table_rows, ignore_index=True)
    for tf in TIMEFRAMES:
        ext = extended_returns[tf]
        regime_series = regime_table_all_df[regime_table_all_df["timeframe"] == tf].set_index("datetime")["regime"]
        horizon_s = regime_windows[tf]
        for (cx, cy) in ALL_PAIRS:
            sub = ext[[cx, cy]].dropna()
            for regime in ("low", "high"):
                mask = regime_series.reindex(sub.index) == regime
                sub_r = sub[mask.values]
                if len(sub_r) < 30:
                    continue
                sigma1_r, sigma2_r = sub_r[cx].std(ddof=1), sub_r[cy].std(ddof=1)
                curve_r = regime_dcca_df[(regime_dcca_df.timeframe == tf) & (regime_dcca_df.pair_x == cx)
                                          & (regime_dcca_df.pair_y == cy) & (regime_dcca_df.regime == regime)]
                if curve_r.empty:
                    continue
                nearest_idx = (curve_r["s"] - horizon_s).abs().idxmin()
                rho_true = curve_r.loc[nearest_idx, "rho_dcca"]
                s_used = curve_r.loc[nearest_idx, "s"]
                reliable_used = bool(curve_r.loc[nearest_idx, "reliable"])
                if not np.isfinite(rho_true):
                    continue
                cmp = compare_static_vs_dcca(sigma1_r, sigma2_r, rho_static_1d[(cx, cy)], rho_true, w1=0.5)
                cmp.update({"timeframe": tf, "pair_x": cx, "pair_y": cy, "regime": regime,
                            "s_used": s_used, "horizon_s_target": horizon_s,
                            "n_obs_regime": len(sub_r), "reliable": reliable_used})
                regime_risk_rows.append(cmp)
    save(pd.DataFrame(regime_risk_rows), "14_portfolio_risk_regime_comparison_v2.csv")

    log("=== [7/9] Additional robustness: Pearson/rolling, s ranges, out-of-sample, MFDFA ===")
    pr_rows, sr_rows, oos_rows = [], [], []
    for tf in TIMEFRAMES:
        ext = extended_returns[tf]
        for (cx, cy) in ALL_PAIRS:
            sub = ext[[cx, cy]].dropna()
            x_s, y_s = sub[cx], sub[cy]
            s_vals = scale_range(len(sub), order=1, n_scales=20)

            pr = compare_pearson_rolling_dcca(x_s, y_s, s_vals, order=1)
            pr.insert(0, "pair_y", cy); pr.insert(0, "pair_x", cx); pr.insert(0, "timeframe", tf)
            pr_rows.append(pr)

            ranges = sensitivity_to_scale_range(x_s.values, y_s.values, len(sub), order=1)
            for name, df_r in ranges.items():
                df_r = df_r.copy()
                df_r.insert(0, "range_name", name)
                df_r.insert(0, "pair_y", cy); df_r.insert(0, "pair_x", cx); df_r.insert(0, "timeframe", tf)
                sr_rows.append(df_r)

            oos = out_of_sample_split(x_s, y_s, split_date="2023-01-01", order=1, n_scales=20)
            for split_name, info in oos.items():
                if info["curve"].empty:
                    continue
                dfc = info["curve"].copy()
                dfc["split"] = split_name
                dfc["n_obs"] = info["n_obs"]
                dfc["date_min"] = info["date_min"]
                dfc["date_max"] = info["date_max"]
                dfc.insert(0, "pair_y", cy); dfc.insert(0, "pair_x", cx); dfc.insert(0, "timeframe", tf)
                oos_rows.append(dfc)
        log(f"  timeframe {tf}: additional robustness done")
    save(pd.concat(pr_rows, ignore_index=True), "15_robustness_pearson_rolling_v2.csv")
    save(pd.concat(sr_rows, ignore_index=True), "16_robustness_scale_range_v2.csv")
    save(pd.concat(oos_rows, ignore_index=True), "17_robustness_out_of_sample_v2.csv")

    mfdfa_rows = []
    unique_series = ["VN30", "VN100", "VNINDEX"] + [p[0] for p in PROXY_PAIRS_V2]
    for tf in TIMEFRAMES:
        ext = extended_returns[tf]
        for series_name in unique_series:
            s = ext[series_name].dropna().values
            s_vals_i = scale_range(len(s), order=1, n_scales=15)
            chk = validate_against_mfdfa_package(s, s_vals_i, order=1)
            if "note" in chk.columns:
                continue
            chk.insert(0, "series", series_name)
            chk.insert(0, "timeframe", tf)
            mfdfa_rows.append(chk)
    save(pd.concat(mfdfa_rows, ignore_index=True), "18_robustness_mfdfa_crosscheck_v2.csv")

    wn_rows = []
    for tf in TIMEFRAMES:
        n = len(all_tf[tf].returns)
        for rho0 in (-0.3, 0.0, 0.3, 0.5, 0.7, 0.9):
            df_wn = validate_against_synthetic_white_noise(rho0=rho0, n=n, order=1, n_scales=15)
            df_wn.insert(0, "timeframe", tf)
            wn_rows.append(df_wn)
    save(pd.concat(wn_rows, ignore_index=True), "19_robustness_white_noise_validation_v2.csv")

    log("=== [8/9] Quantitative slope test: rho_DCCA(s) ~ a + b*log(s) ===")
    dcca_order1 = dcca_all[dcca_all.order == 1].copy()
    slope_df = slope_regression_table(dcca_order1, group_cols=("timeframe", "pair_x", "pair_y", "order"),
                                       reliable_only_col="reliable")
    save(slope_df, "20_scale_dependence_regression_v2.csv")

    elapsed = time.time() - t_start
    log(f"=== [9/9] Pipeline v2 COMPLETE in {elapsed/60:.1f} minutes ===")
    print("\n" + "=" * 90)
    print("KEY RESULTS SUMMARY - ROUND 2 (see outputs_v2/tables/*.csv for full detail)")
    print("=" * 90)
    print(f"\nw_real (HOSE factsheet {HOSE_SNAPSHOT_DATE}) = {W_REAL:.4f}")
    print("\nReliable s_max by timeframe (error threshold |error|<=0.05):")
    for r in smax_rows:
        print(f"  {r['timeframe']}: N={r['n']}, s_max={r['s_max']}")
    print("\nSlope of rho_DCCA(s) ~ log(s), full s range, order=1 (1D):")
    slope_1d = slope_df[slope_df.timeframe == "1D"]
    for _, r in slope_1d.iterrows():
        print(f"  {r.pair_x}-{r.pair_y}: slope={r.full_range_slope:.5f}, "
              f"p={r.full_range_p_value:.4g}, significant={r.full_range_significant_5pct}")
    print(f"\nTotal runtime: {elapsed/60:.1f} minutes.")
    print(f"All {len(list(TABLES_DIR.glob('*.csv')))} CSV files saved to: {TABLES_DIR}")


if __name__ == "__main__":
    main()
