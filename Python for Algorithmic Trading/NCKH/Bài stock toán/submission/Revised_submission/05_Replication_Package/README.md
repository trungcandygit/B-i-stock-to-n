# Online Resource 1: Replication package

**Manuscript:** How Much of a Nested Index Correlation Is Construction? A Scale-Wise Part–Whole Decomposition with Evidence from Vietnam.

This package contains the R code that reproduces every table, figure and in-text number in the manuscript and in the Supplementary Material (Online Resource 2), together with the output files produced by that code.

## Contents

| Path | Content |
|---|---|
| `R/dcca.R` | DCCA, MF-DCCA, multifractal spectrum, Monte Carlo reliability threshold, scale regression |
| `run_all.R` | Descriptive statistics, reliability thresholds, average DCCA coefficients, weight sensitivity, MF-DCCA, Fig. 1 and Fig. S1; then calls the seven scripts below (outputs `01`–`20`) |
| `run_revision.R` | Block-bootstrap inference for averages, gaps and slopes; Forbes–Rigobon with Pearson regimes; portfolio variance errors; GARCH-t reliability thresholds; shuffled-surrogate MF-DCCA (`R1`–`R7`) |
| `run_round2.R` | Lemma 1 decomposition with bootstrap (`R8*`), Holm and Benjamini–Hochberg adjustment (`R9`), Cohen's q (`R10`), lower-tail dependence (`R11`), DMCA (`R12`), daily block-length sensitivity (`R13`), Figs. 2 and 3, session information |
| `run_round3.R` | Weight grid of the decomposition (`R14`), Shapley attribution and scale invariance (`R15`), lower bound (`R16`), contour chart Fig. 4 (`R17`), out-of-sample forecasts (`R18`), factor regressions by regime (`R19`), hedge effectiveness (`R20`) |
| `run_round3b.R` | Weight drawn inside the bootstrap (`R21`), studentized p-values, H2 family and TOST (`R22`), first bar removed (`R23`), M30 block lengths (`R24`), Forbes–Rigobon with VN30 regimes and weight grid (`R25`), Gaussian-copula tail benchmark (`R26`) |
| `run_round3c.R` | Unshaded volatility episodes (`R27`), lead–lag cross-autocorrelations (`R28`) |
| `run_round3d.R` | Factor-loading contagion test (`R29`), slope channels (`R30`), materiality and joint resampling (`R31`), intraday bar schedule (`R32`), Box 1 recipe (`R33`) |
| `run_round3e.R` | Slopes with and without auction bars and broad-minus-nested slope differences (`R34`), slope block lengths at M30 (`R35`), like-for-like gap with weight uncertainty (`R36`), 2021 counted as a crisis (`R37`) |
| `outputs/` | CSV outputs, `scalars.txt`, `R_session_info.txt` and figures (EPS and 600-dpi PNG) exactly as used in the manuscript |
| `data/` | Empty; place the two input files here (see Data below) |

## Data

The index prices (VN30, VN100 and VNINDEX, exchange HOSE, 30-minute, 1-hour, 4-hour and daily bars, 27 January 2014 to 12 December 2025) were exported from TradingView. The vendor's terms of use do not allow redistribution, so the files are not included. Daily closing levels of the three indices are published by the HOSE; we did not compare them with the vendor series date by date. The merged files are available from the corresponding author on reasonable request:

- `data/vn_indices_merged_filled.csv` (SHA-256 `b4b0c31e673baa0c949706f047f2167ec2c866b4b2dec52f494e73a68ba6b1c4`): columns `timeframe, time, datetime, VN30, VN100, VNINDEX, USDVND`, one row per bar. Only the `USDVND` column is forward-filled, and it is not used.
- `data/vn_indices_merged_raw.csv` (SHA-256 `69118a65518a523f0c2c234faae4c201897d3f038868b0b8ad9eff733bfcbe71`): the same columns without filling; used only to check that the index columns of the two files are identical (output `R1`).

## How to run

Requirements: R ≥ 4.3 with `ggplot2` and `sandwich`; base `stats`, `parallel` and `grDevices` (cairo). Tested with R 4.3.3 (stats, sandwich 3.1.0, ggplot2 3.4.4) on an Intel Xeon processor (2.10 GHz, four cores); see `outputs/R_session_info.txt`. OLS uses the QR decomposition, so no iterative optimization is involved; the reliability simulations use fixed seeds starting at 42.

```
Rscript run_all.R                       # main script, then the seven follow-up scripts in order
RUN_ALL_MAIN_ONLY=1 Rscript run_all.R   # main script only
```

