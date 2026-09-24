import copy, csv, os, re, shutil, sys
from lxml import etree
sys.path.insert(0, os.path.dirname(__file__))
from lib_docx import *

S = os.path.dirname(os.path.abspath(__file__))
OUT = '/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/outputs'
src, dst = S + '/clean', S + '/final'
if os.path.exists(dst): shutil.rmtree(dst)
shutil.copytree(src, dst)
tree = etree.parse(dst + '/word/document.xml'); root = tree.getroot(); body = root.find(W + 'body')
P = [None] + list(body.iter(W + 'p'))          # 1-based, matches the audit enumeration
T = [None] + [c for c in body if c.tag == W + 'tbl']

def rd(f): return list(csv.DictReader(open(os.path.join(OUT, f))))
def f(x, d): return f'{float(x):.{d}f}'.replace('-', '−')
def star(p):
    p = float(p); return '***' if p < .01 else '**' if p < .05 else '*' if p < .10 else ''
def pv(p):
    p = float(p); return '<0.001' if p < .001 else f'{p:.3f}'

# sanity: the paragraphs we address must be what we think they are
expect = {1: 'Nested Equity', 2: 'Abstract', 29: '2. Data', 30: '2.1 Institutional', 40: '2.2 Data', 56: '', 121: '3. Nested',
          380: '3.3 Finite', 464: '4. Statistical', 538: '5. Correlation', 632: '6. Independent', 655: 'References'}
for k, v in expect.items():
    assert text_of(P[k]).strip().startswith(v), (k, text_of(P[k])[:40])

H1, H2 = P[5], P[58]   # heading templates (heading1 / heading20)

# ================================================================= Abstract, contributions (Introduction)
set_text(P[2], "Asset allocators in emerging Southeast Asian markets frequently treat large-cap and broad-market indices as separate diversification instruments, even in nested architectures where large-cap stocks dominate the broader market. Standard risk models thereby conflate mechanical constituent overlap with genuine economic co-movement. Utilizing Detrended Cross-Correlation Analysis (DCCA) and its multifractal extension on 30-minute, 1-hour, 4-hour and daily data from the Ho Chi Minh City Stock Exchange (2014–2025), this study illustrates that near-perfect correlations among nested indices (0.975–0.980) primarily reflect shared capitalization rather than cross-tier interdependence. Purging constituent overlap with a capitalization-weighted mid-cap proxy lowers the correlation with large caps by 0.086–0.096. Furthermore, at intraday frequencies this co-movement tends to strengthen over longer holding horizons as microstructure frictions resolve and information diffuses throughout the market. Raw cross-tier correlation rises from 0.63 to 0.93 in high-volatility regimes, but Forbes–Rigobon volatility conditioning shows that the rise is explained by volatility expansion, indicating interdependence rather than contagion. Consequently, static models overstate mid-cap portfolio variance by up to 15.6% during calm market regimes and understate it during turbulent regimes. These research findings highlight the imperative for independent mid-cap benchmarks and volatility-regime-sensitive risk budgeting across the capital markets of the Association of Southeast Asian Nations (ASEAN).",
         bold_lead='Abstract: ')
replace_in(P[3], 'portfolio risk.', 'portfolio risk, Vietnam.')

replace_in(P[10], ' and more than half of the total market capitalization of HOSE', '')
replace_in(P[12], '( Jiang', '(Jiang'); replace_in(P[12], '( Al', '(Al')
replace_in(P[12], 'issue. ', 'issue.')
replace_in(P[14], ' documented shifting volume-return co-movements in US equities driven by index fund proliferation', ' documented time- and scale-varying volume–return cross-correlations in US equity markets')
replace_in(P[16], 'proved that unadjusted sample correlations are an increasing function of market volatility, demonstrating that observed correlation surge reflects mechanical volatility expansion rather than a genuine structural breakdown',
           'showed that unadjusted sample correlations increase mechanically with market volatility, so that an observed correlation surge may reflect volatility expansion rather than a structural change in cross-market linkages')
replace_in(P[16], 'depress short-horizon correlations to zero', 'depress short-horizon correlations')
set_text(P[18], "Regional studies show that financial integration across ASEAN equity markets is time-varying and shaped by trade linkages, market volatility and external shocks (Karim & Ning, 2013; Lean & Teng, 2013). While mature regional platforms such as Bursa Malaysia provide market-completeness mechanisms such as Regulated Short Selling (RSS) and Intraday Short Selling (IDSS) to facilitate continuous cross-tier arbitrage, Vietnam’s HOSE operates under strict statutory prohibitions on cash short selling. We frame this structural contrast as an institutional comparative hypothesis regarding how trading restrictions interact with multiscale price synchronization.")
set_text(P[20], "To address these unresolved issues, this study examines VN30, VN100 and VNINDEX from January 2014 to December 2025 at four trading frequencies: 30-minute (M30), 1-hour (H1), 4-hour (H4) and daily (1D). To isolate genuine economic linkage from constituent overlap, we construct a capitalization-weighted proxy (P_{cap}) that extracts the mid-cap component of VN100 using free-float market weights, and we benchmark it against three alternative statistical decompositions. In addition, we examine regime-dependent correlation shifts using the conditioning framework of Forbes and Rigobon (2002) and quantify the resulting misstatement in Markowitz portfolio variance.")
set_text(P[22], "This study makes three primary contributions to the extant empirical finance and risk management literature.")
set_text(P[24], "Firstly, we map the overlap distortion in nested benchmark systems. While headline large-cap and broad-market indices exhibit near-perfect cross-correlations (0.975–0.980) across intraday and daily intervals, this apparent co-movement falls by 0.086–0.096 correlation points once shared capitalization is extracted through a market-weighted mid-cap proxy. We further show that, at the 30-minute frequency, the purged cross-tier dependence tends to increase with the investment horizon (significantly over the full scale range and with the same sign over the reliable range), consistent with the resolution of intraday microstructure frictions and the gradual diffusion of market-wide information.")
set_text(P[26], "Secondly, we provide a volatility-conditioned evaluation of crisis dynamics. Raw cross-tier correlations tighten by up to 0.30 correlation points in high-volatility regimes, which would conventionally be read as a correlation breakdown. Applying the Forbes and Rigobon (2002) adjustment under two regime definitions, we show that the adjusted crisis correlation never significantly exceeds its calm-period level. Mid-cap diversification failure during Vietnamese market stress therefore reflects interdependence amplified by volatility rather than a structural change in cross-tier transmission.")
set_text(P[28], "Thirdly, we quantify the risk-management cost of static correlations. Cash portfolios formed from parent and child indices suffer variance misstatements of at most 2.7% because their constituents overlap, whereas for a dedicated mid-cap exposure a static correlation overstates portfolio variance by up to 15.6% in calm regimes and understates it by about 2% in turbulent regimes, when volatility itself has multiplied. Given the statutory prohibition on cash short selling in Vietnam, the synthetic mid-cap construct serves as a practical shadow benchmark for risk attribution, stress testing and index-product development.")
org = clone_after(P[28], "The remainder of the paper is organized as follows. Section 1.1 describes the current situation and institutional background of the HOSE. Section 2 presents the data and methods, Section 3 reports the results, including multiscale scaling and robustness checks, and Section 4 discusses the findings and concludes.")
clone_after(P[28], '', template=P[27])

