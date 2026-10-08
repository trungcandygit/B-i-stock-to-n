contract_role: da
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: block
trigger: "A headline claim presented as an empirical or theoretical finding is shown by the manuscript's own definitions or tables to hold by construction or via circular validation"
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

Seat-level report; the completed-panel topology is not known at seat time. Criteria binding: `criteria_binding_unavailable` (no #684 manifest supplied); this report makes no venue-alignment claim.

### Basis for the D3 score
The D3 block trigger fires on M1: two of the three hypotheses Table 8 lists as "Supported" (H1 for its VN30–VN100 component, and H2) follow from the paper's own construction and Corollary 3, not from data that could have refuted them. The block is repairable: the decomposition, the sensitivity result (Eq. 9), the purged-correlation level, and the H4/H5 analyses form a non-circular core that can carry a reframed contribution. The fatal trigger does not fire. Nothing in the manuscript's numbers contradicts its central conclusion, and several substantive claims survive. If the authors recast H1/H2 as estimands, M2–M4 are fixed, and the abstract/introduction are toned down (M5, M6), I would expect D3 to move to warn or pass.

Genuine strengths, stated once: the identity in Eq. (7) is correct (I re-derived Eq. 7, Eq. 9 and the Corollary 3 difference formula; the replication file R8b reproduces the nested coefficient to machine precision). The authors report null results for H3 and H4 in Table 8 instead of hiding them. Power is reported for H4, the multiplicity adjustment for H3 is honest, and the paper itself calls Eq. (7) "an accounting identity rather than an estimated relation".

### Criterion-Bound Judgements
| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| D3a Non-circular hypothesis tests | Contract D3; Phase 1 D3 plan | DOES_NOT_MEET | §2.5 H1/H2; §4.2 Corollary 3; Table 8 | H1 (VN30–VN100 part) and H2 cannot fail under the paper's construction (M1) | H1 also averages two pairs not covered by the identity | yes; drives block |
| D3b Headline attribution uniquely supported | Contract D3 | PARTLY_MEETS | Abstract; §7; Table 5 | "Floor accounts for 0.91" depends on which counterfactual is subtracted first (M2) | none identified | yes |
| D3c Mathematical statements accurate | Contract D3 | PARTLY_MEETS | §2.5, §5.5, §5.7, §6.1; Fig. 3 | "floor" is called a lower bound; that holds only for nonnegative economic correlation (M4) | does not change the empirical magnitudes | yes |
| D3d Uncertainty matches claim precision | Contract D3 | PARTLY_MEETS | Table 5; Table A2; §4.2 | Intervals condition on a single-date w that alone sets the floor (M3) | my w-sweep uses Pearson inputs, not DCCA | yes |
| D3e Null results framed fairly | Contract D3 | MEETS | Table 8; §5.5; §5.6 | H3/H4 reported as not supported, with power and adjustments; residual spin is minor (m1) | none identified | no |
| D3f Claimed contribution matches what is shown | Contract D3 | PARTLY_MEETS | Abstract; §1; §2.4 | Novelty and motivating-practice claims exceed evidence (M5, M6) | prior-art citations need verification by R2 | yes |

### Strongest Counter-Argument
Strip away the vocabulary and the paper reports four numbers about two observed series: VN30 and VN100 returns correlate at 0.988, their volatilities are almost equal, and VN30 holds 68% of VN100 on one day in May 2024. Every entry in Table 5 is an algebraic transform of those inputs. The "economic correlation" is the correlation of VN30 with VN100 minus 0.68 VN30, rescaled. The "floor" is fixed by w: assuming equal volatilities, w/√(w²+(1−w)²) = 0.907, against the reported 0.893–0.900. The mechanical share is that floor divided by a number close to one. H2 asks whether this share exceeds 0.5. With w = 0.68 it would fail only if the purged proxy were about 3.7 times as volatile as VN30, so the test has no realistic chance of failing. H1, for the VN30–VN100 pair, is Corollary 3 restated. The tests that could have failed, H3 and H4, did fail. The narrative "the floor dominates" also depends on the order of attribution. The same numbers support the opposite headline: the economic correlation is 0.884, the overlap adds 0.104, so 89.5% of the observed coefficient is economic. Which story is true is a choice of convention, not a finding. The bootstrap intervals that make the headline look precise (0.895–0.920) hold w fixed. Over the weight range the paper itself treats as plausible, 0.60–0.75, the floor moves from about 0.83 to 0.94 and the share from 0.84 to 0.95, five times the reported interval width. The identity is the classical part–whole (item–total) correlation formula applied to a bilinear covariance, and it is proved in two lines. What survives is a useful, correctly computed measurement exercise: nested index correlations are insensitive to the economic correlation (slope about 0.11). It is not a set of confirmed hypotheses, and it does not establish a new theorem.

### Ignored Alternative Explanations/Paths
1. Reverse-order attribution. Subtract the economic correlation first: the overlap increment is ρ_AB − ρ_AM ≈ 0.104 (Table 5), so the overlap "accounts for" about 10% and economics for 90%. A Shapley-type average of the two orderings would lie between the two. The paper presents only the ordering that favours its title.
2. Weight misspecification as the source of the "economic" level and gap. Eq. (10) shows that a weight gap leaks VN30 returns into the proxy. A 2024 weight applied to 2014–2025 can bias ρ_AM, and therefore the H1 gap, in either direction. Table A2 shows the gap ranging from 0.052 to 0.153 over w, wider than any sampling interval in Table 4.
3. Forbes–Rigobon over-correction. With δ = 7.06 in the quartile regimes, the correction drives ρ* down hard, and it is known to be biased toward "no contagion" when common shocks or endogeneity are present. The authors concede that margin calls weaken exogeneity (§4.6). Their reading of a negative ρ* − ρ_low as a strong null (p = 0.985) is equally consistent with this correction bias. The replication package also contains a DCCA-based version (outputs/10_table4_forbes_rigobon.csv) in which the quartile ρ* (0.663) exceeds ρ_low (0.633), p = 0.165, so the sign of the point estimate depends on the measure.
4. The H5 sign switch is mechanical. A full-sample correlation lies between the calm and turbulent regime correlations, so the static value must overstate variance in calm regimes and understate it in turbulent ones. The ex-post, in-sample design cannot separate this from a forecasting cost.

### Missing Stakeholder Perspectives
- Index users who already know about the overlap. Anyone using a VN30/VN100 pair for diversification (the paper's motivating actor) is not documented. Fund documents, risk-model manuals or regulatory reports showing that practitioners use nested correlations as tier-diversification measures would test whether the problem exists in practice.
- The index provider (HOSE). Historical VN30/VN100 weight files would settle the identification of w. They exist through the semi-annual reviews, and the paper does not say whether they were requested.
- Risk managers working out of sample. The H5 portfolio claim speaks to them, but no out-of-sample regime-forecast evaluation is given; §6.3 concedes this.

### Unexamined Premise
The paper assumes that the attribution "mechanical versus economic" has a unique answer at the level of the correlation coefficient. Correlation is not additive in its components. Without a declared decomposition rule (counterfactual ordering, Shapley, or variance-share), "share of the coefficient" has no unique meaning. The sensitivity in Eq. (9) is order-free, and it is the defensible version of the claim.

### Observations (Non-Defects)
- Eq. (7), Eq. (9) and the Corollary 3 difference formula are algebraically correct; I checked them by hand. R8b reports identity errors of order 1e-16.
- The numbers in Table 5 match outputs/R8_overlap_decomposition.csv. The Table 7 and §5.7 numbers match outputs/R3_forbes_rigobon_pearson_bootstrap.csv and R4_portfolio_error_pearson.csv. Table A2 matches outputs/07_table7_weight_sensitivity.csv.
- The decision to restrict Forbes–Rigobon testing to the non-nested pair is correctly reasoned, and the restriction is disclosed.
- H3 and H4 are reported as not supported, and Table 8 does not spin them. The abstract's description of H3 is fair.
- The weight-sweep numbers in M3 are my own recomputation from Pearson inputs: daily σ_VN30 = 0.012131, σ_VN100 = 0.011910 and ρ = 0.98848, taken from outputs/14_portfolio_relative_error.csv. They show the direction and size of the w-dependence. They are not DCCA estimates, and the authors should replace them with DCCA-based values.

### Minor Issues

- **m1** (D3). After H3 fails adjustment, the text says the unadjusted pattern is "the one H3 predicts" and "fits the Epps effect". This partly re-asserts a hypothesis the paper rejects. Evidence Anchor — text: §5.5 "The unadjusted pattern is nevertheless the one H3 predicts". Confidence: 4 (direct reading). Fix: Keep one sentence calling it exploratory and hypothesis-generating; drop "fits".
- **m2** (D3). The VN30–VN100 zero slope is attributed to Proposition 1. The proposition does not predict a flat curve, because κ(s) itself drifts with scale (R8b: 0.474 to 0.533 at 1D). A non-significant slope is also not evidence of no slope without an equivalence test. Evidence Anchor — text: §5.5 "the VN30–VN100 slope is indistinguishable from zero in both ranges, as Proposition 1 predicts". Confidence: 4 (algebra plus replication file). Fix: Say Proposition 1 implies attenuation (slope about 0.11 times the ρ_AM slope plus a κ term); add a TOST or bound statement.
- **m3** (D3). "Prices the cost of static correlations" overstates an in-sample identity whose sign switch is mechanical (alternative 4). Evidence Anchor — text: §1 "prices the cost of static correlations". Confidence: 4 (definition of a pooled correlation). Fix: Recast H5 as a descriptive magnitude; say the sign pattern is expected by construction; drop "cost" unless an out-of-sample test is added.
- **m4** (D3). The H1 gap averages three nested pairs, two of which (VN30–VNINDEX, VN100–VNINDEX) have no purged counterpart. The like-for-like VN30–VN100 versus P~cap~–VN30 gap is about 0.104, not 0.086–0.096. Evidence Anchor — text: Table 4 notes "nested pairs: mean of VN30–VNINDEX, VN30–VN100 and VN100–VNINDEX". Confidence: 4 (table arithmetic). Fix: Report the like-for-like gap as primary; keep the three-pair mean as secondary.
- **m5** (D3). Claiming that index-level correlations "carry little information" sits uneasily with the paper's own point that Eq. (7) is invertible. The information is present but ill-conditioned (error amplification of about 9). Evidence Anchor — text: §6.2 "Eq. (7) shows how to recover the economic correlation". Confidence: 4 (direct reading). Fix: Rephrase as "a small change in the index-level number maps to a ninefold change in ρ_AM", that is, low signal-to-noise.
- **m6** (D3). The H4 point-estimate sign depends on the measure. The DCCA-based version in the package gives quartile ρ* above ρ_low (0.663 vs 0.633, p = 0.165), and the manuscript does not mention it. Evidence Anchor — dataset: outputs/10_table4_forbes_rigobon.csv, panel B, row Pcap-VN30. Confidence: 4 (read from package). Fix: Report the DCCA-based FR result as a robustness row, or state why only Pearson is admissible.
- **m7** (D3). P~cap~–VN30 is called a "disjoint pair" for FR exogeneity, but P~cap~ is built linearly from VN30. It is disjoint only if w is exact (Eq. 10). Evidence Anchor — text: §4.6 "This is plausible for the disjoint pair P~cap~–VN30". Confidence: 3 (depends on true weight path). Fix: State the condition; reference the M3 weight analysis.

### Issue List

#### CRITICAL
| # | Dimension | Issue Description | Evidence Anchor | Confidence | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|---|---|---|---|---|---|

#### MAJOR
| # | Dimension | Issue Description | Evidence Anchor | Confidence | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|---|---|---|---|---|---|
| M1 | D3 | H1 (for its VN30–VN100 component) and H2 are tested as falsifiable hypotheses and marked "Supported", yet they follow from construction. Corollary 3 guarantees that the nested coefficient exceeds ρ_AM whenever ρ_AM lies in [0,1). The share is at least the floor because ρ_AB is at most 1. The floor exceeds 0.5 unless κ exceeds √3, which at w = 0.68 requires the proxy's detrended amplitude to be about 3.7 times VN30's. The bootstrap "test" against 0.5 is therefore uninformative. Fix: recast H1/H2 as estimation targets (magnitudes with intervals), remove "Supported" for H2 in Table 8 (or replace the 0.5 threshold with a substantively motivated benchmark), and state explicitly that the sign of H1 for VN30–VN100 is implied by Corollary 3. | text: §2.5 "The mechanical floor accounts for more than half of the VN30–VN100 DCCA coefficient" and §4.2 "so overlap can only inflate the coefficient" | 5 (algebra verified by hand) | — | Severity rests on the manuscript's own Corollary 3 and Eq. (8), not on a field norm. |
| M2 | D3 | The headline "floor accounts for 0.905–0.911 / about nine-tenths" uses one counterfactual ordering (set ρ_AM to 0 first). The reverse ordering on the same Table 5 numbers gives overlap increment 0.988 − 0.884 = 0.104, so the economic part "accounts for" 89.5%. Because correlation is non-additive, the attribution is convention-dependent, and the abstract, contributions and conclusion present it as a unique fact. Fix: lead with the order-free sensitivity result (Eq. 9; 0.106–0.112); report both the floor and ρ_AM side by side with an explicit statement that the shares are not additive; drop "nine-tenths" or pair it with the reverse-order figure. | text: §7 "it accounts for about nine-tenths of the VN30–VN100 DCCA coefficient" | 5 (arithmetic from Table 5) | — | Severity rests on Table 5 arithmetic and the definition of the share. |
| M3 | D3 | The floor, share, sensitivity and ρ_AM are essentially set by w: under equal volatilities the floor is w/√(w²+(1−w)²) = 0.907 at w = 0.6826, close to the reported 0.893–0.900. Yet w comes from one factsheet dated 31 May 2024 and is applied to 2014–2025, and the reported intervals (0.895–0.920) hold w fixed. Recomputing from the paper's daily Pearson inputs over the paper's own range w = 0.60–0.75 gives floor 0.833–0.943, share 0.842–0.953 and sensitivity 0.161–0.066. Table A2 omits these quantities, so the H2 headline precision is overstated about fivefold. Fix: add floor, share, sensitivity and ρ_AM (DCCA) to Table A2; report headline ranges over plausible w; reconstruct w at each semi-annual review (or at minimum several dated factsheets) or propagate w uncertainty in the bootstrap. | table: Table A2 (columns w, Mean ρ, Gap to nested only) versus Table 5 floor and share intervals | 4 (Pearson recomputation, not DCCA) | — | Severity rests on the manuscript's own Table A2 range and Eq. (10) leakage, not on an external norm. |
| M4 | D3 | The "mechanical floor" is repeatedly described as a lower bound the nested coefficient "cannot fall" below (§2.5, §5.5, §5.7, §6.1). From Eq. (7), the bound holds only when ρ_AM is nonnegative. The global minimum (for κ below 1) is √(1−κ²), reached at ρ_AM = −κ: about 0.88 for κ = 0.475, below the 0.90 "floor". The paper's own Fig. 3 text shows 0.87 at ρ_AM = −0.5. Fix: either rename the quantity (for example "zero-correlation benchmark") or restrict every bound statement to nonnegative economic correlation and state the global bound √(1−κ²). | text: §6.1 "this fixes a floor below which the nested coefficient cannot fall" and §5.4 "the nested coefficient moves only from about 0.87 to 1" | 5 (closed-form minimisation of Eq. 7) | — | Severity rests on the manuscript's own Eq. (7) and Fig. 3. |
| M5 | D6 | Contribution 1 and the gap statement present Proposition 1 as a new exact result. It is the classical part–whole (item–total) correlation formula, the correlation of a component with a weighted sum containing it, extended to DCCA by the bilinearity the paper itself invokes; the proof is two lines. The zero-correlation floor 1/√(1+κ²) is the familiar uncorrected item–total correlation. Fix: cite the part–whole correlation lineage (psychometric item–total correction; own-asset inclusion in index betas), reposition Proposition 1 as an application or extension, not a discovery, and move the novelty claim to the empirical measurement for nested index systems. | text: §2.4 "and none derives that component exactly" and §1 "This paper answers it with an exact result." | 4 (prior-art citations to be verified by the domain seat) | — | Severity rests on prior-art existence, not a field norm; exact citations need verification. |
| M6 | D3 | The abstract and introduction motivate the paper with a practice ("often treated as separate diversification instruments") and claim to "show that this practice confuses index construction with economic co-movement". No evidence that the practice exists is given: the only citation is Markowitz (1952), and no fund, risk-model or regulatory source is cited. The paper shows an identity, not a practice. Fix: document the practice (fund prospectuses, multi-index allocation rules, risk-system defaults, Vietnamese fund documents), or soften to a conditional ("if nested correlations are used as diversification measures, then..."). | text: Abstract "Large-cap and broad-market indices are often treated as separate diversification instruments even when one index is a subset of the other" | 4 (absence of any cited practitioner source in §1–§2) | — | Severity rests on the absence of supporting evidence for the paper's own motivating claim. |

