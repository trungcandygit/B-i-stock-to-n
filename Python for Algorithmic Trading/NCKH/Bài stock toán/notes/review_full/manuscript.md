# Nested Equity Index Correlations Overstate True Co-Movement: Evidence from Vietnam

Abstract: Asset allocators in emerging Southeast Asian markets frequently treat large-cap and broad-market indices as separate diversification instruments, even in nested architectures where large-cap stocks dominate the broader market. Standard risk models thereby conflate mechanical constituent overlap with genuine economic co-movement. Utilizing Detrended Cross-Correlation Analysis (DCCA) and its multifractal extension on 30-minute, 1-hour, 4-hour and daily data from the Ho Chi Minh City Stock Exchange (2014–2025), this study illustrates that near-perfect correlations among nested indices (0.975–0.980) primarily reflect shared capitalization rather than cross-tier interdependence. Purging constituent overlap with a capitalization-weighted mid-cap proxy lowers the correlation with large caps by 0.086–0.096. Furthermore, at intraday frequencies this co-movement tends to strengthen over longer holding horizons as microstructure frictions resolve and information diffuses throughout the market. Raw cross-tier correlation rises from 0.63 to 0.93 in high-volatility regimes, but Forbes–Rigobon volatility conditioning shows that the rise is explained by volatility expansion, indicating interdependence rather than contagion. Consequently, static models overstate mid-cap portfolio variance by up to 15.6% during calm market regimes and understate it during turbulent regimes. These research findings highlight the imperative for independent mid-cap benchmarks and volatility-regime-sensitive risk budgeting across the capital markets of the Association of Southeast Asian Nations (ASEAN).

Keywords: constituent overlap, DCCA, Forbes–Rigobon adjustment, multiscale correlation, portfolio risk, Vietnam.

JEL Classification: C58, G11, G12.

# 1 Introduction

Portfolio managers and institutional asset allocators in emerging equity markets frequently construct multi-capitalization portfolios under the assumption that large-cap and mid-cap stock indices serve as independent diversification instruments. In empirical practice, risk models, asset allocation algorithms, and regulatory stress-testing frameworks routinely parameterize cross-asset dependence using a single static Pearson correlation coefficient estimated from daily closing prices (Markowitz 1952). This conventional approach embeds two critical, yet rarely tested, assumptions: first, that cross-asset co-movement is scale-invariant across holding horizons ranging from high-frequency intraday intervals to multi-month cycles; and second, that cross-sectional dependence remains constant across calm and volatile market regimes.

In nested equity index systems, this reliance on static correlations creates an econometric bias. Across Southeast Asian equity markets, index providers routinely employ nested, capitalization-tiered architectures. For example, the FTSE Bursa Malaysia KLCI (top 30) is nested within the FTSE Bursa Malaysia Top 100 Index and FBM EMAS Index, the SET50 is nested within the SET100 in Thailand, and the IDX30 is nested within the LQ45 in Indonesia. While mature ASEAN exchanges, such as Bursa Malaysia, support continuous cash-futures arbitrage and market completeness through Regulated Short Selling (RSS) and Intraday Short Selling (IDSS) on eligible constituent equities, emerging frontier exchanges frequently operate under binding short-sale prohibitions and slower settlement cycles. On the Ho Chi Minh City Stock Exchange (HOSE), the flagship large-cap index (VN30) is fully embedded within the top-100 benchmark (VN100), which is in turn nested within the broad market index (VNINDEX), satisfying the strict subset relation:

Because the 30 largest firms represent over two-thirds of the free-float market capitalization of VN100, the return co-movement among these indices is mechanically bound by construction. Treating their empirical correlation as an indicator of genuine economic linkage conflates index engineering overlap with market co-movement. When an institutional investor diversifies across the VN30 and VN100, the perceived diversification benefit may be largely illusory.

To separate multiscale dynamics from nonstationary noise, econophysics and financial econometrics have increasingly adopted Detrended Cross-Correlation Analysis (DCCA) (Podobnik and Stanley 2008) and its multifractal generalization (MF-DCCA) (Zhou 2008). Building on Detrended Fluctuation Analysis (Kantelhardt et al. 2002), DCCA evaluates cross-correlations across non-overlapping temporal segments after filtering out local polynomial trends. Zebende (2011) normalized the DCCA covariance to establish a bounded correlation metric, while Podobnik et al. (2011) established the analytical finite-sample distribution for hypothesis testing. Subsequent advances have integrated moving-average formalisms (Jiang and Zhou 2011) and transfer entropy (Zhou et al. 2025). Applied empirical studies confirm that multiscale cross-correlations vary systematically across holding periods in developed equity markets, commodity baskets, and cross-border assets (Al Rababa’a et al. 2021; Aslam et al. 2023; Chen et al. 2024). However, this literature predominantly analyzes asset pairs that are strictly disjoint in their constituent composition (such as stock-bond pairs or cross-country equity benchmarks). The behavioral dynamics of multiscale cross-correlations within nested index architectures, where mechanical overlap and genuine economic transmission coexist, remain an unaddressed empirical issue.

This gap in the benchmark design interacts directly with index engineering and constituent overlap. When index providers construct size-based benchmarks using top-down capitalization cut-offs, large-cap equities inevitably dominate broad-market indices. While Michis (2022) applied wavelet partial correlations to eliminate redundant factor exposures in non-overlapping asset clusters, Rodriguez and Alvarez-Ramirez (2021) documented time- and scale-varying volume–return cross-correlations in US equity markets. Emerging markets face substantial risk from passive tracking. If risk models fail to purge shared constituent capitalization, they mistake mechanical index engineering for economic diversification.

Market regime shifts and microstructure frictions complicate this dependence. A well-established empirical stylized fact is that cross-asset correlations are asymmetric, increasing during market downturns when diversification is critical (Ang and Chen 2002; Longin and Solnik 2001). However, Forbes and Rigobon (2002) showed that unadjusted sample correlations increase mechanically with market volatility, so that an observed correlation surge may reflect volatility expansion rather than a structural change in cross-market linkages. At intraday intervals, this dynamic intersects with the Epps (1979) effect, where non-synchronous transactions and quote delays depress short-horizon correlations. In parallel, gradual information diffusion models (Hong and Stein 1999) suggest that market-wide news shocks are incorporated rapidly into liquid large caps before diffusing into less liquid mid-caps. Recent empirical evidence from Vietnam confirms that retail dominance and liquidity constraints generate delayed price adjustments and nonlinear volatility spillovers (Le et al. 2025; Tran and Tran 2025).

Regional studies show that financial integration across ASEAN equity markets is time-varying and shaped by trade linkages, market volatility and external shocks (Karim and Ning 2013; Lean and Teng 2013). While mature regional platforms such as Bursa Malaysia provide market-completeness mechanisms such as Regulated Short Selling (RSS) and Intraday Short Selling (IDSS) to facilitate continuous cross-tier arbitrage, Vietnam’s HOSE operates under strict statutory prohibitions on cash short selling. We frame this structural contrast as an institutional comparative hypothesis regarding how trading restrictions interact with multiscale price synchronization.

