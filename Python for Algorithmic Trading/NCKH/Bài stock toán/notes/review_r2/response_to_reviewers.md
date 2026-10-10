# Response to the Editor and Reviewers

**Manuscript:** How Much of a Nested Index Correlation Is Construction? A Scale-Wise Part–Whole Decomposition with Evidence from Vietnam

**Previous title:** Nested Equity Index Correlations Overstate True Co-Movement: Evidence from Vietnam

We thank the editor of *Asia-Pacific Financial Markets* for the earlier decision and the reviewers for their comments. The editor's decision and the reviewer comments led to a substantial revision. The revised manuscript went through an internal pre-submission review by five independent reviewers (an editor, a methodologist, a domain specialist, a practitioner and a devil's advocate). This letter answers all three sources point by point.

- **Part A** answers the earlier editorial decision.
- **Part B** answers the reviewer comments that apply to this manuscript.
- **Part C** answers the 30 items of the internal review (RR-1 to RR-30).

For every changed number we name the R output file that produces it. The file names are listed in the replication README (Online Resource 1).

The main changes are as follows.

1. The analytical result is now presented as what it is: the scale-wise, detrended adaptation of the classical part–whole correlation identity (Pearson 1897; Cureton 1966). It is no longer presented as a new identity.
2. The "floor" is now called the zero-correlation benchmark. It is a lower bound only when the purged coefficient is non-negative, and the manuscript now gives the exact lower bound √(1 − κ²).
3. The sensitivity and an order-free Shapley attribution are now the lead quantities, ahead of the earlier "nine-tenths" share.
4. Uncertainty about the index weight now enters the bootstrap.
5. Hypotheses whose outcome follows from the identity have become estimands. The four remaining hypotheses have explicit decision rules.
6. Contagion is now tested with a factor-model test that is robust to common shocks, and regimes can be sorted on VN30 volatility.
7. An out-of-sample evaluation, a practitioner recipe (Box 1) and a contour chart for other markets have been added.
8. The appendix has become a Supplementary Material document (Online Resource 2).

---

## Part A. Editor, *Asia-Pacific Financial Markets*

**A1. "The paper is essentially a statistical report … insufficient technical innovation."**

The revision answers this comment in three ways.

1. **Analytical framework.** Section 4.2 now contains:
   - Lemma 1, a scale-wise part–whole identity for detrended coefficients;
   - five corollaries: the zero-correlation benchmark, the exact lower bound √(1 − κ²), the sensitivity, the direction result, and the condition κ < √3 under which the benchmark exceeds half of the nested coefficient;
   - a Shapley attribution, Eq. (11);
   - a slope decomposition, Eq. (14), which explains why nested coefficients are flat across scales.

   We do not claim that the identity itself is new. The contribution is its scale-wise form, the inference that accounts for uncertainty in the index weight, and its use as a diagnostic that can be computed from index-level inputs (Box 1 and Fig. 4).
2. **Hypotheses.** The paper now tests four hypotheses with decision rules stated in Section 2.7: H1 a material overlap gap, H2 horizon dependence, H3 contagion, and H4 the out-of-sample value of regime conditioning. They are summarized in Table 9.
3. **Economic content.** The purged series is used to study:
   - the lead from large caps to mid caps (Section 6.1, Table S9);
   - crisis dependence with two volatility-robust tests (Table 7);
   - hedging basis risk (Section 6.2, Table S11);
   - out-of-sample variance forecasting (Table 8, Panel B).

---

## Part B. Reviewer comments that apply to this manuscript

The second report was written for a different manuscript, on Black–Litterman portfolio optimization. We applied every comment that carries over to this paper. Comments on optimization, Sharpe-ratio tests, turnover and matrix algebra do not apply, and we say so below.

