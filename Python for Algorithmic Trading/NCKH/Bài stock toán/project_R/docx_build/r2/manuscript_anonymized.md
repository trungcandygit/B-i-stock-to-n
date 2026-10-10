::: {custom-style="Title"}
How Much of a Nested Index Correlation Is Construction? A Scale-Wise Part–Whole Decomposition with Evidence from Vietnam
:::

::: {custom-style="abstract"}
**Abstract** When one equity index contains another, part of their correlation is fixed by construction. We extend the classical part–whole correlation identity to detrended cross-correlation analysis (DCCA). At every timescale, the coefficient between a parent and a child index is then a closed-form function of the child’s weight, the relative amplitude of the remaining constituents and the overlap-purged coefficient between the child and those constituents. The identity yields a zero-correlation benchmark, an exact lower bound, the sensitivity of the nested coefficient to the purged coefficient and an order-free attribution, and it requires only index-level inputs. On the Ho Chi Minh City Stock Exchange (VN30 within VN100 within VNINDEX, 30-minute to daily data, 2014–2025), the VN30–VN100 coefficient moves by only about 0.11 per unit change in the purged coefficient. Purging the overlap lowers the correlation with large caps by about 0.10 at every frequency. The decomposition barely varies across scales and frequencies, so its Pearson version suffices in these data. The small intraday horizon dependence of broad-market pairs comes from the opening and closing auction bars. Evidence of crisis contagion depends on the test used, and regime-conditioned correlations do not improve out-of-sample portfolio variance forecasts. Correlations between nested indices therefore say little about diversification between size tiers unless the overlap is removed first.
:::

::: {custom-style="keywords"}
**Keywords** constituent overlap; detrended cross-correlation; part–whole correlation; contagion; portfolio risk; Vietnam
:::

::: {custom-style="keywords"}
**JEL Classification** C14; C58; G11; G15
:::

::: {custom-style="heading1"}
1 Introduction
:::

::: {custom-style="p1a"}
Correlations between published equity indices are a convenient measure of how much one market segment diversifies another (Markowitz 1952). In nested index systems, these correlations have a problem unrelated to estimation error: the parent contains the child, so part of their correlation is fixed by construction. On the Ho Chi Minh City Stock Exchange (HOSE),
:::

$$
\mathrm{VN30} \subset \mathrm{VN100} \subset \mathrm{VNINDEX}. \qquad (1)
$$

The 30 largest firms hold about two-thirds of the free-float capitalization of VN100, and the daily VN30–VN100 correlation is 0.988. Read as a measure of how mid caps move with large caps, this number mixes economic linkage with the double counting of VN30 stocks on both sides. Holdings-based risk models avoid the problem; users of index-level data cannot. Index-level co-movement is easy to misread even without overlap (Chen et al. 2016). The arithmetic is old (Pearson 1897; Cureton 1966), but no version exists for the detrended, scale-dependent coefficients of the detrended cross-correlation analysis (DCCA) literature. That literature studies only pairs without shared constituents (Section 2).

Our contribution is to build that version. Lemma 1 shows that, at every timescale, the DCCA coefficient of a nested pair is a known function of the child’s weight, the relative amplitude κ(s) of the remaining constituents and the overlap-purged coefficient between the child and those constituents. It yields a zero-correlation benchmark, an exact lower bound, the sensitivity of the nested coefficient to the purged one and an order-free attribution, all computable from index-level data (Section 4.2). We apply it to VN30, VN100 and VNINDEX at 30-minute to daily frequencies (2014–2025), with a block bootstrap that also draws the index weight. We then use the purged series to test hypotheses on horizon dependence, contagion and the value of regime-conditioned correlations.

We report three main findings. The VN30–VN100 coefficient responds to the purged coefficient with a sensitivity of 0.106–0.112, and the like-for-like gap between nested and purged coefficients is 0.099–0.104; because κ hardly varies with the timescale (0.47–0.52), the Pearson version gives the same answer. On the purged series, horizon dependence is confined to intraday broad-market pairs and comes from the auction bars. Crisis evidence depends on whether contagion is measured by an adjusted correlation or a factor loading, and regime-conditioned correlations do not outperform a static one out of sample.

Section 2 reviews the literature and states the hypotheses. Sections 3–5 present the data, methods and results, Section 6 discusses them and Section 7 concludes. Further checks are in Online Resource 2.

::: {custom-style="heading1"}
2 Literature review and hypothesis development
:::

::: {custom-style="p1a"}
Five literatures bear on nested index correlations: part–whole correlation, detrended cross-correlation, index membership, size-based lead–lag effects and contagion. We review what each establishes and leaves open, then state the gap, estimands and hypotheses.
:::

::: {custom-style="heading2"}
2.1 Part–whole correlation and holdings overlap
:::

::: {custom-style="p1a"}
Pearson (1897) showed that ratios sharing a denominator correlate even when their numerators are independent. In psychometrics the same arithmetic inflates the correlation of an item with the total score that contains it, and Cureton (1966) gave a standard correction. Both results are static Pearson identities; neither measures the component at different timescales or attaches sampling uncertainty to it. Finance handles overlap through holdings: Active Share measures how far a fund departs from its benchmark holdings (Cremers and Petajisto 2009), holdings-based risk models estimate exposures from constituents, and membership studies build comparison portfolios from stocks outside the index (Barberis et al. 2005). Users who observe only index levels lack a return-based counterpart.
:::

::: {custom-style="heading2"}
2.2 Multiscale dependence and detrended cross-correlation
:::

::: {custom-style="p1a"}
DCCA extends detrended fluctuation analysis (Peng et al. 1994; Kantelhardt et al. 2002) to pairs of nonstationary series (Podobnik and Stanley 2008). Zebende (2011) normalized it into a bounded coefficient, Podobnik et al. (2011) proposed tests and Zhou (2008) generalized it to multifractal moments (MF-DCCA). Variants use moving-average detrending (Jiang and Zhou 2011; Kristoufek 2014), sliding windows (Guedes et al. 2021) or partial correlations (Ge and Lin 2021), and Oświęcimka et al. (2014) show that absolute local covariances can create spurious multifractality. Applied work finds horizon-dependent stock–bond and cross-market dependence (Al Rababa’a et al. 2021; Ge and Lin 2021; Chen et al. 2024). Other studies use the coefficient to track contagion (Okorie and Lin 2021; Tilfani et al. 2021) or information flow (Zhou et al. 2025) and build scale-aware portfolios (Wang et al. 2021; Kakinaka et al. 2025). These studies treat the coefficient as a measure of economic dependence between disjoint assets. None of them analyzes nested pairs, where the detrended covariance inherits the part–whole arithmetic at every scale.
:::

::: {custom-style="heading2"}
2.3 Index membership and co-movement
:::

::: {custom-style="p1a"}
Stocks added to the S&P 500 co-move more with the index (Barberis et al. 2005), Nikkei 225 stocks with larger weights co-move more with other index stocks (Greenwood 2008), and regression-discontinuity and tracking-demand designs support the effect (Liao et al. 2022; DeCoste 2025). The evidence is contested: much of the post-inclusion rise also appears in matched stocks that were not added (Chen et al. 2016), and the S&P 500 index effect has almost disappeared (Greenwood and Sammon 2025). Membership-based co-movement is therefore a weak guide even where indices do not overlap. Our concern is the arithmetic overlap, which raises correlations even if no investor trades differently.
:::

::: {custom-style="heading2"}
2.4 Size, lead–lag and horizon effects
:::

::: {custom-style="p1a"}
Large-firm returns lead small-firm returns (Lo and MacKinlay 1990), a pattern Hou (2007) traces to slow diffusion of industry information. Non-synchronous trading depresses short-horizon correlations (Epps 1979), with a size that depends on sampling (Chang et al. 2021), and gradual diffusion (Hong and Stein 1999) lets co-movement build with the horizon. On the HOSE, small-firm liquidity fell after a market surveillance system was introduced (Chen et al. 2021), and price adjustment is delayed under retail-heavy trading (Tran and Tran 2025). Three forces raise all correlations at once: herding in stress (Nguyen et al. 2023), sector connectedness above 60% that rose to near 90% during COVID-19 (Bui et al. 2022) and nonlinear regional dependence (Le et al. 2025).
:::

::: {custom-style="heading2"}
2.5 Volatility, contagion and interdependence
:::

::: {custom-style="p1a"}
Equity correlations rise in downturns (Longin and Solnik 2001; Ang and Chen 2002), but they also rise mechanically with the variance of the conditioning market, so a crisis increase may reflect interdependence rather than contagion (Forbes and Rigobon 2002). The correction can itself be biased toward no contagion because it restricts the variance of idiosyncratic shocks. Corsetti et al. (2005) propose testing for a change in the factor loading instead, and Rigobon (2003) identifies transmission from regime changes in variance. Studies without the correction report COVID-19 contagion (Akhtaruzzaman et al. 2021; Guo et al. 2021; Benkraiem et al. 2022). A DCCA test finds it for some commodity pairs but not others (Santana et al. 2023), and ASEAN integration varies with trade links and volatility (Abdul Karim and Xin Ning 2013; Lean and Teng 2013). No study applies volatility-robust tests to tiers of one market whose indices overlap.
:::

::: {custom-style="heading2"}
2.6 Research gap
:::

::: {custom-style="p1a"}
Table 1 compares representative studies on the dimensions that matter here.
:::

::: {custom-style="tablecaption"}
**Table 1** Prior studies of overlap, multiscale and crisis co-movement and the gap addressed here
:::

| Study | Market and data | Method | Overlap treated? | Scale-wise? | Volatility-robust test? | Main finding |
|---|---|---|---|---|---|---|
| Pearson (1897); Cureton (1966) | Ratios with a common component; test items | Pearson correlation | Yes (static) | No | No | Correlation of a whole with its part is inflated |
| Cremers and Petajisto (2009) | US mutual funds | Holdings overlap (Active Share) | Yes (holdings) | No | No | Overlap with benchmark holdings measures activity |
| Barberis et al. (2005); Greenwood (2008); Chen et al. (2016) | S&P 500; Nikkei 225 | Event study; index weights | Membership, not overlap | No | No | Membership effect on co-movement is contested |
| Podobnik and Stanley (2008); Zebende (2011) | Methodological | DCCA; ρDCCA | No | Yes | No | Scale-wise detrended covariance and coefficient |
| Okorie and Lin (2021); Tilfani et al. (2021) | Stock markets, COVID-19 | DCCA, DMCA; sliding windows | No | Yes | No | Fractal contagion that fades with the horizon |
| Ge and Lin (2021); Chen et al. (2024) | China and United States | MF-DCCA; partial MF-DCCA | No | Yes | No | Scale- and size-dependent cross-correlation |
| Wang et al. (2021); Kakinaka et al. (2025) | Stock portfolios | Mean-MF-X-DMA; mean-DCCA | No | Yes | No | Scale-aware rules improve portfolio performance |
| Santana et al. (2023) | Crude oil and precious metals | ΔρDCCA test | No | Yes | No | Contagion depends on the pair |
| Forbes and Rigobon (2002); Corsetti et al. (2005) | International stock markets | Adjusted correlation; factor model | No | No | Yes | Interdependence versus contagion; bias from restricted idiosyncratic variance |
| Lo and MacKinlay (1990); Hou (2007) | US size portfolios | Cross-autocorrelation | No | No | No | Large caps lead small caps |
| Bui et al. (2022); Tran and Tran (2025) | Vietnamese sectors; intraday HOSE | Spillover connectedness; high-frequency | No | No | No | High connectedness; delayed adjustment |
| This study | VN30, VN100, VNINDEX; M30 to daily, 2014–2025 | Scale-wise part–whole identity; DCCA | Yes (scale-wise, with weight uncertainty) | Yes | Yes | Purged coefficient is largely masked in the nested one |

