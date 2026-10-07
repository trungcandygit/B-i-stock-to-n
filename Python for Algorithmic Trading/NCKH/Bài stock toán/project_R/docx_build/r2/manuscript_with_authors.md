::: {custom-style="Title"}
The Mechanical Floor of Nested Index Correlations: An Exact Multiscale Decomposition with Evidence from Vietnam
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
**Abstract** Large-cap and broad-market indices are often treated as separate diversification instruments even when one index is a subset of the other. We show that this practice confuses index construction with economic co-movement and quantify the confusion exactly. Because a parent index is a capitalization-weighted sum of its child index and the remaining constituents, the detrended cross-correlation analysis (DCCA) coefficient between them decomposes, at every timescale, into a mechanical floor fixed by index weights and relative volatility, and a term that depends on the economic correlation between the child and the remaining constituents. Applying this identity to the Ho Chi Minh City Stock Exchange (VN30 within VN100 within VNINDEX; 30-minute to daily data, 2014–2025), we find that the floor alone accounts for 0.905–0.911 of the observed VN30–VN100 coefficient (block-bootstrap 95% intervals within 0.895–0.920), and that a change of 0.10 in the economic correlation moves the nested coefficient by only about 0.011. Purging the overlap lowers the correlation with large caps by 0.086–0.096 (intervals exclude zero at all four frequencies). Broad-market pairs show small positive horizon slopes at intraday frequencies that do not survive multiple-testing adjustment, and the purged correlation shows none. Forbes–Rigobon volatility conditioning gives no evidence of crisis contagion between tiers, and a static correlation misstates mid-cap portfolio variance by between −2.1% and +9.4% across volatility regimes. The results apply to one market and three indices; the identity itself holds for any nested pair.
:::

::: {custom-style="keywords"}
**Keywords** constituent overlap; detrended cross-correlation; Forbes–Rigobon adjustment; multiscale correlation; portfolio risk; Vietnam
:::

::: {custom-style="keywords"}
**JEL Classification** C14; C58; G11; G15
:::

::: {custom-style="heading1"}
1 Introduction
:::

::: {custom-style="p1a"}
Multi-capitalization portfolios are often built as if large-cap and broad-market indices were separate sources of diversification. Risk models, allocation rules and stress tests typically summarize the dependence between such indices with a single Pearson correlation of daily returns (Markowitz 1952). In nested index systems this number has a problem that is independent of estimation error: the parent index contains the child index, so part of their correlation is fixed by index construction. On the Ho Chi Minh City Stock Exchange (HOSE), the large-cap VN30 index is contained in the VN100 index, which is contained in the market-wide VNINDEX:
:::

$$
\mathrm{VN30} \subset \mathrm{VN100} \subset \mathrm{VNINDEX}. \qquad (1)
$$

Because the 30 largest firms account for about two-thirds of the free-float capitalization of VN100, the correlation between VN30 and VN100 returns is close to one (0.988 at the daily frequency). How much of this number reflects economic linkage between large caps and the rest of the market, and how much reflects the fact that VN30 stocks are counted on both sides? Existing studies of multiscale co-movement, which rely mostly on detrended cross-correlation analysis (DCCA) and wavelet methods, analyze pairs of assets that share no constituents (Section 2), so they do not answer this question.

This paper answers it with an exact result. Writing the parent index return as a capitalization-weighted sum of the child index return and the return on the remaining constituents, we prove (Proposition 1) that the DCCA coefficient of a nested pair is, at every timescale, a known function of two quantities: the DCCA coefficient between the child index and the remaining constituents, which we call the economic correlation, and a relative-amplitude ratio fixed by index weights and volatilities. The function has a strictly positive floor: even if the remaining constituents were uncorrelated with the child index, the nested coefficient would equal that floor. The identity holds for Pearson correlation as a special case and requires no distributional assumption.

We apply the identity, together with a capitalization-weighted mid-cap proxy that removes the overlap, to VN30, VN100 and VNINDEX at 30-minute, 1-hour, 4-hour and daily frequencies from 2014 to 2025. We test five hypotheses, stated in Section 2.5, on overlap inflation, the dominance of the mechanical floor, horizon dependence, crisis contagion and portfolio-variance misstatement. All inference uses stationary block bootstrap intervals, and the horizon-dependence tests are adjusted for multiple comparisons.

The paper makes three contributions. First, it derives an exact, scale-by-scale decomposition of nested index correlations into a mechanical floor and an economic component, with closed forms for the floor and for the sensitivity of the nested coefficient to the economic correlation. In our data the floor accounts for 0.905–0.911 of the VN30–VN100 coefficient, and the nested coefficient responds to the economic correlation with a slope of 0.106–0.112, so index-level correlations carry little information about economic co-movement. Second, it measures the overlap effect with inference: purging the overlap lowers the correlation with large caps by 0.086–0.096 with bootstrap intervals that exclude zero at every frequency, while the purged correlation remains high (about 0.89). Third, it separates volatility from structural change in crises and prices the cost of static correlations: Forbes–Rigobon conditioning gives no evidence of cross-tier contagion, and a static correlation misstates the variance of a mid-cap factor exposure by amounts that switch sign between calm and turbulent regimes.

The remainder of the paper is organized as follows. Section 2 reviews the literature and develops the hypotheses. Section 3 describes the institutional setting and the data. Section 4 presents the methodology, including Proposition 1. Section 5 reports the results, Section 6 discusses mechanisms, implications and limitations, and Section 7 concludes.

::: {custom-style="heading1"}
2 Literature review and hypothesis development
:::

::: {custom-style="p1a"}
Three literatures bear on our question: multiscale dependence measured by detrended cross-correlation, the effect of index construction and membership on co-movement, and the separation of contagion from volatility-driven interdependence. We review each analytically, identifying where findings agree, where they conflict and what they leave unresolved, and then state the gap and the hypotheses.
:::

::: {custom-style="heading2"}
2.1 Multiscale dependence and detrended cross-correlation
:::

::: {custom-style="p1a"}
Detrended cross-correlation analysis (DCCA) extends detrended fluctuation analysis (Peng et al. 1994; Kantelhardt et al. 2002) to pairs of nonstationary series (Podobnik and Stanley 2008). Zebende (2011) normalized the detrended covariance into a bounded coefficient, Podobnik et al. (2011) proposed tests for power-law cross-correlations, and Zhou (2008) generalized the method to multifractal moments (MF-DCCA). Later variants replace polynomial detrending by moving averages (Jiang and Zhou 2011; Kristoufek 2014), compute the coefficient in sliding windows (Guedes et al. 2021) or partial out third variables (Ge and Lin 2021). The methods disagree on one technical point that matters for finance: MF-DCCA must handle negative local covariances, and Oświęcimka et al. (2014) show that taking their absolute values, as many implementations do, can create spurious multifractality; they propose a sign-preserving alternative.
:::

Applied work agrees that financial dependence is scale-dependent. Stock–bond correlations differ across horizons (Al Rababa’a et al. 2021), cross-market correlations between China and the United States vary with scale and fluctuation size (Ge and Lin 2021; Chen et al. 2024), and combining MF-DCCA with transfer entropy reveals both multifractal cross-correlations and the direction of information flow among individual US stocks (Zhou et al. 2025). Two strands then use these coefficients for decisions. One measures crisis transmission: Okorie and Lin (2021) find fractal contagion in the stock markets of 32 economies during COVID-19 that fades over the medium and long run, and Tilfani et al. (2021) track contagion with the DCCA coefficient in sliding windows. The other builds portfolios: a multifractal mean-MF-X-DMA rule outperforms the mean-variance model (Wang et al. 2021), and mean-DCCA portfolios perform better when the investor’s preferred scale adapts to market conditions (Kakinaka et al. 2025).

These strands share an assumption that is rarely stated. They treat the DCCA coefficient between two series as a measure of economic dependence, which is reasonable for disjoint assets such as stocks and bonds or two national markets. When one series contains the other, the coefficient also contains an arithmetic component that a portfolio optimizer or a contagion test would misread. None of the studies above analyzes nested pairs or separates such a component.

::: {custom-style="heading2"}
2.2 Index construction, constituent overlap and co-movement
:::

