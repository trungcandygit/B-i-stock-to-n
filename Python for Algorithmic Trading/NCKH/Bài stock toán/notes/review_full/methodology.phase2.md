contract_role: methodology

## Dimension Scores

### D1: methodology_rigor
score: block
trigger: "Key inferential results rest on significance claims without a valid finite-sample or dependence-robust procedure"
block_class: repairable

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "Claims are somewhat overstated relative to effect sizes or uncertainty"

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Reviewer 1 (methodology). I am a financial econometrician working on DCCA/MF-DCCA, finite-sample inference, HAC regressions and the Forbes–Rigobon test. I read the manuscript and checked it against the R replication (`run_all.R`, `R/dcca.R`, `outputs/*.csv`). The manuscript contains no instruction-like text addressed to reviewers.

Overall assessment. The research question is sound and fits DCCA: how much of the correlation between nested indices is mechanical overlap rather than economic co-movement. The data construction is mostly traceable. Every number I spot-checked in Tables 2, 3, 4, 5, 6 and 7 and in Section 3.6 matches the R outputs. The problem is inference. All three headline claims depend on significance statements, or on point estimates without uncertainty, produced by procedures that do not hold here:
- The horizon-scaling slope uses a Newey–West regression across 30 overlapping scale points taken from a single sample.
- The Forbes–Rigobon test uses an iid Pearson-type standard error with nominal day counts. It is applied to a scale-20 DCCA coefficient estimated on concatenated, non-contiguous regime subsamples.
- The 0.086–0.096 overlap gap is reported with no sampling uncertainty. It also rests on an unvalidated single-snapshot weight.

Each defect is repairable with standard tools (block bootstrap or surrogate inference over whole DCCA curves, effective-sample-size corrections, a Pearson-consistent Forbes–Rigobon implementation, validation against VNMIDCAP). None invalidates the core estimand, so D1 is a repairable block, not a fatal one.

On D3, the manuscript generalises the horizon-dependence result to "intraday frequencies" when it holds only at M30. It also reads non-rejection of the Forbes–Rigobon null as positive evidence of no contagion. The body text hedges appropriately in places ("suggestive", Section 3.8.1), so I score D3 as warn rather than block.

Statistical-reporting judgement:
- Effect sizes and point estimates: MEETS.
- Confidence intervals or standard errors for the headline DCCA averages, gap, multifractal widths and variance errors: DOES_NOT_MEET.
- Validity of inference assumptions (independence, effective sample size, heavy tails): DOES_NOT_MEET.
- Multiple-testing and selective-reporting control across the 4 frequencies × 7 pairs × 2 ranges of scaling regressions: PARTLY_MEETS. Only M30 is tabulated, and the daily result is quoted selectively.
- Reproducibility affordances: PARTLY_MEETS. The code exists and reproduces the numbers, but it is available only on request.
- Uncertainty: medium. My judgements rest on the manuscript plus the R outputs, and I did not rerun the code.

### S1: Explicit finite-sample reliability threshold for the DCCA coefficient
The authors calibrate a maximum reliable scale per frequency by Monte Carlo. They restrict averages (Table 2) and a robustness regression (Table 6) to that range. This is better practice than most applied DCCA papers, which average over all scales up to N/4.
**Evidence Anchor**: text: §3.3 "The reliability threshold is the largest scale below the first scale at which the worst-case error exceeds 0.05."

### S2: Forbes–Rigobon test correctly restricted to the disjoint pair
The authors recognise that nested pairs violate the exogeneity condition by construction. They confine the formal test to Pcap–VN30 and flag the margin-call feedback channel as an identification boundary.
**Evidence Anchor**: text: §2.4 "We therefore restrict the formal test of a structural correlation increase to the Pcap–VN30 pair."

### S3: Sensitivity of the proxy to the capitalization weight
Table 7 re-estimates the mean correlation, the M30 slope and the regime correlations over w30 from 0.60 to 0.75. This directly addresses the main identifying input. The replication output `07_table7_weight_sensitivity.csv` reproduces every cell.
**Evidence Anchor**: table: Table 7 — Pcap statistics re-estimated for w30 = 0.60, 0.65, 0.6826, 0.72, 0.75