::: {custom-style="Compact"}
Notes: Overlap treated: whether the study separates dependence created by shared constituents; scale-wise: whether dependence is measured by timescale; volatility-robust test: whether crisis comparisons correct for heteroskedasticity or common shocks; DMCA: detrending moving-average cross-correlation analysis; ρDCCA: DCCA coefficient. Source: Authors’ compilation.
:::

Three gaps follow. The part–whole identity is known for static Pearson correlations but has not been extended to scale-wise detrended coefficients, equipped with inference under weight uncertainty, or turned into a diagnostic computable from published series. Multiscale studies of crises rarely use volatility-robust tests, and volatility-conditioned studies use one horizon and disjoint markets. To our knowledge, no study covers the Vietnamese index system at intraday and daily frequencies. For this review, we searched Google Scholar and publisher databases for 2021–2026, plus the classical sources these works cite. Search strings combined “detrended cross-correlation” with “index”, “overlap”, “nested” or “constituent”, together with “part–whole” and “item–total correlation”, “contagion” with “Forbes–Rigobon” or “heteroskedasticity”, and “Vietnam” with “co-movement” or “stock index”.

::: {custom-style="heading2"}
2.7 Estimands and hypotheses
:::

::: {custom-style="p1a"}
Lemma 1 (Section 4.2) fixes some quantities once the weight and relative amplitude are known; we report these as estimands and test only what the identity does not determine. E1 is the zero-correlation benchmark ρ̲ of the VN30–VN100 coefficient and its share under three attribution conventions, E2 the sensitivity of the nested to the purged coefficient, and E3 the in-sample misstatement of portfolio variance by a static correlation, judged against sampling error. A share above one half is not a finding: it holds whenever κ < √3 and the purged coefficient is non-negative.
:::

*H1 (material overlap gap).* A purged coefficient near one would leave almost no gap, so the gap size is an empirical question. Rule: the lower 95% bound of the like-for-like gap (VN30–VN100 minus P~cap~–VN30; P~cap~ is the overlap-purged mid-cap series) exceeds 0.05, the estimation tolerance of Section 4.4, at every frequency.

*H2 (horizon dependence).* Large caps lead small caps (Lo and MacKinlay 1990; Hou 2007), non-synchronous trading depresses short-horizon correlations (Epps 1979) and information diffuses gradually (Hong and Stein 1999). Broad-market coefficients should therefore rise with the timescale, whereas the identity predicts a damped VN30–VN100 slope. Rule: among eight broad-market slope tests, at least one pair at each of M30 and H1 has a positive slope with a Holm-adjusted studentized p-value below 0.05. We also report robustness to removing the opening bar and an equivalence test for VN30–VN100.

*H3 (contagion).* Raw crisis correlations rise with volatility alone (Forbes and Rigobon 2002), and the volatility correction is biased toward no contagion when idiosyncratic variance rises (Corsetti et al. 2005). Rule: under VN30 volatility regimes, the adjusted correlation of P~cap~ and VN30 exceeds its calm level (one-sided p < 0.05) and the loading of P~cap~ on VN30 rises (two-sided p < 0.05).

*H4 (value of regime conditioning).* Rule: an exponentially weighted moving average (EWMA) or real-time regime correlation has a lower quasi-likelihood (QLIKE) loss than the static correlation over 2023–2025, with a Diebold–Mariano p-value below 0.05. We fixed these rules, the eight-test family and the factor-loading test at revision, after the first-round results were known. We also report the original specifications.

::: {custom-style="heading1"}
3 Institutional background and data
:::

::: {custom-style="heading2"}
3.1 Institutional background
:::

::: {custom-style="p1a"}
Six features of the HOSE matter here. Prices move within a ±7% daily band, which truncates tails and synchronizes limit hits. Settlement moved from T+3 to T+2 on 1 January 2016 (Vietnam Securities Depository 2015), limiting intraday arbitrage. Each day has an opening call auction (09:00–09:15), continuous trading to 11:30, a break to 13:00, a second continuous session and a closing call auction (14:30–14:45). Short selling is restricted. Circular 120/2020/TT-BTC (Ministry of Finance of Vietnam 2020) provides a framework for covered short sales that, to our knowledge, had not been implemented, and naked short selling is prohibited. The implementing Decree 155/2020/ND-CP (Government of Vietnam 2020) was amended by Decree 245/2025/ND-CP (Government of Vietnam 2025). VN30 futures trade on the Hanoi Stock Exchange, but no mid-cap future exists. A VNMIDCAP exchange-traded fund (FUEDCMID) has been listed since 29 September 2022 (Ho Chi Minh City Stock Exchange 2022), so mid caps can be held long but cannot be shorted or hedged with a dedicated derivative. Finally, foreign ownership limits (30% for banks, for example) concentrate foreign flows in large caps with room under their limits. Vietnam is to be reclassified to Secondary Emerging status from 21 September 2026 (FTSE Russell 2025), after the end of our sample.
:::

::: {custom-style="heading2"}
3.2 Data and sample construction
:::

::: {custom-style="p1a"}
We use VN30, VN100 and VNINDEX levels exported from TradingView (exchange code HOSE). VN30 holds the 30 largest stocks by free-float capitalization, VN100 adds the next 70 (the VNMIDCAP index) and VNINDEX covers all HOSE stocks at full capitalization. Daily (1D) and 30-minute (M30) series run to 12 December 2025, 1-hour (H1) and 4-hour (H4) series to 9 December 2024. M30 bars open at 09:00, 09:30, 10:00, 10:30, 11:00, 11:30, 13:00, 13:30, 14:00, 14:30, H1 bars at 09:00, 10:00, 11:00, 13:00, 14:00, and the two H4 bars cover the two sessions, so at every frequency the first bar of the day holds the overnight return and the opening auction. The vendor has no full VNMIDCAP history, so we recover the mid-cap segment from VN30 and VN100 (Section 4.2). We merge the series by exact timestamp joins without filling gaps. We did not compare them with HOSE closing levels date by date; the replication package records an input checksum. Log returns are
:::

$$
R_t=\ln P_t-\ln P_{t-1}. \qquad (2)
$$

The synchronized window (3 January 2017 to 9 December 2024; 1D: N = 1,983; M30: 19,463; H1: 9,879; H4: 3,953) serves cross-frequency comparisons. All other analyses use the full sample (1D: February 2014 to December 2025, N = 2,963; M30: January 2017 to December 2025, 21,942; H1 and H4: January 2014 to December 2024, 13,523 and 5,410). The indices are computed in real time, so they embed reconstitutions and delistings and carry no survivorship bias.

Regimes use the 20-day rolling standard deviation of returns (Fig. 1). Chronological crises require a VNINDEX drawdown above 25%, at least 45% of days in the top volatility quartile and a documented trigger: the 2018 margin contraction (drawdown 26.2%, 47% of days in the top quartile), COVID-19 in 2020 (33.5%, 52%) and the 2022 bond-market freeze (40.2%, 60%). The three episodes total 539 days, against calm years 2016–2017 and 2023–2024 (1,000 days); the 2021 and 2025 spikes fail the first two conditions (Table S12). Quartile regimes compare the bottom and top quartiles of rolling VNINDEX volatility (10.6% and 20.0% annualized) or of VN30 volatility.

![](/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/docx_build/../outputs/figures/fig1_volatility_regimes.png){width=6.3in}

::: {custom-style="figurecaption"}
**Fig. 1** Twenty-day rolling volatility of VNINDEX (annualized) and market regimes, 2014–2025
:::
::: {custom-style="Compact"}
Notes: Shaded areas: the three chronological crisis episodes; dashed and dotted horizontal lines: 25th and 75th percentiles of rolling volatility. The 2021 and 2025 spikes are not shaded because their drawdowns are below 25% (Section 3.2). Source: Authors’ calculations based on HOSE index data (TradingView).
:::

::: {custom-style="heading1"}
4 Methodology
:::

::: {custom-style="heading2"}
4.1 The DCCA coefficient
:::

::: {custom-style="p1a"}
The DCCA coefficient measures correlation at timescale s after removing local trends (Podobnik and Stanley 2008; Zebende 2011). For return series x and y of length N, the profiles are
:::

$$
X_k=\sum_{t=1}^{k}(x_t-\bar{x}),\quad Y_k=\sum_{t=1}^{k}(y_t-\bar{y}),\quad k=1,\dots,N. \qquad (3)
$$

We split each profile into N~s~ = ⌊N/s⌋ boxes of length s, starting from each end of the series (2N~s~ boxes). In each box ν we fit a polynomial of order m (m = 1 unless stated otherwise) by ordinary least squares (OLS); the residuals ε~X~ and ε~Y~ give the detrended covariance

$$
f^2_{XY}(s,\nu)=\frac{1}{s}\sum_{k=1}^{s}\varepsilon_{X}(k,\nu)\,\varepsilon_{Y}(k,\nu),\qquad F^2_{XY}(s)=\frac{1}{2N_s}\sum_{\nu=1}^{2N_s}f^2_{XY}(s,\nu). \qquad (4)
$$

With F~X~(s) = [F²~XX~(s)]^1/2^ the detrended fluctuation function (Peng et al. 1994), the DCCA coefficient is

$$
\rho_{XY}(s)=\frac{F^2_{XY}(s)}{F_X(s)\,F_Y(s)}. \qquad (5)
$$

Eq. (5) is an inner product of stacked residual vectors divided by their norms, so \|ρ~XY~(s)\| ≤ 1 by the Cauchy–Schwarz inequality whenever both fluctuation functions are positive. Because profiles are linear in the series and OLS detrending is a linear projection, the residuals of a weighted sum of series are the same weighted sum of their residuals.

::: {custom-style="heading2"}
4.2 The overlap-purged series and the part–whole identity
:::

::: {custom-style="p1a"}
Let A~t~ and B~t~ be VN30 and VN100 returns and w the free-float weight of VN30 in VN100. The overlap-purged mid-cap series is
:::

$$
M_t=P_{\mathrm{cap},t}=\frac{B_t-wA_t}{1-w}, \qquad (6)
$$

with w = 0.6826 from the HOSE factsheet of 31 May 2024 (free-float capitalizations of VND 1,316,288 billion and 1,928,303 billion, respectively), so that B~t~ = wA~t~ + (1 − w)M~t~ at every observation. On log returns, P~cap~ differs from the arithmetic mid-cap return by a Jensen term of 3.6 × 10⁻⁶ per day. P~cap~ is a synthetic shadow series: replicating it requires about 315% long VN100 and 215% short VN30. We call ρ~AM~, the coefficient of VN30 and P~cap~, overlap-purged rather than economic, because we cannot validate P~cap~ against the published VNMIDCAP series (Section 6.3).

