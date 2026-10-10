# Stage 4.5 FINAL INTEGRITY — Independent verification report (mode: final-check)

- Agent: integrity_verification_agent (ARS academic-pipeline v3.22.1, Mode 2), fresh context; AUDIT_LEDGER not read.
- Inputs: project_R/docx_build/r2/manuscript_anonymized.md; supplementary_material.md; project_R/outputs/*.csv; R scripts; notes/review_r2/08_citation_audit_v3.md; notes/review_r2/response_to_reviewers.md.
- Date: 2026-10-10. No manuscript or code file was edited.
- Status: report written incrementally (sections appended as completed).

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
Note N1: "Applied to full-sample Pearson correlations, the identity gives a benchmark of 0.898–0.903 and a benchmark-first share of 0.911–0.914 across frequencies." R14 contains Pearson values only for 1D (0.9034/0.9139) and M30 (0.8983/0.9106). I recomputed H1 and H4 from 01_descriptive_stats sds and 14b static correlations: benchmark 0.9020/0.9023, share 0.9141/0.9130. The range is therefore correct, but the H1/H4 values are not written to any output file (traceability gap; MINOR, issue m3).

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