### S4: Reported numbers are reproducible from the R pipeline
All 32 cells of Table 2 match `02_table2_average_dcca.csv` to three decimals. This includes the Panel A synchronised-window N values (1,983 / 19,463 / 9,879 / 3,953). Table 4, Tables 5–6 (M30) and the Section 3.6 variance errors (15.63%, 2.44%, −2.10%, −1.83%, 1.32%, −0.19%) also match their output files.
**Evidence Anchor**: table: Table 2 — Panels A and B, nested-group, Pcap–VN30 and gap columns

### S5: Transparent downgrading of the reliable-range Pcap slope
The authors report that the Pcap–VN30 slope loses significance within the reliable range and label the result suggestive, rather than hiding it.
**Evidence Anchor**: text: §3.8.1 "relies partly on the longer, noisier scales, and we interpret it as suggestive"

### W1: HAC regression across scale points is not a valid inference framework for DCCA scaling
**Problem**: The 30 regressands ρDCCA(s) are deterministic functionals of the same two return series, computed on nested and overlapping boxes. Their "errors" are not a weakly dependent stationary sequence indexed by scale, so Newey–West asymptotics (T → ∞ with fixed lag) do not apply with T = 30 grid points. Three lags cannot capture the near-unit dependence between neighbouring log-spaced scales. The p-values in Tables 5, 6 and 7 are therefore not interpretable as sampling uncertainty about the true slope.
**Evidence Anchor**: text: §2.5 "We therefore use Newey and West (1987) heteroskedasticity- and autocorrelation-consistent (HAC) standard errors with a lag truncation of three"
**Why it matters**: The horizon-dependence contribution (Contribution 1, abstract) rests entirely on these p-values.
**Suggestion**: Obtain the sampling distribution of the slope by resampling the return data, not the scale points. Options include a stationary or moving-block bootstrap of the bivariate return series (block length chosen for volatility clustering), or IAAFT/phase-randomised surrogates that preserve each series' spectrum and cross-spectrum. Recompute the whole DCCA curve and the slope in each replicate. Report bootstrap CIs for βscale and for ρDCCA(smax) − ρDCCA(smin).
**Severity**: Major
**Confidence**: 5 — core expertise: DCCA inference and HAC estimation

### W2: Horizon dependence is specific to M30 and is contradicted at other frequencies in the authors' own outputs
**Problem**: Only M30 regressions are tabulated. The replication output `20_scale_regressions_hac.csv` shows the Pcap–VN30 slope is:
- not positive at the other intraday frequencies: H1 full-range −0.0003 (p = 0.82), H4 full-range 0.0001 (p = 0.93), H4 reliable-range −0.0020 (p = 0.099);
- negative and significant at 1D within the reliable range: −0.0040 (p = 0.032). The text quotes only the insignificant 1D full-range value (0.0014, p = 0.47).

Even at M30 the reliable-range curve (`06_dcca_curves.csv`) rises from 0.874 (s = 5) to 0.891 (s = 27) and is flat thereafter. The full-range significance draws on the unreliable tail, including 0.925 at s = 5,485, which rests on 8 boxes.
**Evidence Anchor**: text: Abstract "at intraday frequencies this co-movement tends to strengthen over longer holding horizons as microstructure frictions resolve"
**Why it matters**: The abstract, Contribution 1 and the Conclusion generalise to "intraday frequencies" a pattern that appears at one of three intraday frequencies. This is selective reporting across a 4 × 7 × 2 grid of tests with no multiplicity control.
**Suggestion**: Report the full frequency × range grid of scaling slopes (at least for Pcap–VN30 and the nested pairs) in a table or appendix, with resampling CIs per W1. Restate the claim as an M30-only, small-scale (roughly s ≤ 30 bars) Epps-type rise. Alternatively, drop the horizon-dependence claim from the abstract.
**Severity**: Major
**Confidence**: 5 — core expertise: multiscale scaling inference, verified against the authors' outputs

### W3: Forbes–Rigobon standard error uses nominal day counts and ignores estimation of δ
**Problem**: The SE treats ρ* and ρlow as Pearson correlations of iid bivariate-normal samples of size Ncrisis = 539 and Ncalm = 1,000 (or 739/739). Three problems follow:
- They are DCCA coefficients at s = 20 (18 in Panel B). The effective sample is about 2⌊N/s⌋ overlapping boxes (roughly 54 in crisis, 100 in calm), not N.
- The returns are heavy-tailed (kurtosis 8.15 for daily Pcap, Table 1) and volatility-clustered.
- ρ* is a nonlinear function of both ρhigh and an estimated δ, whose sampling error is omitted.

