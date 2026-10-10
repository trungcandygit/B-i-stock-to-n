contract_role: methodology

## Dimension Scores

### D1: methodology_rigor
score: block
trigger: "uncertainty omitted for an estimated input that drives a headline result"
block_class: repairable

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: block
trigger: "A formal result or a stated bound is false or holds only under conditions the paper does not state"
block_class: repairable

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

**Methodology Review Report (Peer Reviewer 1).** Reviewer identity: financial time-series econometrician (scale-dependent correlation estimators, resampling inference for dependent data), configured by Card #2. Recommendation from this seat: Major Revision. Confidence: 4 (proof algebra and inference code checked directly; regime and microstructure points rest on standard econometric results). Calibration status: `NOT_CALIBRATED`. Target context: `criteria_binding_unavailable`; no venue-alignment claim is made.

**Summary assessment.** The algebra of Proposition 1 is correct, and I reproduced Eqs. (7)–(9), the third corollary and the Table 5, Table 7 and Section 5.7 point values from the replication outputs. The inference machinery (joint stationary block bootstrap that recomputes every curve and derived statistic) is a real improvement over scale-wise HAC. Two problems with the argument and four problems with the inference stop me from recommending acceptance. On the argument: (i) the "floor" ρ̲ = (1 + κ²)^−1/2^ is the value at zero economic correlation, not a lower bound. For ρ~AM~ below zero the nested coefficient falls below it, down to (1 − κ²)^1/2^ ≈ 0.875 at ρ~AM~ = −κ, and the paper's own Fig. 3 shows this. (ii) H2 cannot fail for any plausible data, because the mechanical share is at least ρ̲, which exceeds 0.5 whenever κ is below √3. On inference: (iii) every interval for κ, the floor, the share and ρ~AM~ is conditional on w = 0.6826. Over the paper's own sensitivity range w ∈ [0.60, 0.75], the share moves from 0.84 to 0.95, about seven times the bootstrap interval width. (iv) The H3 null partly follows from B = 499: with 19 tests the smallest Holm-adjusted p that can occur is 0.076. With a family limited to the eight broad-market tests that H3 actually concerns, BH rejects all four intraday slopes. (v) Intraday returns include overnight and auction bars that carry 37% of M30 variance. (vi) The Forbes–Rigobon test for P~cap~–VN30 is biased toward "no contagion" when there are common shocks. All of these can be repaired with the existing data.

**Criterion-bound judgements** (field-general Q1/Q2 applied financial econometrics standards; not totalled or mapped mechanically to the recommendation):

| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| D3 formal result correctly stated | contract D3 | PARTLY_MEETS | equation: Eq. (8); figure: Fig. 3 | Identity correct; "floor" mislabelled as bound | none identified | yes, concerns the title concept |
| D3 hypotheses falsifiable | contract D3 | DOES_NOT_MEET | text: §2.5 H2 | H2 is guaranteed once κ is below √3 | none identified | yes |
| D1 uncertainty of derived quantities | contract D1 | DOES_NOT_MEET | text: §4.2 | w held fixed in every replicate | size of w uncertainty depends on the true weight path | yes |
| D1 multiplicity and p resolution | contract D1 | PARTLY_MEETS | table: Table 6 | Holm cannot reject at B = 499; family wider than H3 | none identified | yes, for H3 |
| D1 dependence and frequency design | contract D1 | PARTLY_MEETS | text: §3.1, §4.4 | overnight bars, block length vs scale | magnitude of effect unknown until rerun | moderate |
| D1 reproducibility | contract D1 | MEETS | dataset: project_R/outputs | numbers trace to R outputs; raw data not public | vendor licence | no |

### S1: Proposition 1 and its corollaries are algebraically correct
**Evidence Anchor**: equation: Eq. (7) and its proof in §4.2
I re-derived Eq. (7) from ε~B~ = wε~A~ + (1 − w)ε~M~ and the bilinearity of Eq. (4). I also re-derived the derivative in Eq. (9), κ²(κ + ρ)/D^3/2^, and the third corollary's identity ρ²~AB~ − ρ²~AM~ = (1 − ρ²~AM~)(1 + 2κρ~AM~)/D. All are correct. The stated conditions (0 < w < 1, F~A~, F~M~ > 0) are sufficient; F~B~ > 0 follows except in the degenerate case κ = 1, ρ~AM~ = −1.

