# Language round 1 of 2 (proofreading + stop-slop)

Date: 2026-10-10. Independent language editor, fresh context. Sources edited: `project_R/docx_build/r2_text.py`
(Sections 1, 2.7, 3–7, supplement) and `project_R/docx_build/r2_lit.py` (Sections 2.1–2.6, Table 1 note).
Rules applied: `proofreading` skill (six checks, report mode, then fixes applied by the editor), `stop-slop`,
`skill gộp/rules/01_master_editorial_philosophy.md`, `02_mechanical_and_anti_ai_gate.md`, ARS
`academic-paper/references/writing_quality_check.md`. The audit ledger was not read.

Edits were applied by a scripted exact-match replacement (each OLD string asserted to occur exactly once);
pre-edit copies of both sources and both rendered `.md` files are in the session scratchpad (`lang1_bak/`).
No `{...}` f-string expression, number, citation, cross-reference, equation, hypothesis rule or outcome word
was changed or moved; the reference list is untouched.

Detected conventions kept: American spelling (`-ize`, `analyzes`, `centered`, `toward`); no serial (Oxford) comma
(house style used throughout, so it was kept rather than half-converted); subscript convention `P_cap`, `ρ_AM`, `s_rel`.

## 1. Proofreading report (six checks)

| Check | Found | Fixed | Left (reason) |
|---|---|---|---|
| 1 Structure (abstract, intro, related work, hypotheses, conclusion) | 6 | 2 | 4 |
| 2 Math notation | 7 | 3 | 4 |
| 3 Statistical relevance | 0 | 0 | 0 |
| 4 Figures and tables | 3 | 0 | 3 |
| 5 Grammar and style | 71 edits (plus 14 long-sentence units left) | 71 | 14 long units with equations/date lists; serial-comma house style kept |
| 6 Abbreviations | 9 | 7 | 2 |

### Check 1: Paper structure
- [WARN] Abstract is 213 words (skill default 150). Left: APFM limit is 250; `checks_v3.py` passes.
- [WARN] Abstract states the gap only implicitly ("We carry ... over to DCCA"). Left: adding a gap sentence would add a claim and words.
- [ERROR, HARD] The word "contribut..." does not appear in the introduction. Left: the contribution is explicit ("We build that version. Lemma 1 shows ..."); inserting the keyword would be cosmetic and the brief forbids adding claims. Flag for authors.
- [WARN] Roadmap was one 54-word sentence. Fixed (split; "present the data, methods and results").
- [INFO] "Three findings stand out." formulaic opener. Fixed ("We report three main findings.").
- [WARN, factual] Section 3.1 opens "Five features of the HOSE matter here", but the paragraph lists six (price band, settlement, auction schedule, short-selling rules, derivatives/ETF, foreign ownership with reclassification). Left: number words are claims outside a language round. **Authors should change "Five" to "Six" or merge two items.**
- Hypotheses are stated explicitly with decision rules before results (1.7 satisfied); the conclusion carries quantitative results (1.8 satisfied); related work is thematic with a gap statement (1.6 satisfied).

### Check 2: Math symbols and notation
Detected notation convention: plain italic scalars throughout (no vectors or matrices in prose); Convention A/B not applicable.
- [ERROR] `P_cap` used in the H1 rule (Section 2.7) before its definition in Eq. (6). Fixed: "P_cap is the overlap-purged mid-cap series" added inside the rule's parenthesis.
- [ERROR] Display Eq. (10) followed "*Corollary 2 (sensitivity).*" with no lead-in. Fixed: "The sensitivity of ρ_AB to ρ_AM is".
- [WARN] "in proportion to the gap" (Section 4.3) reused "gap", which is reserved for the overlap gap. Fixed: "in proportion to the weight error w_t − w".
- [WARN] `B` denotes both VN100 returns (B_t) and the bootstrap replication count (B = 499, Section 4.4). Left: renaming changes notation and equations.
- [WARN] `β` denotes both the scaling slope (Eq. 13) and the factor loading (Section 4.6); `α` denotes both intercepts and the singularity argument f(α) in Fig. S1. Left: same reason.
- [INFO] Table S13 caption writes "(Eq. 14)" where the text uses "Eq. (14)". Left: the gate freezes cross-reference tokens.
- [INFO] `F_A(s)`, `F_M(s)` in Lemma 1 rely on the F_X(s) definition after Eq. (4); acceptable.

