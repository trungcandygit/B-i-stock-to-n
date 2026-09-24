contract_role: domain
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: warn
trigger: "Omission of important seminal or recent domain literature, imprecise or inconsistent domain terminology, or minor institutional inaccuracies and unreconciled divergences from prior evidence that do not overturn the headline conclusions"

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

I reviewed the manuscript as an emerging-market equity specialist, focusing on Vietnam and ASEAN index construction, microstructure and regulation. Most of the institutional description of HOSE is accurate. That includes the auction windows, the ±7% band, the margin floor, Circular 68/2024 and VN30 futures on the HNX derivatives market. The Forbes–Rigobon algebra is stated correctly, and the nested ASEAN index examples are right. The domain problems sit in three places. First, the mid-cap proxy rests on index-construction assumptions that are not stated: a single 2024 weight, capping, and a full-capitalization VNINDEX. Second, Forbes–Rigobon is carried over to DCCA coefficients without justification. Third, the novelty claim ignores the partial-DCCA literature. Several method and mechanism citations also attribute ideas to the wrong source. None of these, taken alone, overturns the headline direction, because Table 7 shows the gap survives across the weights tried. Together they fit the warn level for domain accuracy rather than block. Following the authors' constraint, every piece of literature named below is a suggestion only, for the authors to verify. I do not ask for it to be added.

### S1: Accurate HOSE microstructure detail
The trading-session description matches HOSE rules and is linked correctly to the behaviour of the first and last M30 bars.
**Evidence Anchor**: text: §1.1 "a 15-minute batch auction sets the opening price (ATO, 09:00–09:15)"

### S2: Forbes–Rigobon test correctly restricted to the disjoint pair
The authors see that nesting breaks the exogeneity assumption and limit formal inference to Pcap–VN30. This matches the method's requirements.
**Evidence Anchor**: text: §2.4 "We therefore restrict the formal test of a structural correlation increase to the Pcap–VN30 pair."

### S3: Honest identification boundary between Epps and diffusion channels
**Evidence Anchor**: text: §3.7 "the two mechanisms are observationally equivalent in index-level closing data"

### S4: Correct diagnosis of degenerate statistical proxies
The explanation of why the correlation-based weight blows up the residual is correct for near-collinear nested indices.
**Evidence Anchor**: text: §2.2 "Statistical weights cannot substitute for capitalization weights in nested index systems."

### S5: Correct regional index-nesting facts
**Evidence Anchor**: text: §1 "the SET50 is nested within the SET100 in Thailand, and the IDX30 is nested within the LQ45 in Indonesia"

### S6: Forbes–Rigobon adjustment formula reproduced correctly
Table 4 recomputes from the stated formula: Panel A gives 0.924/1.150 = 0.803, and Panel B gives a factor of 1.402.
**Evidence Anchor**: equation: §2.4 ρ* = ρhigh / sqrt(1 + δ(1 − ρhigh²))

### W1: Mid-cap proxy ignores HOSE capping, weight drift and the published VNMIDCAP series
**Problem**: Pcap assumes three things: VN100 is exactly a w30-weighted mix of VN30 and the other 70 stocks, VN30's internal weights equal those stocks' relative weights inside VN100, and w30 has stayed at its May 2024 value since 2014. HOSE applies separate per-stock caps and free-float and foreign-ownership adjustments to VN30 and VN100, so neither identity holds exactly. The VN30 share of VN100 has also moved over twelve years. The exchange publishes VNMIDCAP, at least at daily frequency, so the proxy can be checked.
**Evidence Anchor**: text: §2.2 "where w30 = 0.6826 is the free-float market-capitalization weight of VN30 within VN100 computed from the HOSE factsheet of May 31, 2024"
**Why it matters**: The headline gap of 0.086–0.096 moves one-for-one with w30. Table 7 shows 0.824–0.924 across the range tried. Any leakage from capping or drift therefore goes straight into the main number.
**Suggestion**: Check Pcap against daily VNMIDCAP returns and report their correlation and tracking error. Describe the VN30 and VN100 capping rules. Rebuild w30 at least at the semi-annual review dates.
**Severity**: Major
**Confidence**: 4 — core expertise: Vietnamese index construction

