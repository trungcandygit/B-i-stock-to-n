# Stage 2.5 integrity re-verification after fixes (numbers, code, citations)

- Verifier: integrity_verification_agent, independent re-check. No ledger, roadmap or response file was read. The only earlier material read was the two previous reports (`integrity_2p5_numbers.md`, `integrity_2p5_citations.md`).
- Inputs: `project_R/docx_build/r2/manuscript_with_authors.md` (955 lines, 46 references); `project_R/outputs/*.csv`, `scalars.txt`, `figures/`; `run_all.R`, `run_revision.R`, `run_round2.R`.
- Scratch files: `/tmp/claude-0/verify2/` only. No project file was modified.
- Date: 2026-10-07

## Verdict: PASS (no CRITICAL or MAJOR issue remains)

- The CRITICAL bootstrap bug is fixed in code. The regenerated `R2_bootstrap_dcca.csv` gap intervals are identical to the corrected values the first verifier computed independently in a separate rerun. Table 4 and Section 5.3 now quote them exactly.
- The new `p_boot` column in R9 uses the (k+1)/(B+1) convention. Holm and BH are recomputed from it. Under the adjusted p-values no slope test survives either Holm or BH, and every part of the manuscript reflects this: Section 5.5, Table 6, Table A1, Table 8, the Abstract, Section 6.1 and the Conclusion. The H3 decision follows from these adjusted p-values: "not supported after adjustment".
- All earlier MAJOR items are fixed. Six MINOR or cosmetic items remain, none blocking (Section 3).
- 7-mode failure checklist: no mode is SUSPECTED and no Mode 1/3/5/6 is INSUFFICIENT EVIDENCE, so there is no block.

---

## 1. Focus checks

### (1) Bootstrap gap bug fix

- `run_revision.R` l.76 now reads `nested <- colMeans(bs["avg_rel", 1:3, ]); gap <- nested - bs["avg_rel", 4, ]`.
  - `bs` has dimension stats × pairs × B, so `bs["avg_rel", 1:3, ]` is a 3 × B matrix and `colMeans` returns a vector of length B.
  - Pair 4 is `Pcap-VN30` (`PAIRS_MAIN`, l.59).
  - The subtraction therefore pairs replicate b with replicate b. **Correct.**
- `R2_bootstrap_dcca.csv`, rows `nested_mean-minus-Pcap`:

| Freq. | Gap | Interval (CSV) | Table 4 Panel B | Earlier verifier's corrected rerun |
|---|---|---|---|---|
| 1D | 0.0930 | [0.0742, 0.1147] | 0.093 [0.074, 0.115] | [0.074, 0.115] |
| M30 | 0.0962 | [0.0801, 0.1193] | 0.096 [0.080, 0.119] | [0.080, 0.119] |
| H1 | 0.0863 | [0.0707, 0.1032] | 0.086 [0.071, 0.103] | [0.071, 0.103] |
| H4 | 0.0868 | [0.0723, 0.1033] | 0.087 [0.072, 0.103] | [0.072, 0.103] |

- Boot SE at 1D is now 0.0104, consistent with the corrected value. The earlier buggy value was 0.0152.
- Section 5.3 reads "bootstrap intervals between 0.071 and 0.119", which matches.
- Table A5 (`R13`) matches in every cell, and Section 5.9 ("within 0.070 to 0.119") matches.
- `run_all.R` now chains `run_revision.R` and `run_round2.R` through `system2` (l.254–257). The claim that "a single script reproduces every table and figure" is therefore true.

### (2) `p_boot` and H3

- `run_round2.R` l.120 computes `p_boot = min(1, 2(k+1)/(B+1))`, recovering k from the stored `p_two_sided = 2·min(k)/B`.
  - This equals the Section 4.4 formula 2 min{k₋+1, k₊+1}/(B+1).
  - Holm and BH are applied to `p_boot` within each range (19 tests).
- Recomputing by hand from the CSV for the reliable range:
  - Smallest p = 0.004 (VN100–VNINDEX M30). Holm 0.004 × 19 = 0.076.
  - Next three p = 0.012. BH min 0.012 × 19/4 = 0.057.
  - So 0 tests survive Holm and 0 survive BH. The CSV agrees.
