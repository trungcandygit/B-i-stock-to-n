from __future__ import annotations

import re
import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
TABLES_DIR = ROOT / "outputs_v2" / "tables"
DB_PATH = ROOT / "outputs_v2" / "nckh_dcca_results.db"
ARCHIVE_PATH = ROOT / "outputs_v2" / "nckh_dcca_results_archive.txt"

DESCRIPTIONS = {
    "descriptive_stats": "Descriptive statistics (mean, std, skewness, kurtosis, Jarque-Bera test) of log-returns for VN30, VN100, VNINDEX across all 4 timeframes.",
    "outlier_report": "Count and percentage of outlier observations (|return| > 5x std) per series and timeframe.",
    "stationarity_tests": "ADF and KPSS stationarity test results for raw returns and the four MID_CAP_PROXY variants across all timeframes.",
    "proxy_regression_info": "OLS regression info (alpha, beta, R-squared) of VN100 returns on VN30 returns, plus the real and heuristic capitalization weights (w_real, w_heuristic) used to build the weighted MID_CAP_PROXY variants.",
    "proxy_comparison": "Pairwise Pearson correlation and standard deviation comparison among the four MID_CAP_PROXY variants (weighted_real, weighted_heuristic, ratio, residual_DEPRECATED).",
    "dcca_curves": "Full DCCA rho(s) curves for every index pair, timeframe, and detrend order (m=1,2,3), with a reliable-scale flag based on the s_max threshold.",
    "mfdcca_Fxy_grid": "Multifractal DCCA fluctuation functions F_xy, F_xx, F_yy and the generalized correlation rho(s,q) across the full (s,q) grid for every pair and timeframe.",
    "mfdcca_lambda_q": "Generalized cross-correlation exponent lambda(q) and generalized Hurst exponents h_x(q), h_y(q) estimated by log-log regression for every pair and timeframe.",
    "mfdcca_multifractal_spectrum": "Multifractal spectrum (tau(q), alpha(q), f(alpha)) derived via Legendre transform from the generalized Hurst exponents of each series.",
    "stats_inference": "Podobnik significance test, moving-block bootstrap confidence intervals, and placebo shuffle test results for rho_DCCA(s), with a reliable-scale flag.",
    "regime_table": "Rolling realized volatility, low/mid/high volatility regime labels, and known market-event labels (2018/2020/2022) for VNINDEX across all timeframes.",
    "regime_dcca_curves": "DCCA rho(s) curves computed separately within each volatility regime (low/mid/high) for every pair and timeframe.",
    "portfolio_risk_scales": "Markowitz 50/50 and minimum-variance portfolio variance comparison between static Pearson correlation and rho_DCCA(s) across all scales.",
    "portfolio_risk_regime_comparison": "Portfolio variance and volatility estimation error from using a static full-sample correlation instead of the true regime-specific rho_DCCA(s).",
    "robustness_pearson_rolling": "Comparison of rho_DCCA(s), full-sample static Pearson correlation, and rolling-window Pearson correlation for every pair and timeframe.",
    "robustness_scale_range": "Sensitivity of the rho_DCCA(s) curve to three different choices of the scale (s) grid: narrow/small-s, default, and wide/large-s.",
    "robustness_out_of_sample": "Out-of-sample stability check of rho_DCCA(s), splitting each series into a 2014-2022 training period and a 2023-2025 test period.",
    "robustness_mfdfa_crosscheck": "Cross-validation of the in-house DFA fluctuation function F_xx(s) against the independent MFDFA Python package.",
    "robustness_white_noise_validation": "Monte Carlo validation recovering a known Pearson correlation rho0 from simulated bivariate Gaussian white noise, run at each timeframe's true sample size N.",
    "scale_dependence_regression": "OLS regression of rho_DCCA(s) on log(s) (slope, p-value, R-squared) over the full scale range and over the reliable-scale range only, for every pair and timeframe.",
    "reliability_smax": "The maximum reliable time scale s_max per timeframe, determined from the white-noise Monte Carlo worst-case absolute error at a 0.05 threshold.",
}


def table_name_from_filename(filename: str) -> str:
    name = filename[:-4] if filename.lower().endswith(".csv") else filename
    name = re.sub(r"^\d+_", "", name)
    name = re.sub(r"_(v2|all)$", "", name)
    return name


