# Language round 2 of 2 (final polish: proofreading + stop-slop + redline-edit, medium)

Date: 2026-10-10. Independent language editor, fresh context. The audit ledger was not read; the round-1 log
(`11_language_round1.md`) was read so that none of its choices was undone or repeated.
Sources edited: `project_R/docx_build/r2_text.py` (title/abstract checked, Sections 1, 2.7, 3–7, table notes,
supplement) and `project_R/docx_build/r2_lit.py` (Sections 2 intro, 2.2, 2.5, 2.6).
Skills and rules applied: `proofreading` (six checks, report mode, fixes then applied by the editor), `stop-slop`,
`copy-editing:redline-edit` at the **medium** level (applied directly, no CriticMarkup),
`skill gộp/rules/01_master_editorial_philosophy.md`, `02_mechanical_and_anti_ai_gate.md`, `03_semantic_and_logic_gate.md`,
and the wording parts of the section playbooks 01 (title/abstract), 02 (introduction), 06 (results), 07 (robustness), 08 (conclusion).

Method: scripted exact-match replacement (each OLD string asserted to occur exactly once; string-literal boundaries
preserved). Pre-edit copies of both sources and both rendered `.md` files are in the session scratchpad (`lang2_bak/`);
the edit script is `lang2_edits.py`, its log `lang2_log.json`. No `{...}` expression, number, percentage, author–year
citation, equation, cross-reference, hypothesis rule or outcome word was changed or moved; the reference list is untouched.

Conventions kept (style decisions not changed): American spelling; no serial comma (house style, kept as in round 1);
subscripts `ρ_AM`, `P_cap`, `s_rel`; Springer caption style without closing period; "Eq. 14" in the Table S13 caption
(frozen by the gate, as in round 1).

## 1. Proofreading report (six checks)

| Check | Found | Fixed | Left |
|---|---|---|---|
| 1 Structure | 4 | 2 | 2 |
| 2 Math notation | 1 | 1 | 0 new (round-1 symbol-reuse items still open) |
| 3 Statistical relevance | 0 | 0 | 0 |
| 4 Figures and tables | 5 | 5 | 0 new |
| 5 Grammar and style | 22 | 22 | 5 long list/equation sentences |
| 6 Abbreviations | 1 | 1 | 0 |

### Check 1: Paper structure
- [ERROR, HARD; round-1 item 5] The word "contribution" was absent from the Introduction. Fixed: "Our contribution is to build that version." (same claim as "We build that version", now named as the contribution).
- [WARN] The roadmap sat at the end of the findings paragraph. Fixed: moved to its own paragraph (playbook 02, paragraph 7); wording unchanged.
- [INFO] Abstract is 211 words (APFM limit 250; brief window 180–230). Its four parts (motivation, approach, numbers, implication) are present; the gap stays implicit, since adding a gap sentence would add a claim.
- [INFO] Section 3.1 now says "Six features", so round-1 item 1 has been resolved upstream. No action.
- Hypotheses before results, a quantitative conclusion and a thematic related-work section with a gap statement are all in place.

### Check 2: Math symbols and notation
Detected convention: plain italic scalars (Convention A/B do not apply).
- [WARN] Section 4.1: "The DCCA coefficient measures covariance at timescale s". Eq. (5) is a normalized coefficient. Fixed: "measures correlation".
- Round-1 items left open (they need notation changes): `B` (VN100 returns and bootstrap count), `β` (scaling slope and factor loading), `α` (intercept and f(α)).

### Check 3: Statistical relevance
No issues. Every comparison carries an interval, an adjusted p-value or a "descriptive" label.

