## Writing Quality Review, round 2: "How Much of a Nested Index Correlation Is Construction?" (APFM)

Skill: `vendor/sciwrite/SKILL.md`, section-review mode, all five passes on every section (loaded together with ARS `academic-paper`, revision mode, as CLAUDE.md requires). Independent editor; fresh context.
Scope: `docx_build/r2/manuscript_anonymized.md` and `r2/supplementary_material.md`. Edits are confined to prose string literals in `docx_build/r2_text.py` and `docx_build/r2_lit.py`; the reference list is untouched. Round-1 report `14_sciwrite_review.md` was read first, so this round neither repeats nor reverses those edits.
Overrides: no em dashes; numbers, intervals, p-values, citations, cross-references, hypothesis labels, outcome words, decision rules and technical claims stay as they are; conventional Methods passives are kept.
Gate constraint found this round: `numgate.py` counts the digits inside index and frequency codes ("VN30" gives token "0", "M30" gives "0", "VN100" gives "00", "30-minute" gives "30"), and it also counts every new "Section/Table/Eq. n" cross-reference. As a result, no definition that contains such a code or a new cross-reference can be added in a language round. The affected items are listed as content notes (N2, N7).

Backups: `r2_text_pre_sciwrite2.py`, `r2_lit_pre_sciwrite2.py`. Nothing committed.

### Summary

After round 1 the prose is clean. Clutter phrases, smothered verbs and passives that hide the actor are essentially gone. What remained were (i) a few buried or overloaded sentences, the worst being the H1 decision rule (about 17 words between subject and verb) and a single paragraph of about 330 words in Section 4.4; (ii) one undefined abbreviation in the main text ("RE" in Section 4.7, used in Eq. (16), Table 8 and Table 9); and (iii) table and figure legends that do not stand alone (DCCA, MF-DCCA, GARCH, OLS, QLIKE, EWMA, RE, SE, TOST and P_cap undefined in the legends that use them). There were also two small cases of terminology drift ("single-factor" vs "factor-model"; "damping factor" not tied to "sensitivity"). I made 24 wording edits, and the gate passes.

Final counts (`checks_v3.py`): abstract 211 words (unchanged); main text excluding tables 6,941 words (was 6,850; the growth is legend definitions, since table notes are counted); supplement 3,207 (was 3,194). `numgate compare gate_pre_sciwrite2`: GATE PASS. `checks_v3.py`: FAILED: 0.

---

### Section: Title and Abstract