# ================================================================= Section 2: current situation (moved out of Data & Methodology)
set_text(P[30], "1.1 Current Situation and Institutional Background of the HOSE", keep_tabs=True)
tab_r = copy.deepcopy([r for r in P[29].iter(W + 'r')][0]) if list(P[29].iter(W + 'tab')) else None
set_text(P[37], "In addition, each trading day opens and closes with a call auction: a 15-minute batch auction sets the opening price (ATO, 09:00–09:15) and another sets the closing price (ATC, 14:30–14:45), with continuous order matching in between. At the 30-minute frequency, the first bar of each day contains the opening auction and the last bar contains the closing auction, so these bars display higher volatility and less synchronous clearing than midday bars.")
set_text(P[39], "Finally, securities legislation, including Decree 155/2020/ND-CP and SSC Circular 120/2020/TT-BTC, prohibits cash short selling: investors may sell only securities already held in their accounts. Margin regulations require an initial margin of at least 50%, capping gross leverage at about 2.0×, and Circular 68/2024/TT-BTC, which removed the pre-funding requirement for foreign institutional investors, left the short-sale prohibition unchanged. Although VN30 index futures trade on the Hanoi Stock Exchange derivatives market, no exchange-traded hedging instrument exists for the mid-cap segment. The absence of cash short selling prevents arbitrageurs from trading the spread between large caps and mid-caps, which can prolong intraday non-synchronicity (the Epps effect) and delay price synchronization between VN30 and mid-cap stocks.")
# move "2. Data and Methodology" heading below the institutional section and renumber
h_data = P[29]; body.remove(h_data); P[40].addprevious(h_data)
set_text(h_data, "2 Methods", keep_tabs=True)

# ================================================================= Section 3 Data
def heading2(p, txt): set_text(p, txt, keep_tabs=True)
heading2(P[40], "2.1 Data and Sample Construction")
set_text(P[41], "The dataset comprises closing prices of three HOSE indices exported from TradingView (exchange: HOSE) for January 27, 2014, to December 12, 2025: the flagship VN30 index, comprising the 30 largest and most liquid stocks screened for free-float capitalization; the VN100 index, which combines the VN30 constituents with the next 70 largest liquid stocks (the constituents of the VNMIDCAP, or VN70, index); and the composite VNINDEX, which covers all common stocks listed on the HOSE. Because a VNMIDCAP price history is not available from our data source for the full sample and all frequencies, the mid-cap segment is recovered from VN100 and VN30 by the decomposition in Section 2.2.")
set_text(P[43], "The analysis evaluates four trading frequencies: 30-minute (M30), 1-hour (H1), 4-hour (H4) and daily (1D). To guarantee simultaneity and prevent alignment bias, the index series were synchronized by exact inner joins on timestamps, and log returns were computed as:")
replace_in(P[46], 'This sample formed', 'This sample forms')
set_text(P[48], "The second tier is the Extended Historical Depth Sample, deployed to maximize data depth for scaling regressions, regime tests and Monte Carlo reliability thresholds (1D: February 2014–December 2025, N = 2,963; M30: January 2017–December 2025, N = 21,942; H1 and H4: January 2014–December 2024, N = 13,523 and 5,410). The 1-hour and 4-hour series available from the data vendor end on December 9, 2024, whereas the daily and 30-minute series extend to December 12, 2025. All four frequencies overlap without any calendar gap in the first tier, which is used for cross-frequency comparisons.")
set_text(P[49], "To limit survivorship and look-ahead bias, the analysis relies on official index levels calculated in real time by the HOSE rather than on indices back-calculated from current constituent lists. The HOSE reviews index constituents semi-annually, updating memberships and free-float adjustments on the basis of capitalization, liquidity and foreign-ownership criteria. Because the price series are the exchange-computed index levels, historical constituent changes, corporate actions and rebalancing adjustments are embedded in the return paths.")
set_text(P[51], "Regime dependence is evaluated under two definitions based on the 20-day rolling standard deviation of VNINDEX returns (Fig. 1).")
set_text(P[53], "The first definition uses continuous chronological crisis episodes. To avoid arbitrary selection, an episode must satisfy three conditions: (i) a peak-to-trough VNINDEX drawdown of more than 25%; (ii) at least 45% of its trading days in the top quartile of the rolling-volatility distribution; and (iii) a documented macro-financial trigger. Three episodes qualify: the 2018 margin contraction (January–December 2018; drawdown 26.2%, 47% of days in the top quartile), the 2020 COVID-19 shock (January–June 2020; 33.5%, 52%) and the 2022 corporate bond liquidity freeze (April–November 2022; 40.2%, 60%), totaling 539 crisis trading days. The calm benchmark comprises 2016–2017 and 2023–2024 (1,000 trading days). Transient spikes, such as the May 2014 South China Sea standoff (drawdown 14.8%) and the April 2025 tariff shock (18.1%), fail conditions (i) and (ii). The second definition sorts all days by rolling volatility, classifying days below the 25th percentile (10.6% annualized) as low-volatility and days above the 75th percentile (20.0%) as high-volatility.")
set_text(P[55], "Figure 1 maps the rolling annualized volatility of the VNINDEX alongside the three crisis episodes and the two quartile thresholds.")
NOTE_T = P[379]   # a figure-notes paragraph used as template for new notes
fig1_note = clone_after(P[57], "Notes: Shaded areas mark the three crisis episodes; dashed and dotted lines mark the 25th and 75th percentiles. Source: Authors’ calculations based on HOSE index data (TradingView).", template=NOTE_T)

# ---- 3.2 DCCA
heading2(P[58], "2.2 The DCCA Cross-Correlation Coefficient")
replace_in(P[67], 'Equation (3)', 'the fluctuation function')
set_text(P[76], "Because VN30 is embedded within VN100, an auxiliary regression of VN100 returns on VN30 returns produces an R^{2} of 0.973–0.977 and a slope of 0.968–0.975 across the four frequencies (daily estimates shown):")
replace_math(P[77], '0.987', '0.971')
set_text(P[81], "where w_{30} = 0.6826 is the free-float market-capitalization weight of VN30 within VN100 computed from the HOSE factsheet of May 31, 2024 (VND 1,316,288 billion and VND 1,928,303 billion, respectively), implying a scaling factor of 3.151. Because the decomposition is applied to logarithmic rather than arithmetic returns, it carries a small Jensen-inequality term; at the daily frequency this term is 3.6 × 10^{−6} per day and, accumulated over the reliable daily horizons (up to 50 days), remains below 2.5% of the corresponding cumulative return variance, so its effect on the DCCA estimates is negligible.")
set_text(P[82], "For comparison, we examine a statistically calibrated proxy (P_{heur}) that replaces the capitalization weight with the volatility-scaled OLS slope:")
set_text(P[83], "P_{heur,t} = (R_{100,t} − w_{heur}R_{30,t}) / (1 − w_{heur}),   w_{heur} = β_{OLS}σ_{30}/σ_{100} = Corr(R_{30}, R_{100}).")
pp = P[83].find(W + 'pPr'); jc = pp.find(W + 'jc')
if jc is None: jc = etree.SubElement(pp, W + 'jc')
jc.set(W + 'val', 'center')
set_text(P[84], "Because the correlation between VN30 and VN100 returns approaches unity (0.9865–0.9885 across frequencies), the denominator collapses toward zero (0.0115–0.0135), amplifying the numerator by a factor of 74 to 87. P_{heur} therefore behaves as an amplified residual rather than an economic asset proxy: its daily standard deviation is 0.1576, compared with 0.0124 for P_{cap}. Statistical weights cannot substitute for capitalization weights in nested index systems.")
set_text(P[85], "Finally, we construct two baseline statistical proxies for completeness: the ratio-spread proxy (P_{ratio}), defined as the change in the log ratio of VN100 to VN30 and therefore equal to the VN100 return minus the VN30 return, and the orthogonal residual proxy (P_{res}), defined as the residual of the auxiliary regression above. The three statistical proxies are almost perfectly correlated with one another (0.980–0.997).")
set_text(P[86], "Because synthesizing P_{cap} requires a long position of 315% in VN100 and a short position of 215% in VN30, the proxy cannot be executed in cash portfolios under the short-sale prohibition. We therefore treat P_{cap} strictly as an analytical shadow benchmark that isolates inter-tier economic dependence for risk budgeting.")

