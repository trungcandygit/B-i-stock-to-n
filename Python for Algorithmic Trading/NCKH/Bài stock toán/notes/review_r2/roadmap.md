# Revision Roadmap — Round 2 (Iter 24)

Skill: academic-paper `revision-coach` → `revision`; orchestrated by academic-pipeline (mid-entry, Stage 4).
Inputs: (a) Asia-Pacific Financial Markets desk decision on "Nested Equity Index Correlations Overstate True
Co-Movement: Evidence from Vietnam"; (b) Reviewer 1 report from Cogent Economics & Finance on a *different*
manuscript (inverse Black–Litterman + k-means). The user asked that every transferable comment in (b) be
applied to this manuscript. Base text: the authors' uploaded `02_Manuscript_Anonymized.docx`.

Severity: P0 = blocks acceptance; P1 = major; P2 = minor. Status codes: ACCEPT (will address),
PARTIAL, N/A (does not transfer, reason given), DISAGREE (reasoned pushback).

## A. Editor, Asia-Pacific Financial Markets

| ID | Comment | Sev. | Status | Action |
|---|---|---|---|---|
| E1 | "Essentially a statistical report… insufficient technical innovation." | P0 | ACCEPT | New Proposition 1 with proof: exact scale-by-scale decomposition of the nested DCCA coefficient into a mechanical-overlap floor and an economic component, ρ_AB(s) = (1+κρ_AM)/√(1+κ²+2κρ_AM). Derive floor 1/√(1+κ²), sensitivity ∂ρ_AB/∂ρ_AM, and the mechanical share; estimate with block bootstrap at four frequencies (R8). Corollary: the identity holds for any bilinear dependence measure (Pearson, DCCA, DMCA). New Fig. 4. Title, abstract and contributions rewritten around this result. |

## B. Reviewer 1 (Cogent) — transferable comments

