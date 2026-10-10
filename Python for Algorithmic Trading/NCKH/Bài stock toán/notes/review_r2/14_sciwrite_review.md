## Writing Quality Review: "How Much of a Nested Index Correlation Is Construction?" (APFM, round 2)

Skill: `vendor/sciwrite/SKILL.md`, full-review mode (loaded together with ARS `academic-paper`, revision mode, per CLAUDE.md).
Scope: `docx_build/r2/manuscript_anonymized.md` and `r2/supplementary_material.md`; edits applied to prose string literals in `docx_build/r2_text.py` and `docx_build/r2_lit.py`. Reference list untouched.
Overrides applied: no em dashes (Pass 3 dash advice not used); no change to numbers, intervals, p-values, citations, cross-references, hypothesis labels, outcome words, decision rules or technical claims; passive voice kept where conventional in Methods.

### Summary

The manuscript is already tight after two language rounds: clutter is rare, passive voice is limited and mostly conventional, and paragraphs open with their claim. The main remaining problems were terminology drift (Pass 4): one threshold called both "tolerance" and "margin" (the word the TOST test also uses), "benchmark" reused for P_cap, "damping factor" meaning 0.106 in Section 5.4 but "about ten" in Table 9, the undefined abbreviation "FR" in Table 9, and several names for the weight and for the remaining constituents. Sentence architecture had three buried or overloaded sentences in Sections 2.4 and 4.4 and one non sequitur in Section 5.4. All 25 edits change wording only; the number gate passes.

Final counts (checks_v3): abstract 211 words; main text excluding tables 6,844 words (was 6,832); supplement 3,194 words. `numgate compare`: GATE PASS. `checks_v3.py`: FAILED: 0.

### Pass 1: Clutter: 3 issues found (3 fixed)

| # | Location | Original | Revision | Severity | Rationale |
|---|---|---|---|---|---|
| 1.1 | Section 1, para 2 | "this number mixes economic linkage with the fact that VN30 stocks are counted on both sides" | "this number mixes economic linkage with the double counting of VN30 stocks on both sides" | MINOR | "the fact that" is dead weight; this gives a parallel noun pair (linkage / double counting). |
| 1.2 | Section 3.1 | "had not been put into operation" | "had not been implemented" | MINOR | Same meaning, shorter phrase. |
| 1.3 | Table 5 note | "Panel B is computed for the daily and 30-minute frequencies" | "Panel B covers the daily and 30-minute frequencies" | MINOR | Shorter; drops the passive. |

Left as is: the Section 1 sentence "Index-level co-movement is easy to misread even without overlap (Chen et al. 2016)" nearly repeats Section 2.3 ("Index-level co-movement is thus easy to misread even where indices do not overlap"). Deleting either copy would remove a citation instance and a claim, so both stay (see content note C6).

### Pass 2: Voice and Verbs: 2 issues found (2 fixed)

| # | Location | Original | Revision | Severity | Rationale |
|---|---|---|---|---|---|
| 2.1 | Section 4.4, para 2 | "so all inference resamples the data with the stationary block bootstrap ... and recomputes every curve and statistic in each replicate" | "so for all inference we resample the data with the stationary block bootstrap ... and recompute every curve and statistic in each replicate" | MINOR | Here an abstraction ("inference") does what the authors did; this names the actor. |
| 2.2 | Section 4.7 | "Intervals resample the full sample jointly, re-estimating ρ_st, and we compare \|RE\| with ..." | "We obtain intervals by resampling the full sample jointly and re-estimating ρ_st, and compare \|RE\| with ..." | MINOR | Inanimate subject ("Intervals resample"), then a switch to "we" in mid-sentence; now one actor throughout. |

Left as is: the conventional Methods passives ("was amended by Decree 245/2025/ND-CP", "The indices are computed in real time", "were obtained from TradingView" in Data availability). In each one the actor is named or does not matter. Nominalizations: none of the Pass 2 table patterns ("provides a review of", "performs an analysis of", and so on) occur. "Provides a framework for covered short sales" stays because "allows" would change the legal meaning.

### Pass 3: Sentence Architecture: 4 issues found (4 fixed)