# ---- 3.3 weights
heading2(P[87], "2.3 Rebalancing and Weight Dynamics")
replace_in(P[88], ' over an 11-year sample', ' over the 2014–2025 sample')
replace_in(P[88], 'The HOSE conducts formal semi-annual constituent reviews in January and July of each calendar year. ', 'The HOSE conducts semi-annual constituent reviews. ')
replace_math(P[89], '0.6825', '0.6826')
set_text(P[91], "which introduces a time-varying leakage of large-cap returns into the proxy, proportional to the gap between the true and the baseline weight. Because only one factsheet snapshot of free-float weights is available, we do not reconstruct the historical weight path; instead, Section 3.8.2 re-estimates the key statistics for weights between 0.60 and 0.75, a range that brackets plausible drift around the baseline.")
remove(P[92]); remove(P[93])

# ---- 3.4 Forbes-Rigobon
heading2(P[94], "2.4 The Forbes–Rigobon Volatility Conditioning Framework")
set_text(P[101], "The Forbes–Rigobon identifying assumptions require that the conditioning benchmark be exogenous, with no contemporaneous feedback from the dependent series. This condition is plausible for the disjoint pair P_{cap}–VN30, in which large-cap returns serve as the market benchmark and the purged mid-cap component shares no constituents with VN30. For nested pairs (VN30–VN100, VN30–VNINDEX and VN100–VNINDEX), the assumption is violated by construction because VN30 accounts for over two-thirds of VN100 capitalization, so conditioning formulas yield unidentified parameters. We therefore restrict the formal test of a structural correlation increase to the P_{cap}–VN30 pair.")
set_text(P[102], "The identification boundary of the Forbes–Rigobon framework during acute market stress is explicitly recognized: severe downturns on the HOSE often precipitate widespread retail margin calls, driving synchronized liquidations across large-cap and mid-cap equities. This bidirectional selling pressure partially weakens the exogeneity condition, so the adjusted correlation should be interpreted as cross-tier dependence under liquidity-constrained stress rather than as purely unidirectional shock transmission from large caps to mid-caps.")
for t in P[104].iter(W + 't'):
    if t.text: t.text = t.text.lstrip(); break

# ---- 3.5 scale regressions
heading2(P[107], "2.5 Log-Linear Scale Regressions and the Epps Effect")
set_text(P[110], "with the timescale evaluated on 30 logarithmically spaced points between 5 bars and one quarter of the sample length (5 to 5,485 bars at M30); Section 3.8.1 re-estimates the regression below the reliability threshold of Section 3.3. Because DCCA coefficients at adjacent timescales share overlapping data, the regression errors are positively autocorrelated and classical OLS standard errors are biased downward. We therefore use Newey and West (1987) heteroskedasticity- and autocorrelation-consistent (HAC) standard errors with a lag truncation of three, the value given by the standard data-dependent rule for 30 observations.")


set_text(P[98], "As market volatility rises from a calm to a crisis regime, the unadjusted correlation increases toward one purely because the variance of the conditioning market rises, even when the structural slope and residual variance remain constant.")
set_text(P[108], "To evaluate how cross-correlation scales with the investment horizon, we regress the DCCA coefficient of each index pair at each trading frequency on the logarithm of the timescale; the slope coefficient is the multiscale scaling slope:")
set_text(P[111], "We also account for the Epps (1979) effect: at high frequencies (M30, H1), non-synchronous transactions between liquid VN30 large caps and less liquid mid-caps depress the correlation at small timescales (roughly ten bars or fewer). As the timescale increases, aggregation synchronizes price discovery, producing a positive scaling slope that reflects the fading of microstructure frictions combined with gradual information diffusion (Hong and Stein 1999).")
set_text(P[113], "To capture multifractal heterogeneity across fluctuation magnitudes, we implement the MF-DCCA of Zhou (2008) with the absolute-value operator (Oświęcimka et al. 2014), incorporating bivariate moving-average formalisms (Jiang and Zhou 2011). The q-th order fluctuation function is:")
set_text(P[120], "The multifractal spectrum width, the difference between the exponents at the smallest and largest q, quantifies the degree of multifractal complexity and sensitivity to market shocks.")

# ---- 3.6 MF-DCCA
heading2(P[112], "2.6 The MF-DCCA Extension")
set_text(P[116], "Because q = 0 is excluded from the grid, no logarithmic limit is required; segments with zero local covariance are discarded. The generalized cross-correlation exponent h(q) is the slope of the log fluctuation function against the log timescale over 24 logarithmically spaced scales. Through the Legendre transform, the singularity strength α and the spectrum f(α) are:")
remove(P[117]); remove(P[118])

# ================================================================= Section 4 results
set_text(P[121], "3 Results", keep_tabs=True)
heading2(P[122], "3.1 Summary Statistics")
set_text(P[124], "Table 1: Descriptive Statistics for Log Returns Across the Four Trading Frequencies")
desc = rd('01_descriptive_stats.csv'); FRQ = {'1D': 'Daily', 'M30': 'M30', 'H1': 'H1', 'H4': 'H4'}
LAB = {'VN30': 'VN30', 'VN100': 'VN100', 'VNINDEX': 'VNINDEX', 'Pcap': 'P_{cap}'}
for k, d in enumerate(desc):
    r = k + 1
    vals = [LAB[d['index']], FRQ[d['freq']], f"{int(d['n']):,}", f(d['mean'], 4), f(d['median'], 4), f(d['sd'], 4),
            f(d['min'], 2), f(d['max'], 2), f(d['skew'], 2), f(d['kurtosis'], 2), f"{float(d['jb']):,.0f}***"]
    for c, v in enumerate(vals): set_cell(T[1], r, c, v)
for c in (7, 6, 4): delete_col(T[1], c)
set_text(P[312], "Notes: Kurt. is non-excess kurtosis; P_{cap} is the mid-cap proxy of Section 2.2. *** p < 0.01 (Jarque–Bera). Source: Authors’ calculations based on HOSE index data (TradingView).")
set_text(P[313], "At the daily frequency, standard deviations are highest for P_{cap} (0.0124) and VN30 (0.0121) and lowest for VNINDEX (0.0115), consistent with the diversification of the broad index. Across intraday intervals, the standard deviation increases with bar length. All series are negatively skewed, and the Jarque–Bera statistics rise from 3,202–3,898 at 1D to 887,934–1,310,762 at M30, driven by extreme kurtosis (above 33 at M30). This pronounced leptokurtosis supports the use of DCCA and MF-DCCA, which do not rely on Gaussian assumptions.")