::: {custom-style="p1a"}
A separate literature shows that index membership itself changes co-movement. Barberis et al. (2005) find that stocks added to the S&P 500 co-move more with the index afterwards, a result they attribute to trading frictions and investor habitats rather than to fundamentals. Recent work confirms the effect with sharper designs: DeCoste (2025) uses a regression discontinuity around the membership threshold and finds higher co-movement with no change in fundamentals, and Liao et al. (2022) attribute part of it to common demand from index trackers and beta arbitrageurs. The evidence is not uniform, however: Greenwood and Sammon (2025) document that the price effect of S&P 500 additions has almost disappeared, which suggests that membership effects depend on market structure and may weaken as indexing grows.
:::

This literature concerns behavioral co-movement among stocks. Our concern is the arithmetic overlap between indices: when VN30 is part of VN100, their correlation is high even if no investor behaves differently because of index membership. Multiscale studies that address redundant exposures do so with statistical tools, such as wavelet partial correlations for clusters of stocks (Michis 2022), or study volume–return rather than index–index dependence (Rodriguez and Alvarez-Ramirez 2021), so the arithmetic overlap has not been isolated.

Vietnamese evidence suggests that both mechanisms could matter on the HOSE. Liquidity fell after the introduction of a market surveillance system, especially for small firms (Chen et al. 2021), herding appears on the HOSE during stress (Nguyen et al. 2023), sector connectedness exceeds 60% and rose to about 90% during COVID-19 (Bui et al. 2022), price adjustment is delayed under retail-heavy trading (Tran and Tran 2025), and dependence on regional markets is nonlinear (Le et al. 2025). High connectedness and herding raise all correlations, which makes it harder, not easier, to read index-level correlations as evidence about the tiers.

::: {custom-style="heading2"}
2.3 Volatility, contagion and interdependence
:::

::: {custom-style="p1a"}
Equity correlations rise in downturns (Longin and Solnik 2001; Ang and Chen 2002), but Forbes and Rigobon (2002) show that unadjusted correlations rise mechanically with the variance of the conditioning market, so a crisis increase may reflect interdependence rather than contagion. The COVID-19 literature illustrates the resulting disagreement. Studies that do not apply the Forbes–Rigobon correction report contagion: conditional correlations between Chinese and G7 firms rose, especially for financial firms (Akhtaruzzaman et al. 2021), contagion channels multiplied in a network of 19 markets (Guo et al. 2021) and copula dependence intensified across Asian and American indices (Benkraiem et al. 2022). A DCCA-based test on commodities that compares coefficients before and during the crisis finds no contagion between two crude-oil benchmarks that were already highly interdependent, but contagion between crude oil and precious metals (Santana et al. 2023). Whether a crisis increase is structural thus depends on the pair and on how volatility is treated, and no study applies the correction to tiers of the same market whose indices overlap.
:::

Horizon effects add a further layer. Non-synchronous trading depresses correlations at short horizons (Epps 1979), and the size of this Epps effect depends on how prices are sampled (Chang et al. 2021). Gradual information diffusion (Hong and Stein 1999) can make co-movement build up with the horizon among stocks that adjust at different speeds. In ASEAN markets integration varies over time with trade links and volatility (Abdul Karim and Xin Ning 2013; Lean and Teng 2013), so horizon and regime effects can interact.

::: {custom-style="heading2"}
2.4 Research gap
:::

::: {custom-style="p1a"}
Table 1 compares representative studies on the dimensions relevant to our question.
:::

::: {custom-style="tablecaption"}
**Table 1** Prior studies of multiscale and crisis co-movement and the gap addressed here
:::

| Study | Market and data | Method | Overlap treated? | Volatility conditioning? | Main finding |
|---|---|---|---|---|---|
| Podobnik and Stanley (2008); Zebende (2011) | Methodological | DCCA; ρDCCA | No | No | Defines scale-wise detrended covariance and its normalized coefficient |
| Al Rababa’a et al. (2021) | Stock and bond markets | Multiscale correlation | No (disjoint assets) | No | Stock–bond correlation differs across horizons |
| Okorie and Lin (2021) | 32 stock markets, COVID-19 | DCCA, DMCA | No | No | Fractal contagion that fades over the medium and long run |
| Tilfani et al. (2021) | Stock market indices | Sliding-window ρDCCA | No | No | Time-varying cross-correlation and contagion |
| Ge and Lin (2021); Chen et al. (2024) | China and United States | MF-DCCA; partial MF-DCCA | No | No | Scale- and size-dependent cross-correlation |
| Wang et al. (2021); Kakinaka et al. (2025) | Stock portfolios | Mean-MF-X-DMA / mean-DCCA portfolios | No | No | Scale-aware rules improve portfolio performance |
| Santana et al. (2023) | Crude oil and precious metals, COVID-19 | ΔρDCCA test | No | No | No contagion between WTI and Brent; contagion between oil and precious metals |
| Forbes and Rigobon (2002) | International stock markets | Heteroskedasticity-adjusted correlation | No | Yes | Crisis increases reflect interdependence |
| Akhtaruzzaman et al. (2021) | China and G7 firms, COVID-19 | Dynamic conditional correlation | No | No Forbes–Rigobon correction | Contagion concentrated in financial firms |
| Barberis et al. (2005); DeCoste (2025) | S&P 500 additions and membership | Event study; regression discontinuity | Membership, not overlap | No | Index membership raises co-movement |
| Bui et al. (2022) | 24 Vietnamese sectors, 2012–2021 | Spillover connectedness | No | No | Connectedness 60–90%, highest in COVID-19 |
| This study | VN30, VN100, VNINDEX; M30 to daily, 2014–2025 | DCCA, MF-DCCA, exact decomposition | Yes (exact, scale-wise) | Yes | Mechanical floor dominates nested correlations |

::: {custom-style="Compact"}
Notes: Overlap treated: whether the study separates the dependence created by shared constituents; volatility conditioning: whether crisis comparisons correct for heteroskedasticity bias. Source: Authors’ compilation.
:::

Three gaps follow. First, no study we found separates the mechanical component of correlations between overlapping indices from economic co-movement, and none derives that component exactly. Second, multiscale studies of crisis transmission rarely apply volatility conditioning, while volatility-conditioned studies use a single horizon. Third, to our knowledge no DCCA study covers the Vietnamese index system at intraday and daily frequencies. Our search covered the outlets listed in Table 1 and indexed finance and econophysics journals for 2021–2026; the closest prior work is Barberis et al. (2005) and DeCoste (2025) on membership-induced co-movement and Santana et al. (2023) on DCCA-based contagion tests.

::: {custom-style="heading2"}
2.5 Hypothesis development
:::

::: {custom-style="p1a"}
The literature reviewed above and Proposition 1 (Section 4.2) yield five testable hypotheses. For each we state the prediction, the test and the decision rule; all tests use a 5% level.
:::

Constituent overlap adds the variance of shared stocks to both sides of a nested pair. If index-level correlations contain a mechanical component, they should exceed the correlation between the child index and the non-overlapping remainder.

*H1 (overlap inflation).* At every trading frequency, the average reliable-range DCCA coefficient of the nested pairs exceeds that of the purged pair (mid-cap proxy and VN30). Test: the block-bootstrap 95% interval for the difference excludes zero; effect size: Cohen’s q on Fisher-transformed coefficients.

Proposition 1 implies that the nested coefficient cannot fall below a floor determined by index weights and relative volatility. When the child index carries most of the parent’s capitalization, the floor should account for most of the observed coefficient.

*H2 (mechanical dominance).* The mechanical floor accounts for more than half of the VN30–VN100 DCCA coefficient. Test: one-sided bootstrap test of a share above 0.5, with the lower bound of the 95% interval above 0.5 at every frequency.

Non-synchronous trading depresses correlations at short horizons (Epps 1979), and gradual information diffusion (Hong and Stein 1999) lets co-movement build up with the horizon. Both mechanisms predict positive scaling slopes for pairs whose constituents are repriced at different speeds, such as broad-market pairs that include small, illiquid stocks, and no slope for VN30–VN100, whose co-movement is fixed by overlap.

*H3 (horizon dependence).* The DCCA coefficient rises with the timescale for pairs involving the broad market, but not for the VN30–VN100 pair. Test: block-bootstrap intervals for log-linear scaling slopes, with Holm and Benjamini–Hochberg adjustment across all slope tests.

Forbes and Rigobon (2002) show that unadjusted correlations rise mechanically with the variance of the conditioning market. Contagion requires that the adjusted crisis correlation exceed its calm level.

