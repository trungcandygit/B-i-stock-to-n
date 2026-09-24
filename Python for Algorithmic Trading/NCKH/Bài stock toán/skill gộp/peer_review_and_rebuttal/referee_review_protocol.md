# Peer Review & Referee Evaluation Protocol (Top-5 Rigor)

> Evaluate manuscripts with the unforgiving methodological rigor of an AER, QJE, JFE, or Review of Financial Studies referee.
> Reconstruct before judging; categorize concerns into critical dealbreakers versus constructive refinements.

---

## 1. The 4-Stage Referee Evaluation Workflow

```
Stage 0: Boundary & Claim Reconstruction (What does the paper actually claim?)
   │
   ▼
Stage 1: Identification & Empirical Stress Test (Can the empirical design support the claims?)
   │
   ▼
Stage 2: Adjudication & Findings Ledger (Categorize into Critical vs Major vs Minor)
   │
   ▼
Stage 3: Grounded Referee Report & Revision Roadmap (Clear, actionable, fair)
```

---

## 2. The Methodological Stress Test (Referee Checklist)

### 1. The Identification Audit (Dealbreaker Zone)
- **Source of Exogeneity**: Is the shock truly exogenous, or is it endogenous to unobserved firm choices / market conditions?
- **Bad Controls**: Are the authors controlling for intermediate variables that are themselves affected by the treatment (collider bias / controlling away the mechanism)?
- **Omitted Variables**: Does an obvious macroeconomic, sectoral, or seasonal trend explain both $X$ and $Y$?
- **DiD Violations**: Do pre-treatment event study leads show a pre-existing trend? Is there staggered treatment timing with negative weights?
- **Instrument Validity**:
  - Does the first-stage $F$-statistic exceed safe thresholds ($F > 10$ or $KP > 104.7$)?
  - Is the exclusion restriction plausible, or does $Z$ have an obvious direct channel to $Y$?
- **RDD Integrity**: Is there evidence of sorting around the cutoff threshold in the McCrary density test?

### 2. Standard Error & Inference Audit
- Are standard errors clustered at the appropriate level?
- If clusters are fewer than 40, did the authors use the wild cluster bootstrap?
- Are multiple hypotheses tested without adjusting for family-wise error rates or false discovery rates?

### 3. Economic Magnitude vs. Statistical Artifact
- Does the author confuse statistical significance with economic significance?
- Is the sample so massive that a trivial 0.001% effect generates $p < 0.001$?
- What is the real-world economic importance?

---

## 3. The 3-Tier Findings Ledger

When drafting a referee report or auditing a paper, categorize every critique into three distinct tiers:

### Tier 1: Fatal Flaws / Critical Dealbreakers (Recommend Rejection if Unresolved)
- Flawed identification that cannot be fixed within the existing data or setting.
- Violations of the exclusion restriction that invalidate the central thesis.
- Massive confounding trends that fully account for the result.
- Data fabrication, irreproducible sample selection, or severe mathematical errors in proofs.

### Tier 2: Major Methodological Concerns (Require Revision & Re-estimation)
- Missing key robustness checks (e.g., Oster bounds, alternative clustering, placebo tests).
- Alternative competing mechanisms that have not been tested or ruled out.
- Omission of critical control variables or sub-sample sensitivity checks.
- Overstated causal claims that exceed what the empirical design actually proves.

### Tier 3: Minor Technical & Expositional Issues (Can Be Fixed in Polish)
- Unclear figure captions, missing units on table axes, or LaTeX formatting violations.
- Imprecise mathematical notation or missing equation punctuation.
- Literature omissions of non-critical prior studies.
- Minor typos, passive voice overuse, or em-dash violations.

---

## 4. Standard Referee Report Structure

```markdown
# Referee Report

## 1. Summary of the Paper
[Provide a concise 1–2 paragraph reconstruction of the paper's research question, empirical setting, methodology, and central findings. Demonstrate that you have thoroughly understood what the authors did.]

## 2. Assessment of Contribution & Main Takeaway
[Assess the novelty and value-added relative to the frontier literature. Is the question first-order? Is the setting convincing?]

## 3. Major Comments (The Core Evaluation)
1. **Identification Strategy & Endogeneity**: [Detailed, line-referenced critique of the causal claim, accompanied by a specific suggested test or resolution].
2. **Alternative Mechanisms**: [Point out plausible alternative explanations and suggest how data can distinguish between them].
3. **Robustness & Sample Sensitivity**: [Point out necessary sensitivity checks].

## 4. Minor Comments & Expositional Suggestions
- Page 4, Eq (2): Variable $\epsilon_{it}$ is not defined.
- Page 12, Table 3: Clustered standard errors should be clarified in table notes.
- Page 18: Rephrase causal claim into conditional correlation.
```