| ID | Comment | Sev. | Status | Action |
|---|---|---|---|---|
| R1.1 | Title should state the contribution | P2 | ACCEPT | Title names the exact decomposition. |
| R1.2a | Abstract lacks statistical significance of improvements | P1 | ACCEPT | Abstract reports bootstrap intervals for the gap and the mechanical share. |
| R1.2b | Quantify improvement | P1 | ACCEPT | Abstract states the share (≈91%) and the attenuation factor. |
| R1.2c | "Provides empirical evidence" too strong for one market | P1 | ACCEPT | Scope statements limited to HOSE, three indices; ASEAN only as hypothesis. |
| R1.2d | Transaction costs | — | N/A | No trading strategy or rebalancing; portfolio results are variance misstatements, not P&L. Stated explicitly. |
| R1.2e | Monte Carlo robustness covers one parameter | P2 | ACCEPT | Abstract and text now name all robustness dimensions (weight, block length, detrending order, reliability calibration, DMCA, tail dependence). |
| R1.3.1 | Research gap asserted, not demonstrated | P1 | ACCEPT | New literature comparison table (Table 1) and novelty matrix; gap stated against named studies. |
| R1.3.2 | Missing theoretical bridge | P1 | ACCEPT | Proposition 1 supplies the mechanism (linear aggregation + bilinearity); Section 2 links Epps/diffusion and Forbes–Rigobon to testable predictions. |
| R1.3.3 | No hypotheses | P0 | ACCEPT | New Section 2.5 "Hypothesis development": H1–H5, each mapped to a test, significance level and table; summary table of outcomes (Supported / Not supported). |
| R1.4 | Literature review descriptive | P1 | ACCEPT | Rewritten as analytical synthesis (findings compared, controversies, limitations) + comparison table. New verified 2021–2026 references. |
| R1.5.1 | Small asset universe | P2 | PARTIAL | Index-level design is the object of study (three nested indices); external validity limited — stated in Limitations. |
| R1.5.2 | Survivorship bias | P2 | ACCEPT | Exchange-computed index levels embed delistings and reconstitutions; stated in Data. |
| R1.5.3 | Data source | P1 | ACCEPT | Vendor, exchange codes, frequencies, sample dates, export procedure, filled-vs-raw check (R1) described. |
| R1.6.1 | Notation consistency | P1 | ACCEPT | Notation table-free harmonisation: one symbol per object; vectors none; all display equations numbered. |
| R1.6.2 | Parameter choice after seeing results (selection bias) | P1 | ACCEPT (analogue) | Analogue here: w30 fixed from the exchange factsheet before analysis; reliability threshold fixed ex ante; hypotheses and tests listed before results. Sensitivity grids reported (weight, block length). |
| R1.6.3 | Optimisation not derived | — | N/A | No optimisation problem; the closest analogue (Markowitz variance error) is a closed-form identity, Eq. (17). |
| R1.6.4 | Computational details | P1 | ACCEPT | New subsection: R version, packages, seeds, bootstrap B and block lengths, CPU, run time; replication package. |
| R1.6.5 | Key hyperparameter fixed arbitrarily | P1 | ACCEPT (analogue) | Bootstrap block length 5–60 days (R13); w30 0.60–0.75 (Table 7); detrending order 1–3. |
| R1.7.1 | Inappropriate test (paired t on Sharpe) | — | N/A | No Sharpe ratios; inference already by stationary block bootstrap. |
| R1.7.2 | Inflated t-values from dependent replications | P1 | ACCEPT (analogue) | All inference resamples the data (block bootstrap), not scales or simulations; stated explicitly. |
| R1.7.3 | Confidence intervals, effect sizes | P1 | ACCEPT | 95% CIs for every inferential estimate; Cohen's q for the gap (R10). |
| R1.7.4 | Multiple-comparison correction | P1 | ACCEPT | Holm and Benjamini–Hochberg across the 19 slope tests per range (R9). |
| R1.8a | Results interpretation | P1 | ACCEPT | Each result paragraph states the mechanism. |
| R1.8b | Report turnover, weights, costs | — | N/A | No traded portfolio. |
| R1.8c | Confidence bands on figures | P2 | ACCEPT | Fig. 2 carries pointwise 95% bootstrap bands. |
| R1.9 | More robustness (alternative methods, risk measures) | P1 | PARTIAL | Added DMCA coefficient (alternative multiscale estimator) and lower-tail dependence (tail risk). Clustering/optimisation alternatives N/A. |
| R1.10 | Discussion repeats results | P1 | ACCEPT | Discussion rewritten around mechanisms and implications. |
| R1.11 | Overstated conclusions | P1 | ACCEPT | Conclusions limited to one market, three indices, one decomposition. |
| R1.F1–F3 | Notation, transpose, corrupted equations | P1 | ACCEPT | Equations rebuilt as OMML; authors to verify in Word. |
| R1.F4 | Matrix dimensions | — | N/A | No matrices in the model; scalar series only. |
| R1.F5 | Positive definiteness | P2 | ACCEPT (analogue) | Boundedness |ρ_DCCA| ≤ 1 shown by Cauchy–Schwarz on detrended residuals; F_A, F_M > 0 required. |
| R1.F6 | Numerical stability | P2 | ACCEPT | Discussed: P_heur denominator 1 − w_heur ≈ 0.012 amplifies noise 74–87×; Proposition 1 identity error ≤ 4.4×10⁻¹⁶. |
| R1.C | Verify local Vietnamese references | P1 | ACCEPT | Independent citation audit; every reference needs DOI or stable URL; unverifiable items removed. |

## C. User-imposed requirements (prompt, Iter 24)
- New verified references 2021–2026; Q1/Q2 outlets preferred (independent agent search + independent audit).
- Independent agents for integrity, full review, re-review and citation audit.
- Target journal deferred by the user → Springer generic format retained; no venue-specific claims.