**Lemma 1 (scale-wise part–whole identity).** Let B~t~ = wA~t~ + (1 − w)M~t~ for all t, with 0 < w < 1 and F~A~(s), F~M~(s) > 0, and define the relative amplitude κ(s) = (1 − w)F~M~(s)/[wF~A~(s)]. Then, for every s and m,

$$
\rho_{AB}(s)=\frac{1+\kappa(s)\,\rho_{AM}(s)}{\sqrt{1+\kappa(s)^2+2\kappa(s)\,\rho_{AM}(s)}}. \qquad (7)
$$

*Proof.* Residuals are linear in the series, so ε~B~ = wε~A~ + (1 − w)ε~M~ in every box. By bilinearity of Eq. (4), F²~AB~ = wF²~A~ + (1 − w)ρ~AM~ F~A~ F~M~ and F²~B~ = w²F²~A~ + (1 − w)²F²~M~ + 2w(1 − w)ρ~AM~ F~A~ F~M~; substituting into Eq. (5) and dividing by wF²~A~ gives Eq. (7). ∎

With one box and no detrending, Eq. (7) is the classical part–whole correlation (Pearson 1897; Cureton 1966), so the lemma adapts a known identity. It holds scale by scale for detrended coefficients, for the detrending moving-average cross-correlation (DMCA) coefficient (Kristoufek 2014) and for any measure built from a bilinear covariance of linearly filtered series. Five corollaries follow; we fix the scale and suppress it in the notation.

*Corollary 1 (benchmark and bound).* Setting ρ~AM~ = 0 gives the zero-correlation benchmark

$$
\underline{\rho}=\frac{1}{\sqrt{1+\kappa^2}}. \qquad (8)
$$

Eq. (7) increases in ρ~AM~ for ρ~AM~ > −κ, so ρ̲ bounds ρ~AB~ from below only when ρ~AM~ ≥ 0. For κ < 1 the minimum over all admissible ρ~AM~ is

$$
\min_{\rho_{AM}\in[-1,1]}\rho_{AB}=\sqrt{1-\kappa^2},\qquad \text{attained at } \rho_{AM}=-\kappa; \qquad (9)
$$

for κ ≥ 1 no positive bound exists. *Corollary 2 (sensitivity).* The sensitivity of ρ~AB~ to ρ~AM~ is

$$
\frac{\partial\rho_{AB}}{\partial\rho_{AM}}=\frac{\kappa^2\,(\kappa+\rho_{AM})}{(1+\kappa^2+2\kappa\rho_{AM})^{3/2}}, \qquad (10)
$$

which is small when the child dominates the parent; its inverse states how far ρ~AM~ must move to change ρ~AB~ by a given amount. *Corollary 3 (direction).* For ρ~AM~ ≥ 0, ρ²~AB~ − ρ²~AM~ = (1 − ρ²~AM~)(1 + 2κρ~AM~)/(1 + κ² + 2κρ~AM~) ≥ 0, so overlap can only raise the coefficient. *Corollary 4 (dominance).* For ρ~AM~ ≥ 0, ρ~AB~ ≤ 1 implies ρ̲/ρ~AB~ ≥ ρ̲, so the benchmark exceeds half of ρ~AB~ whenever κ < √3, that is, F~M~/F~A~ < √3·w/(1 − w) = 3.73 at the factsheet weight; such a share carries no information. *Corollary 5 (attribution).* With neither overlap nor dependence the coefficient is 0, with overlap only ρ̲, with dependence only ρ~AM~ and with both ρ~AB~. The benchmark-first share ρ̲/ρ~AB~ and the dependence-first share ρ~AM~/ρ~AB~ depend on the order; the Shapley (1953) value averages the two orders into an additive split,

$$
\phi_{\mathrm{overlap}}=\tfrac12\left[\underline{\rho}+(\rho_{AB}-\rho_{AM})\right],\qquad \phi_{\mathrm{dep}}=\tfrac12\left[\rho_{AM}+(\rho_{AB}-\underline{\rho})\right],\qquad \phi_{\mathrm{overlap}}+\phi_{\mathrm{dep}}=\rho_{AB}. \qquad (11)
$$

We lead with the sensitivity, which needs no attribution convention, and report the Shapley overlap share φ_overlap/ρ~AB~. Eq. (7) reproduces the directly estimated VN30–VN100 coefficient at every scale and frequency to within 4.4 × 10⁻¹⁶. We compute all quantities scale by scale and average them over the reliable range (Section 4.4). Because M is a linear combination of A and B, the decomposition also follows from index-level moments alone (Box 1).

::: {custom-style="tablecaption"}
**Box 1** Decomposition of a nested correlation from index-level inputs
:::

| Step | Computation | VN30 in VN100, daily |
|---|---|---|
| 1. Inputs | w; σ~A~, σ~B~; ρ~AB~ | w = 0.6826; σ~A~ = 0.0121, σ~B~ = 0.0119; ρ~AB~ = 0.9885 |
| 2. Volatility of remaining constituents | σ~M~ = (σ²~B~ − 2wρ~AB~ σ~A~ σ~B~ + w²σ²~A~)^1/2^/(1 − w) | σ~M~ = 0.0124 |
| 3. Relative amplitude | κ = (1 − w)σ~M~/(wσ~A~) | κ = 0.475 |
| 4. Benchmark and bound | ρ̲ = (1 + κ²)^−1/2^; bound (1 − κ²)^1/2^ | ρ̲ = 0.903; bound 0.880 |
| 5. Purged coefficient | ρ~AM~ = (ρ~AB~ σ~B~ − wσ~A~)/[(1 − w)σ~M~] | ρ~AM~ = 0.889 |
| 6. Sensitivity | Eq. (10) | 0.103 (inverse 9.7) |

::: {custom-style="Compact"}
Notes: Pearson moments of daily log returns, February 2014 to December 2025. Steps 2 and 5 reproduce the volatility and the correlation of the directly constructed P~cap~ series exactly. Source: Authors’ calculations.
:::

::: {custom-style="heading2"}
4.3 Weight uncertainty
:::

::: {custom-style="p1a"}
Capitalizations drift between semi-annual reviews. If the true weight w~t~ differs from w, the purged series becomes
:::

$$
\hat{M}_t=\frac{1-w_t}{1-w}M_t+\frac{w_t-w}{1-w}A_t, \qquad (12)
$$

so large-cap returns leak into P~cap~ in proportion to the weight error w~t~ − w, and P~cap~ and VN30 are disjoint only at the exact weight. With a single factsheet snapshot we cannot rebuild the weight path, so each bootstrap replicate draws w from U(0.60, 0.75), an interval around the factsheet weight that allows drift in either direction, and recomputes P~cap~ and every statistic. Table S2 evaluates each quantity on a weight grid. The benchmark and sensitivity depend on the data only through κ and are less exposed to weight error than ρ~AM~.

::: {custom-style="heading2"}
4.4 Reliability thresholds and inference
:::

::: {custom-style="p1a"}
The DCCA coefficient becomes noisy at large scales, where boxes are few. For each sample size we simulate Gaussian white-noise pairs with correlations of −0.3, 0, 0.3, 0.5, 0.7 and 0.9 (1,002 per frequency) and set s~rel~ to the largest scale before the worst-case mean absolute error on 40 log-spaced scales first exceeds 0.05. We fixed the grid and tolerance in advance. A GARCH(1,1)-t(5) calibration (generalized autoregressive conditional heteroskedasticity with Student-t errors; 300 simulations) checks heavy tails.
:::

Coefficients at different scales come from the same series, so for all inference we resample the data with the stationary block bootstrap (Politis and Romano 1994) with mean blocks of about 20 trading days and recompute every curve and statistic in each replicate. We use 499 replicates for the DCCA statistics of Tables 4–6 and for the decomposition, hedge-effectiveness and tail-dependence statistics; 399 for the like-for-like gap under weight uncertainty; 199 for the trimmed-bar checks of Section 5.4 and Tables S7 and S15 and the 30-minute block-length checks of Table S6; and 999 for the factor-model, lead–lag and materiality statistics and for the Forbes–Rigobon tests under VN30 quartiles, across weights and with 2021 added. The remaining Forbes–Rigobon and relative-error statistics use 1,999 replicates. Intervals are percentile 95% intervals, capped at ±1 for correlations. With B = 499 replicates, percentile p-values cannot fall below 0.004 (reported as p < 0.005): p = 2 min{k₋ + 1, k₊ + 1}/(B + 1), where k₋ and k₊ count replicates at or below and at or above zero. With 19 tests, the smallest attainable Holm-adjusted value is 0.076. One-sided Forbes–Rigobon p-values use the re-centered bootstrap distribution, and p-values for Δβ and the residual-variance ratio are studentized. Because of the resolution limit, slope tests also use studentized p-values, 2Φ(−\|β̂\|/se~boot~), adjusted by the Holm (1979) and Benjamini and Hochberg (1995) procedures in two families: the original 19 reliable-range tests and the eight broad-market tests of H2. We test equivalence of the VN30–VN100 slope to zero with two one-sided tests (TOST; Schuirmann 1987) and a margin of 0.001 per unit of ln s. Over the 4.5 units of the M30 reliable range, such a slope moves the coefficient by less than a tenth of the 0.05 tolerance.

::: {custom-style="heading2"}
4.5 Scaling regressions and slope channels
:::

::: {custom-style="p1a"}
We measure horizon dependence by the slope β of
:::

$$
\rho_{XY}(s)=\alpha+\beta\ln s+u(s), \qquad (13)
$$

over s ≤ s~rel~ (full-range slopes in Table S1). For the nested pair, Eq. (7) splits the slope into a ρ~AM~ channel and a κ channel,

$$
\frac{d\rho_{AB}}{d\ln s}=\frac{\partial\rho_{AB}}{\partial\rho_{AM}}\frac{d\rho_{AM}}{d\ln s}+\frac{\partial\rho_{AB}}{\partial\kappa}\frac{d\kappa}{d\ln s},\qquad \frac{\partial\rho_{AB}}{\partial\kappa}=-\frac{\kappa(1-\rho_{AM}^2)}{(1+\kappa^2+2\kappa\rho_{AM})^{3/2}}, \qquad (14)
$$

so horizon dependence in ρ~AM~ reaches ρ~AB~ damped by the sensitivity of Eq. (10).

::: {custom-style="heading2"}
4.6 Volatility conditioning and contagion tests
:::

::: {custom-style="p1a"}
If y~t~ = α + βx~t~ + ε~t~ with Var(ε~t~) = σ²~ε~, the correlation [1 + σ²~ε~/(β²σ²~x~)]^−1/2^ rises with the variance of x even when β and σ²~ε~ are constant. Forbes and Rigobon (2002) adjust the crisis correlation as
:::

