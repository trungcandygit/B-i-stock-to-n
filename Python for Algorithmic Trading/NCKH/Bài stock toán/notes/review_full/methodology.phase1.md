## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by methodology): I must judge whether the empirical design can actually support the stated inferences. For a multiscale cross-correlation study this means the DCCA/MF-DCCA estimators are fully specified (profile construction, box sizes, detrending order, overlapping versus non-overlapping windows, q-range), the data pipeline is traceable (sample period, sources, return definition, treatment of missing days, holidays and index-constituent overlap), finite-sample uncertainty is quantified with a procedure appropriate to dependent and heavy-tailed data (surrogate, block bootstrap or known null distribution of the DCCA coefficient), regressions use HAC or otherwise dependence-robust inference, and enough detail (code, seeds, parameter tables) is disclosed for an independent replication.

D2 (domain_accuracy, mandatory, owned by domain): A separate reviewer checks that domain claims and prior literature are represented faithfully. From a methodology standpoint this matters because mis-stated properties of an estimator or test borrowed from prior work propagate directly into invalid inference, but I do not score this dimension.

D3 (argumentative_coherence, mandatory, owned by the devil's advocate, eligible for methodology): I must judge whether the conclusions follow from the evidence actually produced. My angle is inferential: whether the magnitude and statistical support of each result match the strength of the claim, whether causal or mechanism language is justified by the design, whether alternative explanations (mechanical overlap between nested indices, volatility bias in correlations, scale-selection artefacts, multiple testing) are ruled out, and whether the results section and the conclusions are internally consistent.

D4 (cross_disciplinary_relevance, high, owned by perspective): Another reviewer assesses whether definitions and implications are accessible to adjacent fields such as portfolio management and risk practice. Methodologically, clear operational definitions help, but I do not score this dimension.

D5 (writing_and_structure, normal, owned by the editor-in-chief): The editor evaluates organisation, clarity, figures, tables and venue conventions. Legible reporting of equations and tables supports reproducibility, but this dimension is outside my scoring remit.

D6 (venue_fit_and_contribution, mandatory, owned by the editor-in-chief): The editor judges fit to the configured Asia-Pacific finance venue and the originality of the contribution. A contribution can only be credited if the method is sound, yet the fit and novelty judgement itself is not mine to score.

## Scoring Plan

### D1: methodology_rigor
dimension_id: D1
what_to_look_for: Complete specification of DCCA/MF-DCCA estimators and parameters, traceable data construction, dependence-robust finite-sample inference (surrogate or bootstrap nulls for the DCCA coefficient, HAC standard errors), correct Forbes-Rigobon volatility adjustment with stated assumptions, handling of index-constituent overlap, robustness checks across scales and subsamples, and replication affordances such as code, seeds and parameter tables.
what_triggers_block: Key inferential results rest on significance claims without a valid finite-sample or dependence-robust procedure, or core estimator parameters and data construction are missing so the results cannot be reproduced or checked.
what_triggers_warn: The design is broadly sound but has gaps such as limited robustness across scales or subsamples, unreported multiple-testing control, incomplete parameter disclosure, or assumptions of the volatility adjustment stated but not tested.
what_triggers_fatal: The central estimand is mechanically invalid, for example the reported correlation or error metric is computed incorrectly or confounded by construction so that no revision of inference could rescue the main finding.

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: Alignment between the strength of each claim and the statistical evidence behind it, explicit treatment of alternative explanations such as mechanical overlap and volatility bias, consistent numbers and conclusions across results, discussion and abstract, and causal language limited to what the design identifies.
what_triggers_block: A headline conclusion is contradicted by, or not supported by, the reported evidence, or a plausible alternative explanation that would reverse the main claim is left unaddressed.
what_triggers_warn: Claims are somewhat overstated relative to effect sizes or uncertainty, some alternative explanations are only partially discussed, or minor inconsistencies appear between sections.
what_triggers_fatal: The central thesis is internally self-contradictory or rests on circular reasoning, so that the evidence presented cannot in principle support it.
criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
