::: {custom-style="Title"}
How Much of a Nested Index Correlation Is Construction? A Scale-Wise Part–Whole Decomposition with Evidence from Vietnam
:::

::: {custom-style="p1a"}
Nguyen Thanh Binh^a^, Nguyen Van Trung^a,\*^, Ha Hong Hanh^b^, Nguyen Bach Diep^a^
:::

::: {custom-style="Compact"}
^a^ Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam
:::

::: {custom-style="Compact"}
^b^ School of Accounting and Auditing, National Economics University, Hanoi, Vietnam
:::

::: {custom-style="Compact"}
\* Corresponding author: Nguyen Van Trung, Academy of Policy and Development, Hanoi, Vietnam. Email: 15233582\@st.neu.edu.vn. Tel: +84 355 347 831.
:::

::: {custom-style="abstract"}
**Abstract** When one equity index contains another, part of their correlation is fixed by construction. We carry the classical part–whole correlation identity over to detrended cross-correlation analysis (DCCA). At every timescale, the coefficient between a parent and a child index is then a closed-form function of the child’s weight, the relative amplitude of the remaining constituents and the overlap-purged correlation between the child and those constituents. The identity gives a zero-correlation benchmark, an exact lower bound, the sensitivity of the nested coefficient to the purged correlation and an order-free attribution, and it needs only index-level inputs. On the Ho Chi Minh City Stock Exchange (VN30 within VN100 within VNINDEX, 30-minute to daily data, 2014–2025), the VN30–VN100 coefficient moves by only about 0.11 per unit change in the purged correlation, and purging the overlap lowers the correlation with large caps by about 0.10 at every frequency. The decomposition barely varies across scales and frequencies, so its Pearson version suffices in these data. The small intraday horizon dependence of broad-market pairs comes from the opening and closing auction bars, evidence of crisis contagion depends on the test used, and regime-conditioned correlations do not improve out-of-sample portfolio variance forecasts. Correlations between nested indices therefore say little about diversification between size tiers unless the overlap is removed first.
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
Correlations between published equity indices are a convenient summary of dependence. They are available at every frequency, require no holdings data and are easy to compare across markets, so they are a natural input when the question is how much one segment of a market diversifies another (Markowitz 1952). In nested index systems the number has a problem that has nothing to do with estimation error: the parent index contains the child index, so part of their correlation is fixed by construction. On the Ho Chi Minh City Stock Exchange (HOSE), the large-cap VN30 index is contained in VN100, which is contained in the market-wide VNINDEX:
:::

$$
\mathrm{VN30} \subset \mathrm{VN100} \subset \mathrm{VNINDEX}. \qquad (1)
$$

Because the 30 largest firms hold about two-thirds of the free-float capitalization of VN100, the correlation between VN30 and VN100 returns is close to one (0.988 at the daily frequency). If such a number is read as a measure of how mid caps move with large caps, it mixes two things: the economic linkage between the tiers and the fact that VN30 stocks are counted on both sides. Holdings-based risk models avoid the problem because they work with constituents. Users who observe only index levels, or who compare benchmarks across frequencies, cannot, and the co-movement literature shows that index-level co-movement is easy to misread even without overlap (Chen et al. 2016).

The arithmetic behind the problem is old. Pearson (1897) described the spurious correlation between quantities that share a component, and the psychometric item–total correlation (Cureton 1966) is the same identity applied to a score and one of its items. What has been missing is a version that works for the scale-dependent, detrended coefficients now common in financial econophysics, that attaches sampling and weight uncertainty to each component, and that index users can apply. Studies of multiscale co-movement, which rely mostly on detrended cross-correlation analysis (DCCA), analyze pairs of assets that share no constituents (Section 2), so they do not address the question.

This paper builds that version. Writing the parent index return as a weighted sum of the child return and the return on the remaining constituents, we show (Lemma 1) that the DCCA coefficient of a nested pair is, at every timescale, a known function of the child’s weight, the relative amplitude κ(s) of the remaining constituents and the overlap-purged coefficient between the child and those constituents. The function delivers four quantities: a zero-correlation benchmark, the value the nested coefficient takes when the purged coefficient is zero; an exact lower bound over all purged coefficients; the sensitivity of the nested coefficient to the purged one; and an attribution that does not depend on the order in which overlap and economic dependence are switched on. The Pearson identity is the one-box special case.

We apply the decomposition to VN30, VN100 and VNINDEX at 30-minute, 1-hour, 4-hour and daily frequencies from 2014 to 2025, with inference from a stationary block bootstrap that also draws the index weight. The purged series then serves to test three economic hypotheses, on horizon dependence between tiers, crisis contagion and the out-of-sample value of regime-conditioned correlations, each with a decision rule stated in Section 2.7.

The paper makes three contributions. First, it carries the part–whole identity to scale-wise detrended coefficients and derives the benchmark, the lower bound, the sensitivity, a Shapley attribution and the analytic condition under which the benchmark exceeds half of the nested coefficient. A six-step recipe (Box 1) and a contour chart (Fig. 4) make these quantities available for any nested pair from published index data. Second, it measures the overlap component on the HOSE with inference: the nested VN30–VN100 coefficient responds to the purged coefficient with a slope of 0.106–0.112, so a change of 0.1 in the purged coefficient moves the nested one by about 0.01, and the like-for-like gap between nested and purged coefficients is 0.099–0.104. The decomposition hardly varies with the timescale (κ between 0.47 and 0.52 across all reliable scales and frequencies), so in these data the multiscale layer confirms rather than changes the Pearson answer. Third, it tests economic hypotheses on the purged series: horizon dependence appears only for broad-market pairs at intraday frequencies and comes from the opening and closing auction bars, crisis evidence depends on whether contagion is measured by an adjusted correlation or by a factor loading, and regime-conditioned correlations do not beat a static correlation out of sample.

Section 2 reviews the literature and develops the estimands and hypotheses. Section 3 describes the institutional setting and the data, Section 4 the methodology, and Section 5 the results. Section 6 discusses mechanisms, implications, transferability and limitations, and Section 7 concludes. The Supplementary Material (Online Resource 2) contains further robustness checks.

::: {custom-style="heading1"}
2 Literature review and hypothesis development
:::

::: {custom-style="p1a"}
Five literatures bear on our question: the statistics of correlations between a whole and its parts, multiscale dependence measured by detrended cross-correlation, the effect of index membership on co-movement, lead–lag effects between size tiers, and the separation of contagion from volatility-driven interdependence. We review each for what it establishes, where studies disagree and what it leaves open, and then state the gap, the estimands and the hypotheses.
:::

::: {custom-style="heading2"}
2.1 Part–whole correlation and holdings overlap
:::

::: {custom-style="p1a"}
The problem of correlating a whole with one of its parts is old. Pearson (1897) showed that two ratios sharing a common denominator are correlated even when their numerators are independent, and called the result a spurious correlation. In psychometrics the same arithmetic appears as the item–total correlation: an item is part of the total score, so its correlation with the total overstates its correlation with the other items, and Cureton (1966) gave a standard correction that removes the item from the total. Both results are static and use Pearson moments. They imply that the correlation of a parent index with a child index it contains has a component fixed by construction, but neither literature measures that component at different timescales or attaches sampling uncertainty to it.
:::

Finance deals with overlap mainly through holdings. Active Share measures the fraction of a fund’s portfolio that differs from its benchmark holdings (Cremers and Petajisto 2009), and holdings-based factor risk models estimate exposures from constituents, so neither depends on index-level return correlations. Studies of index membership control for overlap by constructing comparison portfolios from stocks outside the index (Barberis et al. 2005). What is missing is the return-based counterpart for users who observe only index levels: a way to tell, from the published series and the index weights, how much of a nested correlation reflects shared constituents.

::: {custom-style="heading2"}
2.2 Multiscale dependence and detrended cross-correlation
:::