*H4 (contagion).* After Forbes–Rigobon conditioning, the crisis correlation between the purged mid-cap component and VN30 exceeds the calm-period correlation. Test: one-sided bootstrap test, reported with its power against an increase of 0.05.

If correlations vary with the volatility regime, a static correlation will misstate portfolio variance, and the error should be larger for the purged mid-cap exposure, whose correlation varies more, than for nested cash portfolios.

*H5 (risk misstatement).* A static correlation misstates the variance of an equally weighted large-cap and mid-cap portfolio in calm and turbulent regimes. Test: block-bootstrap intervals for the relative variance error exclude zero.

::: {custom-style="heading1"}
3 Institutional background and data
:::

::: {custom-style="heading2"}
3.1 Institutional background
:::

::: {custom-style="p1a"}
The HOSE is regulated by the State Securities Commission of Vietnam (SSC). Four features of its microstructure matter for cross-index dependence. First, prices move within a symmetric daily band of ±7% around the reference price; during sharp corrections heavily sold stocks reach the lower limit, where trading dries up, which truncates return tails and can synchronize limit hits across constituents. Second, under the T+2 settlement cycle in force for most of the sample, shares bought could not be sold before the afternoon of the second business day, which restricts intraday arbitrage between constituents and index baskets.
:::

Third, each session opens with a 15-minute call auction (09:00–09:15) and closes with another (14:30–14:45), with continuous matching in between, so the first and last 30-minute bars of each day are more volatile and less synchronous than midday bars. Fourth, Decree 155/2020/ND-CP and Circular 120/2020/TT-BTC prohibit cash short selling; margin rules require an initial margin of at least 50%, and Circular 68/2024/TT-BTC, which removed the pre-funding requirement for foreign institutional investors, left the short-sale prohibition unchanged. VN30 index futures trade on the Hanoi Stock Exchange, but no mid-cap index future exists. Arbitrageurs therefore cannot trade the spread between large caps and mid-caps, which can prolong non-synchronous price adjustment between them.

::: {custom-style="heading2"}
3.2 Data and sample construction
:::

::: {custom-style="p1a"}
We use closing prices of three HOSE indices exported from TradingView (exchange code HOSE; symbols VN30, VN100 and VNINDEX): VN30, which contains the 30 largest and most liquid stocks screened by free-float capitalization; VN100, which adds the next 70 stocks (the constituents of the VNMIDCAP, or VN70, index); and VNINDEX, which covers all common stocks listed on the HOSE, weighted by full market capitalization. Daily and 30-minute series run to 12 December 2025; the 1-hour and 4-hour series available from the vendor end on 9 December 2024. A VNMIDCAP price history is not available from this source for the full sample and all frequencies, so the mid-cap segment is recovered by the decomposition in Section 4.2.
:::

The three series are merged by exact inner joins on timestamps; no index level is filled or interpolated. Log returns are computed as

$$
R_t=\ln P_t-\ln P_{t-1}. \qquad (2)
$$

Two samples are used. The synchronized window (3 January 2017 to 9 December 2024) is the period in which all four frequencies overlap (1D: N = 1,983; M30: N = 19,463; H1: N = 9,879; H4: N = 3,953) and is used for cross-frequency comparisons. The full sample, used for all other analyses, runs from February 2014 to December 2025 at the daily frequency (N = 2,963), from January 2017 to December 2025 at M30 (N = 21,942) and from January 2014 to December 2024 at H1 and H4 (N = 13,523 and 5,410).

The series are official index levels computed in real time by the exchange, not indices back-calculated from current membership lists. Semi-annual constituent reviews, delistings, corporate actions and free-float adjustments are therefore embedded in the return paths, so the sample is free of survivorship and look-ahead bias in index composition.

Regime dependence is evaluated under two definitions based on the 20-day rolling standard deviation of VNINDEX returns (Fig. 1). The first uses chronological crisis episodes that satisfy three conditions: a peak-to-trough VNINDEX drawdown above 25%, at least 45% of trading days in the top quartile of rolling volatility, and a documented macro-financial trigger. Three episodes qualify: the 2018 margin contraction (drawdown 26.2%, 47% of days in the top quartile), the 2020 COVID-19 shock (33.5%, 52%) and the 2022 corporate bond liquidity freeze (40.2%, 60%), totaling 539 trading days; the calm benchmark comprises 2016–2017 and 2023–2024 (1,000 days). The April 2025 tariff shock (drawdown 18.1%) fails the first two conditions. The second definition sorts all days by rolling volatility and compares days below the 25th percentile (10.6% annualized) with days above the 75th percentile (20.0%).

![](/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/docx_build/../outputs/figures/fig1_volatility_regimes.png){width=6.3in}

::: {custom-style="figurecaption"}
**Fig. 1** Twenty-day rolling volatility of VNINDEX (annualized) and market regimes, 2014–2025
:::
::: {custom-style="Compact"}
Notes: Shaded areas mark the three crisis episodes; dashed and dotted lines mark the 25th and 75th percentiles. Source: Authors’ calculations based on HOSE index data (TradingView).
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

Because Eq. (5) is the inner product of the stacked residual vectors divided by the product of their norms, the Cauchy–Schwarz inequality gives \|ρ~XY~(s)\| ≤ 1 for every s, provided both fluctuation functions are positive. Two properties of Eq. (4) are used below: the profile is a linear function of the series, and OLS detrending is a linear projection, so the residuals of a weighted sum of series are the same weighted sum of their residuals.

::: {custom-style="heading2"}
4.2 Mid-cap decomposition and the exact overlap identity
:::

::: {custom-style="p1a"}
Let A~t~ = R~30,t~ and B~t~ = R~100,t~ denote VN30 and VN100 returns, and let w be the free-float weight of VN30 in VN100. We define the capitalization-weighted mid-cap proxy
:::

$$
M_t=P_{\mathrm{cap},t}=\frac{B_t-wA_t}{1-w}, \qquad (6)
$$

with w = 0.6826, computed from the HOSE factsheet of 31 May 2024 (VN30 and VN100 free-float capitalizations of VND 1,316,288 billion and VND 1,928,303 billion). The weight is fixed from the factsheet before any estimation, so it is not tuned to the results. Rearranging Eq. (6), B~t~ = wA~t~ + (1 − w)M~t~ holds exactly at every observation. Because the decomposition is applied to log rather than arithmetic returns, the proxy differs from the true mid-cap return by a Jensen term of 3.6 × 10⁻⁶ per day at the daily frequency, which is negligible for the DCCA estimates. The proxy requires a long position of about 315% in VN100 and a short position of about 215% in VN30, so under the short-sale prohibition it is an analytical shadow benchmark, not a tradable portfolio.

**Proposition 1 (exact overlap decomposition).** Let B~t~ = wA~t~ + (1 − w)M~t~ for all t, with 0 < w < 1, and let F~A~(s), F~M~(s) > 0. Define the relative amplitude κ(s) = (1 − w)F~M~(s)/[wF~A~(s)] and the economic correlation ρ~AM~(s). Then, for every timescale s and detrending order m,

$$
\rho_{AB}(s)=\frac{1+\kappa(s)\,\rho_{AM}(s)}{\sqrt{1+\kappa(s)^2+2\kappa(s)\,\rho_{AM}(s)}}. \qquad (7)
$$

*Proof.* Profiles and box-wise OLS residuals are linear in the series, so ε~B~ = wε~A~ + (1 − w)ε~M~ in every box. Because Eq. (4) is bilinear, F²~AB~ = wF²~A~ + (1 − w)ρ~AM~ F~A~ F~M~ and F²~B~ = w²F²~A~ + (1 − w)²F²~M~ + 2w(1 − w)ρ~AM~ F~A~ F~M~. Substituting into Eq. (5) and dividing numerator and denominator by wF~A~² gives Eq. (7). ∎

Three corollaries follow. First, setting ρ~AM~(s) = 0 gives the mechanical floor

$$
\underline{\rho}(s)=\frac{1}{\sqrt{1+\kappa(s)^2}}>0, \qquad (8)
$$

the value the nested coefficient would take if the remaining constituents were uncorrelated with the child index. We call ρ̲(s)/ρ~AB~(s) the mechanical share. Second, the sensitivity of the nested coefficient to the economic correlation is

$$
\frac{\partial\rho_{AB}(s)}{\partial\rho_{AM}(s)}=\frac{\kappa(s)^2\,[\kappa(s)+\rho_{AM}(s)]}{[1+\kappa(s)^2+2\kappa(s)\,\rho_{AM}(s)]^{3/2}}, \qquad (9)
$$