- Every manuscript location agrees:
  - **Table 6:** all 7 rows match R9 for slope, CI, p, Holm and BH (0.012/0.216/0.057; 0.004/0.076/0.057; 0.980/1.000/0.980; 0.520/1.000/0.894; 0.080/1.000/0.217; 0.076/1.000/0.217; 0.080/1.000/0.217).
  - **Table A1:** all 9 rows match, including BH 0.894/0.057/0.828/0.899. Table A1 now includes VN100–VNINDEX at H1 (earlier item M15).
  - **Section 5.5:** "4 percentile intervals exclude zero … unadjusted p 0.004–0.012 … BH 0 (smallest 0.057) … Holm 0 … H3 is therefore not supported once multiple testing is accounted for." Matches.
  - **Table 8 H3:** "4 of 19 unadjusted CIs > 0; 0 BH- and 0 Holm-significant; Not supported after adjustment." Matches.
  - **Abstract:** "small positive horizon slopes at intraday frequencies that do not survive multiple-testing adjustment". Matches.
  - **Section 6.1:** says "weak, unadjusted". **Conclusion:** makes no horizon claim. **Introduction:** says tests are adjusted. All consistent.
  - "< 0.002" no longer appears anywhere.

---

## 2. Status of earlier items

### Numbers report (`integrity_2p5_numbers.md`)

| Item | Sev. | Status | Evidence now |
|---|---|---|---|
| M1 Table 4 gap CIs | CRITICAL | **Fixed** | See Section 1(1) |
| M2 Sec. 5.3 interval range | CRITICAL | **Fixed** | "between 0.071 and 0.119" |
| M3 Table 4 vs A5 clash | MAJOR | **Fixed** | Gap at L = 20: [0.074, 0.115] vs [0.074, 0.117]. The residual difference is Monte Carlo noise from separate draws (see N1) |
| M4 Abstract "0.91–0.91" | MAJOR | **Fixed** | "0.905–0.911 … within 0.895–0.920" |
| M5 Abstract "0.011–0.011" | MAJOR | **Fixed** | "about 0.011" |
| M6 Introduction degenerate ranges | MAJOR | **Fixed** | "0.905–0.911", "0.106–0.112" |
| M7 "9–9 times" | MINOR | **Fixed** | "about 9 times" |
| M8 Table 8 H5 | MAJOR | **Fixed** | "−2.1% to 9.4%" (R4: −2.07 … 9.38) |
| M9 Holm survival with p = 0 | MAJOR | **Fixed** | `p_boot` convention; Holm 0 and BH 0; H3 downgraded |
| M10 Detrending orders | MINOR | **Fixed** | 0.9665, 0.9663, 0.9667 |
| M11 "Kurtosis above 34" | MINOR | **Fixed** | "above 33" (min 33.94) |
| M12 h(2) range | MINOR | **Fixed** | "h_xy(2) … 0.536 and 0.542" (cross-exponent) |
| M13 2.35% scope | MINOR | **Fixed** | "the daily misstatement is at most 2.35%" |
| M14 Replication counts | MINOR | **Fixed** | "499 … DCCA-based, 1,999 … Pearson-based regime statistics" |
| M15 VN100–VNINDEX H1 untraceable | MINOR | **Fixed** | Row added to Table A1; quoted in Sec. 5.9 |
| C1 Table 1 header | MAJOR | **Fixed** | Overlap treated? / Volatility conditioning? / Main finding |
| C2 "Pinned to the floor" | MAJOR | **Fixed** | No "pinned" or "held near" left; now "bounded below by its floor" (5.5, 5.7, 6.1) |
| C3 "Rejected" vs "Not supported" | MINOR | **Fixed** | Sec. 5.6: "H4 is not supported" |
| C4 Panel A thresholds | MINOR | **Fixed** | Table 4 note: "full-sample thresholds in both panels" |
| C5 Table A2 "Slope (M30)" range | MINOR | **Not fixed** | The column is the full-range slope (`R5`/`07` baseline 0.0025 = Table 6 full range), and the note still does not say so |
| C6 Fig. 3 note | MINOR (cosmetic) | **Partly fixed** | "Dashed" still describes a `longdash` line (acceptable). The vertical line at ρ_AM = 0 (`run_round2.R` l.193) is still not mentioned |
| Byte-identical claim | MINOR | **Fixed** | Restricted to "byte-identical CSV output files". The EPS files still carry `%%CreationDate`, which is consistent with the restricted claim |
| O1 "< 0.002" | MINOR | **Fixed** | Removed |
| O2 Stale PNGs | MINOR | **Fixed** | All figures regenerated 03:21–03:26, after the CSVs |
| O3 Obsolete outputs | MINOR | **Not fixed** | `10_table4_forbes_rigobon.csv`, `14_portfolio_relative_error.csv` and `20_scale_regressions_hac.csv` are still in `outputs/` and would ship in Online Resource 1 |
| O4 `run_all.R` header title | MINOR | **Not fixed** | l.3 still has "Nested Equity Index Correlations Overstate True Co-Movement" |
| O5, O6 Tail-CI bias, regime wrap | Optional | Not addressed | Advisory only |