::: {custom-style="p1a"}
Detrended cross-correlation analysis (DCCA) extends detrended fluctuation analysis (Peng et al. 1994; Kantelhardt et al. 2002) to pairs of nonstationary series (Podobnik and Stanley 2008). Zebende (2011) normalized the detrended covariance into a bounded coefficient, Podobnik et al. (2011) proposed tests for power-law cross-correlations, and Zhou (2008) generalized the method to multifractal moments (MF-DCCA). Later variants replace polynomial detrending by moving averages (Jiang and Zhou 2011; Kristoufek 2014), compute the coefficient in sliding windows (Guedes et al. 2021) or partial out third variables (Ge and Lin 2021). The variants disagree on one technical point: MF-DCCA must handle negative local covariances, and Oświęcimka et al. (2014) show that taking their absolute values can create spurious multifractality.
:::

Applied work agrees that financial dependence can vary with the horizon. Stock–bond correlations differ across horizons (Al Rababa’a et al. 2021), and cross-market correlations between China and the United States vary with scale and fluctuation size (Ge and Lin 2021; Chen et al. 2024). Two strands use the coefficient for decisions. One measures crisis transmission: Okorie and Lin (2021) find fractal contagion among 32 stock markets during COVID-19 that fades in the medium and long run, and Tilfani et al. (2021) track contagion with the coefficient in sliding windows. The other builds portfolios: a mean-MF-X-DMA rule outperforms the mean-variance model (Wang et al. 2021), and mean-DCCA portfolios perform better when the investor’s preferred scale adapts to market conditions (Kakinaka et al. 2025). Combining MF-DCCA with transfer entropy adds the direction of information flow (Zhou et al. 2025).

These strands read the DCCA coefficient as a measure of economic dependence. That reading is reasonable for disjoint assets such as stocks and bonds or two national markets. It is not reasonable when one series contains the other, because the detrended covariance then inherits the part–whole arithmetic of Section 2.1 at every scale. None of the studies above analyzes nested pairs.

::: {custom-style="heading2"}
2.3 Index membership and co-movement
:::

::: {custom-style="p1a"}
A separate literature asks whether index membership changes how stocks co-move. Barberis et al. (2005) find that stocks added to the S&P 500 co-move more with the index afterwards and attribute the change to trading frictions and investor habitats. Greenwood (2008) uses the price weighting of the Nikkei 225 to show that stocks with larger index weights co-move more with other index stocks, which points to index-linked demand. Later designs sharpen the evidence: DeCoste (2025) uses a regression discontinuity around the S&P 500 membership threshold and finds higher co-movement with no change in fundamentals, and Liao et al. (2022) attribute part of it to index trackers and beta arbitrageurs.
:::

The evidence is contested. Chen et al. (2016) show that much of the post-inclusion rise in co-movement also appears in matched stocks that were not added, so it need not reflect membership, and Greenwood and Sammon (2025) document that the price effect of S&P 500 additions has almost disappeared. The lesson for our purpose is that co-movement measured at the index level is easy to misread. This literature concerns behavior; our concern is the arithmetic overlap between indices, which raises their correlation even if no investor trades differently because of membership.

::: {custom-style="heading2"}
2.4 Size, lead–lag and horizon effects
:::

::: {custom-style="p1a"}
Returns on large stocks lead returns on small stocks: Lo and MacKinlay (1990) show that the cross-autocorrelation from large to small firms is much stronger than the reverse, and Hou (2007) traces the effect to slow diffusion of industry information to small firms. Non-synchronous trading also depresses correlations at short horizons (Epps 1979), and the size of this Epps effect depends on how prices are sampled (Chang et al. 2021). Gradual information diffusion (Hong and Stein 1999) can make co-movement build up with the horizon. Together these mechanisms predict that correlations between pairs whose constituents adjust at different speeds rise with the horizon, and that the large-cap tier leads.
:::

Vietnamese evidence suggests that these frictions are present on the Ho Chi Minh City Stock Exchange (HOSE). Liquidity fell after the introduction of a market surveillance system, especially for small firms (Chen et al. 2021), and price adjustment is delayed under retail-heavy trading (Tran and Tran 2025). The same market shows herding during stress (Nguyen et al. 2023), sector connectedness above 60% that rose to about 90% during COVID-19 (Bui et al. 2022) and nonlinear dependence on regional markets (Le et al. 2025). High connectedness and herding raise all correlations at once, which makes index-level numbers harder to interpret as evidence about the tiers.

::: {custom-style="heading2"}
2.5 Volatility, contagion and interdependence
:::

::: {custom-style="p1a"}
Equity correlations rise in downturns (Longin and Solnik 2001; Ang and Chen 2002). Forbes and Rigobon (2002) show that unadjusted correlations rise mechanically with the variance of the conditioning market, so a crisis increase may reflect interdependence rather than contagion. Their correction has known limits. Corsetti et al. (2005) show that it can be biased toward finding no contagion, because it places unrealistic restrictions on the variance of country-specific shocks, and they propose testing for a change in the factor loading within a common-factor model instead. Rigobon (2003) uses the change in variance across regimes to identify the transmission coefficient, which requires the structural parameters to stay constant.
:::

The COVID-19 literature shows how much the conclusion depends on these choices. Studies without the correction report contagion: conditional correlations between Chinese and G7 firms rose, especially for financial firms (Akhtaruzzaman et al. 2021), contagion channels multiplied in a network of 19 markets (Guo et al. 2021) and copula dependence intensified across Asian and American indices (Benkraiem et al. 2022). A DCCA-based test finds no contagion between two crude-oil benchmarks that were already highly interdependent, but contagion between crude oil and precious metals (Santana et al. 2023). In ASEAN markets integration varies with trade links and volatility (Abdul Karim and Xin Ning 2013; Lean and Teng 2013). No study applies volatility-robust tests to tiers of one market whose indices overlap.

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
| This study | VN30, VN100, VNINDEX; M30 to daily, 2014–2025 | Scale-wise part–whole identity; DCCA | Yes (scale-wise, with weight uncertainty) | Yes | Yes | Purged correlation is invisible in the nested one |

::: {custom-style="Compact"}
Notes: Overlap treated: whether the study separates dependence created by shared constituents; scale-wise: whether dependence is measured by timescale; volatility-robust test: whether crisis comparisons correct for heteroskedasticity or common shocks. Source: Authors’ compilation.
:::

Three gaps follow. First, the part–whole identity is known for static Pearson correlations, but it has not been carried to detrended, scale-by-scale coefficients, given inference that accounts for uncertainty in the index weight, or turned into a diagnostic that index users can compute from published series. Second, multiscale studies of crisis transmission rarely apply volatility-robust tests, while volatility-conditioned studies use one horizon and disjoint markets. Third, to our knowledge no study covers the Vietnamese index system at intraday and daily frequencies. Our search covered Google Scholar and publisher databases for 2021–2026, plus the classical sources these works cite, with the strings “detrended cross-correlation” combined with “index”, “overlap”, “nested” or “constituent”; “part–whole correlation” and “item–total correlation”; “contagion” with “Forbes–Rigobon” or “heteroskedasticity”; and “Vietnam” with “co-movement” or “stock index”.

::: {custom-style="heading2"}
2.7 Estimands and hypotheses
:::

::: {custom-style="p1a"}
Lemma 1 (Section 4.2) fixes several quantities once the index weight and the relative amplitude are known. We therefore separate estimands, which we report with intervals but do not test, from hypotheses, whose outcome the identity does not determine.
:::

*Estimands.* E1 is the zero-correlation benchmark ρ̲ of the VN30–VN100 coefficient and its share of the observed coefficient under three attribution conventions. E2 is the sensitivity of the nested coefficient to the purged coefficient. E3 is the in-sample misstatement of portfolio variance when a static correlation replaces a regime correlation, reported against the sampling error of the regime variance. A share above one half is not a finding: it holds whenever κ < √3 and the purged coefficient is non-negative (Section 4.2).

