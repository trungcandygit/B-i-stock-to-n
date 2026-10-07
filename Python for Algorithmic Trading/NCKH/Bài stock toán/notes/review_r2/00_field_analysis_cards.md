# Field Analysis Report (Phase 0, field_analyst_agent)

Skill: ARS `academic-paper-reviewer`, Phase 0. Input: `project_R/docx_build/r2/manuscript_anonymized.md` (anonymized round-2 manuscript). Prior review notes were not read, so this configuration is independent of earlier rounds.

**Target context:** no author-confirmed Review Target Context was supplied, so **`criteria_binding_unavailable`** applies. The dispatch describes a class of venue: a Q1/Q2 international journal in empirical finance or financial econometrics that also accepts econophysics methods (the class that includes *International Review of Financial Analysis*, *Finance Research Letters*, *Physica A*, *Pacific-Basin Finance Journal*). The panel is configured at that field-general level. No reviewer may claim alignment with a specific venue's criteria, scope statement or word limit, and no venue criteria are reconstructed from memory.

**Instruction-data boundary check:** the manuscript contains no text addressed to reviewers or to the panel (nothing about leniency, reviewer identity, the decision, or what to ignore). Nothing to report.

## Paper Basic Information
- **Title**: The Mechanical Floor of Nested Index Correlations: An Exact Multiscale Decomposition with Evidence from Vietnam
- **Abstract length**: about 235 words (unstructured; one paragraph)
- **Full text length**: about 8,800 words from Introduction to Conclusion, excluding the abstract, Appendix A (Tables A1–A5), declarations and references; about 11,200 words in the full file
- **Number of references**: 46
- **Exhibits**: 8 main tables, 4 figures, 5 appendix tables; 1 proposition with proof and 3 corollaries; 5 pre-stated hypotheses (H1–H5)
- **Language**: English. The review should be conducted in English.

## Field Analysis

| Dimension | Analysis Result |
|-----------|----------------|
| Primary Discipline | Empirical finance / financial econometrics. Topic: measuring co-movement between equity indices, diversification across size tiers, and portfolio risk |
| Secondary Disciplines | (1) Econophysics / statistical physics of finance (DCCA, DMCA, MF-DCCA, fluctuation-function scaling); (2) Emerging and frontier-market finance and market microstructure (HOSE price limits, T+2, call auctions, short-sale ban, Epps effect); (3) Index construction and benchmark methodology / risk-model practice |
| Research Paradigm | Quantitative. One deductive analytical result (an exact algebraic identity, Proposition 1) plus confirmatory hypothesis testing (H1–H5 with pre-stated decision rules) |
| Methodology Type | Statistical modeling. Scale-wise DCCA, DMCA and MF-DCCA estimation; Monte Carlo reliability calibration (Gaussian and GARCH-t); stationary block bootstrap inference with Holm/BH multiplicity control; Forbes–Rigobon heteroskedasticity adjustment; closed-form portfolio-variance error; robustness checks. Single-market observational time-series study (case design: one exchange, three nested indices, four sampling frequencies, 2014–2025) |
| Target Journal Tier | `criteria_binding_unavailable`; no specific venue is configured. Field-general observation: the paper is pitched at the Q1/Q2 level of applied financial econometrics and econophysics journals. It has a clean exact result, fully specified inference, multiplicity control, power reporting and reproducible R code. The limits on tier are the single-market scope and the risk that the core identity reads as an accounting tautology, because the proxy M is constructed from A and B. Whether the identity's *empirical content* (the size of the floor and the low sensitivity) is a contribution of Q1 strength is the central question for the panel |
| Paper Maturity | **Pre-submission** (late revision). Rationale: the IMRaD structure is complete, with hypotheses, a decision rule for each hypothesis and a summary table (Table 8). Every table has notes and a source line. References are formatted consistently with DOIs. Online Resource, ethics, data/code availability, AI-use and COI statements are present. The prose is polished, uses hedged claims and reports null results (H3, H4) honestly. Remaining work is substantive: positioning against the "accounting identity" objection, proxy validation, and single-market generalizability. No structural rebuild is needed |

## Candidate Journal Classes (field-general; not a venue-fit claim)

Under `criteria_binding_unavailable`, this section names classes of outlet, not a specific journal. It does not assess fit against any one venue's criteria.

