## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by methodology). From a methodology-rigor lens this dimension asks whether the design can answer the stated questions: estimators suited to the data-generating process, inference procedures whose assumptions are met by the data's dependence and distributional features, effect sizes and uncertainty reported alongside tests, multiplicity handled with families fixed in advance, and enough code, data description and seeds that an independent analyst could reproduce every reported number.

D2 (domain_accuracy, mandatory, owned by domain). This dimension concerns whether claims agree with current domain evidence and whether prior work and terminology are represented correctly. It is not mine to score; I note only that methodological claims about estimator properties that cite prior literature fall into my lens when the issue is statistical correctness rather than literature coverage.

D3 (argumentative_coherence, mandatory, owned by da, methodology eligible). From a methodology-rigor lens this asks whether the inferential chain holds: formal results are proved correctly and under stated conditions, hypotheses are falsifiable rather than true by construction, the evidence actually tests what the conclusions claim, and conclusions do not exceed what the estimates and their uncertainty support.

D4 (cross_disciplinary_relevance, high, owned by perspective). This concerns accessibility and substantiation of interdisciplinary framing for adjacent-field readers. I do not score it.

D5 (writing_and_structure, normal, owned by eic). This concerns organisation, exposition, exhibit quality and venue conventions. I do not score it, although unclear statistical exposition that blocks replication is handled under D1.

D6 (venue_fit_and_contribution, mandatory, owned by eic). This concerns fit with the configured venue and originality and significance of the contribution. I do not score it and make no venue-alignment claim.

## Scoring Plan

### D1: methodology_rigor
dimension_id: D1
what_to_look_for: Estimator choice matched to data frequency and dependence; resampling scheme whose block structure, replication count and p-value resolution fit the dependence and the tail probabilities claimed; whether resampling propagates all estimated inputs; multiplicity families and thresholds fixed before results; calibration of reliability cut-offs; identification assumptions of any heteroskedasticity-adjusted or regime comparison; uncertainty for derived quantities; reproducible code with fixed seeds whose outputs match reported numbers.
what_triggers_block: A core inferential procedure is invalid or miscalibrated for the data (for example dependence structure ignored at the analysed frequency, p-values claimed below the attainable resolution, or uncertainty omitted for an estimated input that drives a headline result) but can be repaired by re-analysis with available data.
what_triggers_warn: Inference is broadly valid but has repairable gaps such as undocumented tuning choices, sensitivity analyses missing for block length or thresholds, under-justified calibration cut-offs, or minor mismatches between code outputs and reported values.
what_triggers_fatal: The central empirical claim rests on a design that cannot identify it at all, or on reported numbers that cannot be reproduced from the supplied code and data, such that no re-analysis within the paper's data could rescue the claim.

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: Correctness and stated conditions of any formal proposition and proof; whether bounds labelled as bounds hold in all sign cases; whether each hypothesis can fail given the construction of the variables; consistency between the test statistic used and the verbal claim; whether conclusions match the significance and size of estimates, including null results.
what_triggers_block: A formal result or a stated bound is false or holds only under conditions the paper does not state, or a confirmatory hypothesis holds mechanically by construction yet is presented as empirical support, while the core argument can be repaired by restating conditions or reframing the test.
what_triggers_warn: The argument is valid but some claims overreach the evidence, conditions are stated loosely, or interpretation leans on unadjusted or descriptive patterns without saying so.
what_triggers_fatal: The central formal result is wrong in a way that removes the paper's main claim, or the main thesis is circular so that the evidence offered cannot in principle bear on it.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