| ID | Comment | Response and location |
|---|---|---|
| B1 | The title should state the contribution | The new title names the scale-wise part–whole decomposition and the question it answers. |
| B2 | The abstract lacks significance and quantification, and overstates generality | The abstract now gives two key quantities (sensitivity of about 0.11 and a purged gap of about 0.10) and one explicit takeaway, and it limits all claims to one market. Intervals are in the body (Tables 4 and 5). |
| B3 | The research gap is asserted, not demonstrated | Table 1 compares studies on overlap treatment, scale-wise measurement and volatility-robust testing. The gap in Section 2.6 is stated against named studies, and the search strategy is reported. |
| B4 | There is no theoretical bridge and there are no hypotheses | Section 2.7 separates estimands, which the identity determines, from hypotheses H1–H4, each grounded in a literature: size lead–lag, Epps (1979), Forbes–Rigobon and Corsetti et al. (2005), and forecasting. |
| B5 | The literature review is descriptive | Sections 2.1–2.5 have been rewritten as an analytical synthesis that sets out agreements, disputes and limits, for example the contested membership effect (Chen et al. 2016; Greenwood and Sammon 2025) and the bias of the Forbes–Rigobon correction. References from 2021–2026 have been added and verified. |
| B6 | Data source, survivorship and universe size | Section 3.2 now gives the vendor, codes, frequencies, sample dates and input checksums (README). Exchange-computed levels embed reconstitutions, so the data are free of survivorship bias. The three-index universe is the object of study, and Section 6.3 limits generalization accordingly. |
| B7 | Parameters chosen after seeing the results | The weight w is taken from the exchange factsheet, and the reliability tolerance and grid were fixed in advance. The decision rules for H1–H4 were set at revision and are labelled as such (Section 2.7). The original families are also reported. |
| B8 | Computational details | Section 4.8 gives the software, packages, seeds and hardware. All bootstrap replication counts are given in Section 4.4. A single script reproduces every number with byte-identical CSV files. |
| B9 | Inflated significance from dependent replications; confidence intervals, effect sizes and multiplicity | All inference resamples the data, never scales or simulations. Every estimate has a 95% interval, and the gap has Cohen's q. Holm and Benjamini–Hochberg adjustments are applied in two declared families, using studentized p-values to avoid the resolution floor of 499 replications. Equivalence is tested with TOST (Section 4.4, Table 6). |
| B10 | Interpretation, discussion, conclusions | Section 6 is organized by mechanism, implications, transferability and limits. The conclusion is limited to the HOSE and to the four hypotheses. |
| B11 | Robustness to alternative methods and risk measures | The paper reports DMCA (now presented as a check on detrending rather than an independent test), tail dependence against a Gaussian-copula benchmark, block lengths at daily and 30-minute frequencies, removal of the first bar, detrending orders 1–3, a weight grid and weight uncertainty inside the bootstrap (Section 5.7, Tables S2–S8). |
| B12 | Notation, equations, positive definiteness and numerical stability | All equations are numbered OMML objects with one symbol per object. Section 4.1 shows that \|ρ\| ≤ 1 by the Cauchy–Schwarz inequality. The identity error is at most 4.4 × 10⁻¹⁶. The ill-conditioning of the volatility-scaled proxy is documented (Table S8). |
| B13 | Verification of local references | Every reference was verified by an independent citation audit, and legal sources are cited as primary documents (Section 3.1). |
| B14 | Not applicable: transaction costs, turnover, optimization derivation, Sharpe-ratio tests, matrix dimensions | This paper has no traded strategy and no optimization problem. The portfolio results are variance statements and forecasts (Section 4.7), and all model objects are scalar series. |

---

## Part C. Internal pre-submission review (five reviewers, decision: major revision)

The table follows the order of the revision roadmap. "Output" names the R file that produces each changed number.