1. **Applied financial-econometrics / international-finance journals that publish multiscale and contagion work** (the IRFA / FRL class). This matches the H4/H5 framing and the risk-management implications. A letters-format outlet would need the paper cut to about a third of its current length.
2. **Econophysics / statistical-mechanics journals that publish DCCA methodology** (the Physica A class). Proposition 1 is a general property of DCCA-type coefficients for nested series, and much of the reference base sits here.
3. **Asia-Pacific regional finance journals** (the Pacific-Basin Finance Journal class). These value the HOSE institutional detail, the short-sale ban and the cross-market implications (SET50/SET100, IDX30/LQ45).

## Reviewer Configuration Cards

This paper is cross-disciplinary across three areas: financial econometrics, econophysics and emerging-market finance/index practice. Coverage strategy: R1 owns the statistical and estimator validity (DCCA plus econometric inference). R2 owns the finance literature, theory and contribution claims, including the Vietnam institutional setting. R3 owns the practitioner side: index-methodology and risk-model practice, plus generalizability. The Journal-Fit Reviewer owns originality, significance and readership at the field-general level. The fixed Devil's Advocate (fifth seat, no card) attacks the strongest claims.

### Reviewer Configuration Card #1

**Role**: EIC
**Display role**: Journal-Fit Reviewer
**Identity Description**: Senior editor at the field-general level (no venue bound; `criteria_binding_unavailable`) with long handling experience at Q1/Q2 journals where empirical finance meets econophysics. Has handled many DCCA/MF-DCCA, connectedness and COVID-contagion submissions. Knows the common desk-reject pattern: "new multiscale method applied to market X" with no economic question behind it.
**Review Focus**:
  1. Originality and significance of the core claim. Does Proposition 1, an exact identity that holds for Pearson correlation as a special case, give finance readers an insight they lack? Or is it a known property of the correlation between a portfolio and one of its sub-portfolios, recast in DCCA notation? Does the paper state honestly that its novelty is the *quantification and inference* of the floor rather than the algebra?
  2. Readership and framing. Is the paper written for finance readers (diversification, risk models, benchmark design) or for econophysics readers (scale-wise coefficients)? Are Title, Abstract, Introduction and contribution statements consistent with that choice? Do the three listed contributions survive given that two of five hypotheses are not supported?
  3. Scope and length. Do single-market evidence (one exchange, three indices, one decomposed pair) and roughly 8,800 words plus 5 appendix tables match a full-length Q1/Q2 article? Which material (the MF-DCCA section, the statistical proxies P~heur~/P~ratio~/P~res~) is peripheral and could move to an online appendix?
**Will particularly care about**: Whether the paper's "headline" (floor ≈ 0.90 of the VN30–VN100 coefficient) is an informative empirical finding or a direct arithmetic consequence of a 68% weight that a reader could compute from the factsheet without DCCA. Also whether the abstract oversells relative to Section 6.3.
**Possible blind spots**: Will not verify the proof algebra, the bootstrap mechanics or the reliability calibration in detail, and will defer to R1. May underweight the Vietnamese institutional detail and the practitioner value of a ready-to-use correction formula.

### Reviewer Configuration Card #2

**Role**: Peer Reviewer 1
**Display role**: Peer Reviewer 1 (Methodology)
**Identity Description**: Financial time-series econometrician who specializes in the statistical properties of scale-dependent correlation estimators (DCCA/DMCA coefficients, wavelet correlations) and in resampling inference for dependent data (stationary and moving-block bootstrap, multiple-testing control). Has published on finite-sample bias and the asymptotic distribution of ρ~DCCA~ under heavy tails and volatility clustering. Particularly focuses on whether constructed regressors and constructed series contaminate inference.
**Review Focus**:
  1. Proposition 1 and the constructed proxy. Check the proof: bilinearity, the two-sided box scheme, and the role of F~M~ > 0. Then assess what is *estimated* and what is *identity*. M is built as (B − wA)/(1 − w), so κ(s), ρ~AM~(s), the floor and the "mechanical share" are all functions of A, B and a fixed w. Are the bootstrap intervals for these quantities meaningful? Is the H2 threshold of 0.5 a non-trivial test, or is it guaranteed once w ≈ 0.68? Assess also the log-return vs arithmetic-weight approximation (the Jensen term) and the weight-drift leakage in Eq. (10). Does Table A2 bound the drift bias adequately when the w path is unobserved?
  2. Inference design. Check the stationary block bootstrap with a mean block of about 20 *trading days*: how this translates into bars at M30/H1/H4, and whether intraday seasonality (opening and closing auction bars) and overnight gaps are respected. Check the p-value formula, the B = 499 replications for tail p-values, percentile vs studentized intervals, and whether inference over averages across the reliable range handles cross-scale dependence. Check the 19-test multiplicity family for H3 and whether scale ranges are pre-specified.
  3. Estimator calibration and regime tests. Is the reliability threshold s~rel~ (white-noise and GARCH-t calibration, 0.05 worst-case MAE) a defensible cut-off, and does it matter that the nested coefficients are near one, where the estimator's sampling behavior differs? Are the Forbes–Rigobon conditions met for P~cap~–VN30? P~cap~ contains −w/(1 − w)·A by construction, so exogeneity of VN30 and the constant-β assumption need checking. Check ex post regime definitions, power computation, the Eq. (13) relative-error derivation, the MF-DCCA absolute-value choice and the surrogate count (100).
