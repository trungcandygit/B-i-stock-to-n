contract_role: perspective

## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: warn
trigger: "no out-of-sample or benchmark check of economic magnitude"

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

### Perspective Review Report (Peer Reviewer 3)

**Reviewer identity.** Index-methodology and quantitative risk-model specialist (size-segment index design, multi-factor equity risk models, covariance estimation and stress testing for asset managers and index providers in Asian emerging markets). I review from the practitioner side. I do not judge the proof, the bootstrap design or the completeness of the literature, which belong to other seats. I may undervalue the econophysics audience's interest in the scale-by-scale layer.

**Overall recommendation (seat-level, advisory to the synthesizer):** Major Revision.

**Confidence score:** 4 (I know index construction and production risk-model practice well; I am less placed to judge the econophysics novelty of the DCCA layer).

**Calibration status:** `NOT_CALIBRATED`

**Criterion binding:** `criteria_binding_unavailable`. No venue criteria were supplied, so this card makes no venue-alignment claim.

### Criterion-Bound Judgements

| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| D4 cross_disciplinary_relevance | Sprint contract reviewer/reviewer_full/v2, D4 (high priority); Phase 1 scoring plan | PARTLY_MEETS | See W1 to W6 and S1 to S4 | The identity is general and readable, and the authors are candid about limits. The practitioner claims (risk-model premise, materiality of H5, policy products, transferability) are directionally sound but not demonstrated. The added value of DCCA over Pearson is left implicit. | Practitioner judgement; I did not re-run any analysis. The sampling-error figure in W3 is my own back-of-envelope calculation from Table 2 kurtosis, not a manuscript result. | yes: drives the D4 warn |

### Summary Assessment

The paper makes a point that practitioners should hear and often get wrong. When a child index is a large part of its parent, the correlation between the two is mostly arithmetic, so it says little about how the rest of the parent moves with the child. Proposition 1 turns this into a closed form: the floor depends only on the child weight and a relative-amplitude ratio. On the HOSE it puts about nine-tenths of the VN30–VN100 coefficient down to construction. The candid limitations section (one market, ex post regimes, single factsheet weight) is a strength.

From a risk desk or index committee, though, the decision value is less than the framing suggests. (i) The practitioner premise, that risk models feed index-level nested correlations into diversification decisions, is asserted and not documented. Holdings-based factor risk models handle overlap automatically. (ii) The multiscale layer adds almost nothing a practitioner can act on, because the Pearson floor and share almost equal the DCCA values and horizon slopes do not survive adjustment. (iii) The portfolio-variance misstatement (H5) is small next to ordinary covariance sampling error. It is in-sample and ex post, and it is benchmarked only against a static correlation, not against EWMA or DCC practice. (iv) The policy recommendations (VNMIDCAP fund, mid-cap futures) do not follow from any reported result. (v) Transferability is asserted but not shown, although the floor formula makes a cross-market table cheap to produce. Each of these can be fixed without new data sources, which is why I recommend major rather than minor revision but see no fatal problem.

### S1: A general, closed-form diagnostic that covers Pearson as a special case
Proposition 1 and Eqs. (8)–(9) give practitioners a two-input diagnostic (child weight and relative volatility). Because it nests the Pearson case, it can be applied without any DCCA software, and it applies to any nested benchmark family. This is the paper's most transferable deliverable.
**Evidence Anchor**: text: §4.2 "it holds for the Pearson correlation (no detrending, one box)"

### S2: Honest scoping of practical claims
The authors say that the portfolio results need out-of-sample validation before they guide practice. This keeps the practitioner implications from overreaching in the limitations section, even though Section 6.2 and the Conclusion are less careful (W3, W5).
**Evidence Anchor**: text: §6.3 "an out-of-sample evaluation of regime-conditioned risk budgets is needed before the portfolio results can guide practice"

### S3: A useful null for stress-testing practice
The Forbes–Rigobon conditioned result (no cross-tier contagion, with power reported) tells stress testers that crisis correlation rises between Vietnamese size tiers are mostly what volatility scaling predicts. A stress scenario that scales volatilities and keeps conditional dependence fixed is therefore a defensible first approximation. The reported power of 0.41 under the quartile definition is a fair warning against over-reading.
**Evidence Anchor**: table: Table 7, columns ρ* − ρ~low~ and Power

### S4: Reproducibility affordance for practitioners
A single deterministic R script that reproduces every output lowers the cost of applying the diagnostic to another market's indices.
**Evidence Anchor**: text: §4.9 "rerunning it yields byte-identical CSV output files"