To address these unresolved issues, this study examines VN30, VN100 and VNINDEX from January 2014 to December 2025 at four trading frequencies: 30-minute (M30), 1-hour (H1), 4-hour (H4) and daily (1D). To isolate genuine economic linkage from constituent overlap, we construct a capitalization-weighted proxy (Pcap) that extracts the mid-cap component of VN100 using free-float market weights, and we benchmark it against three alternative statistical decompositions. In addition, we examine regime-dependent correlation shifts using the conditioning framework of Forbes and Rigobon (2002) and quantify the resulting misstatement in Markowitz portfolio variance.

This study makes three primary contributions to the extant empirical finance and risk management literature.

Firstly, we map the overlap distortion in nested benchmark systems. While headline large-cap and broad-market indices exhibit near-perfect cross-correlations (0.975–0.980) across intraday and daily intervals, this apparent co-movement falls by 0.086–0.096 correlation points once shared capitalization is extracted through a market-weighted mid-cap proxy. We further show that, at the 30-minute frequency, the purged cross-tier dependence tends to increase with the investment horizon (significantly over the full scale range and with the same sign over the reliable range), consistent with the resolution of intraday microstructure frictions and the gradual diffusion of market-wide information.

Secondly, we provide a volatility-conditioned evaluation of crisis dynamics. Raw cross-tier correlations tighten by up to 0.30 correlation points in high-volatility regimes, which would conventionally be read as a correlation breakdown. Applying the Forbes and Rigobon (2002) adjustment under two regime definitions, we show that the adjusted crisis correlation never significantly exceeds its calm-period level. Mid-cap diversification failure during Vietnamese market stress therefore reflects interdependence amplified by volatility rather than a structural change in cross-tier transmission.

Thirdly, we quantify the risk-management cost of static correlations. Cash portfolios formed from parent and child indices suffer variance misstatements of at most 2.7% because their constituents overlap, whereas for a dedicated mid-cap exposure a static correlation overstates portfolio variance by up to 15.6% in calm regimes and understates it by about 2% in turbulent regimes, when volatility itself has multiplied. Given the statutory prohibition on cash short selling in Vietnam, the synthetic mid-cap construct serves as a practical shadow benchmark for risk attribution, stress testing and index-product development.

The remainder of the paper is organized as follows. Section 1.1 describes the current situation and institutional background of the HOSE. Section 2 presents the data and methods, Section 3 reports the results, including multiscale scaling and robustness checks, and Section 4 discusses the findings and concludes.

## 1.1 Current Situation and Institutional Background of the HOSE

The institutional architecture of the HOSE, regulated by the State Securities Commission of Vietnam (SSC), imposes specific regulatory constraints that directly shape price discovery, return distributions and cross-asset correlations.

The primary microstructure constraint is the symmetric daily price fluctuation band of ±7% relative to the previous session’s reference price. During sharp market corrections, heavily sold equities frequently hit lower limits, causing liquidity to freeze. This price collar truncates empirical return tails, is associated with artificial serial correlation, and coincides with mechanical spikes in cross-correlations as multiple index constituents are locked at the limit.

The second structural feature is the settlement cycle. Throughout most of our sample period, equities purchased on the HOSE could not be sold until the afternoon of the second business day. This settlement delay restricts intraday statistical arbitrage, preventing high-frequency traders from eliminating the pricing discrepancies between index constituents and synthetic baskets.

In addition, each trading day opens and closes with a call auction: a 15-minute batch auction sets the opening price (ATO, 09:00–09:15) and another sets the closing price (ATC, 14:30–14:45), with continuous order matching in between. At the 30-minute frequency, the first bar of each day contains the opening auction and the last bar contains the closing auction, so these bars display higher volatility and less synchronous clearing than midday bars.

Finally, securities legislation, including Decree 155/2020/ND-CP and SSC Circular 120/2020/TT-BTC, prohibits cash short selling: investors may sell only securities already held in their accounts. Margin regulations require an initial margin of at least 50%, capping gross leverage at about 2.0×, and Circular 68/2024/TT-BTC, which removed the pre-funding requirement for foreign institutional investors, left the short-sale prohibition unchanged. Although VN30 index futures trade on the Hanoi Stock Exchange derivatives market, no exchange-traded hedging instrument exists for the mid-cap segment. The absence of cash short selling prevents arbitrageurs from trading the spread between large caps and mid-caps, which can prolong intraday non-synchronicity (the Epps effect) and delay price synchronization between VN30 and mid-cap stocks.

# 2 Methods

## 2.1 Data and Sample Construction

The dataset comprises closing prices of three HOSE indices exported from TradingView (exchange: HOSE) for January 27, 2014, to December 12, 2025: the flagship VN30 index, comprising the 30 largest and most liquid stocks screened for free-float capitalization; the VN100 index, which combines the VN30 constituents with the next 70 largest liquid stocks (the constituents of the VNMIDCAP, or VN70, index); and the composite VNINDEX, which covers all common stocks listed on the HOSE. Because a VNMIDCAP price history is not available from our data source for the full sample and all frequencies, the mid-cap segment is recovered from VN100 and VN30 by the decomposition in Section 2.2.

The analysis evaluates four trading frequencies: 30-minute (M30), 1-hour (H1), 4-hour (H4) and daily (1D). To guarantee simultaneity and prevent alignment bias, the index series were synchronized by exact inner joins on timestamps, and log returns were computed as:

$Rt=ln(Pt)-ln(Pt-1).$

The empirical research design operates across two complementary sample tiers:

The first tier is the Multi-Frequency Synchronized Overlap Window (January 3, 2017 to December 9, 2024), establishing a strictly synchronized common calendar window where all four frequencies (M30, H1, H4, 1D) overlap simultaneously without calendar attrition (1D: N=1,983; M30: N=19,463; H1: N=9,879; H4: N=3,953). This sample forms the primary benchmark for cross-frequency comparisons.

The second tier is the Extended Historical Depth Sample, deployed to maximize data depth for scaling regressions, regime tests and Monte Carlo reliability thresholds (1D: February 2014–December 2025, N = 2,963; M30: January 2017–December 2025, N = 21,942; H1 and H4: January 2014–December 2024, N = 13,523 and 5,410). The 1-hour and 4-hour series available from the data vendor end on December 9, 2024, whereas the daily and 30-minute series extend to December 12, 2025. All four frequencies overlap without any calendar gap in the first tier, which is used for cross-frequency comparisons.

To limit survivorship and look-ahead bias, the analysis relies on official index levels calculated in real time by the HOSE rather than on indices back-calculated from current constituent lists. The HOSE reviews index constituents semi-annually, updating memberships and free-float adjustments on the basis of capitalization, liquidity and foreign-ownership criteria. Because the price series are the exchange-computed index levels, historical constituent changes, corporate actions and rebalancing adjustments are embedded in the return paths.

Regime dependence is evaluated under two definitions based on the 20-day rolling standard deviation of VNINDEX returns (Fig. 1).