### Citations report (`integrity_2p5_citations.md`)

| Item | Sev. | Status | Evidence now |
|---|---|---|---|
| Le et al. (2025) pages | Correction | **Fixed** | 8(4), 535–553 |
| Chen, Zhang, Lu & Xie (2024) issue | Correction | **Fixed** | Heliyon 10(17), e36537 |
| Karim & Ning names | Correction | **Fixed** | Reference "Abdul Karim, B., & Xin Ning, H. (2013)"; in-text "(Abdul Karim and Xin Ning 2013 …)". No "Karim and Ning" remains |
| A1 Zhou et al. (2025) | MAJOR | **Fixed** | "combining MF-DCCA with transfer entropy reveals … direction of information flow among individual US stocks" |
| A2 Santana et al. (2023) | MAJOR | **Fixed** | Both results reported (no contagion WTI–Brent; contagion oil–precious metals), in the text and in the Table 1 row |
| A3 Oświęcimka et al. (2014) | MAJOR | **Fixed** | Sec. 4.8 cites Zhou (2008) for absolute covariances and cites Oświęcimka et al. as a caveat. Multifractal results are labelled descriptive with no hypothesis test |
| A4 Table 1 header | MAJOR | **Fixed** | As C1 |
| A5 Okorie & Lin wording | MINOR | **Partly fixed** | "fades over the medium and long run" is closer, but still does not say "over time", so it can be read as across horizons |
| A6 Kakinaka | MINOR | **Fixed** | Outperformance attributed to Wang et al.; Kakinaka for adaptive scale preference |
| A7 Chen et al. (2021) | MINOR | **Fixed** | "Liquidity fell after … surveillance system, especially for small firms"; Sec. 6.1 "more fragile" |
| A8 Akhtaruzzaman "do not condition" | MINOR | **Fixed** | "do not apply the Forbes–Rigobon correction"; Table 1 "No Forbes–Rigobon correction" |
| A9 Santana volatility conditioning | MINOR | **Fixed** | "No" |
| A10 Greenwood & Sammon | MINOR | **Fixed** | "the price effect of S&P 500 additions has almost disappeared" |
| A11 "Small relative to" | MINOR | **Fixed** | Phrase removed |
| Cohen (1988) | MINOR | **Fixed** | In text (Sec. 5.3, "Cohen's q (Cohen 1988)") and in the list. The DOI 10.4324/9780203771587 resolves to Routledge's digital edition of the 2nd ed. (search-confirmed). Acceptable; see N3 |
| Citation order | MINOR | **Fixed** | Chronological, e.g. "(Ge and Lin 2021; Chen et al. 2024)" |
| Podobnik / Zhou list order | MINOR | **Fixed** | Jiang (2011) before Stanley (2008); Zhou, W. (2025) before Zhou, W.-X. (2008) |
| 21 VERIFIED* DOIs | Tooling | Open (not an error) | Still needs a doi.org resolver pass |

Two-way check: there are 46 references (the earlier 45 plus Cohen 1988), and every reference is cited at least once in the body. No orphan citations were found among the citations added in this round.

---

## 3. Fresh pass: new or residual issues

| # | Sev. | Location | Issue | Suggested fix |
|---|---|---|---|---|
| N1 | MINOR | Table 4 (1D) vs Table A5 (L = 20) | The two rows describe the same statistic at the same block length but print different intervals: [0.074, 0.115] vs [0.074, 0.117]. They come from separate RNG streams (`R2` in `run_revision.R`, `R13` in `run_round2.R`). The A5 note says "Table 4, Panel B, 1D", so a reader expects identical numbers | Add "separate bootstrap draws; differences reflect Monte Carlo error" to the A5 note, or reuse the R2 draw for L = 20 |
| N2 | MINOR | Table A2 note | Same as C5: "Slope (M30)" is the full-range slope | Add "full-range slope of Eq. (11)" to the note |
| N3 | INFO | Reference Cohen (1988) | The publisher and year (Lawrence Erlbaum 1988) are paired with the Routledge 2013 e-book DOI | Acceptable. Alternatively drop the DOI, or cite "Routledge, 2013 reprint" |
| N4 | MINOR | `outputs/` (O3) | Obsolete CSVs contradict reported results | Delete them or rename `superseded_*` before packaging Online Resource 1 |
| N5 | MINOR | `run_all.R` l.3 (O4) | Old title | Update the header |
| N6 | MINOR | Sec. 2.1 and Table 1, Okorie & Lin (A5) | Ambiguity between calendar time and timescale | "that diminishes over time in the medium and long run" |