### W1: The DCCA machinery adds little decision value over the Pearson special case, and the paper does not say so in its framing
The title and contributions present an "exact multiscale decomposition". The paper's own numbers show that for a practitioner the multiscale layer changes nothing. The daily Pearson floor (0.903) and share (0.914) almost equal the DCCA values (0.893–0.900; 0.905–0.911). The VN30–VN100 slope is zero. Broad-market slopes imply a rise of about 0.01 and do not survive Holm/BH. As a check, the Pearson floor follows from Table 2 alone: with w = 0.6826, σ~Pcap~ = 0.0124 and σ~VN30~ = 0.0121, κ ≈ 0.477 and the floor ≈ 0.903. This is my arithmetic, and it agrees with the reported value. So a risk manager needs only a factsheet weight and two volatilities. The finding that the floor is scale-invariant (κ(s) nearly constant across scales and frequencies) does have practical content: the choice of return horizon in a risk model does not change the diagnosis. The paper never states this as a result.
**Fix:** Lead Section 4.2 or 6.2 with the Pearson/covariance version as the practitioner tool. Then present the DCCA layer as evidence that the floor is invariant to horizon and sampling frequency, and state that invariance explicitly as a finding (for example, one sentence plus the range of κ across scales). Consider moderating "multiscale" in the title, or justify it by showing a case where the scale dimension changes the floor.
**Severity**: Major | **Evidence Anchor**: text: §5.4 "The same identity applied to full-sample Pearson correlations of daily returns gives a floor of 0.903 and a mechanical share of 0.914" | **Confidence**: 4 — practitioner use of risk-model inputs; the econophysics value of scale-wise results is outside my core competence

### W2: The practitioner premise is asserted, not documented
The motivating claim is that risk models, allocation rules and stress tests use a single index-level correlation between nested indices. It is supported only by Markowitz (1952), which documents nothing about current practice. In production, the major holdings-based multi-factor risk models compute portfolio risk from constituent exposures, where overlap is netted automatically. Nested index-level correlations are used mainly in strategic asset allocation by consultants and plan sponsors, in benchmark and ETF selection, and in simple VaR proxies for fund-of-index portfolios. If the authors do not name who makes the error, the practical contribution reads as correcting a mistake nobody makes. Naming those users would make it much sharper.
**Fix:** Name the user groups that actually feed nested index correlations into decisions (asset-allocation inputs, regulatory or simplified VaR proxies, ETF/benchmark comparison tools, local fund-management practice in Vietnam). Give documentary evidence where possible, such as published capital-market assumption tables or regulatory proxy rules. State plainly that holdings-based factor models are not affected. One paragraph in the Introduction and one sentence in Section 6.2 would suffice.
**Severity**: Major | **Evidence Anchor**: text: §1 "Risk models, allocation rules and stress tests typically summarize the dependence between such indices with a single Pearson correlation of daily returns (Markowitz 1952)" | **Confidence**: 4 — direct experience with production risk-model inputs

### W3: Portfolio-variance results (H5) lack a materiality benchmark and an out-of-sample test
H5 is "supported" because the intervals exclude zero, but significance is not materiality. The misstatements are +2.2% (calm), +9.4% (low-volatility quartile) and −1.8% to −2.1% (turbulent) in variance, or roughly half that in volatility. For comparison, by my own back-of-envelope calculation (not a manuscript result), the relative sampling standard error of a daily variance estimate with kurtosis about 8 is roughly sqrt((kurtosis − 1)/N): about 11% for the 539 crisis days and 8% for the 1,000 calm days. So the turbulent-regime understatement, which is the case that matters for risk limits, is well inside ordinary estimation noise. Second, the regimes are ex post, and the quartile regimes are sorted on the realized volatility of an index that contains the mid caps. A practitioner cannot know the regime in advance. Third, the comparator is a static full-sample correlation. Current practice uses EWMA (RiskMetrics-style) or DCC correlations, which already adapt to regimes. The Abstract and Conclusion present the misstatement without these qualifiers. The qualification appears only in Section 6.3.
**Fix:** (a) Add a materiality benchmark: report the variance misstatement next to the sampling error of the regime variance itself, or next to the misstatement from a one-year rolling estimate. (b) Add a simple out-of-sample check with existing data: estimate on 2014–2022, then evaluate 2023–2025 (which includes the April 2025 tariff shock already in the sample). Compare static, EWMA (λ = 0.94) and regime-conditioned correlations by realized-versus-forecast portfolio variance (for example, a bias statistic or QLIKE loss). (c) Rephrase H5 in the Abstract and Conclusion as an in-sample magnitude, and carry the Section 6.3 caveat forward. No result values should be presumed; if EWMA removes the effect, that is itself a useful practitioner finding.
**Severity**: Major | **Evidence Anchor**: text: §5.7 "a static correlation overstates the variance of an equally weighted VN30 and P~cap~ position by 2.23%" | **Confidence**: 4 — standard covariance-forecast evaluation practice; my sampling-error figure is approximate