### Check 3: Statistical relevance
No issues. Every comparative claim carries a 95% interval, a p-value with its family/adjustment, or is labelled descriptive (Cohen's q, multifractal ranges). Replication counts are stated per statistic.

### Check 4: Figures and tables
- [WARN] Fig. 4 and Box 1 are first cited in the Introduction, before Fig. 1–3 and Table 1, so figure numbering does not follow first citation. Left: renumbering is outside a language round and would change cross-reference tokens.
- [INFO] Captions have no closing period. Left: Springer caption style.
- [INFO] Figures are PNG (raster). Left: production issue, not language.

### Check 5: Grammar and style
- Variant: American. One deviation fixed: "re-centred" to "re-centered" (Section 4.4).
- Em dashes in prose: 0 (the only "—" is inside the Pearson (1897) reference title, left verbatim).
- Long sentences over ~35 words: 41 sentence units flagged by script; 27 split (the 88 edits also include 8 other sentence splits), the remainder are equation-bearing, list-of-dates, or table-note sentences where splitting would move numbers or symbols (left).
- Passive voice where "we" works: 12 converted (Sections 2.7, 3.2, 4.1, 4.2, 4.4, 4.5, 4.6, 4.7, 4.8, 6.2, supplement). Remaining passives describe data or system properties ("The indices are computed in real time"), which the skill allows.
- Commas after introductory phrases / between independent clauses: 7 fixed.
- Ambiguity and vague terms: "they" (intro), "which" (DCCA literature), "everywhere" (x2), "Here", "the question", "the interval", appositive in Section 4.6, parenthetical p-value range in Section 5.5: all fixed.
- Repeated phrase "continuous trading" (Section 3.1): fixed ("a second continuous session").
- Dangling participles ("recomputing every curve", "reported descriptively"): 2 fixed.
- Prohibited vocabulary (very/quite/utilize/paramount/foster, etc.): 0 found. "rather than" (4) is a contrast, kept. "Note that": 0.
- [INFO] Serial comma: the manuscript consistently omits the Oxford comma. The skill prefers it, but converting about 100 lists in one round would risk inconsistency; kept as house style. Clause lists were given a comma where needed for parsing.
- [INFO] Possessives on non-persons ("child’s weight", "pair’s own", "vendor’s terms"): kept; idiomatic and unambiguous.
- Terminology now consistent: "overlap-purged coefficient", "zero-correlation benchmark", "like-for-like gap" (one inverted "like-for-like daily gap" fixed), "three-pair gap", "decision rule".

### Check 6: Abbreviations
- [ERROR] EWMA used undefined (H4 rule). Fixed: "exponentially weighted moving average (EWMA)".
- [ERROR] QLIKE used undefined. Fixed: "quasi-likelihood (QLIKE) loss".
- [ERROR] DMCA never expanded (Table 1, Section 5.7). Fixed: Table 1 note and first body use in Section 4.2 ("detrending moving-average cross-correlation (DMCA) coefficient").
- [ERROR] ETF (Section 6.2) undefined. Fixed: "holder of the VNMIDCAP exchange-traded fund".
- [ERROR] BH (Section 5.4) and FR (Section 5.5 prose) undefined. Fixed: spelled out "Benjamini–Hochberg" and "Forbes–Rigobon"; FR now defined in the Table 7 note (used in Tables 7 and 9).
- [WARN] ρDCCA in Table 1 undefined. Fixed in Table 1 note.
- [ERROR, left] Frequency labels 1D, M30, H1, H4 appear in Section 3.2 before Table 3 defines them. Left: inserting "(M30)" or "(1D)" adds numeric tokens that the number gate rejects. Suggest authors add "Daily (1D), 30-minute (M30), 1-hour (H1) and 4-hour (H4)" in Section 3.2 in a numbers-unlocked round.
- [INFO, left] GARCH, OLS-QR, TOST (defined), CI/SE in tables are standard or defined in notes.
- Abstract: DCCA introduced once and used; self-contained.

## 2. Stop-slop findings

| Pattern | Found | Fixed | Left |
|---|---|---|---|
| Formulaic opener ("Three findings stand out.") | 1 | 1 | 0 |
| Wh- sentence openers ("What is missing is...", "How much of...") | 2 | 2 | 0 |
| Vague declarative ("The nested results have one source.") | 1 | 1 | 0 |
| Inanimate agent ("high-volatility days bring...") | 1 | 1 | 0 |
| Pull-quote paragraph closer ("The error that matters is reading a nested correlation as diversification.") | 1 | 1 (made concrete: "For users of index-level data, ... as evidence of diversification") | 0 |
| Inverted clause ("whether one would be viable we do not study") | 1 | 1 | 0 |
| Throat-clearing openers (Moreover/Furthermore/Notably/Indeed/It is worth noting) | 0 | – | – |
| Banned AI vocabulary (delve, underscore, pivotal, crucial, leverage, robust as filler, etc.) | 0 | – | – ("robust" appears only as the statistical term) |
| Em dashes | 0 | – | – |
| Adverbs: "mechanically" (Section 2.5), "only", "barely", "partly" | kept | – | technical meaning or hedge that the brief requires us to keep |
| "X, not Y" contrasts ("not of continuous trading", "Membership, not overlap") | 2 | 0 | kept: Keep-vs-Cut test, both carry information |
| Short punchy summary lines ("Overlap thus inflates co-movement that is already strong.", "The factor model explains why.") | 2 | 0 | kept: they are topic/summary sentences with content, and the rhythm now varies after splits |

Scores after edits (stop-slop rubric, 1–10): Directness 8, Rhythm 8, Trust 8, Authenticity 8, Density 8: 40/50 (threshold 35).

## 3. Edit table
| # | File | Location | Before | After | Category |
|---|---|---|---|---|---|
| 1 | r2_text.py | Abstract | comes from the opening and closing auction bars, evidence of crisis contagion depends on the test used, and | comes from the opening and closing auction bars. Evidence of crisis contagion depends on the test used, and | long sentence split |
| 2 | r2_text.py | 1 Intro p1 | diversifies another (Markowitz 1952). In nested index systems they have a problem unrelated to estimation error:  | diversifies another (Markowitz 1952). In nested index systems, these correlations have a problem unrelated to estimation error:  | pronoun ambiguity / comma |
| 3 | r2_text.py | 1 Intro p2 | The arithmetic is old (Pearson 1897; Cureton 1966), but there is no version for the detrended, scale-dependent coefficients of the detrended cross-correlation analysis (DCCA) literature, which studies only pairs without shared constituents (Section 2). | The arithmetic is old (Pearson 1897; Cureton 1966), but no version exists for the detrended, scale-dependent coefficients of the detrended cross-correlation analysis (DCCA) literature. That literature studies only pairs without shared constituents (Section 2). | long sentence split; ambiguous "which" |
| 4 | r2_text.py | 1 Intro p3 | (2014–2025), with a block bootstrap that also draws the index weight, and use the purged series to test hypotheses  | (2014–2025), with a block bootstrap that also draws the index weight. We then use the purged series to test hypotheses  | long sentence split |
| 5 | r2_text.py | 1 Intro p4 | f"Three findings stand out. The VN30–VN100 | f"We report three main findings. The VN30–VN100 | formulaic opener (stop-slop) |
| 6 | r2_text.py | 1 Intro p4 | Section 2 reviews the literature and states the hypotheses, Sections 3–5 present data, methods and results, Section 6 discusses them and Section 7 concludes; further checks are in Online Resource 2. | Section 2 reviews the literature and states the hypotheses. Sections 3–5 present the data, methods and results, Section 6 discusses them and Section 7 concludes. Further checks are in Online Resource 2. | long sentence split; article |
| 7 | r2_lit.py | 2.1 | portfolios from stocks outside the index (Barberis et al. 2005). What is missing is a return-based counterpart for users who observe only index levels. | portfolios from stocks outside the index (Barberis et al. 2005). Users who observe only index levels lack a return-based counterpart. | Wh- opener (stop-slop) |
| 8 | r2_lit.py | 2.2 | series (Podobnik and Stanley 2008); Zebende (2011) normalized it | series (Podobnik and Stanley 2008). Zebende (2011) normalized it | long sentence split |
| 9 | r2_lit.py | 2.2 | al. 2025). All of it treats the coefficient as a measure of economic dependence between disjoint assets; none analyzes nested pairs, | al. 2025). This work treats the coefficient as a measure of economic dependence between disjoint assets. None of it analyzes nested pairs, | long sentence split; vague "All of it" |
| 10 | r2_lit.py | 2.3 | where indices do not overlap; our concern is the arithmetic overlap, | where indices do not overlap. Our concern is the arithmetic overlap, | long sentence split |
| 11 | r2_lit.py | 2.4 | small-firm liquidity fell after a market surveillance system was introduced (Chen et al. 2021) and price adjustment is delayed under retail-heavy trading (Tran and Tran 2025), while herding in stress (Nguyen et al. 2023), sector connectedness above 60%, near 90% during COVID-19 (Bui et al. 2022) | small-firm liquidity fell after a market surveillance system was introduced (Chen et al. 2021), and price adjustment is delayed under retail-heavy trading (Tran and Tran 2025). Herding in stress (Nguyen et al. 2023), sector connectedness above 60%, rising to near 90% during COVID-19 (Bui et al. 2022) | long sentence split (76 words); ambiguous list item |
| 12 | r2_lit.py | 2.5 | restricts the variance of idiosyncratic shocks; Corsetti et al. (2005) propose | restricts the variance of idiosyncratic shocks. Corsetti et al. (2005) propose | long sentence split |
| 13 | r2_lit.py | 2.6 | We searched Google Scholar and publisher databases for 2021–2026, plus the classical sources these works cite, combining “detrended cross-correlation” | We searched Google Scholar and publisher databases for 2021–2026, plus the classical sources these works cite. Search strings combined “detrended cross-correlation” | long sentence split (76 words) |
| 14 | r2_lit.py | Table 1 note | heteroskedasticity or common shocks. Source: | heteroskedasticity or common shocks; DMCA: detrending moving-average cross-correlation analysis; ρDCCA: DCCA coefficient. Source: | abbreviation defined at first use |
| 15 | r2_text.py | 2.7 H1 | Rule: the lower 95% bound of the like-for-like gap (VN30–VN100 minus P_cap–VN30) exceeds 0.05, | Rule: the lower 95% bound of the like-for-like gap (VN30–VN100 minus P_cap–VN30; P_cap is the overlap-purged mid-cap series) exceeds 0.05, | symbol used before definition |
| 16 | r2_text.py | 2.7 H2 | Holm-adjusted studentized p-value below 0.05; we also report robustness | Holm-adjusted studentized p-value below 0.05. We also report robustness | long sentence split |
| 17 | r2_text.py | 2.7 H4 | *H4 (value of regime conditioning).* Rule: an EWMA or real-time regime correlation has a lower QLIKE loss than the  | *H4 (value of regime conditioning).* Rule: an exponentially weighted moving average (EWMA) or real-time regime correlation has a lower quasi-likelihood (QLIKE) loss than the  | abbreviations defined at first use |
| 18 | r2_text.py | 2.7 H4 | These rules, the eight-test family and the factor-loading test were fixed at revision, after the first-round results were known; we also report the  | We fixed these rules, the eight-test family and the factor-loading test at revision, after the first-round results were known. We also report the  | active voice; sentence split |
| 19 | r2_text.py | 3.1 | a break to 13:00, continuous trading and a closing call auction | a break to 13:00, a second continuous session and a closing call auction | repeated phrase |
| 20 | r2_text.py | 3.1 | Short selling is restricted: Circular 120/2020/TT-BTC (Ministry of Finance of Vietnam 2020) provides a framework for covered short sales that to our knowledge had not been put into operation, naked short selling is prohibited, and the implementing Decree  | Short selling is restricted. Circular 120/2020/TT-BTC (Ministry of Finance of Vietnam 2020) provides a framework for covered short sales that, to our knowledge, had not been put into operation, and naked short selling is prohibited. The implementing Decree  | long sentence split (52 words); comma splice; parenthetical commas |
| 21 | r2_text.py | 3.1 | futures trade on the Hanoi Stock Exchange but there is no mid-cap future; a VNMIDCAP exchange-traded fund  | futures trade on the Hanoi Stock Exchange, but no mid-cap future exists. A VNMIDCAP exchange-traded fund  | long sentence split; comma before coordinating clause |
| 22 | r2_text.py | 3.1 | concentrate foreign flows in large caps with room under their limits, and Vietnam is to be reclassified to Secondary Emerging status from 21 September 2026 (FTSE Russell 2025), after our sample. | concentrate foreign flows in large caps with room under their limits. Vietnam is to be reclassified to Secondary Emerging status from 21 September 2026 (FTSE Russell 2025), after the end of our sample. | long sentence split (58 words) |
| 23 | r2_text.py | 3.2 | and the two H4 bars cover the two sessions, so the first bar holds the overnight return | and the two H4 bars cover the two sessions, so at every frequency the first bar of the day holds the overnight return | precision |
| 24 | r2_text.py | 3.2 | The vendor has no full VNMIDCAP history, so the mid-cap segment is recovered from VN30 and VN100 (Section 4.2). Series are merged by exact timestamp joins without filling, and we did not compare them with HOSE closing levels date by date (the replication package records an input checksum).  | The vendor has no full VNMIDCAP history, so we recover the mid-cap segment from VN30 and VN100 (Section 4.2). We merge the series by exact timestamp joins without filling gaps. We did not compare them with HOSE closing levels date by date; the replication package records an input checksum.  | active voice; sentence split |
| 25 | r2_text.py | 3.2 | The indices are computed in real time, so reconstitutions and delistings are embedded and there is no survivorship bias. | The indices are computed in real time, so they embed reconstitutions and delistings and carry no survivorship bias. | active voice |
| 26 | r2_text.py | 3.2 | {f(100 * F(c[2]['share_high_vol_days']), 0)}%), {nint(SC['n_crisis_days'][0])} days in all, against calm years | {f(100 * F(c[2]['share_high_vol_days']), 0)}%). The three episodes total {nint(SC['n_crisis_days'][0])} days, against calm years | long sentence split (71 words) |
| 27 | r2_text.py | 4.1 | "Each profile is split into N_s = ⌊N/s⌋ boxes of length s from each end of the series (2N_s boxes). In box ν a polynomial of order m (m = 1 unless stated) is fitted by ordinary least squares (OLS), and the residuals ε_X and ε_Y give the detrended covariance" | "We split each profile into N_s = ⌊N/s⌋ boxes of length s, starting from each end of the series (2N_s boxes). In each box ν we fit a polynomial of order m (m = 1 unless stated otherwise) by ordinary least squares (OLS); the residuals ε_X and ε_Y give the detrended covariance" | active voice; long sentence |
| 28 | r2_text.py | 4.2 | (free-float capitalizations of VND 1,316,288 billion and 1,928,303 billion) | (free-float capitalizations of VND 1,316,288 billion and 1,928,303 billion, respectively) | ambiguity |
| 29 | r2_text.py | 4.2 | replicating it needs about 315% long VN100 and 215% short VN30. | replicating it requires about 315% long VN100 and 215% short VN30. | word choice |
| 30 | r2_text.py | 4.2 | for the detrending moving-average coefficient (Kristoufek 2014) | for the detrending moving-average cross-correlation (DMCA) coefficient (Kristoufek 2014) | abbreviation defined at first body use |
| 31 | r2_text.py | 4.2 | Five corollaries follow, at a fixed scale that we suppress." | Five corollaries follow; we fix the scale and suppress it in the notation." | ambiguous phrasing |
| 32 | r2_text.py | 4.2 | "for κ ≥ 1 no positive bound exists. *Corollary 2 (sensitivity).*" | "for κ ≥ 1 no positive bound exists. *Corollary 2 (sensitivity).* The sensitivity of ρ_AB to ρ_AM is" | equation integration (display equation had no lead-in) |
| 33 | r2_text.py | 4.2 | All quantities are computed scale by scale and averaged over the reliable range " | We compute all quantities scale by scale and average them over the reliable range " | active voice |
| 34 | r2_text.py | 4.3 | "so large-cap returns leak into P_cap in proportion to the gap, and P_cap and VN30 are disjoint only at the exact weight. With a single factsheet snapshot we cannot rebuild the weight path, so each bootstrap replicate draws w from U(0.60, 0.75), an interval around the factsheet weight with room for drift either way, and recomputes P_cap and every " | "so large-cap returns leak into P_cap in proportion to the weight error w_t − w, and P_cap and VN30 are disjoint only at the exact weight. With a single factsheet snapshot we cannot rebuild the weight path, so each bootstrap replicate draws w from U(0.60, 0.75), an interval around the factsheet weight that allows drift in either direction, and recomputes P_cap and every " | terminology clash ("gap" reserved for the overlap gap) |
| 35 | r2_text.py | 4.4 | first exceeds 0.05; the grid and tolerance were fixed in advance; a GARCH(1,1)-t(5) calibration (300 simulations) checks heavy tails." | first exceeds 0.05. We fixed the grid and tolerance in advance, and a GARCH(1,1)-t(5) calibration (300 simulations) checks heavy tails." | double semicolon; active voice |
| 36 | r2_text.py | 4.4 | so all inference resamples the data with the stationary block bootstrap (Politis and Romano 1994), with mean blocks of about 20 trading days, recomputing every curve and statistic per replicate. | so all inference resamples the data with the stationary block bootstrap (Politis and Romano 1994) with mean blocks of about 20 trading days and recomputes every curve and statistic in each replicate. | dangling participle |
| 37 | r2_text.py | 4.4 | hedge-effectiveness and tail-dependence statistics, 399 for the like-for-like gap under weight uncertainty, 199 for " | hedge-effectiveness and tail-dependence statistics, and 399 for the like-for-like gap under weight uncertainty. We use 199 for " | long sentence split (79 words) |
| 38 | r2_text.py | 4.4 | cannot fall below 0.004 with B = 499 (reported as p < 0.005), and with 19 tests the smallest " | cannot fall below 0.004 with B = 499 (reported as p < 0.005). With 19 tests, the smallest " | long sentence split |
| 39 | r2_text.py | 4.4 | use the re-centred bootstrap distribution | use the re-centered bootstrap distribution | spelling variant (British form in American text) |
| 40 | r2_text.py | 4.4 | Equivalence of the VN30–VN100 slope to zero is tested by two one-sided tests (TOST; Schuirmann 1987) with a margin of 0.001 per unit of ln s; over the 4.5 units of the M30 reliable range such a slope | We test equivalence of the VN30–VN100 slope to zero with two one-sided tests (TOST; Schuirmann 1987) and a margin of 0.001 per unit of ln s. Over the 4.5 units of the M30 reliable range, such a slope | active voice; sentence split |
| 41 | r2_text.py | 4.5 | ('p1a', "Horizon dependence is the slope β of") | ('p1a', "We measure horizon dependence by the slope β of") | active voice |
| 42 | r2_text.py | 4.6 | We therefore also test, regime by regime, for changes in the loading β and the residual variance, the contagion concept of Corsetti et al. (2005) and the structural parameter of Rigobon (2003). | We therefore also test, regime by regime, for changes in the residual variance and in the loading β; a change in β is contagion in the sense of Corsetti et al. (2005), and β is the structural parameter of Rigobon (2003). | ambiguous appositive |
| 43 | r2_text.py | 4.6 | Nested pairs are not tested, because the parent contains the conditioning index. | We do not test nested pairs, because the parent contains the conditioning index. | active voice |
| 44 | r2_text.py | 4.7 | re-estimating ρ_st, and \|RE\| is compared with the bootstrap relative standard error | re-estimating ρ_st, and we compare \|RE\| with the bootstrap relative standard error | active voice |
| 45 | r2_text.py | 4.8 | Seeds are fixed in each script (20260924 to 20261014; | Each script fixes its seeds (20260924 to 20261014; | active voice |
| 46 | r2_text.py | 5.1 | "Jarque–Bera test rejects normality everywhere; neither DCCA nor the block bootstrap requires Gaussian returns." | "Jarque–Bera test rejects normality for every series. Neither DCCA nor the block bootstrap requires Gaussian returns." | vague term; sentence split |
| 47 | r2_text.py | 5.1 | Averages below use the Gaussian thresholds; over the heavy-tailed ranges the nested averages become | Averages below use the Gaussian thresholds. Over the heavy-tailed ranges, the nested averages become | sentence split; comma |
| 48 | r2_text.py | 5.2 | at every frequency in both samples, P_cap–VN30 {rng(pcap_all)}.  | at every frequency in both samples, and P_cap–VN30 averages {rng(pcap_all)}.  | elliptical clause |
| 49 | r2_text.py | 5.2 | with Cohen’s q (Cohen 1988) of {rng(qv, 2)}, reported descriptively because both coefficients come from the same sample. | with Cohen’s q (Cohen 1988) of {rng(qv, 2)}. We report q descriptively because both coefficients come from the same sample. | long sentence split; dangling participle |
| 50 | r2_text.py | 5.2 | over w = 0.60–0.75 the like-for-like daily gap is | over w = 0.60–0.75 the daily like-for-like gap is | consistent term ("like-for-like gap") |
| 51 | r2_text.py | 5.2 | "0.05, so H1 holds under weight uncertainty, although the size of the gap is known only to within a factor of about two." | "0.05, so H1 holds under weight uncertainty. The size of the gap, however, is known only to within a factor of about two." | long sentence split |
| 52 | r2_text.py | 5.3 | by about {f(sum(inv_sens) / 4 * 0.01, 2)}, and with weight uncertainty the interval is " | by about {f(sum(inv_sens) / 4 * 0.01, 2)}. With weight uncertainty, the sensitivity interval is " | sentence split; vague referent |
| 53 | r2_text.py | 5.3 | VN100 contributes about half as much detrended variation as VN30, the benchmark is {rng(bench_v, 3)} and the lower bound of Eq. (9) is {rng(tmin_v, 3)}: no purged coefficient | VN100 contributes about half as much detrended variation as VN30, which puts the benchmark at {rng(bench_v, 3)} and the lower bound of Eq. (9) at {rng(tmin_v, 3)}. No purged coefficient | long sentence split |
| 54 | r2_text.py | 5.3 | f"How much of the observed {rng(nest_v, 3)} is due to overlap depends on the question. | f"The part of the observed {rng(nest_v, 3)} attributable to overlap depends on the attribution convention. | Wh- opener; vague "the question" |
| 55 | r2_text.py | 5.3 | coefficient near 0.9; the Shapley split attributes | coefficient near 0.9. The Shapley split attributes | sentence split |
| 56 | r2_text.py | 5.3 | Across reliable scales and frequencies κ lies in  | Across reliable scales and frequencies, κ lies in  | comma after introductory phrase |
| 57 | r2_text.py | 5.3 | percentile interval just excludes zero; the slope, about −0.002 per unit of ln s, is negligible. On full-sample Pearson moments the benchmark is  | percentile interval just excludes zero. The slope, about −0.002 per unit of ln s, is negligible. On full-sample Pearson moments, the benchmark is  | sentence split; comma |
| 58 | r2_text.py | 5.3 | Here the multiscale layer is a check of scale invariance, and Box 1 suffices in practice; the DCCA version matters where " | In these data, the multiscale layer serves as a check of scale invariance, and Box 1 suffices in practice. The DCCA version matters where " | vague "Here"; sentence split |
| 59 | r2_text.py | 5.4 | range; none is significant at 1D or H4, so H2 is | range. None is significant at 1D or H4, so H2 is | sentence split |
| 60 | r2_text.py | 5.4 | none survives (smallest BH-adjusted p = | none survives (smallest Benjamini–Hochberg-adjusted p = | undefined abbreviation (BH) |
| 61 | r2_text.py | 5.4 | and inconclusive elsewhere; the P_cap–VN30 slope is insignificant everywhere." | and the test is inconclusive elsewhere. The P_cap–VN30 slope is not significant at any frequency." | sentence split; vague "everywhere" |
| 62 | r2_text.py | 5.4 | auction, where intraday volatility peaks (Andersen and Bollerslev 1997): it is {f(100 * F(FB['M30']['share_of_bars_dropped']), 0)}% of M30 bars but carries {f(100 * F(FB['M30']['share_of_VN30_sq_return_in_first_bar']), 0)}% of squared VN30 returns, and the last bar holds " | auction, where intraday volatility peaks (Andersen and Bollerslev 1997). It accounts for {f(100 * F(FB['M30']['share_of_bars_dropped']), 0)}% of M30 bars but carries {f(100 * F(FB['M30']['share_of_VN30_sq_return_in_first_bar']), 0)}% of squared VN30 returns. The last bar holds " | long sentence split |
| 63 | r2_text.py | 5.4 | {pfmt(ts('M30', 'drop_first', 'VN30-VNINDEX')['p_studentized'])}); without both auction bars the M30 slopes are  | {pfmt(ts('M30', 'drop_first', 'VN30-VNINDEX')['p_studentized'])}). Without both auction bars, the M30 slopes are  | sentence split |
| 64 | r2_text.py | 5.4 | {f(ts('M30', 'drop_first_last', 'VN100-VNINDEX')['estimate'], 4)}. Within the same replicates the broad-market slopes  | {f(ts('M30', 'drop_first_last', 'VN100-VNINDEX')['estimate'], 4)}. Within the same replicates, the broad-market slopes  | comma after introductory phrase |
| 65 | r2_text.py | 5.4 | "vanish without the auction bars, while the overlap gap does not change ({f(FB['M30']['gap'])} | "vanish without the auction bars. The overlap gap does not change ({f(FB['M30']['gap'])} | long sentence split (55 words) |
| 66 | r2_text.py | 5.4 | at M30 without the opening bar) and the slope intervals are stable  | at M30 without the opening bar), and the slope intervals are stable  | comma between clauses |
| 67 | r2_text.py | 5.4 | "continuous trading; it is consistent with the Epps (1979) mechanism | "continuous trading. It is consistent with the Epps (1979) mechanism | sentence split |
| 68 | r2_text.py | 5.5 | f"The raw correlation rises in every definition, | f"The raw correlation rises under every regime definition, | preposition; precision |
| 69 | r2_text.py | 5.5 | under VN30 quartiles, but the adjusted crisis correlation never " | under VN30 quartiles. The adjusted crisis correlation, however, never " | long sentence split (51 words) |
| 70 | r2_text.py | 5.5 | {f(max(F(frA['p_one_sided']), F(frB['p_one_sided']), F(fr30['p_one_sided'])), 3)}; above {f(min(frw_p) - 0.005, 2)} across weights, Table S10) | {f(max(F(frA['p_one_sided']), F(frB['p_one_sided']), F(fr30['p_one_sided'])), 3)}, and above {f(min(frw_p) - 0.005, 2)} across weights; Table S10) | ambiguous parenthetical |
| 71 | r2_text.py | 5.5 | changes neither result (FR p =  | changes neither result (Forbes–Rigobon p =  | undefined abbreviation (FR) in prose |
| 72 | r2_text.py | 5.5 | Under its rule H3 is {H3_out.lower()}: high-VN30-volatility days bring both a stronger response of mid caps to large caps and more mid-cap-specific risk. | Under its decision rule, H3 is {H3_out.lower()}: on high-VN30-volatility days, mid caps respond more strongly to large caps and also carry more mid-cap-specific risk. | inanimate agent (stop-slop); comma; term "decision rule" |
| 73 | r2_text.py | Table 7 note | p (FR): one-sided bootstrap p-value for H0 | p (FR): one-sided Forbes–Rigobon bootstrap p-value for H0 | abbreviation (FR) defined |
| 74 | r2_text.py | 5.6 | "turbulent regimes, the sign pattern any pooled correlation produces; for nested pairs the misstatement is at most " | "turbulent regimes. Any pooled correlation produces this sign pattern. For nested pairs, the misstatement is at most " | long sentence split (56 words) |
| 75 | r2_text.py | 5.6 | Against sampling error the magnitudes are small: | Relative to sampling error, the magnitudes are small: | preposition; comma |
| 76 | r2_text.py | 5.7 | None of the further checks changes the conclusions. DMCA (Kristoufek 2014), which satisfies the same identity and so checks the detrending only, gives a purged coefficient | None of the further checks changes the conclusions. DMCA (Kristoufek 2014) satisfies the same identity, so it checks only the detrending; it gives a purged coefficient | nested relative clause; "only" placement |
| 77 | r2_text.py | 6.1 | ('p1a', "The nested results have one source. A child’s | ('p1a', "One mechanism drives the nested results. A child’s | vague declarative (stop-slop) |
| 78 | r2_text.py | 6.1 | "how mid caps move with large caps, and changes in the purged coefficient reach it damped by a factor of about ten." | "how mid caps move with large caps. Changes in the purged coefficient reach it damped by a factor of about ten." | long sentence split |
| 79 | r2_text.py | 6.1 | in line with Lo and MacKinlay (1990) and Hou (2007); intraday the lead is symmetric (Table S9). | in line with Lo and MacKinlay (1990) and Hou (2007); at intraday frequencies the lead is symmetric (Table S9). | precision |
| 80 | r2_text.py | 6.2 | ('p1a', "Nested index correlations used to judge diversification between tiers should first be decomposed. Box 1 does this from published series and the index weight; its key outputs | ('p1a', "Users who judge diversification between tiers from nested index correlations should first decompose them. Box 1 does this from published series and the index weight. Its key outputs | active voice; sentence split |
| 81 | r2_text.py | 6.2 | A VNMIDCAP ETF holder hedging with VN30 futures keeps about a fifth of the variance on average and about half in calm markets, the basis risk a mid-cap derivative would remove; whether one would be viable we do not study. | A holder of the VNMIDCAP exchange-traded fund who hedges with VN30 futures keeps about a fifth of the variance on average and about half in calm markets. A mid-cap derivative would remove this basis risk; we do not study whether such a contract would be viable. | undefined abbreviation (ETF); inverted clause |
| 82 | r2_text.py | 6.2 | The error that matters is reading a nested correlation as diversification." | For users of index-level data, the error that matters is reading a nested correlation as evidence of diversification." | pull-quote closer (stop-slop); precision |
| 83 | r2_text.py | 6.3 | With partial overlap the shared constituents form a third component and Eq. (7) does not apply directly. | With partial overlap, the shared constituents form a third component, and Eq. (7) does not apply directly. | commas |
| 84 | r2_text.py | 6.3 | VNINDEX uses full and VN100 free-float capitalization, so VN100 is not a fixed-weight component of VNINDEX, and the mismatch term of Eq. (12) cannot be bounded without constituent data, so the three-pair gap is descriptive for these pairs." | VNINDEX uses full capitalization and VN100 free-float capitalization, so VN100 is not a fixed-weight component of VNINDEX. The mismatch term of Eq. (12) cannot be bounded without constituent data, and the three-pair gap is therefore descriptive for these pairs." | long sentence split; repeated "so" |
| 85 | r2_text.py | 7 | attribution, all computable from index-level inputs. On the HOSE the VN30–VN100 | attribution, all computable from index-level inputs. On the HOSE, the VN30–VN100 | comma after introductory phrase |
| 86 | r2_text.py | Supplement MF | and the nested pairs in {sum( | and the nested-pair ranges do so in {sum( | elliptical clause |
| 87 | r2_text.py | Supplement MF | (Oświęcimka et al. 2014), these results are descriptive. | (Oświęcimka et al. 2014), we treat these results as descriptive. | active voice |
| 88 | r2_text.py | 4.4 | Table S6, 999 for the factor-model, lead–lag and materiality statistics and for the Forbes–Rigobon tests under VN30 quartiles, across weights and with 2021 added, and 1,999 for the remaining Forbes–Rigobon and relative-error statistics. | Table S6, and 999 for the factor-model, lead–lag and materiality statistics and for the Forbes–Rigobon tests under VN30 quartiles, across weights and with 2021 added. The remaining Forbes–Rigobon and relative-error statistics use 1,999 replications. | long sentence split (79 words) |

## 4. Word count
- `checks_v3.py`: abstract 213 (unchanged), main text excluding tables **6,898** (before: 6,790), supplement 3,195 (before: 3,191).
- Plain count of rendered manuscript prose before References (headings, captions and back matter included, tables and display equations excluded): 7,274 (before: 7,168).
- Main text stays inside the 6,400–7,000 window. The +108 words come from defined abbreviations, restored articles and subjects ("we fit", "We fixed"), and the equation lead-in.

## 5. Build, checks and gate output
```
$ python3 build_r2.py
built .../r2/supplementary_material.docx
built .../r2/manuscript_anonymized.docx
built .../r2/manuscript_with_authors.docx

$ python3 checks_v3.py
words: abstract 213 | main text excl. tables 6898 | supplement 3195
PASS abstract <= 250 words
... (all PASS)
FAILED: 0

$ python3 numgate.py compare <scratchpad>/gate_pre_lang1
GATE PASS
```
Gate history: the first pass failed on six token-form changes (a trailing "2." after "Online Resource 2", "0)" to "0,",
"0," to "0.", "5" to "5." after "LQ45", plus two tokens added by "for VN30 ... for VN100"). All six were restored to the
original token form (wording reverted or rephrased: "respectively", "which puts the benchmark at", semicolon kept after
"LQ45", "Further checks are in Online Resource 2."), after which the gate passed. `build_r2_package.py` was not run; nothing was committed.

## 6. Items for the authors (not changed in this round)
1. Section 3.1: "Five features" but six are listed.
2. Define 1D/M30/H1/H4 in the text before first use in Section 3.2 (blocked by the number gate).
3. Symbol reuse: `B` (VN100 returns vs bootstrap count), `β` (scaling slope vs factor loading), `α` (intercepts vs f(α)).
4. Figure and Box numbering vs first citation (Fig. 4 and Box 1 are cited in the Introduction).
5. The word "contribution" is absent from the Introduction (proofreading HARD rule); consider "Our contribution is ..." at "We build that version."
6. Section 5.7 calls P_heur "a volatility-scaled weight", while the Table S8 note says P_heur replaces w by the VN30–VN100 correlation; check that the two descriptions agree.

Edit accounting: 88 edits = 2 structure (Check 1) + 3 notation (Check 2) + 7 abbreviation (Check 6) + 5 stop-slop-only + 71 grammar/style (Check 5).
