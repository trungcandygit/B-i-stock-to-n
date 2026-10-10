# 18 — Find-journal run (find-journal skill, Post-Rejection Mode)

Date: 2026-10-10. Skill: `vendor/find-journal` (SKILL.md, POLICY.md, `references/acceptance_signals_schema.md`).
Manuscript: `project_R/docx_build/r2/manuscript_anonymized.md`, "How Much of a Nested Index Correlation Is
Construction? A Scale-Wise Part–Whole Decomposition with Evidence from Vietnam". Original research article,
about 6,400 words, 9 tables, 4 figures plus supplement. JEL C14, C58, G11, G15.

## 0. Method, sources and limits (read first)

- **Network limit.** The session's egress proxy refused HTTPS CONNECT (403) to every publisher host
  (emerald.com, emeraldgrouppublishing.com, tandfonline.com, link.springer.com, onlinelibrary.wiley.com,
  journals.sagepub.com, sciencedirect.com) and to scimagojr.com. WebFetch could not open any page. The
  only research channel was **WebSearch**, which returns extracts of indexed pages. Every field below was
  transcribed from those extracts of the named URLs (mostly the journal's own page or SCImago's own journal
  page). Anything not seen there is marked **UNVERIFIED**. No impact factor, quartile, APC or turnaround
  figure was inferred or invented.
  The environment's Network-access settings can allow these hosts. Once they are allowed, the profiles
  should be re-checked against the live pages.
- **Profile tier.** Because POLICY.md requires the homepage and author guidelines to be opened directly,
  the 17 new profiles in `vendor/find-journal/references/journal_profiles_finance/` meet the
  **private-tier** bar only. Each carries an evidence note saying so. They are not promoted to the public
  `journal_profiles/` folder.
- **Profiles loaded (Phase 3.1).** Public tier `journal_profiles/`: medical only, 0 in scope. Private tier
  `$HOME/.claude/private-journal-profiles/find-journal/`: absent. New finance tier: **17 profiles loaded**.
  No write-paper detail profiles exist (Pass 2 used the compact profiles only).
- **Tier rule used.** SCImago Journal Rank **SJR 2025** (the latest edition, released 2026), read from
  scimagojr.com journal pages through search extracts. A journal qualifies if its quartile in the **Finance**
  or **Economics and Econometrics** category is Q2 or Q3. A journal with only the
  "Economics, Econometrics and Finance (miscellaneous)" category is judged on that category.
- **Cost rule.** Subscription or hybrid journals with no mandatory APC pass (the author publishes non-OA).
  Full-OA journals pass only if the APC is under USD 1,000, waived or sponsored.

## 1. Step 1 — Candidate pool (26 journals screened)

Screened: Studies in Economics and Finance, Emerging Markets Finance and Trade, Journal of Capital Markets
Studies, Journal of Economics and Finance, Journal of Emerging Market Finance, North American Journal of
Economics and Finance, Quantitative Finance, Review of Quantitative Finance and Accounting, Annals of
Finance, Computational Economics, Journal of Risk Finance, Managerial Finance, Asia-Pacific Journal of
Financial Studies, Journal of Economics and Development (NEU, Emerald), Investment Analysts Journal, Studies
in Nonlinear Dynamics & Econometrics, Journal of Forecasting, Journal of Asian Business and Economic
Studies (UEH, Emerald), Asian Journal of Economics and Banking (BUH, Emerald), Journal of Derivatives and
Quantitative Studies (KDA, Emerald), Review of Pacific Basin Financial Markets and Policies, Cogent
Economics & Finance, Physica A, Asia-Pacific Financial Markets, plus the MDPI titles JRFM and IJFS (and
Risks, Economies, Fractal Fract, Entropy as MDPI class exclusions).

### Excluded journals (hard-filter failures)