heading2(P[314], "3.2 Average Cross-Correlation Across Trading Frequencies")
set_text(P[315], "Table 2 presents the average DCCA cross-correlation coefficients across trading frequencies, allowing cross-index dependence to be compared across temporal horizons and constituent structures.")
t2 = rd('02_table2_average_dcca.csv')
delete_col(T[2], 3)
set_cell(T[2], 0, 0, 'Trading frequency'); set_cell(T[2], 0, 1, 'Nested group'); set_cell(T[2], 0, 2, 'P_{cap}–VN30'); set_cell(T[2], 0, 3, 'Gap'); set_cell(T[2], 0, 4, 'N')
rows = {('A', '1D'): 2, ('A', 'M30'): 3, ('A', 'H1'): 4, ('A', 'H4'): 5, ('B', '1D'): 7, ('B', 'M30'): 8, ('B', 'H1'): 9, ('B', 'H4'): 10}
for d in t2:
    r = rows[(d['panel'], d['timeframe'])]
    for c, v in enumerate([f(d['nested_mean'], 3), f(d['Pcap-VN30'], 3), f(d['gap'], 3), f"{int(d['n']):,}"]):
        set_cell(T[2], r, c + 1, v)
set_text(P[373], "Notes: Averages of ρ_{DCCA}(s) over s ≤ s_{rel} (Table 3), m = 1. The nested group is the mean of VN30–VNINDEX, VN30–VN100 and VN100–VNINDEX. Source: Authors’ calculations.")
set_text(P[374], "Across both samples, the original nested group maintains an average correlation of 0.975–0.980 at every frequency. In contrast, P_{cap}–VN30 produces a markedly lower correlation of 0.883–0.892, a consistent gap of 0.086–0.096 correlation points. Averages in the synchronized window (Panel A) and the full sample (Panel B) differ by at most 0.007 for every series, so the unequal calendar coverage of the four frequencies does not drive the results.")
remove(P[377])
set_text(P[379], "Notes: Line and marker types identify the pairs (legend); vertical dotted lines mark the reliability thresholds s_{rel} (Table 3). Source: Authors’ calculations based on HOSE index data (TradingView).")

heading2(P[380], "3.3 Finite-Sample Reliability Thresholds")
clone_before(P[381], "Because the number of segments shrinks as the timescale grows, the DCCA coefficient becomes unreliable at large timescales. For each sample size, we simulate pairs of Gaussian white-noise series with known correlations of −0.3, 0, 0.3, 0.5, 0.7 and 0.9 (167 replications each, 1,002 per frequency) and compute the mean absolute estimation error on 40 log-spaced scales. The reliability threshold is the largest scale below the first scale at which the worst-case error exceeds 0.05. Table 3 reports the thresholds.", template=P[374])
rel = {d['timeframe']: d for d in rd('03_reliability_smax.csv')}
for c, v in enumerate(['Trading frequency', 'Sample size (N)', 'Maximum reliable scale (s_{rel})']): set_cell(T[3], 0, c, v)
for r, tf in zip(range(1, 5), ['1D', 'M30', 'H1', 'H4']):
    set_cell(T[3], r, 2, rel[tf]['s_rel'])
set_text(P[397], "Notes: Worst-case mean absolute error below 0.05 in 1,002 white-noise simulations per frequency. Source: Authors’ calculations.")
set_text(P[398], "The estimates are insensitive to the detrending order: for VN30–VNINDEX at the daily frequency, the mean reliable-range correlation is 0.9665, 0.9663 and 0.9667 for m = 1, 2 and 3. The statistical proxies (P_{heur}, P_{ratio}, P_{res}) produce average DCCA correlations with VN30 between −0.16 and 0.07, confirming that they are residual artifacts, whereas P_{cap} correlates with them at only 0.277–0.486, indicating that it captures a distinct mid-cap signal.")

heading2(P[399], "3.4 Multifractal Structure")
set_text(P[400], "The generalized Hurst exponent at the second order, h(2), lies within 0.527–0.544 for all series and frequencies, indicating weak positive persistence. However, the multifractal spectrum width, the difference between the exponents at q = −5 and q = 5, reveals substantive heterogeneity across pairs. For the nested index pairs, the width spans 0.252–0.431. For the purged capitalization proxy, it reaches 0.435–0.656 and is the largest of all pairs at every frequency, indicating richer nonlinear cross-correlation structure than in the mechanically bound nested pairs. The statistical residual proxies produce widths of 0.211–0.494 that vary erratically across frequencies, consistent with amplified noise.")
set_text(P[401], "Figure 3 contrasts the multifractal spectra and generalized exponents of the purged mid-cap proxy with those of the nested pairs at the daily frequency.")
remove(P[403])
set_text(P[404], "Fig. 3 MF-DCCA Singularity Spectra and Generalized Exponents (Daily)")
set_text(P[405], "Notes: q ∈ [−5, 5]\\{0}. Source: Authors’ calculations based on HOSE index data (TradingView).")

heading2(P[406], "3.5 Volatility Regimes and the Forbes–Rigobon Adjustment")
set_text(P[407], "Table 4 presents the unadjusted and Forbes–Rigobon conditioned correlations to assess whether the observed surge in co-movement during market turmoil reflects genuine economic interdependence or volatility expansion. Regime correlations are DCCA coefficients at a 20-day horizon estimated on the concatenated calm and turbulent subsamples of daily returns.")
fr = {(d['panel'], d['pair']): d for d in rd('10_table4_forbes_rigobon.csv')}
for r, pan in ((2, 'A'), (5, 'B')):
    d = fr[(pan, 'Pcap-VN30')]
    vals = ['P_{cap}–VN30', f(d['rho_low'], 3), f(d['rho_high'], 3), f(d['delta'], 2), f(d['rho_star'], 3),
            f(d['se'], 3), f(d['t'], 2), f"{float(d['p_one_sided']):.3f}"]
    for c, v in enumerate(vals): set_cell(T[4], r, c, v)
delete_row(T[4], 6); delete_row(T[4], 3)
for c, v in enumerate(['Asset pair', 'ρ_{low}', 'ρ_{high}', 'δ', 'ρ^{*}', 'Asymp. SE', 't-stat', 'p-value']): set_cell(T[4], 0, c, v)
set_text(P[451], "Notes: DCCA correlations at s ≈ 20 days; δ is the relative increase in VN30 return variance; one-sided test of H_{0}: ρ^{*} ≤ ρ_{low}. N_{calm}/N_{crisis} = 1,000/539 (Panel A) and 739/739 (Panel B). Source: Authors’ calculations.")
set_text(P[452], "The formal test in Table 4 is restricted to the disjoint pair P_{cap}–VN30. Because nested pairs embed the conditioning asset in the dependent series, constituent overlap creates an endogenous feedback loop that violates the exogeneity condition of Forbes and Rigobon (2002). For diagnostic comparison only, raw correlations for the nested pairs rise from 0.955–0.983 in calm periods to 0.980–0.992 in crisis episodes, and from 0.923–0.962 to 0.982–0.992 across rolling-volatility regimes.")
set_text(P[453], "In Panel A, regimes correspond to the three prolonged crisis episodes. Raw cross-tier correlation rises from 0.844 in calm years to 0.924 during crises, while the variance of VN30 returns increases by 221% (δ = 2.21). Once this volatility expansion is accounted for, the adjusted crisis correlation falls to 0.803, below its calm level, so the null hypothesis of no structural increase cannot be rejected (t = −2.28, p = 0.989). The tighter co-movement during systemic stress is thus consistent with an unchanged transmission structure operating under higher volatility, the interdependence interpretation of Forbes and Rigobon (2002). Liquidity constraints and delayed price adjustment in retail-dominated trading (Tran & Tran, 2025) offer a plausible channel through which volatility spreads across capitalization tiers without altering their underlying linkage.")
set_text(P[454], "Panel B sorts days by the rolling 20-day volatility of VNINDEX, isolating extreme volatility clustering and producing a much larger variance expansion (δ = 7.06, a 606% increase). The raw correlation rises from 0.633 to 0.929 (+0.296 points), but the volatility adjustment (a factor of 1.402) pulls the adjusted correlation down to 0.663, only 0.030 above the calm level (t = 0.97, p = 0.165). Both definitions therefore reach the same conclusion: the apparent surge in large-cap/mid-cap correlation is a volatility effect rather than evidence of contagion. The rolling definition exaggerates the raw tightening because its low-volatility days are drawn from the quietest, least correlated intervals.")

