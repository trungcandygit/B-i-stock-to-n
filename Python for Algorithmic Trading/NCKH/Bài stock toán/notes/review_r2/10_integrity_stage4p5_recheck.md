# Stage 4.5 FINAL INTEGRITY — Re-verification after condensation (mode: final-check, round 2)

- Agent: integrity_verification_agent (ARS academic-pipeline v3.22.1, Mode 2; checklist references/ai_research_failure_modes.md), fresh context; notes/AUDIT_LEDGER.md not read.
- Inputs: project_R/docx_build/r2/manuscript_anonymized.md (current, HEAD 6943d23); supplementary_material.md; uncondensed text at HEAD~3 (dc7f8b3, "Ledger D53 ..."), the last commit before "Condense v3 manuscript source"; project_R/outputs/*.csv; project_R/run_*.R; notes/review_r2/response_to_reviewers.md; notes/review_r2/09_integrity_stage4p5.md.
- Date: 2026-10-10. No manuscript, code or letter file was edited; only this report was written.
- Status: COMPLETE. Verdict: FAIL (0 CRITICAL, 1 MAJOR, 12 MINOR) — one condensation-introduced misstatement (N1); see Sections 6–7.

## 1. Resolution of the issues in 09_integrity_stage4p5.md

Method: each issue was checked in the current files (manuscript_anonymized.md, supplementary_material.md, response_to_reviewers.md, run_*.R). Note: 09 uses the labels m1, m2, m4–m7, m9; there is no m3, and "m8" (re-centred FR p-value convention, 09 Sec. 3.2) was folded into m2. Both are covered below.

| Issue | 09 required fix | Current state (evidence) | Status |
|---|---|---|---|
| M1 Sec. 4.4 replication counts | List the actual B per analysis | Sec. 4.4 now: 499 (Tables 4–6, decomposition, hedge, tail dependence), 399 (gap under weight uncertainty), 199 (Tables S7, S15), 999 (factor, lead–lag, materiality, FR under VN30 quartiles/weights/2021), 1,999 (remaining FR and RE). Code: run_revision/round2/round3/round3b default B = 499 (R2, R8, R10, R11, R13, R15, R20, R21); round3e B = 199 (R34, R35), 2B+1 = 399 (R36), 5B+4 = 999 (R37); round3b replicate(999) (R25); round3c/round3d B = 999 (R28, R29, R31); run_revision replicate(1999) (R3, R4). All stated counts are TRUE. Residual: two outputs drawn with B = 199 in run_round3b.R are not covered by the sentence (R23 trimmed gap in Sec. 5.4; R24 M30 rows of Table S6) — see new issue n1 (MINOR). | RESOLVED (residual MINOR n1) |
| M2 / L1 Letter RR-16 "H3 is assessed as mixed" | Replace with "not supported" | RR-16 now ends: "Under its two-part decision rule H3 is not supported: the adjusted correlation shows no contagion, while the loading rises on high-volatility days (Table 9, comment column)." Consistent with Table 9 and Sec. 5.5. | RESOLVED |
| m1 Sec. 4.8 seeds | "20260924 to 20261014; reliability simulations seeds from 42" | Sec. 4.8: "(20260924 to 20261014; the reliability simulations use fixed seeds starting at 42)". Code: set.seed 20260924, 20261007, 20261010–20261014; R/dcca.R reliable_smax seed = 42 + offsets. | RESOLVED |
| m2 (+m8) p-value conventions | State re-centred FR p and studentized Δβ / ratio / slopes | Sec. 4.4: "One-sided Forbes–Rigobon p-values use the re-centred bootstrap distribution, and p-values for Δβ and the residual-variance ratio are studentized" + studentized slope p. Code R29: p_d_beta, p_idio = 2Φ(−\|t\|). | RESOLVED |
| m4 κ channel offset | Restrict to M30 and H1 | Sec. 5.4: "at M30 and H1 the κ channel partly offsets the ρ_AM channel". R30: opposite signs at M30 (0.000187 / −0.000244) and H1 (0.000214 / −0.000146); same sign at 1D, H4. | RESOLVED |
| m5 "below 0.935" | "below 0.93" | Sec. 5.5: "above 0.93 across weights, Table S10"; R25 min one-sided p = 0.9349. | RESOLVED |
| m6 Table S2 header | "Pearson ρ̲" | Header now "Pearson ρ̲". | RESOLVED |
| m7 Table S7 separate draws | Add note | S7 note: "199 block-bootstrap replicates, drawn separately from Table 6". | RESOLVED |
| m9 Trimmed samples' thresholds | Add note | S7 note: "... and the full-sample thresholds of Table 3". | RESOLVED |
| r1 VSD entry title | "promulgating the Regulation on clearing and settlement ..." | Reference list now has exactly the recommended title. | RESOLVED |
| r2 HOSE entry form | "Listing and official trading of DCVFMVNMIDCAP ETF fund certificates [Press release]. HOSE." | Present verbatim. | RESOLVED |
| r3 FTSE URL (optional) | Append LSEG URL | Appended (lseg.com/.../ftse-russell-country-classification-september-2025). | RESOLVED |
| L2 Letter B8 counts | Follows M1 | True after M1 (see n1 residual). | RESOLVED |
| L3 Main change 6 "robust to common shocks" | "allows the idiosyncratic variance to change" | Item 6 now uses that wording. | RESOLVED |
| L4 RR-2 "all scales" | "all reliable scales" | RR-2 now "across all reliable scales and frequencies"; R8b reliable rows κ 0.4736–0.5249. | RESOLVED |
| L5 "Section 6.3" vs 6.4 | Point to limitations | No longer applies: Secs. 6.3 and 6.4 were merged into "6.3 Transferability and limitations", which now contains the VNMIDCAP/FUEDCMID validation, weight path and FTSE comparative-statics prediction. All letter pointers to "Section 6.3" (B6, RR-6, RR-13, RR-26, items-declined sentence, Addendum rows) now resolve to the right content. No "Section 6.4" remains in letter, manuscript or supplement. | RESOLVED (by merge) |
| L6 RR-14 superseded contrast | Append note | Present: "(superseded in the second round: the within-replicate contrast is now reported, Table S7)". | RESOLVED |
| L7 B9 "every estimate has a 95% interval" | Narrow claim | B9: "Every gap, decomposition quantity, slope and regime statistic has a 95% interval". Residual: the 2021-variant Δβ interval was dropped from the text by condensation (n6). | RESOLVED (residual MINOR n6) |
| L8 RR-12 "stated in advance" | Distinguish tolerance from rule | RR-12 now says the tolerance was fixed in advance and the rule set at revision (Sec. 2.7). | RESOLVED |
| A1 "five corollaries" note | Optional rewording | A1 now lists "the zero-correlation benchmark with the exact lower bound √(1 − κ²), the sensitivity, the direction result, the condition κ < √3 ..., and the Shapley attribution, Eq. (11)", matching Corollaries 1–5. | RESOLVED |

Summary: all 2 MAJOR, all MINOR (m1, m2/m8, m4–m7, m9), r1–r3 and L1–L8 issues of 09 are resolved. Two narrow residuals are re-raised as new MINOR items (n1, n6).

## 2. Condensation integrity (HEAD~3 dc7f8b3 → HEAD 6943d23)

Method. (a) Scripted comparison of the two Markdown files: all table rows, all table/figure/box captions, all table/figure notes, all display equations, the reference list, and the sets of numbers, citations, equation/table/figure/box/section cross-references in the prose. (b) Full side-by-side reading of the old and new prose, paragraph by paragraph (old prose 9,854 words incl. title/abstract/captions/declarations; new 7,105; new main text Sec. 1–7 = 6,603 words; abstract 213 words).

### 2.1 What is unchanged (scripted, exact)
- Tables 1–9 and Box 1: every row identical (diff of all `|` rows: 0 differences). All captions and all notes identical.
- Display equations (1)–(16): all present, numbered consecutively, identical except a comma replacing a full stop after Eq. (15).
- Reference list: 67 entries, same membership; only the three entries fixed per r1–r3 changed.
- Supplementary material: unchanged apart from the m6, m7, m9 fixes (two lines).
- Cross-reference sets: every Table S1–S15 and Fig. S1 is still referenced from the main text (Table S1 is now referenced explicitly in Sec. 4.5, Table S12 in Sec. 3.2, which the old text did not do); Tables 1–9, Figs. 1–4, Box 1, Corollaries 1–5, Lemma 1, Online Resources 1–2 all still referenced. Dropped section pointers ("Section 2.1", "Section 3/4/5", one "Section 4.2") were roadmap-type references whose targets remain; "Section 6.4" became "Section 6.3" (merge).
- Hypothesis rules H1–H4: each decision rule is preserved in substance (H1 lower 95% bound of the like-for-like gap > 0.05 at every frequency; H2 ≥ 1 broad-market pair at each of M30 and H1 with positive slope and Holm-adjusted studentized p < 0.05 in the eight-test family; H3 FR one-sided p < 0.05 AND Δβ two-sided p < 0.05 under VN30 regimes; H4 EWMA or regime QLIKE below static with DM p < 0.05 over 2023–2025). The disclosure that rules, the eight-test family and the factor-loading test were set at revision is retained. Outcomes (Supported / Supported / Not supported / Not supported; E1–E3 estimated) unchanged in text and Table 9.

### 2.2 Citations
- In-text → list: 65 distinct author–year citations in the main text plus Oświęcimka et al. (2014) in the supplement; every one has a list entry (scripted match; three Chen entries 2016/2021/2024 and two Zhou entries 2008/2025 disambiguated by year).
- List → text: all 67 entries are cited in the main text.
- Old vs new citation set: identical (the only differences in the scripted extraction were false positives such as "Following Podobnik and Stanley (2008)" → "(Podobnik and Stanley 2008; ...)").
- Citation-context changes introduced by condensation (Phase B, all re-read):
  - Chen et al. (2021), Sec. 2.4: old "Liquidity fell after the introduction of a market surveillance system, especially for small firms"; new "liquidity of small firms is fragile". The source's finding (surveillance system reduced liquidity, more for small firms) is generalized to a property. MINOR_DISTORTION (n3).
  - Bui et al. (2022), Sec. 2.4: old "sector connectedness above 60% that rose to about 90% during COVID-19"; new "sector connectedness of 60–90%". Acceptable compression, but loses the COVID-19 timing; MINOR (n3).
  - Okorie and Lin (2021), Tilfani et al. (2021), Guo et al. (2021), Santana et al. (2023), Liao et al. (2022), Wang et al. (2021), Kakinaka et al. (2025), Greenwood and Sammon (2025): details shortened (e.g. "32 stock markets", "19 markets", the crude-oil/precious-metal split, "index trackers and beta arbitrageurs"); the remaining statements are accurate summaries. VERIFIED.
  - Corsetti et al. (2005), Forbes and Rigobon (2002), Rigobon (2003): bias toward no contagion from restricted idiosyncratic variance preserved (Secs. 2.5, 2.7, 4.6). VERIFIED.

### 2.3 Numbers dropped from the prose (scripted set difference, then located)
| Dropped number (old location) | Still available? | Assessment |
|---|---|---|
| "a change of 0.1 ... moves the nested one by about 0.01" (Intro) | Same content as sensitivity 0.106–0.112 | OK |
| 167 replications per correlation (Sec. 4.4) | 1,002 per frequency kept; Table 3 note | OK |
| 2021: drawdown 14.3%, 32%; 2025: 18.1%, 30% (Sec. 3.2) | Table S12 (R27: −14.26, 0.32; −18.11, 0.305) now cited in Sec. 3.2 | OK |
| Upper bounds 0.155–0.168 of the weight-drawn gap (Sec. 5.2) | Not reported anywhere now (R36) | OK (lower bounds carry the H1 test) |
| VN100–VNINDEX M30 drop-first slope 0.0010 (Sec. 5.4) | Table S7 | OK |
| 0.935 → 0.93 (Sec. 5.5) | m5 fix | OK |
| 2021 variant: 789 crisis days, Δβ CI [−0.122, 0.124] (Sec. 5.5) | Not in the supplement; now only "FR p = 0.987; Δβ = −0.005" | MINOR n6 (estimate reported without its interval; letter B9 promises intervals for regime statistics) |
| "Section 6.4" | merged | OK |

Numbers added: 0.93 (m5), 199, 399, 20261014, 42 (M1, m1 fixes), −0.002 (reworded M30 benchmark slope; see N1).

### 2.4 Statements whose meaning changed, or qualifications dropped
| # | Location (new) | Old text | New text | Assessment |
|---|---|---|---|---|
| C1 | Sec. 5.3, para. 3 | "although at M30 the percentile interval just excludes zero; a slope of that size (about 0.002 per unit of ln s) is negligible" | "although at M30 the percentile interval just excludes a negligible slope of about −0.002" | **Meaning inverted. R15 M30 floor_slope = −0.00246 [−0.00452, −0.0000171]: the interval excludes zero and contains −0.002.** MAJOR N1 |
| C2 | Sec. 5.4, para. 3 | "Trimming does not change the overlap gap (0.107 [0.094, 0.127] at M30 without the first bar)" | "but the differences vanish without the auction bars, while the overlap gap does not change (0.107 [0.094, 0.127] at M30)" | The value is the first-bar-removed gap (R23, n = 19,709), but the new sentence attaches it to "without the auction bars" (both bars removed). No gap is reported for the both-bars sample. MINOR n2 |
| C3 | Sec. 6.3 | "The three-pair gap in Table 4 is therefore descriptive for these pairs"; "so the magnitudes should not be generalized beyond the HOSE" | Dropped; 6.3 now says "The evidence comes from one exchange and three indices." Sec. 5.2 still says the broad-market pairs "cannot be purged by weight". | Limitations weakened, not removed. MINOR n4 |
| C4 | Sec. 4.4 | "the grid and the tolerance were fixed before the empirical analysis" | "a tolerance fixed in advance" | Pre-specification of the 40-scale grid dropped; letter B7 still claims "tolerance and grid were fixed in advance". MINOR n5 |
| C5 | Sec. 4.4 | "(20 days times the number of bars per day at intraday frequencies)" | "mean blocks of about 20 trading days" | Still accurate (LBLOCK = 20 × bars/day); detail lost. Advisory |
| C6 | Sec. 4.2, Cor. 3 | "... can only raise the coefficient, with equality only at ρ_AM = 1" | equality clause dropped | Correct as stated; no loss of a claim used later. OK |
| C7 | Sec. 4.2 | P_cap replication "which the short-sale rules rule out"; Sec. 3.1 "so the mid-cap tier can be held long but not shorted or hedged with a dedicated derivative" | both dropped | Sec. 3.1 keeps "no mid-cap future" and "naked short selling is prohibited". Content OK, but the letter (RR-24) quotes the dropped phrase (L-a). |
| C8 | Sec. 4.5 | "We evaluate Eq. (14) with the reliable-range slopes of ρ_AM and κ and compare it with the observed slope." | dropped | Sec. 5.4 and Table S13 still give the comparison. OK |
| C9 | Sec. 5.2 | "so the point estimate stays above the margin at every weight in the grid, but its size is known only to within about a factor of two" | "although the size of the gap is known only to within a factor of about two" now attached to the weight-drawn result | Grid 0.063–0.164 and weight-drawn interval 0.057–0.168 both span a factor of about 2.6–2.9; "about two" was loose before and is unchanged in substance. Advisory |
| C10 | Sec. 5.6 | "Only the calm-quartile overstatement for P_cap–VN30 exceeds one standard error." | dropped | Visible in Table 8 (RE/SE 1.50; all others ≤ 0.43); "0.13–1.50" kept. OK |
| C11 | Sec. 2.7 | "The first-round version of this paper reported five hypotheses with unadjusted tests." | dropped | The revision-stage labelling and "we also report the original specifications" remain. OK |

No other number, rule, outcome, equation, citation, table/figure/box reference or limitation was lost or changed in meaning. Every remaining shortened passage was compared with its old counterpart and carries the same claim.

## 3. Phase C — Fresh number check (abstract, Secs. 1–3, 5, 6–7; Sec. 4 numbers included)

Method: every number in the prose was read from the CSV named (values re-extracted in this session with a script, not copied from 09) and rounded half-up at the printed precision. "OK" = exact match.

### 3.1 Abstract, Section 1, Section 7 (14 numbers; 14 OK)
| Claim | Source | Status |
|---|---|---|
| "about 0.11 per unit change" (abstract, Sec. 7) | R8 sensitivity 0.1060 / 0.1118 / 0.1068 / 0.1064 | OK |
| "about 0.10 at every frequency" | R15 gap_like 0.0987–0.1040 | OK |
| 2014–2025, 30-minute to daily | 01 first 2014-01-27 / last 2025-12-12 | OK |
| "about two-thirds"; 0.988 daily VN30–VN100 | w = 0.6826; R33 rho_AB 0.98848 (Pearson), 02 Panel B 0.98764 (DCCA) | OK |
| slope 0.106–0.112; gap 0.099–0.104; κ 0.47–0.52 | R8; R15; R8b reliable rows (66 of 120): κ 0.4736–0.5249 | OK |
| Abstract length | 213 words | OK |

### 3.2 Section 2 (6 numbers; 6 OK)
60–90% (Bui et al.; wording see n3); search window 2021–2026; H1 margin 0.05 (= tolerance, Sec. 4.4); eight broad-market tests (2 pairs × 4 frequencies, R22 h3_family = 8 rows); κ < √3 (R33 share_condition_kappa_max 1.7320508); 2023–2025 (R18b split 2023-01-01, n_eval 735). OK.

### 3.3 Section 3 (27 numbers; 27 OK)
| Claim | Source | Status |
|---|---|---|
| ±7%; T+2 from 1 Jan 2016; auction times 09:00–09:15, 11:30, 13:00, 14:30–14:45; 29 Sep 2022; 21 Sep 2026; 30% banks | Institutional facts verified in 09/08 against primary sources; wording unchanged in substance | OK (not re-searched) |
| Daily/M30 to 12 Dec 2025; H1/H4 to 9 Dec 2024 | 01 last dates | OK |
| M30/H1 bar opening times; two H4 bars | R32_intraday_bar_schedule (09); unchanged | OK |
| Synchronized 3 Jan 2017 – 9 Dec 2024; N 1,983 / 19,463 / 9,879 / 3,953 | 02 Panel A | OK |
| Full N 2,963 / 21,942 / 13,523 / 5,410; Feb 2014–Dec 2025, Jan 2017–Dec 2025, Jan 2014–Dec 2024 | 01 | OK |
| Episodes 26.2%/47%, 33.5%/52%, 40.2%/60% | 11: −26.209/0.4659, −33.511/0.5207, −40.192/0.5976 | OK |
| 539 crisis days; 1,000 calm | scalars n_crisis_days 539, n_calm_days 1000; 249 + 121 + 169 = 539 | OK |
| Quartiles 10.6% / 20.0% | scalars vol_quartiles_ann_pct 10.6, 20 | OK |

### 3.4 Section 4 (24 numbers; 24 OK)
w = 0.6826, VND 1,316,288 bn / 1,928,303 bn (run_all.R W_REAL); Jensen 3.6 × 10⁻⁶ (scalars 3.63e-06); 315% / 215% (1/(1−w) = 3.150; w/(1−w) = 2.150); 3.73 (R33 3.7252); 4.4 × 10⁻¹⁶ (R8b max \|identity_error\| 4.44e-16); U(0.60, 0.75) (round3b/round3e runif(1, 0.60, 0.75)); correlations −0.3…0.9, 1,002 per frequency, 40 scales (R/dcca.R; 03 n_sims 1002; run_all.R n_repeats = 167); 300 GARCH sims (50 × 6); block length ≈ 20 days (LBLOCK = 20 × bars/day); B = 499/399/199/999/1,999 (see Sec. 1, M1); p ≥ 0.004 at B = 499 (2/500); Holm floor 0.076 (19 × 0.004); TOST margin 0.001 and 4.5 units of ln s (ln(444/5) = 4.49); λ = 0.94, five DM lags (run_round3.R); R 4.3.3 and package versions (as in 09); seeds (Sec. 1, m1). OK.

### 3.5 Section 5 prose (71 numbers; 70 OK, 1 wrong statement)
| Claim | Source | Status |
|---|---|---|
| 5.1: P_cap SD 0.0124, VNINDEX 0.0115; kurtosis > 33 at M30 | 01 (min M30 kurtosis 33.94, P_cap) | OK |
| 5.1: 50 days / 444 bars; heavy tails "cut them by about two-thirds" | 03; R6: 50→20, 444→151, 233→86, 88→28 = cuts of 60%, 66%, 63%, 68% | OK |
| 5.1: heavy-tailed nested 0.975–0.979, purged 0.882–0.890 | R6 0.97486–0.97854; 0.88249–0.88994 | OK |
| 5.2: nested 0.975–0.980; P_cap–VN30 0.883–0.892 | 02 (min 0.97549, max 0.98025; 0.88287–0.89154) | OK |
| 5.2: like-for-like 0.099–0.104, lower bounds ≥ 0.084; three-pair 0.086–0.096; q 0.78–0.89 | R15 gap_like (ci_lo min 0.08398); 02 gap; R10 | OK |
| 5.2: grid like-for-like 0.063–0.164; three-pair 0.052–0.153 | R14 / 07 (unchanged since 09) | OK |
| 5.2: weight-drawn lower bounds 0.057–0.061; every replicate > 0.05 | R36 ci_lo 0.0567–0.0615; share_above_0.05 = 1 (×4) | OK |
| 5.3: sensitivity 0.106–0.112; ≈ 0.09 per 0.01; with weight uncertainty 0.07–0.17 | R8; 0.01/0.112–0.01/0.106 = 0.089–0.094; R21 0.0712–0.1682 | OK |
| 5.3: κ 0.48–0.50; 32% of VN100; benchmark 0.893–0.900; bound 0.864–0.875; "below about 0.86" | R8 κ 0.4839–0.5027; 1 − 0.6826; R8 floor; R16 true_min 0.8644–0.8751 | OK |
| 5.3: 0.987–0.988; benchmark-first 0.905–0.911; dependence-first 0.895–0.900; Shapley 0.505–0.508, intervals within 0.497–0.521 | R8 / R15 (econ_share 0.8946–0.9002; shapley_overlap CIs 0.4971–0.5212) | OK |
| 5.3: weight uncertainty Shapley 0.45–0.56, benchmark-first 0.83–0.95; sampling width ≈ 0.02 | R21 (0.4513–0.5564; 0.8344–0.9488); R15 widths 0.018–0.023 | OK |
| 5.3: κ 0.47–0.52 across reliable scales; benchmark range 0.007–0.016; p = 0.052–0.456; Holm 0.208–0.828 | R8b; R15 floor_range 0.0068–0.0159; floor_slope p, p_holm | OK |
| 5.3: "at M30 the percentile interval just excludes a negligible slope of about −0.002" | R15 M30 floor_slope −0.00246 [−0.00452, −0.0000171] | **WRONG (N1)**: the interval excludes 0 and contains −0.002 |
| 5.3: Pearson benchmark 0.898–0.903, share 0.911–0.914, within 0.01 | R8d floor 0.8983–0.9034, mech_share 0.9106–0.9141; max \|Δ\| vs R8 = 0.0048 | OK |
| 5.3: Fig. 4 point w 0.683, σ_M/σ_A 1.02, benchmark 0.903; "about 0.7" | R17 (0.6826, 1.0209, 0.9034); 1/√2 = 0.707 | OK |
| 5.4: four H2-family survivors, 0.0019–0.0024; rise ≈ 0.01 over the range | R22 p_stud_holm_h3 0.0393, 0.0393, 0.0008, 0.0449; estimates 0.00188–0.00242; × 4.5 | OK |
| 5.4: Holm (19) keeps one, BH four; smallest percentile BH 0.057 | R22 p_stud_holm_all 0.0020 only; p_stud_bh_all 0.0020/0.0375/0.0375/0.0426; BH of p_boot recomputed = 0.057 | OK |
| 5.4: TOST p 0.007, 0.012 | R22 0.0068, 0.0121 | OK |
| 5.4: damping 0.106–0.112; implied − observed ≤ 0.8 × 10⁻⁵ | R30 damping_factor; M30 −6.548e-5 vs −5.712e-5 → 8.4e-6 | OK |
| 5.4: purged slope 0.01 → nested ≈ 0.001; "five times the broad-market slopes" | 0.01 × 0.106–0.112; 0.01/0.0019–0.0024 = 4.2–5.3 | OK |
| 5.4: first bar 10% of M30 bars, 37% of squared VN30 returns | R23 0.1018, 0.3676 | OK |
| 5.4: H1 drop-first 0.0003, −0.0005; M30 VN30–VNINDEX 0.0020 (p 0.031) | R34 0.000338, −0.000491; 0.002005, p 0.0313 | OK |
| 5.4: drop-both M30 −0.00002, −0.0002 | R34 −1.81e-5, −2.02e-4 | OK |
| 5.4: differences 0.0018–0.0024, p ≤ 0.003; vanish without auction bars | R34 0.00182–0.00236, p 5.2e-5–0.00292; drop-both p 0.36–0.96 | OK |
| 5.4: gap 0.107 [0.094, 0.127] at M30 | R23 (first bar removed) 0.1072 [0.0944, 0.1265] | number OK; scope see n2 |
| 5.5: 0.847→0.924; 0.744→0.932; FR p 0.974–0.998; > 0.93 across weights; −0.087 [−0.144, −0.018] | R3 (0.8473, 0.9240; p 0.9850, 0.9745); R25 (min 0.9349; VN30 quartiles p 0.998) | OK |
| 5.5: ratio 2.70 [1.92, 3.68], 2.57; β 0.737→0.948, Δβ 0.210 [0.119, 0.306]; chronological 0.008 [−0.128, 0.140] | R29 C, B, A | OK |
| 5.5: 2021 added: FR p 0.987, Δβ −0.005 | R37 0.98699, −0.00483 | OK |
| 5.5: tail dependence 0.75 vs 0.62 | R26 Pcap–VN30 u = 0.05: 0.7492, 0.6172 | OK |
| 5.6: 2.23%, 9.38%, −1.84%, −2.07%; nested ≤ 2.35%; RE/SE 0.13–1.50, nested ≤ 0.43; DM p 0.069–0.179 | R31 (2.2287, 9.3846, −1.8430, −2.0661; nested max 2.3538; 0.1291–1.4991; nested max 0.4295); R18 | OK |
| 5.7: DMCA 0.882–0.891, gap 0.086–0.096; block 0.070–0.119 for 5–60 days; 0.9665/0.9663/0.9667; proxy weight 0.9865–0.9885 | R12 (0.8822–0.8907; 0.0859–0.0965); R13 (0.0700–0.1190); scalars (09); static correlations | OK |

### 3.6 Section 6 (22 numbers; 22 OK)
68% of VN100; benchmark ≈ 0.90; bound ≈ 0.87; observed 0.99; damping ≈ ten; lead 0.084 [0.028, 0.136], reverse 0.007, asymmetry 0.076 [0.048, 0.102] (R28 1D); intraday symmetric (R28 M30 asym CI [−0.024, 0.017], H1 [−0.028, 0.008]); inverse sensitivity ≈ 10 (R33 9.69; R8 8.9–9.4); 0.001 → 0.01; hedge 0.79 [0.75, 0.82], 0.53 [0.45, 0.61], 0.86 (R20 full, B_low, B_high); "a fifth" (0.21), "about half" (0.47); "above 0.7" at w = 0.5 and σ_M/σ_A ≤ 1 (κ ≤ 1 ⇒ ρ̲ ≥ 0.707); September 2026. OK.

### 3.7 Table spot-check (37 cells; 37 OK)
Table 2: VN30 1D row (2,963; 0.0004; 0.0121; −0.83; 7.81; 3,202) and VN30 M30 row (0.0001 from 5.04e-5; 0.0039; −1.62; 36.16; 1,014,769) — 11 cells, 01. Table 4: Panel A 1D (0.980, 0.988, 0.890, 0.090), Panel B M30 (0.979, 0.987, 0.883, 0.096 [0.080, 0.119]), like-for-like 1D 0.104 [0.085, 0.128], Cohen's q 1D 0.83 [0.75, 0.89] — 10 cells, 02/R2/R15/R10. Table 5: 1D κ 0.484, ρ_AM 0.884 [0.857, 0.906], ρ̲ 0.900 [0.891, 0.910], bound 0.875, sensitivity 0.106 [0.098, 0.114], share 0.911, Shapley 0.508 [0.498, 0.521]; Panel B 1D sensitivity 0.106 [0.071, 0.163], Shapley 0.508 [0.452, 0.556] — 9 cells, R8/R15/R16/R21. Table 6: M30 VN30–VNINDEX 0.0022 [0.0007, 0.0038], 0.012, 0.009, 0.144, 0.045; H1 VN30–VN100 TOST 0.012 — 6 cells, R22. Table 7: VNINDEX-quartile Δβ 0.240 [0.143, 0.332], ratio 2.57 [1.75, 3.66] — R29 B. Table 8: VNINDEX calm P_cap–VN30 9.38 [6.28, 13.27], 6.3, 1.50; Panel B VN30–VNINDEX static −7.9298 vs regime −7.9252 (static lowest) — R31/R18. All match.

**Phase C tally.** About 190 prose numbers and 37 table cells checked afresh. Untraceable numbers: 0. Rounding errors: 0. Wrong statements about a statistic: 1 (N1). Scope ambiguity: 1 (n2).

## 4. Response letter — re-check against the condensed manuscript

Every location and quotation in response_to_reviewers.md (main changes 1–8, A1, B1–B14, RR-1 to RR-30, items declined, Addendum rows) was re-checked against the condensed text, because condensation can make a previously true letter claim false. 61 claims checked; 54 TRUE; 7 problems (all MINOR):

| # | Letter location | Letter says | Current manuscript | Exact fix |
|---|---|---|---|---|
| L-a | RR-24 | "'cannot be traded' now reads 'cannot be shorted or hedged with a dedicated derivative'" | That phrase was removed from Sec. 3.1 by condensation; 3.1 now says only "there is no mid-cap future" and "naked short selling is prohibited". | Either restore in Sec. 3.1 after the FUEDCMID sentence: "so the mid-cap tier can be held long but not shorted or hedged with a dedicated derivative", or change the letter to: "'cannot be traded' was removed; Section 3.1 states that a VNMIDCAP ETF is listed but no mid-cap future exists." |
| L-b | RR-15 | "The bar schedule, including the 11:30–13:00 break and the two H4 bars, is stated in Section 3.1." | The session times are in 3.1, but the M30/H1/H4 bar schedule moved to Sec. 3.2. | "... is stated in Sections 3.1 and 3.2." |
| L-c | RR-4 | Section 1 states the practice conditionally ("if such a number is read as …") | Sec. 1 now reads "Read as a measure of how mid caps move with large caps, this number mixes ...". | Replace the quote by ("read as a measure of how mid caps move with large caps, this number mixes …"). |
| L-d | Addendum, row "H1 not tested under weight uncertainty" | "A daily validation against VNMIDCAP closes would need a series that our vendor export does not include; this is stated in Section 6.3." | Sec. 6.3 states that P_cap could not be validated; the vendor reason is now only in Sec. 3.2 ("The vendor has no full VNMIDCAP history"). | "... this is stated in Sections 3.2 and 6.3." |
| L-e | B7 | "the reliability tolerance and grid were fixed in advance" | Sec. 4.4 now says only "a tolerance fixed in advance" (grid clause dropped, C4). | Restore in Sec. 4.4: "... first exceeds 0.05; the grid and tolerance were fixed in advance" (preferred), or drop "and grid" from B7. |
| L-f | Addendum, "Formatting and wording" | "The M30 benchmark-slope wording is qualified." | The current wording is wrong (N1). | True once N1 is fixed; no letter change. |
| L-g | RR-9 | "The data statement names the HOSE as the public source of daily closes" | The Data availability statement names only TradingView; Sec. 3.2 mentions "HOSE closing levels". (Pre-existing; not introduced by condensation.) | "Section 3.2 names the HOSE closing levels as the public reference series, and the README gives SHA-256 checksums ..." |

Checked and TRUE after condensation (selection): B6 (survivorship, Sec. 3.2; generalization limit, Sec. 6.3); B8 (counts in Sec. 4.4, true subject to n1); B9 (intervals; see n6 for the 2021 variant); B10 (Sec. 6 structure: mechanisms, implications, transferability and limitations); B11 (Sec. 5.7, Tables S2–S8); B12 (Cauchy–Schwarz in Sec. 4.1; 4.4 × 10⁻¹⁶); RR-1, RR-2, RR-3, RR-6, RR-7, RR-11 ("cannot fall below" wording gone; the remaining "cannot fall below 0.004" concerns p-values), RR-12, RR-13, RR-14, RR-16, RR-21, RR-22, RR-25, RR-26 (Sec. 6.1 lists herding, limit hits, margin calls, foreign flows; Sec. 6.3 has the Eq. (8) prediction), RR-28, RR-29, RR-30; Addendum rows on H2/H3 rules, Table S7, Table S15, the sign of the FTSE prediction ("no more volatile" present in 6.3), sources, Table S14, 2021 (Sec. 5.5). Not verifiable from Markdown: B12 "numbered OMML objects" (DOCX property) — advisory. The submitted DOCX (submission/Revised_submission/02_Manuscript_Anonymized.docx) has the same unzipped content as project_R/docx_build/r2/manuscript_anonymized.docx (diff -rq: identical), so the checks above apply to the file that would be submitted.

## 5. AI research failure-mode checklist (7 modes, re-run)

| Mode | Status | Evidence |
|---|---|---|
| 1 Implementation bug passing self-review | CLEAR | Identity error ≤ 4.4e-16 (R8b); Box 1 closed form = directly built series (R33 sd_M = sd_Pcap_direct, rho_AM = rho_AM_direct); Eq. (14) reproduces observed slopes to 8.4e-6 (R30); BH of percentile p recomputed independently = 0.057; Pearson decomposition values within 0.0048 of DCCA; CIs vary across conditions; no constant or suspiciously round outputs. Code was not changed by the condensation (only r2_text.py/r2_lit.py and the letter). |
| 2 Hallucinated citation | CLEAR | 67/67 list entries cited; every in-text citation has an entry; set identical to the pre-condensation text; r1–r3 fixes applied as specified; no new reference added. Two compressed citation contexts flagged MINOR (n3). |
| 3 Hallucinated experimental result | CLEAR | All ~190 prose numbers and 37 table cells traced to CSVs; 0 untraceable. N1 is a mis-description of a real, correctly computed interval (the CSV value and the old sentence are right), not an invented result. |
| 4 Shortcut reliance | CLEAR | Horizon result still stress-tested against the auction-bar artefact and reported as vanishing; weight-error, block-length, detrending-order, heavy-tail and DMCA checks still reported (Sec. 5.7). |
| 5 Bug reframed as insight | CLEAR | grep for "surprising/unexpected/counterintuitive/in hindsight/contrary to": 0 hits in manuscript and supplement; the flat nested slope remains explained analytically (Eq. 14) and numerically. |
| 6 Methodology fabrication | CLEAR | Every replication count now stated in Sec. 4.4 matches the code; seeds match; block length, RiskMetrics λ, DM lags, OOS split, weight draw, joint resampling and p-value conventions match the scripts. Residual incompleteness (two 199-replicate outputs not listed, n1) is an omission, not a false methods statement. Mode 6, SUSPECTED in 09, is resolved. |
| 7 Frame-lock | CLEAR | Frame already revised across rounds (estimands vs hypotheses; DCCA layer conceded to add little over Pearson; H3, H4 not supported); revision-stage rules disclosed in Sec. 2.7. |

Block status: no mode SUSPECTED; no mode INSUFFICIENT EVIDENCE. The 09 Mode 6 block is cleared. Advisory, not re-verified here: "byte-identical CSV outputs" on rerun (run_all.R chains run_revision.R and run_round2–3e.R via system2, seeds fixed; no rerun performed in this check).

## 6. Issue list (sorted by severity)

### CRITICAL (= SERIOUS)
None. No fabricated or untraceable number, no nonexistent or orphan reference, no wrong hypothesis outcome, no change to any table, equation or decision rule.

### MAJOR (= MEDIUM, must fix before Stage 5)
- **N1 — Sec. 5.3, third paragraph (r2_text.py line 534): misstatement of the M30 benchmark-slope interval, introduced by the condensation.** Text: "its slope on ln s is not significant at 5% (p = 0.052–0.456; Holm 0.208–0.828), although at M30 the percentile interval just excludes a negligible slope of about −0.002." R15: M30 floor_slope = −0.00246 [−0.00452, −0.0000171], p = 0.052. The interval excludes **zero**, and it **contains** −0.002; the sentence says the opposite. The pre-condensation text was correct. Exact fix: "..., although at M30 the percentile interval just excludes zero; the slope, about −0.002 per unit of ln s, is negligible." No number, table or conclusion changes.

### MINOR (recommended)
- **n1 Sec. 4.4 replication counts incomplete.** run_round3b.R uses `replicate(199, ...)` for R23 (the trimmed gap 0.107 [0.094, 0.127] in Sec. 5.4) and R24 (M30 rows of Table S6), but Sec. 4.4 lists 199 only "for the trimmed-bar and block-length checks of Tables S7 and S15", and Table S6 (1D rows from R13, B = 499) gives no count. Fix in Sec. 4.4: "199 for the trimmed-bar checks (Table S7 and the trimmed gap in Section 5.4) and the 30-minute block-length checks of Tables S6 and S15"; and in the Table S6 note add "499 replicates at the daily and 199 at the 30-minute frequency."
- **n2 Sec. 5.4, third paragraph: scope of the trimmed gap.** "(0.107 [0.094, 0.127] at M30)" is the gap without the opening bar (R23), but now follows "without the auction bars". Fix: "(0.107 [0.094, 0.127] at M30 without the opening bar)".
- **n3 Sec. 2.4 citation contexts.** Chen et al. (2021): "liquidity of small firms is fragile" → "small-firm liquidity fell after a market surveillance system was introduced (Chen et al. 2021)". Bui et al. (2022): "sector connectedness of 60–90%" → "sector connectedness above 60%, near 90% during COVID-19 (Bui et al. 2022)".
- **n4 Sec. 6.3: limitations shortened.** Add after "...cannot be bounded without constituent data": "so the three-pair gap is descriptive for these pairs"; and after "one exchange and three indices": "so the magnitudes should not be generalized beyond the HOSE".
- **n5 Sec. 4.4: pre-specification of the scale grid dropped.** "... first exceeds 0.05, a tolerance fixed in advance" → "... first exceeds 0.05; the grid and tolerance were fixed in advance" (keeps letter B7 true).
- **n6 Sec. 5.5: 2021 variant lost its interval and day count.** "adding 2021 as a crisis changes neither result (FR p = 0.987; Δβ = −0.005)" → "adding 2021 as a crisis (789 days) changes neither result (FR p = 0.987; Δβ = −0.005 [−0.122, 0.124])" (R37). Keeps letter B9 true.
- **L-a to L-e, L-g** response-letter wording/locations (Section 4 above). L-f resolves with N1.

### Advisory (not counted)
- C5 block-length detail, C9 "factor of about two" (the ranges span about 2.6–2.9), B12 OMML and the byte-identical rerun not verified from Markdown.
- Word count: main text Sec. 1–7 is 6,603 words (prose plus captions and table notes; table rows, references and declarations excluded); abstract 213 words.

## 7. Verdict

**FAIL** (Stage 4.5, final-check, re-verification round) — 0 CRITICAL, 1 MAJOR (N1), 12 MINOR (n1–n6; L-a–L-e, L-g); AI failure-mode checklist: all 7 modes CLEAR (the Mode 6 block of 09 is cleared).

All 09 issues (M1, M2, m1, m2/m8, m4–m7, m9, r1–r3, L1–L8) are resolved; the Section 6.3/6.4 merge makes L5 moot. The condensation kept every table, equation, decision rule, outcome, citation and cross-reference, and dropped only details listed in Section 2; it introduced one wrong sentence (N1) and a few weakened qualifications. N1 is a one-clause text fix in r2_text.py (no R rerun). After N1 is fixed and manuscript_anonymized.md / the DOCX are regenerated, re-verifying that sentence only should give **PASS WITH NOTES**; applying n1–n6 and the letter fixes as well should give **PASS**.

Coverage: Phase C covered 100% of prose numbers in the abstract and Sections 1–7 (about 190) plus 37 table cells; tables were confirmed byte-identical to the version fully checked in 09. Phase E covered all hypothesis rules and outcomes and every verbal claim changed by condensation. Phase A/B: full in-text ↔ list cross-match (67/67) and re-reading of every citation context the condensation changed; the three fixed entries checked against 09's recommended text; the other entries were not re-searched (unchanged since 08/09). Phase D (originality) was not in the requested scope. A PASS would not certify the research as correct beyond these registered populations.