| Journal | Publisher | Reason for exclusion |
|---|---|---|
| Asia-Pacific Financial Markets | Springer | Desk-rejected the earlier version (Post-Rejection Mode). Note: SJR 2025 Finance **Q2** (0.521), Q3 in 2024, which is the reference tier for "one tier down". |
| Journal of Asian Business and Economic Studies (UEH) | Emerald | **Above the tier band.** SJR 2025 = 0.693, Q1 in Econ., Econometrics & Finance (misc.), Q2 only in Business & International Management. It has no Finance or E&E category. Diamond OA, so it would pass on cost. It is a stretch option if the author relaxes the tier filter. |
| Asian Journal of Economics and Banking (BUH) | Emerald | **No quartile yet.** Indexed in Scopus only on 14 Sep 2026 (coverage from 2022), so there is no SJR quartile to verify. Platinum OA with no APC. Revisit in SJR 2026. |
| Journal of Derivatives and Quantitative Studies (KDA) | Emerald | **Tier unverified.** SJR 2024 Finance Q3 (0.220, falling). The 2025 entry was not found, and a third-party page lists Q4. |
| Review of Pacific Basin Financial Markets and Policies | World Scientific | **Tier unverified.** The SCImago page was not reached. Aggregators conflict (Q3 vs Q4; SJR about 0.15–0.32). |
| Cogent Economics & Finance | Taylor & Francis | **Cost.** Full OA with an APC of GBP 1,000 (Editage and researcher.life listings), which is above USD 1,000. |
| Physica A: Statistical Mechanics and its Applications | Elsevier | **Field.** Its SJR categories are Condensed Matter Physics, Statistical & Nonlinear Physics and Statistics & Probability (Q2), not Finance or E&E. It has the strongest DCCA scope fit of any candidate if the field filter is relaxed. |
| Journal of Risk and Financial Management; International Journal of Financial Studies; Risks; Economies; Fractal and Fractional; Entropy | MDPI | **MDPI excluded** by the author's rule. |

**Survivors: 17** (all profiled).

## 2. Phase 2 — Theme extraction

- **Object / "condition":** correlation between *nested* equity indices (child ⊂ parent), where part of the
  coefficient is fixed by constituent overlap.
- **Technique:** detrended cross-correlation analysis (DCCA, ρ_DCCA). Lemma 1 extends the Pearson (1897) and
  Cureton (1966) part–whole identity to scale-wise detrended coefficients. It gives a closed-form benchmark,
  an exact lower bound, a sensitivity and an order-free attribution from index-level inputs. Robustness
  checks use DMCA and MF-DCCA.
- **Methodology:** empirical financial econometrics. Block bootstrap that also draws the index weight;
  intraday 30-minute to daily data; contagion tests (adjusted correlation vs factor loading); out-of-sample
  portfolio variance forecasts with regime-conditioned correlations.
- **Population / market:** Vietnam HOSE (VN30 ⊂ VN100 ⊂ VNINDEX), 2014–2025. One frontier/emerging market.
- **Innovation type:** methodological identity (new decomposition), with an empirical application and
  negative or qualified results (horizon effects confined to auction bars, test-dependent contagion, no
  out-of-sample gain).

## 3. Phase 2.5 — Acceptance-readiness and design-ceiling pre-flight

Script result (re-run 2026-10-10): `flags: (none)`, verdict
`NO LISTED SIGNAL MATCHED - NOT A DESIGN CLEARANCE; ASSESS DESIGN CEILING BY JUDGEMENT`. The script's lexicon
is clinical, so the §3 taxonomy was applied by judgement:

| Category | Signal in this manuscript | Severity |
|---|---|---|
| DESIGN_CEILING | **Single-market evidence.** One exchange and one nested family (HOSE). This is the finance analogue of "single-center": the identity is general, but the empirical magnitudes (sensitivity 0.106–0.112, gap 0.099–0.104, κ 0.47–0.52) are shown for one market only. | Design-level; fixable only by adding a second nested system. |
| IMPORTANCE_RISK | **Prior desk reject on importance** ("statistical report… insufficient technical innovation", APFM). The core result extends a 1897/1966 identity, so editors may read it as **incremental**. | Main risk |
| IMPORTANCE_RISK | **Null / qualified findings** with little importance framing: regime correlations "do not improve" out-of-sample variance forecasts; contagion "depends on the test used"; Pearson "suffices in these data". Three of five headline results are negative or limiting. | Moderate |
| CLAIM_MISMATCH | Conclusion advises that "users of index-level data should decompose nested correlations before reading them as evidence about diversification". This is a general prescription resting on single-market evidence. | Mild |
| UNFIXABLE_DEFECT | None found by judgement. Data come from a vendor (TradingView) under its terms of use. This is not a validity defect, but it conflicts with mandatory-replication venues (SNDE). | Venue-specific |