### S2: Inference resamples the joint series and recomputes all derived statistics
**Evidence Anchor**: text: §4.4 "All inference therefore resamples the data."
The code (run_round2.R, run_revision.R) resamples rows of the joint return matrix. P~cap~ is rebuilt within each replicate, and κ, the floor, the share and the slopes are recomputed. Cross-scale dependence is therefore handled correctly, unlike treating scales as observations.

### S3: Null results are reported honestly with power
**Evidence Anchor**: table: Table 8
H3 and H4 are reported as not supported, and Table 7 gives power against an increase of 0.05. The Abstract describes the H3 pattern as not surviving adjustment.

### S4: Reported numbers trace to the replication outputs
**Evidence Anchor**: dataset: project_R/outputs/R8_overlap_decomposition.csv, R3_forbes_rigobon_pearson_bootstrap.csv, R4_portfolio_error_pearson.csv, R9_slope_tests_multiplicity.csv
I spot-checked Table 5 (floor 0.900 [0.891, 0.910], share 0.911 [0.903, 0.920]), Table 6 p-values, Table 7 (ρ* 0.803 and 0.661, p 0.985 and 0.974, power 0.77 and 0.41), the Section 5.7 RE values and Table A5. All match. The R1_filled_file_check output confirms that the "filled" input file forward-fills only USDVND, so the claim that no index level was filled holds.

### S5: Reliability calibration includes a heavy-tailed DGP and a sensitivity check
**Evidence Anchor**: table: Table 3
The GARCH(1,1)-t(5) calibration and the re-averaging over the shorter heavy-tailed ranges (Section 5.2) show that the H1 averages do not depend on the threshold choice.

### W1: The "mechanical floor" is not a lower bound when the economic correlation is negative
**Severity**: Major
**Evidence Anchor**: text: §2.5 "Proposition 1 implies that the nested coefficient cannot fall below a floor determined by index weights and relative volatility"
**Confidence**: 5 — direct calculus on Eq. (7)
By Eq. (9), ∂ρ~AB~/∂ρ~AM~ has the sign of κ + ρ~AM~. ρ~AB~ is therefore decreasing for ρ~AM~ below −κ and attains its minimum (1 − κ²)^1/2^ at ρ~AM~ = −κ when κ ≤ 1. With κ = 0.484 the minimum is 0.875 and the "floor" is 0.900. For κ ≥ 1 the infimum is −1, so no positive bound exists. The paper's own Fig. 3 shows the curve below the dashed floor line on [−0.5, 0). The claim recurs in §5.5 and §6.1 ("a floor below which the nested coefficient cannot fall"). ρ̲ is a lower bound only under the unstated condition ρ~AM~ ≥ 0. Fix: (a) define ρ̲ as the zero-economic-correlation benchmark, state that it bounds ρ~AB~ from below for ρ~AM~ ≥ 0, and give the global lower bound (1 − κ²)^1/2^ for κ below 1; (b) rewrite §2.5, §5.5, §6.1 and the Fig. 3 notes accordingly. The empirical estimates do not change, because ρ~AM~ ≈ 0.88.

### W2: H2 holds by construction and is not an informative test
**Severity**: Major
**Evidence Anchor**: text: §2.5 H2 "The mechanical floor accounts for more than half of the VN30–VN100 DCCA coefficient"
**Confidence**: 5 — algebra plus code inspection
Because ρ~AB~ ≤ 1, the share ρ̲/ρ~AB~ ≥ ρ̲ = (1 + κ²)^−1/2^. The share can fall to 0.5 only if κ ≥ √3, which at w = 0.6826 requires F~M~/F~A~ ≥ 3.72; the observed ratio is about 1.02. The one-sided bootstrap p is exactly 0 in every replicate (R8_overlap_decomposition.csv, `p_one_sided` = 0). H2 restates w ≈ 0.68 together with comparable volatilities. Fix: drop H2 as a confirmatory hypothesis and present the share as a descriptive consequence of Proposition 1, giving the analytic condition κ below √3. If an informative test is wanted, test something the identity does not fix, for example whether ρ~AB~(s) − ρ̲(s) differs across regimes or scales, or whether ρ~AM~ differs from ρ~AB~ by more than a stated economic margin.

