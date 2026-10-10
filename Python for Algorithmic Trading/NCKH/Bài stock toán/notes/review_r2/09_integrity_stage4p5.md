# Stage 4.5 FINAL INTEGRITY — Independent verification report (mode: final-check)

- Agent: integrity_verification_agent (ARS academic-pipeline v3.22.1, Mode 2), fresh context; AUDIT_LEDGER not read.
- Inputs: project_R/docx_build/r2/manuscript_anonymized.md; supplementary_material.md; project_R/outputs/*.csv; R scripts; notes/review_r2/08_citation_audit_v3.md; notes/review_r2/response_to_reviewers.md.
- Date: 2026-10-10. No manuscript or code file was edited.
- Status: COMPLETE. Verdict: FAIL (0 CRITICAL, 2 MAJOR, 16 MINOR) — see Section 8.

## 1. Phase C — Numbers in the main text against R outputs

Method: every number below was read from the CSV named and rounded by hand (half-up at the shown precision). "OK" = exact match after rounding. Denominators are stated per block.

### 1.1 Abstract and Introduction (12 numbers; 12 OK)
| Claim | Source | Status |
|---|---|---|
| "about 0.11 per unit change" | R8 sensitivity 0.1060–0.1118 | OK |
| "lowers ... by about 0.10 at every frequency" | R15 gap_like 0.0987–0.1040 | OK |
| 0.988 daily VN30–VN100 | R33 rho_AB 0.98848 (Pearson); 02 avg 0.98764 | OK |
| "about two-thirds" | w = 1,316,288/1,928,303 = 0.68261 | OK |
| slope 0.106–0.112; gap 0.099–0.104; κ 0.47–0.52 | R8; R15; R8b reliable rows: κ min 0.4736 (1D), max 0.5249 (M30) | OK |
| 2014–2025, 30-min to daily | 01 first/last dates | OK |

### 1.2 Sections 3–4 (22 numbers; 21 OK, 1 flagged)
| Claim | Source | Status |
|---|---|---|
| Synchronized N 1,983 / 19,463 / 9,879 / 3,953 | 02 Panel A n | OK |
| Full N 2,963 / 21,942 / 13,523 / 5,410; dates | 01 | OK |
| Episodes 26.2%/47%, 33.5%/52%, 40.2%/60%; 539 days; calm 1,000 | 11 (0.4659, 0.5207, 0.5976); scalars n_crisis 539, n_calm 1000; 249+121+169 = 539 | OK |
| 2021 14.3%/32%; 2025 18.1%/30% | R27 | OK |
| quartiles 10.6% / 20.0% | scalars vol_quartiles_ann_pct | OK |
| w = 0.6826; Jensen 3.6×10⁻⁶; 315% / 215% | W; scalars 3.63e-6; 1/(1−w) = 3.150, w/(1−w) = 2.150 | OK |
| identity error 4.4×10⁻¹⁶ | R8b max \|identity_error\| = 4.44e-16 (M30) | OK |
| √3·w/(1−w) = 3.73 | R33 amplitude_ratio_max 3.7252 | OK |
| 167 × 6 = 1,002; 300 GARCH sims | run_all.R n_repeats = 167; run_revision.R smax_garch reps = 50 × 6 ρ₀ | OK |
| p ≥ 0.004 at B = 499; Holm floor 0.076 with 19 tests | 2/500; 19 × 0.004 | OK |
| TOST margin 0.001 × 4.5 = 0.0045 < 0.005 | ln(444/5) = 4.49 | OK |
| "499 replications for DCCA statistics" (Sec. 4.4) | R34/R35 used B = 199 (run_round3e.R default; Supplement notes to Tables S7 and S15 say 199); R36 used 2B+1 = 399 | **FLAG (see issue M1)** |
| Seeds "20260924 to 20261013" (Sec. 4.8) | run_round3e.R uses set.seed(20261014); run_all.R reliability sims use seed = 42 + offsets | **FLAG (see issue M2)** |

### 1.3 Box 1 (11 numbers; 11 OK) — R33_practitioner_recipe.csv
w 0.6826; σ_A 0.01213 → 0.0121; σ_B 0.01191 → 0.0119; ρ_AB 0.98848 → 0.9885; σ_M 0.01238 → 0.0124 (= sd of direct P_cap, 0.0123840 both); κ 0.47466 → 0.475; ρ̲ 0.90340 → 0.903; bound 0.88017 → 0.880; ρ_AM 0.88858 → 0.889 (= direct 0.888580); sensitivity 0.10322 → 0.103; inverse 9.688 → 9.7. Formulas of Steps 2, 3, 5 re-derived from M = (B − wA)/(1 − w): Var(M) = (σ_B² − 2wρσ_Aσ_B + w²σ_A²)/(1 − w)², Cov(A,M) = (ρσ_Aσ_B − wσ_A²)/(1 − w). Correct. "Steps 2 and 5 reproduce ... exactly": confirmed (R33 sd_M = sd_Pcap_direct; rho_AM = rho_AM_direct to 1e-15).

### 1.4 Table 2 (16 rows × 7 numbers = 112; 112 OK) — 01_descriptive_stats.csv
All N, means (4 dp), SDs, skewness, kurtosis and JB statistics match. Rounding edge cases checked: VN100 M30 mean 4.91e-5 → 0.0000; VN30 M30 5.04e-5 → 0.0001; P_cap H1 8.03e-5 → 0.0001. Text: P_cap highest daily SD 0.0124, VNINDEX lowest 0.0115; kurtosis > 33 at M30 (min 33.94): OK.

### 1.5 Table 3 and Sec. 5.1 text (14 numbers; 14 OK) — 03_reliability_smax.csv, R6
50/444/233/88 and 20/151/86/28; "factor of three" (2.5–3.1); heavy-tailed nested 0.975–0.979 (R6 0.97486–0.97854), purged 0.882–0.890 (0.88249–0.88994). OK.

### 1.6 Table 4 and Sec. 5.2 (60 numbers; 60 OK) — 02, R2, R10, R15, R36, R14, 07
Panel A and B means and gaps match 02; three-pair gap CIs match R2 (`nested_mean-minus-Pcap`, 1D [0.0742, 0.1147], M30 [0.0801, 0.1193]; H1/H4 rows in R2 likewise); like-for-like CIs match R15 gap_like; Cohen's q matches R10. Text ranges: nested 0.975–0.980 (min H1 B 0.97549, max H4 A 0.98025), purged 0.883–0.892, like-for-like 0.099–0.104 with lower CI ≥ 0.084 (min 0.08398 H4), three-pair 0.086–0.096, q 0.78–0.89. Weight grid: like-for-like 0.063–0.164 (0.98764 − R14 rho_econ at w = 0.60/0.75), three-pair 0.052–0.153 (07 gap_vs_nested). Weight-drawn gap: lower 0.057–0.061, upper 0.155–0.168, share_above_0.05 = 1 at all four frequencies (R36). OK.

### 1.7 Table 5 and Sec. 5.3 (72 cells + 24 text numbers; all OK, 1 traceability note)
Panel A: κ, ρ_AM [CI], ρ̲ [CI], sensitivity [CI], benchmark-first share from R8_overlap_decomposition.csv; ρ_AB from 02; bound √(1−κ²) = R16 true_min (0.8751, 0.8644, 0.8737, 0.8745); Shapley share [CI] from R15. Panel B from R21 (1D, M30). All 4 × 9 + 2 × 5 cells match.
Text: sensitivity 0.106–0.112, 0.01/0.106–0.112 = 0.089–0.094 ("about 0.09"); weight-uncertainty interval 0.07–0.17 (R21 0.0712–0.1682); κ 0.48–0.50 (0.4839–0.5027); benchmark 0.893–0.900; bound 0.864–0.875; benchmark-first 0.905–0.911; dependence-first 0.895–0.900 (R15 econ_share 0.8946–0.9002); Shapley 0.505–0.508, intervals within 0.497–0.521; weight-uncertainty Shapley 0.45–0.56 and benchmark-first 0.83–0.95; per-scale κ 0.47–0.52 (R8b reliable rows 0.4736–0.5249); benchmark range within frequency 0.007–0.016 (R15 floor_range 0.0068–0.0159); floor-slope p 0.052–0.456, Holm 0.208–0.828 (R15); M30 floor-slope CI [−0.00452, −0.0000171] excludes zero while p = 0.052 — consistent with the percentile-inversion rule (k₊ ≤ 12/499); slope ≈ 0.002 (−0.0025). Fig. 4 point: w 0.683, σ_M/σ_A 1.02, benchmark 0.903 (R17). Equal-volatility w = 0.5 benchmark 1/√2 = 0.707 ("about 0.7"). OK.
Pearson version: "benchmark of 0.898–0.903 and benchmark-first share of 0.911–0.914 across frequencies" = R8d_overlap_decomposition_pearson.csv (floor 0.8983–0.9034, mech_share 0.9106–0.9141, all four frequencies); I also recomputed them independently from 01 sds and 14b correlations (identical). "Within 0.01 of the DCCA values": max difference 0.0048 (M30 benchmark). OK.

### 1.8 Table 6 and Sec. 5.4 (16 rows × 7 = 112 numbers + 30 text numbers; all OK)
Slopes/CIs/p_boot from R2/R9; studentized p, Holm (19 tests), Holm (H2 family), TOST from R22. Every cell matches, including "< 0.005" (p_boot 0.004) and "< 0.001" (p_stud 1.07e-4, Holm-H2 8.5e-4).
Text: four H2-family survivors (Holm-H2 0.039, 0.039, <0.001, 0.045) with estimates 0.0019–0.0024; Holm over 19 keeps one (0.002), BH keeps four (0.002, 0.0375, 0.0375, 0.0427); smallest percentile BH = 0.057; TOST 0.007 and 0.012; P_cap slopes all insignificant. Damping 0.106–0.112; max |implied − observed| = 8.4e-6 (M30) → "0.8 × 10⁻⁵" OK. First-bar share 10.2% of bars, 36.8% of squared VN30 returns (R23). H1 drop-first slopes 0.0003/−0.0005; M30 drop-first 0.0020 (p 0.031) and 0.0010 (p 0.156); drop-both −0.00002/−0.0002; trimmed gap 0.107 [0.094, 0.127] (R23); differences 0.0018–0.0024 with studentized p ≤ 0.0029 (R34). OK.
Claim check: "the κ channel partly offsets the ρ_AM channel" — true at M30 and H1 only. At 1D (channel_rho −0.00042, channel_kappa −0.00035) and H4 (−0.00022, −0.00015) the two channels have the same sign (R30). MINOR wording issue (m4).

### 1.9 Table 7 and Sec. 5.5 (27 cells + 20 text numbers; all OK)
Chronological and VNINDEX-quartile FR columns from R3 (Pcap-VN30 rows A, B); VN30-quartile FR column from R25 (w = factsheet, VN30_quartiles); β, Δβ, residual-variance ratio from R29 (panels A, B, C). All match. Day counts 1,000/539 and 739/739 match. Text: FR p 0.974–0.998; weight-grid minimum p 0.93493 → "no one-sided p falls below 0.935" (rounded; strictly 0.9349 < 0.935 — trivial, m5); −0.087 [−0.144, −0.018]; 2.70 [1.92, 3.68], 2.57; β 0.737 → 0.948, Δβ 0.210 [0.119, 0.306]; chronological Δβ 0.008 [−0.128, 0.140]; tail dependence 0.75 vs 0.62 (R26); 2021 variant 789 days, FR p 0.987, Δβ −0.005 [−0.122, 0.124] (R37). OK.

### 1.10 Table 8 and Sec. 5.6 (8 × 4 + 4 × 5 = 52 cells + 14 text numbers; all OK)
Panel A from R31 (RE_pct, joint CI, regime_var_rel_se_pct, RE_over_se); Panel B from R18 (mean_qlike; DM t and p). All match. Static QLIKE is the lowest of the three for all four pairs; all DM t < 0; p 0.069–0.179. Nested |RE| ≤ 2.354% and RE/SE ≤ 0.430 (R31 daily); P_cap RE/SE 0.13–1.50. OK. (14b shows nested intraday |RE| up to 2.73% at H4, but the text cites daily Table S14 only, so the statement is correct as scoped.)

### 1.11 Table 9 (all numbers repeat Tables 4–8; all OK). Section 6 numbers: lead 0.084 [0.028, 0.136], reverse 0.007, asymmetry 0.076 [0.048, 0.102] (R28); hedge 0.79 [0.75, 0.82], 0.53 [0.45, 0.61], 0.86 (R20); "a fifth" (1 − 0.790 = 0.21), "about half" (1 − 0.528 = 0.47); benchmark ≈ 0.90, bound ≈ 0.87, 68%. OK. Sec. 5.7: DMCA 0.882–0.891 and 0.086–0.096 (R12); block-length 0.070–0.119 (R13); detrending orders 0.9665/0.9663/0.9667 (scalars 0.966516, 0.966296, 0.966681); proxy weight 0.9865–0.9885 (static correlations M30 0.98649, 1D 0.98848). OK.

### 1.12 Supplement (≥ 40 required; 452 numbers checked; 451 OK)
- Table S1 (64 numbers) vs R9 slope_full: all OK.
- Table S2 (70) vs R14: all OK. Header "Pearson ρ̲ (1D)" is wrong for the M30 rows, which show the M30 Pearson benchmark (0.827, 0.873, 0.898, 0.922, 0.938 = R14 M30 pearson_floor). MINOR m6.
- Table S3 (25) vs R5/07: OK. Table S4 (20) vs R12: OK. Table S5 (40, incl. computed "Excess") vs R11/R26: OK.
- Table S6 (21) vs R13/R24: OK. Table S7 (120) vs R34: OK. Table S8 (9) vs R9: OK. Table S9 (21) vs R28: OK.
- Table S10 (60) vs R25: OK. Table S11 (15) vs R20: OK. Table S12 (10) vs R27: OK. Table S13 (28) vs R30: OK. Table S14 (64) vs R31: OK. Table S15 (32) vs R35: OK.
- MF-DCCA paragraph: h_xy(2) 0.526–0.542 (08, all 7 pairs); Δh nested 0.252–0.431, P_cap 0.435–0.656; exceedances 1D only for P_cap and 2/12 for nested pairs (R7). OK.
- Cross-table note: Table S7 "All bars" rows reproduce Table 6 point estimates but have different CIs and studentized p (e.g. M30 VN30–VNINDEX 0.006 vs 0.009; H1 VN30–VNINDEX 0.009 vs 0.006) because R34 is a separate 199-replicate bootstrap. S6 and S10 carry a "separate draws" note; S7 does not. MINOR m7.

**Phase C tally.** Main text: about 560 numbers checked; supplement: 452. Untraceable numbers: 0. Rounding errors: 0. Range errors: 0. Methods-description mismatches: 2 (bootstrap counts; seed range), see issues M1 and m1.

## 2. Phase E — Verbal claims and Table 9 against the decision rules (Sec. 2.7)

### 2.1 Mechanical evaluation of Table 9
| Item | Decision rule (Sec. 2.7) | Evidence in outputs | Rule outcome | Table 9 | Match |
|---|---|---|---|---|---|
| H1 | lower 95% CI of like-for-like gap > 0.05 at every frequency | R15 gap_like ci_lo 0.0846 / 0.0874 / 0.0842 / 0.0840 | Supported | Supported | YES |
| H1 (weight-drawn) | same, with w ~ U(0.60, 0.75) | R36 ci_lo 0.0615 / 0.0605 / 0.0588 / 0.0567 | Supported | "Holds under weight uncertainty" | YES |
| H2 | ≥ 1 broad-market pair with positive slope and Holm-H2 studentized p < 0.05 at M30 AND at H1 | R22 p_stud_holm_h3: M30 0.045 (VN30–VNINDEX), 0.00085 (VN100–VNINDEX); H1 0.039, 0.039; all slopes positive | Supported | Supported, "Not robust: vanishes without the auction bars" | YES |
| H3 | VN30 regimes: FR one-sided p < 0.05 AND Δβ two-sided p < 0.05 | R25 p = 0.998 (fails); R29 C p_d_beta = 1.2e-5 (passes) | Not supported (conjunction fails) | Not supported | YES |
| H4 | EWMA or regime QLIKE < static with DM p < 0.05 | R18: static has lowest QLIKE in 4/4 pairs; all DM t < 0; min p 0.069 | Not supported | Not supported | YES |
| E1–E3 | estimands, no test | R8/R15/R21/R31 | – | "Estimated (not a test)" | YES |

### 2.2 Verbal claims
| Claim (location) | Evidence | Verdict |
|---|---|---|
| "every replicate exceeds 0.05" (Sec. 5.2) | R36 share_above_0.05 = 1 at all four frequencies (399 replicates each, see M1) | VERIFIED |
| "within 0.01 of the DCCA values" (Sec. 5.3) | R8d vs R8: max \|Δ\| 0.0048 (benchmark), 0.0053 (share, M30) | VERIFIED |
| "the differences vanish when the auction bars are removed" (Sec. 5.4); "vanishes without the auction bars" (Table 9) | R34 drop_first_last: differences 0.00015 (p 0.87), −0.00003 (0.96) at M30; −0.0015 (0.36), −0.0016 (0.19) at H1; slopes −0.00002 to −0.0022, all p > 0.12 | VERIFIED. Note: with only the opening bar removed, VN30–VNINDEX at M30 survives (p 0.031) and its difference too (p 0.012); the text says so. |
| "leaves both results unchanged" (2021 added, Sec. 5.5) | R37: FR p 0.987 (no contagion), Δβ −0.005 [−0.122, 0.124] (no change) | VERIFIED as a statement about conclusions (the FR CI now excludes zero from below, which strengthens the no-contagion reading). |
| "none changes the conclusions" (Sec. 5.7) | S1, S4, S6, S8, S15, MF-DCCA | VERIFIED |
| "the static correlation has the lowest mean QLIKE for every pair" | R18 | VERIFIED |
| "Only the calm-quartile overstatement for P_cap–VN30 exceeds one standard error" | R31 RE_over_se: only 1.499 > 1 | VERIFIED |
| "κ lies between 0.47 and 0.52 across all reliable scales and frequencies" | R8b reliable rows 0.4736–0.5249 | VERIFIED (over all 30 scales, including unreliable ones, κ is 0.434–0.571; the manuscript correctly says "reliable") |
| "the κ channel partly offsets the ρ_AM channel" (Sec. 5.4) | R30: opposite signs at M30, H1; same sign at 1D, H4 | PARTLY TRUE → m4 |
| "Intraday the lead is symmetric" | R28 asymmetry CIs contain 0 at M30, H1 | VERIFIED |
| "Steps 2 and 5 reproduce ... exactly" (Box 1) | R33 sd_M = sd_Pcap_direct; rho_AM = rho_AM_direct | VERIFIED |
| "rerunning it yields byte-identical CSV output files" (Sec. 4.8) | Not re-run in this check (run time); seeds are set in every script | INSUFFICIENT EVIDENCE (not an issue; advisory) |
| "no index level is filled or interpolated" (Sec. 3.2) although the input file is `vn_indices_merged_filled.csv` | R1_filled_file_check: same rows, index columns identical; only USDVND (unused) was forward-filled | VERIFIED |

## 3. Mathematics and code

### 3.1 Derivations (re-done by hand)
- **Lemma 1 / Eq. (7).** With B = wA + (1−w)M, profiles (demeaned cumulative sums) and box-wise OLS residuals are linear, so ε_B = wε_A + (1−w)ε_M. Bilinearity of Eq. (4): F²_AB = wF_A² + (1−w)ρ_AM F_A F_M and F_B² = w²F_A² + (1−w)²F_M² + 2w(1−w)ρ_AM F_A F_M. Dividing numerator and denominator of F²_AB/(F_A F_B) by wF_A² gives (1 + κρ)/√(1 + κ² + 2κρ) with κ = (1−w)F_M/(wF_A). CORRECT. Numerically: R8b identity_error ≤ 4.4e-16 at every scale and frequency.
- **Corollary 1.** ρ_AM = 0 ⇒ (1+κ²)^(−1/2). Monotone increasing for ρ_AM > −κ (sign of Eq. 10 numerator). For κ < 1 the minimum over [−1, 1] is at ρ_AM = −κ: (1−κ²)/√(1−κ²) = √(1−κ²). For κ > 1, ρ_AM = −1 gives (1−κ)/\|1−κ\| = −1; no positive bound. CORRECT. R16 true_min = √(1 − κ_from_floor²) matches Table 5.
- **Corollary 2 / Eq. (10).** g' = κD^(−1/2) − κ(1+κρ)D^(−3/2) = κ(κ² + κρ)D^(−3/2) = κ²(κ+ρ)/D^(3/2). CORRECT; R33 sensitivity 0.10322 recomputed from κ = 0.47466, ρ = 0.88858.
- **Corollary 3.** (1+κρ)² − ρ²(1+κ²+2κρ) = 1 + 2κρ − ρ² − 2κρ³ = (1−ρ²)(1+2κρ). CORRECT.
- **Corollary 4.** ρ_AB ≤ 1 ⇒ ρ̲/ρ_AB ≥ ρ̲ > 1/2 ⇔ κ < √3; F_M/F_A < √3·w/(1−w) = 3.725. CORRECT.
- **Corollary 5 / Eq. (11).** Two orderings give (ρ̲, ρ_AB − ρ̲) and (ρ_AB − ρ_AM, ρ_AM); averages sum to ρ_AB. CORRECT; 1D check ½(0.90015 + 0.98764 − 0.88368) = 0.50206 = R15 shapley_overlap.
- **Eq. (14).** ∂g/∂κ = ρD^(−1/2) − (1+κρ)(κ+ρ)D^(−3/2) = D^(−3/2)[κρ² − κ] = −κ(1−ρ²)/D^(3/2). CORRECT; R30 dg_dkappa (−0.0351 at 1D) reproduced.
- **Eq. (12), (15), (16), Sec. 4.6 ρ formula.** Re-derived; correct. Eq. (16): RE = 2σ₁σ₂(ρ_st − ρ_r)/(σ₁² + σ₂² + 2ρ_rσ₁σ₂), equal to the printed form.
- **Box 1.** Var(M) and Cov(A, M) follow from M = (B − wA)/(1−w); formulas correct (see 1.3).
- **Sec. 4.1** \|ρ\| ≤ 1 by Cauchy–Schwarz on stacked residual vectors: correct for the code, which averages box products with equal box length s (R/dcca.R `mean(lf$fxy)`, `sqrt(mean(lf$fxx))`).

### 3.2 Code does what the text says
| Item | Code | Verdict |
|---|---|---|
| DCCA definition (Eqs. 3–5) | R/dcca.R: `cumsum(x − mean(x))`, 2⌊N/s⌋ boxes forward + backward, QR-projection detrending of order m, ρ = mean(f_xy)/√(mean f_xx · mean f_yy) | MATCHES |
| R34 first/last-bar trimming | run_round3e.R `load_tf`: return i is `first_bar` when date(price i+1) ≠ date(price i) (overnight + opening auction); `last_bar` when date(price i+2) ≠ date(price i+1) (bar opening 14:30, closing auction; last return TRUE). Returns are computed on the full series before rows are dropped, so no artificial cross-gap return is created. Block length re-set to 20 × median bars/day of the trimmed sample. | MATCHES. Note: trimmed samples reuse the full-sample s_rel (444 at M30, 233 at H1) although N falls to 17,475 / 8,112; not stated (m9). |
| R34 slope differences "within the same replicates" | `dif_bs <- bs[1:2,] − bs[3,]` from the same `replicate` call | MATCHES |
| R36 weight draw | per replicate: block-resampled index i, `w <- runif(1, 0.60, 0.75)`, M recomputed from resampled VN30/VN100 with that w, gap = mean ρ(A,B) − mean ρ(A,M) over s ≤ s_rel | MATCHES Sec. 4.3; B = 2·199+1 = 399 (see M1) |
| R21 weight draw (Table 5 Panel B) | same scheme, B = 499, all five quantities recomputed per replicate | MATCHES |
| R29 factor test | OLS P_cap on VN30 in each regime; low and high regimes block-resampled independently (block 20); Δβ p = 2Φ(−\|Δβ̂\|/se_boot); variance ratio CI by exp of log-ratio percentiles; B = 999 | MATCHES Sec. 4.6 and Table 7 ("two-sided p"). Note: within-regime blocks of the chronological regime can join non-contiguous episodes (standard, not stated). |
| R31 joint resampling | full daily sample block-resampled (block 20); regime labels travel with the rows; ρ_st recomputed in each replicate; regime-variance relative SE from a within-regime bootstrap; B = 999 | MATCHES Sec. 4.7 |
| R18 OOS design | estimation < 2023-01-01 (n = 2,228), evaluation 735 days; RiskMetrics λ = 0.94 one-step-ahead (uses x_{t−1}); EWMA correlation from the same recursion; regime labels from the 20-day rolling VNINDEX SD lagged to t−1, thresholds = estimation-window quartiles; regime correlations estimated in the estimation window; QLIKE = log h + r²/h; DM with Newey–West, 5 lags, no prewhitening | MATCHES Sec. 4.7; no look-ahead found |
| R25 FR under VN30 quartiles | p = share of re-centred bootstrap differences ≥ observed difference (one-sided), B = 999 | Works, but this is a re-centred convention, not the percentile-inversion rule that Sec. 4.4 states for "bootstrap p-values" (m8); and B = 999, not 1,999 (M1) |
| Input data | `vn_indices_merged_filled.csv`: R1 shows index columns identical to the raw inner join | MATCHES Sec. 3.2 |

## 4. AI research failure-mode checklist (7 modes)
| Mode | Status | Evidence |
|---|---|---|
| 1 Implementation bug passing self-review | CLEAR | Identity reproduced to 4.4e-16; Box 1 closed-form = directly constructed series; Eq. (14) linearization reproduces observed slopes to 8.4e-6; trimming, weight-draw, joint-resampling and OOS code read line by line (Sec. 3.2) with no defect; no suspiciously round or constant numbers; CIs differ across conditions. |
| 2 Hallucinated citation | CLEAR | 67/67 list entries cited in text and vice versa (scripted cross-match); two new references verified to exist (Sec. 5); earlier fixes confirmed applied. Two MINOR form corrections remain. |
| 3 Hallucinated experimental result | CLEAR | ~1,000 numbers traced to CSVs, zero untraceable, zero mismatches. |
| 4 Shortcut reliance | CLEAR | The main horizon result was stress-tested against its obvious artefact (auction bars) and the paper reports that it vanishes; weight-error, block-length, detrending-order, heavy-tail and DMCA checks reported. |
| 5 Bug reframed as insight | CLEAR | No "surprising/unexpected" framing (grep: 0 hits). The one notable pattern (flat nested slope) is explained analytically by Eq. (14) and verified numerically. |
| 6 Methodology fabrication | SUSPECTED (minor, text-level) | Sec. 4.4 states bootstrap replication counts that do not match what the code ran for R34/R35 (199), R36 (399), R25/R37 (999) and R20/R11 (499); Sec. 4.8 seed range omits 20261014 and run_all.R's reliability seeds. The procedures themselves were run as described; only the stated counts/seeds are wrong. Resolved by the text fixes in M1/m1. |
| 7 Frame-lock | CLEAR | The paper changed its frame across rounds (hypotheses turned into estimands; DCCA layer conceded to add little over Pearson; H2 qualified, H3 not supported, H4 not supported); Sec. 2.7 discloses that decision rules were set at revision. |

Block status: Mode 6 SUSPECTED ⇒ per `ai_research_failure_modes.md` the pipeline blocks until the counts are corrected (or the user records an override). After the M1 and m1 text fixes Mode 6 becomes CLEAR; no rerun is needed.

## 5. Phase A/B — References (fresh check of the fixed and new entries; full-list cross-match)

Full list: 67 entries; every entry is cited in the text and every author–year citation in the text has a list entry (scripted match). The 64 other entries were VERIFIED in 08_citation_audit_v3.md; their metadata is unchanged in the current list, so they were cross-matched rather than re-searched.

| Entry | Phase A | Phase B (context) | Evidence |
|---|---|---|---|
| Ministry of Finance (2020) Circular 120/2020/TT-BTC, title "on trading of listed and registered shares, fund certificates, corporate bonds and covered warrants listed on the securities trading system" | VERIFIED (fix applied) | VERIFIED: Art. 2(11) defines covered short selling of securities borrowed through the VSDC lending system; "to our knowledge ... not put into operation" is appropriately hedged | thuvienphapluat.vn/van-ban/chung-khoan/circular-120-2020-tt-btc-...-464506.aspx; caselaw.vn/van-ban-phap-luat/369178-...; thoibaotaichinhvietnam.vn/nha-dau-tu-duoc-ban-khong-co-phieu-va-giao-dich-t0-31730.html |
| FTSE Russell (2025, October 7) "FTSE Russell announces results of September 2025 semi-annual country classification review" [Press release]. LSEG | VERIFIED (fix applied; date and headline confirmed) | VERIFIED: Frontier → Secondary Emerging effective 21 Sep 2026, subject to March 2026 interim review (since confirmed) | lseg.com/en/media-centre/press-releases/ftse-russell/2025/ftse-russell-country-classification-september-2025; mondovisione.com/.../ftse-russell-announces-results-of-september-2025-semi-annual-country-classificat-2025108/ |
| Corsetti, Pericoli & Sbracia (2005) JIMF 24(8) 1177–1199 — wording | VERIFIED | VERIFIED: Sec. 2.5 now says the correction "can be biased toward finding no contagion, because it places unrealistic restrictions on the variance of country-specific shocks", and Table 1 says "bias from restricted idiosyncratic variance"; Secs. 2.7 and 4.6 consistent. Fix C1 applied. | ideas.repec.org/a/eee/jimfin/v24y2005i8p1177-1199.html |
| **NEW** Ho Chi Minh City Stock Exchange (2022, September 29) Press release on the listing of the DCVFMVNMIDCAP ETF. HOSE. | VERIFIED (exists; date correct): HOSE press release (thông cáo báo chí) of 29/09/2022 announcing the listing and first trading of 6,000,000 DCVFMVNMIDCAP ETF certificates (FUEDCMID) | VERIFIED: "listed on the HOSE since 29 September 2022" — first trading day 29/09/2022 | static2.vietstock.vn/vietstock/2022/9/29/20220929_3_2__tcbc_niem_yet_quy_etf_dcvfmvnmidcap__eng_final_.pdf; thitruongtaichinhtiente.vn/chinh-thuc-giao-dich-chung-chi-quy-etf-dcvfmvnmidcap-42502.html; bizhub.vietnamnews.vn/first-mid-cap-etf-listed-on-hose-post337768.html |
| **NEW** Vietnam Securities Depository (2015) Decision No. 211/QĐ-VSD of 18 December 2015 on the securities settlement cycle. | VERIFIED (number, issuer, date) but **title MISDESCRIBED (MINOR)**: Decision 211/QĐ-VSD promulgates the VSD Regulation on clearing and settlement of securities transactions (replacing Decision 28/QĐ-VSD of 13/03/2015); it moved shares and fund certificates from T+3 to T+2 effective 1 January 2016. It was later replaced by Decision 109/QĐ-VSD (effective 29/08/2022). | VERIFIED: "settlement moved from T+3 to T+2 on 1 January 2016" | invest.vndirect.com.vn/?p=17425; kisvn.vn/en/announcement-ref-apply-the-settlement-time-t2-from-01-01-2016; hsc.com.vn/en/thong-bao-ap-dung-chu-ky-thanh-toan-t2; lsvn.vn/chu-ky-thanh-toan-chung-khoan-chinh-thuc-rut-ngan-xuong-t21661824227-a123203.html |
| Government of Vietnam (2025) Decree 245/2025/ND-CP of 11 September 2025 | VERIFIED (one secondary list gives 10/09; the decree's own summaries and most sources give 11/09/2025, effective on signing) | VERIFIED | luatvietnam.vn/tin-van-ban-moi/tu-11-9-2025-rut-ngan-thoi-gian-dua-chung-khoan-len-san-giao-dich-186-104047-article.html; hcc.nghean.gov.vn/laws/detail/Nghi-dinh-so-245-2025-ND-CP-... |

Exact corrections (MINOR, form only):
- r1 VSD entry → `Vietnam Securities Depository. (2015). Decision No. 211/QĐ-VSD of 18 December 2015 promulgating the Regulation on clearing and settlement of securities transactions. Hanoi.` (in-text "(Vietnam Securities Depository 2015)" unchanged).
- r2 HOSE entry → `Ho Chi Minh City Stock Exchange. (2022, September 29). Listing and official trading of DCVFMVNMIDCAP ETF fund certificates [Press release]. HOSE.` (brackets match the FTSE entry's style; the press release is a "Thông cáo báo chí niêm yết Quỹ ETF DCVFMVNMIDCAP"). Optional: add the HOSE/press URL.
- r3 FTSE entry: optional — append the LSEG URL listed above (Springer style permits URLs for press releases and the earlier audit recommended it).

## 6. Response letter — claim-by-claim check against the manuscript
Every row of notes/review_r2/response_to_reviewers.md was compared with the current manuscript and outputs. 52 claims checked; 44 TRUE; 8 problems:

| # | Letter location | Letter says | Manuscript / outputs | Severity | Exact fix |
|---|---|---|---|---|---|
| L1 | Part C, RR-16, last sentence | "H3 is assessed as mixed." | Table 9 and Sec. 5.5: H3 "Not supported" under its two-part rule (Addendum row 1 also says so) | **MAJOR** (claim false of the manuscript; letter contradicts itself) | Replace with: "Under its two-part decision rule H3 is not supported: the adjusted correlation shows no contagion, while the loading rises on high-volatility days (Table 9, comment column)." |
| L2 | Part B, B8 | "All bootstrap replication counts are given in Section 4.4." | Sec. 4.4 omits/misstates the 199, 399 and several 999/499 counts (issue M1) | **MAJOR** until M1 is fixed; TRUE after | Fix M1; no letter change needed then. |
| L3 | Main changes item 6 | "a factor-model test that is robust to common shocks" | After fix C1 the manuscript's rationale is restricted country-specific (idiosyncratic) variance, not common shocks | MINOR | "a factor-model test that allows the idiosyncratic variance to change between regimes" |
| L4 | RR-2 | "κ lies between 0.47 and 0.52 across all scales and frequencies" | Manuscript: "all reliable scales"; over all 30 scales κ is 0.434–0.571 (R8b) | MINOR | "across all reliable scales and frequencies" |
| L5 | RR-13 (twice), RR-26, "Items declined" sentence, Addendum rows "H1 not tested..." and "Sign error in Section 6.3" | Section 6.3 | VNMIDCAP/FUEDCMID validation, weight path and the FTSE comparative-statics prediction are in Sec. 6.4 (Limitations); Sec. 4.2 also mentions validation | MINOR | Change "Section 6.3" to "Section 6.4" in RR-13, RR-26, the Addendum "H1 not tested" row and "Sign error in Section 6.3" (→ "Section 6.4"); "Items declined ... Section 6.3" → "Sections 6.3 and 6.4". |
| L6 | RR-14 | "The difference between broad and nested slopes is reported through Eq. (14) and the TOST rather than as a separate bootstrap contrast." | Superseded: Sec. 5.4 and Table S7 now report the within-replicate contrast (R34), as the Addendum says | MINOR | Append "(superseded in the second round: the within-replicate contrast is now reported, Table S7)". |
| L7 | B9 | "Every estimate has a 95% interval" | Not every estimate does (Table 4 Panel A gaps; κ, ρ_AB, bound in Table 5; Table 8 Panel B QLIKE) | MINOR | "Every gap, decomposition quantity, slope and regime statistic has a 95% interval" |
| L8 | RR-12 | "H1 uses a margin of 0.05 stated in advance" | Sec. 2.7: the 0.05 tolerance was fixed before the analysis but the H1 rule was set at revision | MINOR | "H1 uses a margin of 0.05, the estimation tolerance fixed in advance in Section 4.4; the rule itself was set at revision and is labelled as such (Section 2.7)." |

Also noted (not an error): A1 lists "five corollaries" as benchmark, lower bound, sensitivity, direction and κ < √3, whereas in the manuscript the benchmark and bound are both Corollary 1 and Corollary 5 is the attribution; consider "five corollaries (benchmark and lower bound, sensitivity, direction, the κ < √3 condition, and the Shapley attribution)". Claims I could not verify from the Markdown: B12 "numbered OMML objects" (DOCX property) and B8 "byte-identical CSV files" (needs a rerun): INSUFFICIENT EVIDENCE, advisory.

## 7. Issue list (sorted by severity)

### CRITICAL (= SERIOUS)
None. No fabricated, untraceable or wrong number; no nonexistent reference; no wrong hypothesis outcome; Lemma 1, Corollaries 1–5, Eq. (14) and Box 1 are correct.

### MAJOR (= MEDIUM, must fix before Stage 5)
- **M1 — Sec. 4.4, bootstrap replication counts do not match the code.** Text: "We use 499 replications for DCCA statistics, 999 for the factor-model, lead–lag and materiality statistics and 1,999 for Pearson regime statistics." Actual: R34/R35 (Table S7, Table S15, the trimmed-bar results and slope differences in Sec. 5.4) B = 199; R36 (weight-drawn like-for-like gap, Sec. 5.2) B = 399; R25 (Table 7 VN30-quartile FR column, Table S10) and R37 (2021 variant) B = 999; R20 hedge effectiveness and R11 tail dependence B = 499. Only R3/R4 use 1,999. Fix: replace the sentence with "We use 499 replications for the DCCA statistics of Tables 4–6 and for the decomposition, hedge-effectiveness and tail-dependence statistics, 399 for the like-for-like gap under weight uncertainty, 199 for the trimmed-bar and block-length checks of Tables S7 and S15, 999 for the factor-model, lead–lag and materiality statistics and for the Forbes–Rigobon tests under VN30 quartiles, across weights and with 2021 added, and 1,999 for the remaining Forbes–Rigobon and relative-error statistics." (Alternative: rerun run_round3e.R with B = 499, which changes the R34–R37 numbers and requires re-rendering Sec. 5.2, 5.4, 5.5 and Tables S7, S15.)
- **M2 — Response letter RR-16: "H3 is assessed as mixed."** False of the manuscript (H3 not supported). Fix as in L1.

### MINOR (recommended)
- m1 Sec. 4.8 seeds: "Random seeds are fixed in each script (20260924 to 20261013)" → "(20260924 to 20261014; the reliability simulations in run_all.R use fixed seeds starting at 42)". run_round3e.R uses 20261014; run_all.R calls `reliable_smax` with seed = 42 + offsets.
- m2 Sec. 4.4 p-value convention: add "One-sided Forbes–Rigobon p-values use the re-centred bootstrap distribution; p-values for Δβ, the residual-variance ratio and the slopes are studentized." (R3/R25/R37 use `mean(cen >= diff)`; R29 uses 2Φ(−\|t\|).)
- m4 Sec. 5.4: "and the κ channel partly offsets the ρ_AM channel" → "and at M30 and H1 the κ channel partly offsets the ρ_AM channel" (same sign at 1D and H4, R30/Table S13).
- m5 Sec. 5.5: "no one-sided p falls below 0.935" (min 0.9349) → "no one-sided p falls below 0.93".
- m6 Table S2: column header "Pearson ρ̲ (1D)" → "Pearson ρ̲" (M30 rows show M30 values).
- m7 Table S7 notes: add "Bootstrap draws are separate from Table 6, so intervals and p-values for the all-bars rows differ by Monte Carlo error."
- m9 Table S7 notes / Sec. 5.4: add "Trimmed samples use the full-sample reliability thresholds of Table 3."
- r1 VSD reference title; r2 HOSE reference form; r3 optional FTSE URL (Sec. 5).
- L3–L8 response-letter wording/location fixes (Sec. 6).

### Advisory (not counted)
- "byte-identical CSV output files" and "numbered OMML objects" not re-verified here.
- Table 7 chronological FR CI [−0.082, 0.001] (R3, B = 1,999) vs Table S10 at the factsheet weight [−0.082, −0.005] (R25, B = 999): Monte Carlo difference, disclosed in the S10 note.

## 8. Verdict

**FAIL** (Stage 4.5, final-check) — 0 CRITICAL, 2 MAJOR (M1, M2), 16 MINOR; AI failure-mode checklist: Mode 6 SUSPECTED (text-level replication-count misstatement), Modes 1–5 and 7 CLEAR.

Both MAJOR items are text-only fixes (one sentence in Sec. 4.4 of r2_text.py; one sentence in the response letter). No number, table, figure or conclusion changes; no R rerun is required unless the authors choose to re-run run_round3e.R at B = 499. After M1, M2 and m1 are applied, a re-verification of only those sentences (plus a regeneration check of manuscript_anonymized.md) should give PASS WITH NOTES; applying the MINOR items as well gives PASS.

Coverage statement: Phase C covered 100% of the registered numeric surfaces of the abstract, Box 1, Tables 2–9 and Sections 5–7, plus 452 supplement numbers; Phase E covered 100% of hypothesis outcomes and the listed verbal claims; Phase A re-searched the 3 fixed and 2 new references and cross-matched all 67; Phase D (originality) was not in the requested scope. PASS would not certify the research as correct beyond these registered populations.
