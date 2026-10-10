# Editorial Decision Package (Round 2, `reviewer_full`)

Agent: `editorial_synthesizer_agent` (ARS `academic-paper-reviewer`, Phase 2 synthesis). Contract: `reviewer/reviewer_full/v2` (`vendor/academic-research-skills/shared/contracts/reviewer/full.json`, panel_size 5). Date: 2026-10-10.

Inputs read: `00_field_analysis_cards.md`; `eic`, `methodology`, `domain`, `perspective`, `da` `.phase1.md` and `.phase2.md`. The manuscript `project_R/docx_build/r2/manuscript_anonymized.md` was opened only to check anchors. All 18 quoted text anchors used below were found verbatim in it. No prior-round notes, ledger, roadmap or response files were read.

Instruction-data boundary: neither the manuscript nor the quotations in the cards contain text addressed to the panel or the synthesizer. Nothing to report.

Criteria binding: unbound run. All five cards disclose `criteria_binding_unavailable`, and the field-analysis card confirms that no Review Target Context was supplied. This package makes **no claim of alignment with any specific venue's criteria**. Venue-class statements refer to the field-general Q1/Q2 empirical-finance / econophysics class only.

## Calibration Resolution

`calibration_status: NOT_CALIBRATED`

Current runtime boundary: this package is not upgraded from a candidate or prose-named profile. `PROFILE_MEASURED` is unavailable because no closed profile artifact or replay validator binds this panel's execution topology.

## Review Panel Provenance (#540/#740)

- **Typed artifact**: **missing.** No `review-panel-provenance/1.0` artifact was supplied with the seat cards, so the carrier checks (raw digest, deterministic replay, normalized-manifest digest, execution-topology digest) could not be run. `[PROVENANCE-ARTIFACT-MISSING]`
- **Artifact SHA-256 / Panel ID / Normalized manifest SHA-256 / Execution topology SHA-256**: unknown
- **Fresh-context scope**: `within_panel_attempt_only` (does not compare retries or prior rounds)

| Seat | Role ID | Actor type | Context ID | Peer outputs visible | Model family | Provider | Human reviewer ID |
|---|---|---|---|---|---|---|---|
| Journal-Fit Reviewer | eic | unknown | unknown | unknown | unknown | unknown | unknown |
| R1 Methodology | methodology | unknown | unknown | unknown | unknown | unknown | unknown |
| R2 Domain | domain | unknown | unknown | unknown | unknown | unknown | unknown |
| R3 Perspective | perspective | unknown | unknown | unknown | unknown | unknown | unknown |
| Devil's Advocate | da | unknown | unknown | unknown | unknown | unknown | unknown |

| Provenance axis | Status (`true` / `false` / `unknown`) |
|---|---|
| Role-separated | unknown |
| Within-panel invocation-context separation | unknown |
| Blind to peer outputs | unknown |
| Model-family distinct | unknown |
| Provider distinct | unknown |
| Human-reviewer distinct | unknown |

- **Binary independence claim**: Not computed. Persona or role diversity proves only role separation. This panel is not described as independent.
- **Correlated-error disclosure**: Model-family provenance is incomplete; cross-family separation is unknown, so correlated-error risk cannot be ruled out.
- **Dispatcher attestation (not machine-verified, does not change the axes above)**: the dispatching session states that all five seats ran on **the same model family**, each in a fresh context, with no visibility of peer outputs. If that attestation is accurate, the model-family-distinct and provider-distinct axes would be `false`, and the fixed disclosure would read: "All model-executed review seats used one model family; role separation does not remove correlated-error risk." **Role separation is not independence.** Agreement across seats, especially on algebraic points (part–whole identity, H2 by construction, floor-as-bound), may reflect shared priors of one model family rather than separate confirmation. CONSENSUS labels below count roles, not independent experts. No human reviewer took part.

