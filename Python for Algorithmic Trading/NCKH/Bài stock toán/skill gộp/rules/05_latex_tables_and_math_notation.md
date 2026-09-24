# LaTeX Tables, Mathematical Notation & Typography Standards

> Formatted to meet the exact publication standards of top journals (AER, QJE, JFE, Review of Financial Studies, Econometrica, Management Science).
> Synthesized from Jakob Thumm's academic proofreading checklist and Cochrane's table guidelines.

---

## 1. LaTeX Table Architecture & `booktabs` Standards

### Rule 1: Zero Vertical Lines (Strict Ban)
- Never use vertical lines (`|`) in any academic table. They clutter the visual field and violate all journal typography guidelines.
- Use the standard `booktabs` package commands:
  - `\toprule`: Heavy horizontal line at the very top.
  - `\midrule`: Light horizontal line separating header from data rows.
  - `\bottomrule`: Heavy horizontal line at the bottom of the table.
  - `\cmidrule(lr){c1-c2}`: Partial horizontal line spanning grouped sub-columns.

### Rule 2: Complete, Self-Contained Table Notes
- A reader should be able to understand the entire table without opening the paper's body text.
- Every table note must state:
  1. The exact dependent variable and unit of measurement.
  2. The sample period and sample restrictions.
  3. The estimation method (e.g., OLS, 2SLS, High-dimensional Fixed Effects).
  4. What is in parentheses below the coefficients (e.g., "Standard errors clustered at the industry level are reported in parentheses").
  5. The definition of significance stars: `* p < 0.10, ** p < 0.05, *** p < 0.01`.
  6. Definitions of all acronyms and key control variables appearing in the table.

### Rule 3: Canonical Regression Table Layout

```latex
\begin{table}[htbp]
\centering
\caption{Impact of Liquidity Shocks on Cross-Asset Correlation}
\label{tab:liquidity_correlation}
\begin{threeparttable}
\begin{tabular}{lcccc}
\toprule
& \multicolumn{4}{c}{Dependent Variable: Dynamic Correlation ($\rho_{it}$)} \\
\cmidrule(lr){2-5}
& (1) & (2) & (3) & (4) \\
\midrule
Liquidity Shock ($\Delta \text{Liq}_{it}$) & 0.245*** & 0.218*** & 0.182** & 0.174** \\
& (0.042) & (0.045) & (0.071) & (0.073) \\
Market Volatility ($\sigma_{mt}$) & & 0.115** & 0.098* & 0.091* \\
& & (0.048) & (0.051) & (0.050) \\
Firm Controls & No & Yes & Yes & Yes \\
Macro Controls & No & No & Yes & Yes \\
\midrule
Firm Fixed Effects & No & Yes & Yes & Yes \\
Year-Month Fixed Effects & No & No & Yes & Yes \\
Estimator & OLS & FE & FE & 2SLS \\
Observations & 42,150 & 42,150 & 42,150 & 42,150 \\
$R^2$ & 0.124 & 0.285 & 0.342 & 0.329 \\
First-stage $F$-statistic & & & & 38.4 \\
\bottomrule
\end{tabular}
\begin{tablenotes}[flushleft]
\small
\item \textit{Notes}: This table reports estimates of the effect of liquidity shocks on dynamic cross-asset correlation. The sample spans all VN30 constituents from January 2018 to December 2024. In Columns (1)–(3), models are estimated via OLS with fixed effects. Column (4) reports two-stage least squares (2SLS) estimates where liquidity shocks are instrumented by exogenous trading halts. Standard errors clustered at the firm level are reported in parentheses. ***, **, and * denote statistical significance at the 1\%, 5\%, and 10\% levels, respectively.
\end{tablenotes}
\end{threeparttable}
\end{table}
```

---

## 2. Mathematical Notation & Typography Rules

### Rule 4: Scalar, Vector, and Matrix Formatting
Maintain rigorous, unwavering mathematical consistency across all equations and text:
- **Scalars**: Italic lowercase letters: $x, y, z, \alpha, \beta, \gamma$.
- **Vectors**: Bold lowercase letters: $\mathbf{x}, \mathbf{y}, \mathbf{z}, \boldsymbol{\beta}, \boldsymbol{\epsilon}$.
- **Matrices**: Bold uppercase letters: $\mathbf{X}, \mathbf{Y}, \mathbf{A}, \boldsymbol{\Sigma}$.
- **Sets and Spaces**: Blackboard bold or calligraphic: $\mathbb{R}^n, \mathcal{S}, \mathcal{F}_t$.
- *Never switch notation mid-paper*: If $x$ is a scalar in Section 2, do not make $\mathbf{x}$ a vector in Section 4 without defining the dimensional expansion.

### Rule 5: Operator Names and Functions
Standard mathematical operators and functions must NEVER be formatted in ordinary math italics, which LaTeX interprets as the product of separate variables ($m \times a \times x$):
- ✗ *Wrong*: $max_{x \in X} f(x)$, $Var(x)$, $Cov(x, y)$, $argmin f(x)$
- ✓ *Right*: `\max_{x \in X} f(x)`, `\mathrm{Var}(x)`, `\mathrm{Cov}(x, y)`, `\arg\min_{x \in X} f(x)`
- Mathematical expectation: Use `\mathbb{E}[\cdot]`, not $E[\cdot]$ or $E( \cdot )$.

### Rule 6: Equation Punctuation
- **Treat displayed equations as an integral part of the sentence**.
- Every displayed equation must end with appropriate punctuation:
  - If the sentence ends after the equation, place a full period (`.`) at the end of the equation.
  - If the sentence continues into the next line (e.g., "where $\epsilon_{it}$ is..."), place a comma (`,`) at the end of the equation.
- Never capitalize the word "where" following an equation unless the equation ended with a full stop.

```latex
% Correct displayed equation with punctuation:
The baseline econometric specification is given by:
\begin{equation}
Y_{it} = \alpha_i + \gamma_t + \beta D_{it} + \mathbf{X}_{it}'\boldsymbol{\Gamma} + \epsilon_{it},
\label{eq:baseline}
\end{equation}
where $Y_{it}$ denotes the excess return of asset $i$ at time $t$, $D_{it}$ is the indicator for treatment, $\mathbf{X}_{it}$ is a vector of time-varying covariates, and $\epsilon_{it}$ is an idiosyncratic error term.
```

---

## 3. Typography, Spacing & Cross-References

### Rule 7: Non-Breaking Spaces (`~`)
Always insert a non-breaking space before citations and cross-references so they do not break awkwardly across lines:
- `Table~\ref{tab:results}` (never `Table \ref{tab:results}`)
- `Figure~\ref{fig:architecture}` (never `Figure \ref{fig:architecture}`)
- `Equation~(\ref{eq:baseline})` or `\eqref{eq:baseline}`
- `Section~\ref{sec:methodology}`
- `\cite{Angrist2008}` or `\citet{Cochrane2005}`

### Rule 8: En-Dashes for Ranges
Use an en-dash (`--`) for numerical and page ranges, never a single hyphen (`-`):
- `pp.~124--148`
- `2018--2024`
- `Columns (1)--(3)`
