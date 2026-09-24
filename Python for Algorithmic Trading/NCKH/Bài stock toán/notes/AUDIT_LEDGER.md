# Audit Ledger — BaiBao_DCCA_EN

## Iter 22 — submission package for Asia-Pacific Financial Markets + repository clean-up

- D20 Package `submission/APFM_submission/` modelled on the authors' folder layout (00–08). Title page and cover letter are rebuilt from the authors' uploaded templates for this manuscript and journal (the templates were for a different paper and journal).
- D21 Author order per the user: Nguyen Thanh Binh^a, Nguyen Van Trung^a,* (corresponding), Ha Hong Hanh^b (moved to third), Nguyen Bach Diep^a. CRediT roles are kept as supplied by the authors, reordered only.
- D22 Double-blind compliance: `02_Manuscript_Anonymized.docx` has creator/lastModifiedBy metadata cleared and `word/people.xml` (tracked-change author list, which named the supervisor) removed. The build asserts that no author name or e-mail domain appears.
- D23 Replication package (Online Resource 1): R code with in-package data paths, all outputs and figures, README with the table↔output map. Raw TradingView data are excluded under the vendor terms (consistent with the Data availability statement).
- D24 Highlights and the separate competing-interest declaration are optional for APFM; they are provided and flagged as such in the checklist.
- D25 Removed redundant files (history kept in git):
  - duplicate `Data/` (byte-identical to `project/data/`; its README moved there);
  - `submission/excel/` (old Excel charts, superseded by the R figures);
  - `submission/final_APFM/` (superseded by `APFM_submission/`);
  - `project/figures/` (old Python figures);
  - `merged.txt` (raw phrasebank dump, duplicated in `skill gộp/`);
  - `TLTK/` (text of an uncited article);
  - two empty `.schema` files and all `.DS_Store` files.

## Iter 21 — full 5-seat review (academic-paper-reviewer `full`) → 2 ARS revision rounds → 2 language rounds (proofreading + stop-slop, gated by academic-paper)

User pre-authorized autonomous completion; the decisions below were taken by skill defaults.