The first definition uses continuous chronological crisis episodes. To avoid arbitrary selection, an episode must satisfy three conditions: (i) a peak-to-trough VNINDEX drawdown of more than 25%; (ii) at least 45% of its trading days in the top quartile of the rolling-volatility distribution; and (iii) a documented macro-financial trigger. Three episodes qualify: the 2018 margin contraction (January–December 2018; drawdown 26.2%, 47% of days in the top quartile), the 2020 COVID-19 shock (January–June 2020; 33.5%, 52%) and the 2022 corporate bond liquidity freeze (April–November 2022; 40.2%, 60%), totaling 539 crisis trading days. The calm benchmark comprises 2016–2017 and 2023–2024 (1,000 trading days). Transient spikes, such as the May 2014 South China Sea standoff (drawdown 14.8%) and the April 2025 tariff shock (18.1%), fail conditions (i) and (ii). The second definition sorts all days by rolling volatility, classifying days below the 25th percentile (10.6% annualized) as low-volatility and days above the 75th percentile (20.0%) as high-volatility.

Figure 1 maps the rolling annualized volatility of the VNINDEX alongside the three crisis episodes and the two quartile thresholds.

[FIGURE]

Fig. 1 Twenty-day rolling volatility of VNINDEX (annualized) and market regimes, 2014–2025

Notes: Shaded areas mark the three crisis episodes; dashed and dotted lines mark the 25th and 75th percentiles. Source: Authors’ calculations based on HOSE index data (TradingView).

## 2.2 The DCCA Cross-Correlation Coefficient

Following Podobnik and Stanley (2008) and Zebende (2011), the DCCA cross-correlation coefficient evaluates multiscale covariance after filtering out non-stationary local trends from the data. To preserve long-range dependence and eliminate high-frequency drift, we map the raw return series xt and yt into cumulative deviation profiles:

$Xk=t=1k(xt-x), Yk=t=1k(yt-y), k=1,2,…,N,$

where $x=1Nt=1Nxt$ and $y=1Nt=1Nyt$ denote the respective sample means.

Both profiles are subsequently partitioned into $Ns=⌊N/s⌋$ non-overlapping segments of equal timescale $s$. To prevent data loss near the boundary when $N$ is not an exact multiple of $s$, the partitioning is repeated from the opposite end of the series, generating $2Ns$ total segments.

To remove deterministic intraday patterns and local macroeconomic trends that would otherwise spuriously inflate cross-correlations, we fit local polynomial trends X̃ and Ỹ of order m using ordinary least squares (m = 1 representing linear DCCA) and compute the detrended covariance using piecewise boundary indexing:

$fDCCA2(s,ν)=1sk=1sX(ν-1)s+k-Xk,νY(ν-1)s+k-Yk,ν,for ν=1,…,Ns1sk=1sXN-(ν-Ns)s+k-Xk,νYN-(ν-Ns)s+k-Yk,ν,for ν=Ns+1,…,2Ns.$

To isolate aggregate co-movement at a specific holding horizon, we average the detrended covariances across all 2Ns segments to obtain the bivariate DCCA fluctuation function:

$FDCCA2(s)=12Nsν=12NsfDCCA2(s,ν).$

When $xt=yt$, the fluctuation function collapses to the standard univariate Detrended Fluctuation Analysis (DFA) functions, $FDFA,12(s)$ and $FDFA,22$ (Peng et al. 1994; Kantelhardt et al. 2002).

To bound the dependence metric within $[-1,1]$ and render cross-scale estimates directly comparable to classical correlation benchmarks, the DCCA cross-correlation coefficient normalizes the bivariate covariance by the product of univariate root mean square fluctuations:

$ρDCCA(s)=FDCCA2(s)FDFA,1(s)FDFA,2(s), ρDCCA(s)∈[-1,1],$

where $FDFA,i(s)=FDFA,i2(s)$ denotes the univariate root-mean-square fluctuation function.

To verify whether the observed co-movement at timescale s statistically exceeds random cross-sectional noise, we test the null hypothesis of cross-sectional independence (H0: ρDCCA(s) = 0) using the Podobnik et al. (2011) test statistic:

$t(s)=ρDCCA(s)N-s-21-ρDCCA2(s),$

which follows a Student-$t$ distribution with $N-s-2$ degrees of freedom under the null hypothesis (Podobnik et al. 2011).

Because VN30 is embedded within VN100, an auxiliary regression of VN100 returns on VN30 returns produces an R2 of 0.973–0.977 and a slope of 0.968–0.975 across the four frequencies (daily estimates shown):

$R100,t=αOLS+βOLSR30,t+εt, βOLS=0.971, αOLS=0.000.$

To isolate the non-overlapping mid-cap return component, we evaluate four candidate proxy formulations.

First, we define a fundamental capitalization-weighted proxy ($Pcap$) based on the constituent free-float market capitalization:

$Pcap,t=R100,t-w30R30,t1-w30,$

where w30 = 0.6826 is the free-float market-capitalization weight of VN30 within VN100 computed from the HOSE factsheet of May 31, 2024 (VND 1,316,288 billion and VND 1,928,303 billion, respectively), implying a scaling factor of 3.151. Because the decomposition is applied to logarithmic rather than arithmetic returns, it carries a small Jensen-inequality term; at the daily frequency this term is 3.6 × 10−6 per day and, accumulated over the reliable daily horizons (up to 50 days), remains below 2.5% of the corresponding cumulative return variance, so its effect on the DCCA estimates is negligible.

For comparison, we examine a statistically calibrated proxy (Pheur) that replaces the capitalization weight with the volatility-scaled OLS slope:

Pheur,t = (R100,t − wheurR30,t) / (1 − wheur),   wheur = βOLSσ30/σ100 = Corr(R30, R100).

Because the correlation between VN30 and VN100 returns approaches unity (0.9865–0.9885 across frequencies), the denominator collapses toward zero (0.0115–0.0135), amplifying the numerator by a factor of 74 to 87. Pheur therefore behaves as an amplified residual rather than an economic asset proxy: its daily standard deviation is 0.1576, compared with 0.0124 for Pcap. Statistical weights cannot substitute for capitalization weights in nested index systems.

Finally, we construct two baseline statistical proxies for completeness: the ratio-spread proxy (Pratio), defined as the change in the log ratio of VN100 to VN30 and therefore equal to the VN100 return minus the VN30 return, and the orthogonal residual proxy (Pres), defined as the residual of the auxiliary regression above. The three statistical proxies are almost perfectly correlated with one another (0.980–0.997).

Because synthesizing Pcap requires a long position of 315% in VN100 and a short position of 215% in VN30, the proxy cannot be executed in cash portfolios under the short-sale prohibition. We therefore treat Pcap strictly as an analytical shadow benchmark that isolates inter-tier economic dependence for risk budgeting.

## 2.3 Rebalancing and Weight Dynamics

A central econometric question in constructing the capitalization-weighted proxy Pcap is the stability of the constituent free-float market weight w30 over the 2014–2025 sample. In empirical market index administration, the constituent weights are not mathematically static. The HOSE conducts semi-annual constituent reviews. During these reviews, constituent memberships are refreshed, free-float factors ($f$) are recalibrated, and individual stock weights are adjusted to enforce the index capping rules. Between these discrete semi-annual rebalancing dates, constituent market capitalizations continuously drift in response to daily relative equity price movements.

When the true historical large-cap weight $w30,t$ drifts from the static baseline benchmark $w*=0.6826$, the return on the proxy extracted using fixed weights satisfies:

$Rmid,t=1-w30,t1-w*Rmid,t+w30,t-w*1-w*R30,t,$