which is small when κ is small, that is, when the child index dominates the parent. Third, for ρ~AM~ ≥ 0, ρ²~AB~ − ρ²~AM~ = (1 − ρ²~AM~)(1 + 2κρ~AM~)/(1 + κ² + 2κρ~AM~) ≥ 0, so overlap can only inflate the coefficient, with equality only when ρ~AM~ = 1. The identity uses only linearity and bilinearity: it holds for the Pearson correlation (no detrending, one box), for the detrending moving-average coefficient used in Section 5.9 and for any other dependence measure built from a bilinear covariance of linearly filtered series.

Equation (7) is not an approximation; we verify numerically that it reproduces the directly estimated VN30–VN100 coefficient at every scale and frequency to within 4.4 × 10⁻¹⁶. We estimate κ, the floor, the mechanical share and the sensitivity on each scale of the reliable range (Section 4.4), average them over that range and obtain 95% intervals from the block bootstrap described below. Because P~cap~ is constructed from A and B, Eq. (7) is an accounting identity rather than an estimated relation; its content lies in the decomposition it delivers. The floor and the sensitivity depend only on w and the relative amplitude κ, so they can be computed for any nested pair whose child weight and fluctuation functions are known.

For comparison we construct three statistical proxies: the volatility-scaled proxy P~heur,~ which replaces w by the correlation between VN30 and VN100 returns (0.9865–0.9885); the ratio-spread proxy P~ratio~ = B~t~ − A~t~; and the residual P~res~ of an OLS regression of B~t~ on A~t~ (R² of 0.973–0.977, slope 0.968–0.975). For P~heur~ the denominator 1 − w~heur~ is only 0.0115–0.0135, which multiplies the numerator by 74–87; this is a numerically unstable construction, and its daily standard deviation (0.1576) is more than ten times that of P~cap~ (0.0124).

::: {custom-style="heading2"}
4.3 Weight drift
:::

::: {custom-style="p1a"}
Between semi-annual reviews, constituent capitalizations drift with relative prices. If the true weight w~t~ differs from the fixed weight w, the proxy becomes
:::

$$
\hat{M}_t=\frac{1-w_t}{1-w}M_t+\frac{w_t-w}{1-w}A_t, \qquad (10)
$$

so a fraction of large-cap returns leaks into the proxy in proportion to the weight gap. Only one factsheet snapshot of free-float weights is available, so we do not reconstruct the weight path; Table A2 re-estimates the main statistics for weights from 0.60 to 0.75.

::: {custom-style="heading2"}
4.4 Reliability thresholds and inference
:::

::: {custom-style="p1a"}
The number of boxes falls as s grows, so the DCCA coefficient becomes noisy at large scales. For each sample size we simulate pairs of Gaussian white noise with correlations of −0.3, 0, 0.3, 0.5, 0.7 and 0.9 (167 replications each, 1,002 per frequency) and compute the mean absolute estimation error on 40 log-spaced scales. The reliability threshold s~rel~ is the largest scale below the first scale at which the worst-case error exceeds 0.05; both the error grid and the 0.05 tolerance are fixed before the empirical analysis. Because returns are heavy-tailed and volatility-clustered, we repeat the calibration with generalized autoregressive conditional heteroskedasticity GARCH(1,1) series driven by Student-t innovations with five degrees of freedom (300 simulations).
:::

DCCA coefficients at different scales are functionals of the same two series, so treating scales or simulation replicates as independent observations would overstate precision. All inference therefore resamples the data. A stationary block bootstrap (Politis and Romano 1994) with a mean block length of about 20 trading days (499 replications for DCCA-based statistics and 1,999 for the Pearson-based regime statistics of Sections 4.6 and 4.7) redraws the joint return series, recomputes every DCCA curve and every derived statistic, and yields percentile 95% intervals and two-sided bootstrap p-values computed as 2 min{(k₋ + 1), (k₊ + 1)}/(B + 1), where k₋ and k₊ count replicates at or below and at or above zero. Table A5 shows that the interval for the main gap is stable for mean block lengths from 5 to 60 days. The slope tests in Section 5.5 involve 19 pair-frequency combinations per scale range; we report Holm (1979) family-wise and Benjamini and Hochberg (1995) false-discovery-rate adjusted p-values within each range.

::: {custom-style="heading2"}
4.5 Scaling regressions
:::

::: {custom-style="p1a"}
To test horizon dependence we regress the DCCA coefficient on the log timescale,
:::

$$
\rho_{XY}(s)=\alpha+\beta\ln s+u(s), \qquad (11)
$$

on 30 log-spaced scales between 5 bars and one quarter of the sample (5 to 5,485 bars at M30) and, separately, on the reliable range s ≤ s~rel~. A positive β indicates that co-movement builds up with the horizon, as predicted by the Epps (1979) effect at short scales and by gradual information diffusion (Hong and Stein 1999) beyond them.

::: {custom-style="heading2"}
4.6 Forbes–Rigobon volatility conditioning
:::

::: {custom-style="p1a"}
If y~t~ = α + βx~t~ + ε~t~ with Var(ε~t~) = σ²~ε,~ the correlation ρ = [1 + σ²~ε~/(β²σ²~x~)]^−1/2^ rises with the variance of x even when β and σ²~ε~ are constant. Forbes and Rigobon (2002) correct the high-volatility correlation as
:::

$$
\rho^{*}=\frac{\rho_{\mathrm{high}}}{\sqrt{1+\delta\,(1-\rho_{\mathrm{high}}^2)}},\qquad \delta=\frac{\sigma^2_{x,\mathrm{high}}-\sigma^2_{x,\mathrm{low}}}{\sigma^2_{x,\mathrm{low}}}. \qquad (12)
$$

The correction requires the conditioning series to be exogenous. This is plausible for the disjoint pair P~cap~–VN30, with VN30 as the conditioning market, but fails by construction for the nested pairs, whose parent contains the conditioning index; the formal test is therefore restricted to P~cap~–VN30. Regime correlations are Pearson correlations of daily returns, and δ is the relative increase in the variance of VN30 returns, so the correction and the correlation refer to the same measure. The bootstrap is applied within each regime; we report a 95% interval for ρ* − ρ~low,~ a one-sided p-value for the null of no increase and the power to detect an increase of 0.05. Severe downturns on the HOSE can trigger margin calls and simultaneous selling of large and mid caps, which weakens exogeneity, so ρ* is interpreted as cross-tier dependence under stress rather than one-way transmission.

::: {custom-style="heading2"}
4.7 Portfolio variance error
:::

::: {custom-style="p1a"}
For an equally weighted two-asset portfolio with volatilities σ₁ and σ₂, replacing the regime correlation ρ~r~ by a static full-sample correlation ρ~st~ changes the portfolio variance by the relative error
:::

$$
\mathrm{RE}=\frac{\rho_{\mathrm{st}}-\rho_{r}}{\tfrac{1}{2}\left(\sigma_1/\sigma_2+\sigma_2/\sigma_1\right)+\rho_{r}}, \qquad (13)
$$

evaluated with regime-specific volatilities so that the static and regime cases differ only in the correlation. This is a closed-form identity; no optimization is involved. Intervals come from the within-regime block bootstrap.

::: {custom-style="heading2"}
4.8 Multifractal extension
:::

::: {custom-style="p1a"}
To examine whether scaling differs between small and large fluctuations, we use multifractal DCCA (MF-DCCA; Zhou 2008) with absolute local covariances, which avoids complex-valued moments:
:::

$$
F_q(s)=\left\{\frac{1}{2N_s}\sum_{\nu=1}^{2N_s}\left|f^2_{XY}(s,\nu)\right|^{q/2}\right\}^{1/q},\qquad q\in[-5,5]\setminus\{0\}. \qquad (14)
$$

The generalized exponent h~xy~(q) is the slope of ln F~q~(s) on ln s over 24 log-spaced scales, and the range Δh = h~xy~(−5) − h~xy~(5) measures the strength of multifractality. Because fat tails alone widen Δh, each observed range is compared with 100 surrogates in which the paired returns are jointly shuffled, which preserves the return distributions and their contemporaneous correlation but destroys temporal structure. Oświęcimka et al. (2014) show that taking absolute values of local covariances can create spurious multifractality and propose a sign-preserving alternative; we therefore treat the multifractal results as descriptive and base no hypothesis test on them.