### W3: H1 is partly mechanical for the decomposed pair and pools pairs the identity does not cover
**Severity**: Minor
**Evidence Anchor**: text: §2.5 H1 "the average reliable-range DCCA coefficient of the nested pairs exceeds that of the purged pair"
**Confidence**: 4 — follows from the third corollary
For VN30–VN100, the third corollary already guarantees ρ~AB~ ≥ ρ~AM~ once ρ~AM~ ≥ 0, so the empirical content is the size of the gap, not its sign. The other two nested pairs (VN30–VNINDEX, VN100–VNINDEX) have no decomposition, yet they enter the same average. Fix: report the gap separately by pair, state that the sign for VN30–VN100 is implied by Corollary 3, and reframe H1 around the magnitude (with an a priori economic margin) rather than "excludes zero".

### W4: All intervals for the decomposition are conditional on a single fixed weight whose uncertainty dominates sampling error
**Severity**: Major
**Evidence Anchor**: text: §4.2 "The weight is fixed from the factsheet before any estimation, so it is not tuned to the results"
**Confidence**: 5 — recomputed from the replication data
The bootstrap uses the global constant W in every replicate (run_round2.R, `W <- 1316288 / 1928303`), so the intervals for κ, ρ̲, the share, ρ~AM~ and the gap ignore weight uncertainty. Moreover, B = wA + (1 − w)M̂ holds exactly for every w, so the data alone do not identify the decomposition. I recomputed the daily reliable-range quantities with the authors' code: share 0.839 / 0.886 / 0.911 / 0.936 / 0.952 and ρ~AM~ 0.924 / 0.903 / 0.884 / 0.855 / 0.824 at w = 0.60 / 0.65 / 0.6826 / 0.72 / 0.75. At w equal to the OLS slope (0.971), ρ~AM~ = 0 and the share is 1; at w = 0.5 the share is 0.72. The w range in Table A2 alone moves the share by 0.11, against a bootstrap interval width of 0.017. A single May 2024 snapshot applied to 2014–2025 is the binding identification assumption, and Table A2 does not report the floor or the share. Fix: (a) collect the semi-annual HOSE factsheets (or month-end constituent capitalizations) to build a w~t~ path and recompute with time-varying weights; (b) failing that, draw w in each bootstrap replicate from the empirical range of historical factsheet weights and report the resulting intervals; (c) extend Table A2 to κ, ρ̲, the share and ρ~AM~; (d) validate P~cap~ against a VNMIDCAP series for the subperiod in which it is available, for example by estimating w in B = wA + (1 − w)VNMIDCAP.

### W5: The H3 null is partly an artefact of p-value resolution and of a family wider than the hypothesis
**Severity**: Major
**Evidence Anchor**: table: Table 6, notes "Holm and Benjamini–Hochberg (BH) adjustments are across all 19 reliable-range tests"
**Confidence**: 5 — recomputed from R9_slope_tests_multiplicity.csv
With B = 499 the smallest attainable two-sided p is 2/500 = 0.004, so the smallest Holm-adjusted p with m = 19 is 19 × 0.004 = 0.076. No Holm rejection at 5% was possible regardless of the data, and the reported Holm p of 0.076 is exactly this resolution floor. The 19-test family also includes the three statistical proxies (which §4.2 calls numerically unstable), four VN30–VN100 tests and four P~cap~–VN30 tests, none of which H3 predicts to be positive. Restricting the family to the eight broad-market tests that H3 concerns (VN30–VNINDEX and VN100–VNINDEX × 4 frequencies), BH-adjusted p-values for the four intraday slopes become 0.024 each and Holm rejects VN100–VNINDEX at M30 (0.032). The H3 conclusion therefore depends on two researcher choices. In addition, the "not for VN30–VN100" half of H3 is a claim of no effect and is supported only by non-rejection, and the broad-versus-nested contrast is never tested directly. Fix: (a) raise B to at least 9,999 for the slope statistics, or use bootstrap standard errors with a normal or studentized reference so that p-values are not bounded by resolution; (b) pre-specify the confirmatory family as the eight broad-market tests and report the 19-test family as a secondary analysis; (c) test the VN30–VN100 null by equivalence (TOST) with a stated margin; (d) test the slope difference between broad-market and nested pairs within the same bootstrap.

