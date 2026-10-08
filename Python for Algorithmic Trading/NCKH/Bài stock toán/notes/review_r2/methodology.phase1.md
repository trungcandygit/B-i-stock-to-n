# Reviewer 1 (Methodology), Phase 1: paper-content-blind pre-commitment

Contract: `reviewer/reviewer_full/v2` (panel_size 5). Dispatch role: `methodology`. Seat marker: R1.
Paper metadata supplied: title "The Mechanical Floor of Nested Index Correlations: An Exact Multiscale Decomposition with Evidence from Vietnam"; field: financial econometrics / econophysics / emerging-market finance; word_count about 11,200 (full file). No manuscript body was read before this file was written.

Protocol note: the dispatcher asked for a terminal `[PRE-COMMITMENT-ACKNOWLEDGED]` tag. The pinned grammar in `references/sprint_contract_protocol.md` §4 and in the agent file requires the final nonblank line to be exactly `[CONTRACT-ACKNOWLEDGED]`, and the conformance checker enforces that. I use the protocol tag and record the request here as acknowledged.

## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by methodology and scored only by me). From a methodology standpoint this asks whether the design can answer the paper's questions: whether the estimators are defined correctly and match the data, whether stated analytic results are proved, whether the inference procedures (resampling, multiplicity control, reliability screening, heteroskedasticity adjustment) are valid at the sampling frequencies and sample sizes used, whether uncertainty is reported for the quantities that carry the conclusions, and whether an outside researcher could rerun the pipeline and recover the reported numbers.

D2 (domain_accuracy, mandatory, owned by domain). This is about whether domain claims, prior work and terminology are represented correctly. It is outside my eligible roles; I will not score it, though I may note in prose a methodological point a domain reviewer would want to see.

D3 (argumentative_coherence, mandatory, owned by the Devil's Advocate, methodology also eligible). For me this is the inferential chain: whether each hypothesis is stated so that it can fail, whether the test applied actually discriminates between the competing explanations, whether a result that holds by construction is presented as an empirical finding, and whether the conclusions go further than the estimates and their uncertainty allow.

D4 (cross_disciplinary_relevance, high, owned by perspective). Accessibility and substantiation of interdisciplinary framing. Not eligible for me; not scored.

D5 (writing_and_structure, normal, owned by the Journal-Fit Reviewer). Organisation, clarity, figure/table quality, venue conventions. Not eligible for me; not scored, although reproducibility-relevant table or figure defects will be raised under D1.

D6 (venue_fit_and_contribution, mandatory, owned by the Journal-Fit Reviewer). Fit to venue and originality/significance. Not eligible for me; not scored.

## Scoring Plan

### D1: methodology_rigor
dimension_id: D1
what_to_look_for: Correct estimator definitions and detrending choices; a complete and correct proof of every stated analytic result with its assumptions; resampling inference whose block length, replication count and p-value resolution suit the sampling frequency, serial dependence and the multiplicity correction applied; clearly defined test families for Holm/BH control; reliability or screening thresholds that are calibrated and justified rather than ad hoc; identification assumptions stated for any heteroskedasticity or contagion adjustment; uncertainty intervals for derived quantities that drive conclusions; robustness to alternative estimators and tail-dependence measures; scripts, seeds, data provenance and a one-command rerun that reproduces the reported tables.
what_triggers_block: A load-bearing inference procedure is invalid or uninformative as applied (for example resampling that destroys the dependence it tests, a replication count whose minimum attainable p-value cannot pass the stated multiplicity threshold, an undefined test family, or a heteroskedasticity adjustment applied without its identifying assumption holding), or a headline number cannot be traced to the replication outputs; repairable by re-analysis without changing the research question.
what_triggers_warn: Inference is broadly valid but under-justified or under-reported: block length or replication count stated without sensitivity analysis, thresholds chosen without calibration evidence, missing confidence intervals for secondary derived quantities, partial robustness coverage, or minor mismatches between reported values and replication outputs that do not change any conclusion.
what_triggers_fatal: The central empirical claim rests on an estimator or statistical test that is mathematically wrong or cannot distinguish the claimed effect from its null in principle, such that no re-analysis within the stated design could support the headline conclusion, or the reported results are not reproducible from the provided code and data in a way that implies fabrication or irrecoverable error.

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: Each hypothesis is falsifiable with a threshold or null that has a substantive rationale; results that hold by algebraic construction are labelled as such and kept separate from empirical findings; the test reported for each hypothesis can reject it in the data at hand; conclusions are scoped to the single-market, single-period design; limitations raised in the text are reflected in the strength of the claims.
what_triggers_block: A core hypothesis is tested against a benchmark that the data satisfy mechanically or by construction, so the reported confirmation carries no evidential content, and the conclusions nonetheless rely on that confirmation; or a stated limitation directly contradicts a headline claim that is left unqualified.
what_triggers_warn: Hypotheses are testable but some thresholds lack motivation, by-construction results are only partly distinguished from empirical ones, or the wording of conclusions somewhat exceeds the scope of the evidence (one market, one period, proxy constructs) without undermining the core argument.
what_triggers_fatal: The central thesis is internally contradictory or circular, so that its main empirical conclusion is entailed by its own definitions and the paper offers no non-tautological claim that the evidence could have refuted.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