Every script fixes its seed with `set.seed()` (20260924 to 20261014), so repeated runs give byte-identical CSV files.

## Mapping to the manuscript

| Manuscript item | Output file |
|---|---|
| Table 1 | Literature (no output) |
| Box 1 | `R33_practitioner_recipe.csv` |
| Table 2 | `01_descriptive_stats.csv` |
| Table 3 | `03_reliability_smax.csv`; `R6_reliability_garch_t.csv` |
| Table 4 | `02_table2_average_dcca.csv`; `R2_bootstrap_dcca.csv` (three-pair gap); `R15_attribution_and_scale_invariance.csv` (`gap_like`); `R10_effect_size_cohen_q.csv` |
| Table 5, Panel A | `R8_overlap_decomposition.csv`; `R16_true_lower_bound.csv`; `R15_…` (Shapley share) |
| Table 5, Panel B | `R21_weight_uncertainty_bootstrap.csv` |
| Section 5.3 (scale invariance, Pearson case) | `R8b_overlap_decomposition_by_scale.csv`, `R15_…` (`floor_slope`, `floor_range`), `R8d_overlap_decomposition_pearson.csv` |
| Table 6 | `R22_h3_family_studentized_tost.csv` (from `R9_slope_tests_multiplicity.csv` and `R2_bootstrap_dcca.csv`) |
| Table 7 | `R3_forbes_rigobon_pearson_bootstrap.csv`, `R25_…` (VN30 quartiles, factsheet weight), `R29_factor_model_contagion_test.csv` |
| Table 8 | `R31_materiality_joint_resampling.csv`; `R18_out_of_sample_portfolio_variance.csv`, `R18b_oos_design.csv` |
| Section 3.1 (bar schedule) | `R32_intraday_bar_schedule.csv` |
| Section 3.2 (samples, episodes) | `01_…`, `02_…`, `11_crisis_episode_diagnostics.csv`, `R27_unshaded_episodes.csv`, `scalars.txt` |
| Section 6.1 (lead–lag); 6.2 (hedge) | `R28_lead_lag_tiers.csv`; `R20_hedge_effectiveness.csv` |
| Table S1 | `R9_slope_tests_multiplicity.csv` (`slope_full`) |
| Tables S2, S3 | `R14_weight_sensitivity_decomposition.csv`; `R5_table7_with_pearson_regimes.csv` |
| Tables S4, S5 | `R12_dmca_robustness.csv`; `R11_lower_tail_dependence.csv`, `R26_tail_dependence_gaussian_benchmark.csv` |
| Table S6 | `R13_block_length_sensitivity.csv`, `R24_block_length_sensitivity_M30.csv` |
| Tables S7, S8 | `R34_trimmed_slopes_and_differences.csv` (gap without first bar: `R23_intraday_first_bar_removed.csv`); `R9_…` (proxies), `04_proxy_regression.csv` |
| Tables S14, S15 | `R31_materiality_joint_resampling.csv`; `R35_slope_block_length_M30.csv` |
| Section 5.2 (H1 under weight uncertainty); 5.4 (slope differences); 5.5 (2021) | `R36_like_for_like_gap_weight_uncertainty.csv`; `R34_…`; `R37_crisis_definition_with_2021.csv` |
| Tables S9, S10, S11, S12, S13 | `R28_…`; `R25_…`; `R20_…`; `R27_…`; `R30_slope_channels.csv` |
| Fig. S1 and its text | `outputs/figures/Fig3.eps`; `08_mfdcca_hq.csv`, `R7_mfdcca_shuffle_surrogate.csv` |
| Fig. 1, 2, 3, 4 | `Fig1.eps`, `Fig2.eps` (bands from `R8c_dcca_bootstrap_bands.csv`), `Fig4.eps`, `Fig5.eps` |

Note: the figure file names follow the order in which the scripts create them; the submission folder `03_Figures/` uses the manuscript numbering (Fig3 = `Fig4.eps`, Fig4 = `Fig5.eps`, FigS1 = `Fig3.eps`).

Superseded diagnostics: `run_all.R` still writes `10_table4_forbes_rigobon.csv` (DCCA-scale regime correlations with nominal-N standard errors), `14_portfolio_relative_error.csv` (DCCA-based regime inputs) and `20_scale_regressions_hac.csv` (HAC-over-scales inference). The manuscript does not use them; they were replaced by the Pearson-consistent bootstrap results and the resampling inference above, and they are omitted from `outputs/` in this package.