$$
\rho^{*}=\frac{\rho_{\mathrm{high}}}{\sqrt{1+\delta\,(1-\rho_{\mathrm{high}}^2)}},\qquad \delta=\frac{\sigma^2_{x,\mathrm{high}}-\sigma^2_{x,\mathrm{low}}}{\sigma^2_{x,\mathrm{low}}}, \qquad (15)
$$

with y = P~cap~ and x = VN30. The adjustment assumes constant β and σ²~ε~; if crises raise idiosyncratic variance, ρ* is biased toward no contagion (Corsetti et al. 2005). We therefore also test, regime by regime, for changes in the residual variance and in the loading β; a change in β is contagion in the sense of Corsetti et al. (2005), and β is the structural parameter of Rigobon (2003). Regimes are chronological episodes, VNINDEX volatility quartiles or VN30 volatility quartiles; the last sorts on the conditioning variable rather than on a series containing P~cap~. Statistics are Pearson moments of daily returns, bootstrapped within regimes. We do not test nested pairs, because the parent contains the conditioning index.

::: {custom-style="heading2"}
4.7 Portfolio variance: in-sample misstatement and out-of-sample evaluation
:::

::: {custom-style="p1a"}
For an equally weighted two-asset position, replacing the regime correlation ρ~r~ by the static correlation ρ~st~ changes the variance by
:::

$$
\mathrm{RE}=\frac{\rho_{\mathrm{st}}-\rho_{r}}{\tfrac{1}{2}\left(\sigma_1/\sigma_2+\sigma_2/\sigma_1\right)+\rho_{r}}, \qquad (16)
$$

with regime volatilities σ₁ and σ₂, so only the correlation differs. We obtain intervals by resampling the full sample jointly and re-estimating ρ~st~, and compare \|RE\| with the bootstrap relative standard error of the regime variance. Because these regimes are ex post, we also estimate correlations on 2014–2022 and evaluate forecasts on 2023–2025. Forecasts share one-step-ahead RiskMetrics variances (λ = 0.94; J.P. Morgan/Reuters 1996) and differ only in the correlation: static, EWMA with the same λ, or a regime correlation chosen in real time from lagged rolling volatility with thresholds fixed in the estimation window. Losses are QLIKE (Patton 2011) and squared error, compared by the Diebold and Mariano (1995) test with a Newey and West (1987) variance (five lags).

::: {custom-style="heading1"}
5 Results
:::

::: {custom-style="heading2"}
5.1 Summary statistics and reliability
:::

::: {custom-style="p1a"}
Table 2 reports descriptive statistics and Table 3 the reliability thresholds.
:::

::: {custom-style="tablecaption"}
**Table 2** Descriptive statistics of log returns
:::

| Series | Freq. | N | Mean | Std. dev. | Skew. | Kurt. | Jarque–Bera |
|---|---|---|---|---|---|---|---|
| VN30 | 1D | 2,963 | 0.0004 | 0.0121 | −0.83 | 7.81 | 3,202\*\*\* |
| VN30 | M30 | 21,942 | 0.0001 | 0.0039 | −1.62 | 36.16 | 1,014,769\*\*\* |
| VN30 | H1 | 13,523 | 0.0001 | 0.0051 | −1.33 | 18.20 | 134,167\*\*\* |
| VN30 | H4 | 5,410 | 0.0001 | 0.0084 | −1.17 | 11.23 | 16,490\*\*\* |
| VN100 | 1D | 2,963 | 0.0004 | 0.0119 | −0.96 | 8.21 | 3,804\*\*\* |
| VN100 | M30 | 21,942 | 0.0000 | 0.0038 | −1.83 | 37.63 | 1,108,959\*\*\* |
| VN100 | H1 | 13,523 | 0.0001 | 0.0050 | −1.50 | 19.36 | 155,896\*\*\* |
| VN100 | H4 | 5,410 | 0.0002 | 0.0082 | −1.30 | 11.76 | 18,833\*\*\* |
| VNINDEX | 1D | 2,963 | 0.0004 | 0.0115 | −0.98 | 8.27 | 3,898\*\*\* |
| VNINDEX | M30 | 21,942 | 0.0000 | 0.0037 | −2.04 | 40.64 | 1,310,762\*\*\* |
| VNINDEX | H1 | 13,523 | 0.0001 | 0.0049 | −1.56 | 19.54 | 159,748\*\*\* |
| VNINDEX | H4 | 5,410 | 0.0002 | 0.0080 | −1.31 | 11.99 | 19,767\*\*\* |
| P~cap~ | 1D | 2,963 | 0.0004 | 0.0124 | −1.07 | 8.15 | 3,837\*\*\* |
| P~cap~ | M30 | 21,942 | 0.0000 | 0.0041 | −1.87 | 33.94 | 887,934\*\*\* |
| P~cap~ | H1 | 13,523 | 0.0001 | 0.0052 | −1.51 | 18.81 | 145,968\*\*\* |
| P~cap~ | H4 | 5,410 | 0.0002 | 0.0086 | −1.33 | 11.69 | 18,632\*\*\* |

::: {custom-style="Compact"}
Notes: Kurt.: non-excess kurtosis; P~cap~: overlap-purged series of Eq. (6); \*\*\* p < 0.01. Source: Authors’ calculations based on HOSE index data (TradingView).
:::

P~cap~ has the highest daily standard deviation (0.0124) and VNINDEX the lowest (0.0115). All series are negatively skewed and leptokurtic (kurtosis above 33 at M30), and the Jarque–Bera test rejects normality for every series. Neither DCCA nor the block bootstrap requires Gaussian returns.

::: {custom-style="tablecaption"}
**Table 3** Finite-sample reliability thresholds of the DCCA coefficient
:::

| Frequency | N | Gaussian s~rel~ | Heavy-tailed s~rel~ |
|---|---|---|---|
| Daily (1D) | 2,963 | 50 | 20 |
| 30-minute (M30) | 21,942 | 444 | 151 |
| 1-hour (H1) | 13,523 | 233 | 86 |
| 4-hour (H4) | 5,410 | 88 | 28 |

::: {custom-style="Compact"}
Notes: s~rel~: largest scale (bars) at which the worst-case mean absolute error stays below 0.05; Gaussian: 1,002 white-noise simulations; heavy-tailed: 300 GARCH(1,1)-t(5) simulations. Source: Authors’ calculations.
:::

Gaussian thresholds range from 50 days at 1D to 444 bars at M30, and heavy tails cut them by about two-thirds. Averages below use the Gaussian thresholds. Over the heavy-tailed ranges, the nested averages become 0.975–0.979 and the purged average 0.882–0.890, so no conclusion depends on the choice.

::: {custom-style="heading2"}
5.2 The overlap gap (H1)
:::

::: {custom-style="p1a"}
Table 4 compares nested and purged coefficients; Fig. 2 shows the curves with bootstrap bands.
:::

::: {custom-style="tablecaption"}
**Table 4** Average DCCA coefficients of nested and overlap-purged pairs
:::

| Frequency | Nested mean | VN30–VN100 | P~cap~–VN30 | Three-pair gap [95% CI] | Like-for-like gap [95% CI] | Cohen’s q [95% CI] | N |
|---|---|---|---|---|---|---|---|
| *Panel A: synchronized window, 2017–2024* |  |  |  |  |  |  |  |
| Daily (1D) | 0.980 | 0.988 | 0.890 | 0.090 |  |  | 1,983 |
| 30-minute (M30) | 0.979 | 0.988 | 0.890 | 0.089 |  |  | 19,463 |
| 1-hour (H1) | 0.979 | 0.988 | 0.891 | 0.089 |  |  | 9,879 |
| 4-hour (H4) | 0.980 | 0.988 | 0.892 | 0.089 |  |  | 3,953 |
| *Panel B: full sample, 2014–2025* |  |  |  |  |  |  |  |
| Daily (1D) | 0.977 | 0.988 | 0.884 | 0.093 [0.074, 0.115] | 0.104 [0.085, 0.128] | 0.83 [0.75, 0.89] | 2,963 |
| 30-minute (M30) | 0.979 | 0.987 | 0.883 | 0.096 [0.080, 0.119] | 0.104 [0.087, 0.125] | 0.89 [0.83, 0.94] | 21,942 |
| 1-hour (H1) | 0.975 | 0.988 | 0.889 | 0.086 [0.071, 0.103] | 0.099 [0.084, 0.118] | 0.78 [0.70, 0.83] | 13,523 |
| 4-hour (H4) | 0.976 | 0.988 | 0.890 | 0.087 [0.072, 0.103] | 0.099 [0.084, 0.116] | 0.79 [0.72, 0.84] | 5,410 |

::: {custom-style="Compact"}
Notes: Averages of ρ(s) over s ≤ s~rel~ (Table 3) with m = 1; nested mean: VN30–VNINDEX, VN30–VN100 and VN100–VNINDEX; three-pair gap: nested mean minus P~cap~–VN30; like-for-like gap: VN30–VN100 minus P~cap~–VN30. Brackets: block-bootstrap 95% intervals at the factsheet weight. Source: Authors’ calculations.
:::

The nested pairs average 0.975–0.980 at every frequency in both samples, and P~cap~–VN30 averages 0.883–0.892. Corollary 3 fixes the sign of the like-for-like gap, but not its size: the gap is 0.099–0.104 with interval lower bounds of at least 0.084, above the 0.05 tolerance at every frequency, so H1 is supported. The three-pair gap, which also uses the broad-market pairs that cannot be purged by weight, is 0.086–0.096, with Cohen’s q (Cohen 1988) of 0.78–0.89. We report q descriptively because both coefficients come from the same sample. Overlap thus inflates co-movement that is already strong.

The gap depends on the weight: over w = 0.60–0.75 the daily like-for-like gap is 0.063–0.164 and the three-pair gap 0.052–0.153 (Tables S2 and S3). With w drawn in each replicate, the like-for-like intervals have lower bounds of 0.057–0.061 and every replicate exceeds 0.05, so H1 holds under weight uncertainty. The size of the gap, however, is known only to within a factor of about two.

![](/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/docx_build/../outputs/figures/fig2_dcca_curves.png){width=6.3in}

::: {custom-style="figurecaption"}
**Fig. 2** DCCA coefficients of the nested pairs and P~cap~–VN30 by timescale: (a) 1D, (b) M30, (c) H1, (d) H4
:::
::: {custom-style="Compact"}
Notes: Line and marker types identify the pairs; grey bands: pointwise block-bootstrap 95% intervals; vertical dotted lines: s~rel~ (Table 3). Source: Authors’ calculations based on HOSE index data (TradingView).
:::

::: {custom-style="heading2"}
5.3 The part–whole decomposition (E1, E2)
:::

::: {custom-style="p1a"}
Table 5 applies Lemma 1 to VN30–VN100, and Fig. 3 plots Eq. (7) against the purged coefficient.
:::

::: {custom-style="tablecaption"}
**Table 5** Part–whole decomposition of the VN30–VN100 DCCA coefficient (Lemma 1)
:::

