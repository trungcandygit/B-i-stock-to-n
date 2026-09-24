# Red-Team Adversarial Audit Protocol

> An adversarial audit designed to break the paper's central claims before external peer reviewers can.
> Operates from a fresh, skeptical, referee-grade mindset with zero author bias.

---

## 1. The Red-Team Mindset

The Red-Team auditor is NOT a helpful co-author seeking to polish prose.
The Red-Team auditor acts as a **hyper-skeptical Top-5 referee** (AER / JFE / Review of Financial Studies) whose primary mission is to stress-test the manuscript for:
1. Implicit, unstated assumptions.
2. Fragile identification strategies masquerading as causal shocks.
3. Survivorship bias or sample selection artifacts.
4. Conflation between statistical significance and economic reality.
5. Over-promising in the introduction that is not matched by the empirical tables.

---

## 2. The 5-Vector Adversarial Attack Protocol

### Attack Vector 1: The "Why Not OLS?" Attack (Identification Integrity)
- *The Attack*: "Why is your complex IV or DiD needed? Does the IV actually satisfy the exclusion restriction, or is it merely picking up general industry trends?"
- *Stress Test*: Demand an explicit institutional explanation of why the instrument has NO direct path to the outcome variable. If the author cannot defend the exclusion restriction without resorting to statistical formulas, flag as **CRITICAL**.

### Attack Vector 2: The "Bad Controls & Mechanism Destruction" Attack
- *The Attack*: "Are the controls included in Column 4 intermediate outcomes affected by the treatment? If so, you are conditioning on a collider and destroying the causal effect."
- *Stress Test*: Inspect every control variable in the baseline regression. If any variable is measured post-treatment or could be influenced by the treatment, require its removal.

### Attack Vector 3: The "Sample Cherry-Picking" Attack
- *The Attack*: "Why does your sample start in 2018? Why did you exclude financials? If you include the financial crisis or penny stocks, does the result disappear?"
- *Stress Test*: Review the data filtering ledger. Demand sub-sample estimations showing that the result holds across different sectors and time windows.

### Attack Vector 4: The "Mechanical AI & Slop" Attack
- *The Attack*: Run the automated grep audit for banned vocabulary, em-dashes, and throat-clearing sentences.
- *Stress Test*: Any occurrence of `delve`, `testament`, `em-dash`, or promotional closers results in an immediate audit failure.

### Attack Vector 5: The "So-What / Economic Triviality" Attack
- *The Attack*: "Your $p$-value is 0.001, but the effect size is a 0.02% change in asset returns. In the presence of bid-ask spreads and transaction costs, this effect cannot be monetized or hedged. Why should anyone care?"
- *Stress Test*: Force the authors to state the economic magnitude in basis points, dollars, or portfolio rebalancing costs.

---

## 3. The Red-Team Audit Report Format

```markdown
# Red-Team Adversarial Audit Report

## 1. Executive Summary & Verdict
- **Verdict**: [REJECT / MAJOR REVISION / ACCEPTABLE WITH MINOR REPAIRS]
- **Core Fatal Vulnerability**: [State the single most dangerous weakness that an external referee will attack].

## 2. Critical Methodological Vulnerabilities (Tier 1)
- **Vulnerability 1**: [Description, line number, why it breaks the causal claim, required fix].
- **Vulnerability 2**: [Alternative mechanism that is currently unaddressed].

## 3. Mechanical & Expositional Violations (Tier 2)
- [Grep hit count for banned AI markers, em-dashes, and passive voice %].

## 4. Required Pre-Submission Action Plan
1. [Action 1: Re-estimate model with alternative clustering].
2. [Action 2: Rewrite Section 4.2 to address the macro news counter-explanation].
3. [Action 3: Run regex anti-slop pass on main.tex].
```
