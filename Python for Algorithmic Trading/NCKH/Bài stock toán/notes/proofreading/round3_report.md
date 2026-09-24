# Proofreading Report — Nested Equity Index Correlations Overstate True Co-Movement: Evidence from Vietnam

**Date:** 2026-09-24
**Source:** `submission/final_APFM/Co_movement_manuscript_APFM_final.docx` (Round-2 state, text extracted by `pdump.py`; no line numbers, so paragraph anchors are used)
**Skills:** `proofreading` (JakobThumm/proofreading, six checks, report mode) + `stop-slop` (hardikpandya/stop-slop). Gate: `academic-paper` (numbers, citations, word budget, journal rules).
**Round:** 3 of 4 (first language round after the two ARS revision rounds).

---

## Scorecard (findings before fixes)

| # | Check                   | Errors | Warnings | Info | Total |
|---|-------------------------|--------|----------|------|-------|
| 1 | Paper Structure         | 4      | 3        | 1    | 8     |
| 2 | Math Symbols & Notation | 0      | 1        | 1    | 2     |
| 3 | Statistical Relevance   | 0      | 0        | 1    | 1     |
| 4 | Figures & Tables        | 1      | 1        | 2    | 4     |
| 5 | Grammar & Style         | 3      | 24       | 3    | 30    |
| 6 | Abbreviations           | 3      | 0        | 0    | 3     |
|   | **Total**               | **11** | **29**   | **8**| **48** |

---

## Overall Assessment

The Round-2 manuscript is sound in substance. Every quantitative claim carries an interval or a test, every table and
figure is cited before it appears, and all 23 references are cited. The weak spots were in the language layer:
motivational clauses inside the Methods, inflated or adverb-heavy wording typical of generated text ("genuine",
"markedly", "strictly", "directly", "critical"), a few unsupported absolute claims ("cannot substitute", "guarantee"),
and three abbreviations used in the body before they were introduced.

### Top Issues to Address

1. **[ERROR] Check 1.9** — Four Methods paragraphs open with motivation ("To guarantee simultaneity…", "To preserve long-range dependence…", "To remove deterministic intraday patterns…", "To verify whether the surge…").
2. **[ERROR] Check 6.3** — ASEAN, OLS and GARCH are used in the body before being introduced (ASEAN was fixed in Round 2; OLS/GARCH are fixed here).
3. **[WARN] Check 5.10** — "Statistical weights cannot substitute for capitalization weights in nested index systems" generalizes beyond one market; "To guarantee simultaneity" has no backing.
4. **[WARN] Check 5.5 / stop-slop** — about 25 filler adverbs and inflated words.
5. **[ERROR] Check 4.9** — Fig. 1 has no x-axis label and Fig. 3 no y-axis label.

---

## 1. Paper Structure

**Summary:** The abstract has all four parts in order and includes numbers (222 words; APFM allows 150–250). The introduction has motivation, the gap ("However, this literature…"), the approach, the contributions and a present-tense roadmap. The main problems were motivation inside the Methods and one unsupported paragraph in the introduction.

### Findings

- [ERROR] §2.1 ¶2 — Methods paragraph opens with a motivation/guarantee clause.
  > To guarantee simultaneity and prevent alignment bias, the index series were…
  Suggestion: state the procedure. **Fixed:** "We synchronize the index series by exact inner joins…" (Round 4 moved it to we-voice and present tense).
- [ERROR] §2.2 ¶1 — The rationale clause is unsupported and misdescribes the profile.
  > To preserve long-range dependence and eliminate high-frequency drift, we map…
  **Fixed:** "We map…".
- [ERROR] §2.2 ¶4 — Motivation inside the Methods.
  > To remove deterministic intraday patterns … that would otherwise spuriously inflate…
  **Fixed:** "Within each segment, we fit…".
- [ERROR] §2.4 ¶1 — Uses "verify" without formal backing.
  **Fixed:** "To test whether the rise … reflects a structural change or volatility expansion, we apply…".
- [WARN] §1 ¶4 — Vague declarative plus an unsupported claim ("Emerging markets face substantial risk from passive tracking.").
  **Fixed:** the paragraph was rewritten; the gap is stated ("neither study addresses overlapping constituents") and the unsupported sentence removed.
- [WARN] §1.2 — Novelty is not stated as "to the best of our knowledge, the first…".
  **Not applied:** the authors cannot verify priority within the no-new-references constraint (ARS IRON RULE: no unverifiable claims). The gap statement stays hedged.
- [WARN] §3 — No explicit hypotheses (H1, H2…).
  **Not applied:** APFM empirical papers state tested nulls inline (e.g., H0: ρ* ≤ ρlow in Table 4); adding a hypothesis block would push the word budget.
- [INFO] §4.4 — The conclusion now carries the key number (about 0.09) and no new content.

## 2. Math Symbols & Notation

**Summary:** Detected notation convention: B (scalars and vectors plain). Symbols are defined at or immediately after first use (where-clauses after Eqs. 3, 6, 8, 12, 16–17). Equations are numbered (1)–(17).

### Findings

- [WARN] Eq. (4)–(6) — FDFA,1 and FDFA,2 are introduced after Eq. (5) and before Eq. (6); acceptable (post-equation where-clause).
- [INFO] 2.10 — Several numbered equations are not referenced by number. Springer numbers display equations by convention, so they are kept.

## 3. Statistical Relevance

**Summary:** All inferential claims now carry bootstrap intervals, p-values or power (Tables 2, 4–6, §3.6). Table 1 is descriptive, and the Monte Carlo counts are stated in the Table 3 notes.

