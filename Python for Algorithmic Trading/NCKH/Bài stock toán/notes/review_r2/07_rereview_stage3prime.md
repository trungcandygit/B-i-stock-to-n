# Stage 3' Re-Review (Verification Review), Round 2 to Round 3

Skill: ARS `academic-paper-reviewer`, mode `re-review` (three-gate evidence-before-persuasion discipline). Date: 2026-10-10.
Verifier: independent fresh-context agent. `notes/AUDIT_LEDGER.md` was **not** read.

## 0. Run disclosure

- **Gate order followed.** Phase 1: acceptance criteria for RR-1..RR-30 were committed from `06_editorial_synthesis.md` Part 2 before the revised text was opened. Phase 2A: verdicts were drafted from the revised manuscript, the Supplementary Material, the R outputs and the figures. The response letter was not open at that point. Phase 2B: `response_to_reviewers.md` was then read as untrusted author persuasion. Every verdict that changed after reading the letter is listed in §4 with its basis.
- **Contract machinery.** No hash-bound manifest, no author-adjudication sidecar and no revision-evidence bundle were supplied, so `scripts/check_re_review_synthesis.py` could not be run. The outcome below applies the closed decision rules (G/B steps) by hand. Flag: `[CHECKER-NOT-RUN: inputs absent]`.
- **Yardstick.** The frozen round-2 roadmap was used. Field analysis was not re-run. Routing: each item was verified under its round-2 source seat's persona (R1 for methodology items, R2 for literature and institutional items, and so on). A single model family performed every verification.
- **Calibration:** `NOT_CALIBRATED`. **Provenance artifact:** missing. Single verifier, so there is no independence claim.
- **Instruction-data boundary.** No text addressed to the verifier was found in the manuscript, the supplement or the letter.

## 1. Decision

**Minor Revision** (rule B5). No must_fix item is NOT_ADDRESSED or MADE_WORSE. Three must_fix items are PARTIALLY_ADDRESSED, each with a should_fix residual (RR-13, RR-14, RR-15). should_fix_addressed_rate = 6/6 = 100%. Every new issue from the revision is minor in severity. No DA CRITICAL exists in either round. `reject_recommended: false`.

The paper's core is sound and much improved. The lemma and all five corollaries check out algebraically. The novelty claim is correctly scoped, the "floor" error is gone, H2 has become an estimand, and inference now carries weight uncertainty. The remaining problems are about consistency between the stated decision rules and the verdicts reported, plus a few robustness results that are reported only in part.

## 2. Traceability matrix (RR-1..RR-30)

Counts: **FULLY_ADDRESSED 17**, **PARTIALLY_ADDRESSED 12**, **DECLINED-with-adequate-reason 1**, NOT_ADDRESSED 0, MADE_WORSE 0.
- must_fix (P0): 6 fully, 3 partially.
- should_fix (P1): 4 fully, 2 partially.
- consider (P2): 7 fully, 7 partially, 1 declined.

