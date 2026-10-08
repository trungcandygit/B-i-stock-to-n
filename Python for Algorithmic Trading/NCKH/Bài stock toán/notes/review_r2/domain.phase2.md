contract_role: domain
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: block
trigger: "A headline novelty or gap claim is contradicted by identifiable published precedent that the manuscript does not cite or distinguish"
block_class: repairable

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

### Domain Review Report (Peer Reviewer 2)

Reviewer identity (Configuration Card #3): senior empirical asset-pricing researcher working on return co-movement and contagion, the index-membership and habitat co-movement literature, the Forbes–Rigobon interdependence-versus-contagion debate, and size-tier integration in Asian emerging and frontier markets including Vietnam.

Overall recommendation (domain remit only; the synthesizer decides): Major Revision.

Confidence score: 4 of 5. Strong on co-movement, contagion and index-membership literatures and on HOSE index construction; weaker on econophysics estimator conventions, which I leave to Reviewer 1. Confidence is a scope disclosure only.

Calibration status: `NOT_CALIBRATED`

Criteria binding: `criteria_binding_unavailable`; no venue-alignment claim is made.

### Criterion-Bound Judgements

| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| D2 novelty and gap claim represented accurately against prior work | Sprint contract D2; Card #3 focus 1 | DOES_NOT_MEET | text: §2.4 gap statement (W1) | The exact identity is a classical part–whole correlation; the paper claims nobody derived it and searched only 2021–2026 | The empirical scale-wise application may still be new; I found no DCCA paper doing it | yes: requires repositioning of contribution 1 |
| D2 interpretation of results against contagion and co-movement literature | Sprint contract D2; Card #3 focus 2 | PARTLY_MEETS | text: §6.1 (W2, W4) | Forbes–Rigobon reading presented without the documented critique; purged correlation labelled economic without proxy validation | Methodology bias of the proxy is Reviewer 1's remit | yes: claims must be qualified |
| D2 theoretical grounding of H1–H5 | Sprint contract D2; Card #3 focus 2 | PARTLY_MEETS | text: §2.5 (W3) | H1, H2 follow from Proposition 1 (by construction); H3 omits the size lead-lag literature; H4, H5 grounded | none identified | no: repairable in text |
| D2 accuracy of Vietnam institutional section | Sprint contract D2; Card #3 focus 3 | PARTLY_MEETS | text: §3.1, §6.2 (W5, W6, W7) | Existing mid-cap ETF missed; short-sale law imprecise; FOL and 2025 reclassification absent | Legal details checked through secondary legal databases, not the gazette text | no individually; jointly material for Section 6.2 |
| D2 coverage of key references | Sprint contract D2; Card #3 focus 1 and 3 | PARTLY_MEETS | absence: §2.2 (W8) | Core membership papers present; weight-based and critical membership papers missing | none identified | no |

These judgements are not totalled or mapped mechanically to the recommendation.

### Summary Assessment

The manuscript asks a sensible and practically relevant question: how much of the very high correlation between nested equity indices (VN30 inside VN100 inside VNINDEX) reflects shared constituents rather than economic linkage. Its domain positioning has three problems. First, the central analytical result, the correlation of a component with a weighted sum that contains it, is a classical part–whole correlation known since Pearson (1897) and routinely corrected in psychometrics (Cureton 1966). Its DCCA version follows immediately from bilinearity. The paper's claim that no prior work "derives that component exactly" therefore cannot stand. The contribution needs to be recast as applying and measuring a known identity scale by scale in a real nested index system. That remains a useful contribution. Second, the economic readings of the results are stated with more confidence than the domain literature supports. The "no contagion, only interdependence" conclusion ignores the well-known bias of the Forbes–Rigobon adjustment toward the null (Corsetti et al. 2005). The "purged" correlation of about 0.89 is interpreted as economic co-movement even though the proxy is an index-construction residual whose level moves from 0.82 to 0.92 across plausible weights (Table A2). HOSE capping rules also mean the VN30 index is not exactly the VN30 sleeve of VN100. Third, the institutional section misses facts that bear on the implications. A VNMIDCAP ETF has traded on HOSE since 2022. Foreign-ownership limits are not discussed. The short-sale legal position is stated imprecisely. The authors handle null results honestly and are careful in places, for example by restricting the Forbes–Rigobon test to the disjoint pair. All of the issues above can be fixed by rewriting and adding targeted checks.

### S1: Candid statement that the core relation is an identity

The authors state that Eq. (7) holds by construction and locate its value in the decomposition. This is the right framing and gives a basis for the repositioning requested in W1.
**Evidence Anchor**: text: §4.2 "Eq. (7) is an accounting identity rather than an estimated relation; its content lies in the decomposition it delivers"

### S2: Clear separation of behavioral membership co-movement from arithmetic overlap

The paper distinguishes the Barberis–Shleifer–Wurgler habitat and friction channel from mechanical overlap. Many applied papers conflate the two.
**Evidence Anchor**: text: §2.2 "This literature concerns behavioral co-movement among stocks. Our concern is the arithmetic overlap between indices"

### S3: Appropriate restriction of the Forbes–Rigobon test and acknowledgement of HOSE margin-call dynamics

The test is applied only to the disjoint pair, and the authors note that margin-call cascades weaken exogeneity. Both choices fit the Vietnamese setting.
**Evidence Anchor**: text: §4.6 "Severe downturns on the HOSE can trigger margin calls and simultaneous selling of large and mid caps, which weakens exogeneity"

### S4: Honest reporting of null hypotheses

H3 after multiplicity adjustment and H4 are reported as not supported, and the abstract and conclusion do not lean on the unadjusted pattern.
**Evidence Anchor**: table: Table 8, rows H3 and H4

### S5: Demonstration that the floor is not specific to DCCA

Showing that the Pearson floor (0.903) and share (0.914) nearly equal the DCCA values makes the finding accessible to mainstream finance readers.
**Evidence Anchor**: text: §5.4 "gives a floor of 0.903 and a mechanical share of 0.914, so the result is not specific to DCCA"

### W1: The exactness and novelty claim ignores the classical part–whole correlation and finance overlap measures

**Severity**: Major
**Evidence Anchor**: text: §2.4 "no study we found separates the mechanical component of correlations between overlapping indices from economic co-movement, and none derives that component exactly"
**Confidence**: 5 — the algebra of corr(X, wX + (1 − w)Y) is textbook, and the cited precedents were verified by search

Proposition 1 with κ = (1 − w)σ_M/(wσ_A) is the standard formula for the correlation of a variable with a weighted sum that contains it. Statistics has studied this as "part–whole" or "spurious" correlation since Pearson (1897). Psychometrics corrects the item–total correlation by removing the item from the total (Cureton 1966). That correction is exactly the "purge" applied here. The DCCA version follows from linearity of profiling and detrending, as the authors' own two-line proof shows. In finance, Barberis et al. (2005) already control for the return of non-index stocks in bivariate regressions, which is a purge of overlap. Holdings-overlap measures such as Active Share (Cremers and Petajisto 2009) quantify portfolio–benchmark overlap directly. Because the search window was restricted to 2021–2026 and to the DCCA/econophysics outlets, the gap statement and contribution 1 ("derives an exact, scale-by-scale decomposition") overstate novelty. A referee in the finance community will notice this immediately.
Fix: (i) Cite the part–whole tradition and state that Eq. (7) is the scale-wise DCCA analogue of a known result. (ii) Rewrite the gap as "no study measures the size of the mechanical floor, and its scale and regime behavior, for a real nested index system, and none applies it to diversification and contagion inference." (iii) Rename contribution 1 accordingly. (iv) Extend the search beyond 2021–2026 and beyond DCCA journals, and report the search strings. (v) In Table 1, add a row for the part–whole and holdings-overlap precedents with "Overlap treated: Yes (Pearson, static)".

### W2: The "no contagion, only interdependence" reading omits the documented bias of the Forbes–Rigobon adjustment

**Severity**: Major
**Evidence Anchor**: text: §6.1 "consistent with the interdependence interpretation of Forbes and Rigobon (2002) rather than with a change in transmission"
**Confidence**: 4 — standard contagion-literature debate; references verified

The Forbes–Rigobon correction assumes that the variance of the idiosyncratic shock is unchanged between regimes and that the conditioning market is exogenous. Corsetti, Pericoli and Sbracia (2005) show that the "no contagion" result depends heavily on these restrictions and is biased toward the null when country-specific (here, tier-specific) variance also rises in crises. Rigobon (2003) develops identification through heteroskedasticity, which is the more general alternative. In this paper δ equals 2.21 and 7.06. With variance expansions this large, the adjustment mechanically pulls ρ* far below ρ_high, and the quartile regimes are sorted on VNINDEX, which contains both tiers. The manuscript reports power, but it does not tell readers that the test itself is known to be conservative in this direction. The conclusion and abstract ("gives no evidence of crisis contagion between tiers") are acceptable as stated, but Section 6.1 goes further and endorses interdependence as the mechanism.
Fix: Cite Corsetti et al. (2005) and Rigobon (2003). State in Sections 5.6 and 6.1 that the result means no increase beyond what a constant-β common-factor model implies, under the assumption of constant tier-specific variance. If feasible, report the tier-specific residual variance in calm and crisis regimes so readers can judge whether that assumption holds. Drop the causal "rather than a change in transmission" wording, or make it conditional on that assumption.

### W3: H3's theoretical grounding omits the direct literature on size-based lead–lag and stale index prices

**Severity**: Minor
**Evidence Anchor**: text: §2.5 "Both mechanisms predict positive scaling slopes for pairs whose constituents are repriced at different speeds"
**Confidence**: 4 — core asset-pricing literature; references verified

The horizon-dependence hypothesis rests on Epps (1979) and Hong and Stein (1999). The most directly relevant evidence is the documented lead of large-cap over small-cap returns (Lo and MacKinlay 1990) and its attribution to slow diffusion of industry information (Hou 2007). Index levels built from infrequently traded constituents also carry stale-price autocorrelation, the classical thin-trading problem (Dimson 1979; DOI not verified). These sources would sharpen H3. The prediction should concern lead–lag between tiers, testable with cross-autocorrelations at the index level, which the data allow. They would also show that the "Epps versus diffusion" question in Section 6.1 is partly answerable with lead–lag tests. In addition, the statement that VN30–VN100 should have no slope "because its co-movement is fixed by overlap" does not follow from Proposition 1. The nested coefficient can still vary with s through κ(s) and ρ_AM(s). The prediction should be stated as "a slope bounded by the sensitivity in Eq. (9)".
Fix: Add these references, restate the H3 prediction quantitatively, and consider one lead–lag regression of VNMIDCAP proxy returns on lagged VN30 returns as supplementary evidence. Reviewer 1 should judge whether it is appropriate given the construction of P_cap.

### W4: The purged correlation is interpreted as economic co-movement although the proxy is an unvalidated index-construction residual

**Severity**: Major
**Evidence Anchor**: text: §6.1 "Once the overlap is removed, the remaining dependence behaves like economic co-movement."
**Confidence**: 4 — HOSE index rules checked in factsheets via search; the estimation consequences belong to Reviewer 1

P_cap = (B − wA)/(1 − w) equals VNMIDCAP only if the VN30 index is exactly the VN30 sleeve of VN100. HOSE factsheets state that both indices are free-float capitalization-weighted with a 10% capping limit applied per index. As a result, the largest VN30 stock weighs about 11.9% in VN30 but about 8.3% in VN100 (August 2024 factsheet), and the internal weights of the VN30 index differ from those of the VN30 sleeve inside VN100 whenever a cap binds. Weight drift between semi-annual reviews, and the single 31 May 2024 snapshot applied to 2014–2025, add further construction noise. The factor of 1/(1 − w) ≈ 3.15 amplifies it. Table A2 shows the "economic" correlation ranging from 0.824 to 0.924 for w between 0.60 and 0.75. That range is wider than the gap's bootstrap interval, so the level of ρ_AM, and therefore statements such as "the purged correlation remains high (about 0.89)" and "the mechanical floor and the economic correlation are of the same magnitude", depend on index-construction details as much as on economics. The published VNMIDCAP index and the FUEDCMID ETF (see W5) would allow direct validation for at least the daily frequency.
Fix: (i) Validate P_cap against the published VNMIDCAP daily index (HOSE publishes it) and report the correlation and tracking error. (ii) Discuss the capping and free-float rules explicitly in Sections 3.2 and 4.3. (iii) Call ρ_AM the "overlap-purged correlation" rather than the "economic correlation" unless validation supports the stronger label. (iv) State that the floor and share, which depend on κ, are less exposed to this problem than the level of ρ_AM, which is the more robust part of the contribution.

### W5: Section 6.2 recommends an investable VNMIDCAP fund that already exists

**Severity**: Minor
**Evidence Anchor**: text: §6.2 "such as an investable VNMIDCAP fund or mid-cap index futures alongside the existing VN30 futures"
**Confidence**: 5 — listing verified in exchange and press reports

The DCVFMVN MIDCAP ETF (ticker FUEDCMID), which physically replicates the VNMIDCAP index, has been listed on HOSE since 29 September 2022. The policy recommendation is therefore partly obsolete. Section 5.7's phrase "for example one held through a mid-cap index fund" also implies that such a fund exists, so the two sections are inconsistent. The ETF's existence also means part of the mid-cap tier is investable. The statement that the spread "cannot" be traded should become "cannot be shorted or hedged with futures".
Fix: Acknowledge the ETF, keep the recommendation for mid-cap futures, which do not exist, and use the ETF or index NAV for the validation in W4.

### W6: Imprecise statement of trading rules (short selling, settlement history, session structure)

**Severity**: Minor
**Evidence Anchor**: text: §3.1 "Decree 155/2020/ND-CP and Circular 120/2020/TT-BTC prohibit cash short selling"
**Confidence**: 3 — legal texts checked through secondary legal databases, not the official gazette

Circular 120/2020/TT-BTC does not simply prohibit short selling. It defines a covered (secured) short-sale transaction using securities borrowed through the VSDC lending system, to be implemented by the SSC after Ministry of Finance approval. In practice short selling is not operational, but the accurate statement is "provided for in law but not yet implemented; naked short selling is not permitted". Decree 155/2020 was amended by Decree 245/2025/ND-CP (September 2025), within the sample period. HOSE moved from T+3 to T+2 settlement on 1 January 2016, so 2014–2015 ran under T+3. The paper says "most of the sample", which is right, but the dates should be explicit. The session description omits the 11:30–13:00 midday break, which creates a within-day gap relevant to M30/H1 bars and to the Epps discussion.
Fix: Correct the short-sale sentence, cite the amending decree, give the T+3/T+2 dates, and describe the morning and afternoon continuous sessions with the midday break.

### W7: Foreign-ownership limits and market reclassification are absent from the institutional background

**Severity**: Minor
**Evidence Anchor**: absence: §3.1 Institutional background — expected discussion of foreign ownership limits (49% general, 30% banks) and the October 2025 FTSE reclassification announcement; checked §3.1, §4.6, §6.1, §6.2, §6.3
**Confidence**: 4 — FOL regime and FTSE announcement verified via search

Foreign-ownership limits bind mainly for large caps, especially banks and popular VN30 names. They create full-room premiums and off-exchange trading. This tier-asymmetric friction can drive large/mid-cap divergence and crisis co-movement through foreign flows. It is a natural alternative to herding and margin calls for the regime results. FTSE Russell's announcement on 8 October 2025 of an upgrade to secondary emerging status, effective September 2026, falls inside the sample and implies anticipated passive inflows concentrated in large caps. The authors do not need new analysis, but these features belong in Section 3.1, and Section 6.1 should list them as competing explanations.
Fix: Add a paragraph on FOL and reclassification. In Section 6.1, list FOL-driven foreign flows, ±7% limit-hit synchronization and herding (Nguyen et al. 2023) as rival mechanisms for crisis co-movement that index-level data cannot separate.

### W8: The index-membership literature is cited selectively

**Severity**: Minor
**Evidence Anchor**: absence: §2.2 and reference list — expected Greenwood (2008) and Chen, Singal and Whitelaw (2016) on index-weight-driven and contested excess comovement; checked §2.2, Table 1, References
**Confidence**: 4 — references verified

Greenwood (2008) is the closest finance precedent for the role of index weights. Using cross-sectional variation in Nikkei 225 weights, he shows that overweighting raises co-movement with other index stocks. Chen, Singal and Whitelaw (2016) show that much of the BSW excess co-movement disappears with matched controls and Dimson betas. That critique supports the paper's argument that index-level co-movement measures are easy to misread. Neither is cited, and Section 2.2 currently presents the membership literature as more settled than it is. The authors already note that Greenwood and Sammon (2025) found the price effect has disappeared.
Fix: Add both papers to Section 2.2 and use Chen et al. (2016) to reinforce the motivation.

### W9: Vietnamese studies are mostly listed rather than used analytically

**Severity**: Minor
**Evidence Anchor**: text: §2.2 "Vietnamese evidence suggests that both mechanisms could matter on the HOSE."
**Confidence**: 3 — judgement on synthesis quality

The paragraph strings five Vietnamese findings together in one sentence. Only herding and connectedness are tied back to the research question, and only briefly. Tran and Tran (2025) on delayed high-frequency price adjustment is directly relevant to H3 but is not used in Section 5.5 or 6.1. Chen et al. (2021) on small-firm liquidity is used only in Section 6.1.
Fix: Link each Vietnamese study to the hypothesis it informs (for example, Tran and Tran 2025 to H3, Nguyen et al. 2023 and Bui et al. 2022 to H4), and return to them when interpreting results.

### Detailed Comments

#### Literature review
Coverage: DCCA methods and COVID-era contagion are well covered. The part–whole statistics tradition (W1), the size lead–lag literature (W3), the Forbes–Rigobon critique (W2) and weight-based membership papers (W8) are missing. Integration quality: Sections 2.1–2.3 synthesize rather than enumerate, apart from the Vietnamese paragraph (W9). Research gap: persuasive for "measuring the floor in a real nested system", not for "deriving it" (W1).

#### Theoretical framework
H1 and H2 follow from Proposition 1, and given w ≈ 0.68 they hold almost by construction. That is acceptable only if they are framed as quantifying an identity rather than as testing a theory. H3 needs the lead–lag literature and a quantitative prediction (W3). H4 is grounded in Forbes–Rigobon but needs its critique (W2). H5 is a direct consequence of regime-varying correlation and is well grounded.

#### Academic argument quality
Factual accuracy: issues in W5, W6 and W7. Argument logic: the move from "purged" to "economic" is the main leap (W4). Terminology: "economic correlation" for ρ_AM and "interdependence" as a mechanism are stronger labels than the evidence supports. Elsewhere, "contagion" is defined in the Forbes–Rigobon sense and used consistently.

#### Contribution to the field
The genuine contribution is empirical and expository. It shows, with inference, that in a real nested system the floor is about 0.90, the share about 0.91 and the sensitivity about 0.11, and that these values are stable across scales and frequencies. It gives practitioners a weight-and-volatility formula. Positioned this way, the paper advances understanding of how index-level correlations misstate diversification across size tiers. The overclaiming risk lies in "exact decomposition" as the headline novelty (W1) and in the mechanism statements in Section 6.1 (W2, W4).

### Missing Key References

Verified by web search in this session (bibliographic metadata and DOI seen in publisher, RePEc or institutional records unless noted):

- Pearson, K. (1897). Mathematical contributions to the theory of evolution: On a form of spurious correlation which may arise when indices are used in the measurement of organs. Proceedings of the Royal Society of London, 60, 489–498. https://doi.org/10.1098/rspl.1896.0076 (DOI taken from a secondary listing; confirm the DOI landing page and the year, 1896 or 1897, before citing). Relevance: origin of part–whole/spurious correlation (W1).
- Cureton, E. E. (1966). Corrected item-test correlations. Psychometrika, 31(1), 93–96. https://doi.org/10.1007/BF02289461. Relevance: removing a part from the whole before correlating (W1).
- Cremers, K. J. M., & Petajisto, A. (2009). How active is your fund manager? A new measure that predicts performance. Review of Financial Studies, 22(9), 3329–3365. https://doi.org/10.1093/rfs/hhp057. Relevance: holdings-overlap measure (W1).
- Corsetti, G., Pericoli, M., & Sbracia, M. (2005). 'Some contagion, some interdependence': More pitfalls in tests of financial contagion. Journal of International Money and Finance, 24(8), 1177–1199. https://doi.org/10.1016/j.jimonfin.2005.08.012. Relevance: critique of the Forbes–Rigobon adjustment (W2).
- Rigobon, R. (2003). Identification through heteroskedasticity. Review of Economics and Statistics, 85(4), 777–792. https://doi.org/10.1162/003465303772815727 (DOI inferred from the publisher URL in the RePEc record; confirm). Relevance: W2.
- Lo, A. W., & MacKinlay, A. C. (1990). When are contrarian profits due to stock market overreaction? Review of Financial Studies, 3(2), 175–205. https://doi.org/10.1093/rfs/3.2.175. Relevance: large-cap lead over small caps (W3).
- Hou, K. (2007). Industry information diffusion and the lead-lag effect in stock returns. Review of Financial Studies, 20(4), 1113–1138. https://doi.org/10.1093/rfs/hhm003. Relevance: W3.
- Greenwood, R. (2008). Excess comovement of stock returns: Evidence from cross-sectional variation in Nikkei 225 weights. Review of Financial Studies, 21(3), 1153–1186. https://doi.org/10.1093/rfs/hhm052. Relevance: W8.
- Chen, H., Singal, V., & Whitelaw, R. F. (2016). Comovement revisited. Journal of Financial Economics, 121(3), 624–644. https://doi.org/10.1016/j.jfineco.2016.05.007. Relevance: W8.

[UNVERIFIED] leads (metadata seen, DOI not confirmed; verify before citing):
- Dimson, E. (1979). Risk measurement when shares are subject to infrequent trading. Journal of Financial Economics, 7(2), 197–226. DOI not confirmed. Relevance: W3.
- Bekaert, G., Harvey, C. R., & Ng, A. (2005). Market integration and contagion. Journal of Business, 78(1), 39–69 (page range differs across sources). DOI not confirmed. Relevance: factor-model definition of contagion as an alternative to W2.
- Search lead: the international-integration literature that correlates a country index with a "world-ex-country" or "region-ex-country" index to avoid self-inclusion is a further finance precedent for purging overlap. I did not confirm a specific citation.

Non-academic sources used for institutional checks (to be cited as such if the authors adopt them): HOSE index factsheets (capping limit 10%; largest-weight figures for VN30 and VN100); exchange and press reports of the FUEDCMID listing (29 September 2022); FTSE Russell's September 2025 Country Classification announcement (released 8 October 2025).

### Questions for Authors

1. Can you report the correlation and tracking error between P_cap and the published VNMIDCAP index (or FUEDCMID NAV) at the daily frequency?
2. How often, and by how much, did the 10% cap bind in VN30 but not in VN100 during 2014–2025? How large is the resulting difference between the VN30 index and the VN30 sleeve of VN100?
3. Under the Forbes–Rigobon assumptions, what are the calm and crisis residual variances of P_cap given VN30? Is the constant-idiosyncratic-variance assumption plausible?
4. Did the gap search include the statistics and psychometrics part–whole literature, and finance work using index-ex-constituent returns? If not, can you broaden it and report the search strategy?
5. Are tier-level lead–lag patterns (lagged VN30 predicting mid-cap returns) visible in your data? Would they discriminate between the Epps and diffusion readings?

### Minor Issues

- §3.1: "VN30 index futures trade on the Hanoi Stock Exchange" is correct. Also mention VN30 covered warrants, which are relevant to hedging large caps.
- §3.2: VNINDEX is weighted by full market capitalization and VN100 by free float. This weighting difference, and not only missing weight data, is why the decomposition is not extended to the broad-market pairs. State it in §6.3.
- §5.7: "a mid-cap factor exposure, for example one held through a mid-cap index fund" should name the existing ETF (W5).
- Abstract: "the identity itself holds for any nested pair" should add "with known weights and a common weighting scheme", given W4.

### Coverage Receipt

Not required: both the strengths list (S1–S5) and the weaknesses list (W1–W9) are non-empty.