| Item | Change made and location | Output |
|---|---|---|
| **RR-1** Part–whole precedent | The title, abstract, Section 1 and Section 2.1 cite Pearson (1897), Cureton (1966), Cremers and Petajisto (2009) and the comparison-portfolio practice of Barberis et al. (2005). Proposition 1 is now Lemma 1, described as an adaptation. Table 1 has a precedent row. The gap and contribution 1 now concern the scale-wise form, inference under weight uncertainty and diagnostic use. The search strings are reported in Section 2.6. | – |
| **RR-2** DCCA vs Pearson | We chose remedy (b). Section 5.3 states that κ lies between 0.47 and 0.52 across all scales and frequencies, that the benchmark slope on ln s is not significant, and that the Pearson version gives the same answer to within 0.01. The title and contributions no longer promise scale-dependent content. | `R8b`, `R15` (`floor_slope`, `floor_range`), `R8d` |
| **RR-3** H2 not falsifiable | The share is now estimand E1, and the condition κ < √3 is stated as Corollary 4 (F_M/F_A < 3.73 at the HOSE weight). The share no longer appears as a hypothesis. | `R33` |
| **RR-4** Premise about practitioner use | Section 1 states the practice conditionally ("if such a number is read as …"), cites Chen et al. (2016) on misreading index-level co-movement, and states that holdings-based risk models are not affected (Sections 1 and 6.2). | – |
| **RR-5** Peripheral material | MF-DCCA (now Fig. S1), the statistical proxies (Table S8), full-range slopes (Table S1) and further robustness checks moved to Online Resource 2. The main text keeps only analyses that use or test the decomposition. | – |
| **RR-6** Transferability | Fig. 4 is a contour chart of the benchmark over w and σ_M/σ_A. Section 6.3 states the partial-overlap boundary condition and explains why the broad-market pairs are not decomposed: VNINDEX is weighted by full capitalization while VN100 is weighted by free float. A cross-market table is omitted because we could not verify the index weights; Section 6.3 says so. | `R17` |
| **RR-7** Figures | Fig. 3 is zoomed to [0.80, 1], shows the lower bound and relabels the axis as the overlap-purged coefficient. The notes to Fig. 1 explain the line types and why the 2021 and 2025 spikes are not shaded, and Table S12 documents those spikes; the quartile regimes include them. MF-DCCA was moved to Fig. S1, with a note that f(α) can be negative. Fig. 2 keeps light bands. | `R16`, `R27` |
| **RR-8** Abstract density | The abstract has two key quantities and one takeaway sentence. | `R8`, `R15` |
| **RR-9** Replication | The data statement names the HOSE as the public source of daily closes, and the README gives SHA-256 checksums of the input files. We did not compare vendor and exchange levels date by date; Section 3.2 says so. | README |
| **RR-10** Minor editorial items | These were addressed in the language rounds. Terminology now follows a single convention: "overlap-purged coefficient" and "zero-correlation benchmark". | – |
| **RR-11** Floor is not a lower bound | Corollary 1 states that ρ̲ bounds ρ_AB only for ρ_AM ≥ 0 and gives the global minimum √(1 − κ²) at ρ_AM = −κ, with no positive bound when κ ≥ 1. Table 5 reports the bound (0.864–0.875). All earlier "cannot fall below" wording has been removed. | `R16` |
| **RR-12** H1 partly mechanical | Section 5.2 cites Corollary 3 for the sign. The like-for-like VN30–VN100 gap is now primary (0.099–0.104). H1 uses a margin of 0.05 stated in advance (the estimation tolerance of Section 4.4), and the gap across weights is reported. | `R15` (`gap_like`), `R5`, `R14` |
| **RR-13** Weight uncertainty | The weight is drawn from U(0.60, 0.75) in each replicate (Table 5, Panel B), and Table S2 extends the weight grid to κ, ρ_AM, the benchmark, the share, the sensitivity and the Shapley share. Section 4.3 notes that P_cap and VN30 are disjoint only at the exact weight. Proxy validation against VNMIDCAP or the FUEDCMID NAV was not possible with our data source; Section 6.3 says so, and ρ_AM is therefore labelled "overlap-purged" rather than "economic". A weight path could not be built from a single factsheet. | `R21`, `R14` |
| **RR-14** Multiplicity | Studentized p-values remove the resolution floor. Both the original 19-test family and the eight-test H2 family are reported, and the H2 family is labelled as a revision-stage specification. TOST is applied to VN30–VN100. The difference between broad and nested slopes is reported through Eq. (14) and the TOST rather than as a separate bootstrap contrast. "Fits the Epps effect" no longer stands alone. | `R22`, `R9` |
| **RR-15** Intraday bars and block length | The first bar was removed at M30 and H1 (Table S7); part of the H1 horizon dependence comes from that bar, and Section 5.4 says so. M30 block lengths of 5 and 40 days are reported (Table S6). The bar schedule, including the 11:30–13:00 break and the two H4 bars, is stated in Section 3.1. A data-driven block-length selector was not added. | `R23`, `R24`, `R32` |
| **RR-16** Forbes–Rigobon bias | (a) Corsetti et al. (2005) and Rigobon (2003) are cited and discussed (Sections 2.5 and 4.6). (b) A factor-model test of the change in loading and residual variance has been added (Table 7). (c) VN30-quartile regimes are used, with two-sided intervals. (d) Residual variances by regime are reported. (e) The weight grid is in Table S10. (f) The DCCA-based regime test is not reported, because short regimes leave too few boxes at the reliable scales and δ is defined on Pearson variances. (g) Causal wording has been removed. H3 is assessed as mixed. | `R29`, `R25`, `R19` |
| **RR-17** ρ_st resampling | Joint resampling of the full sample now re-estimates ρ_st in each replicate (Table 8, Panel A). | `R31` |
| **RR-18** Reliability cut-off | Section 5.1 reports averages over the heavy-tailed (GARCH-t) ranges. An extended calibration grid was not added, because no conclusion depends on the cut-off. | `R6` |
| **RR-19** Bootstrap conventions | Section 4.4 states the percentile-inversion p-value, the minimum attainable value (p < 0.005 at B = 499), the cap at ±1 and the use of studentized p-values for multiplicity. | – |
| **RR-20** DMCA and tail dependence | DMCA is described as a check on detrending, because it satisfies the same identity. Table S5 reports the excess of tail dependence over a Gaussian copula with the same correlation. | `R12`, `R26` |
| **RR-21** Zero slope wrongly attributed | Eq. (14) decomposes the nested slope. The implied and observed slopes differ by less than 10⁻⁵ (Table S13). The text no longer says that the identity predicts a zero slope. | `R30` |
| **RR-22** "Accounts for" | Corollary 5 defines the benchmark-first, dependence-first and Shapley conventions. The sensitivity is the lead quantity in the abstract and conclusion, and "nine-tenths" has been removed. | `R15` |
| **RR-23** Size lead–lag | Section 2.4 now cites Lo and MacKinlay (1990) and Hou (2007). The lead–lag statistics are in Section 6.1 and Table S9. Dimson (1979) is not cited, because we could not verify it. | `R28` |
| **RR-24** Product recommendations | The FUEDCMID ETF (listed 29 September 2022) is acknowledged, and "cannot be traded" now reads "cannot be shorted or hedged with a dedicated derivative". The product recommendation was replaced by a hedge-effectiveness calculation (Section 6.2). | `R20` |
| **RR-25** Institutional facts | Section 3.1 has been corrected: T+2 since 1 January 2016; morning and afternoon sessions around the 11:30–13:00 break; covered short selling has a legal framework under Circular 120/2020 but is not in operation; Decree 155/2020 was amended by Decree 245/2025. Primary documents are cited. | – |
| **RR-26** Ownership limits, reclassification, comparative statics | Section 3.1 covers foreign ownership limits and the FTSE Russell reclassification effective 21 September 2026. Section 6.1 lists rival mechanisms (herding, limit hits, margin calls, foreign flows). Section 6.3 gives the comparative-statics prediction from Eq. (8). | – |
| **RR-27** Membership literature | Greenwood (2008) and Chen et al. (2016) are now in Section 2.3. | – |
| **RR-28** Vietnamese studies used analytically | Tran and Tran (2025) and Chen et al. (2021) inform H2 and Section 6.1. Nguyen et al. (2023) and Bui et al. (2022) are discussed as rival mechanisms for the change in loading (Section 6.1). | – |
| **RR-29** Materiality and out-of-sample performance | Table 8, Panel A reports \|RE\| relative to the standard error of the regime variance; it exceeds one standard error only in one case. Panel B gives the 2014–2022 / 2023–2025 comparison of static, EWMA (λ = 0.94) and real-time regime correlations by QLIKE with Diebold–Mariano tests; static performs best, but not significantly. The sign pattern is explained as a consequence of pooling. "Prices the cost" has been removed. | `R31`, `R18` |
| **RR-30** Practitioner recipe | Box 1 sets out six steps from index-level inputs with the daily VN30–VN100 example. Section 6.2 restates the ill-conditioning: an inverse sensitivity of about 10. | `R33` |