which introduces a time-varying leakage of large-cap returns into the proxy, proportional to the gap between the true and the baseline weight. Because only one factsheet snapshot of free-float weights is available, we do not reconstruct the historical weight path; instead, Section 3.8.2 re-estimates the key statistics for weights between 0.60 and 0.75, a range that brackets plausible drift around the baseline.

## 2.4 The Forbes–Rigobon Volatility Conditioning Framework

To verify whether the surge in cross-correlation during turbulent market periods represents structural correlation breakdown or mechanical volatility expansion, we implement the conditioning framework proposed by Forbes and Rigobon (2002).

Let asset returns follow $yt=αFR+βFRxt+εt$, with $Var(εt)=σε2$ and cross-market variance $σx2$. The unadjusted sample correlation is:

$ρ=βFRσxσy=11+σε2βFR2σx2.$

As market volatility rises from a calm to a crisis regime, the unadjusted correlation increases toward one purely because the variance of the conditioning market rises, even when the structural slope and residual variance remain constant.

To eliminate this conditioning bias, Forbes and Rigobon define the unconditional correlation as follows:

$ρ*=ρhigh1+δ1-ρhigh2, where δ=σx,high2-σx,low2σx,low2.$

The Forbes–Rigobon identifying assumptions require that the conditioning benchmark be exogenous, with no contemporaneous feedback from the dependent series. This condition is plausible for the disjoint pair Pcap–VN30, in which large-cap returns serve as the market benchmark and the purged mid-cap component shares no constituents with VN30. For nested pairs (VN30–VN100, VN30–VNINDEX and VN100–VNINDEX), the assumption is violated by construction because VN30 accounts for over two-thirds of VN100 capitalization, so conditioning formulas yield unidentified parameters. We therefore restrict the formal test of a structural correlation increase to the Pcap–VN30 pair.

The identification boundary of the Forbes–Rigobon framework during acute market stress is explicitly recognized: severe downturns on the HOSE often precipitate widespread retail margin calls, driving synchronized liquidations across large-cap and mid-cap equities. This bidirectional selling pressure partially weakens the exogeneity condition, so the adjusted correlation should be interpreted as cross-tier dependence under liquidity-constrained stress rather than as purely unidirectional shock transmission from large caps to mid-caps.

The formal hypothesis test is evaluated as follows:

$H0 :ρ*≤ρlow$ versus $H1:ρ*>ρlow$ using the two-sample asymptotic standard error:

$SE(ρ*-ρlow)=(1-(ρ*)2)2Ncrisis+(1-ρlow2)2Ncalm,$

and test statistic $t=ρ*-ρlowSE(ρ*-ρlow)$.

## 2.5 Log-Linear Scale Regressions and the Epps Effect

To evaluate how cross-correlation scales with the investment horizon, we regress the DCCA coefficient of each index pair at each trading frequency on the logarithm of the timescale; the slope coefficient is the multiscale scaling slope:

$ρi,j,f(s)=αscale,i,j,f+βscale,i,j,fln(s)+εi,j,f(s),$

with the timescale evaluated on 30 logarithmically spaced points between 5 bars and one quarter of the sample length (5 to 5,485 bars at M30); Section 3.8.1 re-estimates the regression below the reliability threshold of Section 3.3. Because DCCA coefficients at adjacent timescales share overlapping data, the regression errors are positively autocorrelated and classical OLS standard errors are biased downward. We therefore use Newey and West (1987) heteroskedasticity- and autocorrelation-consistent (HAC) standard errors with a lag truncation of three, the value given by the standard data-dependent rule for 30 observations.

We also account for the Epps (1979) effect: at high frequencies (M30, H1), non-synchronous transactions between liquid VN30 large caps and less liquid mid-caps depress the correlation at small timescales (roughly ten bars or fewer). As the timescale increases, aggregation synchronizes price discovery, producing a positive scaling slope that reflects the fading of microstructure frictions combined with gradual information diffusion (Hong and Stein 1999).

## 2.6 The MF-DCCA Extension

To capture multifractal heterogeneity across fluctuation magnitudes, we implement the MF-DCCA of Zhou (2008) with the absolute-value operator (Oświęcimka et al. 2014), incorporating bivariate moving-average formalisms (Jiang and Zhou 2011). The q-th order fluctuation function is:

$Fq(s)≡12Nsν=12NsfDCCA2(s,ν)q/21/q, q∈[-5,5]\{0}.$

Because q = 0 is excluded from the grid, no logarithmic limit is required; segments with zero local covariance are discarded. The generalized cross-correlation exponent h(q) is the slope of the log fluctuation function against the log timescale over 24 logarithmically spaced scales. Through the Legendre transform, the singularity strength α and the spectrum f(α) are:

$α=h(q)+qh'(q), f(α)=q(α-h(q))+1.$

The multifractal spectrum width, the difference between the exponents at the smallest and largest q, quantifies the degree of multifractal complexity and sensitivity to market shocks.

# 3 Results

## 3.1 Summary Statistics

Table 1 presents the descriptive statistics for the index log returns across the four trading frequencies (2014–2025).

Table 1 Descriptive statistics of log returns at the four trading frequencies

| Index | Freq. | N | Mean | Std. Dev. | Skew. | Kurt. | Jarque–Bera |

| VN30 | Daily | 2,963 | 0.0004 | 0.0121 | −0.83 | 7.81 | 3,202*** |

| VN30 | M30 | 21,942 | 0.0001 | 0.0039 | −1.62 | 36.16 | 1,014,769*** |

| VN30 | H1 | 13,523 | 0.0001 | 0.0051 | −1.33 | 18.20 | 134,167*** |

| VN30 | H4 | 5,410 | 0.0001 | 0.0084 | −1.17 | 11.23 | 16,490*** |

| VN100 | Daily | 2,963 | 0.0004 | 0.0119 | −0.96 | 8.21 | 3,804*** |

| VN100 | M30 | 21,942 | 0.0000 | 0.0038 | −1.83 | 37.63 | 1,108,959*** |

| VN100 | H1 | 13,523 | 0.0001 | 0.0050 | −1.50 | 19.36 | 155,896*** |

| VN100 | H4 | 5,410 | 0.0002 | 0.0082 | −1.30 | 11.76 | 18,833*** |

| VNINDEX | Daily | 2,963 | 0.0004 | 0.0115 | −0.98 | 8.27 | 3,898*** |

| VNINDEX | M30 | 21,942 | 0.0000 | 0.0037 | −2.04 | 40.64 | 1,310,762*** |

| VNINDEX | H1 | 13,523 | 0.0001 | 0.0049 | −1.56 | 19.54 | 159,748*** |

| VNINDEX | H4 | 5,410 | 0.0002 | 0.0080 | −1.31 | 11.99 | 19,767*** |

| Pcap | Daily | 2,963 | 0.0004 | 0.0124 | −1.07 | 8.15 | 3,837*** |

| Pcap | M30 | 21,942 | 0.0000 | 0.0041 | −1.87 | 33.94 | 887,934*** |

| Pcap | H1 | 13,523 | 0.0001 | 0.0052 | −1.51 | 18.81 | 145,968*** |

