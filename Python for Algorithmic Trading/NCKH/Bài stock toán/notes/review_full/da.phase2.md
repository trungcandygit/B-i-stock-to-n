contract_role: da

## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: block
trigger: "The headline conclusion does not follow from the presented evidence"
block_class: repairable

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

### Calibration Status
`NOT_CALIBRATED`

This is a seat report. The final panel topology is not known at seat time, so the report cannot be marked calibrated.

### Criterion-Bound Judgements
| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| Core thesis challenge | DA agent challenge dimension 1 (unbound run, criteria_binding_unavailable) | PARTLY_MEETS | see M1, M8 | An overstatement exists, but the abstract describes its size and its cause more strongly than the paper's own numbers allow | none identified | yes: the headline wording is involved |
| Logic chain validation | DA agent challenge dimension 4 | DOES_NOT_MEET | see M4, M6 | The paper treats non-rejection as proof and states an unidentified mechanism as fact | none identified | yes: these are claims at abstract level |
| Overgeneralisation check | DA agent challenge dimension 5 | DOES_NOT_MEET | see M6, M7 | Evidence from one frequency and one country is generalised to intraday data in general and to ASEAN | Other ASEAN markets were not examined by me either | yes: implications section |
| Alternative explanations and paths | DA agent challenge dimensions 1 and 6 | PARTLY_MEETS | see M2, M3 | The paper admits weight drift, but does not follow its consequences for the regime and level claims | none identified | yes |
| Cherry-picking and confirmation bias | DA agent challenge dimensions 2 and 3 | PARTLY_MEETS | see M5 | The headline 15.6% figure comes from the regime definition the paper itself calls exaggerating | none identified | no: it is repairable by reporting both definitions |
| So-what test | DA agent challenge dimension 8 | PARTLY_MEETS | see M8 | The premise about practitioners' behaviour is asserted without support | Venue fit is outside the DA remit | no |

These judgements are not totalled, weighted, averaged or mapped mechanically to severity.

### Genuine Strengths
The authors show real self-restraint in several places. They limit the formal Forbes–Rigobon test to the pair that does not share constituents. They say plainly that the Epps and diffusion channels are observationally equivalent. They report that the Pcap slope loses significance over the reliable range. They also provide a weight-sensitivity table. I rechecked the reported Forbes–Rigobon adjusted correlations, standard errors and relative-variance errors from the tabulated inputs, and they match to rounding. My challenges are therefore about inference and framing, not arithmetic.

### Strongest Counter-Argument
A sceptic would say the paper's main contrast compares two different quantities. The first is the correlation between an index and a parent index that is about 68% made of it. The second is the correlation between that index and an algebraic remainder. A parent–child correlation is expected to exceed a disjoint-pair correlation. Nobody in the paper is shown to use VN30–VN100 correlation to measure large-cap/mid-cap co-movement, so the "overstatement" is closer to a definition than a discovery. Worse, the "true" co-movement is not observed. It is Pcap = (R100 − w30·R30)/(1 − w30), which is a deterministic function of the nested correlation, the two volatilities and one assumed weight taken from a single 2024 factsheet. Table 7 shows that this assumed weight moves the purged correlation between 0.824 and 0.924. That range is wider than the precision the abstract reports (0.086–0.096).

Because Pcap loads −2.15 on R30, any weight error leaks VN30 returns straight into the "mid-cap" series. The leakage changes with regimes, since relative capitalisation drifts most in crises. That rival explanation fits the regime evidence as well as the interdependence story does. It also weakens the claim that Pcap–VN30 is exogenous enough for Forbes–Rigobon. The regime tests then conclude "interdependence, not contagion" from failing to reject a null. In the chronological test, the adjusted crisis correlation is significantly *below* the calm level, a result the authors do not discuss and which suggests the adjustment overcorrects. The sceptic's summary: large caps and mid-caps on HOSE are highly correlated (about 0.88) at every horizon and regime. Correlations rise with volatility, as expected. Beyond that, the horizon, mechanism and ASEAN-wide claims rest on one frequency, scales outside the paper's own reliability bounds, an unvalidated proxy and an ex-post regime sort.

### Issue Narrative
M1 is the clearest problem at headline level. The abstract says the nested correlations "primarily reflect shared capitalization". But after overlap is removed, 0.884 of the 0.977 remains. On the paper's own numbers, most of the nested correlation reflects cross-tier dependence, and shared capitalisation adds about 0.09 on top. The title's claim that nested correlations overstate co-movement survives. The causal attribution in the abstract does not. This defect alone justifies the repairable block on D3: it can be fixed by rewording, and no new analysis is needed.