**Reviewer questions.** The answers are as follows.

- **EIC.** Q1 is answered under RR-4, Q2 under RR-2, Q3 under RR-1 and Q4 under RR-6.
- **R1.** Q1 is answered under RR-13, Q2 under RR-14, and Q3 and Q4 under RR-15.
- **R2.**
  - Q1 and Q2 are answered under RR-13: we could not validate P_cap against VNMIDCAP, and we report weight uncertainty instead.
  - Q3 is answered under RR-16.
  - Q4 is answered under RR-1.
  - Q5 is answered under RR-23.
- **R3.** Q1 is answered under RR-4, Q2 under RR-29, Q3 under RR-24, and Q4 under RR-6 and RR-7.

**Items declined or partially addressed.** These remain visible here:

- the weight path and the VNMIDCAP validation (RR-13 a and d);
- the cross-market table (RR-6 b);
- a data-driven block length (RR-15 b);
- an extended calibration grid (RR-18);
- the DCCA-based regime test (RR-16 f).

The reasons are given in the table above and in Section 6.3.

---

## Addendum: second internal round (verification review, decision: minor revision)

An independent verification review checked all 30 items against their acceptance criteria and recomputed 50 numbers. All of them match the R outputs. It found 17 items resolved, 12 partially resolved and none unresolved. The second-round changes are listed below.