*H1 (material overlap gap).* The size of the overlap gap depends on the purged coefficient, which the identity does not fix: a purged coefficient close to one would leave almost no gap. We predict that the like-for-like gap, the VN30–VN100 coefficient minus the P~cap~–VN30 coefficient, exceeds 0.05, the worst-case estimation error tolerated in Section 4.4. Decision rule: the lower bound of the 95% bootstrap interval exceeds 0.05 at every frequency.

*H2 (horizon dependence).* Large-cap returns lead small-cap returns (Lo and MacKinlay 1990; Hou 2007), non-synchronous trading depresses short-horizon correlations (Epps 1979), and information diffuses gradually (Hong and Stein 1999). These mechanisms predict DCCA coefficients that rise with the timescale for broad-market pairs, whose parent contains small and less liquid stocks. For VN30–VN100 the identity predicts a slope damped by the sensitivity of Eq. (10). Decision rule: in the family of eight broad-market slope tests (two pairs, four frequencies), at least one pair at each of M30 and H1, the frequencies with several bars per session, has a positive slope with a Holm-adjusted studentized p-value below 0.05. We also report whether the result survives removal of the opening bar, and assess the VN30–VN100 prediction by an equivalence test.

*H3 (contagion).* A rise in the raw crisis correlation between P~cap~ and VN30 can come from higher volatility alone (Forbes and Rigobon 2002), and the volatility correction is itself biased toward no contagion when crises raise idiosyncratic variance (Corsetti et al. 2005). We predict contagion in the strict sense. Decision rule: under regimes sorted on VN30 volatility, both the Forbes–Rigobon adjusted correlation exceeds its calm level (one-sided p < 0.05) and the loading of P~cap~ on VN30 rises (two-sided p < 0.05).

*H4 (value of regime conditioning).* If correlations between tiers vary with the volatility regime, conditioning on the regime should improve variance forecasts for a mixed large-cap and mid-cap position. Decision rule: an EWMA or a real-time regime correlation has a lower QLIKE loss than the static correlation over 2023–2025, with a Diebold–Mariano p-value below 0.05.

The first-round version of this paper reported five hypotheses with unadjusted tests. The decision rules above, the eight-test family for H2 and the factor-loading test for H3 were fixed at revision, after the first-round results were known. We label them accordingly and also report the original specifications.

::: {custom-style="heading1"}
3 Institutional background and data
:::

::: {custom-style="heading2"}
3.1 Institutional background
:::

::: {custom-style="p1a"}
The HOSE is supervised by the State Securities Commission of Vietnam. Five features of its microstructure matter for cross-tier dependence. First, prices move within a daily band of ±7% around the reference price; in sharp corrections heavily sold stocks reach the lower limit, where trading dries up, which truncates return tails and can synchronize limit hits across constituents. Second, settlement moved from T+3 to T+2 on 1 January 2016 (Vietnam Securities Depository 2015), so shares bought cannot be resold for about two business days, which limits intraday arbitrage between constituents and index baskets.
:::

Third, each trading day has a morning session with an opening call auction (09:00–09:15) and continuous matching to 11:30, a midday break from 11:30 to 13:00, and an afternoon session of continuous matching followed by a closing call auction (14:30–14:45). The vendor’s intraday bars follow this calendar: M30 bars open at 09:00, 09:30, 10:00, 10:30, 11:00, 11:30, 13:00, 13:30, 14:00, 14:30; H1 bars at 09:00, 10:00, 11:00, 13:00, 14:00; and the two H4 bars cover the morning and the afternoon session. The first bar of each day therefore contains the overnight return and the opening auction.

Fourth, short selling is restricted. Circular 120/2020/TT-BTC (Ministry of Finance of Vietnam 2020) provides a legal framework for covered short sales of borrowed securities, but to our knowledge the mechanism had not been put into operation during the sample, and naked short selling is not permitted. Decree 155/2020/ND-CP (Government of Vietnam 2020), the main implementing decree of the Law on Securities, was amended by Decree 245/2025/ND-CP of 11 September 2025 (Government of Vietnam 2025). VN30 index futures trade on the Hanoi Stock Exchange; there is no mid-cap future. A mid-cap exchange-traded fund tracking VNMIDCAP (FUEDCMID) has been listed on the HOSE since 29 September 2022 (Ho Chi Minh City Stock Exchange 2022), so the mid-cap tier can be held long but not shorted or hedged with a dedicated derivative.

Fifth, foreign ownership limits cap the share of many listed firms that foreign investors may hold, for example 30% for commercial banks, so foreign flows concentrate in the large caps that have room under their limits. FTSE Russell announced in October 2025 that Vietnam would be reclassified from Frontier to Secondary Emerging status, effective 21 September 2026 (FTSE Russell 2025). The reclassification falls after our sample but may change the weight and relative volatility of the tiers, and therefore the decomposition.

::: {custom-style="heading2"}
3.2 Data and sample construction
:::

::: {custom-style="p1a"}
We use index levels of VN30, VN100 and VNINDEX exported from TradingView (exchange code HOSE). VN30 contains the 30 largest and most liquid stocks screened by free-float capitalization; VN100 adds the next 70 stocks, which form the VNMIDCAP index; and VNINDEX covers all common stocks listed on the HOSE, weighted by full market capitalization. Daily and 30-minute series run to 12 December 2025; the 1-hour and 4-hour series available from the vendor end on 9 December 2024. The vendor does not provide a VNMIDCAP history for the full sample at all frequencies, so the mid-cap segment is recovered from VN30 and VN100 (Section 4.2). The HOSE publishes daily closing levels of all three indices on its website; we did not compare them with the vendor series date by date, and the replication package records a checksum of the input file.
:::

The three series are merged by exact inner joins on timestamps; no index level is filled or interpolated. Log returns are

$$
R_t=\ln P_t-\ln P_{t-1}. \qquad (2)
$$

Two samples are used. The synchronized window (3 January 2017 to 9 December 2024) is the period in which all four frequencies overlap (1D: N = 1,983; M30: N = 19,463; H1: N = 9,879; H4: N = 3,953) and is used for cross-frequency comparisons. The full sample, used for all other analyses, runs from February 2014 to December 2025 at the daily frequency (N = 2,963), from January 2017 to December 2025 at M30 (N = 21,942) and from January 2014 to December 2024 at H1 and H4 (N = 13,523 and 5,410). The series are official index levels computed in real time, not indices back-calculated from current membership lists, so constituent reviews, delistings and free-float adjustments are embedded in the return paths and the sample is free of survivorship bias in index composition.

Volatility regimes use the 20-day rolling standard deviation of returns (Fig. 1). The chronological definition selects crisis episodes with a peak-to-trough VNINDEX drawdown above 25%, at least 45% of trading days in the top quartile of rolling volatility and a documented macro-financial trigger. Three episodes qualify: the 2018 margin contraction (drawdown 26.2%, 47% of days in the top quartile), the 2020 COVID-19 shock (33.5%, 52%) and the 2022 corporate bond liquidity freeze (40.2%, 60%), 539 trading days in all; the calm benchmark comprises 2016–2017 and 2023–2024 (1,000 days). The volatility spikes of 2021 (drawdown 14.3%, 32% of days in the top quartile) and of March–June 2025 (18.1%, 30%) fail the first two conditions and are not shaded. The quartile definitions sort all days by the rolling volatility of VNINDEX (25th and 75th percentiles at 10.6% and 20.0% annualized) or of VN30, and compare the bottom and top quartiles; they include the unshaded episodes.

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
Following Podobnik and Stanley (2008) and Zebende (2011), the DCCA coefficient measures covariance at timescale s after removing local trends. For return series x and y of length N, the profiles are
:::

