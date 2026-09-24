# Section Playbook 7: Robustness Checks & Threats to Validity

> The armor of the empirical manuscript. Anticipate and preempt every referee objection before it is raised.
> Synthesizes top referee audit protocols, Oster (2019) sensitivity analysis, and placebo design.

---

## 1. Threats to Internal Validity & Preemptive Neutralization

Referees will invariably interrogate four potential threats. Address each systematically in Section 5:

| Threat to Validity | Referee Suspicion | Econometric Solution & Preemption |
| :--- | :--- | :--- |
| **Omitted Variable Bias** | "An unobserved shock correlates with both $X$ and $Y$." | Oster (2019) coefficient stability bounds; High-dimensional granular fixed effects (e.g., industry-by-year). |
| **Reverse Causality** | "$Y$ actually drives $X$, or both anticipate future shocks." | Pre-trends event study ($t-k$ coefficients = 0); Lagged regressors; Instrumental Variables (2SLS). |
| **Outliers & Tail Events** | "The entire result is driven by two market crash days or three mega-cap firms." | Winsorization at 1% and 5%; Leave-one-out cross-validation; Dropping crisis sub-periods. |
| **Model Misspecification** | "The linear functional form is arbitrary." | Non-parametric bin scatters; Quantile regressions; Machine-learning double/debiased estimation. |

---

## 2. The Standard Robustness Table Architecture

Present robustness checks in a consolidated, clean table (Table 6 or Table 7) comparing the alternative estimates against the baseline benchmark:

```latex
\begin{table}[htbp]
\centering
\caption{Robustness Checks and Sensitivity Analysis}
\label{tab:robustness}
\begin{threeparttable}
\begin{tabular}{lcccc}
\toprule
Specification Variant & Coeff ($\beta$) & Std. Err. & $N$ & $R^2$ \\
\midrule
\textbf{Baseline Benchmark} & \textbf{0.218***} & \textbf{(0.045)} & \textbf{42,150} & \textbf{0.285} \\
\addlinespace
\textit{Panel A: Alternative Sample Restrictions} \\
(1) Excluding Top 5 Mega-Cap Stocks & 0.204*** & (0.048) & 35,125 & 0.271 \\
(2) Excluding COVID-19 Period (2020) & 0.195*** & (0.051) & 36,120 & 0.264 \\
(3) Winsorizing at 1\% and 99\% Levels & 0.229*** & (0.042) & 42,150 & 0.298 \\
\addlinespace
\textit{Panel B: Alternative Econometric Estimators} \\
(4) Dynamic Panel GMM (Arellano-Bond) & 0.231*** & (0.058) & 39,210 & -- \\
(5) High-Dimensional Industry $\times$ Month FE & 0.187*** & (0.049) & 42,150 & 0.354 \\
(6) Wild Cluster Bootstrap ($p$-value) & [0.218] & [$p=0.002$] & 42,150 & 0.285 \\
\addlinespace
\textit{Panel C: Placebo / Falsification Tests} \\
(7) Fictitious Treatment Date ($t-1$ Year) & 0.012 & (0.038) & 42,150 & 0.112 \\
(8) Placebo Non-Treated Control Asset & -0.008 & (0.041) & 18,400 & 0.095 \\
\bottomrule
\end{tabular}
\begin{tablenotes}[flushleft]
\small
\item \textit{Notes}: This table reports robustness tests for the primary coefficient $\beta$. Panel A applies alternative sample exclusion criteria. Panel B implements alternative estimation algorithms and clustering methods. Panel C conducts falsification tests using fictitious event dates and unaffected asset classes. Standard errors clustered at the firm level are in parentheses. *** denotes significance at the 1\% level.
\end{tablenotes}
\end{threeparttable}
\end{table}
```

---

## 3. The Oster (2019) Bounding Protocol

When evaluating sensitivity to omitted unobservable confounders:
- Report the proportional selection coefficient $\delta$ that would produce a true treatment effect of zero, assuming maximum explanatory power $R_{\max} = 1.3 \times \tilde{R}^2$.
- If $\delta > 1$, selection on unobservables would need to be stronger than selection on all observable controls combined to invalidate the finding—a standard indicating high empirical robustness in top journals.