| Residual issue | Change made | Output |
|---|---|---|
| H2 and H3 outcomes did not follow their own decision rules | The H2 rule now names M30 and H1. The H3 outcome follows its two-part rule mechanically (not supported). Table 9 has a comment column for the qualifications. | `R22`, `R29`, `R25` |
| Removing the opening bar was reported selectively, with no inference | Table S7 reports slopes with confidence intervals and studentized p-values for all bars, without the first bar and without the first and last bars, at M30 and H1. Section 5.4 states that horizon dependence disappears without the auction bars and qualifies H2 in the abstract, Section 5.4, Section 6.1 and Table 9. | `R34` |
| RR-14(d): slope difference within the same replicates | The broad-market minus VN30–VN100 slope differences are reported for every frequency and sample. They are significant at M30 and H1 on the full data and disappear without the auction bars. | `R34` |
| Block length for slopes | The M30 slope intervals are reported for 5- and 40-day blocks (Table S15). | `R35` |
| H1 not tested under weight uncertainty | The like-for-like gap with w drawn in each replicate has lower bounds of 0.057–0.061, and every replicate exceeds 0.05 (Section 5.2). The U(0.60, 0.75) range is explained in Section 4.3. A daily validation against VNMIDCAP closes would need a series that our vendor export does not include; this is stated in Section 6.3. | `R36` |
| Sign error in Section 6.3 | Corrected: a larger large-cap weight, or lower volatility of the remainder relative to large caps, raises the benchmark. | – |
| Sources for FUEDCMID, T+2 and the FTSE reference | These are now cited to the HOSE (2022) press release, VSD Decision 211/QĐ-VSD (2015) and the 7 October 2025 FTSE Russell press release. | – |
| Formatting and wording | Stray subscript commas were removed. Percentile p-values at the resolution floor are printed as "< 0.005". The M30 benchmark-slope wording is qualified. Section 6.3 now reads "no more volatile". | – |
| Untabulated numbers | Table S14 now reports the misstatement for all pairs. Table S10 notes that its draws are separate from those of Table 7. | `R31` |
| 2021 as a crisis | Adding 2021 to the chronological episodes leaves the Forbes–Rigobon and loading results unchanged (Section 5.5). | `R37` |
| DMCA intervals (RR-20) | Not added. DMCA satisfies the same identity, so it is reported as a check on detrending, not as an independent test. | – |