| RR | P | Verdict | Evidence (revised manuscript) | Residual gap / note |
|---|---|---|---|---|
| RR-1 | P0 | FULLY | Abstract: "We carry the classical part–whole correlation identity over…"; §4.2: "The lemma is therefore an adaptation, not a new identity"; §2.1 cites Pearson 1897, Cureton 1966, Cremers & Petajisto 2009, Barberis et al. 2005; Table 1 row "Pearson (1897); Cureton (1966) … Yes (static)"; search strings in §2.6 | Search window is still "2021–2026, plus the classical sources these works cite" (backward citation chasing only). Acceptable. |
| RR-2 | P0 | FULLY | §5.3: "κ lies between 0.47 and 0.52 … Box 1 is sufficient for practice"; §1 contribution 2; abstract "its Pearson version suffices in these data" | Title keeps "Scale-Wise". This describes the method and makes no result promise, so it is acceptable. |
| RR-3 | P0 | FULLY | §2.7 Estimands: "A share above one half is not a finding: it holds whenever κ < √3"; Corollary 4 "F~M~/F~A~ < … = 3.73" (R33: 3.7252); no share hypothesis in Table 9; decision rules stated in §2.7 before results | — |
| RR-4 | P0 | FULLY | §1: "If such a number is read as a measure of how mid caps move with large caps…"; "Holdings-based risk models avoid the problem"; Chen et al. 2016; §6.2: "If index-level correlations … are used…, they should first be decomposed… Holdings-based risk models are not affected." | Conditional route taken. |
| RR-5 | P1 | PARTIAL | MF-DCCA moved to Fig. S1; proxies to Table S8; full-range slopes to Table S1 | Criterion asks for word counts before and after. Neither the paper nor the letter gives them. Residual: consider. |
| RR-6 | P1 | FULLY | Fig. 4 contour (R17); §6.3 partial-overlap condition; §6.3 states why the broad-market pairs are not decomposed (full-cap vs free-float); cross-market table omitted "because we could not verify the weights" | One wording error in §6.3 (new issue N8). |
| RR-7 | P2 | PARTIAL | Fig. 3 zoomed to [0.80, 1] with dotted bound; Fig. 1 notes explain the lines and the unshaded 2021/2025 spikes; Table S12 | Criterion: the Fig. 1 footnote should cite the R output showing Table 7 is unchanged with 2021 included. No such check is reported (R27 only documents the spikes). |
| RR-8 | P2 | FULLY | Abstract has two quantities (0.11, 0.10), no intervals, and a closing takeaway sentence | — |
| RR-9 | P2 | PARTIAL | §3.2 names the HOSE public closes; README gives SHA-256 checksums of both inputs | Data-availability statement still reads only "available from the corresponding author upon reasonable request". The vendor-vs-exchange check was not done (disclosed). |
| RR-10 | P2 | PARTIAL | Letter: "addressed in the language rounds" | Not itemized. Stray subscript commas remain: Box 1 "σ~A,~ σ~B~" and §4.6 "σ²~ε,~". VN30 covered warrants are not mentioned in §3.1. Abstract lacks the "known weights, common weighting scheme" qualifier (it is only in §6.3). The criterion requires each item to be changed or explained. |
| RR-11 | P0 | FULLY | Corollary 1: "ρ̲ bounds ρ~AB~ from below only when ρ~AM~ ≥ 0"; Eq. (9) √(1−κ²) at ρ~AM~ = −κ; "for κ ≥ 1 no positive lower bound exists"; Table 5 bound column (R16); 0 occurrences of "floor" (previous version: 41) | Math verified (§3). |
| RR-12 | P1 | FULLY | §2.7 H1 margin 0.05 with decision rule; §5.2 "Corollary 3 fixes the sign … but not its size"; Table 4 like-for-like column (R15 `gap_like`) | The margin is a statistical tolerance relabelled as an economic margin and was set after the round-1 results (disclosed in §2.7). Consider. |
| RR-13 | P0 | PARTIAL → residual should_fix | §4.3 w ~ U(0.60, 0.75) inside the bootstrap; Table 5 Panel B (R21); Table S2 grid with κ, ρ~AM~, ρ̲, share, sensitivity, Shapley; Eq. (12) disjointness condition; ρ~AM~ labelled "overlap-purged" (§4.2, §6.4) | (i) The H1 headline intervals (Table 4) are at the factsheet weight only. Panel B covers only 1D and M30 and has no gap row. (ii) The U(0.60, 0.75) range has no empirical basis; it is not tied to any observed weight history. (iii) The infeasibility reason, "neither was available from our data source at all frequencies", rules out only multi-frequency validation. A daily validation against the published VNMIDCAP close or the FUEDCMID NAV is not shown to be infeasible. |
| RR-14 | P0 | PARTIAL → residual should_fix | §4.4 studentized p, two families, TOST margin 0.001; Table 6 (R22); §2.7 labels the revision-stage rules | (d) No broad-vs-nested slope-difference test within one bootstrap. The letter says it is "reported through Eq. (14) and the TOST", but that is not a contrast test. **The Table 9 H2 verdict does not follow the stated rule** (new issue N1). |
| RR-15 | P0 | PARTIAL → residual should_fix | Table S7 (R23) removes the first bar; Table S6 (R24) gives M30 block lengths for the gap; §3.1 bar schedule (R32) | The closing-auction bar is not removed (the criterion says "first and last bars"). The block-length sensitivity covers the gap only, not the slopes, and H1 is not covered. Trimmed slopes have no CIs or p-values. The result weakens H2 (N2) and has not been carried into the H2 verdict. |
| RR-16 | P0 | FULLY | §2.5/§4.6 cite Corsetti et al. 2005 and Rigobon 2003 and state the constant-β/σ²~ε~ assumption; Table 7 adds the factor model with Δβ and the residual-variance ratio (R29); VN30-quartile regimes; weight grid in Table S10 (R25); causal wording gone | The DCCA-row exclusion reason appears only in the letter. Put one sentence in §4.6. The H3 verdict label also conflicts with its rule (N1). |
| RR-17 | P2 | PARTIAL | §4.7: "Intervals resample the full sample jointly" (R31) | The purged-vs-nested \|RE\| difference with an interval is not reported. The "at most 2.35%" for nested pairs (R31, VN30–VNINDEX, VNINDEX-quartile calm) has no table in the paper or the supplement. |
| RR-18 | P2 | DECLINED (adequate in part) + PARTIAL | §5.1 GARCH-t averages (R6) | The extended grid (ρ₀ = 0.95, 0.98) was declined because "no conclusion depends on the cut-off". That is weak, since the observed coefficients are about 0.99, above the top of the grid (0.9). No slopes over the GARCH-t range. No tolerance rationale beyond "fixed before". |
| RR-19 | P2 | PARTIAL | §4.4 states percentile inversion and min p = 0.004 | No p-value cap at 1 (the letter's "cap at ±1" refers to intervals). The re-centred FR convention is not contrasted. Table 6 prints "0.004" although §4.4 says such values are reported "as p < 0.005". |
| RR-20 | P2 | PARTIAL | §5.7 "a check on the detrending method, not an independent test"; Table S5 has CIs and Gaussian-copula excess (R26) | Table S4 (DMCA) still has no bootstrap intervals. |
| RR-21 | P2 | FULLY | §4.5 Eq. (14); §5.4 implied vs observed slope within 0.8 × 10⁻⁵ (R30 max 0.84 × 10⁻⁵); no "predicts zero slope" | The claim that the κ channel "partly offsets" the ρ~AM~ channel holds only at M30 and H1. At 1D and H4 both channels are negative (R30). |
| RR-22 | P1 | FULLY | Corollary 5 with three conventions; sensitivity leads the abstract and §7; "accounts for"/"nine-tenths" removed | — |
| RR-23 | P2 | FULLY | §2.4 Lo & MacKinlay 1990, Hou 2007; Table S9 lead–lag (R28) | Dimson omitted with a reason (letter). |
| RR-24 | P1 | PARTIAL | §3.1 FUEDCMID "listed on the HOSE since 29 September 2022"; "cannot be shorted or hedged with a dedicated derivative"; §6.2 hedge effectiveness (R20) replaces the product recommendation | The criterion requires a **verified source** for the ETF. None is cited. |
| RR-25 | P2 | PARTIAL | §3.1 short-sale wording, Decree 245/2025, T+2 date, session schedule | T+2 date (Circular 203/2015/TT-BTC) and session hours have no primary citation. Verify the claim that Circular 120/2020 provides the covered-short-sale framework against the official text. |
| RR-26 | P2 | PARTIAL | §3.1 FOL and FTSE reclassification; §6.1 rival mechanisms; §6.4 comparative statics | **The comparative-statics sentence in §6.4 has a sign error** (N3). The FTSE reference has a title/date inconsistency and no URL (N4). |
| RR-27 | P2 | FULLY | §2.3 Greenwood 2008, Chen et al. 2016 with DOIs | — |
| RR-28 | P2 | FULLY | §6.1 uses Chen et al. 2021 and Tran & Tran 2025 (H2), Nguyen et al. 2023 and Bui et al. 2022 (loading) | Le et al. 2025 is not used again. Trivial. |
| RR-29 | P1 | FULLY | Table 8 Panel A RE/SE (R31); Panel B OOS QLIKE/DM (R18); §5.6 sign-pattern sentence; "prices the cost" removed | — |
| RR-30 | P1→P2 | FULLY | Box 1 six steps; all numbers match R33; §6.2 ill-conditioning sentence | — |

## 3. Mathematical verification (all items requested)

| Item | Check | Result |
|---|---|---|
| Eq. (7) | With F²~AB~ = wF²~A~ + (1−w)ρF~A~F~M~ and F²~B~ = w²F²~A~ + (1−w)²F²~M~ + 2w(1−w)ρF~A~F~M~, dividing by wF²~A~ gives (1+κρ)/√(1+κ²+2κρ) | Correct. Numerical identity error ≤ 4.4 × 10⁻¹⁶ (R8b) |
| Monotonicity / Eq. (10) | d/dρ = κ(D − N)/D^{3/2} = κ²(κ+ρ)/D^{3/2} | Correct. Increasing for ρ > −κ, so ρ̲ is a lower bound only for ρ~AM~ ≥ 0 |
| Eq. (9) | At ρ = −κ, N = D = 1 − κ², so ρ~AB~ = √(1−κ²). For κ > 1 the minimum on [−1, 1] is −1 (at ρ = −1) | Correct. "No positive lower bound" holds. R16 argmin = −κ |
| ∂ρ~AB~/∂κ (Eq. 14) | [ρD − N(κ+ρ)]/D^{3/2} = −κ(1−ρ²)/D^{3/2} | Correct. R30 values −0.033 to −0.035 are consistent |
| Corollary 3 | N² − ρ²D = (1−ρ²)(1+2κρ) | Correct. Nonnegative for ρ ≥ 0 (in fact for ρ ≥ −1/(2κ)) |
| Corollary 4 | Share = ρ̲/ρ~AB~ ≥ ρ̲ > ½ iff κ < √3, giving F~M~/F~A~ < √3·w/(1−w) | Correct as a sufficient condition. 3.7252 at w = 0.682615 rounds to 3.73 (R33). Calling it "guaranteed for most nested systems" is mild rhetoric |
| Shapley Eq. (11) | v(∅) = 0, v(O) = ρ̲, v(D) = ρ~AM~, v(OD) = ρ~AB~, so φ~O~ = ½[ρ̲ + ρ~AB~ − ρ~AM~] | Correct. Cross-check: ½(0.911 + 1 − 0.895) = 0.508, matching R15 |
| Box 1 | σ~M~ = √(σ²~B~ − 2wρσ~A~σ~B~ + w²σ²~A~)/(1−w) and ρ~AM~ = (ρσ~B~ − wσ~A~)/[(1−w)σ~M~] | Correct. R33 matches the direct P~cap~ moments exactly |
| Replication leverage | 1/(1−w) = 3.15, w/(1−w) = 2.15 | Correct |

**Errors found:** none in the lemma or the corollaries. One sign error in the applied comparative statics (§6.4, N3).

## 4. Phase 2B adjustments (letter read after 2A)

- RR-14(d): the letter confirms that no separate contrast was run. The verdict stays PARTIAL. The letter's stated equivalence is not accepted.
- RR-16(f): the letter's reason (too few boxes in short regimes; δ is defined on Pearson variances) is an adequate `valid_rebuttal` for leaving out the DCCA row. The item stays FULLY addressed, with a request to put that sentence in the paper.
- RR-18: the letter states that the extended grid was deliberately declined. Recorded as DECLINED. The reason is only partly adequate (see table).
- RR-10, RR-19: the letter's claims ("addressed in language rounds"; "cap at ±1") do not match the manuscript. Verdicts unchanged (PARTIAL). An assertion in the letter with no manuscript evidence changes nothing.
- RR-13: the letter repeats the infeasibility claim without new evidence. Verdict unchanged.

No silent verdict changes (G1 clean).

## 5. New issues introduced by the revision

All are attributed `regression` (they sit in content written during the revision). The severity of each is given.

- **N1 (minor, high priority). Hypothesis verdicts do not follow their own decision rules.**
  - *Location:* §2.7, §5.4, §5.5, Table 9.
  - *H2:* the rule requires "at least one pair at each intraday frequency" with Holm-adjusted p < 0.05.
    - If H4 counts as intraday (§3.1 describes H4 as session bars), the rule fails at H4 (Holm = 1.000), so the verdict is **Not supported**.
    - If H4 is excluded, the rule passes, so the verdict is **Supported**.
    - "Partially supported" is not an outcome the rule can produce.
  - *H3:* the rule is a conjunction (FR one-sided p < 0.05 **and** Δβ two-sided p < 0.05). With FR p = 0.998 the rule yields **Not supported**. "Mixed" is not a rule outcome.
  - *Fix:* (a) Define "intraday frequencies" explicitly in the H2 rule (e.g., "M30 and H1"). (b) Report the mechanical outcome in Table 9 ("Supported"/"Not supported"). (c) Put the nuance in a separate "Comment" column (e.g., H3: "Not supported by the rule; loading rises under quartile regimes, not across dated crises").

- **N2 (minor). The opening-bar robustness result weakens H2 but is reported selectively.**
  - *Location:* §5.4 last paragraph, abstract, §1 contribution 3, §7.
  - *Problem:* removing the first bar takes the H1 broad-market slopes to 0.0003 and −0.0005 (R23). The text quotes only the M30 VN30–VNINDEX slope ("0.0020, close to the full-data value"). It omits that the M30 VN100–VNINDEX slope halves (0.0022 to 0.0010). No CIs or p-values are given for the trimmed slopes.
  - *Fix:* (a) Add bootstrap CIs and studentized p for every trimmed slope (extend R23). (b) Report both M30 slopes. (c) State in Table 9 and the abstract that the intraday horizon dependence survives opening-bar removal only at M30, if that is what the p-values show. (d) Also run the closing-auction bar exclusion (RR-15).

- **N3 (minor). Sign error in the comparative statics.**
  - *Location:* §6.4: "if foreign inflows raise the weight or lower the relative volatility of large caps, Eq. (8) predicts a higher benchmark."
  - *Problem:* since κ = (1−w)σ~M~/(wσ~A~), a lower large-cap volatility σ~A~ raises κ and **lowers** ρ̲.
  - *Fix:* "if foreign inflows raise the weight of large caps or lower the volatility of the remaining constituents relative to large caps, Eq. (8) predicts a higher benchmark."

- **N4 (minor). FTSE Russell citation is internally inconsistent.**
  - *Location:* §3.1 and the reference list.
  - *Problem:* §3.1 says "announced in October 2025", but the reference title is "September 2025 interim announcement". FTSE's March reviews are the interim ones and the September cycle is the annual one, so "interim" is probably wrong. The entry has no URL.
  - *Fix:* check the title against the FTSE Russell primary document. Use the exact title and release date, add the URL, and make the month in the text match.

- **N5 (minor). The H1 robustness claim uses point estimates while the H1 rule uses interval bounds.**
  - *Location:* §5.2: "the gap stays above the margin at every weight in the grid".
  - *Problem:* at w = 0.60 the like-for-like gap is 0.063 (= 0.988 − 0.924, Table S2/R14). With a sampling SE of about 0.011 (R15), its lower 95% bound is likely below 0.05. Under the H1 rule, H1 would then fail at the low end of the grid.
  - *Fix:* (a) Add like-for-like gap rows to Table 5 Panel B (R21, w drawn in each replicate) for all four frequencies. (b) Report the H1 decision under weight uncertainty. (c) Rephrase to "the point estimate stays above 0.05 at every weight in the grid".
  - *Also:* Table S2 does not contain the gaps the text cites. The three-pair gap is in Table S3, and the like-for-like gap is not tabulated. Fix the cross-reference.

- **N6 (minor). The same statistic has two different intervals.**
  - *Location:* Table 7 vs Table S10.
  - *Problem:* the chronological FR row at the factsheet weight is −0.044 [−0.082, 0.001], p = 0.985 in Table 7 (R3) but [−0.082, −0.005], p = 0.990 in Table S10 (R25). The upper bound changes sign. Separately, the VN30-quartile row of Table 7 comes from R25 (about 999 replicates), while §4.4 states 1,999 for Pearson regime statistics.
  - *Fix:* (a) Take all Table 7 rows from a single bootstrap run with the stated B, or add a note like the one under Table S6. (b) Correct the replication count in §4.4 if needed.

- **N7 (minor). The p-value convention clashes with a CI at M30.**
  - *Location:* §5.3: "its slope on ln s is not significant (bootstrap p = 0.052–0.456)".
  - *Problem:* at M30 the 95% CI of the benchmark slope [−0.0045, −0.00002] and of the κ slope [0.00004, 0.0124] exclude zero (R15). The "+1" percentile-inversion p of 0.052 conflicts with the percentile CI.
  - *Fix:* write "not significant at the 5% level by the bootstrap p-value (0.052 at M30, where the percentile interval just excludes zero); the slope is −0.0025 per unit of ln s, economically negligible".

- **N8 (minor). Overstated transferability wording.**
  - *Location:* §6.3: "the benchmark exceeds 0.7 whenever the child holds half of the parent and the remainder is not much more volatile".
  - *Problem:* at w = 0.5 and σ~M~/σ~A~ = 1 the benchmark is 1/√2 = 0.707. Any higher relative volatility takes it below 0.7 (Fig. 4).
  - *Fix:* "is about 0.7 or more when the child holds at least half of the parent and the remainder is no more volatile than the child".

- **N9 (trivial). Small labelling and wording slips.**
  - §5.7 calls P~heur~ "volatility-scaled", but Table S8 defines it by the VN30–VN100 correlation. Use one description.
  - §6.2 hedge quartiles are VNINDEX quartiles (R20 panel B), while H3 uses VN30 quartiles. Name the sorting variable in §6.2 and Table S11.
  - §5.4 "the κ channel partly offsets the ρ~AM~ channel": add "at M30 and H1" (R30).
  - README says the superseded files 10/14/20 are omitted from `outputs/`, but they are still in the repo's `outputs/`. Remove them from the package.

No new problem rises to major or critical. No previously-missed issue would move the decision.

## 6. Number spot-check (50 numbers, all against `project_R/outputs`)

All 50 match after rounding, apart from the cross-run discrepancy in N6 and the formatting issue in RR-19 ("0.004" vs "< 0.005").

| # | Manuscript value | Location | R output | Match |
|---|---|---|---|---|
| 1–6 | VN30 1D sd 0.0121, skew −0.83, kurt 7.81, JB 3,202; P~cap~ M30 JB 887,934; VNINDEX M30 kurt 40.64 | Table 2 | 01 | ✓ |
| 7–8 | s~rel~ 50/444/233/88; GARCH-t 20/151/86/28 | Table 3 | 03_smax, R6 | ✓ |
| 9–10 | Heavy-tailed nested 0.975–0.979; purged 0.882–0.890 | §5.1 | R6 | ✓ |
| 11 | Panel B 1D: 0.977 / 0.988 / 0.884 / 0.093 | Table 4 | 02 | ✓ |
| 12 | Like-for-like 0.104 [0.085, 0.128]; H4 0.099 [0.084, 0.116] | Table 4 | R15 gap_like | ✓ |
| 13 | Cohen's q 0.83 [0.75, 0.89] … 0.79 [0.72, 0.84] | Table 4 | R10 | ✓ |
| 14–19 | κ 0.484/0.503; ρ~AM~ 0.884 [0.857, 0.906]; ρ̲ 0.900 [0.891, 0.910]; bound 0.875/0.864; sensitivity 0.106 [0.098, 0.114]; Shapley 0.508 [0.498, 0.521] | Table 5 A | R8, R16, R15 | ✓ |
| 20–21 | Panel B ρ~AM~ [0.821, 0.931]; sensitivity [0.071, 0.163]; Shapley [0.452, 0.556] | Table 5 B | R21 | ✓ |
| 22–23 | κ range 0.47–0.52 (actual 0.4736–0.5249); identity error 4.4 × 10⁻¹⁶ | §5.3, §4.2 | R8b | ✓ |
| 24–25 | Benchmark slope p 0.052–0.456, Holm 0.208–0.828; within-frequency range 0.007–0.016 | §5.3 | R15 | ✓ |
| 26 | Dependence-first share 0.895–0.900 | §5.3 | R15 econ_share | ✓ |
| 27 | Box 1: κ 0.475, ρ̲ 0.903, bound 0.880, ρ~AM~ 0.889, sensitivity 0.103, inverse 9.7, σ~M~ 0.0124 | Box 1 | R33 | ✓ |
| 28 | 3.73 | Cor. 4 | R33 (3.7252) | ✓ |
| 29–31 | Studentized p < 0.001; Holm-19 0.002; H2-family Holm 0.039/0.045; TOST 0.007/0.012/0.385/0.142 | Table 6 | R22 | ✓ |
| 32 | Smallest BH percentile p 0.057 | §5.4 | R22 p_bh | ✓ |
| 33 | All Table 7 entries (ρ, ρ*−ρ~low~, CIs, p, β, Δβ, variance ratios) | Table 7 | R3, R25, R29 | ✓ (see N6) |
| 34 | Weight-grid FR p ≥ 0.935 | §5.5 | R25 (min 0.9349) | ✓ |
| 35 | RE 2.23 [0.71, 3.98], 9.38, −1.84, −2.07; RE/SE 0.14, 1.50 | Table 8 A | R31 | ✓ |
| 36 | Nested max 2.35%, RE/SE ≤ 0.43 | §5.6 | R31 | ✓ (untabulated) |
| 37 | QLIKE values; DM p 0.069–0.179; 735 days | Table 8 B | R18 | ✓ |
| 38 | Hedge 0.79 [0.75, 0.82], 0.53 [0.45, 0.61], 0.86 | §6.2 | R20 | ✓ |
| 39 | Lead 0.084 [0.028, 0.136], 0.007, asymmetry 0.076 [0.048, 0.102] | §6.1 | R28 | ✓ |
| 40 | λ~L~ 0.75 vs 0.62 | §5.5 | R26 | ✓ |
| 41 | First bar 10%, 37%; gap 0.107 [0.094, 0.127], 0.096 [0.082, 0.112]; M30 slope 0.0020 | §5.4 | R23 | ✓ |
| 42–43 | M30 block intervals [0.084, 0.112]/[0.076, 0.119]; daily 0.070–0.119 | §5.4, §5.7 | R24, R13 | ✓ |
| 44 | DMCA purged 0.882–0.891; gap 0.086–0.096 | §5.7 | R12 | ✓ |
| 45 | Implied-observed slope difference ≤ 0.8 × 10⁻⁵ | §5.4 | R30 | ✓ |
| 46–47 | Jensen 3.6 × 10⁻⁶; volatility quartiles 10.6%/20.0%; 539/1,000 days | §4.2, §3.2 | scalars | ✓ |
| 48 | 2021: 14.3%, 32%; 2025: 18.1%, 30% | §3.2 | R27 | ✓ |
| 49 | Proxy weight 0.9865–0.9885 | §5.7 | 04 w_heur | ✓ |
| 50 | Grid gaps 0.063–0.164 (like-for-like) and 0.052–0.153 (three-pair) | §5.2 | R14 (derived), Table S3 | ✓ |

## 7. Prioritized residual-issue list

1. **N1** (§2.7, Table 9): make the H2 and H3 verdicts mechanical outcomes of the stated rules; define "intraday". Text-only fix.
2. **RR-15 / N2** (§5.4, Table S7, abstract): add CIs and p-values to the trimmed slopes; report all trimmed slopes; add closing-bar exclusion and a slope block-length sensitivity at M30/H1 (extend R23/R24); restate H2 accordingly.
3. **RR-13 / N5** (Table 5 Panel B, §5.2): add like-for-like gap rows under w ~ U(0.60, 0.75) for all four frequencies (extend R21); report H1 under weight uncertainty; give an empirical basis for the [0.60, 0.75] range, or state that it is a judgment range. Either run a daily P~cap~-vs-VNMIDCAP (or FUEDCMID NAV) validation from public daily closes, or state precisely why even daily validation is infeasible.
4. **RR-14(d)**: add a bootstrap test of the broad-market minus VN30–VN100 slope difference, computed within the same replicates (R22).
5. **N3** (§6.4): correct the comparative-statics sign (exact text in §5).
6. **RR-24 / N4**: add a verified source for the FUEDCMID listing date. Correct the FTSE Russell reference (title, date, URL) and its month in §3.1.
7. **N6** (Table 7 / S10 / §4.4): unify the bootstrap runs or note Monte Carlo differences; correct the replication count.
8. **RR-10**: remove the stray commas (Box 1 "σ~A,~"; §4.6 "σ²~ε,~"); add the covered-warrant sentence or explain its omission; list each minor item in the letter.
9. **RR-17**: add a supplementary table of R31 (all pairs and regimes, which is where 2.35% lives) and the purged-minus-nested |RE| difference with an interval.
10. **RR-19**: print "< 0.005" in place of "0.004" in Table 6; state the p ≤ 1 cap and the FR re-centring convention.
11. **RR-20**: add bootstrap CIs to Table S4.
12. **RR-7**: add a Table 7 robustness row or footnote with 2021 counted as a crisis, citing the R output.
13. **RR-9**: name the HOSE public route in the Data availability statement itself.
14. **RR-25**: cite primary sources for T+2 (Circular 203/2015/TT-BTC) and the trading schedule; check the Circular 120/2020 short-sale description.
15. **RR-5**: report main-text word counts before and after the revision.
16. **N7, N8, N9, RR-21 wording**: the one-line wording fixes given in §5.
17. **RR-16(f)**: move the DCCA-row exclusion reason into §4.6.

## 8. Decision derivation (closed rules, applied by hand)

- **G0:** manifest absent. Treated as a disclosure, not an abort, because the run is outside the contract harness.
- **G1:** no silent changes.
- **G2:** no pending states. No dissent was recorded, so no dissent bound was tripped.
- **B1–B4:** none fires.
  - No must_fix item is NOT_ADDRESSED, MADE_WORSE or CANNOT_VERIFY.
  - No residual is classed must_fix.
  - No regression is classed major or critical.
- **B5:** fires. Three must_fix items are PARTIALLY_ADDRESSED with should_fix residuals, and the regressions are minor. Result: **Minor Revision**.
- **Floors:** no escalation exception.

**Final: Minor Revision.** Items 1–6 of §7 must be done before resubmission. Items 7–17 are cheap and should be done in the same pass.
