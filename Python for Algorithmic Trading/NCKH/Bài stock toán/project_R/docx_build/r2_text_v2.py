"""Round-2 manuscript body (Sections 1, 3-7, Appendix). Every result is read from the R outputs via r2_data."""
from r2_data import *
from r2_lit import LIT_INTRO, LIT_SECTIONS, TABLE1_ROWS, TABLE1_NOTE

# ---------------------------------------------------------------- derived quantities
gapB = {t: R2[(t, 'nested_mean-minus-Pcap', 'gap')] for t in TF}
gap_vals = [float(AVG[('B', t)]['gap']) for t in TF] + [float(AVG[('A', t)]['gap']) for t in TF]
gap_lo = min(float(gapB[t]['ci_lo']) for t in TF); gap_hi = max(float(gapB[t]['ci_hi']) for t in TF)
nested_all = [float(AVG[(p, t)]['nested_mean']) for p in 'AB' for t in TF]
pcap_all = [float(AVG[(p, t)]['Pcap-VN30']) for p in 'AB' for t in TF]
D = lambda t, s: DEC[(t, s)]
share = [float(D(t, 'mech_share')['estimate']) for t in TF]
share_lo = min(float(D(t, 'mech_share')['ci_lo']) for t in TF)
share_hi = max(float(D(t, 'mech_share')['ci_hi']) for t in TF)
floor_v = [float(D(t, 'floor')['estimate']) for t in TF]
sens_v = [float(D(t, 'sensitivity')['estimate']) for t in TF]
kap_v = [float(D(t, 'kappa')['estimate']) for t in TF]
fme = {t: D(t, 'floor_minus_econ') for t in TF}
fme_pos = [t for t in TF if float(fme[t]['ci_lo']) > 0]
att = [1 / s for s in sens_v]
H2_ok = share_lo > 0.5
idmax = max(float(r['identity_error']) for r in DECS)
P1 = PEAR['1D']
qv = [float(Q[t]['cohen_q']) for t in TF]; q_lo = min(float(Q[t]['ci_lo']) for t in TF); q_hi = max(float(Q[t]['ci_hi']) for t in TF)
H1_ok = all(float(gapB[t]['ci_lo']) > 0 for t in TF)

def slope(t, p, st): return MT[(t, p, st)]
sig_rel = [(t, p) for (t, p, st), r in MT.items() if st == 'slope_rel' and float(r['ci_lo']) > 0]
holm_rel = [(t, p) for (t, p, st), r in MT.items() if st == 'slope_rel' and float(r['p_holm']) < 0.05]
bh_rel = [(t, p) for (t, p, st), r in MT.items() if st == 'slope_rel' and float(r['p_bh']) < 0.05]
bh_min = min(float(r['p_bh']) for (t, p, st), r in MT.items() if st == 'slope_rel')
H3_out = 'Partially supported' if bh_rel else 'Not supported after adjustment'
fam = int(float(next(iter(MT.values()))['family_size']))
B_REPS = 499

frA, frB = FR[('A', 'Pcap-VN30')], FR[('B', 'Pcap-VN30')]
H4_reject = float(frA['p_one_sided']) < 0.05 or float(frB['p_one_sided']) < 0.05
reAl, reAh = RE[('A', 'Pcap-VN30', 'low')], RE[('A', 'Pcap-VN30', 'high')]
reBl, reBh = RE[('B', 'Pcap-VN30', 'low')], RE[('B', 'Pcap-VN30', 'high')]
nested_re = [abs(float(r['RE_pct'])) for k, r in RE.items() if k[1] != 'Pcap-VN30']
pcap_re_ok = all((float(r['ci_lo']) > 0) or (float(r['ci_hi']) < 0) for r in (reAl, reAh, reBl, reBh))

dm_gap = [float(DMCA[(t, 'Pcap-VN30')]['gap_vs_nested_mean']) for t in TF]
dm_pcap = [float(DMCA[(t, 'Pcap-VN30')]['rho_dmca_avg']) for t in TF]
dm_nest = [float(DMCA[(t, p)]['rho_dmca_avg']) for t in TF for p in NESTED]
tl = lambda p, u: TAIL[(p, u)]
blk_lo = min(float(r['ci_lo']) for r in BLK); blk_hi = max(float(r['ci_hi']) for r in BLK)
w_base = [r for r in WS if abs(float(r['w']) - 0.6826) < 1e-3][0]
w_min_gap = min(float(r['gap_vs_nested']) for r in WS)
ols_r2 = [float(OLS[t]['r_squared']) for t in TF]; ols_b = [float(OLS[t]['beta']) for t in TF]
w_heur = [float(OLS[t]['w_heur']) for t in TF]; amp = [float(OLS[t]['amplification_heur']) for t in TF]
dh_nest = [float(SURR[(t, p)]['dh_obs']) for t in TF for p in NESTED]
dh_pcap = [float(SURR[(t, 'Pcap-VN30')]['dh_obs']) for t in TF]
surr_nest_exc = sum(SURR[(t, p)]['exceeds_q95'] == 'TRUE' for t in TF for p in NESTED)
surr_pcap_exc = [t for t in TF if SURR[(t, 'Pcap-VN30')]['exceeds_q95'] == 'TRUE']
h2 = [float(r['lambda_xy']) for r in HQ if r['q'] == '2' and r['pair'] in NESTED + ['Pcap-VN30']]
cr = CRISIS[:3]
W30 = 1316288 / 1928303


def tex(x, d=3):
    return f'{float(x):.{d}f}'


TITLE = 'The Mechanical Floor of Nested Index Correlations: An Exact Multiscale Decomposition with Evidence from Vietnam'

ABSTRACT = (
    "Large-cap and broad-market indices are often treated as separate diversification instruments even when one index is a "
    "subset of the other. We show that this practice confuses index construction with economic co-movement and quantify the "
    "confusion exactly. Because a parent index is a capitalization-weighted sum of its child index and the remaining "
    "constituents, the detrended cross-correlation analysis (DCCA) coefficient between them decomposes, at every timescale, "
    "into a mechanical floor fixed by index weights and relative volatility, and a term that depends on the economic correlation "
    "between the child and the remaining constituents. Applying this identity to the Ho Chi Minh City Stock Exchange (VN30 within "
    f"VN100 within VNINDEX; 30-minute to daily data, 2014–2025), we find that the floor alone accounts for {rng(share, 3)} of the "
    f"observed VN30–VN100 coefficient (block-bootstrap 95% intervals within {f(share_lo, 3)}–{f(share_hi, 3)}), and that a change of "
    f"0.10 in the economic correlation moves the nested coefficient by only about {f(0.1 * sum(sens_v) / 4, 3)}. "
    f"Purging the overlap lowers the correlation with large caps by {rng(gap_vals[:4], 3)} (intervals exclude zero at all four "
    "frequencies). Broad-market pairs show small positive horizon slopes at intraday frequencies that do not survive multiple-testing "
    "adjustment, and the purged correlation shows none. "
    "Forbes–Rigobon volatility conditioning gives no evidence of crisis contagion between tiers, and a static correlation misstates "
    f"mid-cap portfolio variance by between {f(min(float(reAh['RE_pct']), float(reBh['RE_pct'])), 1)}% and +{f(float(reBl['RE_pct']), 1)}% "
    "across volatility regimes. The results apply to one market and three indices; the identity itself holds for any nested pair."
)
KEYWORDS = 'constituent overlap; detrended cross-correlation; Forbes–Rigobon adjustment; multiscale correlation; portfolio risk; Vietnam'
JEL = 'C14; C58; G11; G15'