| Pcap | H4 | 5,410 | 0.0002 | 0.0086 | −1.33 | 11.69 | 18,632*** |

Notes: Kurt. is non-excess kurtosis; Pcap is the mid-cap proxy of Section 2.2. *** p < 0.01 (Jarque–Bera). Source: Authors’ calculations based on HOSE index data (TradingView).

At the daily frequency, standard deviations are highest for Pcap (0.0124) and VN30 (0.0121) and lowest for VNINDEX (0.0115), consistent with the diversification of the broad index. Across intraday intervals, the standard deviation increases with bar length. All series are negatively skewed, and the Jarque–Bera statistics rise from 3,202–3,898 at 1D to 887,934–1,310,762 at M30, driven by extreme kurtosis (above 33 at M30). This pronounced leptokurtosis supports the use of DCCA and MF-DCCA, which do not rely on Gaussian assumptions.

## 3.2 Average Cross-Correlation Across Trading Frequencies

Table 2 presents the average DCCA cross-correlation coefficients across trading frequencies, allowing cross-index dependence to be compared across temporal horizons and constituent structures.

Table 2 Average DCCA cross-correlation by trading frequency

| Trading frequency | Nested group | Pcap–VN30 | Gap | N |

| Panel A: Synchronized Common Baseline Window (2017–2024) |

| 1D (Daily) | 0.980 | 0.890 | 0.090 | 1,983 |

| M30 (30-Minute) | 0.979 | 0.890 | 0.089 | 19,463 |

| H1 (1-Hour) | 0.979 | 0.891 | 0.089 | 9,879 |

| H4 (4-Hour) | 0.980 | 0.892 | 0.089 | 3,953 |

| Panel B: Full Historical Depth Sample (2014–2025) |

| 1D (Daily) | 0.977 | 0.884 | 0.093 | 2,963 |

| M30 (30-Minute) | 0.979 | 0.883 | 0.096 | 21,942 |

| H1 (1-Hour) | 0.975 | 0.889 | 0.086 | 13,523 |

| H4 (4-Hour) | 0.976 | 0.890 | 0.087 | 5,410 |

Notes: Averages of ρDCCA(s) over s ≤ srel (Table 3), m = 1. The nested group is the mean of VN30–VNINDEX, VN30–VN100 and VN100–VNINDEX. Source: Authors’ calculations.

Across both samples, the original nested group maintains an average correlation of 0.975–0.980 at every frequency. In contrast, Pcap–VN30 produces a markedly lower correlation of 0.883–0.892, a consistent gap of 0.086–0.096 correlation points. Averages in the synchronized window (Panel A) and the full sample (Panel B) differ by at most 0.007 for every series, so the unequal calendar coverage of the four frequencies does not drive the results.

Figure 2 plots the multiscale DCCA trajectories across all four trading frequencies, directly contrasting the purged mid-cap proxy with the nested index pairs.

[FIGURE]

Fig. 2 Multiscale DCCA cross-correlation curves for the nested pairs and Pcap–VN30: (a) 1D, (b) M30, (c) H1, (d) H4

Notes: Line and marker types identify the pairs (legend); vertical dotted lines mark the reliability thresholds srel (Table 3). Source: Authors’ calculations based on HOSE index data (TradingView).

## 3.3 Finite-Sample Reliability Thresholds

Because the number of segments shrinks as the timescale grows, the DCCA coefficient becomes unreliable at large timescales. For each sample size, we simulate pairs of Gaussian white-noise series with known correlations of −0.3, 0, 0.3, 0.5, 0.7 and 0.9 (167 replications each, 1,002 per frequency) and compute the mean absolute estimation error on 40 log-spaced scales. The reliability threshold is the largest scale below the first scale at which the worst-case error exceeds 0.05. Table 3 reports the thresholds.

Table 3 Finite-sample reliability thresholds by trading frequency

| Trading frequency | Sample size (N) | Maximum reliable scale (srel) |

| 1D (Daily) | 2,963 | 50 |

| M30 (30-Minute) | 21,942 | 444 |

| H1 (1-Hour) | 13,523 | 233 |

| H4 (4-Hour) | 5,410 | 88 |

Notes: Worst-case mean absolute error below 0.05 in 1,002 white-noise simulations per frequency. Source: Authors’ calculations.

The estimates are insensitive to the detrending order: for VN30–VNINDEX at the daily frequency, the mean reliable-range correlation is 0.9665, 0.9663 and 0.9667 for m = 1, 2 and 3. The statistical proxies (Pheur, Pratio, Pres) produce average DCCA correlations with VN30 between −0.16 and 0.07, confirming that they are residual artifacts, whereas Pcap correlates with them at only 0.277–0.486, indicating that it captures a distinct mid-cap signal.

## 3.4 Multifractal Structure

The generalized Hurst exponent at the second order, h(2), lies within 0.527–0.544 for all series and frequencies, indicating weak positive persistence. However, the multifractal spectrum width, the difference between the exponents at q = −5 and q = 5, reveals substantive heterogeneity across pairs. For the nested index pairs, the width spans 0.252–0.431. For the purged capitalization proxy, it reaches 0.435–0.656 and is the largest of all pairs at every frequency, indicating richer nonlinear cross-correlation structure than in the mechanically bound nested pairs. The statistical residual proxies produce widths of 0.211–0.494 that vary erratically across frequencies, consistent with amplified noise.

Figure 3 contrasts the multifractal spectra and generalized exponents of the purged mid-cap proxy with those of the nested pairs at the daily frequency.

[FIGURE]

Fig. 3 MF-DCCA at the daily frequency: (a) singularity spectra f(α); (b) generalized exponents hxy(q)

Notes: q ∈ [−5, 5]\{0}. Source: Authors’ calculations based on HOSE index data (TradingView).

## 3.5 Volatility Regimes and the Forbes–Rigobon Adjustment

Table 4 presents the unadjusted and Forbes–Rigobon conditioned correlations to assess whether the observed surge in co-movement during market turmoil reflects genuine economic interdependence or volatility expansion. Regime correlations are DCCA coefficients at a 20-day horizon estimated on the concatenated calm and turbulent subsamples of daily returns.

Table 4 Cross-correlation across volatility regimes and Forbes–Rigobon conditioning

| Asset pair | ρlow | ρhigh | δ | ρ* | Asymp. SE | t-stat | p-value |

| Panel A: Chronological Crisis |

| Pcap–VN30 | 0.844 | 0.924 | 2.21 | 0.803 | 0.018 | −2.28 | 0.989 |

| Panel B: 20-Day Rolling Regimes |

| Pcap–VN30 | 0.633 | 0.929 | 7.06 | 0.663 | 0.030 | 0.97 | 0.165 |

Notes: DCCA correlations at s ≈ 20 days; δ is the relative increase in VN30 return variance; one-sided test of H0: ρ* ≤ ρlow. Ncalm/Ncrisis = 1,000/539 (Panel A) and 739/739 (Panel B). Source: Authors’ calculations.

The formal test in Table 4 is restricted to the disjoint pair Pcap–VN30. Because nested pairs embed the conditioning asset in the dependent series, constituent overlap creates an endogenous feedback loop that violates the exogeneity condition of Forbes and Rigobon (2002). For diagnostic comparison only, raw correlations for the nested pairs rise from 0.955–0.983 in calm periods to 0.980–0.992 in crisis episodes, and from 0.923–0.962 to 0.982–0.992 across rolling-volatility regimes.

