# Stage 2.5 Integrity Verification (pre-review): numbers, math, consistency, failure modes

Verifier: integrity_verification_agent (independent; no ledgers, roadmaps or response letters read).
Inputs: `project_R/docx_build/r2/manuscript_with_authors.md`; `project_R/outputs/*.csv`, `scalars.txt/.rds`, `figures/`; `run_all.R`, `run_revision.R`, `run_round2.R`, `R/dcca.R`; data `project/data/vn_indices_merged_filled.csv`.
Scratch recomputations: `/tmp/claude-0/verify/` (nothing in `project_R/outputs/` was touched).

## Verdict: FAIL

The blocking reasons are one implementation bug and two inference or reporting errors:

1. **CRITICAL (Mode 1, implementation bug):** the bootstrap intervals for the nested-minus-purged gap (Table 4 Panel B, Section 5.3, Table 8 H1, Abstract) come from a mis-dimensioned array operation in `run_revision.R`. The point estimates are correct and the "excludes zero" conclusion still holds. The printed intervals are wrong.
2. **MAJOR:** the claim that one slope test survives Holm adjustment rests on a bootstrap p-value of exactly 0 with B = 499. That precision is not attainable at B = 499.
3. **MAJOR:** the abstract and introduction contain degenerate ranges ("0.91–0.91", "0.011–0.011", "0.11–0.11", "9–9 times"), Table 8 misreports H5, and the Table 1 header is missing a column.

Everything else checked (about 400 numeric cells) matches the R outputs after rounding. Proposition 1, Eqs. (8)–(10), (12) and (13), and the extra inequality are correct. The `decomp`/`dcca_multi` code implements them faithfully.

Under the ARS 7-mode rule, Mode 1 is SUSPECTED (confirmed), so the pipeline blocks until the user acknowledges it.

---

## 1. Mismatches