def introduction():
    return [
        ('h1', '1 Introduction'),
        ('p1a', "Multi-capitalization portfolios are often built as if large-cap and broad-market indices were separate sources of "
                "diversification. Risk models, allocation rules and stress tests typically summarize the dependence between such "
                "indices with a single Pearson correlation of daily returns (Markowitz 1952). In nested index systems this number "
                "has a problem that is independent of estimation error: the parent index contains the child index, so part of their "
                "correlation is fixed by index construction. On the Ho Chi Minh City Stock Exchange (HOSE), the large-cap VN30 index "
                "is contained in the VN100 index, which is contained in the market-wide VNINDEX:"),
        ('eq', r'\mathrm{VN30} \subset \mathrm{VN100} \subset \mathrm{VNINDEX}. \qquad (1)'),
        ('p', "Because the 30 largest firms account for about two-thirds of the free-float capitalization of VN100, the correlation "
              f"between VN30 and VN100 returns is close to one ({f(AVG[('B', '1D')]['VN30-VN100'])} at the daily frequency). How "
              "much of this number reflects economic linkage between large caps and the rest of the market, and how much reflects "
              "the fact that VN30 stocks are counted on both sides? Existing studies of multiscale co-movement, which rely mostly on "
              "detrended cross-correlation analysis (DCCA) and wavelet methods, analyze pairs of assets that share no constituents "
              "(Section 2), so they do not answer this question."),
        ('p', "This paper answers it with an exact result. Writing the parent index return as a capitalization-weighted sum of the "
              "child index return and the return on the remaining constituents, we prove (Proposition 1) that the DCCA coefficient "
              "of a nested pair is, at every timescale, a known function of two quantities: the DCCA coefficient between the child "
              "index and the remaining constituents, which we call the economic correlation, and a relative-amplitude ratio fixed "
              "by index weights and volatilities. The function has a strictly positive floor: even if the remaining constituents "
              "were uncorrelated with the child index, the nested coefficient would equal that floor. The identity holds for Pearson "
              "correlation as a special case and requires no distributional assumption."),
        ('p', "We apply the identity, together with a capitalization-weighted mid-cap proxy that removes the overlap, to VN30, VN100 "
              "and VNINDEX at 30-minute, 1-hour, 4-hour and daily frequencies from 2014 to 2025. We test five hypotheses, stated in "
              "Section 2.5, on overlap inflation, the dominance of the mechanical floor, horizon dependence, crisis contagion and "
              "portfolio-variance misstatement. All inference uses stationary block bootstrap intervals, and the horizon-dependence "
              "tests are adjusted for multiple comparisons."),
        ('p', "The paper makes three contributions. First, it derives an exact, scale-by-scale decomposition of nested index "
              "correlations into a mechanical floor and an economic component, with closed forms for the floor and for the "
              "sensitivity of the nested coefficient to the economic correlation. In our data the floor accounts for "
              f"{rng(share, 3)} of the VN30–VN100 coefficient, and the nested coefficient responds to the economic correlation with "
              f"a slope of {rng(sens_v, 3)}, so index-level correlations carry little information about economic co-movement. "
              "Second, it measures the overlap effect with inference: purging the overlap lowers the correlation with large caps by "
              f"{rng(gap_vals[:4], 3)} with bootstrap intervals that exclude zero at every frequency, while the purged correlation "
              f"remains high (about {f(sum(pcap_all) / len(pcap_all), 2)}). Third, it separates volatility from structural change in crises and "
              "prices the cost of static correlations: Forbes–Rigobon conditioning gives no evidence of cross-tier contagion, and a "
              "static correlation misstates the variance of a mid-cap factor exposure by amounts that switch sign between calm and "
              "turbulent regimes."),
        ('p', "The remainder of the paper is organized as follows. Section 2 reviews the literature and develops the hypotheses. "
              "Section 3 describes the institutional setting and the data. Section 4 presents the methodology, including "
              "Proposition 1. Section 5 reports the results, Section 6 discusses mechanisms, implications and limitations, and "
              "Section 7 concludes."),
    ]


def hypotheses():
    return [
        ('h2', '2.5 Hypothesis development'),
        ('p1a', "The literature reviewed above and Proposition 1 (Section 4.2) yield five testable hypotheses. For each we state the "
                "prediction, the test and the decision rule; all tests use a 5% level."),
        ('p', "Constituent overlap adds the variance of shared stocks to both sides of a nested pair. If index-level correlations "
              "contain a mechanical component, they should exceed the correlation between the child index and the non-overlapping "
              "remainder."),
        ('p', "*H1 (overlap inflation).* At every trading frequency, the average reliable-range DCCA coefficient of the nested pairs "
              "exceeds that of the purged pair (mid-cap proxy and VN30). Test: the block-bootstrap 95% interval for the difference "
              "excludes zero; effect size: Cohen’s q on Fisher-transformed coefficients."),
        ('p', "Proposition 1 implies that the nested coefficient cannot fall below a floor determined by index weights and relative "
              "volatility. When the child index carries most of the parent’s capitalization, the floor should account for most of "
              "the observed coefficient."),
        ('p', "*H2 (mechanical dominance).* The mechanical floor accounts for more than half of the VN30–VN100 DCCA coefficient. "
              "Test: one-sided bootstrap test of a share above 0.5, with the lower bound of the 95% interval above 0.5 at every "
              "frequency."),
        ('p', "Non-synchronous trading depresses correlations at short horizons (Epps 1979), and gradual information diffusion "
              "(Hong and Stein 1999) lets co-movement build up with the horizon. Both mechanisms predict positive scaling slopes "
              "for pairs whose constituents are repriced at different speeds, such as broad-market pairs that include small, "
              "illiquid stocks, and no slope for VN30–VN100, whose co-movement is fixed by overlap."),
        ('p', "*H3 (horizon dependence).* The DCCA coefficient rises with the timescale for pairs involving the broad market, but "
              "not for the VN30–VN100 pair. Test: block-bootstrap intervals for log-linear scaling slopes, with Holm and "
              "Benjamini–Hochberg adjustment across all slope tests."),
        ('p', "Forbes and Rigobon (2002) show that unadjusted correlations rise mechanically with the variance of the conditioning "
              "market. Contagion requires that the adjusted crisis correlation exceed its calm level."),
        ('p', "*H4 (contagion).* After Forbes–Rigobon conditioning, the crisis correlation between the purged mid-cap component and "
              "VN30 exceeds the calm-period correlation. Test: one-sided bootstrap test, reported with its power against an increase "
              "of 0.05."),
        ('p', "If correlations vary with the volatility regime, a static correlation will misstate portfolio variance, and the "
              "error should be larger for the purged mid-cap exposure, whose correlation varies more, than for nested cash "
              "portfolios."),
        ('p', "*H5 (risk misstatement).* A static correlation misstates the variance of an equally weighted large-cap and mid-cap "
              "portfolio in calm and turbulent regimes. Test: block-bootstrap intervals for the relative variance error exclude "
              "zero."),
    ]