Cross-model blind decision check (#518): `ARS_CROSS_MODEL` is not set. Not run. Single-model decision.

---

## Part 0: Mechanical Derivation (sprint contract, arithmetic mode)

Pre-step, criteria binding: unbound run. All five cards disclose `criteria_binding_unavailable`, so no #684 marker comparison applies and no venue-alignment claim is made.

Layer-1 card validation: `check_panel_synthesis.py --layer1-only` on the five Phase 2 cards → `LAYER1-ONLY: PASS`.

### Step 1: Role-scoped scoring matrix

Only seats in each dimension's `eligible_roles` count. `not_assessed` from ineligible seats is excluded from numerator and denominator.

| Dim | Name | Priority | Eligible seats | Assessed eligible scores | n | Audit verdict |
|---|---|---|---|---|---|---|
| D1 | methodology_rigor | mandatory | methodology | methodology = block (repairable) | 1 | block |
| D2 | domain_accuracy | mandatory | domain | domain = block (repairable) | 1 | block |
| D3 | argumentative_coherence | mandatory | da, methodology | da = block (repairable); methodology = block (repairable) | 2 | block |
| D4 | cross_disciplinary_relevance | high | perspective | perspective = warn | 1 | warn |
| D5 | writing_and_structure | normal | eic | eic = warn | 1 | warn |
| D6 | venue_fit_and_contribution | mandatory | eic | eic = block (repairable) | 1 | block |

No eligible seat declared `block_class: fatal`. No dimension is unassessed.

Block/warn triggers as declared by the seats:
- D1 (R1): "uncertainty omitted for an estimated input that drives a headline result"
- D2 (R2): "A headline novelty or gap claim is contradicted by identifiable published precedent that the manuscript does not cite or distinguish"
- D3 (R1): "A formal result or a stated bound is false or holds only under conditions the paper does not state"; D3 (DA): "A headline claim presented as an empirical or theoretical finding is shown by the manuscript's own definitions or tables to hold by construction or via circular validation"
- D4 (R3): "no out-of-sample or benchmark check of economic magnitude"
- D5 (EIC): "peripheral analyses crowd the main line"
- D6 (EIC): "The core contribution is substantially a known or trivially derivable result presented as new"

### Step 2: Failure conditions

| ID | Sev. | Quantifier | Expression | Per-dimension evaluation | Fired |
|---|---|---|---|---|---|
| F1 | 95 | any | any mandatory dimension has a fatal block | D1, D2, D3, D6: no fatal block in any assessed eligible seat | false |
| F2 | 90 | any | any mandatory dimension scores 'block' | D1 (1/1 block), D2 (1/1), D3 (2/2), D6 (1/1): ≥1 true | **true** |
| F3 | 70 | majority | two or more mandatory dimensions score 'warn' or worse | majority per dim: D1 n=1 owner block → T; D2 n=1 → T; D3 n=2, both seats ≥ warn → T; D6 n=1 → T; 4 ≥ 2 | **true** |
| F4 | 60 | any | any high-priority dimension scores 'block' | D4 (only high dim): warn → F | false |
| F5 | 40 | any | any dimension scores 'warn' or worse | all six dims ≥ warn | **true** |
| F0 | 10 | all | every dimension scores 'pass' | no dimension passes | false |

### Step 3: Precedence and audit lines

The highest-severity fired condition is F2 (90), action `major_revision`. No fired action is softened. There are no DA CRITICAL findings: the DA card's `#### CRITICAL` table is empty, and its six issues M1–M6 are all MAJOR. The adjudication list is therefore empty and the DA-vs-Accept marker does not apply.

```
dimension_verdicts: [D1=block, D2=block, D3=block, D4=warn, D5=warn, D6=block]
fired_conditions: [F2, F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision
```

Checker result (`scripts/check_panel_synthesis.py --synthesis` on this file with the five Phase 2 cards): see the final section.

---

## Part 1: Editorial Decision Letter

Dear Author(s),

Thank you for submitting "The Mechanical Floor of Nested Index Correlations: An Exact Multiscale Decomposition with Evidence from Vietnam" for review at the field-general Q1/Q2 level (no specific journal bound). The manuscript went through five role-separated review seats: a Journal-Fit Reviewer, three peer-review roles (methodology, domain, practitioner/cross-disciplinary) and a Devil's Advocate. The provenance section above reports how they were executed. All seats ran on one model family, so their agreement does not amount to independent confirmation.

### Decision: Major Revision

The decision is derived mechanically from the contract: four mandatory dimensions (D1, D2, D3, D6) carry repairable blocks, so F2 fires and requires Major Revision. No seat declared a fatal block. The DA raised no CRITICAL issue. All four non-DA seats independently gave Major Revision as their advisory signal, so the mechanical result and the seat signals agree.

### Consensus Analysis

Counts are over the four non-DA seats (EIC, R1, R2, R3). "Silent" means the seat did not mention the point; silence is not disagreement. DA positions are listed separately.

#### Points of agreement

- **[CONSENSUS-3] Proposition 1 is the classical part–whole (component–sum / item–total) correlation identity, and the novelty claim in §2.4 and contribution 1 does not engage this prior art** (SC-1). Raised by EIC W1, R2 W1 and R3 W6. R1 was silent; R1 S1 confirms that the algebra is correct and does not address prior art. DA M5 concurs. → RR-1.
- **[CONSENSUS-3] Finance already purges overlap in other forms (ex-constituent benchmarks, the non-index-stock control in Barberis et al. 2005, holdings-overlap measures, heavyweight self-inclusion in index betas)** (SC-3). EIC W1, R2 W1 and R3 W6; R1 silent. → RR-1.
- **[CONSENSUS-3] H2 (mechanical share > 0.5) holds by construction once κ < √3, so it is not an informative confirmatory test** (SC-6). EIC W3, R1 W2, and R2 (Detailed Comments, Theoretical framework). R3 silent. DA M1 concurs. → RR-3.
- **[CONSENSUS-3] The data cannot be shared, which limits outside replication** (SC-17). EIC W10, R1 W13 and R3 W9; R2 silent. → RR-9.
- **[CONSENSUS-3] The "at most 2.35%" figure for parent–child cash blends is asserted without a table, interval or test** (SC-37). R1 W8, EIC Minor Issues and R3 Minor Issues; R2 silent. → RR-17.
- **Corroborated (2/4)**: the DCCA layer adds nothing over the Pearson floor in these data, so the "multiscale" headline is not delivered (SC-4: EIC W2, R3 W1). The economic premise that practitioners misuse nested correlations is not documented (SC-7: EIC W4, R3 W2; DA M6). The Forbes–Rigobon adjustment is biased toward "no contagion" under common shocks (SC-32: R1 W7, R2 W2). P~cap~ should be validated against the published VNMIDCAP (SC-23: R1 W4, R2 W4). H1's sign for VN30–VN100 follows from Corollary 3 (SC-20: R1 W3, R2). The H5 magnitude needs a materiality benchmark and out-of-sample check (SC-50: R3 W3, EIC Significance comment). Peripheral analyses crowd the main line (SC-9: EIC W5, R3 W8). Foreign-ownership limits and reclassification are missing (SC-47: R2 W7, R3 W10). The zero VN30–VN100 slope is wrongly attributed to Proposition 1 (SC-41: R1 W12, R2 W3). Figures 1 and 3 have readability problems (SC-12, SC-14: EIC W7/W9, R3 W8).
- **Single-reviewer findings with DA corroboration**: the "floor" is not a lower bound when ρ~AM~ < 0 (SC-19: R1 W1; DA M4). "Accounts for" / the attribution order is convention-dependent (SC-42: R1 W14; DA M2). Table A2 should be extended to the floor, share and sensitivity (SC-25: R1 W4; DA M3).

#### Points of disagreement (SPLIT) and tensions

| # | Issue | Positions | Type | Editor's resolution | Rationale |
|---|---|---|---|---|---|
| D-1 | Severity of the single fixed weight w and its missing path (SC-22) | R1 W4: Major (intervals conditional on w; share moves 0.84–0.95 against an interval width of 0.017). R2 W4: Major (ρ~AM~ ranges 0.824–0.924 across w). R3 W9: Minor (data provenance and weight path for uptake). | Severity | **Major retained** (RR-13, P0) | Evidence first: R1's recomputation and R2's reading of Table A2 both show weight uncertainty exceeding sampling uncertainty by a large factor, and R3 does not contest that magnitude. Expertise first: inferential validity is R1's remit. R3's practitioner point (exchange-certified data, weight path) is kept inside RR-13 and RR-9. |
| D-2 | Severity of over-generalisation and transferability (SC-10) | EIC W6: Minor (soften §7 or add a cross-market table). R3 W4: Major (transferability asserted, not shown; a nomogram plus cross-market table is cheap). | Severity | **Major retained, obligation should_fix** (RR-6, P1) | D4 is R3's owned dimension, and transferability is its stated competence. Both seats ask for the same remedy. The minimum acceptable fix is the floor nomogram in (w, σ~M~/σ~A~) plus §7 restricted to the HOSE. The cross-market table is strongly encouraged but left to the author, because R3 itself allows "(a) as the deliverable" if (b) is infeasible. |
| D-3 | Whether the decomposition can be extended to the broad-market pairs (VN100-in-VNINDEX) (SC-53) | R3 W4 and EIC Q4: the VN100-in-VNINDEX weight is published or obtainable, so extend. R2 Minor Issues: VNINDEX is full-cap-weighted and VN100 free-float-weighted, and that mismatch is why the decomposition does not extend. | Existence/direction | **Author's choice with stated reasoning** (in RR-6) | Both positions rest on index-construction facts the panel did not verify against primary rule books. The manuscript's own Eq. (10) shows that a parent that is not an exact fixed-weight sum leaks child returns into the remainder, which supports R2's caution. If the author extends, the weighting-scheme mismatch and its leakage must be stated and bounded. If not, §6.3 must give R2's reason. Unresolved on facts; flagged for the author. |
| T-1 | H3 multiplicity family (R1 W5) vs DA m1 (do not lean on the unadjusted H3 pattern) | R1: the null partly reflects B = 499 resolution (minimum Holm p = 0.076) and a 19-test family wider than H3; an 8-test family rejects. DA m1: drop "fits the Epps effect", call the pattern exploratory. | Direction tension (DA is outside the consensus count) | **Both kept, sequenced** (RR-14) | Raising B, or using non-resolution-bounded p-values, is uncontested and comes first. The family must then be reported transparently. The originally stated 19-test family stays as reported. Any narrower family must be justified from the H3 wording and labelled a revised specification introduced at revision, not a pre-registered one. Unless the re-analysis changes the verdict under the original specification, DA m1's exploratory language applies. |
| T-2 | Reading of the Forbes–Rigobon null | R1 W7 and R2 W2: biased toward the null; causal "interdependence" wording overreaches. R3 S3: the null is a useful first approximation for stress testing, with power 0.41 as a warning. | Perspective tension (not an existence dispute: R3 does not deny the bias) | **R1/R2 remedy required; R3 reading allowed only conditionally** (RR-16) | R3's practitioner reading survives only as "under constant-β and constant tier-specific variance". The author must carry that condition into §5.6, §6.1 and §6.2. |

Anticipated conflicts that did not materialise: the field cards expected R1 and R3 to disagree on the value of the DCCA layer over Pearson. R1 did not defend the DCCA layer on this point, and R2 S5 treats the Pearson equivalence as an accessibility strength, which is compatible with the EIC/R3 request (RR-2). The expected EIC-vs-R2 venue-class disagreement also did not arise: R2 gave no venue view, and EIC finds that the paper "tries to address all three readerships and fully satisfies none".

### Devil's Advocate Findings

- **DA-CRITICAL**: none. The DA's CRITICAL table is empty, so there is nothing to adjudicate and `da_critical_adjudications: []`.
- **DA MAJOR M1–M6** are all corroborated by at least one non-DA seat and are carried into the roadmap: M1 → RR-3 and RR-12; M2 → RR-22; M3 → RR-13; M4 → RR-11; M5 → RR-1; M6 → RR-4. DA minors m1–m7 are carried into RR-14, RR-21, RR-29, RR-12, RR-30, RR-16, and RR-13/RR-16 respectively.
- **DA's strongest counter-argument**: every Table 5 entry is a transform of w, two volatilities and ρ~AB~. The weight-sweep figures the DA computed from Pearson inputs (floor 0.833–0.943, share 0.842–0.953 over w = 0.60–0.75) are the DA's own recomputation, not DCCA results. They are cited here as the DA's evidence, not as verified numbers. RR-13 requires the authors to replace them with DCCA-based values from R.

### Decision Rationale

The paper's organising idea is coherent, its inference machinery is substantially improved (joint stationary block bootstrap recomputing all derived statistics), and it reports nulls honestly. Every seat records these as strengths (EIC S1/S4, R1 S2–S4, R2 S4, R3 S2/S4, DA Observations). The numbers the seats spot-checked match the R outputs (R1 S4; DA Observations). No seat found a fatal flaw.

Four mandatory dimensions are blocked, each for a reason that is repairable but central:

- **D2/D6, positioning.** The lead contribution, an "exact" identity no one has derived, is the classical part–whole correlation. The fix is reframing plus citation, not new data (RR-1).
- **D3, coherence.** The "floor" is called a lower bound but is one only for ρ~AM~ ≥ 0 (RR-11). The headline confirmatory hypothesis H2 cannot fail (RR-3).
- **D1, inference.** Every decomposition interval conditions on one 2024 factsheet weight whose plausible range moves the share several times more than the bootstrap width (RR-13). In addition, the H3 null is bounded by p-value resolution (RR-14), intraday bars mix overnight and auction returns (RR-15), and the Forbes–Rigobon test lacks common-factor robustness (RR-16).

Two warns complete the picture: D4 (practitioner premise, materiality and transferability not shown) and D5 (peripheral analyses).

What survives, per EIC, R2 and the DA, is a modest but genuine empirical contribution. The paper measures, with inference, that the nested coefficient is almost insensitive to the economic correlation (sensitivity about 0.11), that the floor and the purged correlation are of similar size, and that a closed-form diagnostic is portable. The revision should claim that and only that. Because several fixes require re-analysis in R (w propagation, B, intraday filtering, a robust contagion test, out-of-sample H5), the revised manuscript needs re-review.

### Blocking Issues (immutable source order)

| Transport ref | Blocking issue | Source reviewer(s) | Evidence anchor | Resolving roadmap item |
|---|---|---|---|---|
| R1 | Proposition 1 presented as new; it is the classical part–whole correlation (drives the D2 and D6 blocks) | EIC, R2, R3, DA | text: §2.4 "none derives that component exactly" | RR-1 |
| R2 | H2 (and the VN30–VN100 part of H1) hold by construction yet are reported as "Supported" (drives the DA D3 block) | EIC, R1, R2, DA | text: §2.5 "The mechanical floor accounts for more than half of the VN30–VN100 DCCA coefficient" | RR-3 (with RR-12) |
| R3 | All decomposition intervals are conditional on a single fixed w whose uncertainty dominates sampling error (drives the D1 block) | R1, R2, R3, DA | text: §4.2 "The weight is fixed from the factsheet before any estimation" | RR-13 |

Note: the R1 seat's own D3 block trigger (floor stated as a bound that fails for ρ~AM~ < 0) is resolved by RR-11. It is not listed above only because of the three-row cap.

---

## Part 2: Revision Roadmap

### Conventions

- **IDs are immutable.** RR-n is assigned in deterministic source order: the earliest originating finding in roster order (EIC → R1 → R2 → R3 → DA), then finding number. The ID is not a rank or a work order. Later rounds must reference these IDs, never renumber them.
- **Severity (P-level)**, assigned by a fixed rule from transported seat severity and the dimension's scored status (not re-rated):
  - **P0** = must_fix: a Major finding that is the trigger of, or directly drives, a block on a mandatory dimension (D1, D2, D3, D6).
  - **P1** = should_fix: a Major finding on a warn-scored dimension (D4, D5), a Major DA finding whose only non-DA support is Minor, or a Minor finding that is itself a declared warn trigger.
  - **P2** = consider (minor): every other Minor finding, and editorial items.
- **Transported severity** is copied from the cards (Major/Minor). For the R2 Theoretical-framework comment and the EIC Significance comment, which carry no tag, the row is marked `[SEVERITY-SOURCE: letter-fallback]`.
- **Confidence** is the seat's self-reported 1–5 scope disclosure. It is never used as a weight.
- **IRON RULE (citations)**: any reference a seat suggested is a lead until the authors verify it against the publisher or DOI record. Leads the seats marked [UNVERIFIED], and the DOIs R2 flagged for confirmation (Pearson 1896/1897 DOI and year; Rigobon 2003 DOI; Dimson 1979; Bekaert et al. 2005), must not be cited until verified. The FTSE reclassification statement (R2 W7 verified it; R3 W10 marked it [UNVERIFIED]) must be checked against the FTSE Russell primary announcement before inclusion.
- **R rule (repo)**: every new or changed number must come from R (`project_R/run_all.R`, fixed seeds, outputs in `project_R/outputs/`), and every acceptance criterion that involves a number includes "traceable to a named R output file".
- Machine artifact: a `revision-roadmap/1.0` JSON core was not emitted in this run. This markdown roadmap is the authoritative output; author triage belongs in a separate sidecar, not here.

### Summary table

| ID | Item | Sub-claims | Source seats | Transported severity | P | Obligation | Cost scope |
|---|---|---|---|---|---|---|---|
| RR-1 | Part–whole precedent; reposition novelty | SC-1, SC-2, SC-3 | EIC W1, R2 W1, R3 W6, DA M5 | Major | P0 | must_fix | section (§1, §2.4, §4.2, Table 1) |
| RR-2 | DCCA vs Pearson; "multiscale" not delivered | SC-4, SC-5 | EIC W2, R3 W1, DA counter-argument | Major | P0 | must_fix | section (title, abstract, §1, §4.2, §5.4) |
| RR-3 | H2 not falsifiable | SC-6 | EIC W3, R1 W2, R2 (fallback), DA M1 | Major | P0 | must_fix | section (§2.5, Table 5, Table 8) |
| RR-4 | Economic/practitioner premise unsupported | SC-7, SC-8 | EIC W4, R3 W2, DA M6 | Major | P0 | must_fix | section (Abstract, §1, §6.2) |
| RR-5 | Peripheral analyses crowd the main line | SC-9 | EIC W5, R3 W8 (Fig. 4) | Minor (D5 warn trigger) | P1 | should_fix | section (§4.2, §5.5, §5.8, Table 6, Online Resource) |
| RR-6 | Transferability; §7 over-generalisation; broad-pair extension | SC-10, SC-11, SC-53 | EIC W6, EIC Q4, R3 W4, R2 Minor | Major (R3) / Minor (EIC); SPLIT D-2, D-3 | P1 | should_fix | re_analysis (new figure/table) + section (§6.2, §6.3, §7) |
| RR-7 | Figure readability (Figs. 1–4) | SC-12–SC-15 | EIC W7, EIC W9, R3 W8 | Minor | P2 | consider | other (figures) |
| RR-8 | Abstract density | SC-16 | EIC W8 | Minor | P2 | consider | sentence (Abstract) |
| RR-9 | Data availability / replication from public source | SC-17 | EIC W10, R1 W13, R3 W9 | Minor (CONSENSUS-3) | P2 | consider | other (data statement, replication script) |
| RR-10 | Editorial minor-issue bundle | SC-18 | EIC, R2, R3 Minor Issues | Minor | P2 | consider | sentence |
| RR-11 | "Floor" is not a lower bound for ρ~AM~ < 0 | SC-19 | R1 W1, DA M4 | Major | P0 | must_fix | section (§2.5, §5.4, §5.5, §5.7, §6.1, Fig. 3 notes) |
| RR-12 | H1 partly mechanical; pools uncovered pairs | SC-20, SC-21 | R1 W3, R2 (fallback), DA M1, DA m4 | Minor (R1) / Major (DA) | P1 | should_fix | re_analysis (Table 4) + section (§2.5) |
| RR-13 | Weight uncertainty, w path, proxy validation | SC-22–SC-25 | R1 W4, R2 W4, R3 W9, DA M3, DA m7 | Major (SPLIT D-1 resolved Major) | P0 | must_fix | new_data (factsheets, VNMIDCAP) + re_analysis |
| RR-14 | Multiplicity, p-value resolution, H3 family | SC-26–SC-28 | R1 W5, DA m1, DA m2 | Major | P0 | must_fix | re_analysis (Table 6, A1) |
| RR-15 | Intraday overnight/auction bars; block length at intraday | SC-29, SC-30 | R1 W6 (+R2 W6 midday break) | Major | P0 | must_fix | re_analysis (Table 6, A1, A5, H4 bars) |
| RR-16 | Forbes–Rigobon bias and identification | SC-32–SC-35 | R1 W7, R2 W2, DA alt. 3, DA m6, DA m7 | Major | P0 | must_fix | re_analysis (Table 7) + section (§5.6, §6.1) |
| RR-17 | H5 intervals omit ρ~st~ variation; 2.35% untested | SC-36, SC-37 | R1 W8, EIC Minor, R3 Minor | Minor | P2 | consider | re_analysis (§5.7, appendix table) |
| RR-18 | Reliability cut-off and calibration grid | SC-38 | R1 W9 | Minor | P2 | consider | re_analysis (Table 3, Table 6/A1) |
| RR-19 | Bootstrap p-value and interval conventions | SC-39 | R1 W10 | Minor | P2 | consider | section (§4.4) + re_analysis (counts, intervals) |
| RR-20 | DMCA and tail checks are not independent tests | SC-40 | R1 W11 | Minor | P2 | consider | re_analysis (Tables A3, A4) + sentence (§5.9) |
| RR-21 | Zero VN30–VN100 slope wrongly attributed to Prop. 1 | SC-41 | R1 W12, R2 W3, DA m2 | Minor | P2 | consider | re_analysis (implied slope) + sentence (§2.5 H3, §5.5) |
| RR-22 | Attribution order; "accounts for" | SC-42 | R1 W14, DA M2 | Minor (R1) / Major (DA) | P1 | should_fix | sentence (Abstract, §1, §5.4, §7) |
| RR-23 | H3 grounding: size lead–lag and stale prices | SC-43 | R2 W3 | Minor | P2 | consider | section (§2.5, §6.1) |
| RR-24 | Policy recommendations unsupported; VNMIDCAP ETF exists | SC-44, SC-45 | R2 W5, R3 W5 | Minor (R2) / Major (R3) | P1 | should_fix | section (§5.7, §6.2) + re_analysis (hedge effectiveness, optional) |
| RR-25 | Institutional facts: short sale, decree amendment, settlement dates, midday break | SC-31, SC-46 | R2 W6 | Minor | P2 | consider | sentence (§3.1) |
| RR-26 | FOL, reclassification, comparative statics of the floor | SC-47 | R2 W7, R3 W10 | Minor | P2 | consider | section (§3.1, §6.1, §6.2) |
| RR-27 | Membership literature (weights; contested comovement) | SC-48 | R2 W8 | Minor | P2 | consider | section (§2.2) |
| RR-28 | Vietnamese studies used analytically | SC-49 | R2 W9 | Minor | P2 | consider | section (§2.2, §5.5, §6.1) |
| RR-29 | H5 materiality, out-of-sample, EWMA comparator | SC-50, SC-51 | R3 W3, EIC Significance (fallback), DA alt. 4, DA m3 | Major (D4 warn trigger) | P1 | should_fix | re_analysis (new OOS table) + sentence (Abstract, §1, §7) |
| RR-30 | Practitioner recipe; §6.2 "recover" sentence | SC-52 | R3 W7, R3 Minor, DA m5 | Minor | P2 | consider | section (box in §4.2 or §6.2) |

Counts: **P0 = 9** (RR-1, 2, 3, 4, 11, 13, 14, 15, 16); **P1 = 6** (RR-5, 6, 12, 22, 24, 29); **P2 = 15**. Total 30.

### Item details

**RR-1 — Reposition Proposition 1 against the part–whole correlation tradition and finance overlap precedents** (P0, must_fix)
- Sources: EIC W1 (Major, conf. 4), R2 W1 (Major, 5), R3 W6 (Major, 3), DA M5 (Major, 4). Disposition: CONSENSUS-3 (R1 silent).
- Anchor: text: §2.4 "First, no study we found separates the mechanical component of correlations between overlapping indices from economic co-movement, and none derives that component exactly."; text: §1 "This paper answers it with an exact result."
- Required change: (a) cite the part–whole / spurious-correlation lineage (R2 leads: Pearson 1897; Cureton 1966) and the finance overlap precedents (R2: Barberis et al. 2005 non-index-stock control; Cremers and Petajisto 2009 Active Share; EIC: ex-constituent / ex-country benchmark practice), each verified. (b) Relabel Proposition 1 as the scale-wise, detrended adaptation of a known identity (EIC suggests "lemma" or "result"). (c) Rewrite the first gap in §2.4 and contribution 1 so the claimed novelty is measuring the floor, its sensitivity and its scale/regime behaviour in a real nested system, with inference and diagnostic use (R2 W1(ii)). (d) Add a Table 1 row for part–whole and holdings-overlap precedents with "Overlap treated: Yes (Pearson, static)". (e) Extend the literature search beyond 2021–2026 and beyond DCCA outlets, and report the search strings (R2 W1(iv), SC-2).
- Acceptance criterion: no sentence in the Abstract, §1, §2.4, §4.2 or §7 claims that the identity itself is new. At least one verified classical part–whole source and at least one verified finance overlap source are cited and distinguished. Table 1 contains the precedent row. The search strategy is reported.

**RR-2 — State plainly that the DCCA layer adds nothing over Pearson in these data, and either justify or moderate "multiscale"** (P0, must_fix)
- Sources: EIC W2 (Major, 4), R3 W1 (Major, 4); DA strongest counter-argument. R2 S5 (Pearson equivalence as a strength) is compatible. Disposition: corroborated 2/4.
- Anchor: text: §5.4 "The same identity applied to full-sample Pearson correlations of daily returns gives a floor of 0.903 and a mechanical share of 0.914"
- Required change: choose one of the two remedies both seats offer. (a) Show a setting where κ(s) or ρ~AM~(s) varies materially with scale (crisis sub-samples, scales below the reliable range, another nested pair). (b) Reframe the title, abstract and contributions around the nested-correlation diagnostic, present the Pearson/covariance version as the practitioner tool, and report scale and frequency invariance of the floor (range of κ across scales) as an explicit finding. EIC judges (b) cheaper and more honest.
- Acceptance criterion: the title and contribution list no longer promise scale-dependent content that the results do not show; or a reported R output shows material scale variation. A sentence states the κ range across scales and frequencies and that the Pearson floor suffices in these data.

**RR-3 — Remove H2 as a confirmatory hypothesis** (P0, must_fix)
- Sources: EIC W3 (Major, 4), R1 W2 (Major, 5), R2 Detailed Comments, Theoretical framework ("given w ≈ 0.68 they hold almost by construction") [SEVERITY-SOURCE: letter-fallback], DA M1 (Major, 5). Disposition: CONSENSUS-3 (R3 silent).
- Anchor: text: §2.5 "*H2 (mechanical dominance).* The mechanical floor accounts for more than half of the VN30–VN100 DCCA coefficient."; dataset: R8_overlap_decomposition.csv `p_one_sided` = 0 (R1 W2).
- Required change: present the share as a descriptive consequence of Proposition 1 and state the analytic condition κ < √3 (equivalently F~M~/F~A~ < 3.72 at w = 0.6826). Remove "Supported" for H2 in Table 8, or replace the 0.5 threshold with a substantively motivated benchmark. If a test is wanted, test something the identity does not fix. Seat options: cross-regime or cross-scale variation of ρ~AB~ − ρ̲ (R1, EIC); whether ρ~AM~ differs from ρ~AB~ by more than a stated economic margin (R1); information content given the sensitivity (EIC). R2 accepts keeping it only as quantification of an identity.
- Acceptance criterion: no hypothesis in §2.5 or Table 8 can be settled by w and a rough volatility ratio alone. The κ < √3 condition appears in the text. Any replacement test has a decision rule stated before its R output is reported.

**RR-4 — Document or narrow the motivating practice** (P0, must_fix)
- Sources: EIC W4 (Major, 3), R3 W2 (Major, 4), DA M6 (Major, 4). Disposition: corroborated 2/4.
- Anchor: text: Abstract "Large-cap and broad-market indices are often treated as separate diversification instruments even when one index is a subset of the other."; text: §1 "... with a single Pearson correlation of daily returns (Markowitz 1952)".
- Required change: name the user groups that feed nested index-level correlations into decisions (R3: strategic asset-allocation inputs, simplified VaR proxies, ETF/benchmark comparison, Vietnamese fund practice) and give documentary sources where they exist. State that holdings-based factor risk models are not affected (SC-8). If no practice can be documented, soften to a conditional ("if nested correlations are used as diversification measures...", DA) or reframe around measuring segment co-movement when no segment index is published (EIC).
- Acceptance criterion: Markowitz (1952) is no longer the only support for the practice claim. Either at least one verified practitioner, regulatory or academic source documents the use, or the claim is conditional. One sentence scopes out holdings-based models.

**RR-5 — Move peripheral material out of the main line** (P1, should_fix)
- Sources: EIC W5 (Minor, 4; the D5 warn trigger), R3 W8 (Minor, 4; Fig. 4 has no decision use). Disposition: corroborated 2/4.
- Anchor: text: §4.8 "we therefore treat the multifractal results as descriptive and base no hypothesis test on them."
- Required change: move §5.8/Fig. 4 and the statistical-proxy comparison (§4.2 last paragraph; Table 6 rows for P~heur~/P~ratio~/P~res~) to the Online Resource. Shorten H3 to the extent consistent with RR-14. Keep H4/H5 in the main text only if they are tied explicitly to the decomposition (EIC).
- Acceptance criterion: the main text carries only analyses that use or test the decomposition. Moved material is cross-referenced in the Online Resource. The main-text word count falls (the author reports before and after counts).

**RR-6 — Show transferability cheaply and restrict §7 to the evidence** (P1, should_fix; SPLIT D-2 and D-3)
- Sources: EIC W6 (Minor, 4), EIC Q4, R3 W4 (Major, 4), R2 Minor Issues (§3.2 weighting difference).
- Anchor: text: §7 "Risk models and benchmark design in nested index systems should therefore rely on non-overlapping segment returns or on the decomposition derived here."; text: §6.2 "the identity applies directly, but the size of the floor depends on their weights and volatilities and must be estimated"
- Required change: (a) **minimum**: a figure or table of the floor as a function of w and σ~M~/σ~A~ (contour/nomogram), generated in R, plus §7 recommendations limited to the HOSE or explicitly conditioned on κ. (b) **encouraged**: an illustrative table of approximate floors for 2–3 other nested systems (e.g., SET50/SET100, IDX30/LQ45, S&P 500/Russell 1000) from published weights and public return histories. (c) State the partial-overlap boundary condition (SC-11). (d) On the broad-market pairs (D-3), either extend with the weighting-scheme mismatch stated and its leakage bounded, or state in §6.3 that the full-cap vs free-float mismatch is why the decomposition is not extended.
- Acceptance criterion: (a) and (c) are present; the cross-market table is present or its omission is explained. The §6.3/§7 text addresses D-3 one way or the other. All new numbers trace to R outputs, with sources for every weight.

**RR-7 — Fix figure readability** (P2, consider)
- Sources: EIC W7 (Minor, 3), EIC W9 (Minor, 3), R3 W8 (Minor, 4). Fig. 3 (SC-12) and Fig. 1 (SC-14) are corroborated 2/4; Fig. 4 (SC-13) and Fig. 2 (SC-15) are single-reviewer.
- Anchor: figure: Fig. 3, axis range −0.5 to 1 with markers near (0.88, 0.99); figure: Fig. 4(a), f(α) < 0; figure: Fig. 1, unshaded spike near 2021Q1.
- Required change: Fig. 3: zoom or inset (or replace with the RR-6 nomogram). Fig. 4: separate axis labels and a note on negative f(α), or move it (RR-5). Fig. 1: legend for the percentile lines; state why early 2021 is excluded (drawdown criterion) and confirm in a footnote that Table 7 is unchanged if it is included or excluded. Fig. 2: direct labels or a lighter band.
- Acceptance criterion: each listed figure is regenerated in R with the change. The Fig. 1 footnote cites the R output that confirms Table 7's robustness.

**RR-8 — De-densify the abstract** (P2, consider)
- Sources: EIC W8 (Minor, 4). Single-reviewer finding.
- Anchor: text: Abstract "(block-bootstrap 95% intervals within 0.895–0.920)"
- Required change: at most about three numbers (floor share, sensitivity, purge gap), the takeaway in plain words, intervals moved to the body. Abstract numbers must reflect RR-3, RR-13, RR-22 and RR-29.
- Acceptance criterion: the abstract has three or fewer numeric quantities and one explicit takeaway sentence. Every number in it matches an R output.

**RR-9 — Make replication possible from a public source** (P2, consider)
- Sources: EIC W10 (Minor, 3), R1 W13 (Minor, 4), R3 W9 data-provenance part (Minor, 3). Disposition: CONSENSUS-3 (R2 silent).
- Anchor: text: Data availability "the merged dataset is available from the corresponding author upon reasonable request."
- Required change: state whether official HOSE index levels can be obtained publicly. Provide a script that rebuilds the series from such a source, or deposit licence-permitted derived data (returns or fluctuation functions) with checksums of the input file. State whether the vendor series match exchange closing levels on a sample of dates (R3).
- Acceptance criterion: the data statement names a public route or a deposited derived dataset, and the replication README documents the input checksum and the vendor-vs-exchange check.

**RR-10 — Editorial minor-issue bundle** (P2, consider; single-reviewer items)
- Sources and changes: EIC: add an appendix table for the §5.7 "2.35%" values (also RR-17); remove stray commas in subscripts P~heur,~, σ²~ε,~, ρ~low,~; write the §5.4 "about 9 times" as 1/0.11. R2: mention VN30 covered warrants in §3.1; state the VNINDEX full-cap vs VN100 free-float weighting in §6.3; add "with known weights and a common weighting scheme" to the abstract's "the identity itself holds for any nested pair". R3: add a Table 5 note explaining the practical reading of Sensitivity; in §5.7 note that the 2.35% for cash blends is comparable to the 2% turbulent-regime misstatement.
- Acceptance criterion: each listed item is changed or its non-change is explained in the response letter.

**RR-11 — Correct the "floor" as a lower bound** (P0, must_fix)
- Sources: R1 W1 (Major, 5; the R1 D3 block trigger), DA M4 (Major, 5). Disposition: single-reviewer finding with DA corroboration. No seat disputes it.
- Anchor: text: §2.5 "Proposition 1 implies that the nested coefficient cannot fall below a floor determined by index weights and relative volatility"; text: §6.1 "this fixes a floor below which the nested coefficient cannot fall"; figure: Fig. 3, curve below the dashed floor on [−0.5, 0).
- Required change: define ρ̲ as the zero-economic-correlation benchmark (rename it if preferred, e.g., "zero-correlation benchmark"). State that it bounds ρ~AB~ from below only for ρ~AM~ ≥ 0. Give the global minimum √(1 − κ²), attained at ρ~AM~ = −κ for κ ≤ 1, and note that no positive bound exists for κ ≥ 1. Rewrite §2.5, §5.4, §5.5, §5.7, §6.1 and the Fig. 3 notes. The title term "Mechanical Floor" must be consistent with the corrected definition.
- Acceptance criterion: no sentence states an unconditional bound. The condition ρ~AM~ ≥ 0 and the global bound appear with Eq. (8). The global-bound value at the estimated κ comes from an R output.

**RR-12 — Reframe H1 around magnitude and report the like-for-like gap** (P1, should_fix)
- Sources: R1 W3 (Minor, 4), R2 Theoretical framework [SEVERITY-SOURCE: letter-fallback], DA M1 (Major, 5), DA m4 (4). Disposition: corroborated 2/4 (SC-20); SC-21 single plus DA.
- Anchor: text: §2.5 H1 "the average reliable-range DCCA coefficient of the nested pairs exceeds that of the purged pair"; text: Table 4 notes "nested pairs: mean of VN30–VNINDEX, VN30–VN100 and VN100–VNINDEX".
- Required change: state that the sign for VN30–VN100 is implied by Corollary 3 when ρ~AM~ ≥ 0. Report the gap separately by pair, with the like-for-like VN30–VN100 vs P~cap~–VN30 gap as primary (about 0.104 per DA; to be confirmed from R) and the three-pair mean as secondary. Reframe H1 around a magnitude with an a priori economic margin rather than "excludes zero".
- Acceptance criterion: Table 4 (or an appendix table) reports gaps by pair from R. The H1 text cites Corollary 3 for the sign. The decision rule uses a margin stated in §2.5.

**RR-13 — Propagate weight uncertainty and validate the proxy** (P0, must_fix; SPLIT D-1 resolved Major)
- Sources: R1 W4 (Major, 5; the D1 block trigger), R2 W4 (Major, 4), R3 W9 weight-path part (Minor, 3), DA M3 (Major, 4), DA m7 (3).
- Anchor: text: §4.2 "The weight is fixed from the factsheet before any estimation, so it is not tuned to the results"; table: Table A2 (w, mean ρ, gap only); text: §6.1 "Once the overlap is removed, the remaining dependence behaves like economic co-movement."
- Required change, from the seats' remedies in order of preference: (a) collect semi-annual HOSE factsheets or month-end constituent capitalisations, build a w~t~ path, and recompute with time-varying weights (R1, R3, DA). (b) Failing that, draw w in each bootstrap replicate from the empirical range of historical weights and report the resulting intervals (R1, DA). (c) Extend Table A2 to κ, ρ̲, the share, the sensitivity and ρ~AM~, computed with DCCA rather than the DA's Pearson sweep (R1, DA). (d) Validate P~cap~ against the published VNMIDCAP daily index or the FUEDCMID NAV: correlation, tracking error, and estimated w in B = wA + (1 − w)·VNMIDCAP (R1, R2). (e) Discuss the 10% capping and free-float rules and the VN30-index vs VN30-sleeve difference in §3.2/§4.3 (R2). (f) Call ρ~AM~ the "overlap-purged correlation" unless (d) supports "economic" (R2). (g) State that the floor/share (via κ) are less exposed than the level of ρ~AM~ (R2). (h) State the condition under which P~cap~–VN30 is a disjoint pair (exact w; Eq. 10) wherever the Forbes–Rigobon exogeneity argument uses it (DA m7).
- Acceptance criterion: headline intervals either incorporate w uncertainty or are reported alongside ranges over a documented w path/range, all from R outputs. Table A2 includes the decomposition quantities. A P~cap~-vs-VNMIDCAP validation statistic is reported, or the reason it is infeasible is documented in the ledger and the paper. The ρ~AM~ label matches the validation result.

**RR-14 — Fix p-value resolution and the H3 multiplicity family** (P0, must_fix; tension T-1)
- Sources: R1 W5 (Major, 5), DA m1 (4), DA m2 (TOST part, 4). Disposition: single-reviewer finding (R1) with DA input.
- Anchor: table: Table 6 notes "Holm and Benjamini–Hochberg (BH) adjustments are across all 19 reliable-range tests"; text: §5.5 "The unadjusted pattern is nevertheless the one H3 predicts".
- Required change: (a) raise B to at least 9,999 for the slope statistics, or use bootstrap standard errors with a normal or studentized reference, so p-values are not resolution-bounded. (b) Report the originally stated 19-test family. If a narrower confirmatory family (the eight broad-market tests H3 concerns) is reported, justify it from the H3 wording and label it a revised specification introduced at revision, not a pre-specified one. (c) Test the VN30–VN100 "no slope" half of H3 by equivalence (TOST) with a stated margin. (d) Test the broad-vs-nested slope difference within the same bootstrap. (e) Unless the re-analysis changes the verdict under the original specification, keep the unadjusted pattern as exploratory, in one sentence, without "fits the Epps effect" (DA m1).
- Acceptance criterion: the minimum attainable adjusted p is below 0.05 under the reported B or method. Both families are reported with their status labelled. The TOST and difference tests are reported from R. Table 8's H3 verdict follows the stated rule.

**RR-15 — Handle overnight and auction bars and check block length at intraday frequencies** (P0, must_fix)
- Sources: R1 W6 (Major, 4); R2 W6 midday-break remark (Minor, 3) as context. Disposition: single-reviewer finding.
- Anchor: text: §3.1 "the first and last 30-minute bars of each day are more volatile and less synchronous than midday bars"
- Required change: (a) re-estimate Table 6 and A1 excluding the first bar of each day (and the closing-auction bar), or after a time-of-day volatility adjustment (R1 cites Andersen and Bollerslev 1997; verify). (b) Repeat Table A5 at M30 and H1 for the slopes with mean blocks of 10–80 trading days, and report a data-driven block length (R1 cites Politis and White 2004 with the Patton, Politis and White 2009 correction; verify). (c) State the H4 bar definition, including the treatment of the 11:30–13:00 break.
- Acceptance criterion: an R output reports slopes with and without the first and last bars, plus an intraday block-length sensitivity table. The text states whether conclusions change.

**RR-16 — Address Forbes–Rigobon bias and identification** (P0, must_fix; tension T-2)
- Sources: R1 W7 (Major, 4), R2 W2 (Major, 4), DA alternative 3 and m6 (4), DA m7 (3). Disposition: corroborated 2/4.
- Anchor: table: Table 7; text: §6.1 "consistent with the interdependence interpretation of Forbes and Rigobon (2002) rather than with a change in transmission"; dataset: outputs/10_table4_forbes_rigobon.csv panel B (DA m6).
- Required change: (a) cite and discuss the common-shock bias (Corsetti, Pericoli and Sbracia 2005) and identification through heteroskedasticity (Rigobon 2003; DOI to confirm). (b) Add a common-factor-robust test (Corsetti–Pericoli–Sbracia factor-model test or Rigobon identification) (R1). (c) Define the quartile regimes on VN30 volatility, or on a series excluding P~cap~, and report two-sided intervals (R1). (d) Report calm and crisis tier-specific residual variances (R2). (e) Repeat Table 7 across the RR-13 w grid (R1). (f) Report the DCCA-based FR result as a robustness row, or state why only Pearson is admissible (DA m6). (g) Drop the causal "rather than a change in transmission" wording or make it conditional on constant β and constant tier-specific variance, and carry the same condition into any stress-testing reading (T-2).
- Acceptance criterion: Table 7 (or an appendix) includes at least one common-factor-robust result and a VN30-based regime definition, all from R. §5.6 and §6.1 state the identifying assumptions. The DCCA-based row is reported or excluded with a reason.

**RR-17 — Resample ρ~st~ in H5 and test the purged-vs-nested contrast** (P2, consider)
- Sources: R1 W8 (Minor, 5), EIC Minor Issues, R3 Minor Issues. Disposition: CONSENSUS-3 on SC-37 (R2 silent); SC-36 single.
- Anchor: dataset: project_R/run_revision.R RR4 block (`rs` computed outside `replicate()`); text: §5.7 "at most 2.35%".
- Required change: resample the full sample jointly and recompute ρ~st~ and ρ~r~ in each replicate. Report the |RE| difference between purged and nested portfolios with an interval, plus an appendix table of the cash-blend values.
- Acceptance criterion: the RE intervals come from the joint resampling in R, and the appendix table exists.

**RR-18 — Justify the reliability cut-off and extend the calibration** (P2, consider)
- Sources: R1 W9 (Minor, 4). Single-reviewer finding.
- Anchor: text: §5.2 "All averages below use the Gaussian thresholds"
- Required change: report Table 6/A1 over s ≤ s~rel~(GARCH-t). Add ρ~0~ = 0.95 and 0.98 to the calibration. Justify the 0.05 tolerance relative to the gap.
- Acceptance criterion: R outputs for the GARCH-t range slopes and the extended grid exist, and the text gives the tolerance rationale.

**RR-19 — Tighten bootstrap conventions** (P2, consider)
- Sources: R1 W10 (Minor, 4). Single-reviewer finding.
- Anchor: text: §4.4 "two-sided bootstrap p-values computed as 2 min{(k₋ + 1), (k₊ + 1)}/(B + 1)"
- Required change: state the cap at 1 and the percentile-inversion (uncentred) nature of the p-value versus the re-centred FR convention. Store raw counts rather than reconstructing them from proportions. Consider Fisher-z or BCa intervals for coefficients near 1. Report the H2 and gap p-values as below 1/(B + 1).
- Acceptance criterion: §4.4 states both conventions, the code stores counts, and reported p-values use the "< 1/(B+1)" form where applicable.

**RR-20 — Present DMCA and tail checks for what they are** (P2, consider)
- Sources: R1 W11 (Minor, 4). Single-reviewer finding.
- Anchor: table: Table A4; text: §5.9 "overlap also inflates joint crash probabilities"
- Required change: add bootstrap intervals to Table A3. Benchmark λ~L~(u) against the Gaussian-copula value at each pair's own correlation and report the excess. Reword §5.9 accordingly.
- Acceptance criterion: Table A3 has intervals, Table A4 reports the excess over the Gaussian-copula value, and both come from R.

**RR-21 — Correct the attribution of the zero VN30–VN100 slope** (P2, consider)
- Sources: R1 W12 (Minor, 4), R2 W3 last part (Minor, 4), DA m2 (4). Disposition: corroborated 2/4.
- Anchor: text: §5.5 "as Proposition 1 predicts: the coefficient is bounded below by its floor and almost insensitive to the economic correlation"
- Required change: derive the implied slope dρ~AB~/d ln s from Eq. (7) using the estimated κ(s) and ρ~AM~(s) paths and compare it with the observed slope. Restate the H3 prediction for the nested pair as "a slope bounded by the sensitivity in Eq. (9)" (R2). Remove "bounded below" per RR-11. Pair the non-rejection with the RR-14 TOST.
- Acceptance criterion: §5.5 reports implied versus observed slope from R, and no sentence says Proposition 1 predicts a zero slope.

**RR-22 — Declare the attribution convention behind "accounts for"** (P1, should_fix)
- Sources: R1 W14 (Minor, 4), DA M2 (Major, 5). Disposition: single-reviewer finding plus DA (severity differs; DA is outside consensus counting).
- Anchor: text: Abstract "the floor alone accounts for 0.905–0.911 of the observed VN30–VN100 coefficient"; text: §7 "it accounts for about nine-tenths of the VN30–VN100 DCCA coefficient"
- Required change: describe the share as a counterfactual ratio (the coefficient at ρ~AM~ = 0 relative to the observed one), averaged over scales as a mean of ratios, and state that it is not an additive decomposition. Lead with the order-free sensitivity (Eq. 9). Report the floor and ρ~AM~ side by side. Either drop "nine-tenths" or pair it with the reverse-order figure (overlap increment ρ~AB~ − ρ~AM~).
- Acceptance criterion: no "accounts for" or "nine-tenths" wording remains without the convention stated. The sensitivity is the lead quantity in the Abstract and §7. The reverse-order figure, if given, comes from R.

**RR-23 — Ground H3 in the size lead–lag and stale-price literature** (P2, consider)
- Sources: R2 W3 (Minor, 4). Single-reviewer finding.
- Anchor: text: §2.5 "Both mechanisms predict positive scaling slopes for pairs whose constituents are repriced at different speeds"
- Required change: add Lo and MacKinlay (1990) and Hou (2007), plus Dimson (1979) once its DOI is verified. Consider one supplementary lead–lag regression of P~cap~ returns on lagged VN30 returns. R2 defers its appropriateness, given the construction of P~cap~, to R1, so it is optional.
- Acceptance criterion: references are added and verified. If the regression is run, it comes from R.

**RR-24 — Support or drop the product recommendations; acknowledge the existing VNMIDCAP ETF** (P1, should_fix)
- Sources: R2 W5 (Minor, 5; ETF exists), R3 W5 (Major, 3; recommendations unsupported). Different sub-claims on the same §6.2 sentence, so not a SPLIT.
- Anchor: text: §6.2 "standalone non-overlapping segment benchmarks, such as an investable VNMIDCAP fund or mid-cap index futures alongside the existing VN30 futures"
- Required change: acknowledge the DCVFMVN MIDCAP ETF (FUEDCMID, listed 29 September 2022 per R2; verify) and fix the inconsistency with §5.7. Change "cannot be traded" to "cannot be shorted or hedged with futures" (R2). Either drop the mid-cap future recommendation or support it with a hedge-effectiveness calculation from existing outputs (residual variance of a mid-cap exposure hedged with VN30 futures, using the purged correlation and its regime variation) (R3). State that the benchmark exists and the gap is investable or hedging instruments.
- Acceptance criterion: §6.2 contains no recommendation without a linked reported result. The ETF is acknowledged with a verified source. Any hedge-effectiveness figure traces to R.

**RR-25 — Correct the institutional facts** (P2, consider)
- Sources: R2 W6 (Minor, 3). Single-reviewer finding.
- Anchor: text: §3.1 "Decree 155/2020/ND-CP and Circular 120/2020/TT-BTC prohibit cash short selling"
- Required change: restate the short-sale position as "provided for in law (covered short sale via VSDC lending) but not yet implemented; naked short selling not permitted". Cite the amending Decree 245/2025/ND-CP. Give the T+3 to T+2 switch date (1 January 2016). Describe the morning and afternoon sessions with the 11:30–13:00 break. R2 checked these through secondary legal databases, so verify each against the official texts.
- Acceptance criterion: §3.1 is corrected, with each legal claim citing a primary source.

**RR-26 — Add foreign-ownership limits, reclassification and the comparative statics of the floor** (P2, consider)
- Sources: R2 W7 (Minor, 4), R3 W10 (Minor, 3). Disposition: corroborated 2/4.
- Anchor: absence: §3.1 Institutional background (no discussion of foreign-ownership limits); absence: §3.1 and §6.2 (no discussion of how index rules shift w and the floor).
- Required change: add a paragraph on FOL (49% general, 30% banks) and, once verified against FTSE Russell's primary release, the reclassification announcement. In §6.1, list FOL-driven foreign flows, ±7% limit-hit synchronisation and herding as rival mechanisms. In §6.2, give the comparative statics of the floor in w and relative volatility (sign of ∂ρ̲/∂κ), with no new estimation.
- Acceptance criterion: the paragraphs are present, the reclassification statement has a verified primary citation or is omitted, and the comparative-statics statement matches Eq. (8).

**RR-27 — Complete the index-membership literature** (P2, consider)
- Sources: R2 W8 (Minor, 4). Single-reviewer finding.
- Anchor: absence: §2.2 and reference list (Greenwood 2008; Chen, Singal and Whitelaw 2016).
- Required change: add both, verified, and use Chen et al. (2016) to reinforce the motivation that index-level co-movement is easy to misread.
- Acceptance criterion: both appear in §2.2 with DOIs verified.

**RR-28 — Use the Vietnamese studies analytically** (P2, consider)
- Sources: R2 W9 (Minor, 3). Single-reviewer finding.
- Anchor: text: §2.2 "Vietnamese evidence suggests that both mechanisms could matter on the HOSE."
- Required change: link each study to the hypothesis it informs (e.g., Tran and Tran 2025 to H3; Nguyen et al. 2023 and Bui et al. 2022 to H4) and return to them in §5.5 and §6.1.
- Acceptance criterion: each cited Vietnamese study appears at least once in the Results or Discussion tied to a hypothesis.

**RR-29 — Benchmark H5 materiality and test out of sample** (P1, should_fix)
- Sources: R3 W3 (Major, 4; the D4 warn trigger), EIC Detailed Comments, Significance ("modest relative to ordinary covariance estimation error, and the regimes are ex post") [SEVERITY-SOURCE: letter-fallback], DA alternative 4 and m3 (4). Disposition: corroborated 2/4.
- Anchor: text: §5.7 "a static correlation overstates the variance of an equally weighted VN30 and P~cap~ position by 2.23%"; text: §1 "prices the cost of static correlations".
- Required change: (a) report the misstatement next to a materiality benchmark (sampling error of the regime variance, or a one-year rolling estimate). R3's back-of-envelope standard errors (about 11% and 8%) are R3's own estimate, not manuscript results; recompute them in R. (b) Add an out-of-sample check: estimate on 2014–2022, evaluate on 2023–2025, comparing static, EWMA (λ = 0.94) and regime-conditioned correlations with a bias statistic or QLIKE (R3; verify the RiskMetrics and Patton 2011 leads). (c) State that the calm-overstate / turbulent-understate sign pattern is expected by construction for a pooled correlation (DA). (d) Rephrase H5 in the Abstract, §1 and §7 as an in-sample magnitude, and drop "prices the cost" unless (b) supports it.
- Acceptance criterion: an R output reports the materiality benchmark and the out-of-sample comparison. The Abstract, §1 and §7 carry the in-sample qualifier, and the sign-pattern sentence is present. Whatever the out-of-sample result, it is reported as found.

**RR-30 — Add a practitioner recipe and fix the "recover" sentence** (P2, consider)
- Sources: R3 W7 (Minor, 4), R3 Minor Issues, DA m5 (4). Single-reviewer finding plus DA.
- Anchor: text: §4.2 "so they can be computed for any nested pair whose child weight and fluctuation functions are known"; text: §6.2 "Eq. (7) shows how to recover the economic correlation"
- Required change: add a boxed three-step recipe (w from the factsheet → volatility ratio → floor and sensitivity) with the VN30–VN100 daily worked example. Reword §6.2 so the floor is the no-estimation diagnostic and the purged series gives ρ~AM~ directly. Replace "carry little information" with the ill-conditioning statement (a small change in the index-level number maps to about a ninefold change in ρ~AM~) (DA m5).
- Acceptance criterion: the box exists with numbers matching R outputs, and the §6.2 sentence is reworded.

### Source-traceability checklist (source order, not a work order)

- [ ] RR-1 must_fix · [ ] RR-2 must_fix · [ ] RR-3 must_fix · [ ] RR-4 must_fix · [ ] RR-5 should_fix · [ ] RR-6 should_fix · [ ] RR-7 consider · [ ] RR-8 consider · [ ] RR-9 consider · [ ] RR-10 consider
- [ ] RR-11 must_fix · [ ] RR-12 should_fix · [ ] RR-13 must_fix · [ ] RR-14 must_fix · [ ] RR-15 must_fix · [ ] RR-16 must_fix · [ ] RR-17 consider · [ ] RR-18 consider · [ ] RR-19 consider · [ ] RR-20 consider
- [ ] RR-21 consider · [ ] RR-22 should_fix · [ ] RR-23 consider · [ ] RR-24 should_fix · [ ] RR-25 consider · [ ] RR-26 consider · [ ] RR-27 consider · [ ] RR-28 consider · [ ] RR-29 should_fix · [ ] RR-30 consider

### Response letter

The authors should respond to every RR item point by point using `templates/revision_response_template.md`, quoting the RR ID, the change made with its location, and the R output file for every changed number. A declined item stays visible as declined, with reasons. It is not silently dropped.

### Reviewer questions to answer in the response

EIC Q1–Q4, R1 Q1–Q4, R2 Q1–Q5 and R3 Q1–Q4 are carried as they stand in the seat cards. Each maps to an RR item: EIC Q1 → RR-4; EIC Q2 → RR-2; EIC Q3 → RR-1; EIC Q4 → RR-6; R1 Q1 → RR-13; R1 Q2 → RR-14; R1 Q3 → RR-15; R1 Q4 → RR-15; R2 Q1 → RR-13; R2 Q2 → RR-13; R2 Q3 → RR-16; R2 Q4 → RR-1; R2 Q5 → RR-23; R3 Q1 → RR-4; R3 Q2 → RR-29; R3 Q3 → RR-24; R3 Q4 → RR-6/RR-7.

---

## Part 3: Sub-Claim Inventory (Step 1b, compressed)

Positions: R = raised, C = corroborated, — = not mentioned, Dsp = disputed. Severity is transported from the parent finding.

| SC | Parent | EIC | R1 | R2 | R3 | DA | Severity | Disposition | RR |
|---|---|---|---|---|---|---|---|---|---|
| SC-1 | Part–whole identity, novelty | R (W1) | — | R (W1) | R (W6) | M5 | Major | CONSENSUS-3 | RR-1 |
| SC-2 | Search window too narrow | — | — | R (W1) | — | — | Major | single | RR-1 |
| SC-3 | Finance overlap precedents | R (W1) | — | R (W1) | R (W6) | — | Major | CONSENSUS-3 | RR-1 |
| SC-4 | DCCA adds nothing over Pearson | R (W2) | — | — | R (W1) | counter-arg | Major | corroborated | RR-2 |
| SC-5 | Scale invariance as a finding | R (W2b) | — | — | R (W1) | — | Major | corroborated | RR-2 |
| SC-6 | H2 by construction | R (W3) | R (W2) | C (fallback) | — | M1 | Major | CONSENSUS-3 | RR-3 |
| SC-7 | Premise undocumented | R (W4) | — | — | R (W2) | M6 | Major | corroborated | RR-4 |
| SC-8 | Holdings models unaffected | R (W4) | — | — | R (W2) | — | Major | corroborated | RR-4 |
| SC-9 | Peripheral analyses | R (W5) | — | — | C (W8) | — | Minor | corroborated | RR-5 |
| SC-10 | Over-generalisation / transferability | R (W6, Minor) | — | — | Dsp-severity (W4, Major) | — | Minor/Major | SPLIT D-2 | RR-6 |
| SC-11 | Partial-overlap boundary | — | — | — | R (W4) | — | Major | single | RR-6 |
| SC-53 | Extend to broad-market pairs | R (Q4) | — | Dsp (Minor Issues) | R (W4) | — | Minor | SPLIT D-3 | RR-6 |
| SC-12 | Fig. 3 range | R (W7) | — | — | R (W8) | — | Minor | corroborated | RR-7 |
| SC-13 | Fig. 4 f(α) < 0, labels | R (W7) | — | — | — | — | Minor | single | RR-7 |
| SC-14 | Fig. 1 spikes, legend | R (W9) | — | — | R (W8) | — | Minor | corroborated | RR-7 |
| SC-15 | Fig. 2 labels | — | — | — | R (W8) | — | Minor | single | RR-7 |
| SC-16 | Abstract density | R (W8) | — | — | — | — | Minor | single | RR-8 |
| SC-17 | Data not public | R (W10) | R (W13) | — | R (W9) | — | Minor | CONSENSUS-3 | RR-9 |
| SC-18 | Editorial minors | R | — | R | R | — | Minor | single (each) | RR-10 |
| SC-19 | Floor not a bound | — | R (W1) | — | — | M4 | Major | single + DA | RR-11 |
| SC-20 | H1 sign implied by Cor. 3 | — | R (W3) | C (fallback) | — | M1 | Minor | corroborated | RR-12 |
| SC-21 | H1 pools uncovered pairs | — | R (W3) | — | — | m4 | Minor | single + DA | RR-12 |
| SC-22 | Intervals conditional on fixed w | — | R (W4, Major) | C (W4, Major) | Dsp-severity (W9, Minor) | M3 | Major | SPLIT D-1 → Major | RR-13 |
| SC-23 | Validate P~cap~ vs VNMIDCAP | — | R (W4d) | R (W4i) | — | — | Major | corroborated | RR-13 |
| SC-24 | Capping rules; relabel ρ~AM~ | — | — | R (W4) | — | — | Major | single | RR-13 |
| SC-25 | Extend Table A2 | — | R (W4c) | — | — | M3 | Major | single + DA | RR-13 |
| SC-26 | B = 499 resolution | — | R (W5) | — | — | — | Major | single | RR-14 |
| SC-27 | Family wider than H3 | — | R (W5) | — | — | m1 (tension) | Major | single; T-1 | RR-14 |
| SC-28 | TOST for the nested null | — | R (W5c) | — | — | m2 | Major | single + DA | RR-14 |
| SC-29 | Overnight/auction bars | — | R (W6) | — | — | — | Major | single | RR-15 |
| SC-30 | Intraday block length | — | R (W6) | — | — | — | Major | single | RR-15 |
| SC-31 | Midday break omitted | — | — | R (W6) | — | — | Minor | single | RR-25 (ref. RR-15) |
| SC-32 | FR bias toward null | — | R (W7) | R (W2) | — (S3 tension) | alt. 3 | Major | corroborated; T-2 | RR-16 |
| SC-33 | Regimes sorted on VNINDEX | — | R (W7) | C (W2) | — | — | Major | corroborated | RR-16 |
| SC-34 | DCCA-based FR sign differs | — | — | — | — | m6 | (DA minor) | DA-only | RR-16 |
| SC-35 | Causal "interdependence" wording | — | — | R (W2) | — | — | Major | single | RR-16 |
| SC-36 | ρ~st~ not resampled | — | R (W8) | — | — | — | Minor | single | RR-17 |
| SC-37 | 2.35% untested | R (Minor) | R (W8) | — | R (Minor) | — | Minor | CONSENSUS-3 | RR-17 |
| SC-38 | Reliability cut-off | — | R (W9) | — | — | — | Minor | single | RR-18 |
| SC-39 | Bootstrap conventions | — | R (W10) | — | — | — | Minor | single | RR-19 |
| SC-40 | DMCA/tail not independent | — | R (W11) | — | — | — | Minor | single | RR-20 |
| SC-41 | Zero slope attribution | — | R (W12) | R (W3) | — | m2 | Minor | corroborated | RR-21 |
| SC-42 | "Accounts for" / ordering | — | R (W14) | — | — | M2 | Minor | single + DA | RR-22 |
| SC-43 | H3 lead–lag grounding | — | — | R (W3) | — | — | Minor | single | RR-23 |
| SC-44 | VNMIDCAP ETF exists | — | — | R (W5) | — | — | Minor | single | RR-24 |
| SC-45 | Policy recs unsupported | — | — | — | R (W5) | — | Major | single | RR-24 |
| SC-46 | Short sale, decree, T+2 | — | — | R (W6) | — | — | Minor | single | RR-25 |
| SC-47 | FOL, reclassification, statics | — | — | R (W7) | R (W10) | — | Minor | corroborated | RR-26 |
| SC-48 | Membership literature | — | — | R (W8) | — | — | Minor | single | RR-27 |
| SC-49 | Vietnamese studies | — | — | R (W9) | — | — | Minor | single | RR-28 |
| SC-50 | H5 materiality / OOS | C (fallback) | — | — | R (W3) | alt. 4 | Major | corroborated | RR-29 |
| SC-51 | H5 sign switch mechanical | — | — | — | — | m3 | (DA minor) | DA-only | RR-29 |
| SC-52 | Practitioner recipe | — | — | — | R (W7) | m5 | Minor | single + DA | RR-30 |

No sub-claim was introduced that some seat did not raise. The surface-form parity check was applied to arbitration: no sub-claim was down-weighted for informal wording or up-weighted for technical precision. The dispositions above rest on paper anchors.

## Part 4: Reviewer Report Summary (Appendix)

- **Journal-Fit Reviewer (EIC)**: Major Revision, confidence 4. D5 warn, D6 block (repairable). Key point: the originality source is mislocated. The paper should claim the purged correlation with inference, the near-uninformativeness of the nested number and the portable diagnostic, not the algebra.
- **R1 Methodology**: Major Revision, confidence 4. D1 block, D3 block (both repairable). Key point: the identity is correct, but the floor is not a bound, H2 cannot fail, all intervals condition on one w, and the H3 null, intraday design and FR test each need re-analysis. Arithmetic receipts AR1–AR4 are consistent.
- **R2 Domain**: Major Revision, confidence 4. D2 block (repairable). Key point: the classical part–whole result and finance overlap measures pre-empt the "derives exactly" claim; the FR and "economic correlation" readings overreach; institutional facts need correction (existing VNMIDCAP ETF, short-sale law, FOL).
- **R3 Perspective**: Major Revision, confidence 4. D4 warn. Key point: the decision value is less than the framing suggests (premise, Pearson sufficiency, H5 materiality, unsupported policy, untested transferability), and all of it is fixable without new data sources.
- **Devil's Advocate**: findings only. D3 block (repairable). No CRITICAL challenge; six MAJOR (M1–M6) and seven minor (m1–m7), all carried into the roadmap.

## Quality Gates

- [x] All five Phase 2 cards and their Phase 1 contract/scoring plans were read. Layer-1 parse: PASS.
- [x] Consensus and disagreements are identified and labelled. Every SPLIT (D-1, D-2, D-3) and tension (T-1, T-2) has a resolution and rationale.
- [x] The decision follows mechanically from the contract (F2) and matches all four non-DA seat signals.
- [x] Every RR item traces to named seat findings. No synthesizer-originated issue was added.
- [x] Severity and confidence are transported. Fallbacks are marked.
- [x] DA CRITICAL: none exists. The adjudication line is `[]` and no phantom ID is used.
- [x] Provenance is disclosed without an independence claim. The provenance artifact is missing and flagged.

## Checker Result

`python3 -I vendor/academic-research-skills/scripts/check_panel_synthesis.py --contract vendor/academic-research-skills/shared/contracts/reviewer/full.json --report eic.phase2.md --report methodology.phase2.md --report domain.phase2.md --report perspective.phase2.md --report da.phase2.md --roles eic,methodology,domain,perspective,da --synthesis 06_editorial_synthesis.md`

Result (run 2026-10-10): `PANEL-SYNTHESIS: PASS`, exit 0. The checker independently recomputed the dimension verdicts, fired conditions, decision and DA-CRITICAL gate from the five cards, and they match the audit lines in Part 0. Layer-1 (`--layer1-only`) on the five cards: `LAYER1-ONLY: PASS`.