| # | Location | Original | Revision | Severity | Rationale |
|---|---|---|---|---|---|
| 3.1 | Section 2.4, last sentence | "Herding in stress (Nguyen et al. 2023), sector connectedness above 60%, rising to near 90% during COVID-19 (Bui et al. 2022) and nonlinear regional dependence (Le et al. 2025) raise all correlations at once." | "Three forces raise all correlations at once: herding in stress (Nguyen et al. 2023), sector connectedness above 60% that rose to near 90% during COVID-19 (Bui et al. 2022) and nonlinear regional dependence (Le et al. 2025)." | MAJOR | About 30 words came between subject and verb, and the comma before "rising" made the list hard to parse. The predicate now comes first and a colon sets up the list. |
| 3.2 | Section 4.4, para 2 | "We use 499 replications for ... statistics, and 399 for the like-for-like gap under weight uncertainty. We use 199 for ... Table S6, and 999 for ..." | "We use 499 replicates for ... statistics; 399 for the like-for-like gap under weight uncertainty; 199 for ... Table S6; and 999 for ..." | MAJOR | A four-item list of replicate counts was split across two sentences with nested "and"s. Semicolons now separate the items (all counts and table references unchanged). |
| 3.3 | Section 4.4, para 2 | "Percentile p-values, p = 2 min{k₋ + 1, k₊ + 1}/(B + 1), where k₋ and k₊ count replicates at or below and at or above zero, cannot fall below 0.004 with B = 499 (reported as p < 0.005)." | "With B = 499 replicates, percentile p-values cannot fall below 0.004 (reported as p < 0.005): p = 2 min{k₋ + 1, k₊ + 1}/(B + 1), where k₋ and k₊ count replicates at or below and at or above zero." | MAJOR | Buried predicate (about 25 words between subject and verb). The claim now comes first and the formula follows the colon. |
| 3.4 | Section 5.4, para 1 | "None is significant at 1D or H4, so H2 is supported on the full data." | "None is significant at 1D or H4; with significant positive slopes at both frequencies the rule requires, H2 is supported on the full data." | MAJOR | Non sequitur: "so" made the 1D/H4 nulls the reason H2 is supported, but under the Section 2.7 rule the reason is the significant M30 and H1 slopes. The revision restates the rule's own condition, with no new claim. The text is generated conditionally on `intraday_ok`. |

Left as is: Corollary 4 and the 5.3 sentence on benchmark slopes are long but parallel and mathematical, so splitting them would not help. In Section 2.6 the search-strategy sentences sit after the gap statement; moving them is a structural choice for the authors (MINOR, not changed). Sentence-length rhythm: most paragraphs already mix short claim sentences with longer evidence sentences, and no paragraph has uniform lengths.

### Pass 4: Terminology: 16 issues found (16 fixed) + 4 reported only