def institutions_data():
    c = cr
    return [
        ('h1', '3 Institutional background and data'),
        ('h2', '3.1 Institutional background'),
        ('p1a', "The HOSE is regulated by the State Securities Commission of Vietnam (SSC). Four features of its microstructure "
                "matter for cross-index dependence. First, prices move within a symmetric daily band of ±7% around the reference "
                "price; during sharp corrections heavily sold stocks reach the lower limit, where trading dries up, which "
                "truncates return tails and can synchronize limit hits across constituents. Second, under the T+2 settlement cycle "
                "in force for most of the sample, shares bought could not be sold before the afternoon of the second business day, "
                "which restricts intraday arbitrage between constituents and index baskets."),
        ('p', "Third, each session opens with a 15-minute call auction (09:00–09:15) and closes with another (14:30–14:45), with "
              "continuous matching in between, so the first and last 30-minute bars of each day are more volatile and less "
              "synchronous than midday bars. Fourth, Decree 155/2020/ND-CP and Circular 120/2020/TT-BTC prohibit cash short "
              "selling; margin rules require an initial margin of at least 50%, and Circular 68/2024/TT-BTC, which removed the "
              "pre-funding requirement for foreign institutional investors, left the short-sale prohibition unchanged. VN30 index "
              "futures trade on the Hanoi Stock Exchange, but no mid-cap index future exists. Arbitrageurs therefore cannot trade "
              "the spread between large caps and mid-caps, which can prolong non-synchronous price adjustment between them."),
        ('h2', '3.2 Data and sample construction'),
        ('p1a', "We use closing prices of three HOSE indices exported from TradingView (exchange code HOSE; symbols VN30, VN100 and "
                "VNINDEX): VN30, which contains the 30 largest and most liquid stocks screened by free-float capitalization; VN100, "
                "which adds the next 70 stocks (the constituents of the VNMIDCAP, or VN70, index); and VNINDEX, which covers all "
                "common stocks listed on the HOSE, weighted by full market capitalization. Daily and 30-minute series run to "
                "12 December 2025; the 1-hour and 4-hour series available from the vendor end on 9 December 2024. A VNMIDCAP price "
                "history is not available from this source for the full sample and all frequencies, so the mid-cap segment is "
                "recovered by the decomposition in Section 4.2."),
        ('p', "The three series are merged by exact inner joins on timestamps; no index level is filled or interpolated. Log returns "
              "are computed as"),
        ('eq', r'R_t=\ln P_t-\ln P_{t-1}. \qquad (2)'),
        ('p', "Two samples are used. The synchronized window (3 January 2017 to 9 December 2024) is the period in which all four "
              f"frequencies overlap (1D: N = {nint(AVG[('A', '1D')]['n'])}; M30: N = {nint(AVG[('A', 'M30')]['n'])}; H1: N = "
              f"{nint(AVG[('A', 'H1')]['n'])}; H4: N = {nint(AVG[('A', 'H4')]['n'])}) and is used for cross-frequency comparisons. The "
              "full sample, used for all other analyses, runs from February 2014 to December 2025 at the daily frequency (N = "
              f"{nint(DESC[('VN30', '1D')]['n'])}), from January 2017 to December 2025 at M30 (N = {nint(DESC[('VN30', 'M30')]['n'])}) and "
              f"from January 2014 to December 2024 at H1 and H4 (N = {nint(DESC[('VN30', 'H1')]['n'])} and {nint(DESC[('VN30', 'H4')]['n'])})."),
        ('p', "The series are official index levels computed in real time by the exchange, not indices back-calculated from current "
              "membership lists. Semi-annual constituent reviews, delistings, corporate actions and free-float adjustments are "
              "therefore embedded in the return paths, so the sample is free of survivorship and look-ahead bias in index "
              "composition."),
        ('p', "Regime dependence is evaluated under two definitions based on the 20-day rolling standard deviation of VNINDEX returns "
              "(Fig. 1). The first uses chronological crisis episodes that satisfy three conditions: a peak-to-trough VNINDEX "
              "drawdown above 25%, at least 45% of trading days in the top quartile of rolling volatility, and a documented "
              f"macro-financial trigger. Three episodes qualify: the 2018 margin contraction (drawdown {f(-float(c[0]['max_drawdown_pct']), 1)}%, "
              f"{f(100 * float(c[0]['share_high_vol_days']), 0)}% of days in the top quartile), the 2020 COVID-19 shock "
              f"({f(-float(c[1]['max_drawdown_pct']), 1)}%, {f(100 * float(c[1]['share_high_vol_days']), 0)}%) and the 2022 corporate bond "
              f"liquidity freeze ({f(-float(c[2]['max_drawdown_pct']), 1)}%, {f(100 * float(c[2]['share_high_vol_days']), 0)}%), totaling "
              f"{nint(SC['n_crisis_days'][0])} trading days; the calm benchmark comprises 2016–2017 and 2023–2024 "
              f"({nint(SC['n_calm_days'][0])} days). The April 2025 tariff shock (drawdown {f(-float(CRISIS[3]['max_drawdown_pct']), 1)}%) fails "
              "the first two conditions. The second definition sorts all days by rolling volatility and compares days below the 25th "
              f"percentile ({f(SC['vol_quartiles_ann_pct'][0], 1)}% annualized) with days above the 75th percentile "
              f"({f(SC['vol_quartiles_ann_pct'][1], 1)}%)."),
        ('fig', ('fig1', 'Fig. 1 Twenty-day rolling volatility of VNINDEX (annualized) and market regimes, 2014–2025',
                 'Shaded areas mark the three crisis episodes; dashed and dotted lines mark the 25th and 75th percentiles. '
                 'Source: Authors’ calculations based on HOSE index data (TradingView).')),
    ]


