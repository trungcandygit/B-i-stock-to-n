# Section Playbook 6: Empirical Results & Economic Mechanisms

> The core intellectual value of the paper. Moves from baseline documentation to causal mechanisms.
> Synthesizes Cochrane's results rules, Bellemare's economic significance guidelines, and mechanism validation.

---

## 1. Presenting the Baseline Results

### Rule 1: Stepwise Specification Progression
Never dump a single regression column. Present a logical progression of columns in Table 2:
- **Column (1)**: Univariate regression of $Y$ on $X$ without controls or fixed effects (raw correlation benchmark).
- **Column (2)**: Add unit fixed effects ($\alpha_i$).
- **Column (3)**: Add time fixed effects ($\lambda_t$).
- **Column (4)**: Add time-varying firm-level controls ($\mathbf{X}_{it}$).
- **Column (5)**: Preferred benchmark specification (e.g., industry $\times$ year fixed effects or IV estimator).
*Why*: Showing stability of the coefficient $\hat{\beta}$ across columns demonstrates that the effect is not sensitive to control selection or unobserved group trends.

### Rule 2: Economic Significance Translation (Mandatory)
Every discussion of an empirical coefficient must include a 3-part quantitative translation:
1. **The Statistical Metric**: Point estimate, standard error, and $p$-value / $t$-statistic.
2. **The 1-SD Translation**: What does a one standard deviation increase in $X$ do to $Y$ in terms of $Y$'s sample standard deviation?
3. **The Real-World Metric**: Translate the coefficient into basis points, dollars, percentage points, or hours.
   - *Example*: *"The point estimate of $\hat{\beta} = 0.245$ (SE = 0.042, $p < 0.001$) indicates that a one standard deviation increase in liquidity shock (0.18) leads to a 0.044 increase in cross-asset correlation. Relative to the sample mean correlation of 0.32, this represents a 13.8% surge in co-movement, requiring an institutional portfolio manager to rebalance an estimated $14.5 million in index futures to maintain target delta neutrality."*

---

## 2. Uncovering the Economic Mechanism

Reviewers do not just want to know *that* $X$ affects $Y$; they demand to know *why* (the transmission channel).

### The "Horse Race" between Competing Mechanisms
Identify the two or three competing theoretical channels that could explain the baseline finding:
- **Channel A (Liquidity Hoarding)**: Intermediaries withdraw liquidity to satisfy capital buffers.
- **Channel B (Information Discovery)**: Asset prices co-move because macroeconomic news updates fundamental cash-flow expectations simultaneously.
- **Channel C (Investor Sentiment)**: Noise traders induce irrational sentiment contagion.

### How to Test Mechanisms Econometrically
1. **Triple-Difference ($\text{DDD}$) / Heterogeneity Splits**:
   - If Channel A is true, the effect should be concentrated among financially constrained firms or during high-volatility trading hours.
   - Interact the shock with firm-level leverage, cash reserves, or institutional ownership:
     $$Y_{it} = \alpha_i + \lambda_t + \beta_1 \text{Shock}_{it} + \beta_2 (\text{Shock}_{it} \times \text{Constrained}_i) + \dots$$
   - If $\beta_2 > 0$ and statistically significant, it directly confirms Channel A.
2. **Mediating Regressions**:
   - Directly estimate whether the shock affects the hypothesized intermediate variable (e.g., bid-ask spread, order imbalance, funding costs).
3. **Sub-Sample Splits**:
   - Estimate the baseline model separately for Large vs Small caps, State-Owned Enterprises (SOEs) vs Private firms, or Pre-Crisis vs Post-Crisis periods.

---

## 3. Reporting Null and Inconclusive Findings

- Referees respect intellectual honesty. If an interaction term or secondary specification yields a null result, state it clearly:
  - *"In contrast to the predictions of behavioral sentiment models, Column 4 reveals no statistically significant interaction between retail sentiment and correlation spikes ($\hat{\gamma} = -0.012$, SE = 0.035). We therefore fail to reject the null hypothesis of rational liquidity contagion."*
- Never hide, distort, or p-hack away a null result. A well-identified null finding that contradicts conventional wisdom is often a major publication contribution.