$$
X_k=\sum_{t=1}^{k}(x_t-\bar{x}),\quad Y_k=\sum_{t=1}^{k}(y_t-\bar{y}),\quad k=1,\dots,N. \qquad (3)
$$

Each profile is divided into N~s~ = ⌊N/s⌋ non-overlapping boxes of length s, starting once from each end of the series, which gives 2N~s~ boxes. In box ν a polynomial of order m (m = 1 unless stated otherwise) is fitted by ordinary least squares (OLS), and the residuals ε~X~ and ε~Y~ define the detrended covariance

$$
f^2_{XY}(s,\nu)=\frac{1}{s}\sum_{k=1}^{s}\varepsilon_{X}(k,\nu)\,\varepsilon_{Y}(k,\nu),\qquad F^2_{XY}(s)=\frac{1}{2N_s}\sum_{\nu=1}^{2N_s}f^2_{XY}(s,\nu). \qquad (4)
$$

With F~X~(s) = [F²~XX~(s)]^1/2^ the detrended fluctuation function of x (Peng et al. 1994), the DCCA coefficient is

$$
\rho_{XY}(s)=\frac{F^2_{XY}(s)}{F_X(s)\,F_Y(s)}. \qquad (5)
$$

Eq. (5) is the inner product of the stacked residual vectors divided by the product of their norms, so the Cauchy–Schwarz inequality gives \|ρ~XY~(s)\| ≤ 1 at every s whenever both fluctuation functions are positive. Two properties are used below: the profile is linear in the series, and OLS detrending is a linear projection, so the residuals of a weighted sum of series are the same weighted sum of their residuals.

::: {custom-style="heading2"}
4.2 The overlap-purged series and the part–whole identity
:::

::: {custom-style="p1a"}
Let A~t~ and B~t~ denote VN30 and VN100 returns and let w be the free-float weight of VN30 in VN100. The overlap-purged mid-cap series is
:::

$$
M_t=P_{\mathrm{cap},t}=\frac{B_t-wA_t}{1-w}, \qquad (6)
$$

with w = 0.6826 from the HOSE factsheet of 31 May 2024 (VN30 and VN100 free-float capitalizations of VND 1,316,288 billion and VND 1,928,303 billion). By construction B~t~ = wA~t~ + (1 − w)M~t~ at every observation. Because the relation is applied to log returns, P~cap~ differs from the arithmetic mid-cap return by a Jensen term of 3.6 × 10⁻⁶ per day. P~cap~ is a shadow benchmark: replicating it would require a long position of about 315% in VN100 and a short position of about 215% in VN30, which the short-sale rules rule out. We call the coefficient ρ~AM~ between VN30 and P~cap~ the overlap-purged coefficient. Calling it economic would require a validation against the published VNMIDCAP series, which our data source does not provide (Section 6.4).

**Lemma 1 (scale-wise part–whole identity).** Let B~t~ = wA~t~ + (1 − w)M~t~ for all t, with 0 < w < 1, and let F~A~(s), F~M~(s) > 0. Define the relative amplitude κ(s) = (1 − w)F~M~(s)/[wF~A~(s)]. Then, for every timescale s and detrending order m,

$$
\rho_{AB}(s)=\frac{1+\kappa(s)\,\rho_{AM}(s)}{\sqrt{1+\kappa(s)^2+2\kappa(s)\,\rho_{AM}(s)}}. \qquad (7)
$$

*Proof.* Profiles and box-wise OLS residuals are linear in the series, so ε~B~ = wε~A~ + (1 − w)ε~M~ in every box. Because Eq. (4) is bilinear, F²~AB~ = wF²~A~ + (1 − w)ρ~AM~ F~A~ F~M~ and F²~B~ = w²F²~A~ + (1 − w)²F²~M~ + 2w(1 − w)ρ~AM~ F~A~ F~M~. Substituting into Eq. (5) and dividing numerator and denominator by wF²~A~ gives Eq. (7). ∎

With one box and no detrending, Eq. (7) is the classical correlation between a total and one of its parts (Pearson 1897; Cureton 1966). The lemma is therefore an adaptation, not a new identity; what it adds is that the identity holds scale by scale for detrended coefficients, for the detrending moving-average coefficient (Kristoufek 2014) and for any dependence measure built from a bilinear covariance of linearly filtered series. Five corollaries follow, all for a fixed scale s, which we suppress.

*Corollary 1 (zero-correlation benchmark and lower bound).* Setting ρ~AM~ = 0 gives the benchmark

$$
\underline{\rho}=\frac{1}{\sqrt{1+\kappa^2}}. \qquad (8)
$$

Eq. (7) is increasing in ρ~AM~ for ρ~AM~ > −κ, so ρ̲ bounds ρ~AB~ from below only when ρ~AM~ ≥ 0. Over all admissible ρ~AM~ and for κ < 1, the minimum of Eq. (7) is

$$
\min_{\rho_{AM}\in[-1,1]}\rho_{AB}=\sqrt{1-\kappa^2},\qquad \text{attained at } \rho_{AM}=-\kappa; \qquad (9)
$$

for κ ≥ 1 no positive lower bound exists. *Corollary 2 (sensitivity).* The derivative of Eq. (7) with respect to the purged coefficient is

$$
\frac{\partial\rho_{AB}}{\partial\rho_{AM}}=\frac{\kappa^2\,(\kappa+\rho_{AM})}{(1+\kappa^2+2\kappa\rho_{AM})^{3/2}}, \qquad (10)
$$

which is small when the child dominates the parent. Its inverse states how far the purged coefficient must move to change the nested one by a given amount. *Corollary 3 (direction).* For ρ~AM~ ≥ 0, ρ²~AB~ − ρ²~AM~ = (1 − ρ²~AM~)(1 + 2κρ~AM~)/(1 + κ² + 2κρ~AM~) ≥ 0, so overlap can only raise the coefficient, with equality only at ρ~AM~ = 1. *Corollary 4 (when the benchmark dominates).* For ρ~AM~ ≥ 0, ρ~AB~ ≤ 1 implies ρ̲/ρ~AB~ ≥ ρ̲, so the benchmark exceeds half of the nested coefficient whenever κ < √3, that is, whenever F~M~/F~A~ < √3·w/(1 − w) = 3.73 at the HOSE weight. A share above one half is thus guaranteed for most nested systems and carries no information.

*Corollary 5 (attribution).* Let overlap and dependence be switched on separately. With neither, the coefficient is 0; with overlap only, it is ρ̲; with dependence only, it is ρ~AM~; with both, it is ρ~AB~. The benchmark-first share ρ̲/ρ~AB~ and the dependence-first share ρ~AM~/ρ~AB~ answer counterfactual questions and depend on the order. The Shapley (1953) value averages the two orders and gives an additive split,

$$
\phi_{\mathrm{overlap}}=\tfrac12\left[\underline{\rho}+(\rho_{AB}-\rho_{AM})\right],\qquad \phi_{\mathrm{dep}}=\tfrac12\left[\rho_{AM}+(\rho_{AB}-\underline{\rho})\right],\qquad \phi_{\mathrm{overlap}}+\phi_{\mathrm{dep}}=\rho_{AB}. \qquad (11)
$$

We report the sensitivity first, because it does not depend on any attribution convention, and the Shapley share φ_overlap/ρ~AB~ as the order-free attribution. Eq. (7) is an identity, not an estimated relation; we verify that it reproduces the directly estimated VN30–VN100 coefficient at every scale and frequency to within 4.4 × 10⁻¹⁶. Each quantity is computed on each scale of the reliable range (Section 4.4) and averaged over that range.

Box 1 shows that the decomposition needs only index-level inputs. Because M is a linear combination of A and B, its volatility and its correlation with A follow from w, the two index volatilities and their correlation, so a user can compute the benchmark, the bound, the purged coefficient and the sensitivity without constituent data. The worked example uses full-sample Pearson moments of daily returns.