def methodology():
    return [
        ('h1', '4 Methodology'),
        ('h2', '4.1 The DCCA coefficient'),
        ('p1a', "Following Podobnik and Stanley (2008) and Zebende (2011), the DCCA coefficient measures covariance at timescale s "
                "after removing local trends. For return series x and y of length N, the profiles are"),
        ('eq', r'X_k=\sum_{t=1}^{k}(x_t-\bar{x}),\quad Y_k=\sum_{t=1}^{k}(y_t-\bar{y}),\quad k=1,\dots,N. \qquad (3)'),
        ('p', "Each profile is divided into N_s = ⌊N/s⌋ non-overlapping boxes of length s, starting once from each end of the series, "
              "which gives 2N_s boxes. In box ν a polynomial of order m (m = 1 unless stated otherwise) is fitted by ordinary least "
              "squares (OLS), and the residuals ε_X and ε_Y define the detrended covariance"),
        ('eq', r'f^2_{XY}(s,\nu)=\frac{1}{s}\sum_{k=1}^{s}\varepsilon_{X}(k,\nu)\,\varepsilon_{Y}(k,\nu),\qquad F^2_{XY}(s)=\frac{1}{2N_s}\sum_{\nu=1}^{2N_s}f^2_{XY}(s,\nu). \qquad (4)'),
        ('p', "With F_X(s) = [F²_XX(s)]^{1/2} the detrended fluctuation function of x (Peng et al. 1994), the DCCA coefficient is"),
        ('eq', r'\rho_{XY}(s)=\frac{F^2_{XY}(s)}{F_X(s)\,F_Y(s)}. \qquad (5)'),
        ('p', "Because Eq. (5) is the inner product of the stacked residual vectors divided by the product of their norms, the "
              "Cauchy–Schwarz inequality gives |ρ_XY(s)| ≤ 1 for every s, provided both fluctuation functions are positive. Two "
              "properties of Eq. (4) are used below: the profile is a linear function of the series, and OLS detrending is a "
              "linear projection, so the residuals of a weighted sum of series are the same weighted sum of their residuals."),
        ('h2', '4.2 Mid-cap decomposition and the exact overlap identity'),
        ('p1a', "Let A_t = R_{30,t} and B_t = R_{100,t} denote VN30 and VN100 returns, and let w be the free-float weight of VN30 in "
                "VN100. We define the capitalization-weighted mid-cap proxy"),
        ('eq', r'M_t=P_{\mathrm{cap},t}=\frac{B_t-wA_t}{1-w}, \qquad (6)'),
        ('p', f"with w = {f(W30, 4)}, computed from the HOSE factsheet of 31 May 2024 (VN30 and VN100 free-float capitalizations of "
              "VND 1,316,288 billion and VND 1,928,303 billion). The weight is fixed from the factsheet before any estimation, so it "
              "is not tuned to the results. Rearranging Eq. (6), B_t = wA_t + (1 − w)M_t holds exactly at every observation. Because "
              "the decomposition is applied to log rather than arithmetic returns, the proxy differs from the true mid-cap return "
              f"by a Jensen term of {f(SC['jensen_delta'][0] * 1e6, 1)} × 10⁻⁶ per day at the daily frequency, which is negligible for "
              "the DCCA estimates. The proxy requires a long position of about 315% in VN100 and a short position of about 215% in "
              "VN30, so under the short-sale prohibition it is an analytical shadow benchmark, not a tradable portfolio."),
        ('p', "**Proposition 1 (exact overlap decomposition).** Let B_t = wA_t + (1 − w)M_t for all t, with 0 < w < 1, and let "
              "F_A(s), F_M(s) > 0. Define the relative amplitude κ(s) = (1 − w)F_M(s)/[wF_A(s)] and the economic correlation "
              "ρ_AM(s). Then, for every timescale s and detrending order m,"),
        ('eq', r'\rho_{AB}(s)=\frac{1+\kappa(s)\,\rho_{AM}(s)}{\sqrt{1+\kappa(s)^2+2\kappa(s)\,\rho_{AM}(s)}}. \qquad (7)'),
        ('p', "*Proof.* Profiles and box-wise OLS residuals are linear in the series, so ε_B = wε_A + (1 − w)ε_M in every box. "
              "Because Eq. (4) is bilinear, F²_AB = wF²_A + (1 − w)ρ_AM F_A F_M and F²_B = w²F²_A + (1 − w)²F²_M + "
              "2w(1 − w)ρ_AM F_A F_M. Substituting into Eq. (5) and dividing numerator and denominator by wF_A² gives Eq. (7). ∎"),
        ('p', "Three corollaries follow. First, setting ρ_AM(s) = 0 gives the mechanical floor"),
        ('eq', r'\underline{\rho}(s)=\frac{1}{\sqrt{1+\kappa(s)^2}}>0, \qquad (8)'),
        ('p', "the value the nested coefficient would take if the remaining constituents were uncorrelated with the child index. We "
              "call ρ̲(s)/ρ_AB(s) the mechanical share. Second, the sensitivity of the nested coefficient to the economic "
              "correlation is"),
        ('eq', r'\frac{\partial\rho_{AB}(s)}{\partial\rho_{AM}(s)}=\frac{\kappa(s)^2\,[\kappa(s)+\rho_{AM}(s)]}{[1+\kappa(s)^2+2\kappa(s)\,\rho_{AM}(s)]^{3/2}}, \qquad (9)'),
        ('p', "which is small when κ is small, that is, when the child index dominates the parent. Third, for ρ_AM ≥ 0, "
              "ρ²_AB − ρ²_AM = (1 − ρ²_AM)(1 + 2κρ_AM)/(1 + κ² + 2κρ_AM) ≥ 0, so overlap can only inflate the coefficient, with "
              "equality only when ρ_AM = 1. The identity uses only linearity and bilinearity: it holds for the Pearson "
              "correlation (no detrending, one box), for the detrending moving-average coefficient used in Section 5.9 and for any "
              "other dependence measure built from a bilinear covariance of linearly filtered series."),
        ('p', "Equation (7) is not an approximation; we verify numerically that it reproduces the directly estimated VN30–VN100 "
              f"coefficient at every scale and frequency to within {f(idmax * 1e16, 1)} × 10⁻¹⁶. We estimate κ, the floor, the "
              "mechanical share and the sensitivity on each scale of the reliable range (Section 4.4), average them over that range "
              "and obtain 95% intervals from the block bootstrap described below. Because P_cap is constructed from A and B, Eq. (7) "
              "is an accounting identity rather than an estimated relation; its content lies in the decomposition it delivers. The "
              "floor and the sensitivity depend only on w and the relative amplitude κ, so they can be computed for any nested pair "
              "whose child weight and fluctuation functions are known."),
        ('p', "For comparison we construct three statistical proxies: the volatility-scaled proxy P_heur, which replaces w by the "
              f"correlation between VN30 and VN100 returns ({rng(w_heur, 4)}); the ratio-spread proxy P_ratio = B_t − A_t; and the "
              "residual P_res of an OLS regression of B_t on A_t (R² of "
              f"{rng(ols_r2, 3)}, slope {rng(ols_b, 3)}). For P_heur the denominator 1 − w_heur is only "
              f"{rng([1 - x for x in w_heur], 4)}, which multiplies the numerator by {rng(amp, 0)}; this is a numerically unstable "
              "construction, and its daily standard deviation "
              f"({f(PROXY['1D']['sd_Pheur'], 4)}) is more than ten times that of P_cap ({f(PROXY['1D']['sd_Pcap'], 4)})."),
        ('h2', '4.3 Weight drift'),
        ('p1a', "Between semi-annual reviews, constituent capitalizations drift with relative prices. If the true weight w_t differs "
                "from the fixed weight w, the proxy becomes"),
        ('eq', r'\hat{M}_t=\frac{1-w_t}{1-w}M_t+\frac{w_t-w}{1-w}A_t, \qquad (10)'),
        ('p', "so a fraction of large-cap returns leaks into the proxy in proportion to the weight gap. Only one factsheet snapshot "
              "of free-float weights is available, so we do not reconstruct the weight path; Table A2 re-estimates the main "
              "statistics for weights from 0.60 to 0.75."),
        ('h2', '4.4 Reliability thresholds and inference'),
        ('p1a', "The number of boxes falls as s grows, so the DCCA coefficient becomes noisy at large scales. For each sample size we "
                "simulate pairs of Gaussian white noise with correlations of −0.3, 0, 0.3, 0.5, 0.7 and 0.9 (167 replications each, "
                "1,002 per frequency) and compute the mean absolute estimation error on 40 log-spaced scales. The reliability "
                "threshold s_rel is the largest scale below the first scale at which the worst-case error exceeds 0.05; both the "
                "error grid and the 0.05 tolerance are fixed before the empirical analysis. Because returns are heavy-tailed and "
                "volatility-clustered, we repeat the calibration with generalized autoregressive conditional heteroskedasticity "
                "GARCH(1,1) series driven by Student-t innovations with five degrees of freedom (300 simulations)."),
        ('p', "DCCA coefficients at different scales are functionals of the same two series, so treating scales or simulation "
              "replicates as independent observations would overstate precision. All inference therefore resamples the data. A "
              "stationary block bootstrap (Politis and Romano 1994) with a mean block length of about 20 trading days "
              f"({B_REPS} replications for DCCA-based statistics and 1,999 for the Pearson-based regime statistics of Sections 4.6 and "
              "4.7) redraws the joint return series, recomputes every DCCA curve and every derived statistic, and yields percentile "
              "95% intervals and two-sided bootstrap p-values computed as 2 min{(k₋ + 1), (k₊ + 1)}/(B + 1), where k₋ and k₊ count "
              "replicates at or below and at or above zero. Table A5 shows that the interval for the main gap is stable "
              "for mean block lengths from 5 to 60 days. The slope tests in Section 5.5 involve "
              f"{fam} pair-frequency combinations per scale range; we report Holm (1979) family-wise and Benjamini and Hochberg "
              "(1995) false-discovery-rate adjusted p-values within each range."),
        ('h2', '4.5 Scaling regressions'),
        ('p1a', "To test horizon dependence we regress the DCCA coefficient on the log timescale,"),
        ('eq', r'\rho_{XY}(s)=\alpha+\beta\ln s+u(s), \qquad (11)'),
        ('p', "on 30 log-spaced scales between 5 bars and one quarter of the sample (5 to 5,485 bars at M30) and, separately, on the "
              "reliable range s ≤ s_rel. A positive β indicates that co-movement builds up with the horizon, as predicted by the "
              "Epps (1979) effect at short scales and by gradual information diffusion (Hong and Stein 1999) beyond them."),
        ('h2', '4.6 Forbes–Rigobon volatility conditioning'),
        ('p1a', "If y_t = α + βx_t + ε_t with Var(ε_t) = σ²_ε, the correlation ρ = [1 + σ²_ε/(β²σ²_x)]^{−1/2} rises with the "
                "variance of x even when β and σ²_ε are constant. Forbes and Rigobon (2002) correct the high-volatility "
                "correlation as"),
        ('eq', r'\rho^{*}=\frac{\rho_{\mathrm{high}}}{\sqrt{1+\delta\,(1-\rho_{\mathrm{high}}^2)}},\qquad \delta=\frac{\sigma^2_{x,\mathrm{high}}-\sigma^2_{x,\mathrm{low}}}{\sigma^2_{x,\mathrm{low}}}. \qquad (12)'),
        ('p', "The correction requires the conditioning series to be exogenous. This is plausible for the disjoint pair P_cap–VN30, "
              "with VN30 as the conditioning market, but fails by construction for the nested pairs, whose parent contains the "
              "conditioning index; the formal test is therefore restricted to P_cap–VN30. Regime correlations are Pearson "
              "correlations of daily returns, and δ is the relative increase in the variance of VN30 returns, so the correction and "
              "the correlation refer to the same measure. The bootstrap is applied within each regime; we report a 95% interval for "
              "ρ* − ρ_low, a one-sided p-value for the null of no increase and the power to detect an increase of 0.05. Severe "
              "downturns on the HOSE can trigger margin calls and simultaneous selling of large and mid caps, which weakens "
              "exogeneity, so ρ* is interpreted as cross-tier dependence under stress rather than one-way transmission."),
        ('h2', '4.7 Portfolio variance error'),
        ('p1a', "For an equally weighted two-asset portfolio with volatilities σ₁ and σ₂, replacing the regime correlation ρ_r by a "
                "static full-sample correlation ρ_st changes the portfolio variance by the relative error"),
        ('eq', r'\mathrm{RE}=\frac{\rho_{\mathrm{st}}-\rho_{r}}{\tfrac{1}{2}\left(\sigma_1/\sigma_2+\sigma_2/\sigma_1\right)+\rho_{r}}, \qquad (13)'),
        ('p', "evaluated with regime-specific volatilities so that the static and regime cases differ only in the correlation. This "
              "is a closed-form identity; no optimization is involved. Intervals come from the within-regime block bootstrap."),
        ('h2', '4.8 Multifractal extension'),
        ('p1a', "To examine whether scaling differs between small and large fluctuations, we use multifractal DCCA (MF-DCCA; Zhou "
                "2008) with absolute local covariances, which avoids complex-valued moments:"),
        ('eq', r'F_q(s)=\left\{\frac{1}{2N_s}\sum_{\nu=1}^{2N_s}\left|f^2_{XY}(s,\nu)\right|^{q/2}\right\}^{1/q},\qquad q\in[-5,5]\setminus\{0\}. \qquad (14)'),
        ('p', "The generalized exponent h_xy(q) is the slope of ln F_q(s) on ln s over 24 log-spaced scales, and the range "
              "Δh = h_xy(−5) − h_xy(5) measures the strength of multifractality. Because fat tails alone widen Δh, each observed "
              "range is compared with 100 surrogates in which the paired returns are jointly shuffled, which preserves the return "
              "distributions and their contemporaneous correlation but destroys temporal structure. Oświęcimka et al. (2014) show that taking absolute values of local covariances can "
              "create spurious multifractality and propose a sign-preserving alternative; we therefore treat the multifractal "
              "results as descriptive and base no hypothesis test on them."),
        ('h2', '4.9 Computational details'),
        ('p1a', "All computations use R 4.3.3 with the packages stats (base), sandwich 3.1.0 and ggplot2 3.4.4 on an Intel Xeon "
                "processor (2.10 GHz, four cores). OLS fits use the QR decomposition, so no iterative optimization, tolerance or "
                "convergence criterion is involved. Random seeds are fixed (20260924 for the round-one inference, 20261007 for the "
                "decomposition and robustness analyses; the white-noise calibration seeds each simulation by its index). A single "
                "script, run_all.R, reproduces every table and figure; rerunning it yields byte-identical CSV output files. The code and "
                "outputs are provided as Online Resource 1."),
    ]