### W6: The intraday design does not handle overnight and auction bars, and block length is checked only at the daily frequency
**Severity**: Major
**Evidence Anchor**: text: §3.1 "the first and last 30-minute bars of each day are more volatile and less synchronous than midday bars"
**Confidence**: 4 — computed from the replication data; effect on the slopes untested
In the code, intraday returns are `diff(log())` over the whole series, so the first bar of each day contains the overnight return and the opening call auction. On the replication data the first M30 bar of each day is 10.2% of bars but carries 36.8% of VN30 M30 squared-return variation. The small-scale DCCA values that drive the intraday H3 slopes, and the Epps interpretation, are therefore mixtures of overnight and intraday co-movement, and the H4 bars have unequal durations. The bootstrap mean block is 20 × 10 = 200 bars at M30, below s~rel~ = 444. The stationary bootstrap also cuts across day boundaries and mixes intraday seasonal positions. Table A5 checks block length only for the daily gap. Fix: (a) re-estimate Table 6 and A1 excluding the first bar of each day (and the closing-auction bar), or after dividing returns by a time-of-day volatility profile (Andersen and Bollerslev 1997, Journal of Empirical Finance 4(2–3)); (b) repeat Table A5 at M30 and H1 for the slopes, with mean blocks of 10–80 trading days, and report a data-driven block length (Politis and White 2004, Econometric Reviews 23(1), with the Patton, Politis and White 2009 correction); (c) state the H4 bar definition.

### W7: Forbes–Rigobon identification for P~cap~–VN30 is not established
**Severity**: Major
**Evidence Anchor**: table: Table 7
**Confidence**: 4 — standard contagion-test econometrics
The FR correction assumes no common shocks, no feedback and constant β. With a common market factor, which §4.6 itself invokes (margin calls hitting both tiers), the correction is known to be biased toward "no contagion" (Corsetti, Pericoli and Sbracia 2005, Journal of International Money and Finance 24(8)). The point estimates are consistent with over-correction: ρ* falls below ρ~low~ in both definitions, with upper interval limits of 0.001 and 0.008. The quartile regimes are sorted on VNINDEX volatility, which contains P~cap~, while δ uses VN30 variance; conditioning on the volatility of a series that contains the dependent variable is a selection problem (Boyer, Gibson and Loretan, Federal Reserve IFDP 597). Finally, with a misspecified weight, Eq. (10) leaks (w~t~ − w)/(1 − w)·A into P~cap~, which mechanically makes its correlation with VN30 depend on Var(VN30), the quantity the test conditions on. Fix: (a) add a test robust to common factors, for example the Corsetti–Pericoli–Sbracia factor-model test or Rigobon (2003, Review of Economics and Statistics 85(4)) identification through heteroskedasticity; (b) define the quartile regimes on VN30 volatility, or on a series excluding P~cap~, and report two-sided intervals; (c) repeat Table 7 across the w grid of W4.

### W8: Portfolio-error intervals hold the static correlation fixed, and the purged-versus-nested comparison is untested
**Severity**: Minor
**Evidence Anchor**: dataset: project_R/run_revision.R, RR4 block, where the static correlation `rs` is computed once outside `replicate()`
**Confidence**: 5 — code inspection
ρ~st~ is estimated from the full sample, which contains the regime days, but it is not resampled. The intervals for RE therefore omit its sampling variation and its covariance with ρ~r~. The H5 rationale (error larger for the purged exposure than for nested cash portfolios) is asserted ("at most 2.35%") without an interval or a test. Fix: resample the full sample jointly and recompute ρ~st~ and ρ~r~ in each replicate; report the difference in |RE| between the purged and nested portfolios with an interval.