def count_csv_data_rows(csv_path: Path) -> int:
    with open(csv_path, "r", encoding="utf-8") as f:
        n_lines = sum(1 for _ in f)
    return max(n_lines - 1, 0)


def build_database(csv_files: list[Path]) -> list[dict]:
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)

    index_rows = []
    for csv_path in csv_files:
        table_name = table_name_from_filename(csv_path.name)
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        index_rows.append({
            "table_name": table_name,
            "source_csv_filename": csv_path.name,
            "n_rows": df.shape[0],
            "n_columns": df.shape[1],
            "column_names": ", ".join(df.columns),
            "description": DESCRIPTIONS.get(table_name, "No description available."),
        })

    index_df = pd.DataFrame(index_rows)
    index_df.to_sql("_index", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()
    return index_rows


def build_archive(csv_files: list[Path], index_rows: list[dict]) -> None:
    by_name = {r["table_name"]: r for r in index_rows}
    lines = []

    lines.append("=" * 80)
    lines.append("TABLE OF CONTENTS")
    lines.append("=" * 80)
    for i, csv_path in enumerate(csv_files, 1):
        table_name = table_name_from_filename(csv_path.name)
        lines.append(f"{i}. {table_name}")
    lines.append("=" * 80)
    lines.append("")
    lines.append("")

    for csv_path in csv_files:
        table_name = table_name_from_filename(csv_path.name)
        meta = by_name[table_name]
        raw_text = csv_path.read_text(encoding="utf-8")

        lines.append("=" * 80)
        lines.append(f"TABLE: {table_name}")
        lines.append(f"SOURCE: {csv_path.name}")
        lines.append(f"ROWS: {meta['n_rows']}")
        lines.append(f"COLUMNS: {meta['column_names']}")
        lines.append(f"DESCRIPTION: {meta['description']}")
        lines.append("=" * 80)
        lines.append(raw_text.rstrip("\n"))
        lines.append("")
        lines.append("")

    ARCHIVE_PATH.write_text("\n".join(lines), encoding="utf-8")


def verify(csv_files: list[Path], index_rows: list[dict]) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    archive_text = ARCHIVE_PATH.read_text(encoding="utf-8")

    all_ok = True
    print(f"\n{'table_name':<38}{'csv_rows':>10}{'db_rows':>10}{'txt_rows':>10}  content_intact  match")
    print("-" * 96)
    for csv_path, meta in zip(csv_files, index_rows):
        table_name = meta["table_name"]
        expected_rows = count_csv_data_rows(csv_path)

        cur.execute(f'SELECT COUNT(*) FROM "{table_name}"')
        db_rows = cur.fetchone()[0]

        raw_text = csv_path.read_text(encoding="utf-8")
        content_intact = raw_text.rstrip("\n") in archive_text
        txt_rows = max(len(raw_text.splitlines()) - 1, 0)

        ok = content_intact and (expected_rows == db_rows == txt_rows)
        all_ok = all_ok and ok
        print(f"{table_name:<38}{expected_rows:>10}{db_rows:>10}{txt_rows:>10}  "
              f"{str(content_intact):>14}  {'OK' if ok else 'MISMATCH'}")

    conn.close()
    return all_ok


def main():
    csv_files = sorted(TABLES_DIR.glob("*.csv"))
    print(f"Found {len(csv_files)} CSV files in {TABLES_DIR}")

    index_rows = build_database(csv_files)
    print(f"Wrote SQLite database: {DB_PATH}")

    build_archive(csv_files, index_rows)
    print(f"Wrote text archive: {ARCHIVE_PATH}")

    all_ok = verify(csv_files, index_rows)

    db_size = DB_PATH.stat().st_size
    txt_size = ARCHIVE_PATH.stat().st_size

    print("\n" + "=" * 80)
    print(f"Tables consolidated : {len(csv_files)}")
    print(f"SQLite database size: {db_size:,} bytes ({db_size/1024:.1f} KB)")
    print(f"Text archive size   : {txt_size:,} bytes ({txt_size/1024:.1f} KB)")
    print(f"Row-count verification (CSV vs DB vs TXT): {'ALL MATCH' if all_ok else 'MISMATCH FOUND - see table above'}")
    print("=" * 80)
    print(f"Original CSV files in {TABLES_DIR} were left untouched.")


if __name__ == "__main__":
    main()
