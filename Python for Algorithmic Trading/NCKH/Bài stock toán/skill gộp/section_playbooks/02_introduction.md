# Section Playbook 2: The Introduction

> The introduction makes or breaks the paper. 80% of referee rejection decisions are mentally formed before reaching Section 2.
> Synthesizes the Bellemare 5-paragraph inverted pyramid, Cochrane's "bottom-line in paragraph 1", and the SNL 5-stage rhetorical moves.

---

## 1. The 5 Rhetorical Moves of an Elite Introduction

```
Move 1: The Hook & Stakes (Why this matters right now)
   │
   ▼
Move 2: The Landscape & Problem (What is known, what is debated)
   │
   ▼
Move 3: The Critical Friction / Research Gap (Why existing tools/theories fail)
   │
   ▼
Move 4: Our Solution, Setting & Concrete Findings (Numbers, signs, mechanisms)
   │
   ▼
Move 5: Explicit Contributions & Value-Added (Bulleted list + roadmap)
```

---

## 2. Paragraph-by-Paragraph Execution Guide

### Paragraph 1: The Hook & Central Question (Move 1)
- Hook the general reader immediately with the core economic phenomenon or tension.
- Do NOT start with the history of the universe ("Since the dawn of financial markets...").
- State the research question and its economic importance in the very first 3 sentences.
- *Template*: *"Understanding how [phenomenon X] influences [outcome Y] is central to [fundamental economic question Z]. When [exogenous shock occurs], traditional theory predicts [outcome A], yet observed market behavior frequently displays [divergent outcome B]. This paper asks: [explicit research question]?"*

### Paragraph 2: What We Do & Our Empirical Setting (Move 4 Part 1)
- Do not make the reader wait 3 pages to find out what you did.
- State your empirical laboratory: the dataset, time period, sample granularity, and the specific exogenous variation or institutional setting exploited.
- *Template*: *"To answer this question, we exploit [source of exogenous variation or unique high-frequency dataset] covering [sample details, N observations, time span 2018–2024]. This setting provides three distinct advantages: first, [institutional feature 1]; second, [quasi-experimental feature 2]; and third, [measurement precision 3]."*

### Paragraph 3: The Main Concrete Findings (Move 4 Part 2)
- State your primary empirical results with exact magnitudes, statistical significance, and economic interpretation.
- Mention the key economic mechanism uncovered.
- *Template*: *"Our main finding is that [X increases Y by magnitude Z (SE = W)]. In economic terms, this corresponds to [real-world translation, e.g., a $4.2M increase in daily hedging cost]. We show that this effect is driven primarily by [Channel 1: liquidity hoarding] rather than [Alternative Channel 2: credit risk reassessment]."*

### Paragraph 4: Identification Defense & Robustness (Move 4 Part 3)
- Anticipate the referee's immediate skepticism regarding endogeneity, omitted variables, or reverse causality.
- Summarize how your identification strategy shuts down these confounders and cite key falsification/placebo tests.
- *Template*: *"A primary concern with this interpretation is [potential endogeneity/reverse causality threat]. We address this through three complementary strategies: [IV / DiD specification / Oster bounding]. Furthermore, placebo estimations using [unaffected asset group / fictitious dates] yield coefficients indistinguishable from zero, confirming that our findings are not artifacts of [confounding trend]."*

### Paragraph 5–6: Explicit Contribution & Value-Added (Move 5)
- State clearly how this paper advances beyond the existing literature.
- Use an explicit numbered or bulleted list of 3 (maximum 4) distinct contributions:
  1. **Empirical Contribution**: First causal documentation of [X] in [setting Y].
  2. **Methodological Contribution**: Overcoming [identification hurdle Z] via [estimator W].
  3. **Theoretical / Policy Contribution**: Reconciling competing predictions of [Model A] versus [Model B].
- Do not cite 30 papers in this section; cite only the 3–5 most closely related touchstone papers and state your exact delta relative to each.

### Paragraph 7: Roadmap (Single Short Paragraph)
- Provide a concise 2-sentence navigational guide to the remainder of the paper:
  - *"The remainder of the paper is organized as follows. Section 2 outlines the institutional background and theoretical framework. Section 3 describes the data and empirical strategy. Section 4 presents the baseline results and mechanism tests. Section 5 reports robustness checks, and Section 6 concludes."*

---

## 3. The "Introduction-Twice" Principle

1. **Draft 0 Introduction**: Written before running final empirical specifications to establish the hypotheses, guardrails, and target claims.
2. **Final Introduction**: Written completely from scratch AFTER all empirical tables, robustness tests, and mechanism checks are finalized.
3. **The 1-to-1 Mapping Test**:
   - Every single claim, number, and mechanism stated in the Final Introduction MUST map directly to a numbered table or figure in Sections 4–5.
   - If an intro promises to examine "cross-market spillovers" but the evaluation never delivers a table estimating spillovers, the paper will be rejected.
