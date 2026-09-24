# Semantic & Logical Consistency Gate (Reader-Judgment Audit)

> The non-greppable criteria that determine whether referee reports recommend Acceptance or Rejection.
> Assesses clarity of definitions, argument hierarchy, evidence anchoring, and epistemic honesty.

---

## 1. Core Structural Integrity Checks

### S1. Define Before Use (Non-Negotiable)
- Every specialized mathematical symbol, acronym, economic variable, or coined construct MUST be clearly defined at its first appearance in the text.
- Never use a variable in an equation without defining its economic meaning and unit of measurement immediately following the equation.
- Acronyms: Write out the full name at the first instance, followed by the abbreviation in parentheses: e.g., *Generalized Autoregressive Conditional Heteroskedasticity (GARCH)*.

### S2. Strict Concept Hierarchy (Abstraction → Specification → Estimation)
In explaining models and empirical strategies:
1. First, establish the high-level intuition and economic mechanism.
2. Second, state the formal mathematical representation.
3. Third, map the theoretical objects directly to observable empirical proxies in the data.
*Failure Mode*: Presenting an empirical regression equation with five indices ($i, j, k, s, t$) before the reader understands the basic economic decision being modeled.

### S3. Recursive Followability Test
Apply the single recursive question at every level of the paper (Section → Subsection → Paragraph → Sentence):
> *"Given ONLY what has been presented up to this exact line, can an educated reader understand and follow the argument?"*
- Flag forward references to undefined terms ("As we show in Table 8..." on page 3 is acceptable only for previewing main results, not for defining the identification strategy).
- Eliminate unresolvable pronouns ("This phenomenon leads to..." where "This" could refer to three different preceding concepts).

### S4. Gloss Once, Plainly, Then Stop
- Explain each concept clearly once at its introduction.
- Do NOT re-explain or re-gloss textbook concepts in later sections. Continuous tutorial reminders insult the referee's intelligence and dilute paper density.
- Moving technical parameter descriptions into self-contained table footnotes frees the main prose from repetitive inline glossing.

---

## 2. Evidence-First & Anti-Hallucination Protocol

### S5. Zero Hallucinated Citations & Phantom Literature
- Every citation must correspond to a real, verifiable, peer-reviewed paper or working paper.
- Never synthesize or cite non-existent papers.
- Check author names, publication years, and journal titles against Google Scholar, CrossRef, or Semantic Scholar before finalizing the bibliography.
- Accurately represent cited work: Never claim paper X found Y when paper X actually found Z or held only under specific boundary conditions.

### S6. Grounded Assertions (No Unsupported Declarations)
Every single factual or technical assertion in the manuscript must fall into one of three verified categories:
1. **Direct Empirical Evidence**: Directly supported by a specific coefficient, standard error, test statistic, or figure generated from your sample (e.g., "As reported in Table 2, Column 3...").
2. **Prior Literature Grounding**: Supported by an exact literature reference (e.g., "Consistent with Campbell and Shiller (1988), ...").
3. **Formal Mathematical Derivation**: Supported by a proof in the text or appendix.
*Rule*: Any sentence that makes an empirical claim without a citation, a table reference, or a proof is an ungrounded assertion and must be rewritten or removed.

### S7. Single Controlling Thesis & Anti-Drift
- Identify the paper's single controlling thesis in a fixed 3–5 word phrase (e.g., *Regime-dependent liquidity contagion*).
- Trace every empirical table and subsection back to this thesis.
- If a section explores a tangent that does not directly test or qualify this controlling thesis, move it to the Online Appendix or cut it entirely.

---

## 3. Epistemic Calibrated Honesty

### S8. Causal Language Discipline (Bellemare & Cochrane Rules)
- **Do NOT use causal verbs unless identification is bulletproof**:
  - If your identification relies on observational correlations with fixed effects, use *associated with*, *correlated with*, *predicts*, *tracks*.
  - Use causal verbs (*causes*, *leads to*, *drives*, *induces*, *generates*) ONLY when you have a randomized controlled trial, a validated natural experiment, an uncontroversial instrument passing all exclusion restrictions, or a sharp regression discontinuity.
- Never write that a model "proves" a hypothesis. In empirical science, empirical evidence *supports*, *is consistent with*, or *fails to reject* a hypothesis.

### S9. Honest Boundary Conditions & External Validity
- Explicitly state where your empirical results hold and where they may not generalize:
  - Time periods (e.g., "Our sample covers normal market conditions and does not span severe sovereign debt crises.").
  - Institutional context (e.g., "These results apply to emerging frontier markets with T+2 settlement cycles and may differ under real-time gross settlement regimes.").
  - Acknowledging limitations demonstrates maturity and disarms referee attacks.