::: {custom-style="heading2"}
4.9 Computational details
:::

::: {custom-style="p1a"}
All computations use R 4.3.3 with the packages stats (base), sandwich 3.1.0 and ggplot2 3.4.4 on an Intel Xeon processor (2.10 GHz, four cores). OLS fits use the QR decomposition, so no iterative optimization, tolerance or convergence criterion is involved. Random seeds are fixed (20260924 for the round-one inference, 20261007 for the decomposition and robustness analyses; the white-noise calibration seeds each simulation by its index). A single script, run\_all.R, reproduces every table and figure; rerunning it yields byte-identical CSV output files. The code and outputs are provided as Online Resource 1.
:::

::: {custom-style="heading1"}
5 Results
:::

::: {custom-style="heading2"}
5.1 Summary statistics
:::

::: {custom-style="p1a"}
Table 2 reports descriptive statistics of index and proxy returns at the four frequencies.
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
Notes: Kurt. is non-excess kurtosis; P~cap~ is the mid-cap proxy of Eq. (6); \*\*\* p < 0.01. Source: Authors’ calculations based on HOSE index data (TradingView).
:::

At the daily frequency the standard deviation is highest for P~cap~ (0.0124) and lowest for VNINDEX (0.0115), as expected for the broadest index. All series are negatively skewed and leptokurtic, with kurtosis above 33 at M30, and the Jarque–Bera test rejects normality everywhere. DCCA and the block bootstrap do not require Gaussian returns, which is why we use them.

::: {custom-style="heading2"}
5.2 Reliability thresholds
:::

::: {custom-style="p1a"}
Table 3 reports the largest timescale at which the DCCA coefficient is estimated with a worst-case error below 0.05.
:::

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

The Gaussian thresholds range from 50 days at 1D to 444 bars at M30; heavy-tailed series reduce them by roughly a factor of three. All averages below use the Gaussian thresholds; recomputing them over the shorter heavy-tailed ranges changes the nested averages to 0.975–0.979 and the purged average to 0.882–0.890, so no conclusion depends on the choice.

::: {custom-style="heading2"}
5.3 Overlap inflation (H1)
:::

::: {custom-style="p1a"}
Table 4 compares the average DCCA coefficient of the nested pairs with that of the purged pair, and Fig. 2 shows the full curves with bootstrap bands.
:::

::: {custom-style="tablecaption"}
**Table 4** Average DCCA coefficients of nested and purged pairs
:::

| Frequency | Nested pairs | P~cap~–VN30 | Gap [95% CI] | Cohen’s q [95% CI] | N |
|---|---|---|---|---|---|
| *Panel A: synchronized window, 2017–2024* |  |  |  |  |  |
| Daily (1D) | 0.980 | 0.890 | 0.090 |  | 1,983 |
| 30-minute (M30) | 0.979 | 0.890 | 0.089 |  | 19,463 |
| 1-hour (H1) | 0.979 | 0.891 | 0.089 |  | 9,879 |
| 4-hour (H4) | 0.980 | 0.892 | 0.089 |  | 3,953 |
| *Panel B: full sample, 2014–2025* |  |  |  |  |  |
| Daily (1D) | 0.977 | 0.884 | 0.093 [0.074, 0.115] | 0.83 [0.75, 0.89] | 2,963 |
| 30-minute (M30) | 0.979 | 0.883 | 0.096 [0.080, 0.119] | 0.89 [0.83, 0.94] | 21,942 |
| 1-hour (H1) | 0.975 | 0.889 | 0.086 [0.071, 0.103] | 0.78 [0.70, 0.83] | 13,523 |
| 4-hour (H4) | 0.976 | 0.890 | 0.087 [0.072, 0.103] | 0.79 [0.72, 0.84] | 5,410 |

::: {custom-style="Compact"}
Notes: Averages of ρ(s) over s ≤ s~rel~ (Table 3, full-sample thresholds in both panels), m = 1; nested pairs: mean of VN30–VNINDEX, VN30–VN100 and VN100–VNINDEX. Brackets: block-bootstrap 95% intervals. Source: Authors’ calculations.
:::

The nested pairs average 0.975–0.980 at every frequency in both samples, whereas P~cap~–VN30 averages 0.883–0.892. The gap of 0.086–0.096 in the full sample has bootstrap intervals between 0.071 and 0.119, all excluding zero, and Cohen’s q (Cohen 1988) of 0.78–0.89 indicates a large effect on the Fisher scale. H1 is supported. The purged coefficient remains high, so the overlap inflates co-movement that is already strong rather than creating it. The two samples differ by at most 0.004 for the nested mean, so the result does not depend on the sample window.

The reason is the structure of the indices rather than market behavior: the VN30 component appears on both sides of each nested pair, so its variance enters the numerator and the denominator of Eq. (5) and pulls the ratio toward one. The statistical proxies confirm that the remaining signal must be extracted with capitalization weights: their average coefficients with VN30 lie between −0.16 and 0.07, and they correlate with each other at 0.980–0.997 but with P~cap~ at only 0.277–0.486, so they behave as amplified residuals rather than as mid-cap returns.

![](/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/docx_build/../outputs/figures/fig2_dcca_curves.png){width=6.3in}

::: {custom-style="figurecaption"}
**Fig. 2** DCCA coefficients of the nested pairs and P~cap~–VN30 by timescale: (a) 1D, (b) M30, (c) H1, (d) H4
:::
::: {custom-style="Compact"}
Notes: Line and marker types identify the pairs; grey bands are pointwise block-bootstrap 95% intervals; vertical dotted lines mark s~rel~ (Table 3). Source: Authors’ calculations based on HOSE index data (TradingView).
:::

::: {custom-style="heading2"}
5.4 The mechanical floor (H2)
:::

::: {custom-style="p1a"}
Table 5 applies Proposition 1 to the VN30–VN100 pair, and Fig. 3 plots the implied nested coefficient against the economic correlation.
:::

::: {custom-style="tablecaption"}
**Table 5** Exact overlap decomposition of the VN30–VN100 DCCA coefficient (Proposition 1)
:::

| Frequency | κ | Economic ρ~AM~ | Nested ρ~AB~ | Floor ρ̲ | Mechanical share | Sensitivity | Floor − ρ~AM~ |
|---|---|---|---|---|---|---|---|
| Daily (1D) | 0.484 | 0.884 [0.857, 0.906] | 0.988 | 0.900 [0.891, 0.910] | 0.911 [0.903, 0.920] | 0.106 [0.098, 0.114] | 0.016 [−0.005, 0.041] |
| 30-minute (M30) | 0.503 | 0.883 [0.859, 0.904] | 0.987 | 0.893 [0.882, 0.903] | 0.905 [0.895, 0.913] | 0.112 [0.104, 0.122] | 0.011 [−0.007, 0.032] |
| 1-hour (H1) | 0.486 | 0.889 [0.868, 0.905] | 0.988 | 0.899 [0.889, 0.909] | 0.910 [0.901, 0.918] | 0.107 [0.099, 0.116] | 0.010 [−0.002, 0.029] |
| 4-hour (H4) | 0.485 | 0.890 [0.865, 0.908] | 0.988 | 0.900 [0.890, 0.910] | 0.910 [0.902, 0.919] | 0.106 [0.098, 0.115] | 0.010 [−0.006, 0.031] |

::: {custom-style="Compact"}
Notes: Quantities of Eqs. (7)–(9) averaged over s ≤ s~rel~; A = VN30, B = VN100, M = P~cap~. Brackets: block-bootstrap 95% intervals. Source: Authors’ calculations.
:::

The relative amplitude κ is 0.48–0.50: the non-overlapping 32% of VN100 contributes roughly half as much detrended variation as the VN30 component. With κ of this size the floor is 0.893–0.900, so a VN30–VN100 coefficient of about 0.90 would be observed even if mid caps moved independently of large caps. The floor accounts for 0.905–0.911 of the observed coefficient, with bootstrap intervals between 0.895 and 0.920. H2 is supported. The point estimates of the floor also exceed the economic correlation itself, by 0.010–0.016, but the bootstrap intervals include zero at every frequency, so the mechanical floor and the economic correlation are of the same magnitude.

