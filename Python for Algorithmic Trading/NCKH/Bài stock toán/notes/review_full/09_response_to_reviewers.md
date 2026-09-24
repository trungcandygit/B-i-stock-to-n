# Response to Reviewers — Round 1 (internal ARS panel, `full` mode)

Format per roadmap item: **R** (reviewer point, summarised from the decision letter), **A** (action taken), **C** (where the change is, with the R output the numbers come from). All numbers trace to `project_R/outputs/`.

**RR1 — Inference on scaling slopes (methodology W1, W2).**
- R: HAC standard errors across 30 overlapping scales are invalid, and horizon dependence is over-generalised.
- A: The inference now uses a stationary block bootstrap of the bivariate returns that recomputes the whole DCCA curve (499 reps). Slopes are reported for all four frequencies and both ranges. The claim is restated: horizon dependence holds only for broad-market pairs at M30 and H1, and the purged pair is flat everywhere.
- C: §2.5; Tables 5–6; §3.7, §3.8.1; abstract; §4.1 (`R2_bootstrap_dcca.csv`).

**RR2 — Forbes–Rigobon test (methodology W3, W4, W13; domain W2; DA M4).**
- R: The test mixes estimators, its SE ignores dependence, and non-rejection was read as proof.
- A: The test now uses Pearson regime correlations with δ defined as the VN30 variance ratio, a within-regime block bootstrap (1,999 reps), a CI for ρ* − ρlow, a one-sided p and power at +0.05. Non-rejection is read as absence of evidence.
- C: §2.4, Table 4, §3.5 (`R3_…csv`). Panel A: −0.044 [−0.082, 0.001], power 0.77. Panel B: −0.066 [−0.132, 0.008], power 0.41.

**RR3 — Uncertainty of the overlap gap (methodology W7).**
- A: Bootstrap CIs are added for the gap.
- C: Table 2 Panel B and §3.2. The gap is 0.086–0.096, with intervals from 0.060 to 0.126.

**RR4 — Portfolio variance error (methodology W5; perspective W1, W2; eic W3; DA M5).**
- A: The errors are recomputed with one estimator and regime volatilities, with bootstrap CIs. The 15.6% headline is dropped. Regimes are labelled ex post, and P_cap is described as a non-investable factor exposure.
- C: §3.6; abstract; contributions; §4.1 (`R4_…csv`). Calm regimes: +2.23% [0.91, 3.94] and +9.38% [6.20, 13.46]. Turbulent regimes: −1.84% and −2.07%.

**RR5 — Single weight snapshot / no VNMIDCAP (corroborated by four seats).**
- A: A VNMIDCAP price history at the four frequencies is not available from the data source (logged). The limitation is stated in §2.1 and listed first in §4.3, and §3.8.2 presents the purged level as weight-conditional (weights 0.60–0.75).
- C: §2.1, §3.8.2, Table 7 (`R5_…csv`), §4.3. **Partially addressed; acknowledged limitation.**

**RR6 — Causal and overgeneralised wording (DA M1, M6, M8).**
- A: "Primarily reflect" and "proof" wording is removed, and the gap is always reported alongside "the purged correlation remains high".
- C: Abstract, contributions, §4.1, §4.4.

**RR7 — ASEAN-wide recommendations (eic W1; perspective W5; DA M7).**
- A: Statements about other ASEAN markets are now hypotheses, and the policy recommendations are scoped to Vietnam.
- C: Introduction ¶2, §4.2, §4.3.

**RR8 — "Unaddressed" gap claim.**
- A: Softened to "have received little attention", with no new references (author constraint).

**RR9 — Unused Podobnik t-test.**
- A: The test and its equation are removed, and the 2011 citation is reworded to match the paper's title.

**RR10 — Reliability thresholds under heavy tails.**
- A: GARCH(1,1)-t thresholds are added (20/151/86/28). Averages over them leave the results intact.
- C: Table 3, §3.3 (`R6_…csv`).

**RR11 — Multifractal width.**
- A: Δh is renamed the range of generalized exponents, and a benchmark against 100 shuffled surrogates is added. The ranking claim is softened: P_cap exceeds the benchmark only at 1D, and the nested pairs in 2 of 12 cases.
- C: §2.6, §3.4 (`R7_…csv`).

**RR12 — Filled file.**
- A: The paper now states that no index price is filled; the filled file differs only in an unused exchange-rate column (`R1_…csv`).

**RR13 — Code.**
- A: The R code is supplied as Online Resource 1 (`project_R/`, `run_all.R`, `run_revision.R`).

**RR14 — Citation attributions.**
- A: Hong–Stein, Epps scope, Oświęcimka, Peng/Kantelhardt and Podobnik 2011 are corrected.

**RR15 — Factual precision.**
- A: Corrections cover:
  - the T+2 settlement cycle;
  - VNINDEX full-cap weighting;
  - price-band wording;
  - Le et al. wording;
  - ETF wording;
  - the 2018 window;
  - the derivative claim;
  - horizon units.

**RR16 — Presentation.**
- A: Presentation changes:
  - funding pointer added;
  - the subset relation centered as Eq. (1);
  - the redundant RSS/IDSS passage trimmed;
  - equations numbered;
  - "4 Discussion" with 4.1–4.4 matching the roadmap;
  - the pseudo-heading removed.

**RR17 — Reference style (eic W5). REVIEWER_DISAGREE.**
- A: The references keep the style shown in the APFM author instructions (name–year, APA-like list). The editor sided with the journal instructions.

**RR18 — Market-classification status.**
- A: No change. The status cannot be verified within the allowed sources, so the manuscript makes no claim about it.

Verification: `08_rereview_round2.md` (re-review, all items resolved; RR5 as a limitation).