heading2(P[455], "3.6 Markowitz Portfolio Variance Implications")
set_text(P[460], "When the two assets have equal volatility, the volatility term in the denominator equals one. In the daily data (Table 1), the volatilities of P_{cap} (0.0124) and VN30 (0.0121) are so close that the term equals 1.0002, changing the denominator by only 0.02%; all reported figures nevertheless use the exact expression. Evaluating this relative variance error across regimes reveals a sharp distinction between tradable cash portfolios and underlying factor exposures.")
set_text(P[461], "For cash portfolios formed from parent and child indices (such as VN30–VN100), co-movement is dominated by constituent overlap. At the daily frequency, the static correlation of 0.988 compares with regime correlations of 0.962 and 0.992 under the rolling definition, so the static model overstates portfolio variance by 1.32% in the calm regime and understates it by 0.19% in the turbulent regime. Across all frequencies and parent–child pairs, the largest absolute error is 2.73% (VN30–VNINDEX, calm regime, H4), which is negligible for operational risk management.")
set_text(P[462], "Conversely, for the mid-cap factor exposure (P_{cap}), static correlation models produce substantial distortion. Under the rolling definition, the calm-regime correlation is 0.633, whereas the full-sample static correlation is 0.889, so the static model overstates portfolio variance by 15.63%; under the chronological definition, where the calm correlation is 0.844, the overstatement is +2.44%. An allocator relying on static metrics therefore perceives the mid-cap allocation as riskier than it is during tranquil periods, which leads to excessive risk-capital provisioning and inefficient hedging allocations.")
set_text(P[463], "In the turbulent regime, the static model understates portfolio variance by 2.10% under the rolling definition and by 1.83% under the chronological definition. Although these errors appear modest, they arise when the variance of the underlying assets has risen by 221% to 606% (Table 4). Because the crisis correlation increase is explained by volatility (Section 3.5), risk budgets should be conditioned on the volatility regime rather than on a single static correlation.")

# ================================================================= Section 5 scaling
P[464].replace(P[464].find(W + "pPr"), copy.deepcopy(P[40].find(W + "pPr"))); set_text(P[464], "3.7 Multiscale Scaling and Economic Mechanisms"); [r.replace(r.find(W+"rPr"), copy.deepcopy(P[40].find(".//"+W+"r/"+W+"rPr"))) for r in P[464].findall(W+"r") if r.find(W+"rPr") is not None]
set_text(P[465], "Table 5 presents the log-linear scaling regressions of DCCA coefficients at the M30 frequency, whose scale grid spans the widest range of horizons, to quantify the sensitivity of cross-asset co-movement to the investment horizon.")
sc = {(d['timeframe'], d['pair'], d['range']): d for d in rd('20_scale_regressions_hac.csv')}
PAIRS5 = [('VN30-VNINDEX', 'VN30–VNINDEX'), ('VN100-VNINDEX', 'VN100–VNINDEX'), ('VN30-VN100', 'VN30–VN100'),
          ('Pcap-VN30', 'P_{cap}–VN30'), ('Pheur-VN30', 'P_{heur}–VN30'), ('Pratio-VN30', 'P_{ratio}–VN30'), ('Pres-VN30', 'P_{res}–VN30')]
delete_row(T[5], 5)   # VN70 row
for c, v in enumerate(['Pair', 'Intercept (α_{scale})', 'Slope (β_{scale})', 'HAC SE', 'p-value', 'R^{2}', 'Scales (N)']): set_cell(T[5], 0, c, v)
for r, (key, lab) in enumerate(PAIRS5, start=1):
    d = sc[('M30', key, 'full')]
    vals = [lab, f(d['intercept'], 4) + star(d['p_intercept']), f(d['slope'], 4) + star(d['p_slope']), f(d['hac_se_slope'], 4),
            pv(d['p_slope']), f(d['r_squared'], 3), d['n']]
    for c, v in enumerate(vals): set_cell(T[5], r, c, v)
set_text(P[530], "Notes: 30 log-spaced scales (5 ≤ s ≤ 5,485); Newey–West HAC standard errors (3 lags). *** p < 0.01, ** p < 0.05, * p < 0.10. Source: Authors’ calculations.")
set_text(P[532], "First, for the fully nested pair VN30–VN100, the slope is statistically indistinguishable from zero (0.0001, p = 0.636): because VN30 constituents dominate VN100 capitalization, their mechanical co-movement is invariant to the timescale.")
set_text(P[533], "Second, pairs that contain a genuine cross-tier component exhibit significantly positive slopes: VN30–VNINDEX (0.0016, p < 0.001), VN100–VNINDEX (0.0009, p = 0.038) and P_{cap}–VN30 (0.0025, p = 0.009). As the timescale expands from 30 minutes to multiple trading days, cross-correlation increases systematically. The effect is specific to intraday data: at the daily frequency, the P_{cap}–VN30 slope is insignificant (0.0014, p = 0.47), whereas VN30–VNINDEX remains significant (0.0020, p < 0.001).")
set_text(P[534], "Third, for the statistical residual proxies (P_{heur}, P_{ratio}, P_{res}), the slopes are larger (0.0220–0.0222) but imprecise (p = 0.043–0.076). Because the underlying residual retains short-horizon asynchronous noise, detrending over larger timescales averages out bid–ask bounce and tick mismatch, so the residual covariance with VN30 drifts from negative intraday values toward zero.")
set_text(P[536], "This positive scaling behavior is consistent with the joint operation of two complementary economic mechanisms. First, under the Epps (1979) microstructure effect, non-synchronous trades and quote staleness in less liquid mid-cap constituents dampen cross-correlations at ultra-short intraday intervals (fewer than about ten bars). As holding periods lengthen, temporal aggregation synchronizes price discovery across stocks. Second, gradual information diffusion (Hong and Stein 1999) implies horizon-dependent co-movement because institutional investors and market makers trade predominantly in liquid VN30 large caps: market-wide news is reflected immediately in VN30 valuations but diffuses gradually into mid-cap stocks over several trading hours.")
set_text(P[537], "A critical identification boundary arises here. Although microstructure frictions (Epps, 1979) and gradual information diffusion (Hong & Stein, 1999) both imply correlations that rise with the timescale, the two mechanisms are observationally equivalent in index-level closing data. Disentangling transaction delays from cross-firm information diffusion would require tick-by-tick order-book data and firm-level news timestamps, which lie beyond the scope of this study.")

