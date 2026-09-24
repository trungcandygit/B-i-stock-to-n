# Figure Synthesis, Visual Communication & TikZ Standards

> High-impact scientific figures serve as cognitive anchors for referees and readers.
> Synthesized from the SNL Lab figure synthesis guide and top journal visualization standards.

---

## 1. The Primacy of Figure 1 (The Teaser / Architectural Anchor)

### The Page 1–2 Rule
Every paper proposing a methodology, system, theoretical framework, or complex empirical identification strategy MUST feature an informative Figure 1 on page 1 or page 2.

### The 3 Core Jobs of Figure 1
1. **Explain the Intuition Without Words**: A reader skimming the paper should understand the central tension and proposed solution purely by inspecting Figure 1 and its caption.
2. **Show Inputs, Transformation, and Outputs**:
   - Left side: The raw data / problem state / market frictions.
   - Middle: The core economic model / econometric filter / algorithmic engine.
   - Right side: The empirical outcome / policy decision / portfolio performance.
3. **Contrast with the Status Quo**: Visually highlight where traditional approaches fail and where your approach succeeds.

---

## 2. Caption Self-Containment (The 3-Part Formula)

Captions are among the most frequently read text in any academic paper. Never write single-sentence throwaway captions like:
✗ *Banned*: `"Figure 1: Overview of our proposed model."`

### The 3-Part Mandatory Caption Structure
1. **Title / Topic**: What is depicted (in bold or distinct phrasing).
2. **Key Takeaway / Punchline**: What the reader should notice and conclude from the figure.
3. **Methodological / Sample Grounding**: What data, time window, sample size, or econometric estimator generated the visual.

✓ *Exemplary Caption*:
> **Figure 1: Regime-Dependent Asymmetric Dynamic Correlation.** Dynamic conditional correlations spike by 42% during high-volatility regimes (shaded red) compared to calm regimes (shaded blue), indicating systemic liquidity contagion. Shaded bands represent 95% bootstrap confidence intervals. Estimates are derived from daily returns of VN30 constituents (2018–2024) using the multi-scale DCCA-GARCH specification.

---

## 3. Visual & Technical Execution Standards

### Rule 1: Vector Graphics Only (Strict Ban on Blurry Bitmaps)
- Diagrams, schematics, and line/scatter plots MUST be rendered as vector graphics:
  - Formats: `.pdf`, `.eps`, `.svg`, or directly in LaTeX via `TikZ` / `PGFPlots`.
  - Strictly ban raster formats (`.png`, `.jpg`, `.bmp`) for plots and diagrams. Raster graphics pixelate when zoomed by reviewers and read as amateur work.

### Rule 2: Color Accessibility & Monochrome Legibility
- **Colorblind-Safe Palettes**: Use perceptually uniform, colorblind-safe color scales:
  - Categorical data: Okabe-Ito palette, Tol's bright/muted palette.
  - Continuous data: `Viridis`, `Cividis`, or `Magma`.
- **The Black-and-White Test**: Always inspect the figure converted to grayscale. If lines or bars cannot be distinguished without color:
  - Add distinct line styles (`solid`, `dashed`, `dotted`, `dash-dot`).
  - Add distinct point markers (`circles`, `triangles`, `squares`, `diamonds`).
  - Add patterned hatchings for bar charts.

### Rule 3: Typography & Scaling
- Font sizes in figures must closely match the document body font size (typically 9pt–10pt in 100% scale).
- Never embed figures with tiny unreadable axis labels or gigantic cartoonish headings.
- Always include units on both axes: e.g., *Return Volatility (Annualized, %)* or *Log Market Capitalization (VND Trillion)*.

---

## 4. TikZ Skeleton Template for Methodological Architecture

```latex
\begin{figure}[t]
\centering
\begin{tikzpicture}[
    node distance=1.8cm,
    box/.style={rectangle, draw=black!80, fill=blue!5, very thick, minimum width=2.4cm, minimum height=1.2cm, align=center, font=\small\sffamily},
    engine/.style={rectangle, draw=red!80, fill=red!5, very thick, minimum width=2.8cm, minimum height=1.4cm, align=center, font=\small\bfseries\sffamily},
    arrow/.style={-stealth, thick, draw=black!70}
]

% Nodes
\node[box] (data) {High-Frequency\\Tick Data};
\node[box, right of=data, xshift=1.2cm] (filter) {Regime Detection\\(Markov Switching)};
\node[engine, right of=filter, xshift=1.6cm] (dcca) {Multi-Scale\\DCCA Estimator};
\node[box, right of=dcca, xshift=1.6cm] (output) {Dynamic Cross-Correlation\\Matrix $\mathbf{R}_t$};

% Connections
\draw[arrow] (data) -- node[above, font=\scriptsize] {Returns} (filter);
\draw[arrow] (filter) -- node[above, font=\scriptsize] {Regime State} (dcca);
\draw[arrow] (dcca) -- node[above, font=\scriptsize] {Estimates} (output);

\end{tikzpicture}
\caption{\textbf{End-to-End Estimation Framework for Regime-Dependent Asset Correlations.} The pipeline takes raw high-frequency returns, isolates macroeconomic regimes via 2-state Markov switching, estimates cross-asset scaling exponents, and produces time-varying correlation matrices used in downstream risk parity optimization.}
\label{fig:method_pipeline}
\end{figure}
```
