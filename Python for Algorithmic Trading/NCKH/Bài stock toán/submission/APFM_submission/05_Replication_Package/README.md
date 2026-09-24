# Online Resource 1 — Replication package

**Manuscript:** Nested Equity Index Correlations Overstate True Co-Movement: Evidence from Vietnam (Asia-Pacific Financial Markets).

This package contains the R code that reproduces every table, figure and in-text number in the manuscript. It also includes the output files produced by that code.

## Contents

| Path | Content |
|---|---|
| `R/dcca.R` | DCCA, MF-DCCA, multifractal spectrum, Monte Carlo reliability threshold, scale regression |
| `run_all.R` | Tables 1–3 and 7 (baseline), Figures 1–3, detrending and proxy diagnostics (outputs `01`–`20`) |
| `run_revision.R` | Block-bootstrap inference (Tables 2, 5 and 6), Forbes–Rigobon with Pearson regimes (Table 4), portfolio variance errors (Section 3.6), GARCH-t reliability thresholds (Table 3), shuffled-surrogate MF-DCCA (Section 3.4) (outputs `R1`–`R7`) |
| `outputs/` | CSV outputs, `scalars.txt` and figures (EPS and 600-dpi PNG) exactly as used in the manuscript |
| `data/` | Empty; place the two input files here (see Data below) |

## Data

The index prices (VN30, VN100 and VNINDEX, HOSE, 30-minute, 1-hour, 4-hour and daily bars, 27 January 2014 to 12 December 2025) were exported from TradingView. The vendor's terms of use do not allow redistribution, so the files are not included. The merged files are available from the corresponding author on reasonable request:

- `data/vn_indices_merged_filled.csv` has the columns `timeframe, time, datetime, VN30, VN100, VNINDEX, USDVND`, one row per bar. Only the `USDVND` column is forward-filled, and it is not used in the analysis.
- `data/vn_indices_merged_raw.csv` has the same columns without filling. `run_revision.R` uses it only to check that the index columns of the two files are identical (output `R1`).

## How to run

Requirements: R ≥ 4.3 with the packages `ggplot2` and `sandwich`; the base packages `stats` and `grDevices` (cairo) are also used.

```
Rscript run_all.R        # about 4 minutes; writes outputs/01_*.csv ... 20_*.csv and outputs/figures/
Rscript run_revision.R   # about 11 minutes with B = 499; writes outputs/R1_*.csv ... R7_*.csv
```

All random draws use fixed seeds (inside the Monte Carlo functions of `R/dcca.R` and at the top of `run_revision.R`), so repeated runs give byte-identical CSV files.

## Mapping to the manuscript

| Manuscript item | Output file |
|---|---|
| Table 1 | `01_descriptive_stats.csv` |
| Table 2 (averages; gap intervals) | `02_table2_average_dcca.csv`; `R2_bootstrap_dcca.csv` (stat = `gap`, `avg_rel`) |
| Table 3 (Gaussian; heavy-tailed) | `03_reliability_smax.csv`; `R6_reliability_garch_t.csv` |
| Table 4 | `R3_forbes_rigobon_pearson_bootstrap.csv` |
| Tables 5 and 6 | `R2_bootstrap_dcca.csv` (stat = `slope_full`, `slope_rel`) |
| Table 7 | `R5_table7_with_pearson_regimes.csv` (and `07_table7_weight_sensitivity.csv`) |
| Section 3.4 (multifractal ranges, surrogates) | `08_mfdcca_hq.csv`, `09_mfdcca_width.csv`, `R7_mfdcca_shuffle_surrogate.csv` |
| Section 3.6 (portfolio variance errors) | `R4_portfolio_error_pearson.csv`, `14b_portfolio_nested_all_frequencies.csv` |
| Figures 1–3 | `outputs/figures/Fig1.eps` … `Fig3.eps` |