::: {custom-style="tablecaption"}
**Box 1** Decomposition of a nested correlation from index-level inputs
:::

| Step | Computation | VN30 in VN100, daily |
|---|---|---|
| 1. Inputs | w; σ~A~, σ~B~; ρ~AB~ | w = 0.6826; σ~A~ = 0.0121, σ~B~ = 0.0119; ρ~AB~ = 0.9885 |
| 2. Remainder volatility | σ~M~ = (σ²~B~ − 2wρ~AB~ σ~A~ σ~B~ + w²σ²~A~)^1/2^/(1 − w) | σ~M~ = 0.0124 |
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
Between semi-annual reviews, constituent capitalizations drift with relative prices. If the true weight w~t~ differs from the fixed weight w, the purged series becomes
:::

$$
\hat{M}_t=\frac{1-w_t}{1-w}M_t+\frac{w_t-w}{1-w}A_t, \qquad (12)
$$

so large-cap returns leak into P~cap~ in proportion to the weight gap, and P~cap~ and VN30 are disjoint only when the weight is exact. We could obtain only one factsheet snapshot of free-float weights, so we cannot reconstruct the weight path. Instead we treat w as uncertain: in each bootstrap replicate we draw w from a uniform distribution on [0.60, 0.75], an interval that contains the factsheet weight with room for drift in either direction, recompute P~cap~ and recompute every quantity. We report these intervals next to the fixed-weight intervals, and Table S2 evaluates each quantity on a grid of weights. The benchmark and the sensitivity depend on the data only through κ, so they are less exposed to weight error than the level of ρ~AM~.

::: {custom-style="heading2"}
4.4 Reliability thresholds and inference
:::

::: {custom-style="p1a"}
The number of boxes falls as s grows, so the DCCA coefficient becomes noisy at large scales. For each sample size we simulate pairs of Gaussian white noise with correlations of −0.3, 0, 0.3, 0.5, 0.7 and 0.9 (167 replications each, 1,002 per frequency) and compute the mean absolute estimation error on 40 log-spaced scales. The reliability threshold s~rel~ is the largest scale below the first scale at which the worst-case error exceeds 0.05; the grid and the tolerance were fixed before the empirical analysis. Because returns are heavy-tailed and volatility-clustered, we repeat the calibration with GARCH(1,1) series driven by Student-t innovations with five degrees of freedom (300 simulations).
:::

DCCA coefficients at different scales are functionals of the same two series, so treating scales as independent observations would overstate precision. All inference therefore resamples the data with the stationary block bootstrap (Politis and Romano 1994), with a mean block length of about 20 trading days (20 days times the number of bars per day at intraday frequencies). Each replicate redraws the joint return series and recomputes every DCCA curve and derived statistic. We use 499 replications for DCCA statistics, 999 for the factor-model, lead–lag and materiality statistics and 1,999 for Pearson regime statistics. Intervals are percentile 95% intervals, capped at ±1 where the statistic is a correlation. Bootstrap p-values invert the percentile interval, p = 2 min{k₋ + 1, k₊ + 1}/(B + 1), where k₋ and k₊ count replicates at or below and at or above zero; with B = 499 the smallest attainable value is 0.004, which we report as p < 0.005.

That resolution limits multiplicity adjustment: with 19 tests, the smallest Holm-adjusted p-value attainable from 499 replications is 0.076. For the slope tests we therefore also report studentized p-values, 2Φ(−\|β̂\|/se~boot~), where se~boot~ is the bootstrap standard error, and adjust them with the Holm (1979) and Benjamini and Hochberg (1995) procedures in two families: the original 19 reliable-range slope tests, and the eight broad-market tests that H2 concerns. The VN30–VN100 prediction is tested by two one-sided tests (TOST; Schuirmann 1987) with an equivalence margin of 0.001 per unit of ln s; over the reliable range, about 4.5 units of ln s at M30, such a slope moves the coefficient by less than one tenth of the 0.05 tolerance.

::: {custom-style="heading2"}
4.5 Scaling regressions and slope channels
:::

::: {custom-style="p1a"}
To measure horizon dependence we regress the DCCA coefficient on the log timescale,
:::

$$
\rho_{XY}(s)=\alpha+\beta\ln s+u(s), \qquad (13)
$$

over the reliable range s ≤ s~rel~ and, in the Supplementary Material, over 30 log-spaced scales between 5 bars and one quarter of the sample. A positive β indicates that co-movement builds up with the horizon. For the nested pair Eq. (7) splits the slope into a channel through the purged coefficient and a channel through κ,

$$
\frac{d\rho_{AB}}{d\ln s}=\frac{\partial\rho_{AB}}{\partial\rho_{AM}}\frac{d\rho_{AM}}{d\ln s}+\frac{\partial\rho_{AB}}{\partial\kappa}\frac{d\kappa}{d\ln s},\qquad \frac{\partial\rho_{AB}}{\partial\kappa}=-\frac{\kappa(1-\rho_{AM}^2)}{(1+\kappa^2+2\kappa\rho_{AM})^{3/2}}, \qquad (14)
$$

so any horizon dependence in the purged coefficient reaches the nested coefficient damped by the sensitivity of Eq. (10). We evaluate Eq. (14) with the reliable-range slopes of ρ~AM~ and κ and compare it with the observed slope.

::: {custom-style="heading2"}
4.6 Volatility conditioning and contagion tests
:::

::: {custom-style="p1a"}
If y~t~ = α + βx~t~ + ε~t~ with Var(ε~t~) = σ²~ε~, the correlation ρ = [1 + σ²~ε~/(β²σ²~x~)]^−1/2^ rises with the variance of x even when β and σ²~ε~ are constant. Forbes and Rigobon (2002) correct the crisis correlation as
:::

$$
\rho^{*}=\frac{\rho_{\mathrm{high}}}{\sqrt{1+\delta\,(1-\rho_{\mathrm{high}}^2)}},\qquad \delta=\frac{\sigma^2_{x,\mathrm{high}}-\sigma^2_{x,\mathrm{low}}}{\sigma^2_{x,\mathrm{low}}}. \qquad (15)
$$

with y = P~cap~ and x = VN30. The correction assumes that β and σ²~ε~ do not change across regimes. If crises raise idiosyncratic variance, ρ* understates the crisis correlation and the test leans toward no contagion (Corsetti et al. 2005). We therefore estimate the single-factor model in each regime and test whether the loading β and the residual variance change, which is the contagion concept in Corsetti et al. (2005) and the structural parameter of Rigobon (2003). We use three regime definitions: chronological episodes, VNINDEX volatility quartiles and VN30 volatility quartiles. The last one sorts on the conditioning variable and avoids sorting on a series that contains P~cap~. Regime statistics are Pearson correlations of daily returns, and the bootstrap is applied within each regime. The nested pairs are not tested, because the parent contains the conditioning index.

::: {custom-style="heading2"}
4.7 Portfolio variance: in-sample misstatement and out-of-sample evaluation
:::

::: {custom-style="p1a"}
For an equally weighted two-asset position with volatilities σ₁ and σ₂, replacing the regime correlation ρ~r~ by a static full-sample correlation ρ~st~ changes the variance by the relative error
:::

$$
\mathrm{RE}=\frac{\rho_{\mathrm{st}}-\rho_{r}}{\tfrac{1}{2}\left(\sigma_1/\sigma_2+\sigma_2/\sigma_1\right)+\rho_{r}}, \qquad (16)
$$