| # | Sev. | Location | Manuscript text | Expected (from R) | Source |
|---|---|---|---|---|---|
| M1 | **CRITICAL** | Table 4 Panel B, "Gap [95% CI]" | 1D [0.065, 0.124]; M30 [0.070, 0.126]; H1 [0.060, 0.116]; H4 [0.061, 0.114] | Correct CIs (same seed and draws, bug fixed): 1D **[0.074, 0.115]**; M30 **[0.080, 0.119]**; H1 **[0.071, 0.103]**; H4 **[0.072, 0.103]** | `R2_bootstrap_dcca.csv` rows `nested_mean-minus-Pcap` are buggy; corrected rerun in `/tmp/claude-0/verify/R2_fixed.csv` (all other R2 cells reproduce exactly, max diff 0) |
| M2 | CRITICAL (follows from M1) | Sec. 5.3 | "bootstrap intervals between 0.060 and 0.126" | "between 0.071 and 0.119" | as M1 |
| M3 | MAJOR (follows from M1) | Table 4 vs Table A5 | 1D gap CI [0.065, 0.124] (L = 20) vs Table A5 L = 20: [0.074, 0.117] | Same estimator and block length, so the two should agree up to Monte Carlo noise. They agree once M1 is fixed ([0.074, 0.115]) | `R13_block_length_sensitivity.csv` |
| M4 | MAJOR | Abstract | "floor alone accounts for 0.91–0.91 of the observed VN30–VN100 coefficient" | 0.905–0.911 (or "about 0.91") | `R8_overlap_decomposition.csv`, `mech_share` |
| M5 | MAJOR | Abstract | "moves the nested coefficient by only about 0.011–0.011" | 0.011 (0.0106–0.0112) | `R8`, `sensitivity` 0.106–0.112 × 0.10 |
| M6 | MAJOR | Introduction, contribution 1 | "accounts for 0.91–0.91 … slope of 0.11–0.11" | 0.905–0.911; 0.106–0.112 | `R8` |
| M7 | MINOR | Sec. 5.4 para 2 | "a change of about 9–9 times as large" | about 9 (1/0.112 = 8.9 to 1/0.106 = 9.4) | `R8`, `sensitivity` |
| M8 | **MAJOR** | Table 8, H5 Evidence | "−1.8% to 9.4%" | −2.1% to 9.4% (the four RE values are 2.23, 9.38, −1.84, −2.07). The Abstract correctly says −2.1% | `R4_portfolio_error_pearson.csv`, Pcap-VN30 rows |
| M9 | MAJOR | Table 6 and Sec. 5.5 | VN100–VNINDEX M30: p "< 0.002", Holm "< 0.002"; "after Holm adjustment 1 remains" | Bootstrap p = 0 out of 499 with p = 2·min(·) only bounds p < 2/499 ≈ 0.004. The Holm-adjusted p is therefore bounded only by 19 × 0.004 ≈ 0.076, which does not establish p_Holm < 0.05. Report "p < 0.004" and either raise B (≥ 9,999 for this cell) or drop the Holm survival claim. The BH count of 4 is unaffected (0.008 × 19/4 = 0.038) | `R9_slope_tests_multiplicity.csv` (p_two_sided = 0, p_holm = 0) |
| M10 | MINOR | Sec. 5.9 last sentence | "0.9670, 0.9660 and 0.9670 for detrending orders 1, 2 and 3" | 0.9665, 0.9663, 0.9667. The manuscript pads a 3-dp rounding with zeros, so the 4-dp values are wrong; m = 1 must equal Table 2's 0.96652 | `scalars.rds$detrend_order_rho` = 0.96651561, 0.96629579, 0.96668132 |
| M11 | MINOR | Sec. 5.1 | "kurtosis above 34 at M30" | P_cap M30 kurtosis = 33.94 (< 34). Use "about 34 or above" or "above 33" | `01_descriptive_stats.csv` |
| M12 | MINOR | Sec. 5.8 | "h(2) lies between 0.536 and 0.543" | Neither source gives this range. Cross-exponent h_xy(2) for the four main pairs: 0.536–0.542 (`08_mfdcca_hq.csv`, q = 2). Single-series h(2): 0.533–0.543 (`09_mfdcca_width.csv`). Choose one definition and state it | `08`, `09` |
| M13 | MINOR | Sec. 5.7 | "For cash portfolios of parent and child indices the misstatement is at most 2.35%" | True for the daily data (max 2.354%, B/VN30-VNINDEX low, `R4`). Across frequencies (`14b_portfolio_nested_all_frequencies.csv`) the maximum is 2.73% (H4 VN30-VNINDEX). Say "at the daily frequency" | `R4`, `14b` |
| M14 | MINOR | Sec. 4.4 | "(499 replications)" presented as the replication count for all inference | Forbes–Rigobon and portfolio-error bootstraps use **1,999** replications (`run_revision.R`, RR2/RR4) | code |
| M15 | MINOR | Sec. 5.5 | Text cites VN100–VNINDEX at H1 as one of the four significant slopes | That cell (0.0019 [0.0007, 0.0032], BH 0.038) appears in no table. Table A1 shows only VN30–VNINDEX and P_cap–VN30 at 1D/H1/H4, so the claim cannot be traced from the tables | `R9` |

### Verified as matching (no action)

