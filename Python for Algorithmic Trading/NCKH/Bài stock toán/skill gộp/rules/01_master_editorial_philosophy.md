# Master Editorial Philosophy & Author Voice

> Synthesizing authoritative principles from 50+ economics paper writing masters (John Cochrane, Jesse Shapiro, Claudia Goldin, Marc Bellemare, Deirdre McCloskey, Keith Head) and systems/empirical paper revision methodologies (Arpit Gupta, SNL Lab).

---

## 1. Core Writing Axioms

### Rule 1: Reader First (Respect the Reader's Scarcity)
Most readers—including referees—are busy, tired, skeptical, and will skim.
- Keep track of what your reader knows and does not know at every point.
- Write for general PhD economists and empirical scientists who are NOT specialists in your sub-niche.
- Make it effortless for them to extract your main finding within 3 minutes of opening the paper.

### Rule 2: Triangular / Newspaper Style
Lead with the punchline. Put the most important conclusion FIRST, then provide the supporting evidence and details.
- **Never write in "mystery novel" or "joke" style** where the core finding is revealed at the end of the paper or section.
- If your paper finds that tariff shocks reduce manufacturing employment by 4.2%, state that in paragraph 1 of the introduction and paragraph 1 of the results section.

### Rule 3: One Central, Novel Contribution
Every paper must possess exactly ONE controlling idea / central contribution.
- If you cannot state your core contribution in a single concise sentence, you have not figured it out yet.
- Every paragraph, table, equation, and figure must directly serve this single controlling idea. If a section or paragraph does not advance it, eliminate it.

### Rule 4: Concrete Over Abstract (Say What You Find)
State what you **find**, not what you **look for**.
- ✗ *Weak*: "We examine the relationship between corporate governance and debt financing and present interesting empirical results."
- ✓ *Strong*: "Firms with staggered boards pay 28 basis points higher loan spreads (SE = 6.2), driven by heightened lender risk aversion during rollover periods."
- For theoretical models: State the economic mechanism and comparative statics immediately, not just "we develop a dynamic model."

### Rule 5: Economy of Words & Compression Arc
"Most paragraphs have too many sentences, and most sentences have too many words." (Goldin & Katz).
- Target length: Standard empirical papers should be 35–45 pages (double-spaced, including tables and figures). Shorter is stronger.
- Follow the **Expansion-Compression Arc**:
  1. *Draft 0*: Expand comprehensively to get all institutional details, models, and empirical tests down.
  2. *Refactor*: Impose structural narrative contracts and problem-first framing.
  3. *Late-Stage Compression*: Ruthlessly cut 25–40% of words. Delete tutorial material, generic throat-clearing, and redundant qualifiers.

### Rule 6: Active Voice & Present Tense
- Use active voice: "We estimate..." rather than "It is estimated by the authors that..."
- Passive voice threshold: Keep passive voice strictly under 15% across the entire manuscript.
- Use present tense for your findings and cited papers: "Acemoglu et al. (2001) find..." and "Table 4 shows that..."

### Rule 7: Simple Language > Decorative Obscurantism
- "Use", not "utilize".
- "Many", not "a myriad of".
- "Before", not "prior to the inception of".
- Never use complex terminology or excessive mathematical formalism to disguise weak empirical identification or lack of novelty. Referees see through decorative prose instantly.

---

## 2. The 14 Editorial Principles (Empirical & Systems Writing)

### Principle 1: Introduction-Twice (Draft 0 → Empirical Completion → Final Intro)
Write the introduction twice:
- **Draft 0**: Written early to set guardrails and clarify the hypothesis before finalizing estimations. It is explicitly disposable.
- **Final Introduction**: Written from scratch AFTER all empirical results, robustness tests, and mechanism checks are locked down. Every single claim in the final introduction must map 1-to-1 to a concrete table or subsection.

### Principle 2: Named Over Vague
Eliminate all generic non-information words ("significant", "substantial", "promising", "novel").
- Replace generic descriptions with proper names and exact numerical magnitudes:
  - ✗ "Our model delivers substantial accuracy improvements."
  - ✓ "The regime-switching DCCA specification lowers forecast mean squared error by 31.4% relative to standard GARCH(1,1)."