### Fresh numeric scan (all matched R after rounding)

- **Abstract:** 0.905–0.911 [0.895–0.920] (R8 `mech_share`); about 0.011 (= 0.10 × 0.106–0.112); 0.086–0.096 with intervals excluding 0 (R2); −2.1% / +9.4% (R4 −2.07 / 9.38).
- **Introduction:**
  - 0.988 daily: R8 `rho_nested` 1D = 0.9876; Pearson 0.9885.
  - "About two-thirds": w = 0.6826.
  - 0.905–0.911 and 0.106–0.112 (R8).
  - 0.086–0.096 (R2).
  - "About 0.89": P_cap 0.883–0.890.
- **Table 4:** Panel B nested means 0.977/0.979/0.975/0.976 (e.g. 1D (0.9665 + 0.9876 + 0.9759)/3 = 0.9767). P_cap 0.884/0.883/0.889/0.890. Cohen's q 0.83 [0.75, 0.89], 0.89 [0.83, 0.94], 0.78 [0.70, 0.83], 0.79 [0.72, 0.84] (R10).
- **Table 5:** all 28 cells match `R8_overlap_decomposition.csv` (κ, ρ_AM, ρ_AB, floor, share, sensitivity and floor − ρ_AM, with CIs).
- **Section 5.4:**
  - κ 0.48–0.50; floor 0.893–0.900; share 0.905–0.911 [0.895, 0.920]; excess 0.010–0.016 with CIs containing 0; sensitivity 0.106–0.112.
  - "About 9 times" (8.9–9.4).
  - Pearson floor 0.903 and share 0.914 (R8d 1D).
  - Non-overlapping share 32% (1 − 0.6826).
- **Section 5.7:**
  - 2.23 (0.91–3.94), 9.38 (6.20–13.46), −1.84 (0.95–2.63), −2.07 (1.25–2.84).
  - Daily nested maximum 2.35% (R4 B/VN30–VNINDEX low = 2.354).
  - "221% to 706%" = δ 2.21 / 7.06 (Table 7).
- **Section 5.9:**
  - Table A1 H1 values 0.0024 [0.0006, 0.0041] and 0.0019 [0.0007, 0.0032] (R9).
  - A2 gap ≥ 0.052 (R5).
  - A3 purged 0.882–0.891, gap 0.086–0.096 (as tabulated).
  - A4 0.75 vs 0.90.
  - A5 0.070–0.119 (R13).
  - Detrending 0.9665/0.9663/0.9667.
- **Table A2:** ρ_low/ρ_high match the Pearson columns of R5 (0.899/0.952, 0.871/0.937, 0.847/0.924, 0.812/0.904, 0.775/0.881). Means, gaps and slopes match.
- **Table 7 and Sec. 5.6:** unchanged from the earlier PASS.
- **Conclusion:** "about nine-tenths" (0.905–0.911); "about 0.09" (0.086–0.096). No horizon or contagion overclaim.

---

## 4. AI research failure-mode checklist (7 modes)

| Mode | Status | Evidence |
|---|---|---|
| 1. Implementation bugs | **PASS** | The gap array bug is fixed (l.76). The CSV equals an independent corrected rerun, and the SE is consistent. `p_boot` reconstruction is algebraically correct. Holm/BH are applied within the 19-test family. Pair order is verified |
| 2. Hallucinated results | PASS | Every number checked in the abstract, introduction, Tables 4–8, A1–A5 and Sections 5.3–5.9 traces to an R output cell |
| 3. Shortcut reliance | PASS | The p-value resolution issue is resolved by the (k+1)/(B+1) convention. Inference resamples the data, never scales |
| 4. Bug-as-insight | PASS | No result rests on the former bug. "Excludes zero" survives the fix |
| 5. Methodology fabrication | PASS | Every Section 4 procedure is present in the code. Replication counts are now stated correctly. `run_all.R` drives both revision scripts |
| 6. Frame-lock | PASS (note unchanged) | The identity is an accounting identity, as the manuscript states. Its empirical content depends on proxy validity, which is addressed through Table A2, DMCA, Pearson and tail checks |
| 7. Overclaiming | PASS | "Pinned" wording removed. H3 downgraded to "not supported after adjustment" and labelled "weak" in 6.1. H4 power is reported |

Block status: **no block.** No mode is SUSPECTED, and Modes 1/3/5/6 have sufficient evidence.

## 5. Recommended before Stage 3 (non-blocking)

Fix N1, N2/C5, N4/O3, N5/O4 and N6/A5. Clarifying the C6 figure note is optional. Run a doi.org resolver pass for the 21 VERIFIED* DOIs when network access allows.