Together these understate the SE, plausibly by a factor of about 3. A symptom appears in `10_table4_forbes_rigobon.csv`: under this SE, even the nested pairs show adjusted crisis correlations significantly below calm correlations (t = −2.87, −3.63 in Panel A). The Pcap–VN30 value itself is t = −2.28 in the same direction.
**Evidence Anchor**: equation: §2.4 SE(ρ*−ρlow) — the terms (1−(ρ*)²)²/Ncrisis and (1−ρlow²)²/Ncalm use nominal day counts
**Why it matters**: The formal contagion test and its t/p values in Table 4 have no valid reference distribution. An understated SE biases toward rejection, so non-rejection probably survives. The significantly negative Panel A statistic, however, is an artefact, and the power of the test is unknown.
**Suggestion**: Bootstrap ρ*−ρlow by block-resampling within each regime (or across episodes for Panel A), recomputing ρhigh, ρlow and δ in each replicate. Report the CI and the implied power against a meaningful alternative, for example ρ* − ρlow = 0.05.
**Severity**: Major
**Confidence**: 4 — core expertise: Forbes–Rigobon test; effective-N factor is an order-of-magnitude estimate

### W4: DCCA on concatenated, non-contiguous regime subsamples, and δ measured on a different object
**Problem**: The regime correlations come from DCCA on subsamples spliced from non-adjacent dates. In Panel B, high- and low-volatility days are scattered through 2014–2025. So a "20-day" box spans non-consecutive days, and the cumulative profile integrates across calendar gaps, which removes the timescale interpretation. In addition, δ is the ratio of raw daily-return variances. The Forbes–Rigobon correction is derived for a Pearson correlation whose variance-ratio conditioning is on the same measure. The correlation being corrected is a scale-20 detrended covariance ratio, whose conditioning-variable variance ratio need not equal δ.
**Evidence Anchor**: text: §3.5 "Regime correlations are DCCA coefficients at a 20-day horizon estimated on the concatenated calm and turbulent subsamples of daily returns."
**Why it matters**: The Table 4 point estimates of ρlow, ρhigh and ρ* are not consistent estimates of the quantities the Forbes–Rigobon identity refers to. The headline "0.63 to 0.93" rise inherits this problem.
**Suggestion**: Report Pearson regime correlations with the Pearson-consistent δ as the primary Forbes–Rigobon test. If a DCCA version is kept, compute DCCA only within contiguous episodes (Panel A) and use the detrended variance ratio of VN30 at the same s as δ. For Panel B, use contiguous runs above or below the thresholds, discarding runs shorter than s.
**Severity**: Major
**Confidence**: 4 — core expertise: DCCA estimation and the Forbes–Rigobon identity

### W5: Portfolio variance error compares two different estimators
**Problem**: In `run_all.R`, ρstatic is the full-sample Pearson correlation of daily returns (0.889). ρregime is the scale-20 DCCA coefficient on a concatenated regime subsample (W4), and σ1 and σ2 are held at full-sample values. The 15.63% "overstatement" therefore mixes an estimator difference, a subsample-construction effect and a genuine regime effect.
**Evidence Anchor**: text: §3.6 "whereas the full-sample static correlation is 0.889, so the static model overstates portfolio variance by 15.63%"
**Why it matters**: This number appears in the abstract and in Contribution 3 as the economic cost of static models, but it is not an apples-to-apples comparison and carries no uncertainty.
**Suggestion**: Compute ρstatic and ρregime with the same estimator (Pearson on daily returns, or DCCA at the same s over the same kind of sample), with regime-specific σ. Report a bootstrap CI for RE, and state the 15.6% only if it survives.
**Severity**: Major
**Confidence**: 5 — verified directly in the replication code