def T(caption, header, body, note):
    return ('table', (caption, header, body, note))


def results():
    t1d = [DESC[(v, t)] for v in ['VN30', 'VN100', 'VNINDEX', 'Pcap'] for t in TF]
    tab2 = T('Table 2 Descriptive statistics of log returns',
             ['Series', 'Freq.', 'N', 'Mean', 'Std. dev.', 'Skew.', 'Kurt.', 'Jarque–Bera'],
             [[('P_{cap}' if r['index'] == 'Pcap' else r['index']), r['freq'], nint(r['n']), f(r['mean'], 4), f(r['sd'], 4),
               f(r['skew'], 2), f(r['kurtosis'], 2), nint(r['jb']) + '***'] for r in t1d],
             'Kurt. is non-excess kurtosis; P_cap is the mid-cap proxy of Eq. (6); *** p < 0.01. Source: Authors’ calculations '
             'based on HOSE index data (TradingView).')
    tab3 = T('Table 3 Finite-sample reliability thresholds of the DCCA coefficient',
             ['Frequency', 'N', 'Gaussian s_rel', 'Heavy-tailed s_rel'],
             [[TFNAME[t], nint(REL[t]['n']), REL[t]['s_rel'], GARCH[t]['s_rel_garch_t']] for t in TF],
             'Largest scale (bars) at which the worst-case mean absolute error stays below 0.05; Gaussian: 1,002 white-noise '
             'simulations; heavy-tailed: 300 GARCH(1,1)-t(5) simulations. Source: Authors’ calculations.')
    rowsA = [[TFNAME[t], f(AVG[('A', t)]['nested_mean']), f(AVG[('A', t)]['Pcap-VN30']), f(AVG[('A', t)]['gap']), '', nint(AVG[('A', t)]['n'])] for t in TF]
    rowsB = [[TFNAME[t], f(AVG[('B', t)]['nested_mean']), f(AVG[('B', t)]['Pcap-VN30']),
              f(AVG[('B', t)]['gap']) + ' ' + ci(gapB[t]['ci_lo'], gapB[t]['ci_hi']),
              f(Q[t]['cohen_q'], 2) + ' ' + ci(Q[t]['ci_lo'], Q[t]['ci_hi'], 2), nint(AVG[('B', t)]['n'])] for t in TF]
    tab4 = T('Table 4 Average DCCA coefficients of nested and purged pairs',
             ['Frequency', 'Nested pairs', 'P_cap–VN30', 'Gap [95% CI]', 'Cohen’s q [95% CI]', 'N'],
             [['*Panel A: synchronized window, 2017–2024*', '', '', '', '', '']] + rowsA +
             [['*Panel B: full sample, 2014–2025*', '', '', '', '', '']] + rowsB,
             'Averages of ρ(s) over s ≤ s_rel (Table 3, full-sample thresholds in both panels), m = 1; nested pairs: mean of VN30–VNINDEX, VN30–VN100 and VN100–VNINDEX. '
             'Brackets: block-bootstrap 95% intervals. Source: Authors’ calculations.')
    tab5 = T('Table 5 Exact overlap decomposition of the VN30–VN100 DCCA coefficient (Proposition 1)',
             ['Frequency', 'κ', 'Economic ρ_AM', 'Nested ρ_AB', 'Floor ρ̲', 'Mechanical share', 'Sensitivity', 'Floor − ρ_AM'],
             [[TFNAME[t], f(D(t, 'kappa')['estimate']),
               f(D(t, 'rho_econ')['estimate']) + ' ' + ci(D(t, 'rho_econ')['ci_lo'], D(t, 'rho_econ')['ci_hi']),
               f(D(t, 'rho_nested')['estimate']),
               f(D(t, 'floor')['estimate']) + ' ' + ci(D(t, 'floor')['ci_lo'], D(t, 'floor')['ci_hi']),
               f(D(t, 'mech_share')['estimate']) + ' ' + ci(D(t, 'mech_share')['ci_lo'], D(t, 'mech_share')['ci_hi']),
               f(D(t, 'sensitivity')['estimate']) + ' ' + ci(D(t, 'sensitivity')['ci_lo'], D(t, 'sensitivity')['ci_hi']),
               f(fme[t]['estimate']) + ' ' + ci(fme[t]['ci_lo'], fme[t]['ci_hi'])] for t in TF],
             'Quantities of Eqs. (7)–(9) averaged over s ≤ s_rel; A = VN30, B = VN100, M = P_cap. Brackets: block-bootstrap 95% '
             'intervals. Source: Authors’ calculations.')
    pairs6 = ['VN30-VNINDEX', 'VN100-VNINDEX', 'VN30-VN100', 'Pcap-VN30', 'Pheur-VN30', 'Pratio-VN30', 'Pres-VN30']
    lab = lambda p: p.replace('Pcap', 'P_cap').replace('Pheur', 'P_heur').replace('Pratio', 'P_ratio').replace('Pres', 'P_res').replace('-', '–')
    def prow(p):
        a, b = slope('M30', p, 'slope_full'), slope('M30', p, 'slope_rel')
        pv = lambda x: f(x, 3)
        return [lab(p), f(a['estimate'], 4) + ' ' + ci(a['ci_lo'], a['ci_hi'], 4), f(b['estimate'], 4) + ' ' + ci(b['ci_lo'], b['ci_hi'], 4),
                pv(b['p_boot']), pv(b['p_holm']), pv(b['p_bh'])]
    tab6 = T('Table 6 Scaling slopes of DCCA coefficients at the 30-minute frequency',
             ['Pair', 'Full range [95% CI]', 'Reliable range [95% CI]', 'p', 'p (Holm)', 'p (BH)'],
             [prow(p) for p in pairs6],
             f'Slopes of Eq. (11); full range: 30 scales from 5 to 5,485 bars; reliable range: s ≤ {REL["M30"]["s_rel"]}. p-values refer '
             f'to the reliable-range slope; Holm and Benjamini–Hochberg (BH) adjustments are across all {fam} reliable-range tests. '
             'Source: Authors’ calculations.')
    tab7 = T('Table 7 Forbes–Rigobon conditioning of the P_cap–VN30 correlation',
             ['Regime definition', 'ρ_low', 'ρ_high', 'δ', 'ρ*', 'ρ* − ρ_low [95% CI]', 'p', 'Power'],
             [[name, f(r['rho_low']), f(r['rho_high']), f(r['delta'], 2), f(r['rho_star']), f(r['diff']) + ' ' + ci(r['ci_lo'], r['ci_hi']),
               f(r['p_one_sided'], 3), f(r['power_at_0.05'], 2)] for name, r in (('Chronological crises', frA), ('Rolling-volatility quartiles', frB))],
             f'Pearson correlations of daily returns; δ = relative increase in VN30 return variance; p: one-sided bootstrap p-value '
             f'for H0: ρ* ≤ ρ_low; power against an increase of 0.05. Chronological: {nint(frA["n_low"])} calm and {nint(frA["n_high"])} '
             f'crisis days; quartiles: {nint(frB["n_low"])} days per regime. Source: Authors’ calculations.')
    return [
        ('h1', '5 Results'),
        ('h2', '5.1 Summary statistics'),
        ('p1a', "Table 2 reports descriptive statistics of index and proxy returns at the four frequencies."),
        tab2,
        ('p', f"At the daily frequency the standard deviation is highest for P_cap ({f(DESC[('Pcap', '1D')]['sd'], 4)}) and lowest "
              f"for VNINDEX ({f(DESC[('VNINDEX', '1D')]['sd'], 4)}), as expected for the broadest index. All series are negatively "
              f"skewed and leptokurtic, with kurtosis above {int(min(float(DESC[(v, 'M30')]['kurtosis']) for v in ['VN30', 'VN100', 'VNINDEX', 'Pcap']))} "
              "at M30, and the Jarque–Bera test rejects normality everywhere. DCCA and the block bootstrap do not require "
              "Gaussian returns, which is why we use them."),
        ('h2', '5.2 Reliability thresholds'),
        ('p1a', "Table 3 reports the largest timescale at which the DCCA coefficient is estimated with a worst-case error below 0.05."),
        tab3,
        ('p', f"The Gaussian thresholds range from {REL['1D']['s_rel']} days at 1D to {REL['M30']['s_rel']} bars at M30; heavy-tailed "
              "series reduce them by roughly a factor of three. All averages below use the Gaussian thresholds; recomputing them "
              "over the shorter heavy-tailed ranges changes the nested averages to "
              f"{rng([GARCH[t]['nested_avg_conservative'] for t in TF])} and the purged average to "
              f"{rng([GARCH[t]['pcap_avg_conservative'] for t in TF])}, so no conclusion depends on the choice."),
        ('h2', '5.3 Overlap inflation (H1)'),
        ('p1a', "Table 4 compares the average DCCA coefficient of the nested pairs with that of the purged pair, and Fig. 2 shows the "
                "full curves with bootstrap bands."),
        tab4,
        ('p', f"The nested pairs average {rng(nested_all)} at every frequency in both samples, whereas P_cap–VN30 averages "
              f"{rng(pcap_all)}. The gap of {rng(gap_vals[:4])} in the full sample has bootstrap intervals between {f(gap_lo)} and "
              f"{f(gap_hi)}, all excluding zero, and Cohen’s q (Cohen 1988) of {rng(qv, 2)} indicates a large effect on the Fisher scale. "
              f"{'H1 is supported.' if H1_ok else 'H1 is not supported at every frequency.'} The purged coefficient remains high, so "
              "the overlap inflates co-movement that is already strong rather than creating it. The two samples differ by at most "
              f"{f(max(abs(float(AVG[('A', t)]['nested_mean']) - float(AVG[('B', t)]['nested_mean'])) for t in TF), 3)} for the nested mean, "
              "so the result does not depend on the sample window."),
        ('p', "The reason is the structure of the indices rather than market behavior: the VN30 component appears on both sides of "
              "each nested pair, so its variance enters the numerator and the denominator of Eq. (5) and pulls the ratio toward "
              "one. The statistical proxies confirm that the remaining signal must be extracted with capitalization weights: their "
              f"average coefficients with VN30 lie between {f(SC['alt_proxy_mean_rho_range'][0], 2)} and "
              f"{f(SC['alt_proxy_mean_rho_range'][1], 2)}, and they correlate with each other at "
              f"{rng([PROXY[t]['alt_min'] for t in TF] + [PROXY[t]['alt_max'] for t in TF])} but with P_cap at only "
              f"{rng([PROXY[t]['pcap_vs_alt_min'] for t in TF] + [PROXY[t]['pcap_vs_alt_max'] for t in TF])}, so they behave as "
              "amplified residuals rather than as mid-cap returns."),
        ('fig', ('fig2', 'Fig. 2 DCCA coefficients of the nested pairs and P_cap–VN30 by timescale: (a) 1D, (b) M30, (c) H1, (d) H4',
                 'Line and marker types identify the pairs; grey bands are pointwise block-bootstrap 95% intervals; vertical dotted '
                 'lines mark s_rel (Table 3). Source: Authors’ calculations based on HOSE index data (TradingView).')),
        ('h2', '5.4 The mechanical floor (H2)'),
        ('p1a', "Table 5 applies Proposition 1 to the VN30–VN100 pair, and Fig. 3 plots the implied nested coefficient against the "
                "economic correlation."),
        tab5,
        ('p', f"The relative amplitude κ is {rng(kap_v, 2)}: the non-overlapping 32% of VN100 contributes roughly half as much "
              f"detrended variation as the VN30 component. With κ of this size the floor is {rng(floor_v, 3)}, so a VN30–VN100 "
              f"coefficient of about 0.90 would be observed even if mid caps moved independently of large caps. The floor accounts for "
              f"{rng(share, 3)} of the observed coefficient, with bootstrap intervals between {f(share_lo, 3)} and {f(share_hi, 3)}. "
              f"{'H2 is supported.' if H2_ok else 'H2 is not supported at every frequency.'} The point estimates of the floor also exceed "
              f"the economic correlation itself, by {rng([fme[t]['estimate'] for t in TF])}, "
              + ("and the intervals exclude zero at every frequency." if len(fme_pos) == 4 else
                 f"but the bootstrap intervals include zero at {'every frequency' if not fme_pos else 'some frequencies'}, so the "
                 "mechanical floor and the economic correlation are of the same magnitude.")),
        ('p', f"The sensitivity of Eq. (9) is {rng(sens_v, 3)}. An analyst who reads the nested coefficient as a measure of "
              f"large-cap and mid-cap co-movement would therefore need a change of about {f(sum(att) / 4, 0)} times as large in the "
              "economic correlation to see a given change in the index-level number. Fig. 3 shows the consequence: as the "
              "economic correlation moves from −0.5 to 1, the nested coefficient moves only from about 0.87 to 1. The same "
              f"identity applied to full-sample Pearson correlations of daily returns gives a floor of {f(P1['floor'])} and a mechanical "
              f"share of {f(P1['mech_share'])}, so the result is not specific to DCCA."),
        ('fig', ('fig4', 'Fig. 3 Nested VN30–VN100 coefficient implied by Proposition 1 as a function of the economic correlation',
                 'Lines: Eq. (7) evaluated at the average κ of each frequency (Table 5); markers: observed values; dashed horizontal '
                 'line: daily floor; dotted line: 45-degree line; vertical line: zero economic correlation. Source: Authors’ calculations.')),
        ('h2', '5.5 Horizon dependence (H3)'),
        ('p1a', "Table 6 reports scaling slopes at the 30-minute frequency, where the reliable range is widest, with intervals and "
                "multiplicity-adjusted p-values; Table A1 reports the other frequencies."),
        tab6,
        ('p', "Three patterns emerge. First, the VN30–VN100 slope is indistinguishable from zero in both ranges, as Proposition 1 "
              "predicts: the coefficient is bounded below by its floor and almost insensitive to the economic correlation, and both depend on scale only through κ(s) and ρ_AM(s). Second, the broad-market "
              f"pairs VN30–VNINDEX and VN100–VNINDEX have positive reliable-range slopes whose unadjusted intervals exclude zero ({f(slope('M30', 'VN30-VNINDEX', 'slope_rel')['estimate'], 4)} "
              f"and {f(slope('M30', 'VN100-VNINDEX', 'slope_rel')['estimate'], 4)}), which over the reliable range correspond to a rise "
              "of about 0.01 in the coefficient; over the full range, where long scales rest on few boxes, the intervals include "
              "zero. Third, the purged P_cap–VN30 slope is insignificant in both ranges, and the statistical proxies have larger but "
              "imprecise slopes, consistent with amplified noise."),
        ('p', f"Across all {fam} reliable-range tests, {len(sig_rel)} percentile intervals exclude zero ("
              + '; '.join(f"{lab(p)} at {t}" for t, p in sorted(sig_rel)) + "), with unadjusted bootstrap p-values of "
              f"{rng([MT[(t, p, 'slope_rel')]['p_boot'] for t, p in sig_rel])}. After Benjamini–Hochberg adjustment "
              f"{len(bh_rel)} {'remains' if len(bh_rel) == 1 else 'remain'} significant at 5% (smallest adjusted p = {f(bh_min, 3)}), and "
              f"after Holm adjustment {len(holm_rel)} {'remains' if len(holm_rel) == 1 else 'remain'}. No slope is significant at the daily "
              "or 4-hour frequency. "
              + ("H3 is therefore not supported once multiple testing is accounted for. The unadjusted pattern is nevertheless "
                 "the one H3 predicts: positive slopes appear only for broad-market pairs at intraday frequencies, never for "
                 "VN30–VN100, and they are small. This fits the Epps effect, which operates at intraday horizons and involves the "
                 "less liquid constituents that VNINDEX contains and VN30 does not, but the evidence is weak."
                 if not bh_rel else
                 "H3 is therefore partially supported: horizon dependence is confined to broad-market pairs at intraday "
                 "frequencies and it is small. The pattern fits the Epps effect, which operates at intraday horizons and involves "
                 "the less liquid constituents that VNINDEX contains and VN30 does not.")),
        ('h2', '5.6 Volatility regimes and contagion (H4)'),
        ('p1a', "Table 7 reports the unadjusted and Forbes–Rigobon conditioned correlations of P_cap and VN30."),
        tab7,
        ('p', f"Under the chronological definition the raw correlation rises from {f(frA['rho_low'])} in calm years to "
              f"{f(frA['rho_high'])} in crises while the variance of VN30 returns rises by {f(100 * float(frA['delta']), 0)}%. After "
              f"conditioning, the crisis correlation is {f(frA['rho_star'])}, and its difference from the calm level is "
              f"{f(frA['diff'])} (95% interval {f(frA['ci_lo'])} to {f(frA['ci_hi'])}; p = {f(frA['p_one_sided'], 3)}). Under the "
              f"quartile definition, the variance expansion is larger (δ = {f(frB['delta'], 2)}) and the raw correlation rises from "
              f"{f(frB['rho_low'])} to {f(frB['rho_high'])}, but the adjusted correlation ({f(frB['rho_star'])}) again does not exceed "
              f"the calm level (p = {f(frB['p_one_sided'], 3)}). {'H4 is not supported.' if not H4_reject else 'H4 is supported.'} The "
              f"power against an increase of 0.05 is {f(frA['power_at_0.05'], 2)} and {f(frB['power_at_0.05'], 2)}, so moderate "
              "structural increases are unlikely under the first definition, while small ones cannot be excluded under either."),
        ('p', "The mechanism is the heteroskedasticity bias of Eq. (12): a common volatility shock raises the share of variance "
              "explained by the common factor, which lifts the raw correlation without any change in how mid caps respond to large "
              "caps. Both regime definitions are ex post, and the quartile regimes are sorted on VNINDEX, which contains the mid "
              "caps, so the comparison describes in-sample regimes rather than a real-time signal. For the nested pairs, raw "
              "correlations also rise in crises, but the identification condition fails, so we do not test them."),
        ('h2', '5.7 Portfolio variance misstatement (H5)'),
        ('p1a', "Applying Eq. (13) with the regime correlations of Table 7, a static correlation overstates the variance of an "
                f"equally weighted VN30 and P_cap position by {f(reAl['RE_pct'], 2)}% (95% interval {f(reAl['ci_lo'], 2)} to "
                f"{f(reAl['ci_hi'], 2)}) in the chronological calm regime and by {f(reBl['RE_pct'], 2)}% ({f(reBl['ci_lo'], 2)} to "
                f"{f(reBl['ci_hi'], 2)}) in the low-volatility quartile. In turbulent regimes it understates the variance by "
                f"{f(-float(reAh['RE_pct']), 2)}% ({f(-float(reAh['ci_hi']), 2)} to {f(-float(reAh['ci_lo']), 2)}) and "
                f"{f(-float(reBh['RE_pct']), 2)}% ({f(-float(reBh['ci_hi']), 2)} to {f(-float(reBh['ci_lo']), 2)}). "
                f"{'All four intervals exclude zero, so H5 is supported.' if pcap_re_ok else 'Not all intervals exclude zero.'} "
                "For cash portfolios of parent and child indices the daily misstatement is at most "
                f"{f(max(nested_re), 2)}%, because their correlations are bounded below by the mechanical floor and barely move across regimes."),
        ('p', "The asymmetry has a simple source. The variance error is proportional to the gap between the static and the regime "
              "correlation, and the purged correlation varies far more across regimes than the nested ones. The understatement in "
              "crises is small in percentage terms, but it occurs when VN30 return variance has already risen by "
              f"{f(100 * float(frA['delta']), 0)}% to {f(100 * float(frB['delta']), 0)}%. Because P_cap is not investable, these numbers "
              "describe a mid-cap factor exposure, for example one held through a mid-cap index fund, combined with large caps; no "
              "trading strategy is implied, so turnover and transaction costs do not arise."),
        ('h2', '5.8 Multifractal structure'),
        ('p1a', f"The generalized cross-correlation exponent h_xy(2) lies between {f(min(h2), 3)} and {f(max(h2), 3)} for the four pairs, indicating weak persistence. "
                f"The multifractal range Δh is {rng(dh_nest, 3)} for the nested pairs and {rng(dh_pcap, 3)} for P_cap–VN30, but shuffled "
                "surrogates show that most of this range reflects fat tails: the P_cap–VN30 range exceeds the 95th surrogate "
                f"percentile only at {', '.join(surr_pcap_exc) or 'no frequency'}, and the nested pairs exceed it in {surr_nest_exc} of 12 "
                "cases. Fig. 4 contrasts the daily spectra. The multifractal evidence supports only a modest nonlinear structure "
                "and does not change the conclusions above."),
        ('fig', ('fig3', 'Fig. 4 MF-DCCA at the daily frequency: (a) singularity spectra f(α); (b) generalized exponents h_xy(q)',
                 'q ∈ [−5, 5] \\ {0}; daily data. Source: Authors’ calculations based on HOSE index data (TradingView).')),
        ('h2', '5.9 Robustness'),
        ('p1a', "The Appendix collects five robustness checks. Table A1 extends the slope tests to the other frequencies: "
                f"VN30–VNINDEX and VN100–VNINDEX have positive reliable-range slopes at H1 with unadjusted intervals excluding zero ({f(slope('H1', 'VN30-VNINDEX', 'slope_rel')['estimate'], 4)}, "
                f"{ci(slope('H1', 'VN30-VNINDEX', 'slope_rel')['ci_lo'], slope('H1', 'VN30-VNINDEX', 'slope_rel')['ci_hi'], 4)} and "
                f"{f(slope('H1', 'VN100-VNINDEX', 'slope_rel')['estimate'], 4)}, "
                f"{ci(slope('H1', 'VN100-VNINDEX', 'slope_rel')['ci_lo'], slope('H1', 'VN100-VNINDEX', 'slope_rel')['ci_hi'], 4)}) but not at "
                "1D or H4, and the P_cap–VN30 slope is insignificant everywhere. Table A2 varies the capitalization weight from "
                "0.60 to 0.75: a larger weight removes more of the VN30 component and lowers the purged correlation, but the gap to "
                f"the nested pairs stays at or above {f(w_min_gap, 3)}. Table A3 replaces DCCA with the detrending moving-average "
                f"cross-correlation coefficient (DMCA; Kristoufek 2014): the purged coefficient is {rng(dm_pcap)} and the gap "
                f"{rng(dm_gap)}, almost identical to Table 4. Table A4 reports lower-tail dependence at the 5% and 10% quantiles: "
                f"{f(tl('Pcap-VN30', '0.05')['lambda_L'], 2)} for P_cap–VN30 against {f(tl('VN30-VN100', '0.05')['lambda_L'], 2)} for "
                f"VN30–VN100 at 5%, so overlap also inflates joint crash probabilities. Table A5 shows that the bootstrap interval of "
                f"the daily gap stays within {f(blk_lo)} to {f(blk_hi)} for mean block lengths from 5 to 60 days. Finally, the "
                f"daily VN30–VNINDEX average is {f(DETREND[0], 4)}, {f(DETREND[1], 4)} and "
                f"{f(DETREND[2], 4)} for detrending orders 1, 2 and 3."),
        ('h2', '5.10 Summary of hypothesis tests'),
        ('p1a', "Table 8 summarizes the outcome of each hypothesis."),
        T('Table 8 Summary of hypothesis tests',
          ['Hypothesis', 'Test', 'Evidence', 'Outcome'],
          [['H1 Overlap inflation', 'Bootstrap CI of gap', f'Gap {rng(gap_vals[:4])}; all CIs > 0', 'Supported' if H1_ok else 'Not supported'],
           ['H2 Mechanical dominance', 'One-sided test, share > 0.5', f'Share {rng(share)}; lower CI ≥ {f(share_lo)}', 'Supported' if H2_ok else 'Not supported'],
           ['H3 Horizon dependence', 'Slope CIs; Holm and BH', f'{len(sig_rel)} of {fam} unadjusted CIs > 0; {len(bh_rel)} BH- and {len(holm_rel)} Holm-significant', H3_out],
           ['H4 Contagion', 'Forbes–Rigobon, one-sided', f'p = {f(frA["p_one_sided"], 3)} and {f(frB["p_one_sided"], 3)}', 'Supported' if H4_reject else 'Not supported'],
           ['H5 Risk misstatement', 'Bootstrap CI of RE', f'{f(min(float(reAh["RE_pct"]), float(reBh["RE_pct"])), 1)}% to {f(reBl["RE_pct"], 1)}%; CIs exclude 0', 'Supported' if pcap_re_ok else 'Not supported']],
          'All tests at the 5% level; details in Tables 4–7 and Section 5.7. Source: Authors’ calculations.'),
    ]