### W4: Transferability of Proposition 1 is asserted but not demonstrated, though it is cheap to demonstrate
Section 6.2 says the identity "applies directly" to SET50/SET100 and IDX30/LQ45 but that the floor "must be estimated". Yet the floor depends only on w and κ, and κ needs only the child weight and the volatility ratio of child and remainder, all available from public factsheets and index histories. A practitioner would most value a short cross-market table or a nomogram, because it makes the paper useful outside Vietnam. Natural cases: SET50/SET100, IDX30/LQ45, S&P 500/Russell 1000, a top-10 heavyweight inside a cap-weighted market index, and a country inside a regional index such as China in MSCI EM. The proposition also does not cover partial overlap between non-nested indices (for example, two vendors' indices on the same universe, or style indices sharing constituents), which is common in benchmark selection. The paper should say so as a boundary condition.
**Fix:** Add (a) a figure or table of the floor as a function of w and the volatility ratio σ~M~/σ~A~, a two-parameter contour usable without data. Add (b) a small table of approximate floors for two or three other nested systems computed from published weights and public return histories, clearly labeled as illustrative. If (b) is infeasible, make (a) the deliverable and state the partial-overlap boundary. Also state that the VN100-in-VNINDEX weight is published and could extend the decomposition to the broad-market pairs.
**Severity**: Major | **Evidence Anchor**: text: §6.2 "the identity applies directly, but the size of the floor depends on their weights and volatilities and must be estimated" | **Confidence**: 4 — index-construction practice; I did not verify weights for other markets

### W5: Index-provider and exchange recommendations are not supported by any reported result
The recommendation for "standalone non-overlapping segment benchmarks" plus a VNMIDCAP fund and mid-cap futures is not tied to evidence. First, a non-overlapping VNMIDCAP benchmark already exists (Section 3.2 says VN100 adds the VNMIDCAP constituents). The issue is product availability, not benchmark design. Second, the paper's own purged correlation of about 0.89 with VN30 implies that VN30 futures already hedge roughly 79% of mid-cap variance (R² ≈ 0.89²). The case for a mid-cap future therefore rests on the remaining 21% and on basis risk. The paper could quantify this but does not. Third, demand, liquidity and market-maker feasibility under the short-sale ban and foreign-ownership limits are not discussed. A recommendation to an exchange needs at least a hedge-effectiveness argument.
**Fix:** Either drop the product recommendation, or support it with a hedge-effectiveness calculation from existing outputs: the residual variance of a mid-cap exposure hedged with VN30 futures versus a hypothetical mid-cap future, using the purged correlation and its regime variation from Table 7. Also correct the wording so that it says the benchmark exists and the gap is investable products and hedging instruments. Keep the "hidden overlap" language for blends of parent and child indices, where it applies.
**Severity**: Major | **Evidence Anchor**: text: §6.2 "standalone non-overlapping segment benchmarks, such as an investable VNMIDCAP fund or mid-cap index futures alongside the existing VN30 futures" | **Confidence**: 3 — exchange product design practice; I have not verified current Vietnamese mid-cap ETF availability

### W6: Adjacent-field readers will recognise the identity as a part–whole correlation, and the paper does not connect to that tradition
Statisticians and psychometricians will read Eq. (7) as the correlation between a part and a whole that contains it. Psychometrics corrects item–total correlations for exactly this self-inclusion. In finance, the inflation of a heavyweight stock's beta and correlation with an index that contains it is a known practitioner issue in concentrated markets. Without this connection, readers from those fields may treat the closed form as a rediscovery, which weakens the novelty claim, whose real content is the scale-wise extension and the measured size of the floor. This is a framing issue for adjacent-field readers. Literature coverage belongs to the domain seat.
**Fix:** Add two or three sentences in Section 2.2 or 4.2 that place Proposition 1 as the time-series, detrended and scale-wise generalisation of the part–whole (self-inclusion) correlation. Cite the classical sources after verifying them. Search leads, all [UNVERIFIED] and phrased as leads, not citations: Pearson (1897) on spurious correlation of indices; the psychometric "corrected item–total correlation" literature (for example, Cureton, Psychometrika, 1960s); practitioner notes on heavyweight-stock beta bias in concentrated index markets. Then restate the contribution as what the classical result lacks: scale-wise exactness, a sensitivity formula, and empirical magnitudes.
**Severity**: Major | **Evidence Anchor**: absence: Sections 2.1–2.4 and reference list — expected any statistics or psychometrics part–whole or item–total correlation source; checked §2.1–§2.4, Table 1, §4.2 discussion, full reference list | **Confidence**: 3 — I know the concept across fields; exact classical citations need verification

### W7: The most useful deliverable is not presented as a usable recipe
The floor formula is the paper's most portable output, but it appears in the methodology text without a worked recipe. Section 6.2 also says Eq. (7) "shows how to recover the economic correlation". In practice, κ needs F~M~, which needs the remainder series, and with that series in hand one can compute ρ~AM~ directly. The real practical use is the floor as a quick diagnostic that needs no estimation.
**Fix:** Add a boxed "practitioner recipe" (three steps: take w from the factsheet, compute the volatility ratio, read the floor and sensitivity), with the VN30–VN100 daily numbers as the worked example. Reword the 6.2 sentence so that the floor is the diagnostic and the purged series gives the economic correlation directly.
**Severity**: Minor | **Evidence Anchor**: text: §4.2 "so they can be computed for any nested pair whose child weight and fluctuation functions are known" | **Confidence**: 4 — practitioner usability

### W8: Figures are hard for practitioners to read at the decision-relevant range
Fig. 3 spans −0.5 to 1 on both axes, so all observed points sit in one corner and the four frequency lines overlap. The informative region, an economic correlation of 0.7–1 and a nested coefficient of 0.85–1, takes up a few percent of the panel. Fig. 2 uses grayscale lines whose overlapping bootstrap bands make the three nested pairs hard to tell apart. In Fig. 1 the dashed and dotted percentile lines have no legend, so the reader depends on the notes, and the large 2021 and 2025 volatility spikes are unshaded without comment, which invites questions about the regime definition. Fig. 4 (MF-DCCA) has no decision use and per Section 5.8 changes no conclusion.
**Fix:** Fig. 3: add a zoomed inset or restrict the axes, and consider replacing it with the floor contour in w and the volatility ratio proposed in W4. Fig. 2: add direct line labels or a lighter band for the purged pair only. Fig. 1: label the percentile lines in the legend and annotate the unshaded 2021 and 2025 spikes. Move Fig. 4 to the Appendix or Online Resource.
**Severity**: Minor | **Evidence Anchor**: figure: Fig. 3, full axis range −0.5 to 1 with observed markers clustered near (0.88, 0.99) | **Confidence**: 4 — exhibit design for practitioner audiences

### W9: Data provenance and a single weight snapshot limit uptake
Practitioners and index committees work from exchange-certified data and periodic weight files. A vendor export that cannot be redistributed, together with one factsheet weight, makes the results hard to audit. HOSE publishes periodic factsheets, so the weight path from 2014 to 2025 could be reconstructed at least semi-annually. Table A2 shows that conclusions survive w in [0.60, 0.75], but a practitioner wants the actual path.
**Fix:** Report the weight path from available semi-annual factsheets, even partially, and re-estimate the floor under it. State whether the TradingView series match the exchange's published closing levels on a sample of dates. Point users to an official data source for replication. This consolidates with the proxy-validity point that other seats may raise.
**Severity**: Minor | **Evidence Anchor**: text: Data availability "available from the corresponding author upon reasonable request" | **Confidence**: 3 — data-governance practice; I did not check vendor licensing terms

### W10: Market-structure changes that move the floor are not discussed
The floor depends on w and on relative volatility, and both move with structural events. Examples are foreign-ownership-limit adjustments to investable weights, changes to free-float and capping rules at reviews, and a prospective reclassification of Vietnam by global index providers that would bring passive foreign flows concentrated in large caps. A practitioner wants to know in which direction the floor moves under such events, which follows directly from Eq. (8) and the sign of ∂ρ̲/∂κ.
**Fix:** Add a short paragraph in Section 6.2 on how the floor responds to changes in w and in relative volatility. Name the institutional events that move them (reviews, foreign-ownership limits, capping, passive inflows), as comparative statics only, with no new estimation. Any statement about index reclassification status must be verified before inclusion [UNVERIFIED].
**Severity**: Minor | **Evidence Anchor**: absence: Sections 3.1 and 6.2 — expected discussion of how index rules and foreign-ownership limits shift w and the floor; checked §3.1, §3.2, §4.3, §6.2, §6.3 | **Confidence**: 3 — index-methodology practice

### Detailed Comments

#### Assumption Audit
- **Explicit assumptions**: that the parent is an exact weighted sum of child and remainder with a known, fixed w. This is reasonable for a free-float cap-weighted index between reviews. Section 4.3 handles the drift qualitatively, and W9 asks for the path.
- **Implicit assumptions**: (a) that decision-makers use nested index-level correlations (W2); (b) that statistical significance of a variance misstatement implies practical relevance (W3); (c) that a new product follows from a measurement result (W5).
- **Paradigmatic assumptions**: the static-versus-regime comparison inherits an in-sample, ex post evaluation paradigm. Risk practice is forecast-based, so the natural paradigm is out-of-sample loss comparison (W3).

#### Cross-Disciplinary Connections
- **Parallel research**: part–whole and item–total correlation correction in psychometrics and statistics; heavyweight self-inclusion in index beta estimation (W6).
- **Borrowing opportunities**: forecast-evaluation loss functions from volatility forecasting (QLIKE, bias statistics); hedge-effectiveness ratios from derivatives practice (W3, W5).
- **Methodological borrowing**: a two-parameter nomogram of the floor is a standard engineering-style presentation that would serve index committees (W4).

#### Practical Impact
- **Real-world application**: most valuable as a sanity check for allocation inputs and benchmark comparison. It does not affect holdings-based factor risk models.
- **Implementation feasibility**: the floor diagnostic is trivially implementable. The product recommendations face liquidity, short-sale and market-making constraints that are not discussed.
- **Stakeholders**: consultants and plan sponsors (allocation inputs), index providers (segment design, capping), the exchange and regulator (futures listing), foreign passive investors (weight changes). Retail investors, who dominate HOSE turnover, are the most likely to read the 0.99 correlation as diversification evidence, and the paper could say so.

#### Broader Implications
- **Ethical dimensions**: none material. Public data, no personal data.
- **Social impact**: a better-informed choice between VN30 and VN100 products for retail investors. This is modest and positive.
- **Future directions**: partial-overlap generalisation; cross-market floor atlas; out-of-sample risk-budget evaluation; effect of index reclassification on the floor.

### Cross-Disciplinary Reading Recommendations
- [UNVERIFIED] Pearson, K. (1897), on spurious correlation arising from indices (Proceedings of the Royal Society). Search lead for the part–whole and ratio-correlation origin.
- [UNVERIFIED] Psychometric literature on corrected item–total (part–whole) correlations (search lead: Cureton, Psychometrika, 1960s). Search lead for the self-inclusion correction.
- [UNVERIFIED] RiskMetrics technical documentation (J.P. Morgan/Reuters, 1996) for the EWMA correlation benchmark proposed in W3.
- [UNVERIFIED] Patton (2011, Journal of Econometrics) on robust loss functions for volatility forecast comparison, as a lead for the QLIKE evaluation in W3.

### Questions for Authors
1. Which specific decision-makers, in Vietnam or elsewhere, use index-level correlations between nested indices as diversification inputs, and can this be documented?
2. Does the regime-related variance misstatement survive against an EWMA or DCC correlation, out of sample, in 2023–2025?
3. What hedge-effectiveness gain would a mid-cap future add over VN30 futures, given the purged correlation and its regime variation?
4. Could a contour of the floor in w and the volatility ratio replace or complement Fig. 3 as the paper's practitioner deliverable?

### Minor Issues
- Section 6.2 sentence "Eq. (7) shows how to recover the economic correlation" (see W7).
- State explicitly in Section 5.7 that the "at most 2.35%" for parent–child cash blends is comparable to the 2% turbulent-regime misstatement for the mid-cap exposure, so the contrast is mainly in the calm low-volatility quartile.
- Table 5: add a one-line note explaining the practical reading of "Sensitivity" (change in the nested coefficient per 0.10 change in economic correlation, about 0.011), which the Abstract uses.