### Check 4: Figures and tables
- [WARN] Terminology in Table S6: the caption says "gap interval" while the column header says "Three-pair gap". Fixed in the caption and in the Section 5.7 sentence that cites it.
- [WARN] Section 5.4 called the first-bar-removed statistic "the overlap gap". Output `R23_intraday_first_bar_removed.csv` defines `gap = nested_mean − pcap_vn30`, which is the three-pair gap. Fixed: "The three-pair gap does not change".
- [INFO] Note style: Tables 2, 3 and S8 used sentence glosses ("Kurt. is ...", "P_res is the residual ...") while every other note uses "label: gloss". Fixed in all three. Table 3's note now opens with "s_rel:".
- All notes have at most three sentences (`checks_v3.py`). Captions are noun phrases in one style.
- Round-1 items still open: Fig. 4 and Box 1 are cited in the Introduction before Figs. 1–3; figures are PNG.

### Check 5: Grammar and style
- Variant: American, with no deviations found. Em dashes in prose: 0.
- Long sentences (over 40 words): 23 before, 18 after. Five were split (abstract, Sections 2.2, 2.5, 2.7 H2 and 3.2). The rest hold lists of dates, bar times, citations or equations; splitting them would move numbers or symbols.
- Run-on or comma-spliced clauses fixed in Intro p2 and Section 5.4 (", and the test is inconclusive elsewhere").
- Ambiguous referents fixed: "This work" in Section 2.2 could be read as the present paper, so it is now "These studies"; "its size" in H1; "the question" in Section 2 intro.
- Zeugma fixed in Section 2.6 ("given inference under weight uncertainty" is now "equipped with inference ...").
- Logic slip fixed in Section 6.2: "Regime-conditioned tier correlations are not supported" is now "The case for regime-conditioned tier correlations is not supported" (the outcome word is kept).
- Prohibited or inflated vocabulary: none. "rather than" (4) marks real contrasts; "robust" (5) is used only in its statistical sense.
- Possessives on non-persons ("child’s weight") were kept as idiomatic, as in round 1.

### Check 6: Abbreviations
- [ERROR] GARCH was used undefined (Section 4.4, Table 3). Fixed at first use: "A GARCH(1,1)-t(5) calibration (generalized autoregressive conditional heteroskedasticity with Student-t errors; 300 simulations)". `checks_v3.py` now reports "GARCH defined".
- Round-1 item 2 (1D/M30/H1/H4 before Table 3) has been resolved upstream: Section 3.2 now expands them.
- CI and SE in table headers were left as standard.

## 2. Stop-slop findings and score

| Pattern | Found | Fixed | Left (reason) |
|---|---|---|---|
| Informal or vague verbs ("carry ... over", "gives", "needs", "beat", "combine") | 6 | 6 | 0 |
| Nominalization ("serves as a check of") | 1 | 1 | 0 |
| Repeated sentence opener ("With ... With ...", Section 5.3) | 1 | 1 | 0 |
| Formulaic paragraph openers ("Table N reports ..." five times in Section 5) | 5 | 2 (lists / presents) | 3 (plain signposting; rewriting them would be structural) |
| Vague declaratives or referents | 3 | 3 | 0 |
| Banned AI vocabulary, throat-clearing openers, intensifiers | 0 | – | – |
| "X, not Y" contrasts ("not of continuous trading", "Membership, not overlap") | 2 | 0 | kept: Keep-vs-Cut test, both carry information |
| Short summary lines ("Overlap thus inflates co-movement that is already strong.", "The factor model explains why.") | 2 | 0 | kept: they carry content, and the rhythm around them now varies |
| Em dashes | 0 | – | – |

Score after edits (1–10): Directness 9, Rhythm 8, Trust 8, Authenticity 8, Density 8, total **41/50** (round 1: 40/50; threshold 35).

## 3. Redline-edit (medium) categories

Level: medium. Variant: US (-ize, analyze, centered, toward; no UK forms).
Locked items: every number, percentage, `{...}` expression, citation, cross-reference, equation, hypothesis rule and
outcome word, plus the hedges "should", "only", "about", "to our knowledge" and "may". Values changed: 0 (verified by `numgate.py`).