M2 and M3 concern identification of the purged benchmark. M4 and M5 concern the regime and portfolio claims. M6 and M7 concern overgeneralisation. M8 concerns the premise that motivates the paper. None of these, taken alone, makes the paper impossible to accept. Each requires substantial rewriting or re-analysis, while the finding that large-cap/mid-cap co-movement is high but below nested-pair levels survives. I therefore record no Critical finding.

For M4, a supporting methodological note, whose scoring belongs to R1: the two-sample standard error treats the concatenated daily observations as independent draws of a Pearson correlation. It ignores the sampling error in δ and the dependence created by estimating DCCA at a 20-day scale. The reported standard errors are therefore likely too small. Correcting this would make the rolling-regime result less significant, not more, but it would also make the chronological "significantly below calm" result less secure.

### Minor Issues
- MF-DCCA double standard. text: §3.4 "indicating richer nonlinear cross-correlation structure than in the mechanically bound nested pairs". Pcap is itself an amplified linear combination, with a scaling factor of 3.151. The paper dismisses wide spectra for the statistical proxies as "amplified noise" but reads the widest Pcap spectrum as economic richness. The same amplification argument applies to both, at a smaller magnitude. Severity Minor. Confidence 4 (core competence: inferential consistency).
- Non sequitur in proxy validation. text: §3.3 "indicating that it captures a distinct mid-cap signal". A low correlation with residual artefacts shows that Pcap differs from those artefacts. It does not show that Pcap tracks mid-caps. Only a comparison with VNMIDCAP could show that (see M3). Severity Minor. Confidence 4 (core competence: argument analysis).
- Unscoped generalisation. text: §2.2 "Statistical weights cannot substitute for capitalization weights in nested index systems." This is shown for one near-collinear pair on one exchange, but stated as a rule for all nested index systems. It should be limited to the case studied. Severity Minor. Confidence 4 (core competence: scope of inference).

#### CRITICAL
| # | Dimension | Issue Description | Evidence Anchor | Confidence | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|-----------|-------------------|-----------------|------------|---------------------|-----------------------------|