| Frequency | κ | Purged ρ~AM~ | Nested ρ~AB~ | Benchmark ρ̲ | Bound √(1 − κ²) | Sensitivity | Benchmark-first share | Shapley overlap share |
|---|---|---|---|---|---|---|---|---|
| *Panel A: sampling uncertainty, w fixed at the factsheet value* |  |  |  |  |  |  |  |  |
| Daily (1D) | 0.484 | 0.884 [0.857, 0.906] | 0.988 | 0.900 [0.891, 0.910] | 0.875 | 0.106 [0.098, 0.114] | 0.911 | 0.508 [0.498, 0.521] |
| 30-minute (M30) | 0.503 | 0.883 [0.859, 0.904] | 0.987 | 0.893 [0.882, 0.903] | 0.864 | 0.112 [0.104, 0.122] | 0.905 | 0.505 [0.497, 0.515] |
| 1-hour (H1) | 0.486 | 0.889 [0.868, 0.905] | 0.988 | 0.899 [0.889, 0.909] | 0.874 | 0.107 [0.099, 0.116] | 0.910 | 0.505 [0.498, 0.515] |
| 4-hour (H4) | 0.485 | 0.890 [0.865, 0.908] | 0.988 | 0.900 [0.890, 0.910] | 0.874 | 0.106 [0.098, 0.115] | 0.910 | 0.505 [0.498, 0.515] |
| *Panel B: sampling and weight uncertainty, w ~ U(0.60, 0.75) in each replicate* |  |  |  |  |  |  |  |  |
| Daily (1D) |  | 0.884 [0.821, 0.931] |  | 0.900 [0.830, 0.938] |  | 0.106 [0.071, 0.163] | 0.911 [0.841, 0.949] | 0.508 [0.452, 0.556] |
| 30-minute (M30) |  | 0.883 [0.817, 0.926] |  | 0.893 [0.823, 0.932] |  | 0.112 [0.077, 0.168] | 0.905 [0.834, 0.944] | 0.505 [0.451, 0.555] |

::: {custom-style="Compact"}
Notes: Quantities of Eqs. (7)–(11) averaged over s ≤ s~rel~; A = VN30, B = VN100, M = P~cap~. Brackets: block-bootstrap 95% intervals; Panel B covers the daily and 30-minute frequencies. Source: Authors’ calculations.
:::

The sensitivity is 0.106–0.112: moving the nested coefficient by 0.01 requires the purged coefficient to move by about 0.09. Under weight uncertainty, the sensitivity interval is 0.07–0.17. With κ of 0.48–0.50, the remaining 32% of VN100 contributes about half as much detrended variation as VN30, which puts the benchmark at 0.893–0.900 and the lower bound of Eq. (9) at 0.864–0.875. No purged coefficient in [−1, 1] could push the VN30–VN100 coefficient below about 0.86.

The part of the observed 0.987–0.988 attributable to overlap depends on the attribution convention. The benchmark-first share is 0.905–0.911 and the dependence-first share 0.895–0.900, because either factor alone produces a coefficient near 0.9. The Shapley split attributes 0.505–0.508 to overlap (intervals within 0.497–0.521). Weight uncertainty widens the Shapley intervals to 0.45–0.56 and the benchmark-first intervals to 0.83–0.95, against a sampling-only width of about 0.02, so weight error dominates the uncertainty of any attribution.

The decomposition barely varies with the horizon. Across reliable scales and frequencies, κ lies in 0.47–0.52, the benchmark varies by 0.007–0.016 within a frequency, and its slope on ln s is not significant at 5% (p = 0.052–0.456; Holm 0.208–0.828), although at M30 the percentile interval just excludes zero. The slope, about −0.002 per unit of ln s, is negligible. On full-sample Pearson moments, the benchmark is 0.898–0.903 and the benchmark-first share 0.911–0.914, within 0.01 of the DCCA values. In these data, the multiscale layer checks scale invariance, and Box 1 suffices in practice. The DCCA version matters where tiers scale differently, which Eq. (7) reveals as variation in κ(s).

![](/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/docx_build/../outputs/figures/fig4_overlap_decomposition.png){width=6.3in}

::: {custom-style="figurecaption"}
**Fig. 3** Nested VN30–VN100 coefficient implied by Lemma 1 as a function of the overlap-purged coefficient
:::
::: {custom-style="Compact"}
Notes: Lines: Eq. (7) at the average κ of each frequency (Table 5); markers: observed values; dashed line: daily zero-correlation benchmark; dotted line: daily lower bound of Eq. (9). Source: Authors’ calculations.
:::

Fig. 4 places the HOSE among possible nested systems: the contours show the Pearson benchmark by child weight and relative volatility of the remaining constituents, and the triangle marks VN30 in VN100 (w = 0.683, σ~M~/σ~A~ = 1.02, benchmark 0.903). Even a child weight of 0.5 with equal volatilities gives a benchmark of about 0.7.

![](/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/docx_build/../outputs/figures/fig5_floor_contour.png){width=6.3in}

::: {custom-style="figurecaption"}
**Fig. 4** Zero-correlation benchmark ρ̲ as a function of the child weight w and the relative volatility σ~M~/σ~A~
:::
::: {custom-style="Compact"}
Notes: Contours of Eq. (8) with κ = (1 − w)σ~M~/(wσ~A~); triangle: VN30 in VN100, daily Pearson moments. Source: Authors’ calculations.
:::

::: {custom-style="heading2"}
5.4 Horizon dependence (H2)
:::

::: {custom-style="p1a"}
Table 6 lists reliable-range slopes for the four main pairs with bootstrap, studentized and adjusted p-values.
:::

::: {custom-style="tablecaption"}
**Table 6** Reliable-range scaling slopes of DCCA coefficients
:::

| Frequency | Pair | Slope [95% CI] | p (bootstrap) | p (studentized) | Holm, 19 tests | Holm, H2 family | TOST p |
|---|---|---|---|---|---|---|---|
| Daily (1D) | VN30–VNINDEX | 0.0010 [−0.0031, 0.0043] | 0.700 | 0.602 | 1.000 | 1.000 | – |
| Daily (1D) | VN100–VNINDEX | 0.0008 [−0.0021, 0.0027] | 0.736 | 0.530 | 1.000 | 1.000 | – |
| Daily (1D) | VN30–VN100 | −0.0008 [−0.0023, 0.0008] | 0.348 | 0.319 | 1.000 | – | 0.385 |
| Daily (1D) | P~cap~–VN30 | −0.0040 [−0.0157, 0.0085] | 0.576 | 0.512 | 1.000 | – | – |
| 30-minute (M30) | VN30–VNINDEX | 0.0022 [0.0007, 0.0038] | 0.012 | 0.009 | 0.144 | 0.045 | – |
| 30-minute (M30) | VN100–VNINDEX | 0.0022 [0.0011, 0.0032] | < 0.005 | < 0.001 | 0.002 | < 0.001 | – |
| 30-minute (M30) | VN30–VN100 | −0.0001 [−0.0007, 0.0007] | 0.980 | 0.863 | 1.000 | – | 0.007 |
| 30-minute (M30) | P~cap~–VN30 | 0.0017 [−0.0045, 0.0078] | 0.520 | 0.603 | 1.000 | – | – |
| 1-hour (H1) | VN30–VNINDEX | 0.0024 [0.0006, 0.0041] | 0.012 | 0.006 | 0.101 | 0.039 | – |
| 1-hour (H1) | VN100–VNINDEX | 0.0019 [0.0007, 0.0032] | 0.012 | 0.006 | 0.101 | 0.039 | – |
| 1-hour (H1) | VN30–VN100 | 0.0001 [−0.0007, 0.0009] | 0.652 | 0.884 | 1.000 | – | 0.012 |
| 1-hour (H1) | P~cap~–VN30 | 0.0020 [−0.0035, 0.0089] | 0.392 | 0.552 | 1.000 | – | – |
| 4-hour (H4) | VN30–VNINDEX | 0.0003 [−0.0026, 0.0029] | 0.852 | 0.807 | 1.000 | 1.000 | – |
| 4-hour (H4) | VN100–VNINDEX | 0.0002 [−0.0018, 0.0021] | 0.800 | 0.856 | 1.000 | 1.000 | – |
| 4-hour (H4) | VN30–VN100 | −0.0004 [−0.0018, 0.0007] | 0.628 | 0.541 | 1.000 | – | 0.142 |
| 4-hour (H4) | P~cap~–VN30 | −0.0020 [−0.0124, 0.0067] | 0.760 | 0.667 | 1.000 | – | – |

::: {custom-style="Compact"}
Notes: Slopes β of Eq. (13) over s ≤ s~rel~. Holm, 19 tests: studentized p adjusted over the original 19 tests, which include three statistical proxies at M30 (Table S8); H2 family: the eight broad-market tests; TOST: equivalence to zero with a margin of 0.001. Source: Authors’ calculations.
:::

Positive slopes appear only for broad-market pairs at the M30 and H1 frequencies. In the H2 family, four slopes survive Holm adjustment (VN100–VNINDEX at H1; VN30–VNINDEX at H1; VN100–VNINDEX at M30; VN30–VNINDEX at M30), with estimates of 0.0019–0.0024, a rise of about 0.01 across the reliable range. None is significant at 1D or H4; with significant positive slopes at both frequencies the rule requires, H2 is supported on the full data. Over the original 19 tests, Holm keeps one studentized slope and Benjamini–Hochberg four, and with percentile p-values none survives (smallest Benjamini–Hochberg-adjusted p = 0.057). The VN30–VN100 slope is equivalent to zero at M30 and H1 (TOST p = 0.007, 0.012), and the test is inconclusive elsewhere. The P~cap~–VN30 slope is not significant at any frequency.

Eq. (14) explains the flat nested slope: the damping factor is 0.106–0.112, at M30 and H1 the κ channel partly offsets the ρ~AM~ channel, and the implied slope differs from the observed one by at most 0.8 × 10⁻⁵ (Table S13). A flat nested coefficient therefore says little about the tiers: a purged slope of 0.01 per unit of ln s, five times the broad-market slopes, would move the nested slope by about 0.001, the TOST margin.

The auction bars drive the intraday result. The first bar of each day holds the overnight return and the opening auction, where intraday volatility peaks (Andersen and Bollerslev 1997). It accounts for 10% of M30 bars but carries 37% of squared VN30 returns. The last bar holds the closing auction (Table S7). Without the opening bar, the H1 broad-market slopes fall to 0.0003 and −0.0005, and at M30 only VN30–VNINDEX stays significant (0.0020, p = 0.031). Without both auction bars, the M30 slopes are −0.00002 and −0.0002. Within the same replicates, the broad-market slopes exceed the VN30–VN100 slope at M30 and H1 (differences 0.0018–0.0024, p ≤ 0.003), but the differences vanish without the auction bars. The three-pair gap does not change (0.107 [0.094, 0.127] at M30 without the opening bar), and the slope intervals are stable across block lengths (Table S15). Horizon dependence is thus a property of the bars containing the overnight return and the call auctions, not of continuous trading. It is consistent with the Epps (1979) mechanism if the auctions are where prices of less liquid constituents catch up.

::: {custom-style="heading2"}
5.5 Crisis dependence (H3)
:::

