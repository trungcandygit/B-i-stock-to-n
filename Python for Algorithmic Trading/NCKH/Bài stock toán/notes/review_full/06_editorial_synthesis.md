# Editorial Decision — Round 1 (academic-paper-reviewer, `full` mode)

**Manuscript:** Nested Equity Index Correlations Overstate True Co-Movement: Evidence from Vietnam
**Target venue:** Asia-Pacific Financial Markets (Springer). **Contract:** `reviewer/reviewer_full/v2`, panel_size 5.
**Criteria binding:** `criteria_binding_unavailable` (all five cards disclose it; no venue-alignment claim is made).
**Calibration:** `NOT_CALIBRATED`.

## Sprint-contract arithmetic (mechanical)

Step 1 — role-scoped matrix (assessed eligible seats only):

| Dimension | Priority | Eligible seats (score) | Verdict |
|---|---|---|---|
| D1 methodology_rigor | mandatory | methodology (block, repairable) | block |
| D2 domain_accuracy | mandatory | domain (warn) | warn |
| D3 argumentative_coherence | mandatory | da (block, repairable); methodology (warn) | block |
| D4 cross_disciplinary_relevance | high | perspective (warn) | warn |
| D5 writing_and_structure | normal | eic (warn) | warn |
| D6 venue_fit_and_contribution | mandatory | eic (warn) | warn |

Step 2 — failure conditions: F1 (fatal block) not fired; F2 (mandatory block) fired on D1 and D3; F3 (two or more mandatory dimensions warn or worse, majority per dimension) fired on D1, D2, D3, D6; F4 (high-priority block) not fired; F5 (any warn or worse) fired; F0 not fired.

Step 3 — precedence: F2 (severity 90) selected.

dimension_verdicts: [D1=block, D2=warn, D3=block, D4=warn, D5=warn, D6=warn]
fired_conditions: [F2, F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision

## Decision letter (synthesised only from the five cards; no new comments)

The panel finds the research question well posed and in scope for the journal: nested index correlations conflate constituent overlap with economic co-movement, and the paper documents this with a transparent, reproducible R pipeline whose tabulated numbers the methodology seat verified against the outputs (methodology S4). The honest downgrading of weak results and the careful restriction of the Forbes–Rigobon test to the disjoint pair are strengths noted by several seats (methodology S2, S5; perspective S4; eic strengths).

The decision is **major revision** because two mandatory dimensions carry repairable blocks:

1. **Inference (D1, methodology W1, W3, W4, W7; domain W2).** Significance statements rely on procedures that do not hold here: HAC regressions across 30 overlapping scale points, a Forbes–Rigobon standard error with nominal day counts, a scale-20 DCCA coefficient on concatenated non-contiguous regime days, and no sampling uncertainty for the headline gap.
2. **Claims exceed evidence (D3, DA M1, M4, M6; methodology W2, W13).** The abstract says the nested correlations "primarily reflect" shared capitalization although the purged correlation is still 0.88; horizon strengthening is generalised to "intraday frequencies" although it appears only at M30 (and is negative at 1D in the reliable range); and non-rejection of the Forbes–Rigobon null is read as proof of no contagion.

Corroborated concerns (two or more seats): the single-snapshot weight and the absence of a VNMIDCAP comparison (methodology W6, domain W1, perspective W3, DA M2–M3); the 15.6% headline drawn from a non-investable portfolio, the exaggerating regime definition, and a mixed-estimator comparison (methodology W5, perspective W1–W2, eic W3, DA M5); and ASEAN-wide recommendations from single-market evidence (eic W1, perspective W5, DA M7).

Reviewer disagreement: eic W5 recommends "Springer Basic" reference style; the journal's own author instructions (supplied with the submission) show an APA-like reference list and name–year citations, which the manuscript already follows. The editor sides with the journal instructions (REVIEWER_DISAGREE recorded in the roadmap).

## Revision Roadmap (immutable core; author triage recorded separately)

| ID | Source | Severity | Obligation | Item |
|---|---|---|---|---|
| RR1 | methodology W1, W2 | Major | required | Replace HAC-over-scales inference with resampling (block bootstrap of the bivariate returns, recomputing the whole DCCA curve); report the scaling slopes for all four frequencies and both ranges with CIs; restate horizon dependence as M30-specific. |
| RR2 | methodology W3, W4, W13; domain W2; DA M4 | Major | required | Re-specify the Forbes–Rigobon test with Pearson regime correlations and a Pearson-consistent δ; bootstrap ρ*−ρ_low within regimes; report CI and power; interpret non-rejection as absence of evidence. |
| RR3 | methodology W7 | Major | required | Add bootstrap CIs for the Table 2 averages and the overlap gap. |
| RR4 | methodology W5; perspective W1, W2; eic W3; DA M5 | Major | required | Recompute portfolio variance errors with one estimator and regime-specific volatilities, with CIs; drop or qualify the 15.6% headline; state that regimes are classified ex post and that P_cap is a factor exposure, not a holdable portfolio. |
| RR5 | methodology W6; domain W1; perspective W3; DA M2, M3 | Major | required | Validate against VNMIDCAP or reconstruct time-varying weights; otherwise state the limitation prominently and qualify the gap as weight-conditional. |
| RR6 | DA M1, M6, M8 | Major | required | Remove causal/overgeneralised wording in abstract, contributions and conclusion; soften the practitioner-behaviour premise. |
| RR7 | eic W1; perspective W5; DA M7 | Major | required | Restrict ASEAN statements to hypotheses for markets with similar nested architectures. |
| RR8 | domain W3; eic W2 | Major/Minor | required | Soften the "unaddressed" gap claim (authors' constraint: no new references). |
| RR9 | methodology W8; domain W6 | Minor | recommended | Remove the unused Podobnik t-test and its misattributed distribution. |
| RR10 | methodology W9 | Minor | recommended | Re-check reliability thresholds under heavy-tailed, volatility-clustered surrogates. |
| RR11 | methodology W10; domain W8 | Minor | recommended | Add surrogate benchmark for multifractal widths, soften the ranking, rename Δh as the generalized-exponent range. |
| RR12 | methodology W11 | Minor | recommended | Clarify that no index prices were filled (the "filled" file forward-fills only the unused exchange-rate column). |
| RR13 | methodology W12 | Minor | recommended | Provide the code as an Online Resource / public repository. |
| RR14 | domain W4, W5, W7, W16 | Minor | recommended | Correct citation attributions (Hong–Stein, Epps scope, Oświęcimka, Peng/Kantelhardt for DFA). |
| RR15 | domain W9–W15, W17; perspective W4, W6, W7 | Minor | recommended | Fact and framing precision (settlement history, VNINDEX weighting, price-band wording, Le et al., ETF wording, 2018 window, derivative claim, horizon units). |
| RR16 | eic W4, W6, W7–W11 | Minor | recommended | Presentation: funding pointer, subset relation, redundant RSS/IDSS passage, equation numbering, heading/roadmap consistency. |
| RR17 | eic W5 | Minor | REVIEWER_DISAGREE | Keep the journal-instruction reference style (see decision letter). |
| RR18 | domain W12 | Minor | recommended | Market-classification status: no change unless verifiable within the allowed sources. |