- **Table 2**: all 16 rows (N, mean, SD, skewness, kurtosis, JB) match `01_descriptive_stats.csv` after rounding.
- **Table 3**: matches `03_reliability_smax.csv` and `R6_reliability_garch_t.csv` (50/444/233/88; 20/151/86/28). 1,002 sims = 6 × 167; 300 = 6 × 50. "Roughly a factor of three" (2.5–3.1) is acceptable. Heavy-tailed-range averages are 0.975–0.979 nested and 0.882–0.890 purged.
- **Table 4**: Panel A all cells, and Panel B means, P_cap, gap and Cohen's q [CI] all match `02_table2_average_dcca.csv` and `R10_effect_size_cohen_q.csv`. Only the gap CIs are wrong (M1).
- **Sec. 5.3**: 0.975–0.980, 0.883–0.892, 0.086–0.096, q 0.78–0.89, and "differ by at most 0.004" (max 0.0040, H1) all match. The proxy figures (−0.16 to 0.07; 0.980–0.997; 0.277–0.486) match `scalars`, `05`.
- **Sec. 3.2**: sample sizes (1,983 / 19,463 / 9,879 / 3,953; 2,963 / 21,942 / 13,523 / 5,410) and date spans match `02` and `01`. Crisis statistics (26.2%/47%, 33.5%/52%, 40.2%/60%, 539 and 1,000 days, 2025 drawdown 18.1% with 30% high-vol share, quartiles 10.6% and 20.0%) match `11` and `scalars`.
- **Sec. 4.2**: w = 0.6826, the 315%/215% positions, Jensen 3.6 × 10⁻⁶, w_heur 0.9865–0.9885, R² 0.973–0.977, slope 0.968–0.975, 1 − w_heur 0.0115–0.0135, amplification 74–87, and SD 0.1576 vs 0.0124 all match `04`, `05`, `scalars`. The identity error of 4.4 × 10⁻¹⁶ equals max(`identity_error`) in `R8b` (4.440892e-16, at M30).
- **Table 5 and Sec. 5.4**: every point estimate and CI matches `R8`. κ 0.48–0.50, floor 0.893–0.900, share 0.905–0.911 [0.895, 0.920], floor − ρ_AM 0.010–0.016 with all CIs containing 0, and sensitivity 0.106–0.112 all match. The Pearson floor of 0.903 and share of 0.914 match `R8d`. Recomputing Eq. (7) at ρ_AM = −0.5 gives 0.864–0.875, consistent with "about 0.87".
- **Table 6 and Table A1**: every slope, CI, p, Holm and BH value matches `R9`/`R2`. The counts "4 intervals exclude zero, 4 BH, 1 Holm" match the CSV, but see M9 on whether the Holm survival is genuine. "A rise of about 0.01" checks: 0.0022 × ln(444/5) = 0.0099.
- **Table 7 and Sec. 5.6**: matches `R3_forbes_rigobon_pearson_bootstrap.csv` (0.847/0.924/2.21/0.803/−0.044 [−0.082, 0.001]/0.985/0.77; 0.727/0.928/7.06/0.661/−0.066 [−0.132, 0.008]/0.974/0.41; n = 1,000/539 and 739/739).
- **Sec. 5.7**: 2.23 (0.91–3.94), 9.38 (6.20–13.46), −1.84 (0.95–2.63) and −2.07 (1.25–2.84) all match `R4`, and all intervals exclude zero.
- **Sec. 5.8**: Δh 0.252–0.431 nested and 0.435–0.656 P_cap match. The surrogate results (P_cap only at 1D; nested 2 of 12) match `R7`.
- **Table A2**: matches `R5_table7_with_pearson_regimes.csv` (Pearson regime columns) and `07`. Gap ≥ 0.052 holds.
- **Tables A3, A4, A5**: match `R12`, `R11` and `R13` in every cell.

---

## 2. Math check

All results below were derived independently.