def discussion():
    return [
        ('h1', '6 Discussion'),
        ('h2', '6.1 Mechanisms'),
        ('p1a', "The results have one common source. When a parent index contains a child index, the child’s variance appears in "
                "both terms of every covariance and in both standard deviations, and Proposition 1 shows that this fixes a floor "
                f"below which the nested coefficient cannot fall. With VN30 holding {f(100 * W30, 0)}% of VN100, the floor is near 0.90, "
                "so the observed 0.99 contains little information about how mid caps move with large caps. The same structure "
                "explains why the VN30–VN100 coefficient is flat across horizons and regimes: it cannot fall below its floor and "
                "responds weakly to the economic correlation, and the floor depends on time and scale only through relative volatility."),
        ('p', "Once the overlap is removed, the remaining dependence behaves like economic co-movement. It is high, because large "
              "and mid caps trade on the same exchange and respond to the same domestic shocks, but it is lower than the "
              "index-level numbers suggest. It rises in crises only as much as the common volatility shock implies, consistent with "
              "the interdependence interpretation of Forbes and Rigobon (2002) rather than with a change in transmission. The weak, "
              "unadjusted intraday horizon dependence of broad-market pairs is consistent with the Epps (1979) effect: VNINDEX contains small stocks, "
              "whose liquidity is more fragile than that of large caps (Chen et al. 2021) and whose prices adjust with a lag, and aggregation over longer horizons removes the lag. Our "
              "index-level data cannot separate this from gradual information diffusion (Hong and Stein 1999)."),
        ('h2', '6.2 Implications'),
        ('p1a', "For risk management, index-level correlations between nested benchmarks should not be used to measure "
                "diversification between size tiers; Eq. (7) shows how to recover the economic correlation from weights and "
                "fluctuation amplitudes, and the variance results show that regime-conditioned correlations matter for mid-cap "
                "exposures but not for blends of parent and child indices. For index providers and the exchange, standalone "
                "non-overlapping segment benchmarks, such as an investable VNMIDCAP fund or mid-cap index futures alongside the "
                "existing VN30 futures, would let investors hold and hedge the mid-cap tier without the hidden overlap. For other "
                "markets with nested architectures, such as the SET50 within the SET100 in Thailand or the IDX30 within the LQ45 in "
                "Indonesia, the identity applies directly, but the size of the floor depends on their weights and volatilities and "
                "must be estimated."),
        ('h2', '6.3 Limitations and future research'),
        ('p1a', "The evidence comes from one exchange, three indices and one decomposition, so the empirical magnitudes should not be "
                "generalized beyond the HOSE. The mid-cap proxy relies on a single factsheet weight; Table A2 shows that the "
                "conclusions hold for weights from 0.60 to 0.75, but validating the proxy against the published VNMIDCAP index and "
                "reconstructing the weight path from semi-annual reviews would sharpen identification. The decomposition was "
                "applied to the VN30–VN100 pair only, because no capitalization weight for VN100 within VNINDEX was available; "
                "with such a weight the same identity extends to the broad-market pairs. Index-level closing prices cannot separate "
                "microstructure frictions from information diffusion, the Forbes–Rigobon test has limited power against small "
                "structural changes, and the regimes are classified ex post, so an out-of-sample evaluation of regime-conditioned "
                "risk budgets is needed before the portfolio results can guide practice."),
        ('h1', '7 Conclusion'),
        ('p1a', "Correlations between nested equity indices contain a mechanical floor that is fixed by index construction. We "
                "derive this floor exactly, at every timescale, and show that on the HOSE it accounts for about nine-tenths of the "
                "VN30–VN100 DCCA coefficient, leaving the index-level number almost insensitive to the economic co-movement between "
                f"large and mid caps. Removing the overlap lowers the correlation with large caps by about {f(sum(gap_vals[:4]) / 4, 2)}, "
                "the remaining dependence shows no evidence of crisis contagion once volatility is conditioned on, and static "
                "correlations misstate the variance of mid-cap exposures by amounts that change sign with the volatility regime. "
                "Risk models and benchmark design in nested index systems should therefore rely on non-overlapping segment "
                "returns or on the decomposition derived here."),
    ]