| Category | Edits |
|---|---|
| CE-02 grammar/agreement | 1 (#11) |
| CE-04 punctuation (comma between clauses) | 1 (#28) |
| CE-08 abbreviation at first use | 1 (#21) |
| CE-11 pronoun reference | 3 (#9, #12, #16) |
| CE-12 consistency of terms (overlap-purged coefficient, sensitivity vs slope, three-pair gap, nested coefficient) | 8 (#2, #3, #4, #7, #24, #29, #31, #35) |
| CE-13 clarity, wordiness, precise verbs, sentence splits, logic | 17 (#1, #5, #10, #13–15, #17–20, #25–27, #30, #32–34) |
| Note style (consistency) | 3 (#22, #23, #36) |
| Structure (roadmap paragraph, contribution sentence) | 2 (#6, #8) |

Author queries: none raised as blocking. See Section 7 for items left to the authors.
Plain-language checks (these are checks, not a score; main text prose before References):

| Check | Before | After |
|---|---|---|
| Sentences | 343 | 350 |
| Mean sentence length (words) | 20.6 | 20.2 |
| Sentences over 25 words | 100 | 99 |
| Sentences over 40 words | 23 | 18 |
| Passive "be + -ed" constructions (approximate) | 34 | 34 |
| Abbreviations not expanded at first use | 1 (GARCH) | 0 |

Change budget: 36 edits; every hunk of a word diff of the rendered `.md` files (before and after) maps to a logged row
below; unlogged changes: 0. Locked items changed in value: 0.

## 4. Edit table
| # | File | Location | Before | After | Category |
|---|---|---|---|---|---|
| 1 | r2_text.py | Abstract | We carry the classical part–whole correlation identity over to detrended | We extend the classical part–whole correlation identity to detrended | precise verb |
| 2 | r2_text.py | Abstract | the overlap-purged correlation between the child and those constituents. The identity gives a | the overlap-purged coefficient between the child and those constituents. The identity yields a | terminology ("overlap-purged coefficient"); precise verb |
| 3 | r2_text.py | Abstract | to the purged correlation and an order-free attribution, and it needs only | to the purged coefficient and an order-free attribution, and it requires only | terminology; precise verb |
| 4 | r2_text.py | Abstract | per unit change in the purged correlation, and purging the overlap lowers | per unit change in the purged coefficient. Purging the overlap lowers | terminology; long sentence split (49 words) |
| 5 | r2_text.py | 1 Intro p2 | avoid the problem, but users of index-level data cannot, and index-level co-movement | avoid the problem; users of index-level data cannot. Index-level co-movement | run-on sentence split; flow |
| 6 | r2_text.py | 1 Intro p3 | We build that version. Lemma 1 shows | Our contribution is to build that version. Lemma 1 shows | contribution stated explicitly (proofreading 1.3 HARD rule; round-1 author item 5) |
| 7 | r2_text.py | 1 Intro p4 | responds to the purged coefficient with a slope of | responds to the purged coefficient with a sensitivity of | terminology: "slope" is reserved for the scaling slope of Eq. (13) |
| 8 | r2_text.py | 1 Intro p4 | regime-conditioned correlations do not beat a static one out of sample. Section 2 reviews the literature and states  | regime-conditioned correlations do not outperform a static one out of sample. [new paragraph] Section 2 reviews the literature and states  | register (informal "beat"); roadmap moved to its own paragraph (flow) |
| 9 | r2_lit.py | 2 intro | Five literatures bear on the question: | Five literatures bear on nested index correlations: | vague referent ("the question") |
| 10 | r2_lit.py | 2.2 | Chen et al. 2024), uses the coefficient to track contagion (Okorie | Chen et al. 2024). Other studies use the coefficient to track contagion (Okorie | long sentence split (54 words) |
| 11 | r2_lit.py | 2.2 | or information flow (Zhou et al. 2025), and builds scale-aware portfolios | or information flow (Zhou et al. 2025) and build scale-aware portfolios | agreement after split |
| 12 | r2_lit.py | 2.2 | al. 2025). This work treats the coefficient as a measure of economic dependence between disjoint assets. None of it analyzes | al. 2025). These studies treat the coefficient as a measure of economic dependence between disjoint assets. None of them analyzes | ambiguous referent ("This work" can be read as the present paper) |
| 13 | r2_lit.py | 2.5 | Benkraiem et al. 2022), a DCCA test finds it | Benkraiem et al. 2022). A DCCA test finds it | long sentence split (54 words) |
| 14 | r2_lit.py | 2.6 | but has not been carried to scale-wise detrended coefficients, given inference | but has not been extended to scale-wise detrended coefficients, equipped with inference | precise verbs; zeugma ("given inference") |
| 15 | r2_lit.py | 2.6 | intraday and daily frequencies. We searched Google Scholar | intraday and daily frequencies. For this review, we searched Google Scholar | transition into search description (flow) |
| 16 | r2_text.py | 2.7 H1 | almost no gap, so its size is an empirical | almost no gap, so the gap size is an empirical | pronoun reference ("its") |
| 17 | r2_text.py | 2.7 H2 | (Hong and Stein 1999), so broad-market coefficients should rise | (Hong and Stein 1999). Broad-market coefficients should therefore rise | long sentence split (45 words) |
| 18 | r2_text.py | 3.2 | ) serves cross-frequency comparisons; all other analyses use the full sample (1D:  | ) serves cross-frequency comparisons. All other analyses use the full sample (1D:  | long sentence split (57 words) |
| 19 | r2_text.py | 3.2 | Chronological crises combine a VNINDEX drawdown | Chronological crises require a VNINDEX drawdown | precise verb (all three criteria must hold, as the 2021/2025 sentence implies) |
| 20 | r2_text.py | 4.1 | The DCCA coefficient measures covariance at timescale s | The DCCA coefficient measures correlation at timescale s | precision: Eq. (5) is a normalized coefficient, not a covariance |
| 21 | r2_text.py | 4.4 | tolerance in advance, and a GARCH(1,1)-t(5) calibration (300 simulations) checks heavy tails. | tolerance in advance. A GARCH(1,1)-t(5) calibration (generalized autoregressive conditional heteroskedasticity with Student-t errors; 300 simulations) checks heavy tails. | abbreviation (GARCH) expanded at first use; sentence split |
| 22 | r2_text.py | Table 2 note | 'Kurt. is non-excess kurtosis; P_cap is the overlap-purged series of Eq. (6); | 'Kurt.: non-excess kurtosis; P_cap: overlap-purged series of Eq. (6); | note style consistent with other notes (label: gloss) |
| 23 | r2_text.py | Table 3 note | 'Largest scale (bars) at which the worst-case | 's_rel: largest scale (bars) at which the worst-case | note style; symbol glossed in note |
| 24 | r2_text.py | 5.3 | moving the index-level number by 0.01 requires | moving the nested coefficient by 0.01 requires | terminology (vague "index-level number") |
| 25 | r2_text.py | 5.3 | With weight uncertainty, the sensitivity interval is  | Under weight uncertainty, the sensitivity interval is  | repeated sentence opener ("With ... With ...") |
| 26 | r2_text.py | 5.3 | multiscale layer serves as a check of scale invariance | multiscale layer checks scale invariance | wordiness (nominalization) |
| 27 | r2_text.py | 5.4 | Table 6 reports reliable-range slopes | Table 6 lists reliable-range slopes | verb variety ("Table N reports" x5) |
| 28 | r2_text.py | 5.4 | }) and the test is inconclusive elsewhere. | }), and the test is inconclusive elsewhere. | comma between independent clauses |
| 29 | r2_text.py | 5.4 | The overlap gap does not change  | The three-pair gap does not change  | terminology: R23 "gap" is nested mean minus P_cap–VN30, i.e. the three-pair gap |
| 30 | r2_text.py | 5.5 | Table 7 reports the Forbes–Rigobon | Table 7 presents the Forbes–Rigobon | verb variety |
| 31 | r2_text.py | 5.7 | The daily gap interval stays within | The daily three-pair gap interval stays within | terminology (Table S6 reports the three-pair gap) |
| 32 | r2_text.py | 6.2 | viable. Regime-conditioned tier correlations are not supported: | viable. The case for regime-conditioned tier correlations is not supported: | logic: a hypothesis, not a correlation, is (not) supported; outcome word kept |
| 33 | r2_text.py | 7 | fixed by construction. Carrying the part–whole  | fixed by construction. Extending the part–whole  | precise verb; matches abstract |
| 34 | r2_text.py | Supplement intro | reports robustness checks referred to in the main text. | reports the robustness checks cited in the main text. | wordiness |
| 35 | r2_text.py | Table S6 caption | Table S6 Sensitivity of the gap interval to | Table S6 Sensitivity of the three-pair gap interval to | terminology; caption matches column header |
| 36 | r2_text.py | Table S8 note | f'P_heur replaces w by the VN30–VN100 correlation ({rng(w_heur, 4)}); P_ratio = B − A; P_res is the residual of B on A. | f'P_heur: w replaced by the VN30–VN100 correlation ({rng(w_heur, 4)}); P_ratio = B − A; P_res: residual of B on A. | note style (label: gloss) |

