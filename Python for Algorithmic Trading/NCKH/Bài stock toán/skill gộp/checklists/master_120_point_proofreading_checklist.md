# Master 120-Point Academic Proofreading & Quality Checklist

> The ultimate pre-submission verification checklist. Every manuscript must be audited against these 120 criteria across 6 core dimensions before submission.

---

## Dimension 1: Introduction, Framing & Narrative Architecture (Items 1–20)

- [ ] 001. Does paragraph 1 state the fundamental research question and hook the reader within the first 3 sentences?
- [ ] 002. Is the "newspaper / triangular style" strictly followed—is the central finding stated in the opening 2 paragraphs?
- [ ] 003. Does the paper possess exactly ONE controlling idea, stated concisely without divergence?
- [ ] 004. Are the stakes clearly established: Why does this economic/scientific question matter?
- [ ] 005. Is the research gap explicitly articulated rather than merely stating "prior literature is limited"?
- [ ] 006. Is the empirical setting and dataset described concretely (sample period, sample size, unit of observation)?
- [ ] 007. Are the central empirical findings reported with concrete numerical coefficients, signs, and standard errors?
- [ ] 008. Is the primary economic mechanism stated plainly in the introduction?
- [ ] 009. Are threats to identification anticipated and the counter-strategy summarized in paragraph 4?
- [ ] 010. Is the contribution framed as a numbered list of 3 (maximum 4) distinct, non-overlapping items?
- [ ] 011. Does the contribution clearly differentiate the paper from the 3–5 most closely related touchstone studies?
- [ ] 012. Is the "Introduction-Twice" rule satisfied: Was the final introduction rewritten after empirical results were locked down?
- [ ] 013. Does every claim promised in the introduction map 1-to-1 to an actual table or figure in the text?
- [ ] 014. Are section headings written as "So-What" claim headings rather than descriptive topic labels?
- [ ] 015. Is there a concise 2-sentence roadmap paragraph at the end of the introduction?
- [ ] 016. Is the title concise, informative, and either an assertion or an engaging question?
- [ ] 017. Is the abstract between 100 and 150 words and strictly structured (Question, Setting, Finding, Implication)?
- [ ] 018. Does the abstract contain ZERO citations?
- [ ] 019. Does the abstract contain ZERO undefined abbreviations?
- [ ] 020. Does the abstract report concrete numbers and avoid vague promises ("we analyze and discuss...")?

---

## Dimension 2: Econometric & Methodological Rigor (Items 21–45)