| # | Location | Original | Revision | Severity | Rationale |
|---|---|---|---|---|---|
| 4.1 | Section 5.2 | "above the 0.05 margin at every frequency" | "above the 0.05 tolerance at every frequency" | CRITICAL | The H1 rule and Section 4.4 call 0.05 the "estimation tolerance"; "margin" is the TOST term (0.001). Mixing the two suggests the H1 threshold is an equivalence margin. |
| 4.2 | Section 4.2 | "P_cap is a shadow benchmark:" | "P_cap is a synthetic shadow series:" | MAJOR | "Benchmark" is the paper's term for ρ̲ (zero-correlation benchmark). Calling P_cap a benchmark overloads the key term. |
| 4.3 | Table 9, E2 comment | "Damping factor of about ten" | "Purged changes damped about tenfold" | CRITICAL | Section 5.4 defines "the damping factor" as 0.106–0.112. Table 9 used the same term for its inverse (about ten). |
| 4.4 | Section 6.1 | "reach it damped by a factor of about ten" | "reach it damped about tenfold" | MAJOR | Same conflict with the 5.4 definition of "damping factor". |
| 4.5 | Section 4.2 | "report the Shapley share φ_overlap/ρ_AB" | "report the Shapley overlap share φ_overlap/ρ_AB" | MINOR | Matches the Table 5 column name. |
| 4.6 | Table 9, E1 | "ρ̲; Shapley share" | "ρ̲; Shapley overlap share" | MINOR | Same. |
| 4.7 | Table 9, H3 | "FR adjustment ...", "FR p = 0.998" | "Forbes–Rigobon adjustment ...", "Forbes–Rigobon p = 0.998" | MAJOR | "FR" is defined only inside the Table 7 note as "p (FR)". Table 9 must stand alone (acronym austerity). |
| 4.8 | Section 5.6 | "in turbulent regimes" | "in crisis regimes" | MAJOR | Table 8 and Table 7 use "crisis"; "turbulent" reads as a third regime type. |
| 4.9 | Section 5.7 | "Proxies that replace the capitalization weight" | "Proxies that replace the free-float weight" | MINOR | w is defined as "the free-float weight of VN30 in VN100" (Section 4.2). |
| 4.10 | Section 4.2, Corollary 4 | "= 3.73 at the HOSE weight" | "= 3.73 at the factsheet weight" | MINOR | Elsewhere the paper calls the 0.6826 value "the factsheet weight"; "HOSE weight" was a one-off. |
| 4.11 | Box 1, step 2 | "Remainder volatility" | "Volatility of remaining constituents" | MINOR | Lemma 1 and the abstract define M as "the remaining constituents"; "remainder" was never defined. |
| 4.12 | Section 5.3, Fig. 4 text | "relative volatility of the remainder" | "relative volatility of the remaining constituents" | MINOR | Same. |
| 4.13 | Section 6.3 | "the remainder is no more volatile" | "the remaining constituents are no more volatile" | MINOR | Same. |
| 4.14 | Section 6.3 | "large mechanical components should be common" | "large components fixed by construction should be common" | MINOR | The paper's defining phrase is "fixed by construction" (abstract, Section 1, Section 7). "Mechanical" appears nowhere else for this concept. |
| 4.15 | Table 1, "This study" row | "Purged correlation is invisible in the nested one" | "Purged coefficient is invisible in the nested one" | MINOR | The paper's term is "purged coefficient". See content note C1 on "invisible". |
| 4.16 | Section 4.4 (two places) | "499 replications", "1,999 replications" | "499 replicates", "1,999 replicates" | MINOR | The same paragraph, the table notes and Online Resource 2 all say "replicates". |

Checked and consistent (no change): "overlap-purged coefficient" / "purged coefficient" (first use spelled out, then the short form); "nested pair(s)"; "VN30–VN100" (always an en dash); "like-for-like gap" / "three-pair gap"; "benchmark-first share" / "dependence-first share"; "zero-correlation benchmark" / "lower bound"; "reliable range" / s_rel; frequency codes 1D / M30 / H1 / H4 (defined in Section 3.2 and paired with words in table rows); "auction bars" / "opening bar"; "Online Resource 1/2". Abbreviations DCCA, DMCA, MF-DCCA, OLS, EWMA, QLIKE, TOST, GARCH and HOSE are defined at first use in the main text. DCCA is also defined in the abstract.

Reported, not changed:
- R4.a "benchmark holdings" (Section 2.1, Table 1 Cremers and Petajisto row) is the standard Active Share term for a fund's benchmark. Kept, because the meaning is the literal fund benchmark and the context makes it clear.
- R4.b The text mixes codes and words ("daily VN30 returns", "50 days at 1D"). Both forms are defined and the tables pair them ("Daily (1D)"), so this was left.
- R4.c "Mean-MF-X-DMA" (Table 1) is not expanded. It is the cited authors' model name; expanding it would add length for no gain.
- R4.d "intraday" is used for M30 and H1 only ("Positive slopes appear only for broad-market pairs at intraday frequencies"; Table 9 "all intraday"), although H4 is also an intraday bar (two H4 bars per day). See content note C3.

### Pass 5: Numbers and Citations: 0 edits; 7 content notes

I cross-checked the abstract, text, Box 1 and Tables 2–9 against each other. Examples: sensitivity mean 0.108 → abstract "about 0.11"; like-for-like gap mean 0.1015 → "about 0.10"; 1 − 0.6826 = 32%; 1/(1 − w) = 3.15 and w/(1 − w) = 2.15 match "315% long / 215% short"; 0.889² = 0.79 hedge share; 19 × 0.004 = 0.076 Holm floor; 0.001 × 4.5 < 0.005 TOST margin claim; 0.01/0.106–0.112 ≈ 0.09; four H2-family Holm p < 0.05 in Table 6; RE/SE range 0.13–1.50 matches Table 8; static QLIKE lowest for all four pairs in Table 8 Panel B; 539 + 250 = 789 crisis days with 2021. I found no number mismatch between abstract, text and tables. The content notes below are for the authors and change no numbers.