#### MAJOR
| # | Dimension | Issue Description | Evidence Anchor | Confidence | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|-----------|-------------------|-----------------|------------|---------------------|-----------------------------|
| M1 | Core thesis / data-conclusion mismatch | The abstract attributes the nested correlations primarily to shared capitalisation. Yet the purged Pcap–VN30 correlation is 0.883–0.892 against 0.975–0.980 for the nested pairs (Table 2), so most of the co-movement is cross-tier dependence and overlap adds about 0.09. The same wording recurs in §4 ("attributable predominantly to index engineering"). Remedy: restate the finding as an increment of about 0.09 over a high baseline, and remove the causal "primarily" and "predominantly". | text: Abstract "near-perfect correlations among nested indices (0.975–0.980) primarily reflect shared capitalization rather than cross-tier interdependence" | 5 — direct reading of the paper's own reported values | — | — |
| M2 | Alternative explanation / identification of the benchmark | The "true co-movement" level is set by an assumed weight from one May 2024 snapshot applied to 2014–2025. Table 7 moves the purged correlation from 0.924 to 0.824, and the calm and crisis correlations by similar amounts. So the abstract's gap of 0.086–0.096 is precise only conditional on w30. Because Pcap loads −2.15 on R30, weight drift leaks VN30 returns into Pcap, and that drift likely differs across the 2018, 2020 and 2022 crises. This is a rival explanation for the regime correlation shifts that is not addressed. It also undercuts the "shares no constituents" exogeneity claim used for Forbes–Rigobon. Remedy: report the gap as a range over plausible weights, and reconstruct or bound the weight by episode. | table: Table 7 — Pcap–VN30 mean ρDCCA (1D) ranges from 0.924 (w30 = 0.60) to 0.824 (w30 = 0.75), and calm ρlow from 0.897 to 0.767 | 4 — algebra of the proxy plus the paper's own sensitivity table | — | — |
| M3 | Alternative path not taken | An exchange-published mid-cap index (VNMIDCAP/VN70) exists, and the paper names it. Yet the entire purged-benchmark argument rests on a synthetic proxy that is never compared with it, even on a partial sample or at daily frequency only. Until Pcap is shown to track VNMIDCAP, the claim that Pcap measures "genuine" mid-cap co-movement is an assumption, not a result. Deferring this check to Limitations leaves the central construct untested. | text: §2.1 "Because a VNMIDCAP price history is not available from our data source for the full sample and all frequencies" | 4 — logic of construct validation; access to VNMIDCAP data for a partial window assumed, not verified | — | — |
| M4 | Logic chain / regime inference | The abstract says Forbes–Rigobon conditioning "shows" the rise is explained by volatility. That rests on failing to reject H0 (Panel B p = 0.165), which is absence of evidence. In Panel A the adjusted crisis correlation is significantly below the calm level (t = −2.28), which is either a structural decrease or evidence that the adjustment overcorrects. The paper interprets neither. In addition, regimes are sorted on VNINDEX volatility, and VNINDEX contains the mid-caps in Pcap, so the dependent series enters the conditioning variable. The paper also concedes that margin-call feedback weakens exogeneity (§2.4). Remedy: reword to "no evidence of a structural increase", discuss the negative t, and define regimes on VN30 volatility. | table: Table 4 Panel A — ρ* = 0.803 below ρlow = 0.844, t = −2.28, p = 0.989 reported only as non-rejection | 4 — core competence: inference from hypothesis tests; Forbes–Rigobon assumptions as stated in §2.4 | — | — |
| M5 | Cherry-picking / portfolio-risk claim | The headline "up to 15.6%" comes from the rolling-quartile regime. The paper itself says that definition exaggerates, because its calm days are the quietest, least correlated intervals. The chronological definition gives 2.44%. The quartiles are full-sample and ex post, so an allocator could not have used them in real time. The 50/50 Pcap/VN30 portfolio cannot be held (315% long, 215% short), and only the correlation is varied while volatilities are held fixed. Remedy: report both definitions side by side in the abstract, and label the result a correlation-only sensitivity for a shadow exposure. | text: §3.5 "The rolling definition exaggerates the raw tightening because its low-volatility days are drawn from the quietest, least correlated intervals." | 5 — the paper's own statement set against its own headline | — | — |
| M6 | Overgeneralisation / mechanism asserted | The abstract claims horizon strengthening "at intraday frequencies" and states the mechanism as fact. But only M30 regressions are reported (H1 and H4 are absent). The Pcap slope is significant only when scales up to 5,485 bars are included, far beyond the paper's own reliability threshold of 444 (reliable-range p = 0.102). The daily slope is insignificant (p = 0.47). §3.7 concedes that the two mechanisms are observationally equivalent and not identified. The implied change over the reliable range is about 0.01 in correlation. Remedy: limit the claim to M30 and to the broad-market pairs, and present the mechanisms as candidate explanations. | text: Abstract "at intraday frequencies this co-movement tends to strengthen over longer holding horizons as microstructure frictions resolve and information diffuses throughout the market" | 4 — direct comparison of the abstract with Tables 5–6 and §3.7 | — | — |
| M7 | Overgeneralisation beyond sample | Evidence from one exchange is turned into imperatives for ASEAN allocators, including Malaysian funds, and into ASEAN-wide policy. The "institutional comparative hypothesis" about short-sale bans is framed in §1 but never tested. The paper has no cross-country data and no within-Vietnam variation in the rules. The statement that parent–child blends give negligible diversification is also near-arithmetic for nested indices. Remedy: scope the implications to HOSE, and present the ASEAN extension and the short-sale link as hypotheses for future work. | text: §4.1 "must recognize that blending large-cap and broad-market parent-child indices offers negligible diversification benefits" | 4 — scope of inference; no knowledge claimed about other ASEAN index data | — | — |
| M8 | Unsupported premise / estimand mismatch | The motivating premise is that allocators and risk models treat nested indices as separate diversification instruments, or read nested correlations as large-cap/mid-cap co-movement. It is asserted without a citation, survey, product example or data. Without it, the headline "overstatement" is a comparison between a parent–child correlation and a disjoint-pair correlation. Those are different estimands, and the paper never shows that anyone substitutes one for the other. Remedy: document the practice (for example fund mandates, index-product marketing or risk-model defaults), or reframe the contribution as measuring the large-cap/mid-cap dependence level. | absence: Abstract and §1 Introduction — expected evidence or a citation that practitioners or risk models use nested-index correlations as a measure of large-cap/mid-cap co-movement; checked Abstract, §1, §1.1, §4.1, References | 3 — argument analysis; practitioner behaviour in Vietnam not independently verified | — | — |