### W9: The reliability cut-off uses the less conservative calibration and is not propagated to the slope tests
**Severity**: Minor
**Evidence Anchor**: text: §5.2 "All averages below use the Gaussian thresholds"
**Confidence**: 4 — estimator finite-sample behaviour
Returns are heavy-tailed and volatility-clustered (Table 2), so the GARCH-t calibration is the relevant one, yet the Gaussian thresholds (about three times longer) are primary. The calibration grid stops at ρ~0~ = 0.9, while the nested coefficients are about 0.98, where the estimator's sampling variance is much smaller. Sensitivity to the GARCH-t range is shown only for averages, not for the H3 slopes, which are small (about 0.002 per log-scale unit) and range-dependent. The tolerance of 0.05 is half the size of the effect of interest (gap 0.09) and is not motivated. Fix: report Table 6/A1 over s ≤ s~rel~(GARCH-t), add ρ~0~ = 0.95, 0.98 to the calibration, and justify the 0.05 tolerance relative to the gap.

### W10: Bootstrap p-value and interval conventions need tightening
**Severity**: Minor
**Evidence Anchor**: text: §4.4 "two-sided bootstrap p-values computed as 2 min{(k₋ + 1), (k₊ + 1)}/(B + 1)"
**Confidence**: 4 — resampling inference practice
The formula needs a cap at 1 (the code applies one, the text does not). It is a percentile-inversion p-value of the uncentred bootstrap distribution, not a test under a null-imposed resampling scheme, and this should be stated. In the FR test, by contrast, the code re-centres the distribution, so two conventions coexist. The code reconstructs counts from stored proportions (`round(p*B/2)`), which is fragile. Percentile intervals for coefficients near 1 (nested 0.988) can be distorted, so Fisher-z or BCa intervals are preferable. Fix: state both conventions, store raw counts, and report the H2 and gap p-values as below 1/(B + 1) rather than omitting them.

### W11: The DMCA and tail-dependence checks are not independent tests of the floor
**Severity**: Minor
**Evidence Anchor**: table: Table A4
**Confidence**: 4 — follows from the bilinearity argument in §4.2
Section 4.2 notes that the identity holds for DMCA by bilinearity, so Table A3 checks only that the choice of estimator does not matter, not the decomposition itself. Table A3 also has no intervals. The finite-u lower-tail statistic λ~L~(u) rises with linear correlation even under a Gaussian copula, so "overlap also inflates joint crash probabilities" (§5.9) follows from the correlation gap and does not show any additional tail effect. Fix: add bootstrap intervals to Table A3, and benchmark λ~L~(u) against the Gaussian-copula value at each pair's own correlation, reporting the excess.

### W12: The zero slope of VN30–VN100 is attributed to Proposition 1, which does not predict it
**Severity**: Minor
**Evidence Anchor**: text: §5.5 "as Proposition 1 predicts: the coefficient is bounded below by its floor and almost insensitive to the economic correlation"
**Confidence**: 4 — follows from Eq. (7)
ρ~AB~(s) depends on s through both κ(s) and ρ~AM~(s). Low sensitivity dampens the slope but does not make it zero, and the "bounded below" premise fails per W1. The P~cap~–VN30 slope is also insignificant, so the flat nested slope does not distinguish the mechanical explanation from a generally flat scaling. Fix: derive the implied slope dρ~AB~/d ln s from Eq. (7) using the estimated κ(s) and ρ~AM~(s) paths, and compare it with the observed slope.

### W13: Data are not publicly reproducible
**Severity**: Minor
**Evidence Anchor**: text: Data availability "the merged dataset is available from the corresponding author upon reasonable request"
**Confidence**: 4 — reproducibility norms
The code is complete and deterministic, but the TradingView data cannot be redistributed. Fix: deposit code with a script that downloads or rebuilds the series from a public source (HOSE historical index files), or deposit derived returns where the licence allows, together with checksums of the input file.