# ================================================================= Section 6 robustness
P[538].replace(P[538].find(W + "pPr"), copy.deepcopy(P[40].find(W + "pPr"))); set_text(P[538], "3.8 Robustness Checks"); [r.replace(r.find(W+"rPr"), copy.deepcopy(P[40].find(".//"+W+"r/"+W+"rPr"))) for r in P[538].findall(W+"r") if r.find(W+"rPr") is not None]
heading2(P[539], "3.8.1 Full-Range versus Reliable-Range Stability")
rel_m30 = rel['M30']['s_rel']
set_text(P[540], f"Table 6 compares the scaling slopes estimated over the full scale range with those estimated only over the reliable range (timescales up to {rel_m30} bars at M30).")
n_rel = sc[('M30', 'Pcap-VN30', 'reliable')]['n']
set_cell(T[6], 0, 1, 'Full-range Slope (N = 30)'); set_cell(T[6], 0, 2, f'Reliable-range Slope (N = {n_rel})')
delete_row(T[6], 5)
def lab6(a, b):
    sa, sb = float(a['p_slope']) < .05, float(b['p_slope']) < .05
    if not sa and not sb: return 'Flat'
    if sa and sb: return 'Stable'
    return 'Strengthens' if sb else 'Weakens'
for r, (key, lab) in enumerate(PAIRS5, start=1):
    a, b = sc[('M30', key, 'full')], sc[('M30', key, 'reliable')]
    set_cell(T[6], r, 0, lab)
    for c, d in ((1, a), (2, b)):
        tc = cell(T[6], r, c); ps = tc.findall(W + 'p')
        set_text(ps[0], f(d['slope'], 4) + star(d['p_slope']) + ' ')
        if len(ps) > 1: set_text(ps[1], '(' + f(d['hac_se_slope'], 4) + ')')
    set_cell(T[6], r, 3, lab6(a, b))
set_text(P[594], "Notes: HAC standard errors in parentheses. *** p < 0.01, ** p < 0.05, * p < 0.10. Source: Authors’ calculations.")
b = sc[('M30', 'Pcap-VN30', 'reliable')]
set_text(P[595], f"The positive slopes of VN30–VNINDEX and VN100–VNINDEX strengthen in the reliable range (0.0022, p < 0.001 for both), and VN30–VN100 remains flat. For P_{{cap}}–VN30, the reliable-range slope keeps its positive sign ({f(b['slope'],4)}) but is less precisely estimated (p = {float(b['p_slope']):.3f}). The horizon dependence of purged mid-cap co-movement is therefore robust in sign but relies partly on the longer, noisier scales, and we interpret it as suggestive; the multiscale evidence for the broad-market pairs is robust.")
heading2(P[596], "3.8.2 Sensitivity of P_{cap} to the Capitalization Weight")
set_text(P[597], "Because constituent capitalizations drift with relative price movements and periodic rebalancing, Table 7 re-estimates the key P_{cap} statistics for large-cap weights from 0.60 to 0.75.")
set_text(P[598], "Table 7: Sensitivity of P_{cap} to the Capitalization Weight (w_{30})")
for c, v in enumerate(['Weight (w_{30})', 'Mean ρ_{DCCA} (1D)', 'Slope β_{scale} (M30)', 'Calm ρ_{low}', 'Crisis ρ_{high}']):
    set_cell(T[7], 0, c, v)
for r, d in enumerate(rd('07_table7_weight_sensitivity.csv'), start=1):
    w = float(d['w']); wl = f'{w:.4f}' + (' (baseline)' if abs(w - 0.6826) < 1e-3 else '')
    for c, v in enumerate([wl, f(d['rho_mean_1D'], 3), f(d['slope_M30'], 4) + star(d['p_slope']), f(d['rho_low'], 3), f(d['rho_high'], 3)]):
        set_cell(T[7], r, c, v)
set_text(P[629], "Notes: ρ_{low} and ρ_{high} use the chronological regimes (Table 4, Panel A). *** p < 0.01, ** p < 0.05, * p < 0.10. Source: Authors’ calculations.")
set_text(P[630], "Table 7 shows that a higher large-cap weight removes more of the VN30 component and therefore lowers the P_{cap}–VN30 correlation (from 0.924 at a weight of 0.60 to 0.824 at 0.75). The central conclusions are nevertheless invariant: in every specification, the P_{cap} correlation remains at least 0.052 below the 0.977 average of the nested daily pairs, the M30 scaling slope remains positive (significant at the 5% level for weights of at least 0.65 and at the 10% level for 0.60), and raw crisis tightening (0.053–0.117) remains modest relative to the accompanying volatility expansion.")
remove(P[631])

# ================================================================= Section 7 conclusion
set_text(P[632], "4 Discussion and Conclusion", keep_tabs=True)
set_text(P[633], "This study econometrically examines multiscale cross-correlation dynamics and constituent overlap distortion among nested equity benchmarks in Vietnam. By deploying detrended cross-correlation analysis and its multifractal extension across intraday and daily trading horizons, the mechanical influence of shared capitalization is disentangled from genuine economic co-movement.")
set_text(P[634], "The empirical analysis provides three core insights:")
set_text(P[636], "First, conventional index pairs that embed large-cap constituents within broader benchmarks exhibit elevated cross-correlations attributable predominantly to index engineering rather than economic integration. Purging shared constituent capitalization through a market-weighted proxy uncovers a baseline co-movement about 0.09 correlation points lower. At intraday frequencies, cross-tier co-movement tends to be horizon-dependent: short-scale correlations are dampened by microstructure frictions and asynchronous quoting, while longer-horizon correlations strengthen as market-wide news diffuses across liquidity tiers.")
set_text(P[638], "Second, volatility conditioning shows that the tightening of cross-tier co-movement during market turmoil is explained by volatility expansion rather than by a structural break in the large-cap/mid-cap linkage. Systemic stress raises volatility across capitalization tiers, so diversification benefits shrink precisely when they are most needed even though the underlying dependence structure is stable.")
set_text(P[640], "Third, while cash portfolios composed of nested parent–child indices experience negligible variance misstatement, unadjusted static models materially misstate risk for mid-cap factor exposures. In calm market environments, conventional models overstate mid-cap portfolio variance by up to 15.6%, leading to inefficient hedging capital allocations; during market crises, they understate portfolio variance when volatility itself has multiplied.")
heading2(P[642], "4.1 Implications for ASEAN Capital Markets")
replace_in(P[646], 'risk managers should abandon static correlation assumptions in favor of regime-switching covariance frameworks that explicitly account for variance buffers during tranquil periods and sharp correlation surges during market distress.',
           'risk managers should replace static correlation assumptions with volatility-regime-conditioned covariance frameworks that recognize both overstated risk in tranquil periods and elevated co-movement during market distress.')
replace_in(P[648], 'such as VN70', 'such as VNMIDCAP (VN70)')
# 7.2 limitations
lim_h = copy.deepcopy(P[642]); P[650].addnext(lim_h); set_text(lim_h, "4.2 Limitations and Future Research", keep_tabs=True)
spacer = copy.deepcopy(P[651]); lim_h.addprevious(spacer)
l1 = clone_after(lim_h, "This study has limitations that suggest directions for future research. First, the mid-cap segment is identified through a capitalization-weighted decomposition based on a single factsheet snapshot of free-float weights. Although Section 3.8.2 shows that the conclusions are robust to weights between 0.60 and 0.75, validating the proxy against the exchange-published VNMIDCAP (VN70) index at all four frequencies, and reconstructing the historical VN30 weight from semi-annual constituent reviews, would sharpen identification.", template=P[650])
s1 = copy.deepcopy(P[651]); l1.addnext(s1)
l2 = clone_after(s1, "Second, index-level closing prices cannot separate microstructure frictions (Epps, 1979) from gradual information diffusion (Hong & Stein, 1999); constituent-level tick data and order-book depth would allow these channels to be disentangled. Third, the Forbes and Rigobon (2002) adjustment assumes exogenous large-cap shocks, an assumption that forced deleveraging may weaken; regime-switching or heteroskedasticity-based identification could provide complementary evidence. Finally, applying the framework to the nested index systems of Malaysia, Thailand and Indonesia, whose short-selling and settlement rules differ from Vietnam’s, would test the institutional hypothesis that trading restrictions shape multiscale price synchronization.", template=P[650])