In Panel A, regimes correspond to the three prolonged crisis episodes. Raw cross-tier correlation rises from 0.844 in calm years to 0.924 during crises, while the variance of VN30 returns increases by 221% (δ = 2.21). Once this volatility expansion is accounted for, the adjusted crisis correlation falls to 0.803, below its calm level, so the null hypothesis of no structural increase cannot be rejected (t = −2.28, p = 0.989). The tighter co-movement during systemic stress is thus consistent with an unchanged transmission structure operating under higher volatility, the interdependence interpretation of Forbes and Rigobon (2002). Liquidity constraints and delayed price adjustment in retail-dominated trading (Tran and Tran 2025) offer a plausible channel through which volatility spreads across capitalization tiers without altering their underlying linkage.

Panel B sorts days by the rolling 20-day volatility of VNINDEX, isolating extreme volatility clustering and producing a much larger variance expansion (δ = 7.06, a 606% increase). The raw correlation rises from 0.633 to 0.929 (+0.296 points), but the volatility adjustment (a factor of 1.402) pulls the adjusted correlation down to 0.663, only 0.030 above the calm level (t = 0.97, p = 0.165). Both definitions therefore reach the same conclusion: the apparent surge in large-cap/mid-cap correlation is a volatility effect rather than evidence of contagion. The rolling definition exaggerates the raw tightening because its low-volatility days are drawn from the quietest, least correlated intervals.

## 3.6 Markowitz Portfolio Variance Implications

Under the Markowitz (1952) mean-variance framework, the variance of a two-asset portfolio with arbitrary asset volatilities is:

$σport2=w12σ12+w22σ22+2w1w2σ1σ2ρ.$

When an investor applies a static full-sample correlation $ρstatic$ instead of a regime-specific correlation $ρregime$, the relative percentage error in portfolio variance for an equally weighted portfolio ($w1=w2=0.5$) is:

$Relative Error (RE)=σport2(ρstatic)-σport2(ρregime)σport2(ρregime)=ρstatic-ρregime12σ1σ2+σ2σ1+ρregime.$

When the two assets have equal volatility, the volatility term in the denominator equals one. In the daily data (Table 1), the volatilities of Pcap (0.0124) and VN30 (0.0121) are so close that the term equals 1.0002, changing the denominator by only 0.02%; all reported figures nevertheless use the exact expression. Evaluating this relative variance error across regimes reveals a sharp distinction between tradable cash portfolios and underlying factor exposures.

For cash portfolios formed from parent and child indices (such as VN30–VN100), co-movement is dominated by constituent overlap. At the daily frequency, the static correlation of 0.988 compares with regime correlations of 0.962 and 0.992 under the rolling definition, so the static model overstates portfolio variance by 1.32% in the calm regime and understates it by 0.19% in the turbulent regime. Across all frequencies and parent–child pairs, the largest absolute error is 2.73% (VN30–VNINDEX, calm regime, H4), which is negligible for operational risk management.

Conversely, for the mid-cap factor exposure (Pcap), static correlation models produce substantial distortion. Under the rolling definition, the calm-regime correlation is 0.633, whereas the full-sample static correlation is 0.889, so the static model overstates portfolio variance by 15.63%; under the chronological definition, where the calm correlation is 0.844, the overstatement is +2.44%. An allocator relying on static metrics therefore perceives the mid-cap allocation as riskier than it is during tranquil periods, which leads to excessive risk-capital provisioning and inefficient hedging allocations.

In the turbulent regime, the static model understates portfolio variance by 2.10% under the rolling definition and by 1.83% under the chronological definition. Although these errors appear modest, they arise when the variance of the underlying assets has risen by 221% to 606% (Table 4). Because the crisis correlation increase is explained by volatility (Section 3.5), risk budgets should be conditioned on the volatility regime rather than on a single static correlation.

## 3.7 Multiscale Scaling and Economic Mechanisms

Table 5 presents the log-linear scaling regressions of DCCA coefficients at the M30 frequency, whose scale grid spans the widest range of horizons, to quantify the sensitivity of cross-asset co-movement to the investment horizon.

Table 5 Log-linear scaling regressions of DCCA coefficients (M30)

| Pair | Intercept (αscale) | Slope (βscale) | HAC SE | p-value | R2 | Scales (N) |

| VN30–VNINDEX | 0.9625*** | 0.0016*** | 0.0004 | <0.001 | 0.486 | 30 |

| VN100–VNINDEX | 0.9775*** | 0.0009** | 0.0004 | 0.038 | 0.298 | 30 |

| VN30–VN100 | 0.9865*** | 0.0001 | 0.0002 | 0.636 | 0.020 | 30 |

| Pcap–VN30 | 0.8731*** | 0.0025*** | 0.0009 | 0.009 | 0.274 | 30 |

| Pheur–VN30 | −0.0846* | 0.0222* | 0.0112 | 0.058 | 0.293 | 30 |

| Pratio–VN30 | −0.1669*** | 0.0221* | 0.0120 | 0.076 | 0.268 | 30 |

| Pres–VN30 | −0.0117 | 0.0220** | 0.0104 | 0.043 | 0.317 | 30 |

Notes: 30 log-spaced scales (5 ≤ s ≤ 5,485); Newey–West HAC standard errors (3 lags). *** p < 0.01, ** p < 0.05, * p < 0.10. Source: Authors’ calculations.

The regression results reveal a pronounced structural asymmetry between nested and disjoint index pairs:

First, for the fully nested pair VN30–VN100, the slope is statistically indistinguishable from zero (0.0001, p = 0.636): because VN30 constituents dominate VN100 capitalization, their mechanical co-movement is invariant to the timescale.

Second, pairs that contain a genuine cross-tier component exhibit significantly positive slopes: VN30–VNINDEX (0.0016, p < 0.001), VN100–VNINDEX (0.0009, p = 0.038) and Pcap–VN30 (0.0025, p = 0.009). As the timescale expands from 30 minutes to multiple trading days, cross-correlation increases systematically. The effect is specific to intraday data: at the daily frequency, the Pcap–VN30 slope is insignificant (0.0014, p = 0.47), whereas VN30–VNINDEX remains significant (0.0020, p < 0.001).

Third, for the statistical residual proxies (Pheur, Pratio, Pres), the slopes are larger (0.0220–0.0222) but imprecise (p = 0.043–0.076). Because the underlying residual retains short-horizon asynchronous noise, detrending over larger timescales averages out bid–ask bounce and tick mismatch, so the residual covariance with VN30 drifts from negative intraday values toward zero.

Economic Mechanisms and Identification Boundaries:

This positive scaling behavior is consistent with the joint operation of two complementary economic mechanisms. First, under the Epps (1979) microstructure effect, non-synchronous trades and quote staleness in less liquid mid-cap constituents dampen cross-correlations at ultra-short intraday intervals (fewer than about ten bars). As holding periods lengthen, temporal aggregation synchronizes price discovery across stocks. Second, gradual information diffusion (Hong and Stein 1999) implies horizon-dependent co-movement because institutional investors and market makers trade predominantly in liquid VN30 large caps: market-wide news is reflected immediately in VN30 valuations but diffuses gradually into mid-cap stocks over several trading hours.