- Pass 1 Clutter: 0 issues. Pass 2 Voice: 0 (all active). Pass 3 Architecture: 0. Sentence lengths vary from 15 to 45 words. Pass 4 Terminology: 0 edits. DCCA is defined; "benchmark", "lower bound", "sensitivity", "purged coefficient" and "order-free attribution" match Section 4.2 exactly. Pass 5: abstract numbers 0.11 and 0.10 match the Table 5 sensitivity mean (0.108) and the Table 4 like-for-like gap mean (0.1015).
- Deliberately left: "Purging the overlap lowers the correlation with large caps by about 0.10" has no explicit subject (it means VN100's correlation with VN30). Adding "VN100" would add gate token "00" (content note N7).

### Section 1 Introduction

| # | Pass | Original | Revision | Severity | Rationale |
|---|---|---|---|---|---|
| 1.1 | 3 | "...the like-for-like gap between nested and purged coefficients is 0.099–0.104; because κ hardly varies with the timescale (0.47–0.52), the Pearson version gives the same answer." | "...is 0.099–0.104. Because κ hardly varies with the timescale (0.47–0.52), the Pearson version gives the same answer." | MINOR | A 50-word sentence carried two findings plus a causal clause behind a semicolon. Splitting it makes "three main findings" countable. |

- Passes 1, 2, 4 and 5: 0 further issues. The C6 duplicate (Chen et al. 2016) is left as in round 1.
- Content note N1 (claim wording): "On the purged series, horizon dependence is confined to intraday broad-market pairs". Broad-market pairs are not the purged series, and the P_cap–VN30 slope is not significant at any frequency (Section 5.4). See N1.

### Section 2 (2.1–2.6, Table 1)

| # | Pass | Location | Original | Revision | Severity | Rationale |
|---|---|---|---|---|---|---|
| 2.1 | 3 | 2.4 | "Non-synchronous trading depresses short-horizon correlations (Epps 1979), with a size that depends on sampling (Chang et al. 2021)" | "..., an effect whose size depends on the sampling scheme (Chang et al. 2021)" | MINOR | "with a size" attached loosely to "correlations". The appositive names the effect. "Sampling scheme" is the concept in Chang et al. |
| 2.2 | 4 | Table 1 note | (DCCA and MF-DCCA used in the Method column, undefined in the legend) | added "DCCA: detrended cross-correlation analysis; MF-DCCA: multifractal DCCA;" | MINOR | Legends must stand alone (acronym austerity). |

- 2.1, 2.2, 2.3, 2.5 and 2.6: Passes 1, 2, 3 and 5 found nothing further. Passives in 2.6 ("has not been extended") describe work nobody has done, so they are correct. ASEAN, S&P 500 and Nikkei 225 are standard names.
- Left: "M30 to daily" in the Table 1 "This study" row is the first appearance of a frequency code, before Section 3.2 defines it. Gate-blocked (N2). "Mean-MF-X-DMA" is left as in round 1 (R4.c).

### Section 2.7 Estimands and hypotheses

| # | Pass | Original | Revision | Severity | Rationale |
|---|---|---|---|---|---|
| 2.7.1 | 3 | "Rule: the lower 95% bound of the like-for-like gap (VN30–VN100 minus P_cap–VN30; P_cap is the overlap-purged mid-cap series) exceeds 0.05, the estimation tolerance of Section 4.4, at every frequency." | "Rule: at every frequency, the lower 95% bound of the like-for-like gap exceeds 0.05, the estimation tolerance of Section 4.4; the gap is VN30–VN100 minus P_cap–VN30 (P_cap is the overlap-purged mid-cap series)." | MAJOR | Buried predicate: about 17 words between "bound" and "exceeds", with a nested parenthesis inside it. A reader needs the decision rule in one pass. The rule itself (lower 95% bound > 0.05 at every frequency) is unchanged. |

- Passes 1, 2, 4 and 5: 0. H2–H4 rules have their subject and verb within 8 words. The E1–E3 sentence is long but parallel.
- Left: "M30 and H1" in the H2 rule come before their Section 3.2 definition. Gate-blocked (N2).

### Section 3 Institutional background and data

- Pass 1–5: 0 edits. 3.1 has six features and six items, so the count is correct. "Was amended by Decree 245/2025/ND-CP" is a passive with the actor named, so it stays. Sentence lengths in 3.1 range from 4 to 35 words.
- Content note N5: "Regimes use the 20-day rolling standard deviation of returns (Fig. 1)" does not name the index (VNINDEX for the chronological and VNINDEX-quartile regimes, VN30 for the VN30 quartiles). Naming it adds "VN30" tokens, so it is gate-blocked.

### Section 4 Methodology (4.1–4.7, Box 1)

| # | Pass | Location | Original | Revision | Severity | Rationale |
|---|---|---|---|---|---|---|
| 4.1 | 4 | 4.7 | "replacing the regime correlation ρ_r by the static correlation ρ_st changes the variance by [Eq. (16): RE = ...]" | "... changes the portfolio variance by the relative error (RE) [Eq. (16)]" | MAJOR | "RE" was never spelled out in the main text but runs through Eq. (16), Section 5.6, Table 8, Table 9 and Table S14. "Relative error" is the term Section 4.4 already uses ("relative-error statistics"), so the term matches its own earlier use. |
| 4.2 | 3 | 4.4, para 2 | one ~330-word paragraph: bootstrap design, replicate counts, interval type, p-value floor, Holm floor, studentization, multiple-testing families, TOST | split after "...use 1,999 replicates." into (a) resampling design and replicate counts and (b) intervals, p-values, multiplicity and TOST | MAJOR | The paragraph had two separate topics. The second now opens with its topic sentence ("Intervals are percentile 95% intervals ..."), and "Because of the resolution limit" now sits beside the floor it refers to. No words changed. |
| 4.3 | 4 | Box 1 notes | "...correlation of the directly constructed P_cap series exactly." | "...correlation of the directly constructed overlap-purged series P_cap exactly; subscripts A, B and M: child, parent and remaining constituents." | MINOR | The Box is meant to be used alone (Section 6.2), but its subscripts and P_cap were defined only in Lemma 1. Child, parent and remaining constituents are the Lemma's own terms. |

- 4.1, 4.2, 4.3, 4.5 and 4.6: Pass 2 found the standard Methods passives ("are computed", "is biased toward"). Each either names the actor or describes a property, so they stay. Pass 1: none. Pass 3: Corollary 4 is long but mathematical (left, as in round 1).
- Content note N3: "999 for the factor-model, lead–lag and materiality statistics" (4.4). "Materiality" appears nowhere else in the paper. It may mean the H1 materiality test or the E3 misstatement, and the next sentence gives "relative-error statistics" 1,999 replicates. The authors should name the estimand. I could not infer it safely.

### Section 5 Results (5.1–5.8, Tables 2–9, Figs. 2–4)

| # | Pass | Location | Original | Revision | Severity | Rationale |
|---|---|---|---|---|---|---|
| 5.1 | 3 | 5.2 | "The three-pair gap, which also uses the broad-market pairs that cannot be purged by weight, is 0.086–0.096, with Cohen's q (Cohen 1988) of 0.78–0.89." | "The three-pair gap is 0.086–0.096, with Cohen's q (Cohen 1988) of 0.78–0.89; it also uses the broad-market pairs, which cannot be purged by weight." | MINOR | About 13 words between subject and verb. The result now comes first and the qualifier second. Non-restrictive "which" is correct because no broad-market pair can be purged (Section 6.3). |
| 5.2 | 4 | 5.4 | "the damping factor is 0.106–0.112" | "the damping factor (the sensitivity) is 0.106–0.112" | MINOR | Banana Rule: Section 4.5 says the slope is "damped by the sensitivity of Eq. (10)", and Section 5.4 renames it "damping factor". The gloss shows they are one quantity. A new "Eq. (10)" reference would add a gate token. |
| 5.3 | 4 | 5.5 lead | "the Forbes–Rigobon and single-factor tests" | "the Forbes–Rigobon and factor-model tests" | MINOR | The Table 7 caption and the next paragraph ("The factor model explains why") say "factor model"; "single-factor" was a third name. |
| 5.4 | 3 | 5.5, para 2 | "...but not between chronological episodes (Δβ = 0.008, [−0.128, 0.140]), and adding 2021 as a crisis (789 days) changes neither result (Forbes–Rigobon p = 0.987; Δβ = −0.005, [−0.122, 0.124])." | "...but not between chronological episodes (Δβ = 0.008, [−0.128, 0.140]). Neither result changes when 2021 is added as a crisis (789 days; Forbes–Rigobon p = 0.987; Δβ = −0.005, [−0.122, 0.124])." | MINOR | A 70-word sentence with three parenthetical statistics blocks. The robustness check is now its own sentence. (Starting it with "Adding 2021" would have created a false citation token in the gate.) |
| 5.5 | 4 | Table 3 note | DCCA, GARCH undefined in legend | added "DCCA: detrended cross-correlation analysis;" and "(generalized autoregressive conditional heteroskedasticity)" | MINOR | Legend acronyms. |
| 5.6 | 4 | Table 4 caption | "Average DCCA coefficients of nested and overlap-purged pairs" | "Average DCCA coefficients of the nested pairs and the overlap-purged pair" | MINOR | The table has one purged pair (P_cap–VN30); the plural implied more. |
| 5.7 | 4 | Table 4 note | P_cap undefined in legend | added "P_cap: overlap-purged mid-cap series;" | MINOR | Legend stands alone. |
| 5.8 | 4 | Table 5 note | "M = P_cap" | "M = P_cap (overlap-purged mid-cap series)" | MINOR | Same. |
| 5.9 | 4 | Table 6 note | P_cap undefined | added "; P_cap: overlap-purged mid-cap series" | MINOR | Same. |
| 5.10 | 4 | Table 7 note | "β: OLS slope of P_cap on VN30" | "β: ordinary least squares slope of P_cap (overlap-purged mid-cap series) on VN30" | MINOR | OLS and P_cap were undefined in this legend. |
| 5.11 | 4 | Table 8 note | "Panel A: RE of Eq. (16) ..."; QLIKE and EWMA used in column heads | "Panel A: RE: relative error of Eq. (16) ...; P_cap: overlap-purged mid-cap series; ... Panel B: QLIKE: quasi-likelihood loss; EWMA: exponentially weighted moving average; mean QLIKE over ..." | MAJOR | Table 8 used four undefined abbreviations in its headers. |
| 5.12 | 4 | Table 9 note | RE, SE, TOST, QLIKE, CI undefined | added "RE: relative error of portfolio variance; SE: standard error; TOST: two one-sided tests; QLIKE: quasi-likelihood loss; CI: confidence interval" | MAJOR | Table 9 is the summary readers jump to; it now stands alone apart from the frequency codes (N2). |
| 5.13 | 4 | Fig. 2 note | P_cap in caption, undefined | added "P_cap: overlap-purged mid-cap series;" | MINOR | Same. |

- 5.1, 5.3, 5.6, 5.7 and 5.8: Passes 1 and 2 found nothing. Pass 3 rhythm: each paragraph mixes short claim sentences ("The decomposition barely varies with the horizon.", "The factor model explains why.") with longer evidence sentences.
- Pass 5 checks: Table 9 H3 "Δβ = 0.210, p < 0.001" now matches Section 5.5 text (round-1 C5 resolved by the authors in the text; Table 7 still has no p column for Δβ). 2.23/9.38/1.84/2.07 in 5.6 match Table 8 Panel A. 0.0019–0.0024 in 5.4 matches the four Holm-surviving Table 6 slopes. Kurtosis "above 33 at M30" matches the minimum 33.94. Heavy-tailed averages 0.975–0.979 and 0.882–0.890 cannot be checked against a displayed table (they come from R output only). I found no mismatch.
- Left: Table 2 "Freq." codes, Table 9 "M30 or H1" and Table S8 "(M30)" are undefined in their legends. Gate-blocked (N2).

### Section 6 Discussion (6.1–6.3)

| # | Pass | Location | Original | Revision | Severity | Rationale |
|---|---|---|---|---|---|---|
| 6.1 | 3 | 6.2 | "A holder of the VNMIDCAP exchange-traded fund who hedges with VN30 futures keeps about a fifth of the variance on average and about half in calm markets." | "Hedging the VNMIDCAP exchange-traded fund with VN30 futures leaves about a fifth of the variance on average and about half in calm markets." | MINOR | Twelve words between the subject and "keeps". A gerund subject gives the same claim with the verb in position 9. |

- 6.1 and 6.3: Passes 1–5 found nothing to edit. 6.3 para 2 has five sentences of 20–30 words, but each is a separate limitation, so I kept the parallel shape (author voice).
- Content note N6: Section 6.1 says "crises also bring mid-cap-specific shocks". The evidence is the VN30-quartile residual-variance ratio (2.70 [1.92, 3.68]); the chronological-episode ratio is 1.42 [0.91, 2.15], whose interval includes 1. "On high-volatility days" would match the evidence more closely. This is a claim-scope change for the authors.

### Section 7 Conclusion

- Passes 1–5: 0 edits. Sentence lengths 12–40 words. Terms match Sections 4.2 and 5.
- Content note N1 also applies here: "The purged series shows ... horizon effects confined to the auction bars". The horizon effects are in the broad-market pairs, not in P_cap–VN30.
- N7 also applies: "removing the overlap lowers the correlation with large caps by about 0.10" (subject implicit).

### Supplement (Online Resource 2)

| # | Pass | Location | Original | Revision | Severity | Rationale |
|---|---|---|---|---|---|---|
| S.1 | 4 | Table S2 note | "DCCA quantities averaged ..." | "DCCA (detrended cross-correlation analysis) quantities averaged ..." | MINOR | The supplement is read separately, and DCCA was never defined in it. |
| S.2 | 4 | Table S4 note | (DMCA in caption, undefined) | "DMCA: detrending moving-average cross-correlation analysis; centered moving-average detrending ..." | MINOR | Legend acronym. |
| S.3 | 4 | Fig. S1 note | (MF-DCCA in caption, undefined) | "MF-DCCA: multifractal detrended cross-correlation analysis; q ∈ ..." | MINOR | Legend acronym. |

- Passes 1–3 and 5: 0 issues. Notes are short, and terms ("replicates", "factsheet", "first bar / last bar", "three-pair gap") match the main text.

---

### Totals by pass

| Pass | Edits applied | Reported only |
|---|---|---|
| 1 Clutter | 0 | none found after round 1 |
| 2 Voice and verbs | 0 | conventional Methods passives kept; "misstatement of portfolio variance" kept (defined estimand name) |
| 3 Sentence architecture | 7 (1.1, 2.1, 2.7.1, 4.2, 5.1, 5.4, 6.1) | Corollary 4; 6.3 para 2 |
| 4 Terminology and acronyms | 17 (2.2, 4.1, 4.3, 5.2, 5.3, 5.5–5.13, S.1–S.3) | frequency codes in legends and before Section 3.2 (N2) |
| 5 Numbers and citations | 0 | N1, N3, N5, N6, N7 below |

Severity of applied edits: MAJOR 5 (2.7.1, 4.1, 4.2, 5.11, 5.12); MINOR 19; CRITICAL 0.

### Top 5 Priority Revisions (all applied)

1. **2.7.1** H1 decision rule: the predicate is no longer buried, so the rule reads in one pass.
2. **4.1 / 5.11 / 5.12** RE defined as "relative error" at first use (Section 4.7) and in the Table 8 and Table 9 legends, matching "relative-error statistics" in Section 4.4.
3. **4.2** The 330-word inference paragraph in Section 4.4 is split into resampling design and p-values/multiplicity.
4. **5.11 / 5.12 / 5.5 / 5.10 and Box 1** Legends now define QLIKE, EWMA, SE, TOST, CI, GARCH, OLS, DCCA and P_cap, so Tables 3–9 and Box 1 stand alone (frequency codes excepted, N2).
5. **5.2 / 5.3** Terminology drift: "damping factor" glossed as the sensitivity; "single-factor" changed to "factor-model".

### Content notes for the authors (no numbers changed)

- **N1 (claim wording, Section 1 para 4 and Section 7).** "On the purged series, horizon dependence is confined to intraday broad-market pairs" and "The purged series shows ... horizon effects confined to the auction bars". Horizon dependence appears in the broad-market pairs, and the P_cap–VN30 slope is not significant at any frequency. Suggested: "Horizon dependence is confined to intraday broad-market pairs and comes from the auction bars; the purged pair shows none." This changes the claim, so I did not make it.
- **N2 (frequency codes, gate-blocked).** M30 and H1 are used before Section 3.2 defines them (Table 1 "This study" row; the H2 rule in Section 2.7), and they are undefined in the Table 2, Table 9 and Table S8 legends. Any definition adds digit tokens ("30-minute" gives "30"), which `numgate` rejects. Suggested: "at each of the 30-minute (M30) and 1-hour (H1) frequencies" in the H2 rule, and "1D, M30, H1, H4: daily, 30-minute, 1-hour and 4-hour bars" in the Table 2 and Table 9 notes, with a recorded gate exception.
- **N3 (Section 4.4).** "Materiality statistics" (999 replicates) is not defined anywhere and sits next to "relative-error statistics" (1,999). Please name the estimand.
- **N4 (round-1 C3 partly resolved).** Section 5.4 now says "at the M30 and H1 frequencies", but the abstract ("small intraday horizon dependence"), Section 1 ("intraday broad-market pairs") and Table 9 ("all at M30 or H1") still treat "intraday" as M30 and H1 only, although H4 bars are also intraday.
- **N5 (Section 3.2).** "Regimes use the 20-day rolling standard deviation of returns" does not say which index's returns.
- **N6 (Section 6.1 claim scope).** "crises also bring mid-cap-specific shocks" rests on the VN30-quartile ratio. The chronological-episode ratio interval [0.91, 2.15] includes 1.
- **N7 (abstract and Section 7).** "lowers the correlation with large caps" has no subject (it means VN100's correlation with VN30, after purging). Adding "VN100" is gate-blocked; a digit-free option is "lowers the parent's correlation with large caps".
- **C7 carried over.** No citation is a secondary-source ("telephone game") case.

### Deliberately left

- All round-1 edits are kept, and none was reversed. No em dashes were introduced; the only em dash in the files is in the Pearson (1897) reference title.
- Conventional Methods passives; the authors' short declarative openers; Corollary 4; the Section 2.6 order; the duplicate Chen et al. (2016) sentence (round-1 C6); "benchmark holdings"; "Mean-MF-X-DMA"; "misstatement of portfolio variance" (estimand name).
- The abstract is unchanged (211 words). Each candidate edit there would either add gate tokens or touch a claim.

### Verification

`python3 build_r2.py && python3 numgate.py compare <scratchpad>/gate_pre_sciwrite2 && python3 build_r2_package.py && python3 checks_v3.py` gives: GATE PASS; words: abstract 211, main text excluding tables 6,941, supplement 3,207; FAILED: 0. During editing the gate flagged one token: "0," from "P_cap–VN30, where" in the new H1 rule. I reworded it to "P_cap–VN30 (P_cap is ...)." I also avoided starting a sentence with "Adding 2021", which would have registered as a citation token. `ast.parse` passes on both edited files. Nothing committed.
