# Section Playbook 4: Theoretical Framework & Model Setup

> Models in applied papers exist to generate falsifiable empirical predictions, not to showcase mathematical acrobatics.
> Synthesizes Cochrane's and Varian's rules for theoretical modeling in economics and finance.

---

## 1. Core Principles of Theory in Applied Papers

### Rule 1: Intuition Before Formalism
- Never write three pages of dense mathematical equations without first explaining the underlying economic intuition in plain English.
- Before presenting any theorem or proposition, state the result in one intuitive sentence:
  - *"In equilibrium, informed traders concentrate their orders during high-volatility regimes because market depth provides greater camouflage."*

### Rule 2: Minimalist Modeling (Ockham's Razor)
- Write down the simplest possible model that delivers the empirical prediction.
- If a 2-period model conveys the economic mechanism, do not construct an infinite-horizon stochastic dynamic game.
- Every state variable and parameter in the model must have a clear purpose. If deleting a parameter does not change the sign or qualitative behavior of the comparative statics, eliminate it.

### Rule 3: Direct Mapping to Empirical Observables
- Every theoretical construct must map to a specific variable in your empirical data:
  - Asset return volatility $\sigma_i \to$ Realized daily return variance.
  - Information asymmetry $\theta \to$ Bid-ask spread or order flow imbalance.
  - Risk aversion $\gamma \to$ Institutional ownership share or margin requirements.

---

## 2. Standard Structure of the Theoretical Section

### 1. The Economic Environment
- Specify the timeline: Dates $t \in \{0, 1, 2, \dots\}$.
- Specify the agents: Consumers, firms, informed traders, noise traders, market makers.
- State agent objectives: Utility maximization, profit maximization, or portfolio optimization.
- State information endowments: What is common knowledge, and what is private information?

### 2. Market Structure & Clearing
- Specify the price determination mechanism: Walrasian auctioneer, batch auction, or continuous limit order book.
- State the market clearing conditions.

### 3. Equilibrium Characterization
- Define the equilibrium concept (e.g., *Rational Expectations Equilibrium*, *Markov Perfect Equilibrium*, *Nash Equilibrium*).
- State First-Order Conditions (FOCs) and envelope conditions clearly.
- Move long, tedious algebraic proofs to the Mathematical Appendix. State only the main Propositions and Corollaries in the body text.

### 4. Comparative Statics & Empirical Hypotheses
- Derive the partial derivatives showing how the equilibrium outcome varies with key parameters:
  $$\frac{\partial \rho^*_{ij}}{\partial \text{Vol}_m} > 0, \quad \frac{\partial^2 \rho^*_{ij}}{\partial \text{Vol}_m \partial \text{Liq}_i} < 0$$
- Translate each comparative static into a concrete, testable empirical hypothesis:
  - **Hypothesis 1 (Direct Effect)**: *Cross-asset correlation increases monotonically with market volatility.*
  - **Hypothesis 2 (Interaction Effect)**: *The volatility-correlation sensitivity is amplified for assets with lower market liquidity.*