# ================================================================= Declarations
eth = P[652]; coi = P[654]
set_text(eth, "This study uses only publicly available historical index price data from the Ho Chi Minh City Stock Exchange; it involves no human participants or personal data, therefore required no ethical approval, and complies with the current laws of Vietnam.", bold_lead='Ethical standards ')
decl = [("Data availability ", "The index price data were obtained from TradingView (exchange: HOSE) and are subject to the vendor’s terms of use; the merged dataset is available from the corresponding author upon reasonable request.", None),
        ("Code availability ", "The R code that reproduces every table and figure is available from the corresponding author upon request.", None),
]
anchor = eth
for lead, txt, hl in decl:
    sp = copy.deepcopy(P[653]); anchor.addnext(sp)
    anchor = clone_after(sp, txt, template=eth, bold_lead=lead, highlight=hl)
set_text(coi, "The authors declare that they have no conflict of interest.", bold_lead='Conflict of interest ')
sp = copy.deepcopy(P[653]); coi.addnext(sp)
clone_after(sp, "During the preparation of this work, the authors used an AI assistant (Claude, Anthropic) for language editing, reference verification and translation of the analysis code into R. The authors reviewed all content and take full responsibility for the publication.", template=eth, bold_lead='Declaration of generative AI use ')

# ================================================================= Journal (Asia-Pacific Financial Markets) conventions
set_text(P[5], "1 Introduction", keep_tabs=True)
# captions: bold "Table n" / "Fig. n", no colon, no final punctuation
CAP = {124: ("Table 1", "Descriptive statistics of log returns at the four trading frequencies"),
       316: ("Table 2", "Average DCCA cross-correlation by trading frequency"),
       381: ("Table 3", "Finite-sample reliability thresholds by trading frequency"),
       408: ("Table 4", "Cross-correlation across volatility regimes and Forbes–Rigobon conditioning"),
       466: ("Table 5", "Log-linear scaling regressions of DCCA coefficients (M30)"),
       541: ("Table 6", "Full-range versus reliable-range scaling slopes (M30)"),
       598: ("Table 7", "Sensitivity of P_{cap} to the capitalization weight w_{30}"),
       57: ("Fig. 1", "Twenty-day rolling volatility of VNINDEX (annualized) and market regimes, 2014–2025"),
       378: ("Fig. 2", "Multiscale DCCA cross-correlation curves for the nested pairs and P_{cap}–VN30: (a) 1D, (b) M30, (c) H1, (d) H4"),
       404: ("Fig. 3", "MF-DCCA at the daily frequency: (a) singularity spectra f(α); (b) generalized exponents h_{xy}(q)")}
for k, (lead, txt) in CAP.items():
    set_text(P[k], txt, bold_lead=lead + ' ')

# references rebuilt in the journal's style (journal and volume italic)
REFS = [
 "Al Rababa’a, A. R., Alomari, M., & McMillan, D. (2021). Multiscale stock-bond correlation: Implications for risk management. 〈Research in International Business and Finance, 58〉, 101435. https://doi.org/10.1016/j.ribaf.2021.101435",
 "Ang, A., & Chen, J. (2002). Asymmetric correlations of equity portfolios. 〈Journal of Financial Economics, 63〉(3), 443–494. https://doi.org/10.1016/S0304-405X(02)00068-5",
 "Aslam, F., Ferreira, P., Ali, H., Arifa, & Oliveira, M. (2023). Islamic vs. conventional equity markets: A multifractal cross-correlation analysis with economic policy uncertainty. 〈Economies, 11〉(1), 16. https://doi.org/10.3390/economies11010016",
 "Chen, Y., Zhang, J., Lu, L., & Xie, Z. (2024). Cross-correlation and multifractality analysis of the Chinese and American stock markets based on the MF-DCCA model. 〈Heliyon, 10〉(15), e36537. https://doi.org/10.1016/j.heliyon.2024.e36537",
 "Epps, T. W. (1979). Comovements in stock prices in the very short run. 〈Journal of the American Statistical Association, 74〉(366), 291–298. https://doi.org/10.1080/01621459.1979.10482508",
 "Forbes, K. J., & Rigobon, R. (2002). No contagion, only interdependence: Measuring stock market comovements. 〈The Journal of Finance, 57〉(5), 2223–2261. https://doi.org/10.1111/0022-1082.00494",
 "Hong, H., & Stein, J. C. (1999). A unified theory of underreaction, momentum trading, and overreaction in asset markets. 〈The Journal of Finance, 54〉(6), 2143–2184. https://doi.org/10.1111/0022-1082.00184",
 "Jiang, Z.-Q., & Zhou, W.-X. (2011). Multifractal detrending moving-average cross-correlation analysis. 〈Physical Review E, 84〉(1), 016106. https://doi.org/10.1103/PhysRevE.84.016106",
 "Kantelhardt, J. W., Zschiegner, S. A., Koscielny-Bunde, E., Havlin, S., Bunde, A., & Stanley, H. E. (2002). Multifractal detrended fluctuation analysis of nonstationary time series. 〈Physica A: Statistical Mechanics and its Applications, 316〉(1–4), 87–114. https://doi.org/10.1016/S0378-4371(02)01383-3",
 "Karim, B. A., & Ning, H. X. (2013). Driving forces of the ASEAN-5 stock markets integration. 〈Asia-Pacific Journal of Business Administration, 5〉(3), 186–191. https://doi.org/10.1108/APJBA-07-2012-0053",
 "Le, T. T. V., Dang, T. P. T., & Phan, T. H. N. (2025). The nonlinear dependence of the Vietnam stock market on the Asian stock market: Evidence from a quantile-on-quantile regression. 〈International Journal of Innovative Research and Scientific Studies, 8〉(4), 7901–7914. https://doi.org/10.53894/ijirss.v8i4.7901",
 "Lean, H. H., & Teng, K. T. (2013). Integration of world leaders and emerging powers into the Malaysian stock market: A DCC-MGARCH approach. 〈Economic Modelling, 32〉, 333–342. https://doi.org/10.1016/j.econmod.2013.02.013",
 "Longin, F., & Solnik, B. (2001). Extreme correlation of international equity markets. 〈The Journal of Finance, 56〉(2), 649–676. https://doi.org/10.1111/0022-1082.00340",
 "Markowitz, H. (1952). Portfolio selection. 〈The Journal of Finance, 7〉(1), 77–91. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x",
 "Michis, A. A. (2022). Multiscale partial correlation clustering of stock market returns. 〈Journal of Risk and Financial Management, 15〉(1), 24. https://doi.org/10.3390/jrfm15010024",
 "Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. 〈Econometrica, 55〉(3), 703–708. https://doi.org/10.2307/1913610",
 "Oświęcimka, P., Drożdż, S., Forczek, M., Jadach, S., & Kwapień, J. (2014). Detrended cross-correlation analysis consistently extended to multifractality. 〈Physical Review E, 89〉(2), 022805. https://doi.org/10.1103/PhysRevE.89.022805",
 "Peng, C.-K., Buldyrev, S. V., Havlin, S., Simons, M., Stanley, H. E., & Goldberger, A. L. (1994). Mosaic organization of DNA nucleotides. 〈Physical Review E, 49〉(2), 1685–1689. https://doi.org/10.1103/PhysRevE.49.1685",
 "Podobnik, B., & Stanley, H. E. (2008). Detrended cross-correlation analysis: A new method for analyzing two nonstationary time series. 〈Physical Review Letters, 100〉(8), 084102. https://doi.org/10.1103/PhysRevLett.100.084102",
 "Podobnik, B., Jiang, Z.-Q., Zhou, W.-X., & Stanley, H. E. (2011). Statistical tests for power-law cross-correlated processes. 〈Physical Review E, 84〉(6), 066118. https://doi.org/10.1103/PhysRevE.84.066118",
 "Rodriguez, E., & Alvarez-Ramirez, J. (2021). Time-varying cross-correlation between trading volume and returns in US stock markets. 〈Physica A: Statistical Mechanics and its Applications, 581〉, 126211. https://doi.org/10.1016/j.physa.2021.126211",
 "Tran, M. H., & Tran, N. M. (2025). High-frequency dynamics of the Vietnam stock market. 〈VNU Journal of Economics and Business, 5〉(2), 51–59. https://doi.org/10.57110/vnu-jeb.v5i2.395",
 "Zebende, G. F. (2011). DCCA cross-correlation coefficient: Quantifying level of cross-correlation. 〈Physica A: Statistical Mechanics and its Applications, 390〉(4), 614–618. https://doi.org/10.1016/j.physa.2010.10.022",
 "Zhou, W.-X. (2008). Multifractal detrended cross-correlation analysis for two nonstationary signals. 〈Physical Review E, 77〉(6), 066211. https://doi.org/10.1103/PhysRevE.77.066211",
 "Zhou, W., Huang, J., & Wang, M. (2025). Multifractal characteristics and information flow analysis of stock markets based on multifractal detrended cross-correlation analysis and transfer entropy. 〈Fractal and Fractional, 9〉(1), 14. https://doi.org/10.3390/fractalfract9010014",
]
ref_ps = [q for q in body.iter(W + 'p') if q.find(W + 'pPr/' + W + 'pStyle') is not None and q.find(W + 'pPr/' + W + 'pStyle').get(W + 'val') == 'referenceitem']
tmpl = ref_ps[0]
for q in ref_ps[1:]: remove(q)
set_text(tmpl, REFS[0], keep_tabs=True); last = tmpl
for rtxt in REFS[1:]:
    last = clone_after(last, rtxt, template=tmpl, keep_tabs=True)