A critical identification boundary arises here. Although microstructure frictions (Epps 1979) and gradual information diffusion (Hong and Stein 1999) both imply correlations that rise with the timescale, the two mechanisms are observationally equivalent in index-level closing data. Disentangling transaction delays from cross-firm information diffusion would require tick-by-tick order-book data and firm-level news timestamps, which lie beyond the scope of this study.

## 3.8 Robustness Checks

## 3.8.1 Full-Range versus Reliable-Range Stability

Table 6 compares the scaling slopes estimated over the full scale range with those estimated only over the reliable range (timescales up to 444 bars at M30).

Table 6 Full-range versus reliable-range scaling slopes (M30)

| Asset Pair | Full-range Slope (N = 30) | Reliable-range Slope (N = 19) | Stability Assessment |

| VN30–VNINDEX | 0.0016*** (0.0004) | 0.0022*** (0.0005) | Stable |

| VN100–VNINDEX | 0.0009** (0.0004) | 0.0022*** (0.0004) | Stable |

| VN30–VN100 | 0.0001 (0.0002) | −0.0001 (0.0001) | Flat |

| Pcap–VN30 | 0.0025*** (0.0009) | 0.0017 (0.0010) | Weakens |

| Pheur–VN30 | 0.0222* (0.0112) | 0.0289*** (0.0052) | Strengthens |

| Pratio–VN30 | 0.0221* (0.0120) | 0.0291*** (0.0050) | Strengthens |

| Pres–VN30 | 0.0220** (0.0104) | 0.0283*** (0.0054) | Stable |

Notes: HAC standard errors in parentheses. *** p < 0.01, ** p < 0.05, * p < 0.10. Source: Authors’ calculations.

The positive slopes of VN30–VNINDEX and VN100–VNINDEX strengthen in the reliable range (0.0022, p < 0.001 for both), and VN30–VN100 remains flat. For Pcap–VN30, the reliable-range slope keeps its positive sign (0.0017) but is less precisely estimated (p = 0.102). The horizon dependence of purged mid-cap co-movement is therefore robust in sign but relies partly on the longer, noisier scales, and we interpret it as suggestive; the multiscale evidence for the broad-market pairs is robust.

## 3.8.2 Sensitivity of Pcap to the Capitalization Weight

Because constituent capitalizations drift with relative price movements and periodic rebalancing, Table 7 re-estimates the key Pcap statistics for large-cap weights from 0.60 to 0.75.

Table 7 Sensitivity of Pcap to the capitalization weight w30

| Weight (w30) | Mean ρDCCA (1D) | Slope βscale (M30) | Calm ρlow | Crisis ρhigh |

| 0.6000 | 0.924 | 0.0014* | 0.897 | 0.951 |

| 0.6500 | 0.903 | 0.0019** | 0.869 | 0.936 |

| 0.6826 (baseline) | 0.884 | 0.0025*** | 0.844 | 0.924 |

| 0.7200 | 0.855 | 0.0033*** | 0.806 | 0.904 |

| 0.7500 | 0.824 | 0.0043*** | 0.767 | 0.883 |

Notes: ρlow and ρhigh use the chronological regimes (Table 4, Panel A). *** p < 0.01, ** p < 0.05, * p < 0.10. Source: Authors’ calculations.

Table 7 shows that a higher large-cap weight removes more of the VN30 component and therefore lowers the Pcap–VN30 correlation (from 0.924 at a weight of 0.60 to 0.824 at 0.75). The central conclusions are nevertheless invariant: in every specification, the Pcap correlation remains at least 0.052 below the 0.977 average of the nested daily pairs, the M30 scaling slope remains positive (significant at the 5% level for weights of at least 0.65 and at the 10% level for 0.60), and raw crisis tightening (0.053–0.117) remains modest relative to the accompanying volatility expansion.

# 4 Discussion and Conclusion

This study econometrically examines multiscale cross-correlation dynamics and constituent overlap distortion among nested equity benchmarks in Vietnam. By deploying detrended cross-correlation analysis and its multifractal extension across intraday and daily trading horizons, the mechanical influence of shared capitalization is disentangled from genuine economic co-movement.

The empirical analysis provides three core insights:

First, conventional index pairs that embed large-cap constituents within broader benchmarks exhibit elevated cross-correlations attributable predominantly to index engineering rather than economic integration. Purging shared constituent capitalization through a market-weighted proxy uncovers a baseline co-movement about 0.09 correlation points lower. At intraday frequencies, cross-tier co-movement tends to be horizon-dependent: short-scale correlations are dampened by microstructure frictions and asynchronous quoting, while longer-horizon correlations strengthen as market-wide news diffuses across liquidity tiers.

Second, volatility conditioning shows that the tightening of cross-tier co-movement during market turmoil is explained by volatility expansion rather than by a structural break in the large-cap/mid-cap linkage. Systemic stress raises volatility across capitalization tiers, so diversification benefits shrink precisely when they are most needed even though the underlying dependence structure is stable.

Third, while cash portfolios composed of nested parent–child indices experience negligible variance misstatement, unadjusted static models materially misstate risk for mid-cap factor exposures. In calm market environments, conventional models overstate mid-cap portfolio variance by up to 15.6%, leading to inefficient hedging capital allocations; during market crises, they understate portfolio variance when volatility itself has multiplied.

## 4.1 Implications for ASEAN Capital Markets

These findings carry concrete implications for institutional investors, index providers, and regulatory authorities across Southeast Asia.

For institutional portfolio management, asset allocators operating in ASEAN markets (such as Malaysian institutional funds, regional pension managers, and private wealth allocators) must recognize that blending large-cap and broad-market parent-child indices offers negligible diversification benefits. When constructing multi-capitalization strategies, risk managers should replace static correlation assumptions with volatility-regime-conditioned covariance frameworks that recognize both overstated risk in tranquil periods and elevated co-movement during market distress.

Regarding index architecture and product innovation, stock exchanges and index providers across emerging Southeast Asian markets should prioritize the development and promotion of standalone, non-overlapping segment benchmarks. On the Ho Chi Minh City Stock Exchange, listing dedicated mid-cap exchange-traded funds based on standalone benchmarks such as VNMIDCAP (VN70) provides transparent building blocks for institutional factor allocation, helping allocators avoid the hidden overlaps inherent in headline index blends.

Finally, for market development and risk mitigation, expanding derivative product suites beyond large-cap index futures to include mid-cap and sector contracts would substantially enhance market completeness. Providing tradeable hedging instruments across multiple capitalization tiers enables institutional investors to manage cross-tier exposure without destabilizing underlying cash equity positions during periods of market stress.

## 4.2 Limitations and Future Research

This study has limitations that suggest directions for future research. First, the mid-cap segment is identified through a capitalization-weighted decomposition based on a single factsheet snapshot of free-float weights. Although Section 3.8.2 shows that the conclusions are robust to weights between 0.60 and 0.75, validating the proxy against the exchange-published VNMIDCAP (VN70) index at all four frequencies, and reconstructing the historical VN30 weight from semi-annual constituent reviews, would sharpen identification.