::: {custom-style="p1a"}
Table 7 presents the Forbes–Rigobon and single-factor tests under three regime definitions.
:::

::: {custom-style="tablecaption"}
**Table 7** Crisis dependence between P~cap~ and VN30: adjusted correlation and factor-model tests
:::

| Regime definition | ρ~low~ | ρ~high~ | ρ* − ρ~low~ [95% CI] | p (FR) | β_low | β_high | Δβ [95% CI] | Residual variance ratio [95% CI] |
|---|---|---|---|---|---|---|---|---|
| Chronological episodes | 0.847 | 0.924 | −0.044 [−0.082, 0.001] | 0.985 | 0.919 | 0.927 | 0.008 [−0.128, 0.140] | 1.42 [0.91, 2.15] |
| VNINDEX volatility quartiles | 0.727 | 0.928 | −0.066 [−0.132, 0.008] | 0.974 | 0.716 | 0.956 | 0.240 [0.143, 0.332] | 2.57 [1.75, 3.66] |
| VN30 volatility quartiles | 0.744 | 0.932 | −0.087 [−0.144, −0.018] | 0.998 | 0.737 | 0.948 | 0.210 [0.119, 0.306] | 2.70 [1.92, 3.68] |

::: {custom-style="Compact"}
Notes: Daily returns; ρ* from Eq. (15); p (FR): one-sided Forbes–Rigobon bootstrap p-value for H0: ρ* ≤ ρ~low~; β: OLS slope of P~cap~ on VN30; residual variance ratio: crisis over calm. Chronological: 1,000 calm and 539 crisis days; quartiles: 739 days per regime. Source: Authors’ calculations.
:::

The raw correlation rises under every regime definition, from 0.847 to 0.924 chronologically and from 0.744 to 0.932 under VN30 quartiles. The adjusted crisis correlation, however, never exceeds its calm level (one-sided p = 0.974–0.998, and above 0.93 across weights; Table S10), and under VN30 quartiles it is significantly lower (−0.087, [−0.144, −0.018]).

The factor model explains why. The residual variance of P~cap~ rises by a factor of 2.70 [1.92, 3.68] under VN30 quartiles (2.57 under VNINDEX quartiles), which violates the assumption behind Eq. (15) and pushes ρ* down (Corsetti et al. 2005). The loading rises from 0.737 to 0.948 under VN30 quartiles (Δβ = 0.210, [0.119, 0.306], p < 0.001) but not between chronological episodes (Δβ = 0.008, [−0.128, 0.140]), and adding 2021 as a crisis (789 days) changes neither result (Forbes–Rigobon p = 0.987; Δβ = −0.005, [−0.122, 0.124]). Under its decision rule, H3 is not supported: on high-VN30-volatility days, mid caps respond more strongly to large caps and also carry more mid-cap-specific risk. Because the lower-tail dependence of P~cap~–VN30 (0.75 at the 5% quantile) exceeds its Gaussian-copula value (0.62; Table S5), we cannot tell a structural shift from a stable nonlinear relation.

::: {custom-style="heading2"}
5.6 Portfolio variance (E3, H4)
:::

::: {custom-style="p1a"}
Table 8 reports the in-sample misstatement from a static correlation and the out-of-sample forecast comparison.
:::

::: {custom-style="tablecaption"}
**Table 8** Portfolio variance: in-sample misstatement and out-of-sample forecast comparison
:::

| Regime or pair | Pair or static QLIKE | RE, % [95% CI] or EWMA QLIKE | Relative SE, % or regime QLIKE | RE/SE or DM, static vs EWMA | DM, static vs regime |
|---|---|---|---|---|---|
| *Panel A: in-sample misstatement (E3)* |  |  |  |  |  |
| Chronological, calm | P~cap~–VN30 | 2.23 [0.71, 3.98] | 15.6 | 0.14 |  |
| Chronological, calm | VN30–VN100 | 0.28 [0.11, 0.45] | 13.3 | 0.02 |  |
| Chronological, crisis | P~cap~–VN30 | −1.84 [−3.01, −0.82] | 14.3 | 0.13 |  |
| Chronological, crisis | VN30–VN100 | −0.19 [−0.33, −0.08] | 14.8 | 0.01 |  |
| VNINDEX quartiles, calm | P~cap~–VN30 | 9.38 [6.28, 13.27] | 6.3 | 1.50 |  |
| VNINDEX quartiles, calm | VN30–VN100 | 0.77 [0.49, 1.14] | 5.3 | 0.14 |  |
| VNINDEX quartiles, crisis | P~cap~–VN30 | −2.07 [−2.88, −1.40] | 8.8 | 0.23 |  |
| VNINDEX quartiles, crisis | VN30–VN100 | −0.20 [−0.30, −0.13] | 8.9 | 0.02 |  |
| *Panel B: out-of-sample, 2023–2025 (H4)* |  |  |  |  |  |
| P~cap~–VN30 | −7.7771 | −7.7434 | −7.7644 | −1.69 (0.091) | −1.34 (0.179) |
| VN30–VN100 | −7.8357 | −7.8315 | −7.8346 | −1.74 (0.081) | −1.45 (0.146) |
| VN30–VNINDEX | −7.9298 | −7.9258 | −7.9252 | −1.82 (0.069) | −1.44 (0.150) |
| VN100–VNINDEX | −7.8904 | −7.8880 | −7.8867 | −1.64 (0.100) | −1.43 (0.153) |

::: {custom-style="Compact"}
Notes: Panel A: RE of Eq. (16) for an equally weighted position; relative SE: bootstrap standard error of the regime portfolio variance. Panel B: mean QLIKE over 735 evaluation days; DM: Diebold–Mariano t-statistic (p) on the QLIKE difference, negative when the static correlation has the lower loss. Source: Authors’ calculations.
:::

In sample, a static correlation overstates the variance of an equally weighted VN30 and P~cap~ position by 2.23% in chronological calm periods and 9.38% in the low-volatility quartile, and understates it by 1.84% and 2.07% in crisis regimes. Any pooled correlation produces this sign pattern. For nested pairs, the misstatement is at most 2.35% (Table S14). Relative to sampling error, the magnitudes are small: \|RE\| is 0.13–1.50 standard errors of the regime variance for P~cap~–VN30 and at most 0.43 for nested pairs. Out of sample, the static correlation has the lowest mean QLIKE for every pair, and all Diebold–Mariano statistics are negative (p = 0.069–0.179). H4 is not supported: regime variation in correlations is real in sample but too small or too poorly timed to exploit.

::: {custom-style="heading2"}
5.7 Further robustness
:::

::: {custom-style="p1a"}
None of the further checks changes the conclusions. DMCA (Kristoufek 2014) satisfies the same identity, so it checks only the detrending; it gives a purged coefficient of 0.882–0.891 and a three-pair gap of 0.086–0.096 (Table S4). The daily three-pair gap interval stays within 0.070–0.119 for blocks of 5–60 days (Table S6), and the daily VN30–VNINDEX average is 0.9665, 0.9663 and 0.9667 for detrending orders 1–3. Proxies that replace the free-float weight, such as the VN30–VN100 correlation (0.9865–0.9885), are unstable (Table S8), and shuffled surrogates attribute most of the multifractal range to fat tails (Fig. S1). Lead–lag, hedge-effectiveness and episode statistics are in Tables S9, S11 and S12.
:::

::: {custom-style="heading2"}
5.8 Summary
:::

::: {custom-style="p1a"}
Table 9 summarizes the estimands and hypotheses.
:::

::: {custom-style="tablecaption"}
**Table 9** Summary of estimands and hypothesis tests
:::

| Item | Statistic | Evidence | Outcome | Comment |
|---|---|---|---|---|
| E1 Benchmark and attribution | ρ̲; Shapley overlap share | ρ̲ 0.893–0.900; Shapley 0.505–0.508 | Estimated (not a test) | Attribution depends mainly on the weight |
| E2 Sensitivity | Eq. (10) | 0.106–0.112; with weight uncertainty 0.07–0.17 | Estimated (not a test) | Purged changes damped about tenfold |
| E3 In-sample misstatement | RE, Eq. (16) | P~cap~–VN30 −2.1% to 9.4%; mostly below one SE | Estimated (not a test) | Sign pattern expected from pooling |
| H1 Material overlap gap | Like-for-like gap; lower CI > 0.05 | Gap 0.099–0.104; lower CI ≥ 0.084 | Supported | Holds under weight uncertainty |
| H2 Horizon dependence | Studentized slopes; Holm (H2 family); TOST | 4 of 8 broad-market slopes significant, all at M30 or H1; VN30–VN100 equivalent to zero at M30, H1 | Supported | Not robust: vanishes without the auction bars |
| H3 Contagion | Forbes–Rigobon adjustment and Δβ, VN30 regimes | Forbes–Rigobon p = 0.998; Δβ = 0.210, p < 0.001 | Not supported | Loading rises on high-volatility days; residual variance rises too |
| H4 Value of regime conditioning | QLIKE; Diebold–Mariano | Static lowest for all pairs; p 0.07–0.18 | Not supported | Static correlation has the lowest loss |

::: {custom-style="Compact"}
Notes: Decision rules for H1–H4 in Section 2.7; all tests at the 5% level. Source: Authors’ calculations.
:::

::: {custom-style="heading1"}
6 Discussion
:::

::: {custom-style="heading2"}
6.1 Mechanisms
:::

::: {custom-style="p1a"}
One mechanism drives the nested results. A child’s variation enters every covariance and both standard deviations of a nested pair, and Lemma 1 pins the coefficient near a benchmark set by weight and relative amplitude. With VN30 at 68% of VN100, the benchmark is near 0.90 and the bound near 0.87, so the observed 0.99 says little about how mid caps move with large caps. Changes in the purged coefficient reach it damped about tenfold.
:::

The purged series has the features the size literature predicts. Daily VN30 returns lead P~cap~ returns (cross-autocorrelation 0.084, [0.028, 0.136]) while the reverse is negligible (0.007), an asymmetry of 0.076 [0.048, 0.102] in line with Lo and MacKinlay (1990) and Hou (2007); at intraday frequencies the lead is symmetric (Table S9). The auction-bar horizon dependence of broad-market pairs fits the Epps (1979) effect for small, less liquid stocks (Chen et al. 2021; Tran and Tran 2025), which index-level data cannot separate from gradual diffusion (Hong and Stein 1999). The higher loading on high-volatility days has several candidate sources that our data cannot rank: herding (Nguyen et al. 2023) and sector connectedness (Bui et al. 2022), limit hits under the ±7% band, margin calls and foreign flows concentrated in large caps with room under ownership limits. The rise in residual variance shows that crises also bring mid-cap-specific shocks, which the Forbes–Rigobon correction misreads as lower dependence.

::: {custom-style="heading2"}
6.2 Implications
:::