**Round map** (ARS IRON RULE: at most 2 revision rounds; language rounds added at the user's request)
1. **R1 (review + revision):** 5-seat panel under sprint contract `reviewer/reviewer_full/v2` → major_revision (F2: D1 and D3 block) → roadmap RR1–RR18 (`review_full/06_editorial_synthesis.md`). Revision in `docx_build/stage3.py` + `stage3_text.py`, with new R analyses in `project_R/run_revision.R` (outputs R1–R7).
2. **R2 (re-review + residual fixes):** three-gate re-review (`review_full/08_rereview_round2.md`) → all RR resolved (RR5 as a limitation, RR17 REVIEWER_DISAGREE upheld). 15 residual fixes in `stage4.py` (`proofreading/round2_edits.md`). The revision loop closes here.
3. **R3 (proofreading + stop-slop):** six-check report (`proofreading/round3_report.md`), 48 findings, 59 edits (`stage5.py`, `round3_edits.md`); stop-slop score 29 → 39/50.
4. **R4 (second proofreading + stop-slop pass):** 9 residual findings, 10 edits (`stage6.py`, `round4_edits.md`); stop-slop score 41/50. Academic-paper gate passed.

**Decisions**
- D14 stop-slop is applied in academic register. Its "no passive / use *you* / kill all adverbs" rules conflict with the APFM register required by academic-paper. Applied as: we-voice where an actor exists, no second person, filler and intensifying adverbs removed, technical adverbs kept.
- D15 Proofreading rules overridden by journal rules: captions without final period (Springer style); no serial comma (manuscript house style); numbered display equations kept; no "first to…" novelty claim, which is unverifiable without new references (IRON RULE).
- D16 Figures: x label "Date" (Fig. 1) and y label f(α)/h_xy(q) (Fig. 3) added in `run_all.R`. Full re-run with the fixed seed: all 26 CSVs byte-identical to the previous run, confirming reproducibility.
- D17 Table 6 caption corrected (it reported 1D/H1/H4, not M30); "at least 0.052" → "at least 0.05" (rounded tables give 0.053); δ wording ("variance of VN30 returns").
- D18 Numeric-token diff of Round-2 vs Round-4 text: no result number changed in the language rounds.
- D19 Final checks:
  - length: 7,604 words including tables and references (< 8,500); abstract 222 words (150–250);
  - page count: 21;
  - docx validates against the original;
  - references: all 23 cited, no new authors;
  - tables and figures: every one cited before it appears; every note ≤ 3 sentences.

**Open items for the authors** (unchanged): fill the Title_Page.docx placeholders; open the docx once in Microsoft Word to check the OMML equations (LibreOffice does not render them); obtain the VNMIDCAP history if possible (RR5).

## Iter 20 — supervisor revision (Hạnh, 24/9) + R replication + APFM formatting (ARS academic-paper revision mode, 2 rounds; academic-paper-reviewer quick re-check)

User pre-authorized autonomous completion (no questions); decisions below were taken by skill defaults.

**Decisions**
- D1 Accepted all supervisor tracked changes (56 ins / 38 del, incl. 2 paragraph merges); fixed artefacts they introduced.
- D2 Comment 48/49 → institutional context moved out of Methods into §1.1 "Current Situation and Institutional Background of the HOSE".
- D3 Comment 65 → "Source:" line on every table and figure; notes cut to ≤ 3 sentences; every table/figure cited before it appears.
- D4 Comment 117 → final section "4 Discussion and Conclusion" with 4.2 Limitations and Future Research (journal structure Intro/Methods/Results/Discussion, Asia-Pacific Financial Markets instructions).
- D5 All experiments re-run in R (project_R/run_all.R; seed-fixed). R reproduces the Python DCCA values exactly (1D VN30–VNINDEX curve identical to 1e-7).
- D6 VN70/VNMIDCAP: no series exists in data, pipeline archive or figure workbooks → all VN70 results removed (IRON RULE: no fabricated data); disclosed as limitation. The uploaded 05_Replication_Package (405 stocks, 2024–2026, no caps/constituents, different paper) cannot rebuild VN70 → not used (scope creep).
- D7 Forbes–Rigobon Panel A did not reproduce (paper 0.629/t=7.71 → R 0.844/t=−2.28); paper re-framed to interdependence; Panel B reproduced (t=0.97).
- D8 Monte Carlo reliability run as 1,002 sims/frequency (6 ρ0 × 167) → s_rel 50/444/233/88 (old 34/217/141/57 came from 48 sims while text claimed 1,000).
- D9 Table 1 recomputed (old skew/kurt wrong); Table 7 recomputed (old direction reversed); MF-DCCA widths and detrending sensitivity recomputed.
- D10 Crisis rule changed from ">30% drawdown" (2018 fails: 26.2%) to ">25% drawdown and ≥45% top-quartile-volatility days", both computed in R.
- D11 References: removed unverifiable Goh & Wong 2020, Vo 2017, Nguyen & Nguyen 2021, Lee & Azali 2012; corrected Epps 1979, Karim & Ning 2013, Lean & Teng 2013 to verified records; no new authors added (user rule). Springer name–year style.
- D12 Mandatory statements: Ethics, Data availability, Code availability, COI, AI-use in manuscript; CRediT + Funding on separate Title_Page.docx (double-blind journal) with highlighted placeholders for the authors.
- D13 Round 2: inline math in prose replaced by words; display equations kept. Word count 8,083 (< 8,500); abstract 198.

**Open items for the authors**: fill Title_Page.docx placeholders; check OMML equations once in Microsoft Word; obtain VNMIDCAP history if possible (reviewer issue 1).

## Iter 19 (this pass) — proofreading review round 11 (3 ERROR, 4 WARN)

Round 11 verified the Iter 18 proxy rename was clean in running text/tables (all 51 symbol occurrences
byte-identical, no leftover snake_case, consistent en dashes) but found the rename never reached the
embedded figure, plus two pre-existing bare-Unicode math symbols the exhaustive re-scan finally caught.

**ERROR fixed:**
- **1** (Figure 1's legend, baked into `media/image1.png`, still read "Weighted Real Proxy-VN30" — the
  old snake_case name, title-cased, with a hyphen instead of the paper's en dash): no source plotting
  script for this specific chart existed in the project (the pipeline's `make_figures.py` generates
  different figures), so regenerated it from scratch in matplotlib using Table 1b's already-verified
  numbers, with the corrected legend "Real-Weighted Proxy–VN30" and an added x-axis title ("Trading
  Frequency," previously missing per an earlier round's INFO note) — visually confirmed the new PNG.
- **2** (bare Unicode "⊂" outside math mode, Abstract and Section 3.1 — the paper's only unwrapped
  relational symbol; ≤, ≈ etc. are always wrapped): changed both to `$\subset$`.
- **3** (bare Unicode "R²" in the Abstract, inconsistent with `$R^2$` used correctly in Section 3.4 and
  Table 3/4 — the exact defect class an earlier round already fixed for the tables but missed here):
  wrapped as `$R^2$`.

**WARN fixed:**
- Two different names for the same proxy — Abstract/Introduction said "real-capitalization-weighted
  proxy," Section 3.4's formal definition said "real-weighted proxy" — unified on
  "real-capitalization-weighted proxy" (the more informative form) in Section 3.4's list; also added a
  forward pointer in the Introduction ("denoted $P^{\text{real}}$; constructed in Section 3.4") since the
  bare symbol appeared there before its formal definition.
- $\lambda_{xy}(q)$, $\tau(q)$, $\alpha(q)$, $f(\alpha)$ (Section 3.6) were defined but never reported
  numerically anywhere in the results: reworded to explicitly state only the generalized Hurst exponent
  $h(q)$ and its spectrum width are carried forward into Section 4.4, and that the other four symbols
  characterize the full multifractal structure without being reported themselves — rather than silently
  leaving them as orphaned symbols.
- Figure 1 and Table 1b showed only point averages with no uncertainty indicator despite the 0.007–0.062
  Monte Carlo error band being available: added a source-line footnote to Table 1b stating the band
  applies per cell (adding literal error bars to the regenerated figure was avoided since the band varies
  by $\rho_0$ and $s$ rather than being a single fixed CI per bar, which a literal error bar would
  misrepresent).
- Contribution (1) in the Introduction was vague ("detailed empirical evidence... across four
  timeframes") next to two concrete, numeric contributions (2) and (3): reworded to state the actual
  numbers already established elsewhere (0.955–0.992 vs. 0.848–0.925).

**INFO noted, not actioned:** DCCA/MF-DCCA introduced abbreviation-first rather than "full term (ABBREV)"
order (applied consistently both times, low impact); roadmap paragraph has no opening linking phrase
(already a deliberate fix from an earlier round per the zero-tolerance passive/content-free-opener rule);
"Table 1b" labeling convention (no "Table 1a" exists); Figure 1's two-shade-of-green series distinction
has no texture/pattern differentiator; $\beta$ used unsubscripted for two different regressions in
Section 3.4 vs. Tables 3/4 (context disambiguates).

## Iter 18 (this pass) — user feedback + proofreading review round 10 fixes

**User feedback (direct, not from a review agent):**
- The backtick-wrapped `` `reliable = False` `` (Section 4.3) rendered as a code-style badge in the
  preview, out of place in an academic paper. Rewrote as prose: "are flagged as unreliable and do not
  support the paper's main conclusions."
- The four proxy names (weighted_real, weighted_heuristic, ratio, residual_DEPRECATED) were written as
  literal snake_case code identifiers throughout the running text and tables, reading like a code
  variable dump rather than academic notation. User chose (via AskUserQuestion) the highest-effort
  option: assign formal math symbols and use them everywhere. Introduced $P^{\text{real}}$,
  $P^{\text{heur}}$, $P^{\text{ratio}}$, $P^{\text{res}}$ at their definition in Section 3.4 (each also
  given a natural-language name: "the real-weighted proxy," "the heuristic-weighted proxy," "the ratio
  proxy," "the deprecated-residual proxy"), and replaced all ~50 subsequent occurrences across the
  Abstract, Introduction, Sections 3.5, 4.2–4.6, 5, 6, 8, and Tables 1b/3/4 (including every
  "weighted_real–VN30"-style pair name). Verified zero snake_case identifiers remain anywhere in the
  document. Also unified $r_t^{\text{mid}}$ → $r_t^{\text{real}}$ (the proxy's own return-series formula)
  so the construction formula's superscript matches its new symbol $P^{\text{real}}$, avoiding a
  two-symbols-one-concept split.

**Proofreading review round 10 (proofreading-skill-only, per user's cost-saving instruction to stop
re-running the full paper-writing-skill gates) — 1 ERROR + 8 WARN found and fixed alongside the above:**
- ERROR (Check 6.4): Section 4.1 re-introduced "1D"/"M30" with a second "full term (ABBREV)"
  parenthetical, already defined in Section 3.1 — removed the redundant re-definition.
- WARN (Check 2.7/2.9): the OLS equation's bare full-ticker subscripts ($r_{VN100,t}$, $r_{VN30,t}$)
  were inconsistent with the paper's \text{}-wrapping convention, and the shorthand switch to
  $r_{100,t}$/$r_{30,t}$ two lines later was never explained — wrapped consistently and added "where the
  subscripts 100 and 30 abbreviate VN100 and VN30" at first use.
- WARN (Check 2.3): $\alpha$ denoted the regression intercept (Sections 3.3/3.4) and, unrelatedly, the
  multifractal singularity strength $\alpha(q)$ (Section 3.6) — added a disambiguating parenthetical at
  the Section 3.6 definition.
- WARN (Check 2.5): equation (7) (Markowitz variance) was the only numbered equation set inline instead
  of displayed like (1)–(6)/(2b) — promoted to a `$$...$$` display equation.
- WARN (Check 2.2): the subscript $p$ meant "asset pair" throughout Sections 3.3–3.6 but was reused for
  "portfolio" in Section 4.6's $\sigma_p^2$ — renamed to $\sigma_{\text{port}}^2$ throughout Section 4.6,
  with a clause noting the distinction from the pair subscript $p$.
- WARN (Check 2.6): Table 3's header mixed a `$$R^2$$` display-math block inside a table cell with a
  bare Unicode β instead of $\beta$ — normalized both to inline `$R^2$`/`$\beta$`, and did the same in
  Table 4's header.
- WARN (Check 2.4): Table 3's footnote had "p<0.01" and "(m=1)" outside math mode — wrapped both in `$$`.
- WARN (Check 4.1/4.8): Table 1b was discussed in prose but its label was never cited by name — added
  "Table 1b reports the same pattern numerically by frequency:" as an explicit lead-in.
- WARN (Check 3.1): Figure 1 showed group averages with no uncertainty indicator or explanatory note —
  added a clause in the Section 4.2 lead paragraph pointing readers to the Section 4.3 Monte Carlo error
  band (0.007–0.062) as the relevant uncertainty context, rather than regenerating the chart (no source
  plotting script was located).

**Verification:** re-grepped the full document; zero remaining snake_case proxy identifiers, all four new
symbols ($P^{\text{real}}$ ×27, $P^{\text{heur}}$ ×6, $P^{\text{ratio}}$ ×9, $P^{\text{res}}$ ×9) used
consistently.

**Process note:** per user instruction, closure-loop rounds from here forward use ONLY the `proofreading`
skill (paper-writing-skill's gates remain closed from round 7 and are not re-run), to save tokens. The
next round should specifically re-verify this pass's large rename didn't introduce any new
inconsistency (e.g., a stray hyphenation, a table row whose symbol doesn't match its neighbors) in
addition to the standard Check 2/6 sweep.

## Iter 17 — combined gate + proofreading review round 9 (2 ERROR, several MINOR/INFO)

Fresh `general-purpose` reviewer (no context) re-verified every Iter 16 fix against the database
independently (all confirmed correct, including re-deriving the $h(q)$/series_role clarification from
scratch) and re-ran the full mechanical gate, full semantic gate (all ~50 cross-references traced,
zero dangling/mismatched), and proofreading Check 2/6, plus viewed Figure 1 directly. Found the round-8
proofreading pass had fixed the $w_{\text{real}}$-style unwrapped-word bug everywhere except one
remaining spot, and one new notation gap (a never-named symbol).

**ERROR fixed:**
- **1** (Section 3.6/equation 6: three instances of bare `DCCA` subscript — $f_{DCCA}^2(v,s)$ ×2 and
  $\rho_{DCCA}(s)$ — missed by the Iter 16 sweep, which fixed this exact defect class in Section 3.4/8
  but not Section 3.6): wrapped all three in `\text{}`, matching the `\text{DCCA}` convention used
  correctly in 12 other instances throughout the paper (Section 3.2's equations, Abstract, Section 3.5).
- **2** (the detrending order is used as the symbol $m$ in Table 3's note and Section 6's prose, but
  Section 4.3, which defines the concept in words, never ties the symbol to it): added "denoted $m$" at
  the concept's first prose definition in Section 4.3.

**MINOR/INFO reviewed, not fixed** (judgment calls, not defects): equation (7) set inline rather than
displayed like the other 7 equations (stylistic, not incorrect); Figure 1 shows only means without error
bars (the underlying range is already in the text; regenerating the chart is out of scope without its
source script); Figure 1's x-axis has no explicit "Trading Frequency" title (categories are
self-explanatory); Figure 1's caption is terse but the preceding paragraph supplies the missing context;
6 of 8 numbered equations are never cited by number (equations 1/2/2b/5/6/7 stand alone as derivations,
which is normal); "timeframe" vs. "trading frequency" used interchangeably (unlikely to confuse); Table
1's medians aren't materialized in the DB schema (independently reconfirmed correct against the raw CSV,
a pipeline-documentation note, not a paper defect); "840 shuffled replications" describes 840
already-averaged rows rather than 840 raw shuffle draws (cosmetic, the cited mean is correct either way).

**Verdict:** paper-writing-skill's gates (mechanical + semantic, all ~50 cross-references, every
numeric claim spot-checked against the DB) returned fully clean — no new findings in that lens at all
this round. Only the proofreading skill's math-notation check (2.2/2.7) found anything, and both were
narrow, mechanical fixes.

**Process note (user instruction):** from this point forward, closure-loop review rounds use ONLY the
`proofreading` skill (not the full paper-writing-skill gates, which are considered closed after 7 clean
rounds) — narrower scope, lower token cost, focused on math notation/abbreviations/terminology
("từ vựng") consistency.

## Iter 16 — proofreading skill pass (ERROR/WARN findings, mapped to CRITICAL/MAJOR)

Applied `~/.claude/skills/proofreading` (SKILL.md) against `final-translation.md`, adapted for a Markdown
econometrics paper rather than the skill's default LaTeX/ML-conference target (LaTeX-specific rules —
booktabs tables, IEEE caption packages, vector-figure format, `\label`/`\ref` discipline, H1/H2
hypothesis labels, theorem/algorithm-backed contributions — do not apply to this venue and were not
enforced). This is the first pass to inspect Figure 1's actual image content, since the file was missing
until Iter 15 restored it.

**ERROR-level (math notation, Check 2) — fixed:**
- Five unwrapped English-word subscripts/superscripts in Section 3.4's proxy formulas render as products
  of italic letters in real LaTeX/MathJax rather than as labels: $r_t^{mid}$, $w_{real}$ (×3),
  $w_{heuristic}$ (×2), $r_t^{ratio}$, plus one more $w_{real}$ instance in Section 8. All wrapped in
  `\text{}`, matching the `\text{full}`/`\text{rel}`/`\text{static}`/`\text{true}` convention already used
  correctly elsewhere in the paper — this was a localized inconsistency, not a paper-wide pattern.
- $N$ (total return observations) was used in equation (2b) at its first appearance in Section 3.2 but
  only ever defined in prose later, in Section 4.3 — a genuine used-before-defined violation. Added its
  definition immediately after equation (2b), alongside $n(s)$'s existing definition.
- $h(q)$ in the Legendre transform (Section 3.6, "$\tau(q) = qh(q)-1$") was never defined and is
  ambiguous against the three DIFFERENT exponents just introduced one sentence earlier ($h_x(q)$,
  $h_y(q)$, $\lambda_{xy}(q)$) — confirmed against the database schema (`mfdcca_multifractal_spectrum`
  has a `series_role` column, i.e. the spectrum is computed per-series, not jointly for a pair) that
  $h(q)$ denotes $h_x(q)$ or $h_y(q)$, never $\lambda_{xy}(q)$. Added an explicit sentence establishing
  this before the transform, and clarified in the same edit that Section 4.4's reported widths are
  computed per series, not jointly per pair — a fact that was already true of the numbers but not stated.
- $F_{xy}^2(s)$ itself, and the base series $X_t$/$Y_t$ underlying the tilde-decorated
  $\widetilde{X}_v(k)$/$\widetilde{Y}_v(k)$, were used in equations (1)-(2) without ever being named in
  prose. Extended the existing "where" clause to name both.
- A dangling relative clause ("which follows a Student-t distribution...") continued equation (2b)'s
  sentence across a paragraph break with no grammatical antecedent in the same sentence. Reworded to
  "This statistic follows..." as a self-contained sentence.

**ERROR-level (abbreviations, Check 6) — fixed:**
- DCCA and MF-DCCA were each expanded once in the Abstract but used bare at their first body occurrence
  (Introduction, paragraph 1) — the skill requires independent introduction in the body even when the
  abstract already expanded the term. Expanded both at first body use.

**HARD rule (contribution list, Check 1.3) — fixed:**
- The word "contribut-" never appeared anywhere in the Introduction (the paper said "three main
  findings," not "contributions") — changed to "three main contributions" and reworded the three list
  items to open with "we" for parallelism.

**WARN-level — fixed:**
- HOSE was introduced in the Abstract but used only once there (introduction-for-a-single-use is
  unnecessary per the skill); removed the parenthetical there since the body independently and correctly
  reintroduces "Ho Chi Minh City Stock Exchange (HOSE)" in Section 3.1.

**WARN-level — reviewed, not fixed (author-judgment / venue-calibration, not defects):**
- Figure 1 (bar chart, now viewable for the first time) has correct axis labels, a readable legend, no
  chartjunk, and no 3D/gradient effects, but shows only the mean DCCA correlation per frequency with no
  error bars or range indicator. The underlying range this would show (e.g. 0.955–0.992) is already
  reported in the surrounding prose (Section 4.2), so no information is hidden from the reader; adding
  error bars would require regenerating the chart from its original plotting script, which was not
  located. Left as a residual, judgment-level enhancement rather than a correctness defect.
- Possessive-apostrophe rule (5.5, prefer "of X" over "X's" for inanimate/concept nouns) and the abstract
  word-count/150-word guideline (1.1) are calibrated for CS/ML conference papers; applying them to this
  finance/econometrics paper's natural academic register (e.g., "the market's volatility regime," a
  ~310-word abstract, both standard for the venue) would fight the already-established craft register
  from the paper-writing-skill's own review. Not applied.
- Raster figure format (PNG vs. vector PDF/SVG) and LaTeX-specific table/caption/float rules
  (booktabs, `\label`/`\ref`, IEEE caption packages) do not apply to a Markdown paper headed for Word
  submission to a domestic Vietnamese journal. Not applicable, not flagged as defects.

**Verification:** re-grepped the full document for any remaining unwrapped 3+ letter English-word
subscripts/superscripts inside math mode after the fixes — zero remaining hits.

## CLOSURE — round 7 (fresh `general-purpose`, no context) returned zero CRITICAL and zero MAJOR

Per gate_semantic.md S31, this is the closure reviewer's sign-off: after re-running the full mechanical
gate (every en-dash, passive-voice, antithesis, and banned-word hit individually inspected, not just
counted) and the full S1–S31 semantic gate over the entire document fresh, independently re-verifying
essentially every headline number against the database/raw CSV, and tracing all 30+ cross-section
references, the reviewer found **zero CRITICAL and zero MAJOR findings** and stated explicitly: "I
believe this paper has reached closure... further rounds are very likely to yield only diminishing-return
cosmetic polish, not substantive defects." The four highest-risk recent edits (§4.3 detrending-order
attribution, §4.5 swing-ratio claim, §8 Limitation 1 date-coverage, §4.6 minvar sentence) were each
independently re-derived and confirmed accurate.

**Iter 15 — trivial post-closure polish (MINOR items from round 7, applied for completeness, not required for closure):**
- §4.1: "18.5–21.7 times" → "18.5–21.6 times" (independent recomputation from raw CSV gave 18.47–21.58×).
- Abstract and §4.5: "0.848–0.926" → "0.848–0.925" (true max from `dcca_curves` is 0.9254).
- §3.3 line 99: loosely bundled cross-reference "(Section 4.3 and Section 6 report these results)"
  tightened to "(detrending orders in Section 4.3, scale ranges in Section 6)."
- §3.5: "time-robust characterization" (unquantified "robust") → "period-independent characterization."
- Abstract: added a one-clause gloss for VN30/VN100/VNINDEX at first use ("three nested Ho Chi Minh City
  Stock Exchange indices of increasing breadth") per S1, since the paper may reach readers outside the
  domestic Vietnamese context who don't already know these three indices nest.
- **Figure 1 image restored**: `media/image1.png`, referenced in §4.2 but missing from the working
  directory (a Word→Markdown export artifact — the media folder wasn't copied alongside the .md file),
  was extracted from the original `BaiBao_DCCA_VN.docx` (`word/media/image1.png`, byte-identical: same
  97717-byte PNG) and placed at `media/image1.png` relative to `final-translation.md`. The figure now
  resolves.

**Status: the closure-gate loop (S31) is CLOSED.** Seven independent review rounds (see Iter 10–14 below
for full history) progressively found and fixed 7+7+1+2+1+2+1 CRITICAL findings and a larger number of
MAJOR/MINOR findings, each round narrower than the last, until round 7 returned a clean sign-off. Six of
those seven rounds found at least one CRITICAL or MAJOR defect that a prior round's own fix had
introduced — the loop's insistence on a genuinely independent, no-context reviewer for every round (never
trusting the author's self-assessment) is what caught each of those self-inflicted regressions before
they could compound. The paper is ready for a final human read-through and, when desired, export to
Word.

## Iter 14 (this pass) — fixes responding to genuinely-independent review round 6 (1 CRITICAL, 2 MAJOR, 2 MINOR)

Round 6 reviewer (fresh `general-purpose`, no context) independently re-derived essentially every cited
statistic from the DB/CSV; all matched. Found one CRITICAL self-contradiction (Iter 13's own §4.3 rewrite
misattributed detrending order to Section 6, contradicting both Section 6's own text and §4.3's own later
paragraph two paragraphs down — an error introduced by the immediately preceding fix), plus two MAJOR
findings.

**CRITICAL fixed:**
- **C1** (§4.3's opening paragraph, rewritten in Iter 13, claimed the detrending order "enter[s] through
  the separate stratified re-estimation reported in... Section 6," but Section 6 itself says "Section
  4.3 reports the complementary check across detrending orders," and §4.3's own text three paragraphs
  later contains that exact analysis): corrected the attribution — detrending order is analyzed later in
  Section 4.3 itself; Section 6 is now correctly described as reporting the scale-range robustness check.

**MAJOR fixed:**
- **M-A** (§4.5's Iter 13 fix claimed the three original pairs' regime swing is "an order of magnitude
  smaller than weighted_real's," but querying `regime_dcca_curves` for all pairs/frequencies/regimes
  shows this holds only for VN30–VN100, ~10.8×; VN30–VNINDEX is only ~3.8× smaller and VN100–VNINDEX
  ~5.3× smaller, both well short of an order of magnitude): corrected to "roughly 3–10 times smaller...,
  narrowest for the two indices sharing VNINDEX and closest to an order of magnitude for VN30–VN100, the
  pair with the highest mechanical overlap."
- **M-B** (§8 Limitation 1 self-contradicted within one sentence: "1D extends to 2025-12-12... no single
  frequency covers the full 2014–2025 window on its own," when 1D's own stated range in §3.1 is exactly
  2014-02-06 to 2025-12-12, i.e. 1D does cover it): corrected to "no frequency besides 1D covers the full
  2014–2025 window."

**MINOR fixed:**
- §4.6's minimum-variance robustness check (added in Iter 12/13) is directionally correct but uses the
  scale-varying $\rho_{DCCA}(s)$ from the `portfolio_risk_scales` table, not the regime-specific $\rho$
  behind the 2.84%/15.63% headline maxima it sits next to — added a clause making that basis difference
  explicit rather than implying it was checked against the same numbers.
- Intro contribution-list citation (2) cited only "(Sections 3.4 and 4.3)" for the weighted_real
  separation claim, but the actual quantitative comparison (0.977 vs. 0.884, Table 1b) is in Section 4.2
  — added "4.2" to the citation list.

**MINOR deferred (cosmetic):** "Table 1b" labeling convention (inserted between Tables 1 and 2 rather
than renumbered) — a formatting choice, not a factual defect; not changed this pass.

## Iter 13 (this pass) — fixes responding to genuinely-independent review round 5 (1 CRITICAL, 2 MAJOR, 1 MINOR)

Round 5 reviewer (fresh `general-purpose`, no context) re-verified all Iter 12 edits exactly (§4.4
spectrum-width correction, §3.5's 100% figure, the §4.1 duplicate-paragraph removal, the Intro
roadmap-sentence deletion, and every §4.2/4.3/6 numeric correction) and traced all ~35 cross-section
references, finding only one mismatch. Explicitly stated the paper's numerical grounding is
"exceptionally strong" after four rounds — the remaining defects were narrow.

**CRITICAL fixed:**
- **1** (§4.5 claimed "the three original index pairs... stay above 0.95 in every regime," but
  `regime_dcca_curves` shows VN30–VNINDEX and VN100–VNINDEX both fall below 0.95 in the low-volatility
  regime at every one of the four frequencies, VN30–VNINDEX min 0.905 at H1; only VN30–VN100 genuinely
  stays above 0.95 throughout): corrected to "stay mostly in the 0.90–0.99 range across regimes, a swing
  an order of magnitude smaller than weighted_real's," and softened the "proxy-level, not index-level,
  phenomenon" claim to "far weaker at the index level... though not entirely absent," since the
  qualitative point (index pairs move far less than weighted_real) holds even though the strict "above
  0.95" floor does not.

**MAJOR fixed:**
- **2** (§4.6 claimed minimum-variance weighting was confirmed to produce smaller errors "at the regime
  level," but the only committed minimum-variance table, `portfolio_risk_scales`, is indexed by scale
  using the full-sample correlation curve, not any regime-conditioned one — no committed regime-level
  minvar artifact exists): corrected "at the regime level" to "across scales," matching what is actually
  committed.
- **3** (§4.3's opening sentence claimed "the regression in Section 5 uses three covariates... the
  timescale grid, the volatility regime..., and the detrending order," but Section 5's actual regression,
  equation 3/Table 3, uses only $\ln(s)$ as its covariate; regime and detrending order enter through
  separate stratified re-estimations in Sections 4.5 and 6, not as regression terms in Section 5):
  rewrote to describe the three as separate robustness dimensions explored across Sections 4.5, 5, and 6,
  rather than as covariates inside Section 5's regression.

**MINOR fixed:** Introduction's slope-significance claim (line 19) held only under the reliable-scale
specification (Table 4), not the full-range specification (Table 3) that the surrounding prose
otherwise draws from — added "under the reliable-scale specification" to disambiguate.

**MINOR deferred (cosmetic, not blocking):** "feature" used as a vague noun twice (§4.2), "meaningful"
once (§5) — both on the mechanical gate's vague-word list but low-impact and domain-acceptable in
context; not re-litigated this pass.

## Iter 12 (this pass) — fixes responding to genuinely-independent review round 4 (2 CRITICAL, 4 MAJOR)

Round 4 reviewer (fresh `general-purpose`, no context) independently re-verified the Section 3.4/3.5
cross-references (all 7 correctly targeted, no findings), the regime-correlation headline numbers in
Abstract/§4.5 (exact match to `regime_dcca_curves`, including the precise per-frequency attribution of
each bound), and recomputed essentially every table in the paper from the DB/CSV directly — all
matched. Findings were narrower and more surgical than round 3's:

**CRITICAL fixed:**
- **C1** (§4.4 multifractal spectrum width for the three alternative proxies stated "0.164–0.227," but
  `residual_DEPRECATED` reaches 0.2522 at 1D, so the true combined range is 0.164–0.252): corrected the
  range and rewrote the interpretive sentence, which had claimed a clean separation from weighted_real's
  0.249–0.282 range; the corrected ranges actually overlap marginally (0.249–0.252), so the sentence now
  says "distinguishes the proxies on average" and "not cleanly separated" rather than implying a clean
  split.
- **C2** (§3.5 claimed weighted_real–VN30 is "significant across 96.7–100%" of the reliable-scale range,
  but this matches neither the reliable-range definition, which gives a uniform 100% at all four
  frequencies, nor the full-range definition, which tops out at 96.7%; the two definitions were
  conflated): corrected to "100% of that range as well," consistent with the reliable-range definition
  used one sentence earlier for the three original pairs.

**MAJOR fixed:**
- **M-A** (§4.1 contained a near-verbatim duplicate paragraph: the "18.5–21.7 times" gap and its
  short-term-noise interpretation were stated twice in back-to-back paragraphs, lines 154 and 156):
  deleted the redundant restatement, kept only the one-sentence bridge into Section 3's DCCA/MF-DCCA
  framing.
- **M-B** (M11 passive-voice sweep from Iter 11 was incomplete: 5 more genuine passives survived, one
  inside §3.5, which Iter 11 claimed to have swept clean): fixed all 5 — Intro roadmap sentence (deleted
  the "is organized as follows" boilerplate per the zero-exception rule), §2 ("is also confirmed by" →
  active), §3.5 ("is not driven by" → active), §4.1 ("tends to be skewed and... affected by" → active),
  §5 ("are less diluted or distorted by" → active).
- **M-C** (§4.6 stated the reported Markowitz errors are "the largest absolute error across both
  weighting schemes," i.e. 50/50 and minimum-variance, but the committed `portfolio_risk_regime_comparison`
  table backing the headline 2.84%/15.63% figures contains only the 50/50 scheme; a manual
  reproduction of the min-variance scheme confirmed it gives smaller errors and doesn't overturn the
  headline maxima, but the claim as written wasn't traceable to a committed artifact per S15): reworded
  to state the headline figures use the 50/50 allocation, and describe the min-variance check as a
  manual robustness confirmation rather than a second committed data source.
- **M-D** (cluster of four ±0.001–0.003 rounding slips): §4.3 proxy-correlation bounds corrected
  0.979→0.980 and 0.487→0.486; §6 scale-range robustness bound corrected 0.960→0.962; §4.2's
  error-band comparison reworded to avoid the ambiguous claim that a 0.006 spread is "an order of
  magnitude smaller" than a band whose lower bound (0.007) it's actually comparable to (now compares
  explicitly against the upper bound and notes the lower-bound comparison separately).

**Not flagged as violations (reviewer confirmed, no action needed):** en-dash usage (88 hits, all range/
pair notation, zero rhetorical use), "rather than"/antithesis density (18 hits, all real contrasts),
topic-first top-level chapter headings (matches standard IMRaD/thesis convention, treated as an accepted
register choice in earlier rounds).

## Iter 11 (this pass) — fixes responding to genuinely-independent review round 3 (2 CRITICAL, 2 MAJOR, 6 MINOR)

Round 3 reviewer (fresh `general-purpose`, no context, queried the DB directly via `sqlite3`) independently
re-verified 25+ numbers including the two highest-stakes figures (Markowitz 15.63%/2.84%, the
β/R²/amplification chain) — all reconciled exactly, confirming no fabrication survives. Findings were
concentrated exactly where predicted: residual cross-reference damage from the §3.4/§3.5 swap, one
data-scope imprecision in the regime-correlation headline, and unfixed passive voice.

**CRITICAL fixed:**
- **C1** (Introduction contribution-list line pointed at "Sections 3.5 and 4.3" for the weighted_real
  proxy construction, but construction lives in 3.4, not 3.5, a leftover from the 3.4/3.5 swap):
  corrected to "Sections 3.4 and 4.3."
- **C2** (Limitations §8 item 4 cited "Section 5" for weighted_real–VN30's per-frequency slope
  significance pattern, M30/H1 significant, 1D/H4 not, but Section 5 is M30-only and contains no such
  breakdown): added the actual per-frequency finding as a new sentence in Section 6 (the natural home,
  since §6 already reports cross-frequency slope-stability results), then repointed the Limitations
  citation to "(Section 6)."

**MAJOR fixed:**
- **M1** (regime-correlation headline "0.63–0.76 → 0.91–0.94" in Abstract and §4.5 matches only the 1D
  row; H1 reaches down to 0.560 and up to 0.807 in the low regime, M30 reaches up to 0.954 in the high
  regime — both outside the stated bounds, contradicting the sentence's own "depending on trading
  frequency" wording): rescoped both the Abstract and §4.5 to state the 0.63–0.76/0.91–0.94 figures
  explicitly "at the daily frequency" (consistent with how §4.6's Markowitz calculation already scopes
  its own 0.6333/0.8886 inputs to 1D), and added the true pooled cross-frequency bounds (low: 0.560–
  0.807 at H1; high: 0.905–0.954 at M30) so the "depending on trading frequency" claim is now accurate
  rather than approximated from one frequency alone.
- **M2** (10 genuine unfixed passive-voice instances against the mechanical gate's zero-tolerance M11
  rule): rewrote all 10 to active voice — Introduction (2, DCCA/MF-DCCA method descriptions), §1
  paragraph 2 (2, "portfolio risk is distributed" / "diversification benefits are preserved"), §3.2
  ("after local trends have been removed"), §3.3 (2, "is shaped by" / "is expected"), §3.5 ("This
  approach is designed to"), §4.5 ("is dominated by constituent overlap"), §6 ("are concentrated"), §8
  ("should not be generalized").

**MINOR addressed:** added "4.3" to the proxy-comparison cross-reference list in §3.4 (line ~105),
which previously cited only "Sections 5 and 6" while the actual inter-proxy correlation comparison
(0.979–0.997 vs. 0.277–0.487) lives in §4.3.

**MINOR deferred (immaterial / inherited from source, not introduced by translation):**
- Table 1 medians lack a committed-script provenance trail (numbers independently verified correct
  against the raw CSV, but `DOCUMENTATION.md` documents no median computation in the pipeline) — a
  pipeline-documentation gap, not a paper defect; out of scope for a text-only fix.
- weighted_real–VN30 upper bound stated as "0.926" vs. computed 0.9254 (rounds to 0.925) — this exact
  figure is already in `DOCUMENTATION.md` §4.1, inherited rather than introduced here; ~0.001,
  immaterial to any conclusion.
- En-dash usage (87 hits, all tight numeric ranges or index-pair names, zero rhetorical dashes) —
  reviewer judged this legitimate econometrics typography, not an M1 violation.
- Topic-first subsection headings (vs. `project_context.md`'s claim-first instruction) — pervasive,
  consistent with standard finance-journal convention, treated as an accepted departure in earlier
  rounds; not re-litigated here.
- "feature" used 3x as a plain noun — mild, domain-acceptable, optional tightening only.

## Iter 10 — fixes responding to round 2 (7 CRITICAL, 15 MAJOR, 21 MINOR) — summary retained for history

All 7 CRITICAL fixed: M30 date-range accuracy (C1), deleted a fabricated "7.4 candles/day" statistic
that contradicted §4.4's own persistence finding (C2), corrected a slope-significance overclaim in the
Introduction (C3), added the missing Podobnik test formula to §3.2 (C4), swapped §3.4/§3.5 content order
so weighted_real/ratio are defined before use and fixed all 5 then-known external cross-references (C5),
trimmed duplicated content out of §4.3 (C6), and fixed a backwards error-band comparison in §4.2 (C7).
Also fixed: DCCA acronym expansion, duplicate section title, 2 misattributed citations, a unit mismatch,
an orphan comparison, and the Markowitz equal-volatility inconsistency. Deferred at the time: M-2 through
M-8, M-14 (passive voice), M-15 (sentence-length compression), and 21 MINOR items — M-14 and the
cross-reference-adjacent items (M-4/M-5/M-6, which concerned exactly the swapped-section citations) are
now resolved via Iter 11 above; sentence-length compression (M-15) remains open.

**Next step:** launch a FOURTH genuinely independent reviewer (fresh `general-purpose`, no context, must
not read this ledger) to verify the Iter 11 fixes hold, specifically: the corrected 3.4/3.5
cross-references, the rescoped regime-correlation numbers (re-check the new pooled bounds arithmetic
against the DB independently), the new Section 6 sentence's placement and accuracy, and a fresh full
passive-voice sweep to confirm zero genuine hits remain. Also decide whether the still-open M-15
(sentence-length compression, mean 30.6 words vs ~21 target) and remaining MINOR items block a "ready
for submission" call, or are acceptable residual polish per S31's judgment call on closure.