## 5. Word counts
- `checks_v3.py`: abstract **211** (before 213), main text excluding tables **6,912** (before 6,899), supplement **3,194** (before 3,195).
- Main text stays inside the 6,400–7,000 window and the abstract inside 180–230. The +13 words come from the GARCH expansion (+7), "Our contribution is to" (+3), "For this review," (+3), "nested index correlations" (+2) and the three-pair labels (+2), offset by shorter wording elsewhere.

## 6. Build, checks and gate output
```
$ python3 build_r2.py
built .../r2/supplementary_material.docx
built .../r2/manuscript_anonymized.docx
built .../r2/manuscript_with_authors.docx

$ python3 checks_v3.py
words: abstract 211 | main text excl. tables 6912 | supplement 3194
PASS abstract <= 250 words
... (all PASS, including "note <= 3 sentences" for every note and "abbreviation GARCH defined at or before first use")
FAILED: 0

$ python3 numgate.py compare <scratchpad>/gate_pre_lang2
GATE PASS
```
The gate passed on the first run, so no edit had to be reverted. Both sources parse as valid Python.
`build_r2_package.py` was not run, and nothing was committed.

## 7. Items left for the authors
1. Symbol reuse (from round 1): `B` (VN100 returns and bootstrap replication count), `β` (scaling slope and factor loading), `α` (intercept and f(α)). Renaming needs equation edits.
2. Figure and Box numbering against first citation (from round 1): Fig. 4 and Box 1 are cited in the Introduction before Figs. 1–3.
3. Round-1 item 6 (P_heur described as "a volatility-scaled weight") is resolved upstream: that phrase no longer appears, and Section 5.7 ("proxies that replace the capitalization weight, such as the VN30–VN100 correlation") now agrees with the Table S8 note.
4. The abstract states the gap only implicitly. A gap sentence such as "Existing DCCA studies treat nested pairs as if they were disjoint" would add a claim, so it was not inserted.
5. Section 6.3: "IDX30 within LQ45; we did not compute them ..." keeps a semicolon, because a full stop after "LQ45" changes a gate token (as in round 1).
6. Section 3.1: "a framework for covered short sales that, to our knowledge, had not been put into operation" mixes present and past perfect tense. Changing it to "has not been" would change the time claim, so the authors should confirm which status applies at submission.
