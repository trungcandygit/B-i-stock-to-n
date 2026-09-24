# Re-review — Round 2 (academic-paper-reviewer `re-review` mode, verification of the Round-1 Revision Roadmap)

**Manuscript:** Nested Equity Index Correlations Overstate True Co-Movement: Evidence from Vietnam (APFM).
**Input:** the immutable Round-1 roadmap (`06_editorial_synthesis.md`, RR1–RR18) and the revised manuscript
built by `docx_build/stage3.py` (Round-1 revision), plus the Round-2 residual fixes (`stage4.py`).
**Calibration:** `NOT_CALIBRATED`. **Criteria binding:** `criteria_binding_unavailable`.
**Provenance disclosure:** the re-review ran in the same session and model family as the author-side revision.
It is role-separated but not independent (see `07_review_panel_provenance.json`).

## Gate 1 — criteria commitment (fixed before reading the revision)

Each RR item counts as **resolved** only when (a) the requested change appears in the manuscript, (b) every number it
introduces traces to an R output in `project_R/outputs/`, and (c) the claim wording does not exceed that evidence.

## Gate 2 — evidence verdicts

| ID | Verdict | Evidence (manuscript location → R output) |
|---|---|---|
| RR1 | Resolved | §2.5 describes a stationary block bootstrap that recomputes the whole DCCA curve (499 reps). Tables 5–6 report full/reliable slopes with CIs at all four frequencies (`R2_bootstrap_dcca.csv`). Horizon dependence is restated as "broad-market pairs at M30 and H1 only" (abstract, §3.7, §3.8.1, §4.1). *Round-2 residual fixed:* the §2.5 Epps paragraph pre-judged a positive slope; it now says "can produce" and points to §3.7. |
| RR2 | Resolved | §2.4 specifies Pearson regime correlations with δ as the VN30 variance ratio. Inference is a within-regime bootstrap (1,999 reps) with CI, one-sided p and power (Table 4; `R3_forbes_rigobon_pearson_bootstrap.csv`). Non-rejection is read as absence of evidence (§3.5, §4.1). |
| RR3 | Resolved | Table 2 Panel B reports gap CIs (`R2_…`, stat = gap). The text cites the 0.060–0.126 range. |
| RR4 | Resolved | §3.6 applies one estimator with regime volatilities and reports CIs (`R4_portfolio_error_pearson.csv`). The 15.6% headline is dropped. Regimes are described as ex post, and P_cap as a non-investable factor exposure. |
| RR5 | Resolved as limitation | VNMIDCAP data are unavailable (logged D-items). §2.1 states this. §3.8.2 calls the purged level weight-conditional. The §4.3 limitation comes first. |
| RR6 | Resolved | Abstract, contributions and conclusion no longer say "primarily reflect"/"proof"; they report the gap alongside "remains high". *Round-2 residual fixed:* "Mid-cap diversification failure" became "The loss of mid-cap diversification". |
| RR7 | Resolved | §4.2 frames the ASEAN implications as hypotheses. *Round-2 residual fixed:* the intro sentence generalizing to "emerging frontier exchanges" was replaced by the specific Malaysia/Vietnam contrast. The §4.2 product recommendation was scoped to Vietnam in Round 3. |
| RR8 | Resolved | "remain comparatively underexplored" → "have received little attention", with no new references. |
| RR9 | Resolved | The Podobnik t-test and its equation were removed. *Round-2 residual fixed:* the intro still credited Podobnik et al. (2011) with "the analytical finite-sample distribution"; it now says "proposed statistical tests for power-law cross-correlations" (their title). |
| RR10 | Resolved | Table 3 adds the GARCH(1,1)-t thresholds. §3.3 reports conservative averages (`R6_reliability_garch_t.csv`). |
| RR11 | Resolved | §2.6 renames Δh to "range of generalized exponents" and adds the shuffled-surrogate benchmark. §3.4 reports the exceedances (`R7_mfdcca_shuffle_surrogate.csv`: P_cap only at 1D; nested 2 of 12). |
| RR12 | Resolved | §2.1: "no index price is filled or interpolated" (`R1_filled_file_check.csv`). |
| RR13 | Resolved | Code availability names Online Resource 1 (`project_R/`). |
| RR14 | Resolved | Hong–Stein is cited for diffusion, Peng/Kantelhardt for DFA, and Oświęcimka for the complex-moment issue; see RR9 for Podobnik 2011. |
| RR15 | Resolved | T+2 settlement, VNINDEX full-cap weighting and the 2018 window are stated. *Round-2 residuals fixed:* price-band wording ("can reach the lower limit, where trading dries up") and the derivative claim ("no futures contract is listed on a mid-cap index"). |
| RR16 | Resolved | Funding pointer, centered subset relation, equation numbering (1)–(17) and "4 Discussion" with 4.1–4.4 are in place. *Round-2 residual fixed:* the "Economic Mechanisms and Identification Boundaries:" pseudo-heading was removed and a duplicate tier sentence deleted. |
| RR17 | REVIEWER_DISAGREE upheld | The reference style follows the APFM author instructions. |
| RR18 | No change | Market-classification status cannot be verified within the allowed sources, so no claim is made. |

Additional Round-2 findings (not on the roadmap, found by the re-read and fixed in `stage4.py`):
- ASEAN, OLS and GARCH were not introduced in the body before first use; now introduced.
- "variance of the underlying assets has risen by 221% to 706%": δ refers to VN30, so the wording was corrected.
- "at least 0.052 below": the rounded tables give 0.977 − 0.924 = 0.053, so the text now says "at least 0.05".

## Gate 3 — claim matching

Every number in the abstract, contributions, §3 and §4 was matched to the R outputs listed above (and `01`–`20` for
the unchanged tables). No unmatched claim remains.

## Outcome

All required items are resolved (RR5 is resolved as a stated limitation), and no new Critical/Major issue was found.
Per the academic-paper IRON RULE (at most two revision rounds), the revision loop closes. Rounds 3–4 are
language-level passes (proofreading + stop-slop, requested by the author) and must not change any result.
