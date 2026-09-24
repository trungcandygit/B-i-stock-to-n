# Proofreading Report — Nested Equity Index Correlations Overstate True Co-Movement: Evidence from Vietnam

**Date:** 2026-09-24
**Source:** Round-3 output (`docx_build/stage5.py` applied), re-scanned with `docx_build/checks.py` plus a full manual read
**Skills:** `proofreading` (six checks, report mode) + `stop-slop`. Gate: `academic-paper`.
**Round:** 4 of 4 (verification pass on the language round).

---

## Scorecard (residual findings on the Round-3 text)

| # | Check                   | Errors | Warnings | Info | Total |
|---|-------------------------|--------|----------|------|-------|
| 1 | Paper Structure         | 0      | 0        | 0    | 0     |
| 2 | Math Symbols & Notation | 0      | 0        | 1    | 1     |
| 3 | Statistical Relevance   | 0      | 0        | 0    | 0     |
| 4 | Figures & Tables        | 0      | 0        | 0    | 0     |
| 5 | Grammar & Style         | 1      | 5        | 1    | 7     |
| 6 | Abbreviations           | 0      | 0        | 1    | 1     |
|   | **Total**               | **1**  | **5**    | **3**| **9** |

---

## Overall Assessment

After Round 3 the paper passes every structural, statistical, figure and abbreviation check. The automated checks
(`checks.py`) confirm:
- no em dashes;
- no "e.g."/"i.e." without a comma;
- no Wh- sentence openers and no "not X, but Y" frames;
- every table and figure cited before it appears;
- all 23 references cited and no orphan citations.

The residual findings were small consistency and voice issues, all fixed in `stage6.py`.

### Top Issues to Address

1. **[ERROR] Check 5.4** — The single serial comma ("commodity baskets, and cross-border assets") broke the house style. Fixed.
2. **[WARN] Check 5.1/5.2** — Passive and past tense in §2.1 ("were synchronized", "were computed", "is evaluated"). Now "We synchronize…", "We evaluate…".
3. **[WARN] Check 5.12** — "Firstly/Secondly/Thirdly" vs "First/Second/Third" elsewhere. Unified to "First/Second/Third".

---

## 1. Paper Structure

**Summary:** No issues found. The roadmap lists Sections 1.1, 2, 3 and 4, matching the headings (1 Introduction, 2 Methods, 3 Results, 4 Discussion with 4.1–4.4), as APFM's Title/Abstract/Introduction/Methods/Results/Discussion structure requires.

### Findings

No issues found.

## 2. Math Symbols & Notation

**Summary:** Detected notation convention: B.

### Findings

- [INFO] §2.2 — "ordinary least squares, OLS (m = 1 …)" read awkwardly. **Fixed** to "ordinary least squares (OLS; m = 1 representing linear DCCA)".

## 3. Statistical Relevance

**Summary:** No issues found.

### Findings

No issues found.

## 4. Figures & Tables

**Summary:** After regenerating Figs. 1 and 3 in R, all axes are labeled. The Table 6 caption matches its content, and every table note has at most 3 sentences.

### Findings

No issues found.

## 5. Grammar & Style

**Summary:** American English is used consistently.

### Findings

- [ERROR] 5.4 — serial comma inconsistency. **Fixed.**
- [WARN] 5.1 — "The index series were synchronized … log returns were computed". **Fixed:** "We synchronize … and compute …; no index price is filled or interpolated".
- [WARN] 5.1 — "Regime dependence is evaluated under two definitions". **Fixed:** "We evaluate regime dependence…".
- [WARN] 5.12 — "Firstly/Secondly/Thirdly". **Fixed.**
- [WARN] stop-slop — "Both profiles are subsequently partitioned" **fixed** to "then". "The empirical research design operates across two complementary sample tiers:" **fixed** to "We use two sample tiers."
- [WARN] clarity — abstract: "Risk models that use these correlations" had an unclear antecedent. **Fixed:** "Risk models built on index-level correlations therefore conflate…".
- [INFO] — The remaining adverbs are technical (statistically, significantly, logarithmically, jointly, separately, respectively), so they are kept.

## 6. Abbreviations

**Summary:** All body abbreviations are introduced before use; abstract abbreviations (DCCA, ASEAN) are introduced in the abstract.

### Findings

- [INFO] — Index tickers (VN30, VN100, VNINDEX, SET50, IDX30, LQ45, KLCI) are proper names, not abbreviations, and need no expansion.

---

## stop-slop score (academic register)

| Dimension | After Round 3 | After Round 4 |
|---|---|---|
| Directness | 8 | 8 |
| Rhythm | 7 | 8 |
| Trust | 8 | 8 |
| Authenticity | 8 | 8 |
| Density | 8 | 9 |
| **Total** | **39/50** | **41/50 (pass)** |

## Academic-paper gate (Round 4 — final)

- **Numbers:** a numeric-token diff of Round-2 vs Round-4 text shows no result number changed. The only removed tokens are frequency labels ("M30, H1, H4, 1D") dropped from a redundant clause and the index names in one rewritten sentence.
- **R traceability:**
  - `run_all.R` was re-run end to end with the fixed seed after the figure-label change.
  - All tabulated CSVs are byte-identical to the previous run; see AUDIT_LEDGER Iter 21.
- **Citations:** 23 references, all cited, no new authors.
- **Word budget:** under 8,500 for the whole manuscript (final count in AUDIT_LEDGER Iter 21).
- **Journal rules:**
  - Springer caption style.
  - Every table and figure cited before it appears.
  - Every table note has at most 3 sentences.
  - Declarations present: ethics, data, code, funding (pointer to title page), conflict of interest, AI use.