- **C1 (claim strength, Table 1).** "Purged coefficient is invisible in the nested one" is stronger than the paper's own result. The nested coefficient responds to the purged one with sensitivity 0.106–0.112, so changes are damped about tenfold, not invisible. Suggested wording for the authors: "Purged coefficient is largely masked in the nested one". This changes the claim, so I did not make it.
- **C2 (Corollary 4 rounding).** √3·w/(1 − w) with w = 1,316,288/1,928,303 gives 3.7252, which rounds to 3.73 only just. Correct as printed, but 3.725 is on the rounding edge; confirm against `REC['amplitude_ratio_max']`.
- **C3 ("intraday" scope).** The text treats H4 as non-intraday ("None is significant at 1D or H4"; "all intraday" in Table 9), yet the H4 bars are within-day session bars (Section 3.2). Consider "at the 30-minute and 1-hour frequencies" wherever "intraday" means M30 and H1 only.
- **C4 (sample labels).** Table 4 Panel B and Table 1 say "2014–2025", but per Section 3.2 M30 starts in January 2017 and H1/H4 end in December 2024. The label is the union of samples and is not wrong, but readers may take it as a common span.
- **C5 (Table 9, H3).** "Δβ = 0.210, p < 0.001" gives a p-value that appears neither in Table 7 nor in the Section 5.5 text (which gives only the interval [0.119, 0.306]). The number is traceable to `FAC['C']['p_d_beta']`. Consider adding the p-value to Table 7 so Table 9 summarizes rather than introduces it.
- **C6 (duplicate sentence).** Section 1 and Section 2.3 both say index-level co-movement is easy to misread without overlap (Chen et al. 2016). Cutting the Section 1 copy would save about 14 words but changes the citation multiset, so I left it for the authors.
- **C7 (citation integrity).** No statistic is cited only through a secondary source. The 60%/90% connectedness figures cite the primary study (Bui et al. 2022), and the S&P 500 and Nikkei 225 co-movement claims cite primary studies. No "telephone game" pattern found.

### Top 5 Priority Revisions (all applied)

1. **4.1** "0.05 margin" → "0.05 tolerance" (Section 5.2): this separates the H1 threshold from the TOST margin.
2. **4.3 / 4.4** "damping factor of about ten" → "damped about tenfold" (Table 9, Section 6.1): this removes one term carrying two values (0.106 vs ten).
3. **3.4** H2 non sequitur in Section 5.4: the support for H2 now follows from the decision rule, not from the 1D/H4 nulls.
4. **4.2** "shadow benchmark" → "synthetic shadow series" (Section 4.2): this keeps "benchmark" for ρ̲ only.
5. **3.1 / 3.3** buried predicates in Section 2.4 (forces that raise all correlations) and Section 4.4 (percentile p-value floor).

### Deliberately left

- All em-dash-free punctuation kept. No dashes introduced. The only em dash in the rendered files is inside the Pearson (1897) reference title, which is out of scope.
- Methods passives that are conventional; author voice in short declarative openers ("One mechanism drives the nested results.", "The auction bars drive the intraday result.").
- Section 2.6 order (gaps, then search strategy); duplicate Chen et al. (2016) sentence (C6); "benchmark holdings"; mixed 1D/daily usage; "Mean-MF-X-DMA".
- No change to Table 1 claim strength (C1) or any number, interval, p-value, citation, cross-reference, hypothesis label, outcome word or decision rule.

### Verification

`python3 build_r2.py && python3 numgate.py compare <scratchpad>/gate_pre_sciwrite && python3 build_r2_package.py && python3 checks_v3.py` → GATE PASS; words: abstract 211 | main text excl. tables 6,844 | supplement 3,194; FAILED: 0. While editing, the gate first flagged two tokens: "499," from the reordered p-value sentence, and a "0" token from "M30" in the new 5.4 clause. I reworded both ("With B = 499 replicates, ..."; "at both frequencies the rule requires") until the gate passed. Backups: `r2_text_pre_sciwrite.py`, `r2_lit_pre_sciwrite.py`. Nothing committed.