**Ceiling verdict (judgement):** `SPECIALTY / TOLERANT-VENUE OR DESIGN FIX RECOMMENDED`, with
`IMPORTANCE-FRAMING REVIEW RECOMMENDED`. There is one design-ceiling signal (single market) and two
importance signals, one of them already confirmed by an editor's desk reject.

**Post-Rejection Mode consequence.** The desk reject was on importance or novelty, not a fixable revision.
A venue at APFM's level (Finance Q2, SJR 0.52) or higher that screens hard for novelty will probably
desk-reject again. Routing: (a) Q2 venues with **SJR at or below APFM** or an **accessible** acceptance
profile, and Q3 venues (one tier down); (b) a **presubmission inquiry** to the primary target; (c) reframe
the contribution before submission (see §6).

## 4. Phase 3 — Two-axis scoring (17 survivors)

Axis 1 weights: scope 40, study type 25, tier 20 (Q2 and Q3 both meet the author's band, so both score 20),
cost/OA 10 (diamond OA = 10, subscription with no fee = 8, submission fee = 6), special fit 5 (published fast
first decision, emerging-market or Vietnam alignment). Axis 2 is a band only, never a probability.

| # | Journal (publisher) | SJR 2025 tier | Scope | Type | Tier | Cost | Spec. | **Axis 1** | Axis 2 feasibility (reason) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Studies in Economics and Finance (Emerald) | Finance Q2, E&E Q2 (0.484) | 32 | 22 | 20 | 8 | 5 | **87** | Medium: SJR below APFM, but published acceptance rate is only 5.7 % |
| 2 | Emerging Markets Finance and Trade (T&F) | Finance Q2 (0.747) | 33 | 22 | 20 | 8 | 3 | **86** | Medium-High: 33 % acceptance; explicitly no geographic preference, which suits the single-market design |
| 3 | Journal of Capital Markets Studies (Emerald/TSPB) | Finance Q2, E&E Q2 (0.496) | 32 | 21 | 20 | 10 | 3 | **86** | Medium: SJR below APFM, diamond OA; prefers comparative/regional work, so the single market is a mild mismatch |
| 4 | Journal of Economics and Finance (Springer) | Finance Q3, E&E Q3 (0.413) | 28 | 22 | 20 | 8 | 5 | **83** | Medium-High: one tier down; empirical-econometric emphasis |
| 5 | Journal of Emerging Market Finance (Sage) | Finance Q3, E&E Q3 (0.426) | 31 | 22 | 20 | 8 | 1 | **82** | Medium-High: one tier down; emerging-market finance core scope |
| – | Quantitative Finance (T&F) | Finance Q2 (0.762) | 34 | 22 | 20 | 8 | 4 | 88 | **Low (demoted):** above APFM's level, 23 % acceptance, requires interest to a broad quantitative readership, which is the same novelty bar that failed at APFM |
| – | N. American J. of Economics and Finance (Elsevier) | Finance Q2, E&E Q2 (0.812) | 34 | 22 | 20 | 8 | 3 | 87 | **Low-Medium (demoted):** above APFM's level; about 12 % acceptance (Elsevier shop page) |
| 6 | Review of Quantitative Finance and Accounting (Springer) | Finance Q2 (0.700) | 30 | 22 | 20 | 8 | 4 | 84 | Medium: above APFM's level; scope text UNVERIFIED |
| 7 | Studies in Nonlinear Dynamics & Econometrics (De Gruyter) | E&E Q3 (0.411) | 30 | 22 | 20 | 10 | 1 | 83 | Medium: mandatory data-and-code replication conflicts with the TradingView vendor terms |
| 8 | Annals of Finance (Springer) | Finance Q3 (0.343) | 28 | 22 | 20 | 8 | 4 | 82 | Medium: theory-leaning finance; low-SJR Q3 |
| 9 | Asia-Pacific J. of Financial Studies (Wiley/KSA) | Finance Q2 (0.542) | 31 | 22 | 20 | 6 | 2 | 81 | Medium: about APFM's level; 29 % acceptance; submission fee USD 100–150 (dated page) |
| 10 | Computational Economics (Springer) | EEF misc Q2 (0.459) | 27 | 22 | 20 | 8 | 4 | 81 | Medium: computational-methods angle; the 2-day median reflects desk decisions |
| 11 | Journal of Risk Finance (Emerald) | Finance Q2 (0.916) | 26 | 22 | 20 | 8 | 4 | 80 | Medium-Low: insurance/risk-transfer scope; high SJR |
| 12 | Managerial Finance (Emerald) | best Q2 (0.555) | 26 | 22 | 20 | 8 | 4 | 80 | Medium: broad finance scope |
| 13 | Journal of Economics and Development (Emerald/NEU) | E&E Q2 (0.810) | 22 | 20 | 20 | 10 | 5 | 77 | Medium: development-economics scope, finance not named; diamond OA, 30 days |
| 14 | Investment Analysts Journal (T&F) | Finance Q3, E&E Q3 (0.428) | 24 | 22 | 20 | 8 | 3 | 77 | Medium-High: 29 % acceptance |
| 15 | Journal of Forecasting (Wiley) | E&E Q2 (0.665) | 20 | 20 | 20 | 8 | 4 | 72 | Low-Medium: forecasting is a secondary theme; 12 % acceptance |

Ranking rule (SKILL §3.4): Axis 1 first, then Axis 2. Quantitative Finance and NAJEF have the highest scope
scores but are demoted for feasibility. Both mismatches are spelled out in the comparison note below.

## 5. Phase 4 — Output

### Rank 1: Studies in Economics and Finance (Q2 — SJR 2025 Finance Q2, E&E Q2)

**Scope fit:** SEF's stated scope is the intersection of finance, financial markets and economics, and
lists asset pricing, market efficiency, financial econometrics and risk management. Those cover the paper's
DCCA decomposition, bootstrap inference and portfolio-risk evaluation. Unlike APFM's focus on Asia-Pacific
financial engineering and econometrics, SEF is a general finance outlet, so the paper should be framed as a
general measurement problem for any nested index system, with Vietnam as the test case.

**Article types accepted:** Research paper (empirical and theoretical); other types UNVERIFIED.

**Open Access:** Subscription/hybrid. No mandatory APC (USD 0 on the non-OA route).

**Acceptance feasibility:** Medium. The Q2 tier sits just below APFM (SJR 0.484 vs 0.521), and the 16-day
first decision makes a desk answer cheap. However, the published 5.7 % acceptance rate means the
importance case must be made in the first paragraph and the cover letter.

**Homepage:** https://www.emerald.com/sef
**Author guidelines:** https://www.emeraldgrouppublishing.com/journal/sef (exact guidelines URL UNVERIFIED)

**AI disclosure:** Required. Under Emerald policy, AI may copy-edit the authors' own text. Generating new
content is not permitted. Any use must be declared in Methods/Acknowledgements and at submission. See the
AI-declaration flag in §6.

**Review speed:** 16 days to first decision; 42 days from acceptance to publication (Emerald page,
submissions Apr 2024–Mar 2025).

### Rank 2: Emerging Markets Finance and Trade (Q2 — SJR 2025 Finance Q2; best Q1 in EEF misc.)

**Scope fit:** EMFT publishes empirical emerging-market finance with implications for policymakers,
investors and financial institutions. It states no country or region preference, so a single-market HOSE
study is within scope by design. The contagion tests, size-tier diversification and out-of-sample
portfolio-risk results map to its "implications for stakeholders" requirement. APFM is
econometrics-leaning; for EMFT, lead with what index users and fund managers in emerging markets should do
differently.

**Article types accepted:** Original research article; other types UNVERIFIED.

**Open Access:** Hybrid. No mandatory APC.

**Acceptance feasibility:** Medium-High. The 33 % published acceptance rate and the explicit tolerance for
single-country emerging-market studies fit the single-market ceiling. The risk is the "practical
implications" bar: a methods-first framing could read as theory without application.

**Homepage:** https://www.tandfonline.com/journals/mree20
**Author guidelines:** UNVERIFIED (About page: https://www.tandfonline.com/journals/mree20/about-this-journal)

**AI disclosure:** Required (Taylor & Francis). Name the tool and version, and say how and why it was used,
in Methods or Acknowledgments. AI cannot be an author.

**Review speed:** 52 days average to first decision, including desk rejects; 18 days from acceptance to
online publication.

### Rank 3: Journal of Capital Markets Studies (Q2 — SJR 2025 Finance Q2, E&E Q2)

**Scope fit:** JCMS focuses on capital markets and on the link between academic research and practice,
including financial instruments and market microstructure. The nested-index construction problem, the
auction-bar horizon effect and the diversification-between-size-tiers implication are capital-market
microstructure and index-design issues. Its preference for comparative or regional work means a short
comparative extension would strengthen the fit.

**Article types accepted:** Research paper (empirical or policy), literature review, case study, theoretical
contribution, book review.

**Open Access:** Full OA, diamond. No APC and no submission charge (funded by the Turkish Capital Markets
Association); CC BY 4.0.

**Acceptance feasibility:** Medium. SJR is below APFM (0.496), the journal is small, and the cost is zero.
The single-market design collides mildly with the stated preference for comparative studies.

**Homepage:** https://www.emerald.com/jcms
**Author guidelines:** UNVERIFIED (About page: https://www.emerald.com/jcms/pages/about)

**AI disclosure:** Required (Emerald policy, as for Rank 1).

**Review speed:** 49 days to first decision; 34 days from acceptance to publication (Emerald page); DOAJ
says about 12 weeks from submission to publication.

### Rank 4: Journal of Economics and Finance (Q3 — SJR 2025 Finance Q3, E&E Q3)

**Scope fit:** JEF (official journal of the Academy of Economics and Finance) emphasises empirical work that
uses recent econometric advances, with attention to policy relevance. The scale-wise DCCA identity with
weight-drawing block bootstrap is a recent econometric tool applied to a policy-relevant measurement
question. This is a one-tier step down from APFM, which Post-Rejection Mode advises after an importance
desk-reject.

**Article types accepted:** Original research paper; other types UNVERIFIED.

**Open Access:** Hybrid (Springer Open Choice optional). No mandatory APC.

**Acceptance feasibility:** Medium-High. A Q3 venue with an empirical-econometrics mandate fits the design
ceiling. The single-market scope is unlikely to be disqualifying.

**Homepage:** https://link.springer.com/journal/12197
**Author guidelines:** https://link.springer.com/journal/12197/submission-guidelines

**AI disclosure:** Required (Springer Nature). Document LLM use in Methods or an equivalent section; AI-assisted
copy editing is exempt.

**Review speed:** median 10 days from submission to first decision (Springer page, 2025 metrics; includes
desk decisions).

### Rank 5: Journal of Emerging Market Finance (Q3 — SJR 2025 Finance Q3, E&E Q3)

**Scope fit:** JEMF is a forum on the theory and practice of finance in emerging markets, with emphasis on
practical significance. A Vietnam-specific index-correlation study with portfolio-risk consequences is
central to that scope. Like JEF, this is one tier below APFM.

**Article types accepted:** Research article; other types UNVERIFIED.

**Open Access:** Subscription. Sage Choice OA is optional after acceptance. No mandatory APC.

**Acceptance feasibility:** Medium-High. A Q3 emerging-market specialist suits the single-market ceiling.
Note that it uses double-anonymized review and **does not accept preprints**, so confirm no SSRN or arXiv
version is posted.

**Homepage:** https://journals.sagepub.com/home/emf
**Author guidelines:** https://journals.sagepub.com/author-instructions/emf

**AI disclosure:** Required for generative use (Sage). Assistive language or grammar tools need no
disclosure. Generative use must name the model and purpose.

**Review speed:** not published.

**Comparison note.** The top three are Q2 venues at or below APFM's SJR (SEF, JCMS) or with an accessible
acceptance profile (EMFT). They trade tier for desk-screen risk. JEF and JEMF are the one-tier-down Q3
options that Post-Rejection Mode favours after an importance desk-reject. **Quantitative Finance** and
**NAJEF** have the strongest raw scope fit (88 and 87), because quantitative methods, financial econometrics
and stock markets are core to both. Both were demoted because they sit above APFM's level with 12–23 %
acceptance and an explicit novelty or broad-readership bar. If a second market is added (see §6), they
become realistic primaries. **SNDE** fits methodologically, but its mandatory online data-and-code
replication conflicts with the vendor-terms data statement.

**Summary table (top 5)**

| Rank | Journal | Publisher | Tier (source, year) | Cost to author | Review speed (journal's own figure) | Feasibility |
|---|---|---|---|---|---|---|
| 1 | Studies in Economics and Finance | Emerald | Q2 Finance & E&E — SCImago SJR 2025 (0.484) | USD 0 (subscription/hybrid, no mandatory APC) | 16 d to first decision | Medium |
| 2 | Emerging Markets Finance and Trade | Taylor & Francis | Q2 Finance — SCImago SJR 2025 (0.747) | USD 0 (hybrid, no mandatory APC) | 52 d to first decision (incl. desk); 33 % acceptance | Medium-High |
| 3 | Journal of Capital Markets Studies | Emerald / TSPB | Q2 Finance & E&E — SCImago SJR 2025 (0.496) | USD 0 (diamond OA) | 49 d to first decision | Medium |
| 4 | Journal of Economics and Finance | Springer | Q3 Finance & E&E — SCImago SJR 2025 (0.413) | USD 0 (hybrid, no mandatory APC) | 10 d median to first decision | Medium-High |
| 5 | Journal of Emerging Market Finance | Sage | Q3 Finance & E&E — SCImago SJR 2025 (0.426) | USD 0 (subscription) | not published | Medium-High |

---
### Acceptance-Readiness Summary

**Ceiling verdict:** SPECIALTY / TOLERANT-VENUE OR DESIGN FIX RECOMMENDED, plus IMPORTANCE-FRAMING REVIEW
RECOMMENDED. The lexical script returned no flags; this verdict comes from applying the §3 taxonomy by
judgement.
**Top flags:**
- IMPORTANCE_RISK (confirmed): APFM desk-rejected the paper as a "statistical report… insufficient
  technical innovation". The headline result extends a classical identity, which editors may read as
  incremental.
- DESIGN_CEILING: single-market evidence (one exchange, one nested family). The general identity is
  demonstrated on one system only.
- IMPORTANCE_RISK: three of five results are null or qualified (no out-of-sample gain, test-dependent
  contagion, Pearson suffices) without an importance argument for the null.
- CLAIM_MISMATCH (mild): a general prescription to all index-data users rests on HOSE evidence alone.
**Implication for venue tier:** Without a second market or a sharper contribution statement, venues at or
above APFM's Q2 level that screen hard for novelty (Quantitative Finance, NAJEF, RQFA) are likely to
desk-reject again. The picks above go to Q2 venues at or below APFM's SJR, an accessible emerging-market Q2,
and two Q3 one-tier-down options.

_Advisory only — a risk band, not an acceptance prediction; flags are not auto-fixable._

---
### Cascade plan (primary → reject-fallback)

1. **Primary: Studies in Economics and Finance (Emerald).** Its 16-day first decision makes it the cheapest
   test of the reframed importance argument. It is Q2 at an SJR just below APFM, and it costs nothing.
   **Send a presubmission inquiry first** (abstract plus a 3-sentence contribution statement), because the
   risk is importance, not design.
2. **If desk-rejected:** **Journal of Capital Markets Studies**, the same publisher (Emerald). It is diamond
   OA, Q2, and its capital-markets and microstructure angle is a different framing. An Emerald formal
   transfer service is UNVERIFIED, so if the editor offers a transfer, take it, because the manuscript
   skips a fresh desk screen. If rejected **after review**, go instead to **Emerging Markets Finance and
   Trade** (T&F), with the referee points addressed and the emerging-market policy implications in front.
3. **Then: Journal of Economics and Finance (Springer)**, one tier down, with a 10-day median first decision.
   If JEF declines, ask about the **Springer Nature Transfer Desk** (publisher-level service; per-title
   availability UNVERIFIED) towards **Annals of Finance** (Q3 Finance) or Computational Economics (EEF misc.
   Q2). After JEF, the Sage option is **Journal of Emerging Market Finance** (Q3); check the no-preprint rule
   first.
4. **Upgrade path (only after a design fix):** if a second nested index system is added, re-target
   **Quantitative Finance** (T&F) or **NAJEF** (Elsevier; Elsevier Article Transfer Service on reject).

Phase 2.5 risk is **importance** rather than design, so a **presubmission inquiry** to the primary target is
recommended before full submission. It lets the editor quickly judge contribution and fit, and saves a
desk-reject cycle.

No confidential editor-bar overlay exists in `$HOME/.claude/private-journal-profiles/find-journal/`, so none
was merged.

## 6. Post-Rejection Mode — scope and design suggestions

1. **Lead with the identity's generality, not Vietnam.** In the title, abstract and first paragraph, state
   the problem as "any nested index family (S&P 500/100, FTSE 350/100, MSCI EM/Asia)". State Lemma 1's
   benchmark, lower bound and order-free attribution as a tool index-data users lack, and keep HOSE as the
   test case.
2. **Design fix for the single-market ceiling (raises feasibility one band):** add a second nested family
   from another market, even daily-only, using only index-level inputs. This is the fix that would reopen
   the QF and NAJEF targets.
3. **Frame the nulls as findings.** For example: "regime-conditioned correlations add no out-of-sample
   value once overlap is purged". This turns IMPORTANCE_RISK statements into decision-relevant results for
   portfolio managers (fits EMFT and JEMF).
4. **Cover letter:** address the APFM criticism directly. State the technical innovation (closed form,
   bound, sensitivity, attribution, and the weight-drawing bootstrap) and why a "statistical report"
   reading is wrong.
5. **AI-declaration flag (must resolve before any Emerald submission).** The manuscript declares Claude was
   used for "drafting of revisions" and code translation. Emerald's policy, as quoted from its
   publication-ethics page and its May-2024 statement, **does not permit AI to generate or draft any part of
   a submission**; it allows only copy-editing of the authors' own text. The authors must make the
   declaration accurate and confirm the use complies before submitting to SEF or JCMS. T&F, Springer
   Nature and Sage allow declared generative use. The current wording follows the Elsevier template, so
   reword it per target (for T&F, add the tool version and the reason).
6. **Data statement:** the vendor-terms restriction (TradingView) rules out mandatory-replication venues
   such as SNDE unless redistribution rights are obtained.

## 7. Decisions taken without asking (CLAUDE.md §1b)

- The quartile source is SCImago SJR 2025, the latest edition. JCR quartiles from aggregators were ignored.
- JABES was excluded as above the Q2–Q3 band (its only finance-group category is EEF misc. Q1), though it
  passes on cost.
- "Feasibility" is anchored to APFM's SJR 2025 (0.521, Finance Q2) as the reference tier for "one tier
  down".
- Profiles are private-tier because direct page verification was impossible (network policy). They were
  not promoted.
- This report does not modify `notes/AUDIT_LEDGER.md` (per instruction); the caller should log the
  decision.

---
**Important Disclaimer**

Impact Factor, APC fees, acceptance rates, and turnaround times change frequently
and are subject to copyright restrictions. Please verify current values directly
at each journal's homepage before making your submission decision.

Recommended verification sources:
- Journal Citation Reports (JCR) via institutional access: for Impact Factor
- Journal homepage -> Author Guidelines: for current APC and formatting requirements
- Clarivate Master Journal List: for indexing status

## Correction (orchestrator, 2026-10-10)

EMFT's best SJR 2025 quartile is **Q1** (Economics, Econometrics and Finance, miscellaneous), not Q2. That places it above APFM (Q2), which desk-rejected the paper on importance. Under Post-Rejection Mode (route one or two tiers below the rejecting journal) EMFT's acceptance feasibility is revised from Medium-High to **Medium**; its 33 % acceptance rate is a journal-wide figure across all submissions and does not offset a higher bar on novelty. Revised feasibility-adjusted order inside the author's Q2–Q3 band: Journal of Economics and Finance → Journal of Emerging Market Finance → (Q1, optional) EMFT. IAJ dropped by the author (USD 50 submission fee).