The sensitivity of Eq. (9) is 0.106–0.112. An analyst who reads the nested coefficient as a measure of large-cap and mid-cap co-movement would therefore need a change of about 9 times as large in the economic correlation to see a given change in the index-level number. Fig. 3 shows the consequence: as the economic correlation moves from −0.5 to 1, the nested coefficient moves only from about 0.87 to 1. The same identity applied to full-sample Pearson correlations of daily returns gives a floor of 0.903 and a mechanical share of 0.914, so the result is not specific to DCCA.

![](/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/docx_build/../outputs/figures/fig4_overlap_decomposition.png){width=6.3in}

::: {custom-style="figurecaption"}
**Fig. 3** Nested VN30–VN100 coefficient implied by Proposition 1 as a function of the economic correlation
:::
::: {custom-style="Compact"}
Notes: Lines: Eq. (7) evaluated at the average κ of each frequency (Table 5); markers: observed values; dashed horizontal line: daily floor; dotted line: 45-degree line. Source: Authors’ calculations.
:::

::: {custom-style="heading2"}
5.5 Horizon dependence (H3)
:::

::: {custom-style="p1a"}
Table 6 reports scaling slopes at the 30-minute frequency, where the reliable range is widest, with intervals and multiplicity-adjusted p-values; Table A1 reports the other frequencies.
:::

::: {custom-style="tablecaption"}
**Table 6** Scaling slopes of DCCA coefficients at the 30-minute frequency
:::

| Pair | Full range [95% CI] | Reliable range [95% CI] | p | p (Holm) | p (BH) |
|---|---|---|---|---|---|
| VN30–VNINDEX | 0.0016 [−0.0025, 0.0034] | 0.0022 [0.0007, 0.0038] | 0.012 | 0.216 | 0.057 |
| VN100–VNINDEX | 0.0009 [−0.0010, 0.0021] | 0.0022 [0.0011, 0.0032] | 0.004 | 0.076 | 0.057 |
| VN30–VN100 | 0.0001 [−0.0015, 0.0010] | −0.0001 [−0.0007, 0.0007] | 0.980 | 1.000 | 0.980 |
| P~cap~–VN30 | 0.0025 [−0.0102, 0.0093] | 0.0017 [−0.0045, 0.0078] | 0.520 | 1.000 | 0.894 |
| P~heur~–VN30 | 0.0222 [−0.0236, 0.0582] | 0.0289 [−0.0033, 0.0534] | 0.080 | 1.000 | 0.217 |
| P~ratio~–VN30 | 0.0221 [−0.0226, 0.0589] | 0.0291 [−0.0030, 0.0531] | 0.076 | 1.000 | 0.217 |
| P~res~–VN30 | 0.0220 [−0.0249, 0.0574] | 0.0283 [−0.0029, 0.0526] | 0.080 | 1.000 | 0.217 |

::: {custom-style="Compact"}
Notes: Slopes of Eq. (11); full range: 30 scales from 5 to 5,485 bars; reliable range: s ≤ 444. p-values refer to the reliable-range slope; Holm and Benjamini–Hochberg (BH) adjustments are across all 19 reliable-range tests. Source: Authors’ calculations.
:::

Three patterns emerge. First, the VN30–VN100 slope is indistinguishable from zero in both ranges, as Proposition 1 predicts: the coefficient is bounded below by its floor and almost insensitive to the economic correlation, and both depend on scale only through κ(s) and ρ~AM~(s). Second, the broad-market pairs VN30–VNINDEX and VN100–VNINDEX have positive reliable-range slopes whose unadjusted intervals exclude zero (0.0022 and 0.0022), which over the reliable range correspond to a rise of about 0.01 in the coefficient; over the full range, where long scales rest on few boxes, the intervals include zero. Third, the purged P~cap~–VN30 slope is insignificant in both ranges, and the statistical proxies have larger but imprecise slopes, consistent with amplified noise.

Across all 19 reliable-range tests, 4 percentile intervals exclude zero (VN100–VNINDEX at H1; VN30–VNINDEX at H1; VN100–VNINDEX at M30; VN30–VNINDEX at M30), with unadjusted bootstrap p-values of 0.004–0.012. After Benjamini–Hochberg adjustment 0 remain significant at 5% (smallest adjusted p = 0.057), and after Holm adjustment 0 remain. No slope is significant at the daily or 4-hour frequency. H3 is therefore not supported once multiple testing is accounted for. The unadjusted pattern is nevertheless the one H3 predicts: positive slopes appear only for broad-market pairs at intraday frequencies, never for VN30–VN100, and they are small. This fits the Epps effect, which operates at intraday horizons and involves the less liquid constituents that VNINDEX contains and VN30 does not, but the evidence is weak.

::: {custom-style="heading2"}
5.6 Volatility regimes and contagion (H4)
:::

::: {custom-style="p1a"}
Table 7 reports the unadjusted and Forbes–Rigobon conditioned correlations of P~cap~ and VN30.
:::

::: {custom-style="tablecaption"}
**Table 7** Forbes–Rigobon conditioning of the P~cap~–VN30 correlation
:::

| Regime definition | ρ~low~ | ρ~high~ | δ | ρ* | ρ* − ρ~low~ [95% CI] | p | Power |
|---|---|---|---|---|---|---|---|
| Chronological crises | 0.847 | 0.924 | 2.21 | 0.803 | −0.044 [−0.082, 0.001] | 0.985 | 0.77 |
| Rolling-volatility quartiles | 0.727 | 0.928 | 7.06 | 0.661 | −0.066 [−0.132, 0.008] | 0.974 | 0.41 |

::: {custom-style="Compact"}
Notes: Pearson correlations of daily returns; δ = relative increase in VN30 return variance; p: one-sided bootstrap p-value for H0: ρ* ≤ ρ~low~; power against an increase of 0.05. Chronological: 1,000 calm and 539 crisis days; quartiles: 739 days per regime. Source: Authors’ calculations.
:::

Under the chronological definition the raw correlation rises from 0.847 in calm years to 0.924 in crises while the variance of VN30 returns rises by 221%. After conditioning, the crisis correlation is 0.803, and its difference from the calm level is −0.044 (95% interval −0.082 to 0.001; p = 0.985). Under the quartile definition, the variance expansion is larger (δ = 7.06) and the raw correlation rises from 0.727 to 0.928, but the adjusted correlation (0.661) again does not exceed the calm level (p = 0.974). H4 is not supported. The power against an increase of 0.05 is 0.77 and 0.41, so moderate structural increases are unlikely under the first definition, while small ones cannot be excluded under either.

The mechanism is the heteroskedasticity bias of Eq. (12): a common volatility shock raises the share of variance explained by the common factor, which lifts the raw correlation without any change in how mid caps respond to large caps. Both regime definitions are ex post, and the quartile regimes are sorted on VNINDEX, which contains the mid caps, so the comparison describes in-sample regimes rather than a real-time signal. For the nested pairs, raw correlations also rise in crises, but the identification condition fails, so we do not test them.

::: {custom-style="heading2"}
5.7 Portfolio variance misstatement (H5)
:::

::: {custom-style="p1a"}
Applying Eq. (13) with the regime correlations of Table 7, a static correlation overstates the variance of an equally weighted VN30 and P~cap~ position by 2.23% (95% interval 0.91 to 3.94) in the chronological calm regime and by 9.38% (6.20 to 13.46) in the low-volatility quartile. In turbulent regimes it understates the variance by 1.84% (0.95 to 2.63) and 2.07% (1.25 to 2.84). All four intervals exclude zero, so H5 is supported. For cash portfolios of parent and child indices the daily misstatement is at most 2.35%, because their correlations are bounded below by the mechanical floor and barely move across regimes.
:::

The asymmetry has a simple source. The variance error is proportional to the gap between the static and the regime correlation, and the purged correlation varies far more across regimes than the nested ones. The understatement in crises is small in percentage terms, but it occurs when VN30 return variance has already risen by 221% to 706%. Because P~cap~ is not investable, these numbers describe a mid-cap factor exposure, for example one held through a mid-cap index fund, combined with large caps; no trading strategy is implied, so turnover and transaction costs do not arise.

::: {custom-style="heading2"}
5.8 Multifractal structure
:::

::: {custom-style="p1a"}
The generalized cross-correlation exponent h~xy~(2) lies between 0.536 and 0.542 for the four pairs, indicating weak persistence. The multifractal range Δh is 0.252–0.431 for the nested pairs and 0.435–0.656 for P~cap~–VN30, but shuffled surrogates show that most of this range reflects fat tails: the P~cap~–VN30 range exceeds the 95th surrogate percentile only at 1D, and the nested pairs exceed it in 2 of 12 cases. Fig. 4 contrasts the daily spectra. The multifractal evidence supports only a modest nonlinear structure and does not change the conclusions above.
:::