def appendix():
    lab = lambda p: p.replace('Pcap', 'P_cap').replace('-', '–')
    a1 = []
    for t in ['1D', 'H1', 'H4']:
        for p in ['VN30-VNINDEX', 'VN100-VNINDEX', 'Pcap-VN30']:
            a, b = slope(t, p, 'slope_full'), slope(t, p, 'slope_rel')
            a1.append([TFNAME[t], lab(p), f(a['estimate'], 4) + ' ' + ci(a['ci_lo'], a['ci_hi'], 4),
                       f(b['estimate'], 4) + ' ' + ci(b['ci_lo'], b['ci_hi'], 4), f(b['p_bh'], 3)])
    a2 = [[f(r['w'], 4) + (' (baseline)' if abs(float(r['w']) - W30) < 1e-6 else ''), f(r['rho_mean_1D']), f(r['gap_vs_nested']),
           f(r['slope_M30'], 4), f(r['rho_low_pearson']), f(r['rho_high_pearson'])] for r in WS]
    a3 = [[TFNAME[t]] + [f(DMCA[(t, p)]['rho_dmca_avg']) for p in NESTED + ['Pcap-VN30']] + [f(DMCA[(t, 'Pcap-VN30')]['gap_vs_nested_mean'])] for t in TF]
    a4 = [[lab(p)] + [f(tl(p, u)['lambda_L'], 3) + ' ' + ci(tl(p, u)['ci_lo'], tl(p, u)['ci_hi']) for u in ('0.05', '0.1')]
          for p in ['VN30-VN100', 'VN30-VNINDEX', 'VN100-VNINDEX', 'Pcap-VN30']]
    a5 = [[r['block_length_days'], f(r['gap']), ci(r['ci_lo'], r['ci_hi'])] for r in BLK]
    return [
        ('h1', 'Appendix A Robustness tables'),
        T('Table A1 Scaling slopes at the daily, 1-hour and 4-hour frequencies',
          ['Frequency', 'Pair', 'Full range [95% CI]', 'Reliable range [95% CI]', 'p (BH)'], a1,
          f'Slopes of Eq. (11); reliable ranges from Table 3; BH: Benjamini–Hochberg adjustment across all {fam} reliable-range tests. '
          'Source: Authors’ calculations.'),
        T('Table A2 Sensitivity of the purged correlation to the capitalization weight w',
          ['w', 'Mean ρ (1D)', 'Gap to nested', 'Slope (M30)', 'Calm ρ_low', 'Crisis ρ_high'], a2,
          'Slope (M30): full-range slope of Eq. (11); ρ_low and ρ_high are Pearson correlations in the chronological regimes (Table 7). Source: Authors’ calculations.'),
        T('Table A3 Average DMCA coefficients over the reliable range',
          ['Frequency', 'VN30–VNINDEX', 'VN30–VN100', 'VN100–VNINDEX', 'P_cap–VN30', 'Gap'], a3,
          'Centered moving-average detrending with odd windows matched to the DCCA scales s ≤ s_rel; gap: mean of the nested pairs '
          'minus P_cap–VN30. Source: Authors’ calculations.'),
        T('Table A4 Lower-tail dependence of daily returns',
          ['Pair', 'u = 0.05 [95% CI]', 'u = 0.10 [95% CI]'], a4,
          'Empirical λ_L(u) = P(X ≤ q_X(u), Y ≤ q_Y(u))/u; block-bootstrap intervals. Source: Authors’ calculations.'),
        T('Table A5 Sensitivity of the daily gap interval to the bootstrap block length',
          ['Mean block length (days)', 'Gap', '95% CI'], a5,
          'Gap between the nested-pair mean and P_cap–VN30 (Table 4, Panel B, 1D); bootstrap draws are separate from Table 4, so the intervals differ by Monte Carlo error. Source: Authors’ calculations.'),
    ]


TABLE1 = T('Table 1 Prior studies of multiscale and crisis co-movement and the gap addressed here',
           ['Study', 'Market and data', 'Method', 'Overlap treated?', 'Volatility conditioning?', 'Main finding'],
           TABLE1_ROWS, TABLE1_NOTE)


def body():
    return (introduction() + [('h1', '2 Literature review and hypothesis development')] + LIT_INTRO + LIT_SECTIONS(TABLE1)
            + hypotheses() + institutions_data() + methodology() + results() + discussion())