- **Eq. (7):** take B = wA + (1−w)M. Profiles and box-wise OLS residuals are linear, so F²_AB = wF_A² + (1−w)ρ_AM F_A F_M and F_B² = w²F_A² + (1−w)²F_M² + 2w(1−w)ρ_AM F_A F_M. Then ρ_AB = F²_AB/(F_A F_B). Divide the numerator by wF_A² to get 1 + κρ_AM. Since F_B/(wF_A) = √(1 + κ² + 2κρ_AM), the result is Eq. (7). **Correct.** The proof sketch says "dividing numerator and denominator by wF_A²". That is loose: the denominator F_A F_B is divided by wF_A², which gives F_B/(wF_A). Harmless.
- **Eq. (8):** ρ_AM = 0 gives 1/√(1+κ²) > 0. **Correct.**
- **Eq. (9):** with D = 1 + κ² + 2κρ, g′ = κD^{-1/2} − κ(1+κρ)D^{-3/2} = κD^{-3/2}(D − 1 − κρ) = κ²(κ+ρ)/D^{3/2}. **Correct.**
- **Inequality:** (1+κρ)² − ρ²D = 1 − ρ² + 2κρ − 2κρ³ = (1−ρ²)(1+2κρ). So ρ²_AB − ρ²_AM = (1−ρ²_AM)(1+2κρ_AM)/D ≥ 0 for ρ_AM ≥ 0. Equality holds iff ρ_AM = 1, where ρ_AB = 1. **Correct.** The inequality actually holds for all ρ_AM > −1/(2κ), so the stated condition is sufficient but conservative.
- **Cauchy–Schwarz bound (Sec. 4.1):** correct. F²_XY and F²_X share the 1/(2N_s s) normalisation over stacked residual vectors.
- **Eq. (10), weight drift:** substituting B = w_tA + (1−w_t)M into (B − wA)/(1−w) reproduces Eq. (10). **Correct.**
- **Eq. (12), Forbes–Rigobon:** this is the standard form ρ* = ρ_h/√(1 + δ(1−ρ_h²)) with δ = σ²_h/σ²_l − 1. The preamble formula ρ = [1 + σ²_ε/(β²σ²_x)]^{-1/2} is also correct. The code (`fr_point` in `run_revision.R`) matches: Pearson ρ, and δ from VN30 variance.
- **Eq. (13):** RE = [pv(ρ_st) − pv(ρ_r)]/pv(ρ_r) with pv = ¼σ₁² + ¼σ₂² + ½σ₁σ₂ρ, which reduces to (ρ_st − ρ_r)/[½(σ₁/σ₂ + σ₂/σ₁) + ρ_r]. `re_point` implements the pv form with regime σ's. **Equivalent.**
- **Eq. (11):** the bootstrap slopes are plain OLS of ρ on ln s (`curve_stats`). **Matches.** HAC (`sandwich`) is used only in `20_scale_regressions_hac.csv` and `07$p_slope`, neither of which is reported.
- **Eq. (14), MF-DCCA:** `q_average(abs_signed = TRUE)` computes mean(|f²|^{q/2})^{1/q}. Δh = λ(−5) − λ(5) over 24 scales, with 100 joint-shuffle surrogates. **Matches.**
- **Code for `dcca_multi` / `decomp` (run_round2.R):** κ = (1−W)F_M/(W F_A), g = (1+κr)/√D, floor = 1/√(1+κ²), share = floor/g, sensitivity = κ²(κ+r)/D^{1.5}. Every quantity uses the same boxes and the same Q basis, so the code is exactly Eqs. (7)–(9). The Table 5 entries are scale-wise averages over s ≤ s_rel, as the note says. **Matches.**
- **Identity error:** max `identity_error` in `R8b` = 4.44 × 10⁻¹⁶ (M30), as stated. Recomputing |rho_implied − rho_nested| from the CSV text gives 1.1 × 10⁻¹⁵, purely from the 15-digit CSV serialisation. The stored column is authoritative.

---

## 3. Cross-reference and consistency issues

| # | Sev. | Issue |
|---|---|---|
| C1 | **MAJOR** | **Table 1 header is missing a column.** The header has 6 columns: Study, Market and data, Method, *Overlap treated?*, *Main finding*, *Limitation for our question*. Every row carries Overlap, then a second Yes/No/Partly value (volatility conditioning, which the table note defines), then the finding. As a result the "Main finding" column shows Yes/No values, the "Limitation" column shows the main findings, and no limitation text exists. Rename the headers to: Overlap treated? / Volatility conditioning? / Main finding, or add the missing column. |
| C2 | MAJOR | **"Pinned to the floor" wording conflicts with the paper's own numbers.** Sec. 5.5 says "the coefficient is held near its floor", Sec. 5.7 says "pinned near the mechanical floor in every regime", and Sec. 6.1 says "it is pinned to its floor". Yet ρ_AB ≈ 0.988 and the floor is ≈ 0.90, a gap of about 0.09 (Table 5). Proposition 1 implies insensitivity (slope ≈ 0.11) and a lower bound, not proximity to the floor. Reword to "bounded below by the floor and insensitive to ρ_AM". |
| C3 | MINOR | Sec. 5.6 says "H4 is rejected"; Table 8 says "Not supported". Use one term (H4 is a hypothesis of contagion; "not supported" is the precise wording). |
| C4 | MINOR | Table 4 Panel A (N = 1,983 etc.) averages over s ≤ s_rel taken from Table 3, but Table 3 was calibrated at the full-sample N (2,963 etc.). Sec. 4.4 says thresholds are simulated "for each sample size". Either calibrate the Panel A sizes or say the full-sample thresholds are reused. |
| C5 | MINOR | The Table A2 column "Slope (M30)" is the **full-range** slope (`07`, baseline 0.0025 = Table 6 full range). The note does not say which range. |
| C6 | MINOR | The Fig. 3 note says "dashed horizontal line". The code uses `longdash` and also draws an unmentioned vertical line at ρ_AM = 0. Cosmetic. |
| C7 | PASS | Every Table (1–8, A1–A5), Figure (1–4), Equation (1–14) and Section cross-reference resolves to existing content that says what the text claims. Every table and figure is cited in the text before it appears. Equations are numbered sequentially. Figure files are correctly remapped (manuscript Fig. 3 = `fig4_overlap_decomposition`, Fig. 4 = `fig3_mfdcca`, in both `build_r2.py` FIGMAP and `build_r2_package.py` FIGS). |
| C8 | PASS | Every table and figure note has at most 3 sentences (Tables 4–7 reach exactly 3). |
| C9 | PASS with M9 | Section 5.5 counts against `R9_slope_tests_multiplicity.csv`: family size 19 (1D 4 + M30 7 + H1 4 + H4 4), adjusted within each range (`stat`), 4 CIs exclude zero, 4 BH < 0.05, 1 Holm < 0.05. All agree with the CSV. The Holm survival is an artefact of p = 0 (M9). |
| C10 | Mostly PASS | Table 8 decisions. H1: supported (CIs exclude 0, before and after the M1 fix). H2: supported (lower CI 0.895 > 0.5; one-sided p = 0). H3: partially supported (consistent; see M9). H4: not supported (p 0.985/0.974). H5: supported (CIs exclude 0), but the Evidence cell is wrong (M8). |