evaluated with regime-specific volatilities so that only the correlation differs. Intervals resample the full sample jointly, so that ρ~st~ is re-estimated in each replicate. As a materiality benchmark we compare \|RE\| with the bootstrap relative standard error of the regime portfolio variance itself. In-sample regimes are ex post, so we also run an out-of-sample comparison. Correlations are estimated from 2014 to 2022 and evaluated on 2023–2025. All forecasts share one-step-ahead RiskMetrics variances with λ = 0.94 (J.P. Morgan/Reuters 1996) and differ only in the correlation: static, EWMA with the same λ, or a regime correlation chosen in real time from the lagged rolling volatility with thresholds fixed in the estimation window. Losses are QLIKE, which is robust to the noise in squared returns as a variance proxy (Patton 2011), and squared error. Differences are tested with the Diebold and Mariano (1995) statistic using a Newey and West (1987) variance with five lags.

::: {custom-style="heading2"}
4.8 Computational details
:::

::: {custom-style="p1a"}
All computations use R 4.3.3 with the packages stats, sandwich 3.1.0 and ggplot2 3.4.4 on an Intel Xeon processor (2.10 GHz, four cores). OLS fits use the QR decomposition, so no iterative optimization, tolerance or convergence criterion is involved. Random seeds are fixed in each script (20260924 to 20261013). A single script, run\_all.R, reproduces every table and figure; rerunning it yields byte-identical CSV output files. The code, outputs and a mapping from every reported number to its output file are provided as Online Resource 1.
:::

::: {custom-style="heading1"}
5 Results
:::

::: {custom-style="heading2"}
5.1 Summary statistics and reliability
:::

::: {custom-style="p1a"}
Table 2 reports descriptive statistics of index and purged returns at the four frequencies.
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
Notes: Kurt. is non-excess kurtosis; P~cap~ is the overlap-purged series of Eq. (6); \*\*\* p < 0.01. Source: Authors’ calculations based on HOSE index data (TradingView).
:::

At the daily frequency the standard deviation is highest for P~cap~ (0.0124) and lowest for VNINDEX (0.0115). All series are negatively skewed and leptokurtic, with kurtosis above 33 at M30, and the Jarque–Bera test rejects normality everywhere. Neither DCCA nor the block bootstrap requires Gaussian returns. Table 3 reports the reliability thresholds.

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
Notes: Largest scale (bars) at which the worst-case mean absolute error stays below 0.05; Gaussian: 1,002 white-noise simulations; heavy-tailed: 300 GARCH(1,1)-t(5) simulations. Source: Authors’ calculations.
:::

The Gaussian thresholds range from 50 days at 1D to 444 bars at M30, and heavy-tailed series reduce them by roughly a factor of three. All averages below use the Gaussian thresholds. Over the shorter heavy-tailed ranges the nested averages become 0.975–0.979 and the purged average 0.882–0.890, so no conclusion depends on the choice.

::: {custom-style="heading2"}
5.2 The overlap gap (H1)
:::

::: {custom-style="p1a"}
Table 4 compares the average DCCA coefficients of the nested pairs with that of the purged pair, and Fig. 2 shows the full curves with bootstrap bands.
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

The nested pairs average 0.975–0.980 at every frequency in both samples, whereas P~cap~–VN30 averages 0.883–0.892. Corollary 3 fixes the sign of the like-for-like gap once ρ~AM~ ≥ 0, but not its size. The gap is 0.099–0.104 with interval lower bounds of at least 0.084, above the 0.05 margin at every frequency, so H1 is supported. The three-pair gap, which also uses the broad-market pairs for which no weight-based purge is available, is 0.086–0.096, and Cohen’s q (Cohen 1988) of 0.78–0.89 indicates a large effect on the Fisher scale; we use it descriptively, since both coefficients come from the same sample. The purged coefficient remains high: overlap inflates co-movement that is already strong rather than creating it.

The gap depends on the weight. Over the grid from 0.60 to 0.75, the like-for-like daily gap ranges from 0.063 to 0.164 and the three-pair gap from 0.052 to 0.153 (Tables S2 and S3), so the point estimate stays above the margin at every weight in the grid, but its size is known only to within about a factor of two. With the weight drawn inside each bootstrap replicate, the like-for-like gap has 95% intervals with lower bounds of 0.057–0.061 (upper bounds 0.155–0.168), and every replicate exceeds 0.05, so H1 also holds under weight uncertainty. A larger weight removes more of the VN30 component and lowers the purged coefficient.

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
Table 5 applies Lemma 1 to the VN30–VN100 pair, and Fig. 3 plots Eq. (7) against the purged coefficient.
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
Notes: Quantities of Eqs. (7)–(11) averaged over s ≤ s~rel~; A = VN30, B = VN100, M = P~cap~. Brackets: block-bootstrap 95% intervals; Panel B is computed for the daily and 30-minute frequencies. Source: Authors’ calculations.
:::

The sensitivity of the nested coefficient to the purged coefficient is 0.106–0.112: to move the index-level number by 0.01, the purged coefficient would have to move by about 0.09. With weight uncertainty the interval widens to 0.07–0.17, so the qualitative conclusion does not depend on the weight. The relative amplitude κ is 0.48–0.50, so the remaining 32% of VN100 contributes about half as much detrended variation as the VN30 component, and the benchmark is 0.893–0.900. At these values Eq. (9) gives a lower bound of 0.864–0.875: no purged coefficient in [−1, 1] could push the VN30–VN100 coefficient below about 0.86.

How much of the observed 0.987–0.988 is due to overlap depends on the question asked. The benchmark-first share is 0.905–0.911 and the dependence-first share is 0.895–0.900; both are large because each factor alone already produces a coefficient near 0.9. The Shapley split, which averages the two orders, attributes 0.505–0.508 of the coefficient to overlap (intervals within 0.497–0.521). Weight uncertainty widens the Shapley intervals to 0.45–0.56 and the benchmark-first intervals to 0.83–0.95, against a sampling-only width of about 0.02. Weight error, not sampling error, is the main source of uncertainty about the attribution.

The decomposition hardly varies with the horizon. Across all reliable scales and frequencies κ lies between 0.47 and 0.52, the benchmark varies by 0.007–0.016 within each frequency, and its slope on ln s is not significant at 5% (bootstrap p = 0.052–0.456; Holm-adjusted 0.208–0.828), although at M30 the percentile interval just excludes zero; a slope of that size (about 0.002 per unit of ln s) is negligible. Applied to full-sample Pearson correlations, the identity gives a benchmark of 0.898–0.903 and a benchmark-first share of 0.911–0.914 across frequencies, within 0.01 of the DCCA values. In these data the multiscale layer therefore adds a check of scale invariance rather than a different answer, and Box 1 is sufficient for practice. The DCCA version remains necessary where the tiers have different scaling, which Eq. (7) would reveal as variation in κ(s).

![](/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/docx_build/../outputs/figures/fig4_overlap_decomposition.png){width=6.3in}

::: {custom-style="figurecaption"}
**Fig. 3** Nested VN30–VN100 coefficient implied by Lemma 1 as a function of the overlap-purged coefficient
:::
::: {custom-style="Compact"}
Notes: Lines: Eq. (7) at the average κ of each frequency (Table 5); markers: observed values; dashed line: daily zero-correlation benchmark; dotted line: daily lower bound of Eq. (9). Source: Authors’ calculations.
:::

Fig. 4 places the HOSE in the space of possible nested systems. The contours show the Pearson benchmark as a function of the child weight and the relative volatility of the remainder, and the triangle marks VN30 in VN100 (w = 0.683, σ~M~/σ~A~ = 1.02, benchmark 0.903). A child weight of 0.5 with equal volatilities would still give a benchmark of about 0.7, so a large mechanical component is the rule rather than a HOSE peculiarity.

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
Table 6 reports reliable-range scaling slopes for the four main pairs at all frequencies, with bootstrap, studentized and adjusted p-values.
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