**Will particularly care about**: Whether bootstrap intervals around quantities that are deterministic functions of a constructed series overstate how much is learned. Also whether the "reliable-range average" and the scale grid are fixed before seeing results, so the reported intervals are not conditional on researcher choices.
**Possible blind spots**: May treat the identity's algebraic triviality as fatal without weighing its economic usefulness. May not engage with the finance literature on index-membership co-movement or with the HOSE institutional features that drive the Epps-effect interpretation.

### Reviewer Configuration Card #3

**Role**: Peer Reviewer 2
**Display role**: Peer Reviewer 2 (Domain)
**Identity Description**: Senior empirical asset-pricing researcher who works on return co-movement and contagion: the index-membership / habitat co-movement literature (Barberis–Shleifer–Wurgler line, index-inclusion effects), the Forbes–Rigobon interdependence-vs-contagion debate, and size-tier and segment integration in Asian emerging and frontier markets, including Vietnam and ASEAN.
**Review Focus**:
  1. Literature positioning and gap claim. Is the claimed gap ("no study separates the mechanical component of correlations between overlapping indices") accurate? Check the literature on portfolio–sub-portfolio correlation, part–whole correlation, and the "spurious correlation of ratios/sums" tradition. Check benchmark-overlap and active-share/holdings-overlap measures in fund research, and factor-mimicking or orthogonalized size portfolios (SMB-type long–short constructions), which already remove overlap. Is the Table 1 comparison fair, and is the 2021–2026 search window adequate for a claim of exactness and novelty?
  2. Theoretical interpretation of findings. Does the paper's economic reading hold? Purged correlation of about 0.89 is "high economic co-movement". Absence of contagion is "interdependence". Weak intraday slopes are the "Epps effect" vs Hong–Stein diffusion. Do herding, the ±7% price limits, margin-call cascades and foreign-ownership limits (absent from the institutional section) offer alternative explanations? Is the mid-cap shadow benchmark economically interpretable when it implies a 315% long / 215% short position?
  3. Contribution to the field and Vietnamese evidence. Do the results change how finance researchers measure diversification across size tiers, beyond the HOSE? Is the institutional background (SSC rules, Decree 155/2020, Circulars 120/2020 and 68/2024, VN30 futures) accurate and relevant? Are Vietnamese studies (Chen et al. 2021; Nguyen et al. 2023; Bui et al. 2022; Tran and Tran 2025; Le et al. 2025) used analytically or only listed? Is the absence of a published-VNMIDCAP validation a serious gap?
**Will particularly care about**: Whether the paper engages with the closest finance precedents for removing mechanical overlap, such as orthogonalized or long–short size factors and holdings-overlap measures, so that the novelty claim does not rest on searching only the DCCA/econophysics literature.
**Possible blind spots**: May not check the proof, bootstrap block lengths or reliability calibration in detail. May be unfamiliar with the econophysics conventions (DCCA reliability ranges, MF-DCCA surrogates) and judge them by econometrics norms alone.

### Reviewer Configuration Card #4