---

## 4. AI research failure-mode checklist (7 modes)

| Mode | Status | Evidence |
|---|---|---|
| 1. Implementation bugs | **SUSPECTED (confirmed)** | `run_revision.R` line ~69: `nested <- colMeans(bs["avg_rel", 1:3, , drop = FALSE])` on a 1 × 3 × B array returns a **3 × B matrix** (per-pair averages, not their mean). `gap <- nested - bs["avg_rel", 4, ]` then recycles a length-B vector over 3B cells in column-major order, which subtracts P_cap values from the *wrong replicates*. The quantiles are taken over 3B mixed values. The inflated SE (0.0152 vs a correct 0.0104 at 1D) and the clash with Table A5 confirm it. I re-ran the R2 block with the one-line fix `colMeans(bs["avg_rel", 1:3, ])` and the same seed. All other R2 cells reproduce to 0 difference, and the gap CIs become 1D [0.074, 0.115], M30 [0.080, 0.119], H1 [0.071, 0.103], H4 [0.072, 0.103]. The sign of the conclusion is unchanged. The other bootstraps (`R8`, R10 Cohen's q, `R8c` bands, R11–R13) index correctly. |
| 2. Hallucinated results | PASS | Every number in the abstract, text and tables traces to an R output cell. The deviations listed are rounding, range or typing errors, not invented values. |
| 3. Shortcut reliance | PASS | Inference resamples the joint return series and recomputes full curves. No scale-as-independent-observation shortcut appears in reported results (HAC-over-scales output exists but is not reported). One weak spot: bootstrap p-value resolution with B = 499 (M9). |
| 4. Bug-as-insight | PASS | The buggy gap CI is not interpreted as a finding. Only "excludes zero" is used, and that survives the fix. |
| 5. Methodology fabrication | PASS (minor gaps) | Every Section 4 method is implemented: reliability thresholds (`reliable_smax`, 6 × 167, 40 scales, 0.05 rule as stated); GARCH(1,1)-t(5) calibration (`garch_t_pair`, 6 × 50 = 300); stationary block bootstrap (`sb_index`, mean ~20 trading days via `LBLOCK`); Holm/BH (`p.adjust`); Cohen's q; Forbes–Rigobon with within-regime bootstrap, one-sided p and power; Eq. (13) RE; DMCA (`dmca_rho`, centred MA, odd windows); lower-tail dependence (`tail_dep` + bootstrap); MF-DCCA with 100 joint-shuffle surrogates; Pearson special case (`R8d`); weight grid; detrending orders 1–3; filled-file check (`R1`: index columns identical to the raw inner join, so "no index level is filled" holds). Gaps: the replication count is mis-stated (M14). "Error grid and 0.05 tolerance fixed before the empirical analysis" and "weight fixed before any estimation" are process claims the code cannot verify (unverifiable, not contradicted). |
| 6. Frame-lock | PASS (note) | The decomposition is an algebraic identity once M is defined residually as (B − wA)/(1 − w), so it holds for any w. Its empirical content therefore rests on the proxy's validity. The paper acknowledges this (Secs. 4.3, 6.3, Table A2) and adds DMCA, Pearson, tail and weight robustness checks. The floor counterfactual ("if mid caps were uncorrelated") holds F_M fixed. This is implicit and could be stated. |
| 7. Overclaiming | SUSPECTED (minor) | Two instances: "pinned to / held near the floor" (C2), and "1 Holm-significant" (M9). Other claims are appropriately hedged: H3 partial, H4 power stated, one market, ex-post regimes, P_cap not investable. |

**Seeds and byte-identical reruns.**
- `run_revision.R` uses `set.seed(20260924)` and `run_round2.R` uses `set.seed(20261007)`.
- The white-noise calibration seeds each simulation by its index (`seed + 1000(i−1) + (r−1)`).
- `run_all.R` sets no seed, but it uses no unseeded RNG.
- My rerun of the R2 block reproduced `R2_bootstrap_dcca.csv` exactly, so CSV reproducibility is plausible.
- **However**, all four EPS files carry a `%%CreationDate:` header written by cairo. "Rerunning it yields byte-identical output files" is therefore false for the EPS figures (MINOR). Restrict the claim to the CSV/tables or strip the timestamps.

---

## 5. Other observations

- O1 (MINOR): the minimum attainable two-sided bootstrap p is 2/499 ≈ 0.004. Report bootstrap p = 0 as "< 0.004", not "< 0.002" (Table 6, both rows).
- O2 (MINOR): mtimes of `fig1_volatility_regimes.png` and `fig3_mfdcca.png` (02:25) predate every CSV and the matching EPS files (02:34–02:37). `run_all.R` writes each PNG and EPS back-to-back, so the embedded PNGs for manuscript Figs. 1 and 4 may not come from the final run. I cannot confirm this from metadata alone. Re-run `run_all.R` once and rebuild the docx before submission.
- O3 (MINOR): obsolete outputs remain in `outputs/` and would ship in Online Resource 1. These are `10_table4_forbes_rigobon.csv` (DCCA-at-s = 20 Forbes–Rigobon: quartile ρ_low 0.633, p = 0.165), `14_portfolio_relative_error.csv` (RE_low 15.6%) and `20_scale_regressions_hac.csv` (HAC p-values). They contradict the reported Pearson-based Table 7 and Sec. 5.7 and could confuse a referee. Delete them or label them superseded.
- O4 (MINOR): the `run_all.R` header still carries the old title ("Nested Equity Index Correlations Overstate True Co-Movement").
- O5 (MINOR): lower-tail dependence bootstrap CIs are strongly asymmetric around the point estimates (e.g. 0.904 [0.874, 0.958]). Block resampling duplicates joint-tail days, which biases the percentile CI upward. Consider a bias-corrected interval or say so in the note.
- O6 (MINOR): the stationary bootstrap in the chronological Forbes–Rigobon regimes wraps blocks across non-contiguous episodes (2016–17 with 2023–24; 2018/2020/2022). This is acceptable but worth one clause.
- O7 (INFO): Sec. 4.9 software claims (R 4.3.3, sandwich 3.1.0, ggplot2 3.4.4, Xeon 2.10 GHz, 4 cores) match `R_session_info.txt` and the installed `sandwich` 3.1.0.

## Required fixes before Stage 3

1. Fix `run_revision.R` (`nested <- colMeans(bs["avg_rel", 1:3, ])`), re-run, and update Table 4 Panel B CIs, Sec. 5.3 ("0.071 and 0.119") and anything that quotes them.
2. Replace the degenerate ranges in the Abstract, Introduction and Sec. 5.4 (M4–M7).
3. Correct the Table 8 H5 Evidence cell to "−2.1% to 9.4%".
4. Resolve the Holm claim (M9): raise B for the slope bootstrap, or report p < 0.004 and drop "1 Holm-significant" from Sec. 5.5 and Table 8.
5. Repair the Table 1 header (C1) and the "pinned to the floor" wording (C2).
6. Make the MINOR corrections: M10–M15, C3–C5, the byte-identical claim, and O1–O4.