### W6: Identification rests on a single 2024 weight snapshot applied to 2014–2025 and not validated against VNMIDCAP
**Problem**: Pcap uses a fixed w30 = 0.6826 from one May 2024 factsheet. Algebraically, corr(Pcap, R30) is a deterministic function of the VN30–VN100 variance–covariance matrix and w30. My check with the Table 1 daily moments and ρ(30,100) = 0.9885 gives about 0.88. So the "gap" is essentially a re-expression of VN30–VN100 moments through an assumed weight. Table 7 shows the gap moves from 0.052 to 0.153 across plausible weights.
**Evidence Anchor**: text: §2.2 "computed from the HOSE factsheet of May 31, 2024"
**Why it matters**: The headline gap and every Pcap-based result depend on w30 being right throughout the sample. The authors acknowledge this in Section 4.2, but the check is feasible now: daily VNMIDCAP levels are published by HOSE.
**Suggestion**: At least at daily frequency, validate Pcap against the exchange VNMIDCAP return (correlation, tracking error, and the DCCA curve of VNMIDCAP–VN30 against Pcap–VN30). Reconstruct a semi-annual w30 path from the constituent-review factsheets and re-estimate with the time-varying weight.
**Severity**: Major
**Confidence**: 4 — core expertise: index-decomposition identification; VNMIDCAP daily availability as reported in §2.1 caveat

### W7: No sampling uncertainty for the headline average correlations and overlap gap
**Problem**: Table 2 reports averages of ρDCCA over s ≤ srel and the nested-minus-Pcap gap to three decimals with no CI or SE. Section 3.2 then treats Panel A–B differences of up to 0.007 as negligible without a yardstick.
**Evidence Anchor**: absence: Table 2 and §3.2 — expected confidence intervals or bootstrap standard errors for the average DCCA coefficients and for the gap; checked §2.2, §3.2, Table 2 notes, §3.3, §3.8, §4.2
**Why it matters**: The gap is the paper's primary quantitative claim (title, abstract, Contribution 1).
**Suggestion**: Add block-bootstrap CIs for each Table 2 cell and for the gap, using the same resampling scheme as W1.
**Severity**: Major
**Confidence**: 4 — core expertise: finite-sample DCCA inference

### W8: The Podobnik-type t-test is described but never applied, and its distribution is questionable
**Problem**: Section 2.2 presents t(s) = ρ√(N−s−2)/√(1−ρ²) with a Student-t (N−s−2) null, attributed to Podobnik et al. (2011). As I understand it, that paper provides simulation-based critical values for ρDCCA under independent white noise, not an exact t distribution. The statistic is not used anywhere in Sections 3.1–3.8, and it would be invalid for dependent, heavy-tailed returns in any case.
**Evidence Anchor**: equation: §2.2 t(s) statistic with N−s−2 degrees of freedom attributed to Podobnik et al. (2011)
**Why it matters**: It is a dead methodological element with an unsupported distributional claim.
**Suggestion**: Remove it, or replace it with the simulation or surrogate critical values that are actually used, and apply them.
**Severity**: Minor
**Confidence**: 3 — core expertise, but source not re-read for this review

### W9: Reliability thresholds calibrated on iid Gaussian white noise
**Problem**: The thresholds srel come from iid Gaussian pairs, while the data show kurtosis up to 40.6 (Table 1) and volatility clustering. The criterion is also the worst-case mean absolute error across replications, which is closer to bias plus average dispersion than to a quantile of the error distribution.
**Evidence Anchor**: text: §3.3 "we simulate pairs of Gaussian white-noise series with known correlations"
**Why it matters**: The thresholds are probably optimistic for the actual data, which would shift the reliable range used in Tables 2 and 6.
**Suggestion**: Repeat the calibration with GARCH-t or block-bootstrapped surrogates that match the empirical marginal distributions and volatility persistence. Consider a 90th- or 95th-percentile error criterion.
**Severity**: Minor
**Confidence**: 4 — core expertise: DCCA finite-sample properties

### W10: Multifractal width rankings reported without uncertainty or a surrogate benchmark
**Problem**: The claim that Pcap has the largest width "at every frequency" rests on very small margins: in `09_mfdcca_width.csv`, M30 Pcap 0.495 against Pres 0.494, and H1 Pcap 0.435 against Pheur 0.428. There is no shuffled or phase-randomised surrogate to separate fat-tail multifractality from correlation multifractality. The h(q) fits use 24 scales up to N/4, well beyond srel.
**Evidence Anchor**: text: §3.4 "is the largest of all pairs at every frequency"
**Why it matters**: The "richer nonlinear cross-correlation structure" interpretation is not supported at the reported precision.
**Suggestion**: Report bootstrap CIs for Δh and surrogate-based widths, restrict the fits to s ≤ srel, and soften the ranking claim.
**Severity**: Minor
**Confidence**: 4 — core expertise: MF-DCCA