::: {custom-style="p1a"}
Users who judge diversification between tiers from nested index correlations should first decompose them. Box 1 does this from published series and the index weight. Its key outputs are the purged coefficient and the sensitivity, whose inverse of about 10 shows how ill-conditioned the index-level number is: an error of 0.001 in the nested coefficient becomes about 0.01 in the purged one. Holdings-based risk models are not affected. For hedging, a minimum-variance VN30 hedge removes a share ρ² of mid-cap variance (Ederington 1979), 0.79 [0.75, 0.82] over the full sample but 0.53 [0.45, 0.61] in the low-volatility quartile and 0.86 in the high-volatility quartile (Table S11). A holder of the VNMIDCAP exchange-traded fund who hedges with VN30 futures keeps about a fifth of the variance on average and about half in calm markets. A mid-cap derivative would remove this basis risk; we do not study whether such a contract would be viable. The case for regime-conditioned tier correlations is not supported: their in-sample gain is mostly within sampling error and vanishes out of sample. For users of index-level data, the error that matters is reading a nested correlation as evidence of diversification.
:::

::: {custom-style="heading2"}
6.3 Transferability and limitations
:::

::: {custom-style="p1a"}
Lemma 1 applies to any child contained in its parent with a known weight under one weighting scheme. Fig. 4 shows benchmarks above 0.7 whenever the child holds half of the parent and the remaining constituents are no more volatile, so large components fixed by construction should be common in families such as SET50 within SET100 or IDX30 within LQ45; we did not compute them because we could not verify their weights. With partial overlap, the shared constituents form a third component, and Eq. (7) does not apply directly. We did not decompose the broad-market pairs: VNINDEX uses full capitalization and VN100 free-float capitalization, so VN100 is not a fixed-weight component of VNINDEX. The mismatch term of Eq. (12) cannot be bounded without constituent data, and the three-pair gap is therefore descriptive for these pairs.
:::

The evidence comes from one exchange and three indices, so the magnitudes should not be generalized beyond the HOSE. The purged series rests on one factsheet weight; a weight path from semi-annual reviews would narrow the attribution intervals, which weight error dominates. We could not validate P~cap~ against the published VNMIDCAP index or the FUEDCMID net asset value, so we call ρ~AM~ overlap-purged rather than economic. Index-level prices cannot separate microstructure from diffusion, crisis evidence depends on the regime definition, and the out-of-sample period covers three years. The FTSE Russell reclassification from September 2026 offers a test: if foreign inflows raise the large-cap weight or lower the volatility of the remaining constituents relative to large caps, Eq. (8) predicts a higher benchmark.

::: {custom-style="heading1"}
7 Conclusion
:::

::: {custom-style="p1a"}
Correlations between nested equity indices contain a component fixed by construction. Extending the part–whole identity to scale-wise detrended coefficients yields a benchmark, a lower bound, a sensitivity and an order-free attribution, all computable from index-level inputs. On the HOSE, the VN30–VN100 coefficient moves by only about 0.11 per unit change in the purged coefficient, and removing the overlap lowers the correlation with large caps by about 0.10. The purged series shows a large-to-small lead, horizon effects confined to the auction bars, a higher mid-cap loading together with more mid-cap-specific risk on volatile days, and no out-of-sample gain from regime-conditioned correlations. Users of index-level data should decompose nested correlations before reading them as evidence about diversification between tiers.
:::

::: {custom-style="p1a"}
**Ethical standards** This study uses only publicly available historical index price data from the Ho Chi Minh City Stock Exchange; it involves no human participants or personal data, therefore required no ethical approval, and complies with the current laws of Vietnam.
:::

::: {custom-style="p1a"}
**Data availability** The index price data were obtained from TradingView (exchange: HOSE) and are subject to the vendor’s terms of use; the merged dataset is available from the corresponding author upon reasonable request.
:::

::: {custom-style="p1a"}
**Code availability** The R code that reproduces every table and figure, with a map from each reported number to its output file, is provided as Online Resource 1 and will be deposited in a public repository upon acceptance. Supplementary tables and figures are provided as Online Resource 2.
:::

::: {custom-style="p1a"}
**Funding** Funding information is provided on the separate title page in accordance with the journal’s double-blind review policy.
:::

::: {custom-style="p1a"}
**Conflict of interest** The authors declare that they have no conflict of interest.
:::

::: {custom-style="p1a"}
**Declaration of generative AI use** During the preparation of this work the authors used Claude (Anthropic) for language editing, reference searching and verification, translation of the analysis code into R and drafting of revisions, and Gemini (Google) to improve the language and readability of the manuscript. After using these tools, the authors reviewed and edited the content as needed and take full responsibility for the content of the publication.
:::

::: {custom-style="heading1"}
References
:::

::: {custom-style="referenceitem"}
Abdul Karim, B., & Xin Ning, H. (2013). Driving forces of the ASEAN-5 stock markets integration. Asia-Pacific Journal of Business Administration, 5(3), 186–191. https://doi.org/10.1108/APJBA-07-2012-0053
:::

::: {custom-style="referenceitem"}
Akhtaruzzaman, M., Boubaker, S., & Sensoy, A. (2021). Financial contagion during COVID–19 crisis. Finance Research Letters, 38, 101604. https://doi.org/10.1016/j.frl.2020.101604
:::

::: {custom-style="referenceitem"}
Al Rababa’a, A. R., Alomari, M., & McMillan, D. (2021). Multiscale stock-bond correlation: Implications for risk management. Research in International Business and Finance, 58, 101435. https://doi.org/10.1016/j.ribaf.2021.101435
:::

::: {custom-style="referenceitem"}
Andersen, T. G., & Bollerslev, T. (1997). Intraday periodicity and volatility persistence in financial markets. Journal of Empirical Finance, 4(2–3), 115–158. https://doi.org/10.1016/S0927-5398(97)00004-2
:::

::: {custom-style="referenceitem"}
Ang, A., & Chen, J. (2002). Asymmetric correlations of equity portfolios. Journal of Financial Economics, 63(3), 443–494. https://doi.org/10.1016/S0304-405X(02)00068-5
:::

::: {custom-style="referenceitem"}
Barberis, N., Shleifer, A., & Wurgler, J. (2005). Comovement. Journal of Financial Economics, 75(2), 283–317. https://doi.org/10.1016/j.jfineco.2004.04.003
:::

::: {custom-style="referenceitem"}
Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. Journal of the Royal Statistical Society: Series B (Methodological), 57(1), 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x
:::

::: {custom-style="referenceitem"}
Benkraiem, R., Garfatta, R., Lakhal, F., & Zorgati, I. (2022). Financial contagion intensity during the COVID-19 outbreak: A copula approach. International Review of Financial Analysis, 81, 102136. https://doi.org/10.1016/j.irfa.2022.102136
:::

::: {custom-style="referenceitem"}
Bui, H. Q., Tran, T., Pham, T. T., Nguyen, H. L.-P., & Vo, D. H. (2022). Market volatility and spillover across 24 sectors in Vietnam. Cogent Economics & Finance, 10(1), 2122188. https://doi.org/10.1080/23322039.2022.2122188
:::

::: {custom-style="referenceitem"}
Chang, P., Pienaar, E., & Gebbie, T. (2021). The Epps effect under alternative sampling schemes. Physica A: Statistical Mechanics and its Applications, 583, 126329. https://doi.org/10.1016/j.physa.2021.126329
:::

::: {custom-style="referenceitem"}
Chen, H., Singal, V., & Whitelaw, R. F. (2016). Comovement revisited. Journal of Financial Economics, 121(3), 624–644. https://doi.org/10.1016/j.jfineco.2016.05.007
:::

::: {custom-style="referenceitem"}
Chen, R., Geng, H., Lin, H., & Nguyen, P. T. L. (2021). Liquidity, informed trading, and a market surveillance system: Evidence from the Vietnamese stock market. Pacific-Basin Finance Journal, 67, 101567. https://doi.org/10.1016/j.pacfin.2021.101567
:::

::: {custom-style="referenceitem"}
Chen, Y., Zhang, J., Lu, L., & Xie, Z. (2024). Cross-correlation and multifractality analysis of the Chinese and American stock markets based on the MF-DCCA model. Heliyon, 10(17), e36537. https://doi.org/10.1016/j.heliyon.2024.e36537
:::

::: {custom-style="referenceitem"}
Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Lawrence Erlbaum Associates. https://doi.org/10.4324/9780203771587
:::

::: {custom-style="referenceitem"}
Corsetti, G., Pericoli, M., & Sbracia, M. (2005). ‘Some contagion, some interdependence’: More pitfalls in tests of financial contagion. Journal of International Money and Finance, 24(8), 1177–1199. https://doi.org/10.1016/j.jimonfin.2005.08.012
:::

::: {custom-style="referenceitem"}
Cremers, K. J. M., & Petajisto, A. (2009). How active is your fund manager? A new measure that predicts performance. The Review of Financial Studies, 22(9), 3329–3365. https://doi.org/10.1093/rfs/hhp057
:::

::: {custom-style="referenceitem"}
Cureton, E. E. (1966). Corrected item-test correlations. Psychometrika, 31(1), 93–96. https://doi.org/10.1007/BF02289461
:::

::: {custom-style="referenceitem"}
DeCoste, J. (2025). Comovement and S&P 500 membership. Global Finance Journal, 65, 101110. https://doi.org/10.1016/j.gfj.2025.101110
:::

::: {custom-style="referenceitem"}
Diebold, F. X., & Mariano, R. S. (1995). Comparing predictive accuracy. Journal of Business & Economic Statistics, 13(3), 253–263. https://doi.org/10.1080/07350015.1995.10524599
:::

::: {custom-style="referenceitem"}
Ederington, L. H. (1979). The hedging performance of the new futures markets. The Journal of Finance, 34(1), 157–170. https://doi.org/10.1111/j.1540-6261.1979.tb02077.x
:::

::: {custom-style="referenceitem"}
Epps, T. W. (1979). Comovements in stock prices in the very short run. Journal of the American Statistical Association, 74(366), 291–298. https://doi.org/10.1080/01621459.1979.10482508
:::

::: {custom-style="referenceitem"}
Forbes, K. J., & Rigobon, R. (2002). No contagion, only interdependence: Measuring stock market comovements. The Journal of Finance, 57(5), 2223–2261. https://doi.org/10.1111/0022-1082.00494
:::

::: {custom-style="referenceitem"}
FTSE Russell. (2025, October 7). FTSE Russell announces results of September 2025 semi-annual country classification review [Press release]. London Stock Exchange Group. https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2025/ftse-russell-country-classification-september-2025
:::

::: {custom-style="referenceitem"}
Ge, X., & Lin, A. (2021). Multiscale multifractal detrended partial cross-correlation analysis of Chinese and American stock markets. Chaos, Solitons & Fractals, 145, 110731. https://doi.org/10.1016/j.chaos.2021.110731
:::

::: {custom-style="referenceitem"}
Government of Vietnam. (2020). Decree No. 155/2020/ND-CP of 31 December 2020 detailing and guiding the implementation of a number of articles of the Law on Securities. Hanoi.
:::

::: {custom-style="referenceitem"}
Government of Vietnam. (2025). Decree No. 245/2025/ND-CP of 11 September 2025 amending and supplementing a number of articles of Decree No. 155/2020/ND-CP. Hanoi.
:::

