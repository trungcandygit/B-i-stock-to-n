contract_role: eic
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: warn
trigger: "peripheral analyses crowd the main line"

### D6: venue_fit_and_contribution
score: block
trigger: "The core contribution is substantially a known or trivially derivable result presented as new"
block_class: repairable

## Review Body

**Manuscript**: The Mechanical Floor of Nested Index Correlations: An Exact Multiscale Decomposition with Evidence from Vietnam (anonymized round-2 version). **Review round**: 2. **Review date**: 2026-10-08.

**Reviewer role**: Journal-Fit Reviewer (EIC seat). **Identity**: senior editor at the field-general level for Q1/Q2 outlets where empirical finance meets econophysics (Configuration Card #1). No venue is bound (`criteria_binding_unavailable`), so this card makes no claim of alignment with any specific journal's criteria, scope statement or word limit. It judges fit against the venue class only.

**Review focus**: whether the paper's central result gives finance and econophysics readers an insight they lack; whether the framing, contribution statements and evidence are consistent; and whether the scope and length suit a full-length article in this class.

**Overall recommendation (seat signal for the synthesizer, non-binding)**: Major Revision. **Confidence**: 4 (high; journal-fit and contribution assessment are within my remit; I defer to R1 on the proof mechanics and inference). **Calibration status**: `NOT_CALIBRATED`.

### Summary Assessment

The manuscript argues that the correlation between a child index and a parent index that contains it (VN30 within VN100) is mostly fixed by construction. It writes the parent as a weighted sum of the child and a mid-cap remainder and derives a closed-form identity for the DCCA coefficient (Proposition 1), with a "mechanical floor" and a sensitivity term. It then quantifies these quantities for the HOSE with bootstrap inference and adds four further hypotheses: horizon slopes, Forbes–Rigobon contagion, portfolio-variance misstatement, and a descriptive MF-DCCA section. Compared with what was criticized earlier as a "statistical report", this version has a real organizing idea, pre-stated hypotheses, honest null reporting and good reproducibility. It is much closer to a journal article.

The contribution problem is now one of positioning and substance, not presentation. Proposition 1 is the classical part–whole (component–sum) correlation formula. It is written in DCCA notation and holds for any bilinear covariance, as the paper itself notes. The manuscript claims no one has derived it. The headline floor (about 0.90) can be computed from the factsheet weight and two standard deviations. The multiscale layer changes nothing in these data, since the Pearson and DCCA floors agree to three decimals. The headline hypothesis H2 is close to guaranteed once the weight is known. What remains is a useful diagnostic and a clean, well-documented case study. That can be publishable in this class, but only if the paper is reframed around what the identity reveals empirically rather than around the identity itself. This is repairable in one major revision, so the D6 block is classed repairable, not fatal.

### Criterion-Bound Judgements

| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| D6 originality of core result | Contract D6; Card #1 focus 1 | DOES_NOT_MEET | §2.4 gap claim; §4.2 Proposition 1 | The algebra is a known part–whole correlation result; the novelty claim is stated without engaging that prior art | I did not run a systematic prior-art search; I rely on the identity being a textbook component–sum result | yes, the main reason for the block |
| D6 significance for the readership | Contract D6; Card #1 focus 1–2 | PARTLY_MEETS | Abstract opening; §5.4 Pearson floor | The diagnostic is useful, but the premise that practitioners misuse nested correlations is not evidenced, and the DCCA layer adds nothing in these data | Practitioner usage is an empirical question R3 is better placed to judge | yes |
| D6 consistency of contributions with supported hypotheses | Contract D6; Card #1 focus 2 | PARTLY_MEETS | Table 8; §1 third contribution | Contribution 3 rests on a null (H4) with power 0.41 under one definition; the claims are mostly worded honestly | none identified | no, wording-level |
| D6 scope and length for a full article | Contract D6; Card #1 focus 3 | PARTLY_MEETS | §5.8; §4.2 statistical proxies; Appendix A | About 8,800 words with five hypotheses for one decomposed pair in one market; several sections are peripheral | No venue word limit is bound | no |
| D5 organisation and exposition | Contract D5 | MEETS | §1 roadmap; Table 8 | Clear IMRaD flow, hypotheses with decision rules, summary table | none identified | no |
| D5 exhibit quality | Contract D5 | PARTLY_MEETS | Fig. 3; Fig. 4 | Tables are clean; two figures have readability or interpretation problems | Judged from PNG renders | no |
| D5 abstract and conclusion alignment | Contract D5 | MEETS | Abstract; §7 | The numbers in the abstract and conclusion match Tables 4, 5 and 7 and §5.7; the nulls are reported | none identified | no |

### Strengths

### S1: Honest reporting of null and weak results
H3 is reported as not supported after Holm and BH adjustment, H4 as not supported with its power, and the unadjusted H3 pattern is labelled "the evidence is weak". This candour is uncommon in DCCA submissions and builds editorial trust.
**Evidence Anchor**: table: Table 8 — H3 "Not supported after adjustment", H4 "Not supported"

### S2: The identity is openly labelled as an accounting identity
The authors pre-empt the obvious objection rather than hiding it. This is the right basis on which to build the reframing requested below.
**Evidence Anchor**: text: §4.2 "Eq. (7) is an accounting identity rather than an estimated relation; its content lies in the decomposition it delivers."

### S3: Ready-to-use closed-form diagnostic
The floor and the sensitivity depend only on the child weight and the relative amplitude. That gives practitioners and index providers a one-line check usable in any nested system. This is the paper's most portable deliverable.
**Evidence Anchor**: equation: Eq. (8) — floor 1/sqrt(1+κ²) and Eq. (9) sensitivity

### S4: Reproducibility and transparent inference
A single R script with fixed seeds regenerates every exhibit. Block-length sensitivity (Table A5), multiplicity control and pre-fixed reliability tolerances are documented. This meets or exceeds the norm in the venue class.
**Evidence Anchor**: text: §4.9 "reproduces every table and figure; rerunning it yields byte-identical CSV output files"

### S5: Careful institutional setting
Price bands, T+2, the call auctions, the short-sale ban and the absence of mid-cap futures are tied directly to the interpretation, for example the infeasibility of the 315%/−215% shadow benchmark. This gives regional readers a concrete reason to care.
**Evidence Anchor**: text: §3.1 "VN30 index futures trade on the Hanoi Stock Exchange, but no mid-cap index future exists."

### Weaknesses

### W1: Proposition 1 is a known part–whole correlation result, and the novelty claim does not engage the prior art
**Problem**: Eq. (7) is the standard formula for the correlation between a component X and a weighted sum wX + (1 − w)Y. It is long established in statistics (part–whole or component–total correlation, the basis of the "corrected item–total correlation" in psychometrics, and the spurious-correlation tradition going back to Pearson). Finance practice handles the same problem with "ex-country" or "ex-constituent" benchmarks. The DCCA version follows immediately because, as §4.2 itself says, the derivation uses only linearity and bilinearity. Yet §2.4 claims that no study derives the component exactly, and Table 1 compares only against DCCA and contagion papers. A finance or econophysics editor would read this as a textbook identity presented as a theorem.
**Evidence Anchor**: text: §2.4 "First, no study we found separates the mechanical component of correlations between overlapping indices from economic co-movement, and none derives that component exactly."
**Why it matters**: Contribution 1 in §1 is the paper's lead claim. If referees recognise the formula, the paper is desk-rejectable on originality grounds regardless of the empirical quality.
**Suggestion**: Cite the classical part–whole correlation result and the ex-constituent benchmark practice. Relabel Proposition 1 as a lemma or "result" that adapts a known identity to detrended, scale-wise coefficients. Move the claimed novelty to what is new: the scale-wise extension, inference on the floor and sensitivity for a real nested system, and the diagnostic use. Rewrite the first gap in §2.4 and the "Overlap treated?" column of Table 1 accordingly. R2 should verify the specific citations.
**Severity**: Major
**Confidence**: 4 — the identity is standard algebra I can verify; I have not done a systematic bibliographic search, so specific precedents are left to R2.

### W2: The headline is recoverable without DCCA, and the "multiscale" promise in the title is not delivered
**Problem**: With w = 0.6826 and the daily standard deviations in Table 2 (0.0124 vs 0.0121), κ ≈ 0.465 × 1.025 ≈ 0.477, which gives a floor of about 0.903. That is the paper's own Pearson floor, and it is within 0.003 of every DCCA floor in Table 5. κ is 0.48–0.50 at all frequencies, and Fig. 2 shows flat curves. So in these data the scale dimension adds no information to the decomposition, while the title, abstract and contribution 1 present an "exact multiscale decomposition" as the core.
**Evidence Anchor**: text: §5.4 "The same identity applied to full-sample Pearson correlations of daily returns gives a floor of 0.903 and a mechanical share of 0.914"
**Why it matters**: For econophysics readers the scale-wise result is the hook, and it turns out empty here. For finance readers the DCCA machinery looks like overhead on a one-line calculation. Either way the significance argument weakens.
**Suggestion**: Either (a) show where κ(s) or ρ~AM~(s) genuinely varies with scale, for example in crisis sub-samples, at intraday scales below the reliable range, or in another nested pair, so the multiscale element earns its place; or (b) reframe the title and contributions around the nested-correlation diagnostic and present scale-invariance as a finding, stating plainly that the Pearson floor is a sufficient practitioner shortcut. Option (b) is cheaper and more honest.
**Severity**: Major
**Confidence**: 4 — arithmetic recomputed from Table 2 and §4.2; whether scale variation appears elsewhere is untested.

### W3: The headline hypothesis H2 is close to guaranteed by construction
**Problem**: The mechanical share is floor/ρ~AB~ and ρ~AB~ ≤ 1, so the share is at least the floor. The floor exceeds 0.5 whenever κ < √3, that is, unless the remainder's detrended amplitude is more than about 3.7 times the child's at w = 0.68. H2 is therefore settled by the factsheet weight and a rough volatility ratio before any test is run. Reporting it as a "supported" hypothesis with bootstrap intervals adds the look of a test without its substance. This is part of the residual "statistical report" impression.
**Evidence Anchor**: text: §2.5 "*H2 (mechanical dominance).* The mechanical floor accounts for more than half of the VN30–VN100 DCCA coefficient."
**Why it matters**: Card #1 asked whether the headline is informative or a direct arithmetic consequence of the weight. For H2 as stated, it is the latter. Referees will notice.
**Suggestion**: Replace H2 with an informative question the identity actually answers. One option is how much of the cross-regime or cross-scale *variation* in ρ~AB~ is mechanical versus economic. Another is whether index-level correlations can distinguish economically different ρ~AM~ values given the estimated sensitivity (an identification or "information content" test). Alternatively, present the floor as a computed diagnostic, not a hypothesis. R1 and the DA may also assess the test itself.
**Severity**: Major
**Confidence**: 4 — follows directly from Eqs. (7)–(8).

### W4: The economic premise that motivates the paper is asserted, not shown
**Problem**: The abstract and §1 open by stating that nested indices are "often treated as separate diversification instruments" and that risk models summarise their dependence with one Pearson correlation. The only support given is Markowitz (1952). No evidence is offered that investors, risk-model vendors, allocation rules or the cited DCCA portfolio studies actually use nested index pairs this way. Production risk models typically work from holdings, where overlap is handled automatically.
**Evidence Anchor**: text: Abstract "Large-cap and broad-market indices are often treated as separate diversification instruments even when one index is a subset of the other."
**Why it matters**: Without a documented misuse, the finance reader's question is "who makes this mistake?" Significance then rests on a straw man, which is the desk-reject pattern this venue class sees most often in DCCA submissions.
**Suggestion**: Document the practice concretely. Possible sources are published studies or fund documents that correlate nested benchmarks (VN30 vs VNINDEX ETFs, size-tier allocation guidance), DCCA or contagion papers that pair overlapping indices, or index-provider materials. Alternatively, narrow the claim to the cases where it is demonstrably made. If no such practice can be shown, reframe the motivation around measuring segment co-movement when no segment index is available, which is a real data problem the proxy solves.
**Severity**: Major
**Confidence**: 3 — I know the general industry practice, but R3 is better placed to judge it.

### W5: Peripheral analyses still crowd the main line
**Problem**: Only H1–H2 use Proposition 1. H4 and H5 use daily Pearson correlations of the proxy, H3 is a scaling-slope exercise that ends in a null, §5.8 is explicitly descriptive with no hypothesis test, and the three statistical proxies (P~heur~, P~ratio~, P~res~) are constructions the paper itself shows to be unstable. Together these push the paper to about 8,800 words for one decomposed pair. This is the remaining trace of the earlier "statistical report" criticism: a battery of analyses around one idea.
**Evidence Anchor**: text: §4.8 "we therefore treat the multifractal results as descriptive and base no hypothesis test on them."
**Why it matters**: Dilutes the contribution and makes the paper longer than its core warrants. A short-format outlet in the class would require the paper to be cut to about a third.
**Suggestion**: Move §5.8 and the statistical-proxy comparison (§4.2 last paragraph, Table 6 rows 5–7) to the Online Resource. Shorten H3 to a robustness paragraph. Keep H4 and H5 only if they are tied explicitly to the decomposition, for example by showing that nested-pair regime changes are mechanically muted while the purged pair is not, as §5.7 hints.
**Severity**: Minor
**Confidence**: 4 — structural judgement within remit.

### W6: The conclusion generalises beyond a one-market, one-pair evidence base
**Problem**: §6.3 correctly limits the magnitudes to the HOSE, but §7 recommends that risk models and benchmark design "in nested index systems" rely on the decomposition, on the strength of one decomposed pair. The identity is general, but the empirical claim that index-level correlations carry little information depends on κ, which varies across markets.
**Evidence Anchor**: text: §7 "Risk models and benchmark design in nested index systems should therefore rely on non-overlapping segment returns or on the decomposition derived here."
**Why it matters**: International readers in the venue class will ask whether the floor is large elsewhere. Answering would turn a case study into a general finding at low cost.
**Suggestion**: Add a short cross-market table of floors computed from published weights and volatilities (e.g., SET50/SET100, IDX30/LQ45, S&P 500/Russell 1000, VN100/VNINDEX if a weight can be obtained). This uses the paper's own Eq. (8) and needs only public factsheets. Otherwise, soften §7 to the HOSE.
**Severity**: Minor
**Confidence**: 4 — scope judgement within remit.

### W7: Figure readability and interpretation issues
**Problem**: In Fig. 4(a) the P~cap~–VN30 singularity spectrum takes negative f(α) values (down to about −0.2). The caption does not comment, though such values are usually read as a numerical artefact of the absolute-covariance construction. Both panels also share one y-axis label ("f(α) (panel a) or h~xy~(q) (panel b)"). In Fig. 3 the y-axis runs from −0.5 to 1, while all the information lies between 0.85 and 1, so the observed markers overlap in one corner.
**Evidence Anchor**: figure: Fig. 4 panel (a) — P~cap~–VN30 spectrum below zero at α > 1.25
**Why it matters**: Minor readability; negative f(α) invites a referee query about the MF-DCCA implementation.
**Suggestion**: Give each panel its own axis label, note or trim the negative-f(α) region (or move Fig. 4 to the Online Resource per W5), and zoom Fig. 3's y-range or add an inset around the observed points.
**Severity**: Minor
**Confidence**: 3 — judged from the PNG renders.

### W8: The abstract is number-dense and buries the message
**Problem**: The roughly 235-word abstract carries about a dozen numeric ranges and intervals, and the one-sentence takeaway that index-level correlation between nested indices says little about tier co-movement is spread across them.
**Evidence Anchor**: text: Abstract "(block-bootstrap 95% intervals within 0.895–0.920)"
**Why it matters**: Editors triage on the abstract; density lowers the chance of being sent out.
**Suggestion**: Keep three numbers at most (the floor share, the sensitivity, the purge gap), state the takeaway in plain words, and move the intervals to the body.
**Severity**: Minor
**Confidence**: 4 — presentation judgement.

### W9: Regime shading in Fig. 1 leaves visible volatility spikes unexplained
**Problem**: Fig. 1 shows spikes of about 48% annualised volatility in early 2021 and April 2025 that belong to neither the crisis episodes nor the calm benchmark. The calm benchmark (2023–2024) contains spikes near 29%. §3.2 explains the April 2025 exclusion but not 2021.
**Evidence Anchor**: figure: Fig. 1 — unshaded spike near 2021Q1 at about 48%
**Why it matters**: Readers will ask whether the regime definitions were chosen to fit. It is a small credibility point for H4 and H5.
**Suggestion**: State explicitly why early 2021 is excluded (drawdown criterion) and confirm in a footnote that excluding it does not change Table 7. I defer the regime methodology itself to R1.
**Severity**: Minor
**Confidence**: 3 — visual reading of the figure.

### W10: Data cannot be shared, which limits replication
**Problem**: The code is provided, but the data are vendor-licensed and available only on request. Many outlets in the class now expect replication packages.
**Evidence Anchor**: text: Data availability "the merged dataset is available from the corresponding author upon reasonable request."
**Why it matters**: May conflict with replication policies in the venue class and weakens the reproducibility strength (S4) for outside readers.
**Suggestion**: State whether the official HOSE daily index levels can be obtained from a public or exchange source, and provide a script that runs end-to-end on such a source. Alternatively, deposit derived statistics that the licence allows to be shared (e.g., fluctuation functions) sufficient to rebuild every table.
**Severity**: Minor
**Confidence**: 3 — data-policy expectations vary across outlets.

### Detailed Comments

#### Journal Fit
At the venue-class level (no specific journal bound), the topic sits inside empirical finance and econophysics scope. The fit question is which readership the paper is written for. The DCCA, MF-DCCA and reliability apparatus and much of the reference base point to the econophysics class, but W2 removes the multiscale hook for those readers. The diversification, risk-model, contagion and index-design framing points to the finance class, but W4 leaves the economic premise unproven. A regional finance outlet would value §3.1 and the policy implications in §6.2. A short-format finance outlet could carry the core result well once W5's peripheral material is cut. As written, the paper tries to address all three readerships and fully satisfies none.

#### Originality
Versus the earlier "statistical report" criticism: real progress. There is now one organizing result, hypotheses derived from it, a summary table and a coherent mechanism section (§6.1). But the originality source is mislocated. It is not the algebra (W1), not the scale dimension in these data (W2), and not H2 (W3). It is (i) the purged mid-cap correlation of about 0.89 with inference, (ii) the observation that the floor and the economic correlation are of the same size, so the nested number is almost entirely uninformative, and (iii) a portable diagnostic. These are modest but genuine, and the paper should claim them, and only them.

**Is Proposition 1 a genuine contribution?** As mathematics, no. It is the component–sum correlation identity applied to a bilinear detrended covariance, and the paper's own remark that it holds for Pearson correlation and any bilinear covariance concedes this. As an organizing device that makes the mechanical share explicit, scale by scale, with a sensitivity formula and a floor-based diagnostic, it is useful. It should be presented as an adapted known identity with clear prior-art attribution, not as the paper's theoretical contribution.

#### Significance
If reframed, the result matters for anyone using segment-level co-movement when only nested indices are published, which is common in emerging and frontier markets. The cross-market table suggested in W6 would raise significance from local to regional or international at low cost. The H5 variance-misstatement figures (−2.1% to +9.4%) are modest relative to ordinary covariance estimation error, and the regimes are ex post. I defer to R3 on whether they change any practical decision.

#### Structural Coherence
Title to abstract to introduction to conclusion is internally consistent and numerically aligned with the tables. The weak link is the gap from claim to delivery: "exact multiscale decomposition" is promised, and a scale-invariant, Pearson-equivalent result is delivered. The contribution 3 wording ("separates volatility from structural change") is acceptable given the reported power, but it should note the 0.41 power under the quartile definition.

#### Title & Abstract
The title is precise but overstates the multiscale element (W2). Consider a title built around the information content of nested index correlations. For the abstract, see W8.

#### Conclusion
It addresses the research question and reports the nulls, but over-generalises the scope (W6).

### Failure-condition exposure (advisory; the synthesizer alone evaluates panel conditions)
From this seat: one mandatory dimension (D6) is scored block, classed repairable, and one normal-priority dimension (D5) is scored warn. No fatal block is asserted. The seat signal is Major Revision. Whether the panel-level conditions are met depends on the other seats' scores, which I have not seen.

### Questions for Authors
1. Which specific investors, risk models or published studies correlate nested index pairs as if they were separate diversification sources (W4)?
2. Is there any frequency, sub-period or nested pair in which κ(s) or ρ~AM~(s) varies materially with scale? If not, what does the DCCA layer add beyond the Pearson floor (W2)?
3. How does Proposition 1 differ, beyond notation, from the standard component–sum correlation formula (W1)?
4. Can a VN100-in-VNINDEX weight be obtained (even approximately) so that the decomposition covers the broad-market pairs too?

### Minor Issues
- §5.7 cites a maximum misstatement of 2.35% for cash portfolios of parent and child indices with no table; add the values to an appendix table.
- §4.2 "P~heur,~" and §4.6 "σ²~ε,~", "ρ~low,~" have stray commas inside the subscripts.
- The sensitivity statement in §5.4 ("about 9 times as large") would be clearer written as the reciprocal of the sensitivity (1/0.11 ≈ 9).