Positive slopes appear only for the broad-market pairs at intraday frequencies. In the eight-test H2 family, four slopes survive Holm adjustment of the studentized p-values (VN100–VNINDEX at H1; VN30–VNINDEX at H1; VN100–VNINDEX at M30; VN30–VNINDEX at M30), with estimates of 0.0019–0.0024 per unit of ln s, or a rise of about 0.01 across the reliable range. No slope is significant at 1D or H4. Under its decision rule H2 is supported on the full data; the robustness checks below qualify this result.

The conclusion depends on the test family, which is why we report both. Over the original 19 tests, Holm keeps one studentized slope and Benjamini–Hochberg keeps four; with percentile p-values from 499 replications no test survives either adjustment (smallest BH-adjusted p = 0.057). For VN30–VN100, the slope is equivalent to zero at M30 and H1 (TOST p = 0.007, 0.012) and inconclusive elsewhere. The purged P~cap~–VN30 slope is insignificant everywhere.

Eq. (14) explains why the nested slope is flat. The damping factor, the sensitivity of Eq. (10), is 0.106–0.112, and the κ channel partly offsets the ρ~AM~ channel. The linearized slope implied by Eq. (14) differs from the observed VN30–VN100 slope by at most 0.8 × 10⁻⁵ at any frequency (Table S13). A flat nested coefficient is therefore not evidence that the tiers have no horizon structure: a purged slope of 0.01 per unit of ln s, about five times the broad-market slopes above, would move the nested slope by only about 0.001, the TOST margin.

The intraday design needs two checks. The first bar of each day contains the overnight return and the opening auction, the bar in which intraday volatility is highest (Andersen and Bollerslev 1997); it is 10% of M30 bars but carries 37% of the squared VN30 returns, and the last bar contains the closing auction. Table S7 re-estimates the slopes without these bars. At H1, removing the opening bar alone reduces the broad-market slopes to 0.0003 and −0.0005, with intervals that include zero. At M30, the VN30–VNINDEX slope survives removal of the opening bar (0.0020, studentized p = 0.031) while the VN100–VNINDEX slope halves to 0.0010 and loses significance; removing both auction bars leaves slopes of −0.00002 and −0.0002, both insignificant. Trimming does not change the overlap gap (0.107 [0.094, 0.127] at M30 without the first bar). Second, the M30 slope intervals hardly change with the block length (Table S15).

Within the same bootstrap replicates, the broad-market slopes exceed the VN30–VN100 slope at M30 and H1 (differences 0.0018–0.0024, studentized p at most 0.003), but not at 1D or H4, and the differences vanish when the auction bars are removed. H2 is therefore supported on the full data under its decision rule, but the horizon dependence is not a property of continuous trading: it comes from the bars that contain the overnight return and the two call auctions. This is consistent with the Epps (1979) mechanism if the auctions are where the prices of less liquid constituents catch up with large caps, and it means that the H2 result says more about the auction calendar than about gradual information diffusion.

::: {custom-style="heading2"}
5.5 Crisis dependence (H3)
:::

::: {custom-style="p1a"}
Table 7 reports the Forbes–Rigobon adjusted correlations and the single-factor tests under three regime definitions.
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
Notes: Daily returns; ρ* from Eq. (15); p (FR): one-sided bootstrap p-value for H0: ρ* ≤ ρ~low~; β: OLS slope of P~cap~ on VN30; residual variance ratio: crisis over calm. Chronological: 1,000 calm and 539 crisis days; quartiles: 739 days per regime. Source: Authors’ calculations.
:::

The raw correlation rises in every crisis definition, from 0.847 to 0.924 chronologically and from 0.744 to 0.932 under VN30 quartiles. After the Forbes–Rigobon correction the crisis correlation never exceeds its calm level (one-sided p between 0.974 and 0.998), and across the weight grid no one-sided p falls below 0.935 (Table S10). Under VN30 quartiles the adjusted correlation is even significantly lower than in calm periods (−0.087, [−0.144, −0.018]).

The factor model shows why this result should not be read as no contagion. The residual variance of P~cap~ rises by a factor of 2.70 [1.92, 3.68] under VN30 quartiles and 2.57 under VNINDEX quartiles, which violates the constant-variance assumption behind Eq. (15) and pushes ρ* down (Corsetti et al. 2005). The loading of P~cap~ on VN30 rises from 0.737 to 0.948 under VN30 quartiles (Δβ = 0.210, [0.119, 0.306]), but it does not change between the chronological episodes (Δβ = 0.008, [−0.128, 0.140]). Under the stated rule H3 is not supported: the adjusted correlation shows no contagion, while the loading rises on high-volatility days but not across the dated crises. Days of high VN30 volatility thus bring both a stronger response of mid caps to large caps and more mid-cap-specific risk. A rise in the loading is also what nonlinear dependence produces: the lower-tail dependence of P~cap~–VN30 is 0.75 at the 5% quantile against 0.62 under a Gaussian copula with the same correlation (Table S5), so we cannot tell a structural shift from a stable but nonlinear relation. Adding 2021 to the chronological episodes (789 crisis days) leaves both results unchanged (Forbes–Rigobon p = 0.987; Δβ = −0.005, [−0.122, 0.124]).

::: {custom-style="heading2"}
5.6 Portfolio variance (E3, H4)
:::

::: {custom-style="p1a"}
Table 8 reports the in-sample misstatement from using a static correlation and the out-of-sample comparison of correlation forecasts.
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

In sample, a static correlation overstates the variance of an equally weighted VN30 and P~cap~ position by 2.23% in chronological calm periods and by 9.38% in the low-volatility quartile, and understates it by 1.84% and 2.07% in turbulent regimes. The sign pattern is expected for any pooled correlation, which lies between the regime values. For nested pairs the misstatement is at most 2.35% (Table S14). The magnitudes are small against sampling error: \|RE\| is 0.13–1.50 times the standard error of the regime variance for P~cap~–VN30 and at most 0.43 times for the nested pairs. Only the calm-quartile overstatement for P~cap~–VN30 exceeds one standard error.

Out of sample, conditioning does not help. The static correlation has the lowest mean QLIKE for every pair, and the Diebold–Mariano statistics are all negative (p between 0.069 and 0.179), so neither EWMA nor real-time regime correlations improve on it. H4 is not supported. In these data, regime variation in correlations is real in sample but too small or too poorly timed to be exploited with volatility signals.

::: {custom-style="heading2"}
5.7 Further robustness
:::

::: {custom-style="p1a"}
The Supplementary Material reports further checks; none changes the conclusions. The detrending moving-average coefficient (DMCA; Kristoufek 2014) gives a purged coefficient of 0.882–0.891 and a three-pair gap of 0.086–0.096 (Table S4). Because DMCA satisfies the same identity, this is a check on the detrending method, not an independent test. The daily gap interval stays within 0.070–0.119 for mean block lengths from 5 to 60 days (Table S6). The daily VN30–VNINDEX average is 0.9665, 0.9663 and 0.9667 for detrending orders 1, 2 and 3. Statistical proxies that replace the capitalization weight, such as the volatility-scaled proxy with weight 0.9865–0.9885, are numerically unstable and behave as amplified residuals (Table S8). Multifractal DCCA with shuffled surrogates attributes most of the multifractal range to fat tails (Fig. S1). The lead–lag, hedge-effectiveness and episode statistics used in Section 6 are in Tables S9, S11 and S12.
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
| E1 Benchmark and attribution | ρ̲; Shapley share | ρ̲ 0.893–0.900; Shapley 0.505–0.508 | Estimated (not a test) | Attribution depends mainly on the weight |
| E2 Sensitivity | Eq. (10) | 0.106–0.112; with weight uncertainty 0.07–0.17 | Estimated (not a test) | Damping factor of about ten |
| E3 In-sample misstatement | RE, Eq. (16) | P~cap~–VN30 −2.1% to 9.4%; mostly below one SE | Estimated (not a test) | Sign pattern expected from pooling |
| H1 Material overlap gap | Like-for-like gap; lower CI > 0.05 | Gap 0.099–0.104; lower CI ≥ 0.084 | Supported | Holds under weight uncertainty |
| H2 Horizon dependence | Studentized slopes; Holm (H2 family); TOST | 4 of 8 broad-market slopes significant, all intraday; VN30–VN100 equivalent to zero at M30, H1 | Supported | Not robust: vanishes without the auction bars |
| H3 Contagion | FR adjustment and Δβ, VN30 regimes | FR p = 0.998; Δβ = 0.210, p < 0.001 | Not supported | Loading rises on high-volatility days; residual variance rises too |
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
The results on nested pairs have one source. When a parent index contains a child, the child’s variation appears in both terms of every covariance and in both standard deviations, and Lemma 1 shows that this pins the nested coefficient near a benchmark fixed by the weight and the relative amplitude. With VN30 holding 68% of VN100, the benchmark is near 0.90 and the lower bound near 0.87, so the observed 0.99 carries little information about how mid caps move with large caps. The same arithmetic explains why the VN30–VN100 coefficient is flat across horizons and regimes: changes in the purged coefficient reach it damped by a factor of about ten.
:::