Second, index-level closing prices cannot separate microstructure frictions (Epps 1979) from gradual information diffusion (Hong and Stein 1999); constituent-level tick data and order-book depth would allow these channels to be disentangled. Third, the Forbes and Rigobon (2002) adjustment assumes exogenous large-cap shocks, an assumption that forced deleveraging may weaken; regime-switching or heteroskedasticity-based identification could provide complementary evidence. Finally, applying the framework to the nested index systems of Malaysia, Thailand and Indonesia, whose short-selling and settlement rules differ from Vietnam’s, would test the institutional hypothesis that trading restrictions shape multiscale price synchronization.

Ethical standards This study uses only publicly available historical index price data from the Ho Chi Minh City Stock Exchange; it involves no human participants or personal data, therefore required no ethical approval, and complies with the current laws of Vietnam.

Data availability The index price data were obtained from TradingView (exchange: HOSE) and are subject to the vendor’s terms of use; the merged dataset is available from the corresponding author upon reasonable request.

Code availability The R code that reproduces every table and figure is available from the corresponding author upon request.

Conflict of interest The authors declare that they have no conflict of interest.

Declaration of generative AI use During the preparation of this work, the authors used an AI assistant (Claude, Anthropic) for language editing, reference verification and translation of the analysis code into R. The authors reviewed all content and take full responsibility for the publication.

# References

Al Rababa’a, A. R., Alomari, M., & McMillan, D. (2021). Multiscale stock-bond correlation: Implications for risk management. Research in International Business and Finance, 58, 101435. https://doi.org/10.1016/j.ribaf.2021.101435

Ang, A., & Chen, J. (2002). Asymmetric correlations of equity portfolios. Journal of Financial Economics, 63(3), 443–494. https://doi.org/10.1016/S0304-405X(02)00068-5

Aslam, F., Ferreira, P., Ali, H., Arifa, & Oliveira, M. (2023). Islamic vs. conventional equity markets: A multifractal cross-correlation analysis with economic policy uncertainty. Economies, 11(1), 16. https://doi.org/10.3390/economies11010016

Chen, Y., Zhang, J., Lu, L., & Xie, Z. (2024). Cross-correlation and multifractality analysis of the Chinese and American stock markets based on the MF-DCCA model. Heliyon, 10(15), e36537. https://doi.org/10.1016/j.heliyon.2024.e36537

Epps, T. W. (1979). Comovements in stock prices in the very short run. Journal of the American Statistical Association, 74(366), 291–298. https://doi.org/10.1080/01621459.1979.10482508

Forbes, K. J., & Rigobon, R. (2002). No contagion, only interdependence: Measuring stock market comovements. The Journal of Finance, 57(5), 2223–2261. https://doi.org/10.1111/0022-1082.00494

Hong, H., & Stein, J. C. (1999). A unified theory of underreaction, momentum trading, and overreaction in asset markets. The Journal of Finance, 54(6), 2143–2184. https://doi.org/10.1111/0022-1082.00184

Jiang, Z.-Q., & Zhou, W.-X. (2011). Multifractal detrending moving-average cross-correlation analysis. Physical Review E, 84(1), 016106. https://doi.org/10.1103/PhysRevE.84.016106

Kantelhardt, J. W., Zschiegner, S. A., Koscielny-Bunde, E., Havlin, S., Bunde, A., & Stanley, H. E. (2002). Multifractal detrended fluctuation analysis of nonstationary time series. Physica A: Statistical Mechanics and its Applications, 316(1–4), 87–114. https://doi.org/10.1016/S0378-4371(02)01383-3

Karim, B. A., & Ning, H. X. (2013). Driving forces of the ASEAN-5 stock markets integration. Asia-Pacific Journal of Business Administration, 5(3), 186–191. https://doi.org/10.1108/APJBA-07-2012-0053

Le, T. T. V., Dang, T. P. T., & Phan, T. H. N. (2025). The nonlinear dependence of the Vietnam stock market on the Asian stock market: Evidence from a quantile-on-quantile regression. International Journal of Innovative Research and Scientific Studies, 8(4), 7901–7914. https://doi.org/10.53894/ijirss.v8i4.7901

Lean, H. H., & Teng, K. T. (2013). Integration of world leaders and emerging powers into the Malaysian stock market: A DCC-MGARCH approach. Economic Modelling, 32, 333–342. https://doi.org/10.1016/j.econmod.2013.02.013

Longin, F., & Solnik, B. (2001). Extreme correlation of international equity markets. The Journal of Finance, 56(2), 649–676. https://doi.org/10.1111/0022-1082.00340

Markowitz, H. (1952). Portfolio selection. The Journal of Finance, 7(1), 77–91. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x

Michis, A. A. (2022). Multiscale partial correlation clustering of stock market returns. Journal of Risk and Financial Management, 15(1), 24. https://doi.org/10.3390/jrfm15010024

Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica, 55(3), 703–708. https://doi.org/10.2307/1913610

Oświęcimka, P., Drożdż, S., Forczek, M., Jadach, S., & Kwapień, J. (2014). Detrended cross-correlation analysis consistently extended to multifractality. Physical Review E, 89(2), 022805. https://doi.org/10.1103/PhysRevE.89.022805

Peng, C.-K., Buldyrev, S. V., Havlin, S., Simons, M., Stanley, H. E., & Goldberger, A. L. (1994). Mosaic organization of DNA nucleotides. Physical Review E, 49(2), 1685–1689. https://doi.org/10.1103/PhysRevE.49.1685

Podobnik, B., & Stanley, H. E. (2008). Detrended cross-correlation analysis: A new method for analyzing two nonstationary time series. Physical Review Letters, 100(8), 084102. https://doi.org/10.1103/PhysRevLett.100.084102

Podobnik, B., Jiang, Z.-Q., Zhou, W.-X., & Stanley, H. E. (2011). Statistical tests for power-law cross-correlated processes. Physical Review E, 84(6), 066118. https://doi.org/10.1103/PhysRevE.84.066118

Rodriguez, E., & Alvarez-Ramirez, J. (2021). Time-varying cross-correlation between trading volume and returns in US stock markets. Physica A: Statistical Mechanics and its Applications, 581, 126211. https://doi.org/10.1016/j.physa.2021.126211

Tran, M. H., & Tran, N. M. (2025). High-frequency dynamics of the Vietnam stock market. VNU Journal of Economics and Business, 5(2), 51–59. https://doi.org/10.57110/vnu-jeb.v5i2.395

Zebende, G. F. (2011). DCCA cross-correlation coefficient: Quantifying level of cross-correlation. Physica A: Statistical Mechanics and its Applications, 390(4), 614–618. https://doi.org/10.1016/j.physa.2010.10.022

Zhou, W.-X. (2008). Multifractal detrended cross-correlation analysis for two nonstationary signals. Physical Review E, 77(6), 066211. https://doi.org/10.1103/PhysRevE.77.066211

Zhou, W., Huang, J., & Wang, M. (2025). Multifractal characteristics and information flow analysis of stock markets based on multifractal detrended cross-correlation analysis and transfer entropy. Fractal and Fractional, 9(1), 14. https://doi.org/10.3390/fractalfract9010014