- [ ] 021. Is the source of exogenous variation or quasi-experimental shock explicitly identified?
- [ ] 022. Is the counterfactual clearly described (what would have happened without the shock)?
- [ ] 023. If using DiD, is a dynamic event study plot included showing pre-treatment leads?
- [ ] 024. Are pre-treatment leads statistically indistinguishable from zero ($p > 0.10$)?
- [ ] 025. If using staggered DiD, are heterogeneity-robust estimators (Callaway-Sant'Anna, Sun-Abraham) employed?
- [ ] 026. If using IV, is the first-stage regression explicitly reported with the first-stage $F$-statistic?
- [ ] 027. Does the first-stage $F$-statistic exceed the rule of thumb ($F > 10$) or Montiel Olea-Pflueger critical thresholds?
- [ ] 028. Is the exclusion restriction qualitatively defended through institutional knowledge and ruling out direct channels?
- [ ] 029. Is the Local Average Treatment Effect (LATE) complier sub-population explicitly characterized?
- [ ] 030. If using RDD, is the McCrary or Cattaneo-Jansson-Ma manipulation/density test reported?
- [ ] 031. Are optimal data-driven bandwidths (CCT or IK) utilized and plotted with sensitivity to bandwidth choice?
- [ ] 032. Is covariate balance verified at the discontinuity cutoff?
- [ ] 033. Are standard errors clustered at the appropriate level where treatment is assigned?
- [ ] 034. If clusters are fewer than 40, is the wild cluster bootstrap implemented?
- [ ] 035. Are unit fixed effects and time fixed effects clearly specified in the regression equations?
- [ ] 036. Are controls selected thoughtfully to avoid bad controls (conditioning on colliders/post-treatment variables)?
- [ ] 037. Is an Oster (2019) bound for selection on unobservables computed and reported ($\delta > 1$)?
- [ ] 038. Are placebo/falsification tests conducted using fictitious treatment dates or unaffected asset groups?
- [ ] 039. Are results robust to trimming or winsorizing extreme outliers at the 1% and 99% levels?
- [ ] 040. Are alternative econometric estimators compared (e.g., OLS vs FE vs GMM vs Quantile)?
- [ ] 041. Are sample attrition and filtering steps completely documented in a sequential ledger?
- [ ] 042. Is economic significance explicitly distinguished from statistical significance throughout the text?
- [ ] 043. Are coefficients translated into 1-SD shifts and real-world metrics (basis points, percentages, dollars)?
- [ ] 044. Are competing economic mechanisms evaluated in a formal "horse race"?
- [ ] 045. Are null results reported transparently without defensive rationalization or p-hacking?

---

## Dimension 3: Mathematical Notation & Equation Formatting (Items 46–65)

- [ ] 046. Are scalars formatted in math italics ($x, y, \beta$)?
- [ ] 047. Are vectors formatted in bold lowercase ($\mathbf{x}, \boldsymbol{\beta}$)?
- [ ] 048. Are matrices formatted in bold uppercase ($\mathbf{X}, \boldsymbol{\Sigma}$)?
- [ ] 049. Are sets and spaces formatted in blackboard bold or calligraphic ($\mathbb{R}, \mathcal{S}$)?
- [ ] 050. Are operator names formatted as Roman text (`\max`, `\min`, `\arg\min`, `\sup`), never math italics ($max$)?
- [ ] 051. Is expectation formatted using `\mathbb{E}[\cdot]`, not $E[\cdot]$?
- [ ] 052. Are variance and covariance operators formatted as `\mathrm{Var}(\cdot)` and `\mathrm{Cov}(\cdot)`?
- [ ] 053. Does every displayed equation end with appropriate punctuation (period or comma)?
- [ ] 054. Is the word "where" following an equation lowercase unless preceded by a full stop?
- [ ] 055. Is every variable and subscript defined in the text immediately following the equation?
- [ ] 056. Are subscripts and superscripts applied consistently throughout all sections without notation drift?
- [ ] 057. Are multi-line equation splits aligned properly using `align` or `split` environments?
- [ ] 058. Are parentheses and brackets properly sized using `\left(` and `\right)` or `\bigl(` and `\bigr)`?
- [ ] 059. Are equations cross-referenced using `\eqref{...}` or `Equation~(\ref{...})`?
- [ ] 060. Are all mathematical definitions and lemmas numbered sequentially?
- [ ] 061. Is economic intuition provided before every formal proposition or theorem?
- [ ] 062. Are long algebraic proofs relegated to the Mathematical Appendix?
- [ ] 063. Are comparative statics signs derived explicitly and connected to empirical testable hypotheses?
- [ ] 064. Are equilibrium concepts formally defined before presenting solutions?
- [ ] 065. Are dimensionalities of all matrix multiplications verified and algebraically valid?

---

## Dimension 4: Tables, Figures & Visual Standards (Items 66–85)

- [ ] 066. Are all tables formatted using `booktabs` (`\toprule`, `\midrule`, `\bottomrule`)?
- [ ] 067. Are vertical lines (`|`) STRICTLY ABSENT from all tables?
- [ ] 068. Does every table have a self-contained note explaining sample, estimator, and clustered SEs?
- [ ] 069. Are standard errors reported in parentheses directly below point estimates?
- [ ] 070. Are significance stars explicitly defined in table notes: `* p < 0.10, ** p < 0.05, *** p < 0.01`?
- [ ] 071. Are column headers descriptive, indicating the dependent variable in each column?
- [ ] 072. Are fixed effects and control variable sets indicated with clean "Yes/No" rows?
- [ ] 073. Are observation counts ($N$) and goodness-of-fit statistics ($R^2$, pseudo-$R^2$) reported for all columns?
- [ ] 074. Are first-stage diagnostic test statistics ($F$-stat, Hansen $J$) reported in IV tables?
- [ ] 075. Are table columns aligned on decimal points using `dcolumn` or `siunitx`?
- [ ] 076. Does the paper feature an informative Figure 1 on page 1 or 2 summarizing architecture/findings?
- [ ] 077. Are all figures provided as vector graphics (`.pdf`, `.eps`, `.svg`, `TikZ`), never blurry bitmaps?
- [ ] 078. Does every figure have a 3-part self-contained caption (Title, Key Takeaway, Data/Method)?
- [ ] 079. Are color palettes colorblind-safe (Okabe-Ito, Viridis, Cividis)?
- [ ] 080. Are line plots distinguishable in black-and-white (using varied dashed styles and markers)?
- [ ] 081. Do all figure axes have clear labels with units of measurement?
- [ ] 082. Are font sizes in figures readable and comparable to the body text size at 100% scale?
- [ ] 083. Are confidence interval bands (95% CI) clearly plotted and explained in regression plots?
- [ ] 084. Are figures and tables cited in the body text in numerical sequential order?
- [ ] 085. Is every table and figure referenced with a non-breaking space: `Table~\ref{...}`, `Figure~\ref{...}`?

---

## Dimension 5: Mechanical & Anti-AI Slop Gate (Items 86–105)

- [ ] 086. Are ALL em-dashes (`---`, `—`, `–` used as punctuation) strictly removed?
- [ ] 087. Is the word `delve` or `delve into` completely eliminated?
- [ ] 088. Is the phrase `testament to` completely eliminated?
- [ ] 089. Are words `underscores` and `underpins` replaced with active verbs (*shows, indicates*)?
- [ ] 090. Are words `pivotal` and `paramount` replaced with grounded terms (*key, central*)?
- [ ] 091. Are poetic metaphors (`beacon`, `tapestry`, `kaleidoscope`, `realm`) banned?
- [ ] 092. Are vague buzzwords (`multifaceted`, `nuanced understanding`, `interplay`, `vibrant`) eliminated?
- [ ] 093. Is the verb `utilize` replaced everywhere with `use`?
- [ ] 094. Is the verb `leverage` replaced with `use` or `exploit`?
- [ ] 095. Are promotional closing sentences at paragraph ends deleted?
- [ ] 096. Are throat-clearing openers (`Moreover`, `Furthermore`, `Notably`, `Importantly`, `Indeed`) stripped?
- [ ] 097. Are vacuous intensifiers (`at its core`, `in essence`, `truly`, `seamlessly`) removed?
- [ ] 098. Are triadic parallel lists of synonyms (rule-of-three padding) broken up?
- [ ] 099. Is passive voice usage strictly below 15% across the entire draft?
- [ ] 100. Are smothered verbs / nominalizations replaced with active verbal roots?
- [ ] 101. Is sentence cadence varied: short claims (6–12 words) followed by analytical explanations?
- [ ] 102. Are generic adjectives (`significant`, `substantial`, `impressive`, `novel`) replaced with exact metrics?
- [ ] 103. Are en-dashes (`--`) used for all numerical ranges (e.g., `pp.~12--25`, `2018--2024`)?
- [ ] 104. Is the Oxford comma applied consistently throughout the entire manuscript?
- [ ] 105. Has the automated regex grep suite returned zero forbidden tokens?

---

## Dimension 6: Semantic Followability, Integrity & Citations (Items 106–120)

- [ ] 106. Is every technical term and acronym defined at its first appearance before argumentative use?
- [ ] 107. Is the definition-before-use rule applied recursively down to every sentence?
- [ ] 108. Are terms glossed plainly once, with zero repetitive tutorial reminders in later sections?
- [ ] 109. Does every single technical assertion have either a citation, an empirical table, or a proof?
- [ ] 110. Are all cited papers verified against real, verifiable sources (zero hallucinated citations)?
- [ ] 111. Are author names, publication years, and journal titles in the bibliography 100% accurate?
- [ ] 112. Are non-breaking spaces used before citations: `\cite{...}` and `\citet{...}`?
- [ ] 113. Is the literature review synthesized by theme rather than a serial laundry list of book reports?
- [ ] 114. Are causal claims strictly calibrated to what the identification strategy legitimately proves?
- [ ] 115. Does the manuscript avoid claiming that empirical data "proves" a theoretical model?
- [ ] 116. Are sample limitations and institutional boundary conditions stated frankly in the discussion?
- [ ] 117. Does the conclusion provide actionable policy/practical takeaways without fluff?
- [ ] 118. Does the conclusion avoid verbatim copying of the abstract and introduction?
- [ ] 119. Has the paper been subjected to an independent Red-Team adversarial audit?
- [ ] 120. Is the entire LaTeX document compiling cleanly with zero undefined references or missing citations?