Once the overlap is removed, the remaining dependence has the features the size literature predicts. Daily VN30 returns lead P~cap~ returns (cross-autocorrelation 0.084, [0.028, 0.136]), the reverse is negligible (0.007), and the asymmetry of 0.076 [0.048, 0.102] matches the large-to-small lead of Lo and MacKinlay (1990) and Hou (2007). Intraday the lead is symmetric (Table S9), and the intraday horizon dependence of broad-market pairs, which comes from the auction bars, is consistent with the Epps (1979) effect: VNINDEX contains small stocks whose liquidity is fragile (Chen et al. 2021) and whose prices adjust with a delay (Tran and Tran 2025). Index-level data cannot separate this from gradual information diffusion (Hong and Stein 1999).

Several mechanisms can raise the loading of mid caps on large caps on high-volatility days, and our data cannot rank them. Herding during stress (Nguyen et al. 2023) and high sector connectedness (Bui et al. 2022) make stocks move together; limit hits under the ±7% band synchronize the tails; margin calls force simultaneous selling across tiers; and foreign flows, which concentrate in large caps with room under their ownership limits, can transmit large-cap shocks to the rest of the market through domestic portfolio rebalancing. The rise in residual variance shows that crises also bring mid-cap-specific shocks, which the Forbes–Rigobon correction misreads as lower dependence.

::: {custom-style="heading2"}
6.2 Implications
:::

::: {custom-style="p1a"}
If index-level correlations between nested benchmarks are used to judge diversification between size tiers, they should first be decomposed. Box 1 does this from the published series and the index weight, without constituent data. The useful output is the purged coefficient together with the sensitivity, because the inverse sensitivity of about 10 states how ill-conditioned the index-level number is as a measure of tier co-movement: an error of 0.001 in the nested coefficient maps into an error of about 0.01 in the purged one. Holdings-based risk models are not affected.
:::

For hedging, the purged series gives the relevant numbers directly. A minimum-variance hedge of a mid-cap exposure with VN30 removes a share ρ² of its variance (Ederington 1979), 0.79 [0.75, 0.82] over the full sample, but only 0.53 [0.45, 0.61] in the low-volatility quartile and 0.86 in the high-volatility quartile (Table S11). A holder of the VNMIDCAP exchange-traded fund who hedges with VN30 futures therefore keeps about a fifth of the variance on average and about half in calm markets. This basis risk is the quantity a mid-cap derivative would remove; whether such a product would be viable depends on demand and liquidity, which we do not study.

For portfolio risk, our results do not support regime-conditioned correlations between tiers: the in-sample misstatement is mostly within sampling error, and real-time conditioning does not improve forecasts. The relevant error is the one the decomposition removes, which comes from reading a nested correlation as a measure of diversification, not the one from ignoring regimes.

::: {custom-style="heading2"}
6.3 Transferability
:::

::: {custom-style="p1a"}
Lemma 1 holds for any nested pair whose child is contained in the parent with a known weight under one weighting scheme. Fig. 4 shows that the benchmark exceeds 0.7 whenever the child holds half of the parent and the remainder is no more volatile, so large mechanical components should be common in nested families such as SET50 within SET100 or IDX30 within LQ45. Their size must be computed from each family’s weights and volatilities; we did not do this because we could not verify the weights. When indices overlap only partly, Eq. (7) does not apply directly; the shared constituents then form a third component and the benchmark depends on the overlap weight in each index.
:::

We did not extend the decomposition to the broad-market pairs. VNINDEX is weighted by full market capitalization and VN100 and VN30 by free-float capitalization, so VN100 is not a fixed-weight component of VNINDEX and Eq. (6) does not hold exactly. Applying it would leak a mismatch term of the form of Eq. (12) into the purged series, with a size we cannot bound without constituent-level data. The three-pair gap in Table 4 is therefore descriptive for these pairs.

::: {custom-style="heading2"}
6.4 Limitations and future research
:::

::: {custom-style="p1a"}
The evidence comes from one exchange and three indices, so the magnitudes should not be generalized beyond the HOSE. The purged series relies on one factsheet weight; we propagate a plausible range of weights, but a weight path built from semi-annual reviews would narrow the attribution intervals considerably, since weight error dominates sampling error. We could not validate P~cap~ against the published VNMIDCAP index or the FUEDCMID net asset value, because neither was available from our data source at all frequencies; for that reason we call ρ~AM~ overlap-purged rather than economic. Index-level prices cannot separate microstructure frictions from information diffusion, the crisis evidence depends on how regimes are defined, and the out-of-sample period covers three years. The FTSE Russell reclassification from September 2026 offers a natural experiment: if foreign inflows raise the weight of large caps or lower the volatility of the remaining constituents relative to large caps, Eq. (8) predicts a higher benchmark.
:::

::: {custom-style="heading1"}
7 Conclusion
:::

::: {custom-style="p1a"}
Correlations between nested equity indices contain a component fixed by construction. We carry the part–whole identity to scale-wise detrended coefficients, derive a benchmark, a lower bound, a sensitivity and an order-free attribution, and show that all of them can be computed from index-level inputs. On the HOSE, the VN30–VN100 coefficient moves by only about 0.11 per unit change in the overlap-purged coefficient, so the index-level number says little about how mid caps move with large caps; removing the overlap lowers the correlation with large caps by about 0.10. The purged series shows a large-to-small lead, intraday horizon effects that come from the auction bars, a higher loading of mid caps on large caps on high-volatility days alongside more mid-cap-specific risk, and no out-of-sample gain from regime-conditioned correlations. Users who rely on index levels should decompose nested correlations before reading them as evidence about diversification between tiers.
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
**Funding** This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.
:::

::: {custom-style="p1a"}
**Conflict of interest** The authors declare that they have no conflict of interest.
:::

::: {custom-style="p1a"}
**Author contributions** Nguyen Thanh Binh: Conceptualization, Supervision, Validation, Writing – review & editing. Nguyen Van Trung: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Software, Visualization, Writing – original draft, Writing – review & editing. Ha Hong Hanh: Validation, Writing – review & editing. Nguyen Bach Diep: Methodology, Formal analysis, Writing – original draft.
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
FTSE Russell. (2025, October 7). FTSE Russell announces results of September 2025 semi-annual country classification review [Press release]. London Stock Exchange Group.
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
Ho Chi Minh City Stock Exchange. (2022, September 29). Press release on the listing of the DCVFMVNMIDCAP ETF. HOSE.
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
Vietnam Securities Depository. (2015). Decision No. 211/QĐ-VSD of 18 December 2015 on the securities settlement cycle. Hanoi.
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