### W11: Possible inconsistency between the stated synchronisation and the data file used
**Problem**: The manuscript states exact inner joins, but `run_all.R` loads `vn_indices_merged_filled.csv`. The file name suggests forward-filled prices, which would create zero returns and non-synchronous bars, contrary to the stated procedure. I did not inspect the data file.
**Evidence Anchor**: text: §2.1 "the index series were synchronized by exact inner joins on timestamps"
**Why it matters**: Forward-filled bars would bias intraday correlations downward, which is an Epps-like artefact.
**Suggestion**: State whether any filling was applied, and report the count of filled bars per frequency.
**Severity**: Minor
**Confidence**: 2 — inferred from the file name only

### W12: Code and data available only on request
**Problem**: The R pipeline exists and reproduces the tables, but the manuscript offers it only on request.
**Evidence Anchor**: text: Code availability "The R code that reproduces every table and figure is available from the corresponding author upon request"
**Why it matters**: This limits independent verification. The TradingView licence may restrict the data, but not the code.
**Suggestion**: Deposit the code, and derived non-proprietary outputs, in a public repository with a DOI.
**Severity**: Minor
**Confidence**: 5 — directly observed

### W13: Non-rejection of the Forbes–Rigobon null is read as positive evidence of no contagion
**Problem**: Failure to reject H0: ρ* ≤ ρlow is interpreted as showing that the crisis rise "is a volatility effect", without a CI or power statement. In Panel A the statistic is significantly negative under the authors' own SE. The paper does not discuss this, and it would imply decoupling rather than unchanged interdependence.
**Evidence Anchor**: text: §3.5 "the apparent surge in large-cap/mid-cap correlation is a volatility effect rather than evidence of contagion"
**Why it matters**: The conclusion is stronger than the test can deliver.
**Suggestion**: Report CIs for ρ* − ρlow (see W3) and phrase the conclusion as "no evidence of a structural increase", with the detectable effect size stated.
**Severity**: Minor
**Confidence**: 4 — core expertise: contagion testing

Additional minor note. The detrending-order check (m = 1, 2, 3) is reported only for VN30–VNINDEX, the least informative pair. Repeating it for Pcap–VN30 would be more useful.

## Arithmetic Receipts

### AR1
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 4 Panel A Pcap–VN30 — t-stat −2.28, p-value 0.989
reported_inputs: asymptotic two-sample test of rho* against rho_low; statistic t = −2.28; reported p = 0.989 at three decimals
assumptions: standard normal reference as licensed by the stated two-sample asymptotic standard error; one-sided test of H0 rho* at most rho_low as stated in the Table 4 notes
tail_convention: one-tailed
derivation: p = 1 − Phi(−2.28) = Phi(2.28) = 0.98870; over the statistic rounding interval [−2.285, −2.275) the p-value spans 0.98855 to 0.98884
derived_value_or_range: 0.98855 to 0.98884
comparison_rule: consistent if the derived range intersects the rounding interval [0.9885, 0.9895) of the reported p
status: consistent

### AR2
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 4 Panel B Pcap–VN30 — t-stat 0.97, p-value 0.165
reported_inputs: asymptotic two-sample test of rho* against rho_low; statistic t = 0.97; reported p = 0.165 at three decimals
assumptions: standard normal reference as licensed by the stated two-sample asymptotic standard error; one-sided test of H0 rho* at most rho_low as stated in the Table 4 notes
tail_convention: one-tailed
derivation: p = 1 − Phi(0.97) = 0.16602; over the statistic rounding interval [0.965, 0.975) the p-value spans 0.16478 to 0.16727
derived_value_or_range: 0.16478 to 0.16727
comparison_rule: consistent if the derived range intersects the rounding interval [0.1645, 0.1655) of the reported p
status: consistent

### AR3
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 1 VN30 Daily — Jarque–Bera 3,202 marked significant at the 1% level
reported_inputs: Jarque–Bera statistic 3,202; reported significance p below 0.01
assumptions: Jarque–Bera statistic referred to its standard chi-square distribution with 2 degrees of freedom, which is the test's defining null distribution
tail_convention: upper-tail
derivation: p = P(chi-square with 2 df exceeds 3,202) = exp(−3,202/2), which underflows to 0 in double precision
derived_value_or_range: effectively 0, far below 0.01
comparison_rule: consistent if the derived p is below the reported 0.01 threshold
status: consistent