**Role**: Peer Reviewer 3
**Display role**: Peer Reviewer 3 (Cross-disciplinary / Practical)
**Identity Description**: Index-methodology and quantitative risk-model specialist from industry, now partly in academia. Has designed size-segment indices and multi-factor equity risk models (covariance estimation, factor-exposure attribution, stress-testing) for asset managers and index providers in Asian emerging markets. Particularly focuses on whether an academic correction changes a decision that practitioners actually make.
**Review Focus**:
  1. Practitioner novelty and decision relevance. Do risk managers actually feed index-level (nested) correlations into diversification decisions, or do production risk models already work from holdings and constituent-level covariance, where overlap is handled automatically? Is the "static correlation misstates mid-cap variance by −2.1% to +9.4%" result (H5) large relative to ordinary covariance estimation error and to regime-switching or EWMA practice? Does it hold out of sample, given that regimes are classified ex post?
  2. Index-design and policy implications. Are the recommendations sound and actionable for exchange and index-provider policy (Section 6.2)? These cover standalone non-overlapping segment benchmarks, a VNMIDCAP fund and mid-cap futures. How do free-float vs full-market-cap weighting (VN100 vs VNINDEX), semi-annual reviews, sector caps and foreign-ownership-limit adjustments affect the floor? Is the reported w = 0.6826 from a single 31 May 2024 factsheet adequate for practice?
  3. Transferability and broader assumptions. Does the identity transfer to other nested architectures: SET50/SET100, IDX30/LQ45, S&P 500/Russell 1000, MSCI EM/MSCI Asia ex-Japan, sector-in-market and country-in-region indices? Could the authors give a simple cross-market table of floors computed from published weights alone? Does the vendor data source (TradingView export, not exchange-certified) and its licensing, which blocks data sharing, limit replication and practical uptake?
**Will particularly care about**: Whether a practitioner gains anything from the DCCA machinery beyond the Pearson version, given that the Pearson floor (0.903) and share (0.914) almost equal the DCCA values. Also whether the paper's single most useful deliverable, a weight-and-volatility formula for the floor, is presented prominently enough to be used.
**Possible blind spots**: May undervalue the scale-by-scale (multiscale) contribution and the econophysics audience. May judge the statistical inference by industry conventions rather than academic rigor, and may not assess the literature-gap claim in depth.

## Non-overlap Check of Review Focus

| Seat | Owns | Explicitly defers |
|---|---|---|
| Journal-Fit Reviewer (EIC) | Originality, significance, readership, scope/length, contribution framing | Proof, inference mechanics → R1; literature detail → R2 |
| R1 Methodology | Proof validity, constructed-series inference, bootstrap design, reliability calibration, Forbes–Rigobon identification, MF-DCCA technique | Literature novelty → R2; practitioner relevance → R3 |
| R2 Domain | Gap claim vs finance precedents, economic interpretation, institutional accuracy, Vietnam/ASEAN literature | Estimator properties → R1; industry practice → R3 |
| R3 Practical | Decision relevance in risk models, index-design policy, cross-market transferability, data-source practicality | Statistical rigor → R1; academic literature → R2 |

## Review Strategy Recommendations
- **Central tension the panel should test from different angles:** "exact identity" vs "empirical contribution". M is constructed from A and B, so Proposition 1 holds by construction. Its value lies in (a) the closed-form floor and sensitivity, (b) the measured size of the floor in a real nested system, and (c) the purged correlation. R1 tests whether inference on these quantities is informative. R2 tests whether the finance literature already contains the insight. R3 tests whether it changes practice. The EIC weighs the sum. The Devil's Advocate should target the H2 test, whose 0.5 threshold may be trivially exceeded given w ≈ 0.68, and the claim that the floor is something "the identity itself holds for any nested pair" can tell readers without the data.
- **Two hypotheses are not supported (H3 after adjustment, H4).** Reviewers should check that the Abstract, contributions and Conclusion describe these nulls accurately and do not lean on unadjusted H3 patterns. Reviewers should not penalize honest null reporting.
- **Proxy validity is a shared fault line.** The single factsheet weight, the log-return approximation, weight drift and the missing check against the published VNMIDCAP all bear on R1 (bias), R2 (interpretation) and R3 (practice). The synthesizer should merge these comments into one consolidated request rather than counting it three times.
- **Expected complementarity and conflict:** R1 and R3 may disagree on whether the DCCA layer adds anything over Pearson. R1 may value the scale-wise inference; R3 may see the Pearson floor as sufficient. R2 and the EIC may disagree on venue class: finance framing vs an econophysics outlet. The synthesizer should state these tensions explicitly and not average them away.
- **Register:** pre-submission maturity, so reviewers should use a standard rigorous peer-review register (not developmental). Under `criteria_binding_unavailable`, the recommendation must be evidence-based against general Q1/Q2 field standards, not against any one journal's criteria.
- **Seat count:** these four cards plus the fixed Devil's Advocate make five execution seats. No fifth card is issued, and the DA is not dynamically configured.