### W2: Forbes–Rigobon correction applied to DCCA coefficients on concatenated subsamples
**Problem**: Forbes and Rigobon derived their bias correction for Pearson correlations of returns in a regression model with an exogenous conditioning market. Here it is applied to a scale-20 DCCA coefficient computed on calm and turbulent days joined end to end. The manuscript never shows that the heteroskedasticity-bias algebra carries over to detrended covariances, or to profiles that splice together non-contiguous episodes.
**Evidence Anchor**: text: §3.5 "Regime correlations are DCCA coefficients at a 20-day horizon estimated on the concatenated calm and turbulent subsamples of daily returns"
**Why it matters**: The claim of "interdependence rather than contagion" rests entirely on this transfer of the method.
**Suggestion**: Report the Forbes–Rigobon test on Pearson return correlations alongside it, or justify the DCCA analogue. Also discuss the known critiques of the adjustment. As a suggestion only: Corsetti, Pericoli and Sbracia (2005, J. Int. Money Finance) is the standard critique.
**Severity**: Major
**Confidence**: 3 — core expertise: contagion testing; the DCCA transfer argument is adjacent

### W3: Research-gap claim ignores detrended partial cross-correlation methods
**Problem**: The paper says that separating shared components within DCCA is unaddressed. But the DCCA family already has partial-correlation versions (DPCCA) built to strip a common external driver from a pair. These are the natural method-level benchmark for the "purging" exercise. As a suggestion only: Yuan et al. (2015, Scientific Reports) and Qian et al. (2015, Phys. Rev. E).
**Evidence Anchor**: text: §1 "remain an unaddressed empirical issue"
**Why it matters**: The novelty claim is overstated, and there is no comparison with the established tool.
**Suggestion**: Narrow the claim to nested index architectures specifically. Explain why capitalization decomposition beats partial DCCA controlling for VN30, or report the partial-DCCA result.
**Severity**: Major
**Confidence**: 4 — core expertise: DCCA literature

### W4: Hong and Stein (1999) cited for cross-firm large-to-small lead-lag
**Problem**: Hong–Stein models slow diffusion of firm-specific news across groups of investors. It is not a model of market-wide news passing from large caps to small caps. The large-to-small lead-lag story belongs to a separate literature on nonsynchronous trading and cross-autocorrelation. As a suggestion only: Lo and MacKinlay (1990), Chordia and Swaminathan (2000, J. Finance) and Hou (2007, Rev. Financ. Stud.).
**Evidence Anchor**: text: §3.7 "market-wide news is reflected immediately in VN30 valuations but diffuses gradually into mid-cap stocks over several trading hours"
**Suggestion**: Reword the mechanism and attribute it to the right source.
**Severity**: Minor
**Confidence**: 4 — core expertise: asset-pricing mechanisms

### W5: The Epps effect cannot explain slopes beyond about ten bars
**Problem**: The paper confines the Epps effect to roughly ten bars or fewer, yet cites it for a positive slope estimated over 5 to 5,485 bars, which is weeks of trading. Stale index constituents during limit-lock days are a more plausible short-horizon channel on HOSE.
**Evidence Anchor**: text: §2.5 "depress the correlation at small timescales (roughly ten bars or fewer)"
**Suggestion**: Make the timescales the mechanism is claimed for match the scales where the slope is actually identified.
**Severity**: Minor
**Confidence**: 3 — core expertise: microstructure

### W6: Podobnik et al. (2011) contribution misstated
**Problem**: The reviewer's understanding is that Podobnik et al. (2011) gave simulation-based critical values for the DCCA statistic, not an analytical finite-sample distribution. The same source does not establish that a Student-t with N−s−2 degrees of freedom holds for ρDCCA.
**Evidence Anchor**: text: §1 "Podobnik et al. (2011) established the analytical finite-sample distribution for hypothesis testing"
**Suggestion**: Reword the sentence, and either justify the t-approximation or drop it.
**Severity**: Minor
**Confidence**: 3 — core expertise: DCCA inference

### W7: MF-DCCA variant attribution inconsistent
**Problem**: Oświęcimka et al. (2014) proposed a sign-preserving extension, MFCCA, and not the absolute-value operator, which goes back to Zhou (2008). Jiang and Zhou (2011) is the moving-average alternative to polynomial detrending, and the paper does not use it.
**Evidence Anchor**: text: §2.6 "with the absolute-value operator (Oświęcimka et al. 2014), incorporating bivariate moving-average formalisms (Jiang and Zhou 2011)"
**Suggestion**: State which single variant was actually estimated and cite its source.
**Severity**: Minor
**Confidence**: 4 — core expertise: multifractal methods

### W8: "Spectrum width" used for the generalized-exponent range
**Problem**: The difference between h(−5) and h(5) is Δh. The width of the singularity spectrum is Δα.
**Evidence Anchor**: text: §3.4 "the multifractal spectrum width, the difference between the exponents at q = −5 and q = 5"
**Suggestion**: Report Δα, or rename the measure Δh.
**Severity**: Minor
**Confidence**: 4 — core expertise: multifractal terminology