![](/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/docx_build/../outputs/figures/fig3_mfdcca.png){width=6.3in}

::: {custom-style="figurecaption"}
**Fig. 4** MF-DCCA at the daily frequency: (a) singularity spectra f(α); (b) generalized exponents h~xy~(q)
:::
::: {custom-style="Compact"}
Notes: q ∈ [−5, 5] \ {0}; daily data. Source: Authors’ calculations based on HOSE index data (TradingView).
:::

::: {custom-style="heading2"}
5.9 Robustness
:::

::: {custom-style="p1a"}
The Appendix collects five robustness checks. Table A1 extends the slope tests to the other frequencies: VN30–VNINDEX and VN100–VNINDEX have positive reliable-range slopes at H1 with unadjusted intervals excluding zero (0.0024, [0.0006, 0.0041] and 0.0019, [0.0007, 0.0032]) but not at 1D or H4, and the P~cap~–VN30 slope is insignificant everywhere. Table A2 varies the capitalization weight from 0.60 to 0.75: a larger weight removes more of the VN30 component and lowers the purged correlation, but the gap to the nested pairs stays at or above 0.052. Table A3 replaces DCCA with the detrending moving-average cross-correlation coefficient (DMCA; Kristoufek 2014): the purged coefficient is 0.882–0.891 and the gap 0.086–0.096, almost identical to Table 4. Table A4 reports lower-tail dependence at the 5% and 10% quantiles: 0.75 for P~cap~–VN30 against 0.90 for VN30–VN100 at 5%, so overlap also inflates joint crash probabilities. Table A5 shows that the bootstrap interval of the daily gap stays within 0.070 to 0.119 for mean block lengths from 5 to 60 days. Finally, the daily VN30–VNINDEX average is 0.9665, 0.9663 and 0.9667 for detrending orders 1, 2 and 3.
:::

::: {custom-style="heading2"}
5.10 Summary of hypothesis tests
:::

::: {custom-style="p1a"}
Table 8 summarizes the outcome of each hypothesis.
:::

::: {custom-style="tablecaption"}
**Table 8** Summary of hypothesis tests
:::

| Hypothesis | Test | Evidence | Outcome |
|---|---|---|---|
| H1 Overlap inflation | Bootstrap CI of gap | Gap 0.086–0.096; all CIs > 0 | Supported |
| H2 Mechanical dominance | One-sided test, share > 0.5 | Share 0.905–0.911; lower CI ≥ 0.895 | Supported |
| H3 Horizon dependence | Slope CIs; Holm and BH | 4 of 19 unadjusted CIs > 0; 0 BH- and 0 Holm-significant | Not supported after adjustment |
| H4 Contagion | Forbes–Rigobon, one-sided | p = 0.985 and 0.974 | Not supported |
| H5 Risk misstatement | Bootstrap CI of RE | −2.1% to 9.4%; CIs exclude 0 | Supported |

::: {custom-style="Compact"}
Notes: All tests at the 5% level; details in Tables 4–7 and Section 5.7. Source: Authors’ calculations.
:::

::: {custom-style="heading1"}
6 Discussion
:::

::: {custom-style="heading2"}
6.1 Mechanisms
:::

::: {custom-style="p1a"}
The results have one common source. When a parent index contains a child index, the child’s variance appears in both terms of every covariance and in both standard deviations, and Proposition 1 shows that this fixes a floor below which the nested coefficient cannot fall. With VN30 holding 68% of VN100, the floor is near 0.90, so the observed 0.99 contains little information about how mid caps move with large caps. The same structure explains why the VN30–VN100 coefficient is flat across horizons and regimes: it cannot fall below its floor and responds weakly to the economic correlation, and the floor depends on time and scale only through relative volatility.
:::

Once the overlap is removed, the remaining dependence behaves like economic co-movement. It is high, because large and mid caps trade on the same exchange and respond to the same domestic shocks, but it is lower than the index-level numbers suggest. It rises in crises only as much as the common volatility shock implies, consistent with the interdependence interpretation of Forbes and Rigobon (2002) rather than with a change in transmission. The weak, unadjusted intraday horizon dependence of broad-market pairs is consistent with the Epps (1979) effect: VNINDEX contains small stocks, whose liquidity is more fragile than that of large caps (Chen et al. 2021) and whose prices adjust with a lag, and aggregation over longer horizons removes the lag. Our index-level data cannot separate this from gradual information diffusion (Hong and Stein 1999).

::: {custom-style="heading2"}
6.2 Implications
:::

::: {custom-style="p1a"}
For risk management, index-level correlations between nested benchmarks should not be used to measure diversification between size tiers; Eq. (7) shows how to recover the economic correlation from weights and fluctuation amplitudes, and the variance results show that regime-conditioned correlations matter for mid-cap exposures but not for blends of parent and child indices. For index providers and the exchange, standalone non-overlapping segment benchmarks, such as an investable VNMIDCAP fund or mid-cap index futures alongside the existing VN30 futures, would let investors hold and hedge the mid-cap tier without the hidden overlap. For other markets with nested architectures, such as the SET50 within the SET100 in Thailand or the IDX30 within the LQ45 in Indonesia, the identity applies directly, but the size of the floor depends on their weights and volatilities and must be estimated.
:::

::: {custom-style="heading2"}
6.3 Limitations and future research
:::

::: {custom-style="p1a"}
The evidence comes from one exchange, three indices and one decomposition, so the empirical magnitudes should not be generalized beyond the HOSE. The mid-cap proxy relies on a single factsheet weight; Table A2 shows that the conclusions hold for weights from 0.60 to 0.75, but validating the proxy against the published VNMIDCAP index and reconstructing the weight path from semi-annual reviews would sharpen identification. The decomposition was applied to the VN30–VN100 pair only, because no capitalization weight for VN100 within VNINDEX was available; with such a weight the same identity extends to the broad-market pairs. Index-level closing prices cannot separate microstructure frictions from information diffusion, the Forbes–Rigobon test has limited power against small structural changes, and the regimes are classified ex post, so an out-of-sample evaluation of regime-conditioned risk budgets is needed before the portfolio results can guide practice.
:::

::: {custom-style="heading1"}
7 Conclusion
:::

::: {custom-style="p1a"}
Correlations between nested equity indices contain a mechanical floor that is fixed by index construction. We derive this floor exactly, at every timescale, and show that on the HOSE it accounts for about nine-tenths of the VN30–VN100 DCCA coefficient, leaving the index-level number almost insensitive to the economic co-movement between large and mid caps. Removing the overlap lowers the correlation with large caps by about 0.09, the remaining dependence shows no evidence of crisis contagion once volatility is conditioned on, and static correlations misstate the variance of mid-cap exposures by amounts that change sign with the volatility regime. Risk models and benchmark design in nested index systems should therefore rely on non-overlapping segment returns or on the decomposition derived here.
:::

::: {custom-style="heading1"}
Appendix A Robustness tables
:::

::: {custom-style="tablecaption"}
**Table A1** Scaling slopes at the daily, 1-hour and 4-hour frequencies
:::

| Frequency | Pair | Full range [95% CI] | Reliable range [95% CI] | p (BH) |
|---|---|---|---|---|
| Daily (1D) | VN30–VNINDEX | 0.0020 [−0.0064, 0.0043] | 0.0010 [−0.0031, 0.0043] | 0.894 |
| Daily (1D) | VN100–VNINDEX | 0.0005 [−0.0052, 0.0026] | 0.0008 [−0.0021, 0.0027] | 0.894 |
| Daily (1D) | P~cap~–VN30 | 0.0014 [−0.0255, 0.0118] | −0.0040 [−0.0157, 0.0085] | 0.894 |
| 1-hour (H1) | VN30–VNINDEX | 0.0015 [−0.0027, 0.0040] | 0.0024 [0.0006, 0.0041] | 0.057 |
| 1-hour (H1) | VN100–VNINDEX | 0.0007 [−0.0021, 0.0025] | 0.0019 [0.0007, 0.0032] | 0.057 |
| 1-hour (H1) | P~cap~–VN30 | −0.0003 [−0.0137, 0.0089] | 0.0020 [−0.0035, 0.0089] | 0.828 |
| 4-hour (H4) | VN30–VNINDEX | 0.0014 [−0.0056, 0.0039] | 0.0003 [−0.0026, 0.0029] | 0.899 |
| 4-hour (H4) | VN100–VNINDEX | 0.0005 [−0.0043, 0.0025] | 0.0002 [−0.0018, 0.0021] | 0.894 |
| 4-hour (H4) | P~cap~–VN30 | 0.0001 [−0.0176, 0.0103] | −0.0020 [−0.0124, 0.0067] | 0.894 |