### W14: "Accounts for" overstates what the mechanical share measures
**Severity**: Minor
**Evidence Anchor**: text: Abstract "the floor alone accounts for 0.905–0.911 of the observed VN30–VN100 coefficient"
**Confidence**: 4 — interpretation of a ratio
The share is the ratio of a counterfactual coefficient (at ρ~AM~ = 0) to the observed one, averaged over scales (a mean of ratios). It is not an additive decomposition of variance or covariance, and "accounts for" invites that reading. Fix: describe it as "the coefficient would still be 0.90, about 91% of its observed value, if mid caps were uncorrelated with large caps", and state that the share is a scale-average of ratios.

**Detailed comments (methodological fallacies checklist).** I found no survivorship bias, because the indices are official real-time levels. The main design risk is circularity: P~cap~ is constructed from A and B with an external w. Inference on κ, ρ̲ and the share is informative about sampling variation in relative amplitudes but not about the decomposition itself, which is fixed by w (W4). Confirmation-bias risk is low, since the nulls are reported. Multiple-testing handling is present but its family and resolution decide the outcome (W5).

**Questions for authors.** (1) What range of VN30/VN100 weights do the semi-annual factsheets 2014–2025 show? (2) Was the 19-test family fixed before the slopes were computed, and why does it include the statistical proxies? (3) How are H4 bars defined across the lunch break? (4) Do the M30 slopes survive excluding the first bar of each day?

## Arithmetic Receipts

### AR1
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 2, row VN30 1D
reported_inputs: Jarque–Bera 3,202, N 2,963, reported p below 0.01 (three asterisks)
assumptions: Jarque–Bera statistic referred to its defining asymptotic chi-square distribution with 2 df; upper-tail by family
test_family: chi_square
statistic_value: 3202
df: 2
reported_p_comparator: less_than
reported_p_value: 0.01
tail_convention: upper-tail
derivation: P(chi-square with 2 df exceeds 3202) equals exp(-3202/2) = exp(-1601)
derived_value_or_range: p approximately 1e-695, far below 0.01
comparison_rule: derived p is below the reported upper bound 0.01
status: consistent

### AR2
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 2, row VN100 1D
reported_inputs: Jarque–Bera 3,804, N 2,963, reported p below 0.01 (three asterisks)
assumptions: Jarque–Bera statistic referred to its defining asymptotic chi-square distribution with 2 df; upper-tail by family
test_family: chi_square
statistic_value: 3804
df: 2
reported_p_comparator: less_than
reported_p_value: 0.01
tail_convention: upper-tail
derivation: P(chi-square with 2 df exceeds 3804) equals exp(-1902)
derived_value_or_range: p approximately 1e-826, far below 0.01
comparison_rule: derived p is below the reported upper bound 0.01
status: consistent

### AR3
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 2, row VNINDEX 1D
reported_inputs: Jarque–Bera 3,898, N 2,963, reported p below 0.01 (three asterisks)
assumptions: Jarque–Bera statistic referred to its defining asymptotic chi-square distribution with 2 df; upper-tail by family
test_family: chi_square
statistic_value: 3898
df: 2
reported_p_comparator: less_than
reported_p_value: 0.01
tail_convention: upper-tail
derivation: P(chi-square with 2 df exceeds 3898) equals exp(-1949)
derived_value_or_range: p approximately 1e-846, far below 0.01
comparison_rule: derived p is below the reported upper bound 0.01
status: consistent

### AR4
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 2, row Pcap 1D
reported_inputs: Jarque–Bera 3,837, N 2,963, reported p below 0.01 (three asterisks)
assumptions: Jarque–Bera statistic referred to its defining asymptotic chi-square distribution with 2 df; upper-tail by family
test_family: chi_square
statistic_value: 3837
df: 2
reported_p_comparator: less_than
reported_p_value: 0.01
tail_convention: upper-tail
derivation: P(chi-square with 2 df exceeds 3837) equals exp(-1918.5)
derived_value_or_range: p approximately 1e-833, far below 0.01
comparison_rule: derived p is below the reported upper bound 0.01
status: consistent