### W9: Settlement-cycle description applies only to the end of the sample
**Problem**: The reviewer's understanding is as follows. Settlement was T+3 before 2016. From 2016 until the August 2022 change, shares bought on day T could be sold only from the morning of T+3. The "afternoon of the second business day" rule applies only after that change.
**Evidence Anchor**: text: §1.1 "Throughout most of our sample period, equities purchased on the HOSE could not be sold until the afternoon of the second business day"
**Suggestion**: Check the settlement rules against SSC and VSDC records and give the date of each regime.
**Severity**: Minor
**Confidence**: 3 — core expertise: Vietnamese market rules; exact dates to be verified

### W10: VNINDEX weighting not described
**Problem**: VNINDEX is weighted by full market capitalization without free-float adjustment, while VN30 and VN100 use capped free-float weights. The nesting therefore holds for constituents but not for weights. This affects how the VN30–VNINDEX and VN100–VNINDEX overlap should be read.
**Evidence Anchor**: text: §2.1 "the composite VNINDEX, which covers all common stocks listed on the HOSE"
**Suggestion**: State the weighting scheme of each index.
**Severity**: Minor
**Confidence**: 4 — core expertise: HOSE index methodology

### W11: Uncited mechanical claims about the price band
**Evidence Anchor**: text: §1.1 "is associated with artificial serial correlation, and coincides with mechanical spikes in cross-correlations"
**Problem**: Empirical claims about price-limit effects are stated without evidence from the literature or from the paper's own data.
**Suggestion**: Support the claims or soften them to hypotheses.
**Severity**: Minor
**Confidence**: 3 — core expertise: price-limit microstructure

### W12: Vietnam's market-classification status out of date
**Problem**: The reviewer's understanding is that FTSE Russell announced in October 2025 that Vietnam would move to Secondary Emerging from September 2026. The manuscript calls HOSE a frontier exchange, while the abstract speaks of "emerging" markets.
**Evidence Anchor**: text: §1 "emerging frontier exchanges frequently operate under binding short-sale prohibitions and slower settlement cycles"
**Suggestion**: Verify and state the current classification, and use one term consistently.
**Severity**: Minor
**Confidence**: 3 — core expertise: index-provider classification; authors to verify

### W13: Prior Vietnamese evidence overstated
**Problem**: As its title indicates, Le et al. (2025) studies how Vietnam's dependence on Asian markets varies across quantiles. The manuscript cites it as confirming a causal retail-dominance mechanism.
**Evidence Anchor**: text: §1 "Recent empirical evidence from Vietnam confirms that retail dominance and liquidity constraints generate delayed price adjustments"
**Suggestion**: Replace "confirms ... generate" with wording that matches what the cited papers actually show.
**Severity**: Minor
**Confidence**: 2 — based on the cited titles; full texts not checked

### W14: Mid-cap ETF recommendation may overlook an existing product
**Problem**: The reviewer's understanding is that an ETF tracking VNMIDCAP has been listed on HOSE since about 2022, which would make the recommendation partly already implemented.
**Evidence Anchor**: text: §4.1 "listing dedicated mid-cap exchange-traded funds based on standalone benchmarks such as VNMIDCAP (VN70)"
**Suggestion**: Check which products are listed and reword the policy implication to fit.
**Severity**: Minor
**Confidence**: 3 — core expertise: Vietnamese fund products; authors to verify

### W15: The 2018 crisis window includes the pre-peak rally
**Problem**: VNINDEX peaked in April 2018. A January–December window therefore includes a rally. The "margin contraction" label is not documented.
**Evidence Anchor**: text: §2.1 "the 2018 margin contraction (January–December 2018; drawdown 26.2%, 47% of days in the top quartile)"
**Suggestion**: Justify the start date and the name of the trigger, or date the episode from the peak.
**Severity**: Minor
**Confidence**: 3 — core expertise: Vietnamese market history

### W16: Foundational attributions
**Problem**: DFA comes from Peng et al. (1994), which is cited correctly in §2.2. Kantelhardt et al. (2002) is its multifractal extension. In the same way, Markowitz (1952) does not document the practice of using static daily Pearson correlations.
**Evidence Anchor**: text: §1 "Building on Detrended Fluctuation Analysis (Kantelhardt et al. 2002)"
**Suggestion**: Fix the attributions.
**Severity**: Minor
**Confidence**: 4 — core expertise: method history

### W17: Practitioner behaviour in the motivation is asserted without evidence
**Problem**: The whole framing depends on allocators treating nested indices as separate diversifiers, but no source for this is given.
**Evidence Anchor**: text: Abstract "Asset allocators in emerging Southeast Asian markets frequently treat large-cap and broad-market indices as separate diversification instruments"
**Suggestion**: Give evidence for the claim, such as allocation practice or product structures, or soften it.
**Severity**: Minor
**Confidence**: 3 — core expertise: regional asset management