::: {custom-style="Compact"}
Notes: Slopes of Eq. (11); reliable ranges from Table 3; BH: Benjamini–Hochberg adjustment across all 19 reliable-range tests. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table A2** Sensitivity of the purged correlation to the capitalization weight w
:::

| w | Mean ρ (1D) | Gap to nested | Slope (M30) | Calm ρ~low~ | Crisis ρ~high~ |
|---|---|---|---|---|---|
| 0.6000 | 0.924 | 0.052 | 0.0014 | 0.899 | 0.952 |
| 0.6500 | 0.903 | 0.074 | 0.0019 | 0.871 | 0.937 |
| 0.6826 (baseline) | 0.884 | 0.093 | 0.0025 | 0.847 | 0.924 |
| 0.7200 | 0.855 | 0.122 | 0.0033 | 0.812 | 0.904 |
| 0.7500 | 0.824 | 0.153 | 0.0043 | 0.775 | 0.881 |

::: {custom-style="Compact"}
Notes: ρ~low~ and ρ~high~ are Pearson correlations in the chronological regimes (Table 7). Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table A3** Average DMCA coefficients over the reliable range
:::

| Frequency | VN30–VNINDEX | VN30–VN100 | VN100–VNINDEX | P~cap~–VN30 | Gap |
|---|---|---|---|---|---|
| Daily (1D) | 0.966 | 0.987 | 0.976 | 0.882 | 0.094 |
| 30-minute (M30) | 0.969 | 0.987 | 0.982 | 0.883 | 0.096 |
| 1-hour (H1) | 0.965 | 0.988 | 0.975 | 0.890 | 0.086 |
| 4-hour (H4) | 0.966 | 0.988 | 0.975 | 0.891 | 0.086 |

::: {custom-style="Compact"}
Notes: Centered moving-average detrending with odd windows matched to the DCCA scales s ≤ s~rel~; gap: mean of the nested pairs minus P~cap~–VN30. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table A4** Lower-tail dependence of daily returns
:::

| Pair | u = 0.05 [95% CI] | u = 0.10 [95% CI] |
|---|---|---|
| VN30–VN100 | 0.904 [0.874, 0.958] | 0.921 [0.901, 0.954] |
| VN30–VNINDEX | 0.850 [0.817, 0.931] | 0.847 [0.813, 0.891] |
| VN100–VNINDEX | 0.864 [0.830, 0.945] | 0.864 [0.834, 0.908] |
| P~cap~–VN30 | 0.749 [0.702, 0.830] | 0.766 [0.717, 0.803] |

::: {custom-style="Compact"}
Notes: Empirical λ~L~(u) = P(X ≤ q~X~(u), Y ≤ q~Y~(u))/u; block-bootstrap intervals. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table A5** Sensitivity of the daily gap interval to the bootstrap block length
:::

| Mean block length (days) | Gap | 95% CI |
|---|---|---|
| 5 | 0.093 | [0.079, 0.110] |
| 10 | 0.093 | [0.077, 0.111] |
| 20 | 0.093 | [0.074, 0.117] |
| 40 | 0.093 | [0.073, 0.119] |
| 60 | 0.093 | [0.070, 0.119] |

::: {custom-style="Compact"}
Notes: Gap between the nested-pair mean and P~cap~–VN30 (Table 4, Panel B, 1D). Source: Authors’ calculations.
:::

::: {custom-style="p1a"}
**Ethical standards** This study uses only publicly available historical index price data from the Ho Chi Minh City Stock Exchange; it involves no human participants or personal data, therefore required no ethical approval, and complies with the current laws of Vietnam.
:::

::: {custom-style="p1a"}
**Data availability** The index price data were obtained from TradingView (exchange: HOSE) and are subject to the vendor’s terms of use; the merged dataset is available from the corresponding author upon reasonable request.
:::

::: {custom-style="p1a"}
**Code availability** The R code that reproduces every table and figure is provided as Online Resource 1 and will be deposited in a public repository upon acceptance.
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
Chen, R., Geng, H., Lin, H., & Nguyen, P. T. L. (2021). Liquidity, informed trading, and a market surveillance system: Evidence from the Vietnamese stock market. Pacific-Basin Finance Journal, 67, 101567. https://doi.org/10.1016/j.pacfin.2021.101567
:::

::: {custom-style="referenceitem"}
Chen, Y., Zhang, J., Lu, L., & Xie, Z. (2024). Cross-correlation and multifractality analysis of the Chinese and American stock markets based on the MF-DCCA model. Heliyon, 10(17), e36537. https://doi.org/10.1016/j.heliyon.2024.e36537
:::

::: {custom-style="referenceitem"}
Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Lawrence Erlbaum Associates. https://doi.org/10.4324/9780203771587
:::

::: {custom-style="referenceitem"}
DeCoste, J. (2025). Comovement and S&P 500 membership. Global Finance Journal, 65, 101110. https://doi.org/10.1016/j.gfj.2025.101110
:::

::: {custom-style="referenceitem"}
Epps, T. W. (1979). Comovements in stock prices in the very short run. Journal of the American Statistical Association, 74(366), 291–298. https://doi.org/10.1080/01621459.1979.10482508
:::

::: {custom-style="referenceitem"}
Forbes, K. J., & Rigobon, R. (2002). No contagion, only interdependence: Measuring stock market comovements. The Journal of Finance, 57(5), 2223–2261. https://doi.org/10.1111/0022-1082.00494
:::

::: {custom-style="referenceitem"}
Ge, X., & Lin, A. (2021). Multiscale multifractal detrended partial cross-correlation analysis of Chinese and American stock markets. Chaos, Solitons & Fractals, 145, 110731. https://doi.org/10.1016/j.chaos.2021.110731
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
Holm, S. (1979). A simple sequentially rejective multiple test procedure. Scandinavian Journal of Statistics, 6(2), 65–70. https://www.jstor.org/stable/4615733
:::

::: {custom-style="referenceitem"}
Hong, H., & Stein, J. C. (1999). A unified theory of underreaction, momentum trading, and overreaction in asset markets. The Journal of Finance, 54(6), 2143–2184. https://doi.org/10.1111/0022-1082.00184
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
Longin, F., & Solnik, B. (2001). Extreme correlation of international equity markets. The Journal of Finance, 56(2), 649–676. https://doi.org/10.1111/0022-1082.00340
:::

::: {custom-style="referenceitem"}
Markowitz, H. (1952). Portfolio selection. The Journal of Finance, 7(1), 77–91. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x
:::

::: {custom-style="referenceitem"}
Michis, A. A. (2022). Multiscale partial correlation clustering of stock market returns. Journal of Risk and Financial Management, 15(1), 24. https://doi.org/10.3390/jrfm15010024
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
Rodriguez, E., & Alvarez-Ramirez, J. (2021). Time-varying cross-correlation between trading volume and returns in US stock markets. Physica A: Statistical Mechanics and its Applications, 581, 126211. https://doi.org/10.1016/j.physa.2021.126211
:::

::: {custom-style="referenceitem"}
Santana, T. P., Horta, N., Revez, C., Dias, R. M. T. S., & Zebende, G. F. (2023). Effects of interdependence and contagion on crude oil and precious metals according to ρDCCA: A COVID-19 case study. Sustainability, 15(5), 3945. https://doi.org/10.3390/su15053945
:::

::: {custom-style="referenceitem"}
Tilfani, O., Ferreira, P., & El Boukfaoui, M. Y. (2021). Dynamic cross-correlation and dynamic contagion of stock markets: A sliding windows approach with the DCCA correlation coefficient. Empirical Economics, 60(3), 1127–1156. https://doi.org/10.1007/s00181-019-01806-1
:::

::: {custom-style="referenceitem"}
Tran, M. H., & Tran, N. M. (2025). High-frequency dynamics of the Vietnam stock market. VNU Journal of Economics and Business, 5(2), 51–59. https://doi.org/10.57110/vnu-jeb.v5i2.395
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
