# Online Resource 1 — Replication package

**Manuscript:** The Mechanical Floor of Nested Index Correlations: An Exact Multiscale Decomposition with Evidence from Vietnam.

This package contains the R code that reproduces every table, figure and in-text number in the manuscript, together with the output files produced by that code.

## Contents

| Path | Content |
|---|---|
| `R/dcca.R` | DCCA, MF-DCCA, multifractal spectrum, Monte Carlo reliability threshold, scale regression |
| `run_all.R` | Descriptive statistics, reliability thresholds, average DCCA coefficients, weight sensitivity, MF-DCCA, Fig. 1 and Fig. 4 (MF-DCCA); then calls the two scripts below (outputs `01`–`20`) |
| `run_revision.R` | Block-bootstrap inference for averages, gaps and scaling slopes; Forbes–Rigobon with Pearson regimes; portfolio variance errors; GARCH-t reliability thresholds; shuffled-surrogate MF-DCCA (outputs `R1`–`R7`) |
| `run_round2.R` | Proposition 1 decomposition with bootstrap (`R8*`), Holm and Benjamini–Hochberg adjustment (`R9`), Cohen's q (`R10`), lower-tail dependence (`R11`), DMCA (`R12`), block-length sensitivity (`R13`), Fig. 2 with bootstrap bands and Fig. 3 (decomposition), session information |
| `outputs/` | CSV outputs, `scalars.txt`, `R_session_info.txt` and figures (EPS and 600-dpi PNG) exactly as used in the manuscript |
| `data/` | Empty; place the two input files here (see Data below) |

## Data

The index prices (VN30, VN100 and VNINDEX, exchange HOSE, 30-minute, 1-hour, 4-hour and daily bars, 27 January 2014 to 12 December 2025) were exported from TradingView (files `HOSE_DLY_VN301D.csv`, `HOSE_DLY_VN1001D.csv`, `HOSE_DLY_VNINDEX1D.csv`, the corresponding 30-minute files, and `HOSEVN30H1.csv`/`HOSEVN30H4.csv` and their VN100/VNINDEX counterparts for the 1-hour and 4-hour bars). The vendor's terms of use do not allow redistribution, so the files are not included. The merged files are available from the corresponding author on reasonable request:

- `data/vn_indices_merged_filled.csv` has the columns `timeframe, time, datetime, VN30, VN100, VNINDEX, USDVND`, one row per bar. Only the `USDVND` column is forward-filled, and it is not used in the analysis.
- `data/vn_indices_merged_raw.csv` has the same columns without filling; `run_revision.R` uses it only to check that the index columns of the two files are identical (output `R1`).

## How to run

Requirements: R ≥ 4.3 with `ggplot2` and `sandwich`; base `stats`, `parallel` and `grDevices` (cairo) are also used. Tested with R 4.3.3, ggplot2 3.4.4 and sandwich 3.1.0 (see `outputs/R_session_info.txt`).

```
Rscript run_all.R     # about 3 minutes, then runs run_revision.R (about 8 minutes) and run_round2.R (B = 499)
RUN_ALL_MAIN_ONLY=1 Rscript run_all.R   # main script only
```

All random draws use fixed seeds (inside the Monte Carlo functions of `R/dcca.R`, and `set.seed()` at the top of `run_revision.R` and `run_round2.R`), so repeated runs give byte-identical CSV files.

## Mapping to the manuscript

| Manuscript item | Output file |
|---|---|
| Table 1 | Literature (no output) |
| Table 2 | `01_descriptive_stats.csv` |
| Table 3 (Gaussian; heavy-tailed) | `03_reliability_smax.csv`; `R6_reliability_garch_t.csv` |
| Table 4 (averages; gap intervals; Cohen's q) | `02_table2_average_dcca.csv`; `R2_bootstrap_dcca.csv` (stat = `gap`); `R10_effect_size_cohen_q.csv` |
| Table 5 (Proposition 1) | `R8_overlap_decomposition.csv`; by scale: `R8b_overlap_decomposition_by_scale.csv`; Pearson case: `R8d_overlap_decomposition_pearson.csv` |
| Table 6 and Table A1 (slopes, Holm, BH) | `R9_slope_tests_multiplicity.csv` (from `R2_bootstrap_dcca.csv`) |
| Table 7 | `R3_forbes_rigobon_pearson_bootstrap.csv` |
| Section 5.7 (portfolio variance errors) | `R4_portfolio_error_pearson.csv` |
| Section 5.8 (multifractal ranges, surrogates) | `08_mfdcca_hq.csv`, `09_mfdcca_width.csv`, `R7_mfdcca_shuffle_surrogate.csv` |
| Table A2 | `R5_table7_with_pearson_regimes.csv` |
| Table A3 | `R12_dmca_robustness.csv` |
| Table A4 | `R11_lower_tail_dependence.csv` |
| Table A5 | `R13_block_length_sensitivity.csv` |
| Section 3.2 (sample sizes, crisis episodes) | `01_descriptive_stats.csv`, `02_table2_average_dcca.csv`, `11_crisis_episode_diagnostics.csv`, `scalars.txt` |
| Section 4.2 (proxy diagnostics) | `04_proxy_regression.csv`, `05_proxy_comparison.csv`, `scalars.txt` |
| Fig. 1 | `outputs/figures/Fig1.eps` (`fig1_volatility_regimes.png`) |
| Fig. 2 | `outputs/figures/Fig2.eps` (`fig2_dcca_curves.png`; bands from `R8c_dcca_bootstrap_bands.csv`) |
| Fig. 3 | `outputs/figures/Fig4.eps` (`fig4_overlap_decomposition.png`) |
| Fig. 4 | `outputs/figures/Fig3.eps` (`fig3_mfdcca.png`) |

Note: the file names of Figs. 3 and 4 are swapped relative to their order in the manuscript; the submission folder `03_Figures/` uses the manuscript numbering.