::: {custom-style="referenceitem"}
Greenwood, R. (2008). Excess comovement of stock returns: Evidence from cross-sectional variation in Nikkei 225 weights. The Review of Financial Studies, 21(3), 1153–1186. https://doi.org/10.1093/rfs/hhm052
:::

::: {custom-style="referenceitem"}
Greenwood, R., & Sammon, M. (2025). The disappearing index effect. The Journal of Finance, 80(2), 657–698. https://doi.org/10.1111/jofi.13410
:::

::: {custom-style="referenceitem"}
Guedes, E. F., da Silva Filho, A. M., & Zebende, G. F. (2021). Detrended multiple cross-correlation coefficient with sliding windows approach. Physica A: Statistical Mechanics and its Applications, 574, 125990. https://doi.org/10.1016/j.physa.2021.125990
:::

::: {custom-style="referenceitem"}
Guo, Y., Li, P., & Li, A. (2021). Tail risk contagion between international financial markets during COVID-19 pandemic. International Review of Financial Analysis, 73, 101649. https://doi.org/10.1016/j.irfa.2020.101649
:::

::: {custom-style="referenceitem"}
Ho Chi Minh City Stock Exchange. (2022, September 29). Listing and official trading of DCVFMVNMIDCAP ETF fund certificates [Press release]. HOSE.
:::

::: {custom-style="referenceitem"}
Holm, S. (1979). A simple sequentially rejective multiple test procedure. Scandinavian Journal of Statistics, 6(2), 65–70. https://www.jstor.org/stable/4615733
:::

::: {custom-style="referenceitem"}
Hong, H., & Stein, J. C. (1999). A unified theory of underreaction, momentum trading, and overreaction in asset markets. The Journal of Finance, 54(6), 2143–2184. https://doi.org/10.1111/0022-1082.00184
:::

::: {custom-style="referenceitem"}
Hou, K. (2007). Industry information diffusion and the lead-lag effect in stock returns. The Review of Financial Studies, 20(4), 1113–1138. https://doi.org/10.1093/rfs/hhm003
:::

::: {custom-style="referenceitem"}
J.P. Morgan/Reuters. (1996). RiskMetrics: Technical document (4th ed.). Morgan Guaranty Trust Company.
:::

::: {custom-style="referenceitem"}
Jiang, Z.-Q., & Zhou, W.-X. (2011). Multifractal detrending moving-average cross-correlation analysis. Physical Review E, 84(1), 016106. https://doi.org/10.1103/PhysRevE.84.016106
:::

::: {custom-style="referenceitem"}
Kakinaka, S., Hayakawa, T., Kato, D., & Umeno, K. (2025). Fractal portfolio strategies: Does scale preference of investors matter? Applied Economics Letters, 32(3), 415–421. https://doi.org/10.1080/13504851.2023.2274298
:::

::: {custom-style="referenceitem"}
Kantelhardt, J. W., Zschiegner, S. A., Koscielny-Bunde, E., Havlin, S., Bunde, A., & Stanley, H. E. (2002). Multifractal detrended fluctuation analysis of nonstationary time series. Physica A: Statistical Mechanics and its Applications, 316(1–4), 87–114. https://doi.org/10.1016/S0378-4371(02)01383-3
:::

::: {custom-style="referenceitem"}
Kristoufek, L. (2014). Detrending moving-average cross-correlation coefficient: Measuring cross-correlations between non-stationary series. Physica A: Statistical Mechanics and its Applications, 406, 169–175. https://doi.org/10.1016/j.physa.2014.03.015
:::

::: {custom-style="referenceitem"}
Le, T. T. V., Dang, T. P. T., & Phan, T. H. N. (2025). The nonlinear dependence of the Vietnam stock market on the Asian stock market: Evidence from a quantile-on-quantile regression. International Journal of Innovative Research and Scientific Studies, 8(4), 535–553. https://doi.org/10.53894/ijirss.v8i4.7901
:::

::: {custom-style="referenceitem"}
Lean, H. H., & Teng, K. T. (2013). Integration of world leaders and emerging powers into the Malaysian stock market: A DCC-MGARCH approach. Economic Modelling, 32, 333–342. https://doi.org/10.1016/j.econmod.2013.02.013
:::

::: {custom-style="referenceitem"}
Liao, Y., Coakley, J., & Kellard, N. (2022). Index tracking and beta arbitrage effects in comovement. International Review of Financial Analysis, 83, 102330. https://doi.org/10.1016/j.irfa.2022.102330
:::

::: {custom-style="referenceitem"}
Lo, A. W., & MacKinlay, A. C. (1990). When are contrarian profits due to stock market overreaction? The Review of Financial Studies, 3(2), 175–205. https://doi.org/10.1093/rfs/3.2.175
:::

::: {custom-style="referenceitem"}
Longin, F., & Solnik, B. (2001). Extreme correlation of international equity markets. The Journal of Finance, 56(2), 649–676. https://doi.org/10.1111/0022-1082.00340
:::

::: {custom-style="referenceitem"}
Markowitz, H. (1952). Portfolio selection. The Journal of Finance, 7(1), 77–91. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x
:::

::: {custom-style="referenceitem"}
Ministry of Finance of Vietnam. (2020). Circular No. 120/2020/TT-BTC of 31 December 2020 on trading of listed and registered shares, fund certificates, corporate bonds and covered warrants listed on the securities trading system. Hanoi.
:::

::: {custom-style="referenceitem"}
Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica, 55(3), 703–708. https://doi.org/10.2307/1913610
:::

::: {custom-style="referenceitem"}
Nguyen, H. M., Bakry, W., & Vuong, T. H. G. (2023). COVID-19 pandemic and herd behavior: Evidence from a frontier market. Journal of Behavioral and Experimental Finance, 38, 100807. https://doi.org/10.1016/j.jbef.2023.100807
:::

::: {custom-style="referenceitem"}
Okorie, D. I., & Lin, B. (2021). Stock markets and the COVID-19 fractal contagion effects. Finance Research Letters, 38, 101640. https://doi.org/10.1016/j.frl.2020.101640
:::

::: {custom-style="referenceitem"}
Oświęcimka, P., Drożdż, S., Forczek, M., Jadach, S., & Kwapień, J. (2014). Detrended cross-correlation analysis consistently extended to multifractality. Physical Review E, 89(2), 022805. https://doi.org/10.1103/PhysRevE.89.022805
:::

::: {custom-style="referenceitem"}
Patton, A. J. (2011). Volatility forecast comparison using imperfect volatility proxies. Journal of Econometrics, 160(1), 246–256. https://doi.org/10.1016/j.jeconom.2010.03.034
:::

::: {custom-style="referenceitem"}
Pearson, K. (1897). Mathematical contributions to the theory of evolution.—On a form of spurious correlation which may arise when indices are used in the measurement of organs. Proceedings of the Royal Society of London, 60, 489–498. https://doi.org/10.1098/rspl.1896.0076
:::

::: {custom-style="referenceitem"}
Peng, C.-K., Buldyrev, S. V., Havlin, S., Simons, M., Stanley, H. E., & Goldberger, A. L. (1994). Mosaic organization of DNA nucleotides. Physical Review E, 49(2), 1685–1689. https://doi.org/10.1103/PhysRevE.49.1685
:::

::: {custom-style="referenceitem"}
Podobnik, B., Jiang, Z.-Q., Zhou, W.-X., & Stanley, H. E. (2011). Statistical tests for power-law cross-correlated processes. Physical Review E, 84(6), 066118. https://doi.org/10.1103/PhysRevE.84.066118
:::

::: {custom-style="referenceitem"}
Podobnik, B., & Stanley, H. E. (2008). Detrended cross-correlation analysis: A new method for analyzing two nonstationary time series. Physical Review Letters, 100(8), 084102. https://doi.org/10.1103/PhysRevLett.100.084102
:::

::: {custom-style="referenceitem"}
Politis, D. N., & Romano, J. P. (1994). The stationary bootstrap. Journal of the American Statistical Association, 89(428), 1303–1313. https://doi.org/10.1080/01621459.1994.10476870
:::

::: {custom-style="referenceitem"}
Rigobon, R. (2003). Identification through heteroskedasticity. The Review of Economics and Statistics, 85(4), 777–792. https://doi.org/10.1162/003465303772815727
:::

::: {custom-style="referenceitem"}
Santana, T. P., Horta, N., Revez, C., Dias, R. M. T. S., & Zebende, G. F. (2023). Effects of interdependence and contagion on crude oil and precious metals according to ρDCCA: A COVID-19 case study. Sustainability, 15(5), 3945. https://doi.org/10.3390/su15053945
:::

::: {custom-style="referenceitem"}
Schuirmann, D. J. (1987). A comparison of the two one-sided tests procedure and the power approach for assessing the equivalence of average bioavailability. Journal of Pharmacokinetics and Biopharmaceutics, 15(6), 657–680. https://doi.org/10.1007/BF01068419
:::

::: {custom-style="referenceitem"}
Shapley, L. S. (1953). A value for n-person games. In H. W. Kuhn & A. W. Tucker (Eds.), Contributions to the theory of games II (pp. 307–317). Princeton University Press. https://doi.org/10.1515/9781400881970-018
:::

::: {custom-style="referenceitem"}
Tilfani, O., Ferreira, P., & El Boukfaoui, M. Y. (2021). Dynamic cross-correlation and dynamic contagion of stock markets: A sliding windows approach with the DCCA correlation coefficient. Empirical Economics, 60(3), 1127–1156. https://doi.org/10.1007/s00181-019-01806-1
:::

::: {custom-style="referenceitem"}
Tran, M. H., & Tran, N. M. (2025). High-frequency dynamics of the Vietnam stock market. VNU Journal of Economics and Business, 5(2), 51–59. https://doi.org/10.57110/vnu-jeb.v5i2.395
:::

::: {custom-style="referenceitem"}
Vietnam Securities Depository. (2015). Decision No. 211/QĐ-VSD of 18 December 2015 promulgating the Regulation on clearing and settlement of securities transactions. Hanoi.
:::

::: {custom-style="referenceitem"}
Wang, F., Ye, X., Chen, H., & Wu, C. (2021). A portfolio strategy of stock market based on mean-MF-X-DMA model. Chaos, Solitons & Fractals, 143, 110645. https://doi.org/10.1016/j.chaos.2020.110645
:::

::: {custom-style="referenceitem"}
Zebende, G. F. (2011). DCCA cross-correlation coefficient: Quantifying level of cross-correlation. Physica A: Statistical Mechanics and its Applications, 390(4), 614–618. https://doi.org/10.1016/j.physa.2010.10.022
:::

::: {custom-style="referenceitem"}
Zhou, W., Huang, J., & Wang, M. (2025). Multifractal characteristics and information flow analysis of stock markets based on multifractal detrended cross-correlation analysis and transfer entropy. Fractal and Fractional, 9(1), 14. https://doi.org/10.3390/fractalfract9010014
:::

::: {custom-style="referenceitem"}
Zhou, W.-X. (2008). Multifractal detrended cross-correlation analysis for two nonstationary signals. Physical Review E, 77(6), 066211. https://doi.org/10.1103/PhysRevE.77.066211
:::