### Findings

- [INFO] Fig. 2 has no uncertainty bands. The intervals for the summary statistics are in Tables 2 and 5–6; bands on 30 scales × 4 pairs × 4 panels would clutter the figure.

## 4. Figures & Tables

**Summary:** Every table and figure is cited in the text before it appears (checked by `checks.py`). All figures use line types plus markers (grayscale-safe) with a legend, and the notes explain the shading and the dotted and dashed lines.

### Findings

- [ERROR] 4.9 — Fig. 1 has no x-axis label; Fig. 3 has no y-axis label.
  **Fixed in R:** `run_all.R` adds `x = "Date"` (Fig. 1) and `y = f(α) (panel a) or h_xy(q) (panel b)` (Fig. 3). Figures were regenerated with the fixed seed.
- [WARN] 4.3 — Captions end without a period.
  **Kept:** the Springer caption style ("Fig. 1 Caption text", no final punctuation) governs. Journal rule > generic skill rule.
- [INFO] 4.5 — The PNG figures are embedded in the docx; EPS vector versions are supplied separately in `final_APFM/figures/` as Springer requires.
- [INFO] Table 6 caption said "(M30)" although it reports 1D/H1/H4. **Fixed:** "Scaling slopes of DCCA coefficients at the daily, 1-hour and 4-hour frequencies".

## 5. Grammar & Style

**Summary:** Detected variant: American English (analyze, behavior, annualized), with no British spellings. No em dashes, and "e.g." and "i.e." are always followed by commas. The main issues were filler adverbs, inflated vocabulary and possessives on inanimate nouns.

### Findings

- [ERROR] 5.4 — Serial comma is inconsistent: "commodity baskets, and cross-border assets" is the only serial comma in the paper. **Fixed in Round 4** toward the house style of no serial comma, which is used about 40 times and follows the supervisor's edits.
- [ERROR] 5.5 — "Utilizing" in the abstract. **Fixed:** "Using" (Round 2).
- [ERROR] 5.10 — "guarantee" (§2.1) and "verify" (§2.4). **Fixed** (see Check 1).
- [WARN] 5.5 possessives — "Vietnam’s HOSE", "the previous session’s reference price". **Fixed:** "Because the HOSE prohibits…" and "the reference price of the previous session". The data-availability and funding possessives ("vendor’s terms", "journal’s policy") are kept as legal phrasing.
- [WARN] 5.10 — "Statistical weights cannot substitute for capitalization weights in nested index systems." **Fixed:** "In this nested system, statistical weights are a poor substitute…".
- [WARN] stop-slop adverbs/inflated wording (21 instances), all **fixed**: frequently (×2), increasingly, predominantly, strictly (×3), fully, directly (×3), markedly (×3), essentially, continuously, mathematically, purely, materially, econometrically, "genuine" (×5), "critical" (×2), "fundamental", "sharp distinction", "a well-established empirical stylized fact", "the natural responses".
- [WARN] stop-slop false agency / vague declaratives — "Standard risk models thereby conflate…", "this reliance … creates an econometric bias", "This gap in the benchmark design interacts directly with…", "In empirical market index administration, the constituent weights are not mathematically static." **All rewritten or cut.**
- [WARN] 5.9 redundancy — The second-tier sample paragraph repeated the first tier's overlap sentence. **Removed** (Round 2).
- [INFO] 5.1 — Passive voice in the Methods. Converted to "we" where an actor exists (§2.1, §2.2, §2.4, §4.1). Passive is kept for fixed properties of the data (e.g., "the partitioning is repeated").
- [INFO] 5.12 — First/Second/Third markers span adjacent paragraphs only (contributions, §3.7, §4.1), so no change.

## 6. Abbreviations

**Summary:** The abstract introduces DCCA and ASEAN itself. In the body, three abbreviations were used before introduction.

### Findings

- [ERROR] ASEAN — First body use was "mature ASEAN exchanges". **Fixed:** "the Association of Southeast Asian Nations (ASEAN)" (Round 2).
- [ERROR] OLS — First used as "the volatility-scaled OLS slope" (§2.2). **Fixed:** "ordinary least squares, OLS" at first mention.
- [ERROR] GARCH — First used as "GARCH(1,1) surrogates" (§3.3). **Fixed:** expanded at first mention.

---

## stop-slop score (academic register)

| Dimension | Round-2 text | After Round 3 |
|---|---|---|
| Directness | 6 | 8 |
| Rhythm | 6 | 7 |
| Trust | 6 | 8 |
| Authenticity | 5 | 8 |
| Density | 6 | 8 |
| **Total** | **29/50 (revise)** | **39/50 (pass ≥ 35)** |

**Register adaptation (logged in AUDIT_LEDGER Iter 21, D14):** stop-slop's "no passive voice at all", "use *you*" and
"kill all adverbs" rules conflict with the academic register that the academic-paper skill and APFM require. They
were applied as follows:
- we-voice wherever an actor exists;
- no second person;
- filler and intensifying adverbs removed;
- technical adverbs kept (statistically, significantly, logarithmically, jointly, separately).

## Academic-paper gate (Round 3)

- Numbers: no number was changed by the language edits; `checks.py` and a diff of the numeric tokens confirm this.
- Citations: all 23 references are cited, no citation lacks a reference, and no new author was added (user constraint).
- Word count: 7,587 words for the full manuscript including tables and references (limit 8,500). The abstract is 222 words.
- Table notes: every note has at most 3 sentences.