### Principle 3: What → Why → So-What Heading Progression
Headings must evolve from topic names to claim assertions:
1. *Topic Heading (Weak)*: "Empirical Results"
2. *Why Heading (Better)*: "Why Standard OLS Underestimates Volatility Spillover"
3. *So-What Heading (Master)*: "Cross-Market Correlation Spikes 42% During Liquidity Shocks"
Referees skimming only the table of contents and headings should absorb the entire narrative argument.

### Principle 4: Labeled Paragraphs as Narrative Contracts
Lead each major analytical paragraph with an explicit takeaway or italicized lead-in:
- Example: *"Liquidity channel explains the divergence."* followed immediately by the empirical evidence.
- This creates an implicit contract: every subsequent sentence in that paragraph must support that specific lead assertion.

### Principle 5: Structural Rewrites Over Incremental Polishing
If a section is muddy or confusing, do not attempt sentence-level cosmetic edits. Strip back to the core finding, clarify the economic mechanism, and rewrite the section from scratch.

### Principle 6: Problem-First, Not Method-First
Never lead with the econometric or machine learning tool:
- ✗ "In this paper, we apply a double-machine-learning LASSO framework to financial time series..."
- ✓ "Estimating the causal impact of institutional trading on price discovery is confounded by high-frequency endogeneity. We isolate this shock using..."

### Principle 7: Takeaway Paragraphs & Skim-Friendly Cues
At the conclusion of each empirical subsection, provide a 2–3 sentence takeaway paragraph summarizing:
1. The parameter estimate and its economic magnitude.
2. The economic mechanism validated or rejected.
3. The bridge to the next empirical question.

### Principle 8: Dual Evaluation for Dual Claims
If you claim your methodology is both *more accurate* and *computationally efficient*, your empirical evaluation must feature two distinct, balanced experimental designs—one dedicated strictly to accuracy, one to computational overhead.

### Principle 9: Technical Claims Require Direct Grounding
Every technical statement or assumption must be accompanied by either:
1. A direct citation to existing peer-reviewed literature (`\cite{...}`).
2. A formal mathematical proof in the text or appendix.
3. Direct empirical validation from your estimation sample.
Uncited assertions read as unsubstantiated speculation to referees.

### Principle 10: Rejection Drives Abstraction
When revising after a rejection or critical referee report, do not merely patch the specific complaints. Ask: *"Did the paper claim to do X while delivering Y?"* Reframe the paper at a higher level of conceptual clarity to align the stated identity with the delivered evidence.

### Principle 11: Raw Data Before Complex Regressions
Before presenting IV, DiD, or structural estimations, present the raw data:
- Plot the raw time series, the distribution histograms, the scatter plot with local polynomial smoothing, and the raw group means.
- If the effect is not visible or suggestive in the raw descriptive data, reviewers will be deeply skeptical of sophisticated econometric machinery.

### Principle 12: Economic Significance vs Statistical Significance
Never confuse a tiny p-value with an economically meaningful finding:
- Always translate regression coefficients into real-world units: standard deviation shifts, percentage changes, dollar amounts, or basis points.
- A coefficient that is statistically significant at the 0.1% level but corresponds to a 0.001% change in firm value is economically trivial.

### Principle 13: Honest Boundary Conditions (Limitations)
State your paper's limitations clearly and non-defensively in the Discussion section:
- Define the exact population and institutional environment where your results hold.
- Distinguish between internal validity (established within your sample) and external validity (generality to other markets, time periods, or institutional frameworks).

### Principle 14: The Division of Labor in Drafting
- Stage 1: Fast, unconstrained drafting of empirical facts.
- Stage 2: Structural restructuring (re-ordering, imposing problem-first logic).
- Stage 3: Aggressive compression and anti-AI sanitization.
- Stage 4: Micro-proofreading (LaTeX tables, math notation, citations).