# in-text citations: Springer name-year style, e.g. (Hong and Stein 1999), Forbes and Rigobon (2002)
refs_head = [q for q in body.iter(W + 'p') if text_of(q).strip() == 'References'][0]
cit = re.compile(r"([A-Z][A-Za-z’'\-ÀÁĐ-ỹśęćźżłńó]+(?: et al\.)?(?: (?:&|and) [A-Z][A-Za-z’'\-ÀÁĐ-ỹśęćźżłńó]+)?),\s((?:19|20)\d\d)")
for q in list(body.iter(W + 'p')):
    if q is refs_head: break
    for t in q.iter(W + 't'):
        if t.text and re.search(r'(19|20)\d\d', t.text):
            new = cit.sub(r'\1 \2', t.text)
            new = re.sub(r"([A-Z][a-z’'\-]+) & ([A-Z][a-z’'\-]+)( \d{4}| \()", r"\1 and \2\3", new)
            t.text = new

# ================================================================= Figures: replace media, Fig. 1 chart -> picture
FIG = OUT + '/figures/'
shutil.copy(FIG + 'fig2_dcca_curves.png', dst + '/word/media/image1.png')
shutil.copy(FIG + 'fig3_mfdcca.png', dst + '/word/media/image2.png')
shutil.copy(FIG + 'fig1_volatility_regimes.png', dst + '/word/media/image4.png')
WP = '{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
def set_extent(drawing, cx, cy):
    for e in drawing.iter(WP + 'extent', A + 'ext'):
        if e.get('cx'): e.set('cx', str(cx)); e.set('cy', str(cy))
CX = 5943600
d2 = P[376].find('.//' + W + 'drawing'); set_extent(d2, CX, int(CX * 5 / 6.5))
d3 = P[402].find('.//' + W + 'drawing'); set_extent(d3, CX, int(CX * 3.4 / 6.5))
d1 = copy.deepcopy(d2); set_extent(d1, CX, int(CX * 3.2 / 6.5))
for e in d1.iter():
    if e.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed'):
        e.set('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed', 'rId900')
    if e.tag == WP + 'docPr': e.set('id', '9001'); e.set('name', 'Figure 1')
old = P[56].find('.//' + W + 'drawing'); old.getparent().replace(old, d1)
rels_p = dst + '/word/_rels/document.xml.rels'; rels = open(rels_p).read()
rels = re.sub(r'<Relationship Id="rId9" [^>]*/>', '', rels)
rels = re.sub(r'<Relationship Id="rId12" [^>]*/>', '', rels)
rels = rels.replace('</Relationships>', '<Relationship Id="rId900" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image4.png"/></Relationships>')
open(rels_p, 'w').write(rels)
shutil.rmtree(dst + '/word/charts', ignore_errors=True)
for fx in ('image3.gif',):
    if os.path.exists(dst + '/word/media/' + fx): os.remove(dst + '/word/media/' + fx)
if os.path.exists(dst + '/word/embeddings'): shutil.rmtree(dst + '/word/embeddings')
ct_p = dst + '/[Content_Types].xml'; ct = open(ct_p).read()
ct = re.sub(r'<Override [^>]*PartName="/word/charts/[^"]*"[^>]*/>', '', ct)
ct = re.sub(r'<Override [^>]*PartName="/word/embeddings/[^"]*"[^>]*/>', '', ct)
open(ct_p, 'w').write(ct)


# final citation-style pass across run boundaries + typography
cit2 = re.compile(r"([A-Z][^\s(),;]+(?: et al\.)?(?: (?:&|and) [A-Z][^\s(),;]+)?),\s((?:19|20)\d\d)")
for q in list(body.iter(W + 'p')):
    if q is refs_head: break
    txt = text_of(q)
    for m in set(cit2.findall(txt)):
        old = f"{m[0]}, {m[1]}"; replace_in(q, old, f"{m[0].replace(' & ', ' and ')} {m[1]}")
    for m in set(re.findall(r"[A-Z][^\s(),;]+ & [A-Z][^\s(),;]+ (?:19|20)\d\d", text_of(q))):
        replace_in(q, m, m.replace(' & ', ' and '))
    replace_in(q, "Al Rababa'a", "Al Rababa’a")
    while replace_in(q, ".  ", ". "): pass

for q in body.iter(W + 'p'):
    if text_of(q).startswith('Notes:'):
        pp = q.find(W + 'pPr')
        sp = pp.find(W + 'spacing')
        if sp is None:
            sp = etree.Element(W + 'spacing'); kids = [etree.QName(k).localname for k in pp]
            idx = next((i for i, k in enumerate(kids) if k in ('ind', 'jc', 'rPr')), len(kids)); pp.insert(idx, sp)
        sp.set(W + 'before', '60'); sp.set(W + 'after', '200')
tree.write(dst + '/word/document.xml', xml_declaration=True, encoding='UTF-8', standalone=True)
print('stage2 ok')
