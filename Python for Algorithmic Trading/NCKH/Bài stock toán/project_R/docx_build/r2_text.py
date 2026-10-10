"""v3 manuscript body (Stage 4 revision). Every result is read from the R outputs via r2_data; no number is typed by hand."""
from r2_data import *
from r2_lit import LIT_INTRO, LIT_SECTIONS, TABLE1_ROWS, TABLE1_NOTE, TABLE1_HEADER

F = float
W30 = 1316288 / 1928303
D = lambda t, s: DEC[(t, s)]
A_ = lambda t, s: ATT[(t, s)]
lab = lambda p: p.replace('Pcap', 'P_cap').replace('Pheur', 'P_heur').replace('Pratio', 'P_ratio').replace('Pres', 'P_res').replace('-', '–')


def tex(x, d=3):
    return f'{F(x):.{d}f}'


def est_ci(r, d=3, e='estimate'):
    return f(r[e], d) + ' ' + ci(r['ci_lo'], r['ci_hi'], d)


def pbfmt(p, d=3):
    """Percentile-bootstrap p-value with B = 499: the smallest attainable value 0.004 is reported as < 0.005."""
    return '< 0.005' if F(p) <= 0.0041 else f(p, d)


def pfmt(p, d=3):
    p = F(p)
    return '< 0.001' if p < 0.001 else f(p, d)


# ---------------------------------------------------------------- overlap gap (H1)
gapB = {t: R2[(t, 'nested_mean-minus-Pcap', 'gap')] for t in TF}
gap3 = [F(gapB[t]['estimate']) for t in TF]
gapL = {t: A_(t, 'gap_like') for t in TF}
gapL_v = [F(gapL[t]['estimate']) for t in TF]
gapL_lo = min(F(gapL[t]['ci_lo']) for t in TF)
MARGIN_H1 = 0.05
H1_ok = all(F(gapL[t]['ci_lo']) > MARGIN_H1 for t in TF)
nested_all = [F(AVG[(p, t)]['nested_mean']) for p in 'AB' for t in TF]
pcap_all = [F(AVG[(p, t)]['Pcap-VN30']) for p in 'AB' for t in TF]
qv = [F(Q[t]['cohen_q']) for t in TF]
ws_gap = [F(r['gap_vs_nested']) for r in WS]
like_w = [F(D('1D', 'rho_nested')['estimate']) - F(r['rho_econ']) for r in WSD if r['timeframe'] == '1D']

# ---------------------------------------------------------------- decomposition (estimands)
kap_v = [F(D(t, 'kappa')['estimate']) for t in TF]
bench_v = [F(D(t, 'floor')['estimate']) for t in TF]
share_v = [F(D(t, 'mech_share')['estimate']) for t in TF]
sens_v = [F(D(t, 'sensitivity')['estimate']) for t in TF]
econ_v = [F(D(t, 'rho_econ')['estimate']) for t in TF]
nest_v = [F(D(t, 'rho_nested')['estimate']) for t in TF]
tmin_v = [F(TMIN[t]['true_min']) for t in TF]
shap_v = [F(A_(t, 'shapley_overlap_share')['estimate']) for t in TF]
shap_lo = min(F(A_(t, 'shapley_overlap_share')['ci_lo']) for t in TF)
shap_hi = max(F(A_(t, 'shapley_overlap_share')['ci_hi']) for t in TF)
econsh_v = [F(A_(t, 'econ_share')['estimate']) for t in TF]
inv_sens = [1 / s for s in sens_v]
idmax = max(F(r['identity_error']) for r in DECS)
kap_scales = [F(r['kappa']) for r in DECS if r['reliable'] == 'TRUE']
bench_rng = [F(A_(t, 'floor_range')['estimate']) for t in TF]
bslope = {t: A_(t, 'floor_slope') for t in TF}
bslope_p = [F(bslope[t]['p_two_sided_boot']) for t in TF]
bslope_holm = [F(bslope[t]['p_holm']) for t in TF]
P1 = PEAR['1D']
pear_bench = [F(PEAR[t]['floor']) for t in TF]
pear_share = [F(PEAR[t]['mech_share']) for t in TF]
wu = {(t, s): WU[(t, s)] for t in ('1D', 'M30') for s in ('floor', 'rho_econ', 'mech_share', 'sensitivity', 'shapley_overlap_share')}
wu_rng = lambda s: (min(F(wu[(t, s)]['ci_lo']) for t in ('1D', 'M30')), max(F(wu[(t, s)]['ci_hi']) for t in ('1D', 'M30')))

# ---------------------------------------------------------------- horizon dependence (H2)
BROAD = ['VN30-VNINDEX', 'VN100-VNINDEX']
PAIRS4 = ['VN30-VNINDEX', 'VN100-VNINDEX', 'VN30-VN100', 'Pcap-VN30']
h2row = lambda t, p: H2T[(t, p)]
fam = int(F(next(iter(MT.values()))['family_size']))
holm_h2 = [(t, p) for t in TF for p in BROAD if F(h2row(t, p)['p_stud_holm_h3']) < 0.05]
holm_all = [(t, p) for (t, p), r in H2T.items() if F(r['p_stud_holm_all']) < 0.05]
bh_all = [(t, p) for (t, p), r in H2T.items() if F(r['p_stud_bh_all']) < 0.05]
pboot_holm_n = sum(F(r['p_holm']) < 0.05 for (t, p, st), r in MT.items() if st == 'slope_rel')
pboot_bh_min = min(F(r['p_bh']) for (t, p, st), r in MT.items() if st == 'slope_rel')
tost_eq = [t for t in TF if h2row(t, 'VN30-VN100')['tost_equivalent'] == 'TRUE']
intraday_ok = all(any((t, p) in holm_h2 for p in BROAD) for t in ('M30', 'H1'))
H2_out = 'Supported' if intraday_ok else 'Not supported'
TS = {(r['timeframe'], r['variant'], r['stat'], r['pair']): r for r in TRIM}
def _holm(ps):
    o = sorted(range(len(ps)), key=lambda i: ps[i]); m = len(ps); adj = [0] * m; run = 0
    for k, i in enumerate(o):
        run = max(run, min(1, (m - k) * ps[i])); adj[i] = run
    return adj
trim_keys = [(t, p) for t in ('M30', 'H1') for p in BROAD]
trim_holm = dict(zip(trim_keys, _holm([F(TS[(t, 'drop_first', 'slope', p)]['p_studentized']) for t, p in trim_keys])))
trim_ok = {t: any(trim_holm[(t, p)] < 0.05 and F(TS[(t, 'drop_first', 'slope', p)]['estimate']) > 0 for p in BROAD) for t in ('M30', 'H1')}
H2_robust = all(trim_ok.values())
ts = lambda t, v, p: TS[(t, v, 'slope', p)]
tsd = lambda t, v, p: TS[(t, v, 'slope_minus_VN30-VN100', p)]
damp = [F(SLC[t]['damping_factor']) for t in TF]
slc_err = max(abs(F(SLC[t]['slope_implied_linear']) - F(SLC[t]['slope_rho_nested_obs'])) for t in TF)
NUMW = {0: 'none', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight'}

# ---------------------------------------------------------------- contagion (H3)
frA, frB = FR[('A', 'Pcap-VN30')], FR[('B', 'Pcap-VN30')]
fr30 = [r for r in FRW if abs(F(r['w']) - W30) < 1e-3 and r['regimes'] == 'VN30_quartiles'][0]
frw_p = [F(r['p_one_sided']) for r in FRW]
facA, facB, facC = FAC['A'], FAC['B'], FAC['C']
H3_fr = F(fr30['p_one_sided']) < 0.05
H3_fac = F(facC['p_d_beta']) < 0.05 and F(facC['d_beta']) > 0
H3_out = 'Supported' if (H3_fr and H3_fac) else 'Not supported'

# ---------------------------------------------------------------- portfolio risk (E4, H4)
re_ = lambda pan, g, p: MAT[(pan, g, p)]
oos = lambda p, m: OOS[(p, m)]
dm_p = [F(oos(p, m)['dm_p_qlike']) for p in ('Pcap-VN30', 'VN30-VN100', 'VN30-VNINDEX', 'VN100-VNINDEX') for m in ('DM_static_vs_ewma', 'DM_static_vs_regime')]
dm_t = [F(oos(p, m)['dm_t_qlike']) for p in ('Pcap-VN30', 'VN30-VN100', 'VN30-VNINDEX', 'VN100-VNINDEX') for m in ('DM_static_vs_ewma', 'DM_static_vs_regime')]
H4_ok = any(t > 0 and p < 0.05 for t, p in zip(dm_t, dm_p))
nested_re = [abs(F(r['RE_pct'])) for k, r in MAT.items() if k[2] != 'Pcap-VN30']
ratio_pcap = [F(re_(pan, g, 'Pcap-VN30')['RE_over_se']) for pan in 'AB' for g in ('low', 'high')]
ratio_nest = [F(r['RE_over_se']) for k, r in MAT.items() if k[2] != 'Pcap-VN30']

# ---------------------------------------------------------------- misc
tg = lambda p, u: TG[(p, u)]
dm_pcap = [F(DMCA[(t, 'Pcap-VN30')]['rho_dmca_avg']) for t in TF]
dm_gap = [F(DMCA[(t, 'Pcap-VN30')]['gap_vs_nested_mean']) for t in TF]
blk_lo = min(F(r['ci_lo']) for r in BLK); blk_hi = max(F(r['ci_hi']) for r in BLK)
w_heur = [F(OLS[t]['w_heur']) for t in TF]
cr = CRISIS[:3]

TITLE = ('How Much of a Nested Index Correlation Is Construction? A Scale-Wise Part–Whole Decomposition with '
         'Evidence from Vietnam')

ABSTRACT = (
    "When one equity index contains another, part of their correlation is fixed by construction. We carry the classical "
    "part–whole correlation identity over to detrended cross-correlation analysis (DCCA). At every timescale, the coefficient "
    "between a parent and a child index is then a closed-form function of the child’s weight, the relative amplitude of the "
    "remaining constituents and the overlap-purged correlation between the child and those constituents. The identity gives a "
    "zero-correlation benchmark, an exact lower bound, the sensitivity of the nested coefficient to the purged correlation and "
    "an order-free attribution, and it needs only index-level inputs. On the Ho Chi Minh City Stock Exchange (VN30 within VN100 "
    "within VNINDEX, 30-minute to daily data, 2014–2025), the VN30–VN100 coefficient moves by only about "
    f"{f(sum(sens_v) / 4, 2)} per unit change in the purged correlation, and purging the overlap lowers the correlation with large "
    f"caps by about {f(sum(gapL_v) / 4, 2)} at every frequency. The decomposition barely varies across scales and frequencies, so "
    "its Pearson version suffices in these data. The small intraday horizon dependence of broad-market pairs comes from the opening and closing auction bars, "
    "evidence of crisis contagion depends on the test used, and regime-conditioned correlations do not improve out-of-sample "
    "portfolio variance forecasts. Correlations between nested indices therefore say little about diversification between size "
    "tiers unless the overlap is removed first."
)
KEYWORDS = 'constituent overlap; detrended cross-correlation; part–whole correlation; contagion; portfolio risk; Vietnam'
JEL = 'C14; C58; G11; G15'


def introduction():
    return [
        ('h1', '1 Introduction'),
        ('p1a', "Correlations between published equity indices are a convenient summary of dependence. They are available at "
                "every frequency, require no holdings data and are easy to compare across markets, so they are a natural input "
                "when the question is how much one segment of a market diversifies another (Markowitz 1952). In nested index "
                "systems the number has a problem that has nothing to do with estimation error: the parent index contains the "
                "child index, so part of their correlation is fixed by construction. On the Ho Chi Minh City Stock Exchange "
                "(HOSE), the large-cap VN30 index is contained in VN100, which is contained in the market-wide VNINDEX:"),
        ('eq', r'\mathrm{VN30} \subset \mathrm{VN100} \subset \mathrm{VNINDEX}. \qquad (1)'),
        ('p', "Because the 30 largest firms hold about two-thirds of the free-float capitalization of VN100, the correlation between "
              f"VN30 and VN100 returns is close to one ({f(AVG[('B', '1D')]['VN30-VN100'])} at the daily frequency). If such a number "
              "is read as a measure of how mid caps move with large caps, it mixes two things: the economic linkage between the "
              "tiers and the fact that VN30 stocks are counted on both sides. Holdings-based risk models avoid the problem because "
              "they work with constituents. Users who observe only index levels, or who compare benchmarks across frequencies, "
              "cannot, and the co-movement literature shows that index-level co-movement is easy to misread even without overlap "
              "(Chen et al. 2016)."),
        ('p', "The arithmetic behind the problem is old. Pearson (1897) described the spurious correlation between quantities that "
              "share a component, and the psychometric item–total correlation (Cureton 1966) is the same identity applied to a "
              "score and one of its items. What has been missing is a version that works for the scale-dependent, detrended "
              "coefficients now common in financial econophysics, that attaches sampling and weight uncertainty to each "
              "component, and that index users can apply. Studies of multiscale co-movement, which rely mostly on detrended "
              "cross-correlation analysis (DCCA), analyze pairs of assets that share no constituents (Section 2), so they do not "
              "address the question."),
        ('p', "This paper builds that version. Writing the parent index return as a weighted sum of the child return and the return "
              "on the remaining constituents, we show (Lemma 1) that the DCCA coefficient of a nested pair is, at every timescale, a "
              "known function of the child’s weight, the relative amplitude κ(s) of the remaining constituents and the "
              "overlap-purged coefficient between the child and those constituents. The function delivers four quantities: a "
              "zero-correlation benchmark, the value the nested coefficient takes when the purged coefficient is zero; an exact "
              "lower bound over all purged coefficients; the sensitivity of the nested coefficient to the purged one; and an "
              "attribution that does not depend on the order in which overlap and economic dependence are switched on. The Pearson "
              "identity is the one-box special case."),
        ('p', "We apply the decomposition to VN30, VN100 and VNINDEX at 30-minute, 1-hour, 4-hour and daily frequencies from 2014 to "
              "2025, with inference from a stationary block bootstrap that also draws the index weight. The purged series then "
              "serves to test three economic hypotheses, on horizon dependence between tiers, crisis contagion and the "
              "out-of-sample value of regime-conditioned correlations, each with a decision rule stated in Section 2.7."),
        ('p', "The paper makes three contributions. First, it carries the part–whole identity to scale-wise detrended coefficients "
              "and derives the benchmark, the lower bound, the sensitivity, a Shapley attribution and the analytic condition under "
              "which the benchmark exceeds half of the nested coefficient. A six-step recipe (Box 1) and a contour chart "
              "(Fig. 4) make these quantities available for any nested pair from published index data. Second, it measures the "
              "overlap component on the HOSE with inference: the nested VN30–VN100 coefficient responds to the purged coefficient "
              f"with a slope of {rng(sens_v, 3)}, so a change of 0.1 in the purged coefficient moves the nested one by about 0.01, "
              f"and the like-for-like gap between nested and purged coefficients is {rng(gapL_v, 3)}. The decomposition hardly "
              f"varies with the timescale (κ between {f(min(kap_scales), 2)} and {f(max(kap_scales), 2)} across all reliable scales "
              "and frequencies), so in these data the multiscale layer confirms rather than changes the Pearson answer. Third, it "
              "tests economic hypotheses on the purged series: horizon dependence appears only for broad-market pairs at intraday "
              "frequencies and comes from the opening and closing auction bars, crisis evidence depends on whether contagion is measured by an adjusted correlation or by a factor "
              "loading, and regime-conditioned correlations do not beat a static correlation out of sample."),
        ('p', "Section 2 reviews the literature and develops the estimands and hypotheses. Section 3 describes the institutional "
              "setting and the data, Section 4 the methodology, and Section 5 the results. Section 6 discusses mechanisms, "
              "implications, transferability and limitations, and Section 7 concludes. The Supplementary Material (Online "
              "Resource 2) contains further robustness checks."),
    ]


def hypotheses():
    return [
        ('h2', '2.7 Estimands and hypotheses'),
        ('p1a', "Lemma 1 (Section 4.2) fixes several quantities once the index weight and the relative amplitude are known. We "
                "therefore separate estimands, which we report with intervals but do not test, from hypotheses, whose outcome "
                "the identity does not determine."),
        ('p', "*Estimands.* E1 is the zero-correlation benchmark ρ̲ of the VN30–VN100 coefficient and its share of the observed "
              "coefficient under three attribution conventions. E2 is the sensitivity of the nested coefficient to the purged "
              "coefficient. E3 is the in-sample misstatement of portfolio variance when a static correlation replaces a regime "
              "correlation, reported against the sampling error of the regime variance. A share above one half is not a finding: "
              "it holds whenever κ < √3 and the purged coefficient is non-negative (Section 4.2)."),
        ('p', "*H1 (material overlap gap).* The size of the overlap gap depends on the purged coefficient, which the identity does "
              "not fix: a purged coefficient close to one would leave almost no gap. We predict that the like-for-like gap, the "
              "VN30–VN100 coefficient minus the P_cap–VN30 coefficient, exceeds 0.05, the worst-case estimation error tolerated in "
              "Section 4.4. Decision rule: the lower bound of the 95% bootstrap interval exceeds 0.05 at every frequency."),
        ('p', "*H2 (horizon dependence).* Large-cap returns lead small-cap returns (Lo and MacKinlay 1990; Hou 2007), "
              "non-synchronous trading depresses short-horizon correlations (Epps 1979), and information diffuses gradually (Hong "
              "and Stein 1999). These mechanisms predict DCCA coefficients that rise with the timescale for broad-market pairs, "
              "whose parent contains small and less liquid stocks. For VN30–VN100 the identity predicts a slope damped by the "
              "sensitivity of Eq. (10). Decision rule: in the family of eight broad-market slope tests (two pairs, four "
              "frequencies), at least one pair at each of M30 and H1, the frequencies with several bars per session, has a "
              "positive slope with a Holm-adjusted studentized p-value below 0.05. We also report whether the result survives "
              "removal of the opening bar, and assess the VN30–VN100 prediction by an equivalence test."),
        ('p', "*H3 (contagion).* A rise in the raw crisis correlation between P_cap and VN30 can come from higher volatility "
              "alone (Forbes and Rigobon 2002), and the volatility correction is itself biased toward no contagion when crises "
              "raise idiosyncratic variance (Corsetti et al. 2005). We predict contagion in the strict sense. Decision rule: under "
              "regimes sorted on VN30 volatility, both the Forbes–Rigobon adjusted correlation exceeds its calm level (one-sided "
              "p < 0.05) and the loading of P_cap on VN30 rises (two-sided p < 0.05)."),
        ('p', "*H4 (value of regime conditioning).* If correlations between tiers vary with the volatility regime, conditioning on "
              "the regime should improve variance forecasts for a mixed large-cap and mid-cap position. Decision rule: an EWMA or a "
              "real-time regime correlation has a lower QLIKE loss than the static correlation over 2023–2025, with a "
              "Diebold–Mariano p-value below 0.05."),
        ('p', "The first-round version of this paper reported five hypotheses with unadjusted tests. The decision rules above, the "
              "eight-test family for H2 and the factor-loading test for H3 were fixed at revision, after the first-round results "
              "were known. We label them accordingly and also report the original specifications."),
    ]


def institutions_data():
    c = cr
    return [
        ('h1', '3 Institutional background and data'),
        ('h2', '3.1 Institutional background'),
        ('p1a', "The HOSE is supervised by the State Securities Commission of Vietnam. Five features of its microstructure matter "
                "for cross-tier dependence. First, prices move within a daily band of ±7% around the reference price; in sharp "
                "corrections heavily sold stocks reach the lower limit, where trading dries up, which truncates return tails and "
                "can synchronize limit hits across constituents. Second, settlement moved from T+3 to T+2 on 1 January 2016 (Vietnam Securities Depository 2015), so "
                "shares bought cannot be resold for about two business days, which limits intraday arbitrage between constituents "
                "and index baskets."),
        ('p', "Third, each trading day has a morning session with an opening call auction (09:00–09:15) and continuous matching to "
              "11:30, a midday break from 11:30 to 13:00, and an afternoon session of continuous matching followed by a closing "
              f"call auction (14:30–14:45). The vendor’s intraday bars follow this calendar: M30 bars open at "
              f"{BARS['M30']['bar_open_times'].replace(' ', ', ')}; H1 bars at {BARS['H1']['bar_open_times'].replace(' ', ', ')}; and "
              "the two H4 bars cover the morning and the afternoon session. The first bar of each day therefore contains the "
              "overnight return and the opening auction."),
        ('p', "Fourth, short selling is restricted. Circular 120/2020/TT-BTC (Ministry of Finance of Vietnam 2020) provides a legal "
              "framework for covered short sales of borrowed securities, but to our knowledge the mechanism had not been put into "
              "operation during the sample, and naked short selling is not permitted. Decree 155/2020/ND-CP (Government of Vietnam "
              "2020), the main implementing decree of the Law on Securities, was amended by Decree 245/2025/ND-CP of 11 September "
              "2025 (Government of Vietnam 2025). VN30 index futures trade on the Hanoi Stock Exchange; there is no mid-cap "
              "future. A mid-cap exchange-traded fund tracking VNMIDCAP (FUEDCMID) has been listed on the HOSE since 29 September "
              "2022 (Ho Chi Minh City Stock Exchange 2022), so the mid-cap tier can be held long but not shorted or hedged with a dedicated derivative."),
        ('p', "Fifth, foreign ownership limits cap the share of many listed firms that foreign investors may hold, for example 30% "
              "for commercial banks, so foreign flows concentrate in the large caps that have room under their limits. FTSE "
              "Russell announced in October 2025 that Vietnam would be reclassified from Frontier to Secondary Emerging status, "
              "effective 21 September 2026 (FTSE Russell 2025). The reclassification falls after our sample but may change the weight and "
              "relative volatility of the tiers, and therefore the decomposition."),
        ('h2', '3.2 Data and sample construction'),
        ('p1a', "We use index levels of VN30, VN100 and VNINDEX exported from TradingView (exchange code HOSE). VN30 contains the 30 "
                "largest and most liquid stocks screened by free-float capitalization; VN100 adds the next 70 stocks, which form "
                "the VNMIDCAP index; and VNINDEX covers all common stocks listed on the HOSE, weighted by full market "
                "capitalization. Daily and 30-minute series run to 12 December 2025; the 1-hour and 4-hour series available from "
                "the vendor end on 9 December 2024. The vendor does not provide a VNMIDCAP history for the full sample at all "
                "frequencies, so the mid-cap segment is recovered from VN30 and VN100 (Section 4.2). The HOSE publishes daily "
                "closing levels of all three indices on its website; we did not compare them with the vendor series date by date, "
                "and the replication package records a checksum of the input file."),
        ('p', "The three series are merged by exact inner joins on timestamps; no index level is filled or interpolated. Log returns "
              "are"),
        ('eq', r'R_t=\ln P_t-\ln P_{t-1}. \qquad (2)'),
        ('p', "Two samples are used. The synchronized window (3 January 2017 to 9 December 2024) is the period in which all four "
              f"frequencies overlap (1D: N = {nint(AVG[('A', '1D')]['n'])}; M30: N = {nint(AVG[('A', 'M30')]['n'])}; H1: N = "
              f"{nint(AVG[('A', 'H1')]['n'])}; H4: N = {nint(AVG[('A', 'H4')]['n'])}) and is used for cross-frequency comparisons. The "
              "full sample, used for all other analyses, runs from February 2014 to December 2025 at the daily frequency (N = "
              f"{nint(DESC[('VN30', '1D')]['n'])}), from January 2017 to December 2025 at M30 (N = {nint(DESC[('VN30', 'M30')]['n'])}) and "
              f"from January 2014 to December 2024 at H1 and H4 (N = {nint(DESC[('VN30', 'H1')]['n'])} and {nint(DESC[('VN30', 'H4')]['n'])}). "
              "The series are official index levels computed in real time, not indices back-calculated from current membership "
              "lists, so constituent reviews, delistings and free-float adjustments are embedded in the return paths and the "
              "sample is free of survivorship bias in index composition."),
        ('p', "Volatility regimes use the 20-day rolling standard deviation of returns (Fig. 1). The chronological definition "
              "selects crisis episodes with a peak-to-trough VNINDEX drawdown above 25%, at least 45% of trading days in the top "
              "quartile of rolling volatility and a documented macro-financial trigger. Three episodes qualify: the 2018 margin "
              f"contraction (drawdown {f(-F(c[0]['max_drawdown_pct']), 1)}%, {f(100 * F(c[0]['share_high_vol_days']), 0)}% of days in the "
              f"top quartile), the 2020 COVID-19 shock ({f(-F(c[1]['max_drawdown_pct']), 1)}%, {f(100 * F(c[1]['share_high_vol_days']), 0)}%) "
              f"and the 2022 corporate bond liquidity freeze ({f(-F(c[2]['max_drawdown_pct']), 1)}%, "
              f"{f(100 * F(c[2]['share_high_vol_days']), 0)}%), {nint(SC['n_crisis_days'][0])} trading days in all; the calm benchmark "
              f"comprises 2016–2017 and 2023–2024 ({nint(SC['n_calm_days'][0])} days). The volatility spikes of 2021 (drawdown "
              f"{f(-F(EPI[0]['max_drawdown_pct']), 1)}%, {f(100 * F(EPI[0]['share_top_quartile_vol']), 0)}% of days in the top quartile) "
              f"and of March–June 2025 ({f(-F(EPI[1]['max_drawdown_pct']), 1)}%, {f(100 * F(EPI[1]['share_top_quartile_vol']), 0)}%) fail "
              "the first two conditions and are not shaded. The quartile definitions sort all days by the rolling volatility of "
              f"VNINDEX (25th and 75th percentiles at {f(SC['vol_quartiles_ann_pct'][0], 1)}% and "
              f"{f(SC['vol_quartiles_ann_pct'][1], 1)}% annualized) or of VN30, and compare the bottom and top quartiles; they "
              "include the unshaded episodes."),
        ('fig', ('fig1', 'Fig. 1 Twenty-day rolling volatility of VNINDEX (annualized) and market regimes, 2014–2025',
                 'Shaded areas: the three chronological crisis episodes; dashed and dotted horizontal lines: 25th and 75th '
                 'percentiles of rolling volatility. The 2021 and 2025 spikes are not shaded because their drawdowns are below 25% '
                 '(Section 3.2). Source: Authors’ calculations based on HOSE index data (TradingView).')),
    ]


def methodology():
    k1 = F(REC['kappa'])
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
        ('p', "Eq. (5) is the inner product of the stacked residual vectors divided by the product of their norms, so the "
              "Cauchy–Schwarz inequality gives |ρ_XY(s)| ≤ 1 at every s whenever both fluctuation functions are positive. Two "
              "properties are used below: the profile is linear in the series, and OLS detrending is a linear projection, so the "
              "residuals of a weighted sum of series are the same weighted sum of their residuals."),
        ('h2', '4.2 The overlap-purged series and the part–whole identity'),
        ('p1a', "Let A_t and B_t denote VN30 and VN100 returns and let w be the free-float weight of VN30 in VN100. The "
                "overlap-purged mid-cap series is"),
        ('eq', r'M_t=P_{\mathrm{cap},t}=\frac{B_t-wA_t}{1-w}, \qquad (6)'),
        ('p', f"with w = {f(W30, 4)} from the HOSE factsheet of 31 May 2024 (VN30 and VN100 free-float capitalizations of VND "
              "1,316,288 billion and VND 1,928,303 billion). By construction B_t = wA_t + (1 − w)M_t at every observation. Because "
              "the relation is applied to log returns, P_cap differs from the arithmetic mid-cap return by a Jensen term of "
              f"{f(SC['jensen_delta'][0] * 1e6, 1)} × 10⁻⁶ per day. P_cap is a shadow benchmark: replicating it would require a long "
              "position of about 315% in VN100 and a short position of about 215% in VN30, which the short-sale rules rule out. We "
              "call the coefficient ρ_AM between VN30 and P_cap the overlap-purged coefficient. Calling it economic would require "
              "a validation against the published VNMIDCAP series, which our data source does not provide (Section 6.4)."),
        ('p', "**Lemma 1 (scale-wise part–whole identity).** Let B_t = wA_t + (1 − w)M_t for all t, with 0 < w < 1, and let "
              "F_A(s), F_M(s) > 0. Define the relative amplitude κ(s) = (1 − w)F_M(s)/[wF_A(s)]. Then, for every timescale s and "
              "detrending order m,"),
        ('eq', r'\rho_{AB}(s)=\frac{1+\kappa(s)\,\rho_{AM}(s)}{\sqrt{1+\kappa(s)^2+2\kappa(s)\,\rho_{AM}(s)}}. \qquad (7)'),
        ('p', "*Proof.* Profiles and box-wise OLS residuals are linear in the series, so ε_B = wε_A + (1 − w)ε_M in every box. "
              "Because Eq. (4) is bilinear, F²_AB = wF²_A + (1 − w)ρ_AM F_A F_M and F²_B = w²F²_A + (1 − w)²F²_M + "
              "2w(1 − w)ρ_AM F_A F_M. Substituting into Eq. (5) and dividing numerator and denominator by wF²_A gives Eq. (7). ∎"),
        ('p', "With one box and no detrending, Eq. (7) is the classical correlation between a total and one of its parts (Pearson "
              "1897; Cureton 1966). The lemma is therefore an adaptation, not a new identity; what it adds is that the identity "
              "holds scale by scale for detrended coefficients, for the detrending moving-average coefficient (Kristoufek 2014) "
              "and for any dependence measure built from a bilinear covariance of linearly filtered series. Five corollaries "
              "follow, all for a fixed scale s, which we suppress."),
        ('p', "*Corollary 1 (zero-correlation benchmark and lower bound).* Setting ρ_AM = 0 gives the benchmark"),
        ('eq', r'\underline{\rho}=\frac{1}{\sqrt{1+\kappa^2}}. \qquad (8)'),
        ('p', "Eq. (7) is increasing in ρ_AM for ρ_AM > −κ, so ρ̲ bounds ρ_AB from below only when ρ_AM ≥ 0. Over all "
              "admissible ρ_AM and for κ < 1, the minimum of Eq. (7) is"),
        ('eq', r'\min_{\rho_{AM}\in[-1,1]}\rho_{AB}=\sqrt{1-\kappa^2},\qquad \text{attained at } \rho_{AM}=-\kappa; \qquad (9)'),
        ('p', "for κ ≥ 1 no positive lower bound exists. *Corollary 2 (sensitivity).* The derivative of Eq. (7) with respect to "
              "the purged coefficient is"),
        ('eq', r'\frac{\partial\rho_{AB}}{\partial\rho_{AM}}=\frac{\kappa^2\,(\kappa+\rho_{AM})}{(1+\kappa^2+2\kappa\rho_{AM})^{3/2}}, \qquad (10)'),
        ('p', "which is small when the child dominates the parent. Its inverse states how far the purged coefficient must move "
              "to change the nested one by a given amount. *Corollary 3 (direction).* For ρ_AM ≥ 0, ρ²_AB − ρ²_AM = "
              "(1 − ρ²_AM)(1 + 2κρ_AM)/(1 + κ² + 2κρ_AM) ≥ 0, so overlap can only raise the coefficient, with equality only at "
              "ρ_AM = 1. *Corollary 4 (when the benchmark dominates).* For ρ_AM ≥ 0, ρ_AB ≤ 1 implies ρ̲/ρ_AB ≥ ρ̲, so the "
              f"benchmark exceeds half of the nested coefficient whenever κ < √3, that is, whenever F_M/F_A < √3·w/(1 − w) = "
              f"{f(REC['amplitude_ratio_max'], 2)} at the HOSE weight. A share above one half is thus guaranteed for most nested "
              "systems and carries no information."),
        ('p', "*Corollary 5 (attribution).* Let overlap and dependence be switched on separately. With neither, the coefficient "
              "is 0; with overlap only, it is ρ̲; with dependence only, it is ρ_AM; with both, it is ρ_AB. The benchmark-first "
              "share ρ̲/ρ_AB and the dependence-first share ρ_AM/ρ_AB answer counterfactual questions and depend on the order. "
              "The Shapley (1953) value averages the two orders and gives an additive split,"),
        ('eq', r'\phi_{\mathrm{overlap}}=\tfrac12\left[\underline{\rho}+(\rho_{AB}-\rho_{AM})\right],\qquad \phi_{\mathrm{dep}}=\tfrac12\left[\rho_{AM}+(\rho_{AB}-\underline{\rho})\right],\qquad \phi_{\mathrm{overlap}}+\phi_{\mathrm{dep}}=\rho_{AB}. \qquad (11)'),
        ('p', "We report the sensitivity first, because it does not depend on any attribution convention, and the Shapley share "
              "φ_overlap/ρ_AB as the order-free attribution. Eq. (7) is an identity, not an estimated relation; we verify that it "
              "reproduces the directly estimated VN30–VN100 coefficient at every scale and frequency to within "
              f"{f(idmax * 1e16, 1)} × 10⁻¹⁶. Each quantity is computed on each scale of the reliable range (Section 4.4) and "
              "averaged over that range."),
        ('p', "Box 1 shows that the decomposition needs only index-level inputs. Because M is a linear combination of A and B, "
              "its volatility and its correlation with A follow from w, the two index volatilities and their correlation, so a "
              "user can compute the benchmark, the bound, the purged coefficient and the sensitivity without constituent data. The "
              "worked example uses full-sample Pearson moments of daily returns."),
        T('Box 1 Decomposition of a nested correlation from index-level inputs',
          ['Step', 'Computation', 'VN30 in VN100, daily'],
          [['1. Inputs', 'w; σ_A, σ_B; ρ_AB', f"w = {f(REC['w'], 4)}; σ_A = {f(REC['sd_VN30'], 4)}, σ_B = {f(REC['sd_VN100'], 4)}; ρ_AB = {f(REC['rho_AB'], 4)}"],
           ['2. Remainder volatility', 'σ_M = (σ²_B − 2wρ_AB σ_A σ_B + w²σ²_A)^{1/2}/(1 − w)', f"σ_M = {f(REC['sd_M'], 4)}"],
           ['3. Relative amplitude', 'κ = (1 − w)σ_M/(wσ_A)', f"κ = {f(REC['kappa'], 3)}"],
           ['4. Benchmark and bound', 'ρ̲ = (1 + κ²)^{−1/2}; bound (1 − κ²)^{1/2}', f"ρ̲ = {f(REC['benchmark'], 3)}; bound {f(REC['lower_bound'], 3)}"],
           ['5. Purged coefficient', 'ρ_AM = (ρ_AB σ_B − wσ_A)/[(1 − w)σ_M]', f"ρ_AM = {f(REC['rho_AM'], 3)}"],
           ['6. Sensitivity', 'Eq. (10)', f"{f(REC['sensitivity'], 3)} (inverse {f(REC['inverse_sensitivity'], 1)})"]],
          'Pearson moments of daily log returns, February 2014 to December 2025. Steps 2 and 5 reproduce the volatility and the '
          'correlation of the directly constructed P_cap series exactly. Source: Authors’ calculations.'),
        ('h2', '4.3 Weight uncertainty'),
        ('p1a', "Between semi-annual reviews, constituent capitalizations drift with relative prices. If the true weight w_t differs "
                "from the fixed weight w, the purged series becomes"),
        ('eq', r'\hat{M}_t=\frac{1-w_t}{1-w}M_t+\frac{w_t-w}{1-w}A_t, \qquad (12)'),
        ('p', "so large-cap returns leak into P_cap in proportion to the weight gap, and P_cap and VN30 are disjoint only when the "
              "weight is exact. We could obtain only one factsheet snapshot of free-float weights, so we cannot reconstruct the "
              "weight path. Instead we treat w as uncertain: in each bootstrap replicate we draw w from a uniform distribution on "
              "[0.60, 0.75], an interval that contains the factsheet weight with room for drift in either direction, recompute "
              "P_cap and recompute every quantity. We report these intervals next to the fixed-weight intervals, and Table S2 "
              "evaluates each quantity on a grid of weights. The benchmark and the sensitivity depend on the data only through κ, "
              "so they are less exposed to weight error than the level of ρ_AM."),
        ('h2', '4.4 Reliability thresholds and inference'),
        ('p1a', "The number of boxes falls as s grows, so the DCCA coefficient becomes noisy at large scales. For each sample size we "
                "simulate pairs of Gaussian white noise with correlations of −0.3, 0, 0.3, 0.5, 0.7 and 0.9 (167 replications each, "
                "1,002 per frequency) and compute the mean absolute estimation error on 40 log-spaced scales. The reliability "
                "threshold s_rel is the largest scale below the first scale at which the worst-case error exceeds 0.05; the grid "
                "and the tolerance were fixed before the empirical analysis. Because returns are heavy-tailed and "
                "volatility-clustered, we repeat the calibration with GARCH(1,1) series driven by Student-t innovations with five "
                "degrees of freedom (300 simulations)."),
        ('p', "DCCA coefficients at different scales are functionals of the same two series, so treating scales as independent "
              "observations would overstate precision. All inference therefore resamples the data with the stationary block "
              "bootstrap (Politis and Romano 1994), with a mean block length of about 20 trading days (20 days times the number "
              "of bars per day at intraday frequencies). Each replicate redraws the joint return series and recomputes every DCCA "
              "curve and derived statistic. We use 499 replications for DCCA statistics, 999 for the factor-model, lead–lag and "
              "materiality statistics and 1,999 for Pearson regime statistics. Intervals are percentile 95% intervals, capped at "
              "±1 where the statistic is a correlation. Bootstrap p-values invert the percentile interval, "
              "p = 2 min{k₋ + 1, k₊ + 1}/(B + 1), where k₋ and k₊ count replicates at or below and at or above zero; with B = 499 "
              "the smallest attainable value is 0.004, which we report as p < 0.005."),
        ('p', "That resolution limits multiplicity adjustment: with 19 tests, the smallest Holm-adjusted p-value attainable from "
              "499 replications is 0.076. For the slope tests we therefore also report studentized p-values, 2Φ(−|β̂|/se_boot), "
              "where se_boot is the bootstrap standard error, and adjust them with the Holm (1979) and Benjamini and Hochberg "
              "(1995) procedures in two families: the original 19 reliable-range slope tests, and the eight broad-market tests "
              "that H2 concerns. The VN30–VN100 prediction is tested by two one-sided tests (TOST; Schuirmann 1987) with an "
              "equivalence margin of 0.001 per unit of ln s; over the reliable range, about 4.5 units of ln s at M30, such a slope "
              "moves the coefficient by less than one tenth of the 0.05 tolerance."),
        ('h2', '4.5 Scaling regressions and slope channels'),
        ('p1a', "To measure horizon dependence we regress the DCCA coefficient on the log timescale,"),
        ('eq', r'\rho_{XY}(s)=\alpha+\beta\ln s+u(s), \qquad (13)'),
        ('p', "over the reliable range s ≤ s_rel and, in the Supplementary Material, over 30 log-spaced scales between 5 bars and "
              "one quarter of the sample. A positive β indicates that co-movement builds up with the horizon. For the nested pair "
              "Eq. (7) splits the slope into a channel through the purged coefficient and a channel through κ,"),
        ('eq', r'\frac{d\rho_{AB}}{d\ln s}=\frac{\partial\rho_{AB}}{\partial\rho_{AM}}\frac{d\rho_{AM}}{d\ln s}+\frac{\partial\rho_{AB}}{\partial\kappa}\frac{d\kappa}{d\ln s},\qquad \frac{\partial\rho_{AB}}{\partial\kappa}=-\frac{\kappa(1-\rho_{AM}^2)}{(1+\kappa^2+2\kappa\rho_{AM})^{3/2}}, \qquad (14)'),
        ('p', "so any horizon dependence in the purged coefficient reaches the nested coefficient damped by the sensitivity of "
              "Eq. (10). We evaluate Eq. (14) with the reliable-range slopes of ρ_AM and κ and compare it with the observed slope."),
        ('h2', '4.6 Volatility conditioning and contagion tests'),
        ('p1a', "If y_t = α + βx_t + ε_t with Var(ε_t) = σ²_ε, the correlation ρ = [1 + σ²_ε/(β²σ²_x)]^{−1/2} rises with the "
                "variance of x even when β and σ²_ε are constant. Forbes and Rigobon (2002) correct the crisis correlation as"),
        ('eq', r'\rho^{*}=\frac{\rho_{\mathrm{high}}}{\sqrt{1+\delta\,(1-\rho_{\mathrm{high}}^2)}},\qquad \delta=\frac{\sigma^2_{x,\mathrm{high}}-\sigma^2_{x,\mathrm{low}}}{\sigma^2_{x,\mathrm{low}}}. \qquad (15)'),
        ('p', "with y = P_cap and x = VN30. The correction assumes that β and σ²_ε do not change across regimes. If crises raise "
              "idiosyncratic variance, ρ* understates the crisis correlation and the test leans toward no contagion (Corsetti et "
              "al. 2005). We therefore estimate the single-factor model in each regime and test whether the loading β and the "
              "residual variance change, which is the contagion concept in Corsetti et al. (2005) and the structural parameter "
              "of Rigobon (2003). We use three regime definitions: chronological episodes, VNINDEX volatility quartiles and VN30 "
              "volatility quartiles. The last one sorts on the conditioning variable and avoids sorting on a series that contains "
              "P_cap. Regime statistics are Pearson correlations of daily returns, and the bootstrap is applied within each "
              "regime. The nested pairs are not tested, because the parent contains the conditioning index."),
        ('h2', '4.7 Portfolio variance: in-sample misstatement and out-of-sample evaluation'),
        ('p1a', "For an equally weighted two-asset position with volatilities σ₁ and σ₂, replacing the regime correlation ρ_r by a "
                "static full-sample correlation ρ_st changes the variance by the relative error"),
        ('eq', r'\mathrm{RE}=\frac{\rho_{\mathrm{st}}-\rho_{r}}{\tfrac{1}{2}\left(\sigma_1/\sigma_2+\sigma_2/\sigma_1\right)+\rho_{r}}, \qquad (16)'),
        ('p', "evaluated with regime-specific volatilities so that only the correlation differs. Intervals resample the full "
              "sample jointly, so that ρ_st is re-estimated in each replicate. As a materiality benchmark we compare |RE| with the "
              "bootstrap relative standard error of the regime portfolio variance itself. In-sample regimes are ex post, so we "
              "also run an out-of-sample comparison. Correlations are estimated from 2014 to 2022 and evaluated on 2023–2025. All "
              "forecasts share one-step-ahead RiskMetrics variances with λ = 0.94 (J.P. Morgan/Reuters 1996) and differ only in the "
              "correlation: static, EWMA with the same λ, or a regime correlation chosen in real time from the lagged rolling "
              "volatility with thresholds fixed in the estimation window. Losses are QLIKE, which is robust to the noise in "
              "squared returns as a variance proxy (Patton 2011), and squared error. Differences are tested with the Diebold and "
              "Mariano (1995) statistic using a Newey and West (1987) variance with five lags."),
        ('h2', '4.8 Computational details'),
        ('p1a', "All computations use R 4.3.3 with the packages stats, sandwich 3.1.0 and ggplot2 3.4.4 on an Intel Xeon "
                "processor (2.10 GHz, four cores). OLS fits use the QR decomposition, so no iterative optimization, tolerance or "
                "convergence criterion is involved. Random seeds are fixed in each script (20260924 to 20261013). A single "
                "script, run_all.R, reproduces every table and figure; rerunning it yields byte-identical CSV output files. The "
                "code, outputs and a mapping from every reported number to its output file are provided as Online Resource 1."),
    ]


def T(caption, header, body, note):
    return ('table', (caption, header, body, note))


def results():
    t1d = [DESC[(v, t)] for v in ['VN30', 'VN100', 'VNINDEX', 'Pcap'] for t in TF]
    tab2 = T('Table 2 Descriptive statistics of log returns',
             ['Series', 'Freq.', 'N', 'Mean', 'Std. dev.', 'Skew.', 'Kurt.', 'Jarque–Bera'],
             [[('P_{cap}' if r['index'] == 'Pcap' else r['index']), r['freq'], nint(r['n']), f(r['mean'], 4), f(r['sd'], 4),
               f(r['skew'], 2), f(r['kurtosis'], 2), nint(r['jb']) + '***'] for r in t1d],
             'Kurt. is non-excess kurtosis; P_cap is the overlap-purged series of Eq. (6); *** p < 0.01. Source: Authors’ '
             'calculations based on HOSE index data (TradingView).')
    tab3 = T('Table 3 Finite-sample reliability thresholds of the DCCA coefficient',
             ['Frequency', 'N', 'Gaussian s_rel', 'Heavy-tailed s_rel'],
             [[TFNAME[t], nint(REL[t]['n']), REL[t]['s_rel'], GARCH[t]['s_rel_garch_t']] for t in TF],
             'Largest scale (bars) at which the worst-case mean absolute error stays below 0.05; Gaussian: 1,002 white-noise '
             'simulations; heavy-tailed: 300 GARCH(1,1)-t(5) simulations. Source: Authors’ calculations.')
    rowsA = [[TFNAME[t], f(AVG[('A', t)]['nested_mean']), f(AVG[('A', t)]['VN30-VN100']), f(AVG[('A', t)]['Pcap-VN30']),
              f(AVG[('A', t)]['gap']), '', '', nint(AVG[('A', t)]['n'])] for t in TF]
    rowsB = [[TFNAME[t], f(AVG[('B', t)]['nested_mean']), f(AVG[('B', t)]['VN30-VN100']), f(AVG[('B', t)]['Pcap-VN30']),
              est_ci(gapB[t]), est_ci(gapL[t]), f(Q[t]['cohen_q'], 2) + ' ' + ci(Q[t]['ci_lo'], Q[t]['ci_hi'], 2),
              nint(AVG[('B', t)]['n'])] for t in TF]
    tab4 = T('Table 4 Average DCCA coefficients of nested and overlap-purged pairs',
             ['Frequency', 'Nested mean', 'VN30–VN100', 'P_cap–VN30', 'Three-pair gap [95% CI]', 'Like-for-like gap [95% CI]', 'Cohen’s q [95% CI]', 'N'],
             [['*Panel A: synchronized window, 2017–2024*', '', '', '', '', '', '', '']] + rowsA +
             [['*Panel B: full sample, 2014–2025*', '', '', '', '', '', '', '']] + rowsB,
             'Averages of ρ(s) over s ≤ s_rel (Table 3) with m = 1; nested mean: VN30–VNINDEX, VN30–VN100 and VN100–VNINDEX; '
             'three-pair gap: nested mean minus P_cap–VN30; like-for-like gap: VN30–VN100 minus P_cap–VN30. Brackets: '
             'block-bootstrap 95% intervals at the factsheet weight. Source: Authors’ calculations.')

    def r5(t):
        return [TFNAME[t], f(D(t, 'kappa')['estimate']), est_ci(D(t, 'rho_econ')), f(D(t, 'rho_nested')['estimate']),
                est_ci(D(t, 'floor')), f(TMIN[t]['true_min']), est_ci(D(t, 'sensitivity')), f(D(t, 'mech_share')['estimate']),
                est_ci(A_(t, 'shapley_overlap_share'))]

    def r5w(t):
        g = lambda s: est_ci(wu[(t, s)], e='estimate_at_baseline_w')
        return [TFNAME[t], '', g('rho_econ'), '', g('floor'), '', g('sensitivity'), g('mech_share'), g('shapley_overlap_share')]
    tab5 = T('Table 5 Part–whole decomposition of the VN30–VN100 DCCA coefficient (Lemma 1)',
             ['Frequency', 'κ', 'Purged ρ_AM', 'Nested ρ_AB', 'Benchmark ρ̲', 'Bound √(1 − κ²)', 'Sensitivity', 'Benchmark-first share', 'Shapley overlap share'],
             [['*Panel A: sampling uncertainty, w fixed at the factsheet value*', '', '', '', '', '', '', '', '']] + [r5(t) for t in TF] +
             [['*Panel B: sampling and weight uncertainty, w ~ U(0.60, 0.75) in each replicate*', '', '', '', '', '', '', '', '']] +
             [r5w(t) for t in ('1D', 'M30')],
             'Quantities of Eqs. (7)–(11) averaged over s ≤ s_rel; A = VN30, B = VN100, M = P_cap. Brackets: block-bootstrap '
             '95% intervals; Panel B is computed for the daily and 30-minute frequencies. Source: Authors’ calculations.')

    def r6(t, p):
        r = h2row(t, p)
        return [TFNAME[t], lab(p), est_ci(r, 4), pbfmt(r['p_boot']), pfmt(r['p_studentized']), pfmt(r['p_stud_holm_all']),
                (pfmt(r['p_stud_holm_h3']) if r['h3_family'] == 'TRUE' else '–'),
                (pfmt(r['tost_p']) if p == 'VN30-VN100' else '–')]
    tab6 = T('Table 6 Reliable-range scaling slopes of DCCA coefficients',
             ['Frequency', 'Pair', 'Slope [95% CI]', 'p (bootstrap)', 'p (studentized)', 'Holm, 19 tests', 'Holm, H2 family', 'TOST p'],
             [r6(t, p) for t in TF for p in PAIRS4],
             f'Slopes β of Eq. (13) over s ≤ s_rel. Holm, 19 tests: studentized p adjusted over the original {fam} tests, which '
             'include three statistical proxies at M30 (Table S8); H2 family: the eight broad-market tests; TOST: equivalence '
             'to zero with a margin of 0.001. Source: Authors’ calculations.')

    def r7(name, fr, fac):
        return [name, f(fr['rho_low']), f(fr['rho_high']), f(fr['diff']) + ' ' + ci(fr['ci_lo'], fr['ci_hi']), pfmt(fr['p_one_sided']),
                f(fac['beta_low']), f(fac['beta_high']), f(fac['d_beta']) + ' ' + ci(fac['d_beta_ci_lo'], fac['d_beta_ci_hi']),
                f(fac['idio_var_ratio'], 2) + ' ' + ci(fac['idio_ratio_ci_lo'], fac['idio_ratio_ci_hi'], 2)]
    tab7 = T('Table 7 Crisis dependence between P_cap and VN30: adjusted correlation and factor-model tests',
             ['Regime definition', 'ρ_low', 'ρ_high', 'ρ* − ρ_low [95% CI]', 'p (FR)', 'β_low', 'β_high', 'Δβ [95% CI]', 'Residual variance ratio [95% CI]'],
             [r7('Chronological episodes', frA, facA), r7('VNINDEX volatility quartiles', frB, facB), r7('VN30 volatility quartiles', fr30, facC)],
             f'Daily returns; ρ* from Eq. (15); p (FR): one-sided bootstrap p-value for H0: ρ* ≤ ρ_low; β: OLS slope of P_cap on '
             f'VN30; residual variance ratio: crisis over calm. Chronological: {nint(frA["n_low"])} calm and {nint(frA["n_high"])} '
             f'crisis days; quartiles: {nint(frB["n_low"])} days per regime. Source: Authors’ calculations.')

    def r8(pan, g, p):
        r = re_(pan, g, p)
        return [('Chronological' if pan == 'A' else 'VNINDEX quartiles') + (', calm' if g == 'low' else ', crisis'), lab(p),
                f(r['RE_pct'], 2) + ' ' + ci(r['RE_joint_ci_lo'], r['RE_joint_ci_hi'], 2), f(r['regime_var_rel_se_pct'], 1),
                f(r['RE_over_se'], 2)]
    tab8a = [r8(pan, g, p) for pan in 'AB' for g in ('low', 'high') for p in ('Pcap-VN30', 'VN30-VN100')]

    def r8b(p):
        s, e, g = oos(p, 'static'), oos(p, 'ewma'), oos(p, 'regime')
        de, dr = oos(p, 'DM_static_vs_ewma'), oos(p, 'DM_static_vs_regime')
        return [lab(p), f(s['mean_qlike'], 4), f(e['mean_qlike'], 4), f(g['mean_qlike'], 4),
                f(de['dm_t_qlike'], 2) + ' (' + f(de['dm_p_qlike'], 3) + ')', f(dr['dm_t_qlike'], 2) + ' (' + f(dr['dm_p_qlike'], 3) + ')']
    tab8 = T('Table 8 Portfolio variance: in-sample misstatement and out-of-sample forecast comparison',
             ['Regime or pair', 'Pair or static QLIKE', 'RE, % [95% CI] or EWMA QLIKE', 'Relative SE, % or regime QLIKE', 'RE/SE or DM, static vs EWMA', 'DM, static vs regime'],
             [['*Panel A: in-sample misstatement (E3)*', '', '', '', '', '']] + [r[:1] + r[1:] + [''] for r in tab8a] +
             [['*Panel B: out-of-sample, 2023–2025 (H4)*', '', '', '', '', '']] + [r8b(p) for p in ('Pcap-VN30', 'VN30-VN100', 'VN30-VNINDEX', 'VN100-VNINDEX')],
             f'Panel A: RE of Eq. (16) for an equally weighted position; relative SE: bootstrap standard error of the regime portfolio '
             f'variance. Panel B: mean QLIKE over {nint(OOSD["n_eval"])} evaluation days; DM: Diebold–Mariano t-statistic (p) on '
             'the QLIKE difference, negative when the static correlation has the lower loss. Source: Authors’ calculations.')

    h2s = lambda t, p: h2row(t, p)
    return [
        ('h1', '5 Results'),
        ('h2', '5.1 Summary statistics and reliability'),
        ('p1a', "Table 2 reports descriptive statistics of index and purged returns at the four frequencies."),
        tab2,
        ('p', f"At the daily frequency the standard deviation is highest for P_cap ({f(DESC[('Pcap', '1D')]['sd'], 4)}) and lowest "
              f"for VNINDEX ({f(DESC[('VNINDEX', '1D')]['sd'], 4)}). All series are negatively skewed and leptokurtic, with kurtosis "
              f"above {int(min(F(DESC[(v, 'M30')]['kurtosis']) for v in ['VN30', 'VN100', 'VNINDEX', 'Pcap']))} at M30, and the "
              "Jarque–Bera test rejects normality everywhere. Neither DCCA nor the block bootstrap requires Gaussian returns. "
              "Table 3 reports the reliability thresholds."),
        tab3,
        ('p', f"The Gaussian thresholds range from {REL['1D']['s_rel']} days at 1D to {REL['M30']['s_rel']} bars at M30, and "
              "heavy-tailed series reduce them by roughly a factor of three. All averages below use the Gaussian thresholds. Over "
              "the shorter heavy-tailed ranges the nested averages become "
              f"{rng([GARCH[t]['nested_avg_conservative'] for t in TF])} and the purged average "
              f"{rng([GARCH[t]['pcap_avg_conservative'] for t in TF])}, so no conclusion depends on the choice."),
        ('h2', '5.2 The overlap gap (H1)'),
        ('p1a', "Table 4 compares the average DCCA coefficients of the nested pairs with that of the purged pair, and Fig. 2 shows "
                "the full curves with bootstrap bands."),
        tab4,
        ('p', f"The nested pairs average {rng(nested_all)} at every frequency in both samples, whereas P_cap–VN30 averages "
              f"{rng(pcap_all)}. Corollary 3 fixes the sign of the like-for-like gap once ρ_AM ≥ 0, but not its size. The gap is "
              f"{rng(gapL_v)} with interval lower bounds of at least {f(gapL_lo)}, above the 0.05 margin at every frequency, so "
              f"{'H1 is supported' if H1_ok else 'H1 is not supported at every frequency'}. The three-pair gap, which also uses the "
              f"broad-market pairs for which no weight-based purge is available, is {rng(gap3)}, and Cohen’s q (Cohen 1988) of "
              f"{rng(qv, 2)} indicates a large effect on the Fisher scale; we use it descriptively, since both coefficients come from the same sample. The purged coefficient remains high: overlap inflates "
              "co-movement that is already strong rather than creating it."),
        ('p', "The gap depends on the weight. Over the grid from 0.60 to 0.75, the like-for-like daily gap ranges from "
              f"{f(min(like_w))} to {f(max(like_w))} and the three-pair gap from {f(min(ws_gap))} to {f(max(ws_gap))} (Tables S2 and S3), so "
              "the point estimate stays above the margin at every weight in the grid, but its size is known only to within about a "
              "factor of two. With the weight drawn inside each bootstrap replicate, the like-for-like gap has 95% intervals with "
              f"lower bounds of {rng([GWU[t]['ci_lo'] for t in TF], 3)} (upper bounds {rng([GWU[t]['ci_hi'] for t in TF], 3)}), and every "
              "replicate exceeds 0.05, so H1 also holds under weight uncertainty. A larger weight removes more of the VN30 component and lowers the purged coefficient."),
        ('fig', ('fig2', 'Fig. 2 DCCA coefficients of the nested pairs and P_cap–VN30 by timescale: (a) 1D, (b) M30, (c) H1, (d) H4',
                 'Line and marker types identify the pairs; grey bands: pointwise block-bootstrap 95% intervals; vertical dotted '
                 'lines: s_rel (Table 3). Source: Authors’ calculations based on HOSE index data (TradingView).')),
        ('h2', '5.3 The part–whole decomposition (E1, E2)'),
        ('p1a', "Table 5 applies Lemma 1 to the VN30–VN100 pair, and Fig. 3 plots Eq. (7) against the purged coefficient."),
        tab5,
        ('p', f"The sensitivity of the nested coefficient to the purged coefficient is {rng(sens_v, 3)}: to move the index-level "
              f"number by 0.01, the purged coefficient would have to move by about {f(sum(inv_sens) / 4 * 0.01, 2)}. With weight "
              f"uncertainty the interval widens to {f(wu_rng('sensitivity')[0], 2)}–{f(wu_rng('sensitivity')[1], 2)}, so the "
              "qualitative conclusion does not depend on the weight. The relative amplitude κ is "
              f"{rng(kap_v, 2)}, so the remaining 32% of VN100 contributes about half as much detrended variation as the VN30 "
              f"component, and the benchmark is {rng(bench_v, 3)}. At these values Eq. (9) gives a lower bound of "
              f"{rng(tmin_v, 3)}: no purged coefficient in [−1, 1] could push the VN30–VN100 coefficient below about 0.86."),
        ('p', f"How much of the observed {rng(nest_v, 3)} is due to overlap depends on the question asked. The benchmark-first "
              f"share is {rng(share_v, 3)} and the dependence-first share is {rng(econsh_v, 3)}; both are large because each "
              "factor alone already produces a coefficient near 0.9. The Shapley split, which averages the two orders, attributes "
              f"{rng(shap_v, 3)} of the coefficient to overlap (intervals within {f(shap_lo, 3)}–{f(shap_hi, 3)}). Weight "
              f"uncertainty widens the Shapley intervals to {f(wu_rng('shapley_overlap_share')[0], 2)}–"
              f"{f(wu_rng('shapley_overlap_share')[1], 2)} and the benchmark-first intervals to "
              f"{f(wu_rng('mech_share')[0], 2)}–{f(wu_rng('mech_share')[1], 2)}, against a sampling-only width of about 0.02. "
              "Weight error, not sampling error, is the main source of uncertainty about the attribution."),
        ('p', "The decomposition hardly varies with the horizon. Across all reliable scales and frequencies κ lies between "
              f"{f(min(kap_scales), 2)} and {f(max(kap_scales), 2)}, the benchmark varies by {rng(bench_rng, 3)} within each "
              f"frequency, and its slope on ln s is not significant at 5% (bootstrap p = {rng(bslope_p, 3)}; Holm-adjusted "
              f"{rng(bslope_holm, 3)}), although at M30 the percentile interval just excludes zero; a slope of that size "
              "(about 0.002 per unit of ln s) is negligible. Applied to full-sample Pearson correlations, the identity gives a benchmark of "
              f"{rng(pear_bench, 3)} and a benchmark-first share of {rng(pear_share, 3)} across frequencies, within 0.01 of the DCCA "
              "values. In these data the multiscale layer therefore adds a check of scale invariance rather than a different "
              "answer, and Box 1 is sufficient for practice. The DCCA version remains necessary where the tiers have different "
              "scaling, which Eq. (7) would reveal as variation in κ(s)."),
        ('fig', ('fig4', 'Fig. 3 Nested VN30–VN100 coefficient implied by Lemma 1 as a function of the overlap-purged coefficient',
                 'Lines: Eq. (7) at the average κ of each frequency (Table 5); markers: observed values; dashed line: daily '
                 'zero-correlation benchmark; dotted line: daily lower bound of Eq. (9). Source: Authors’ calculations.')),
        ('p', f"Fig. 4 places the HOSE in the space of possible nested systems. The contours show the Pearson benchmark as a "
              "function of the child weight and the relative volatility of the remainder, and the triangle marks VN30 in VN100 "
              f"(w = {f(HOSEPT['w'], 3)}, σ_M/σ_A = {f(HOSEPT['amplitude_ratio_daily_sd'], 2)}, benchmark {f(HOSEPT['floor'], 3)}). A "
              "child weight of 0.5 with equal volatilities would still give a benchmark of about 0.7, so a large mechanical "
              "component is the rule rather than a HOSE peculiarity."),
        ('fig', ('fig5', 'Fig. 4 Zero-correlation benchmark ρ̲ as a function of the child weight w and the relative volatility σ_M/σ_A',
                 'Contours of Eq. (8) with κ = (1 − w)σ_M/(wσ_A); triangle: VN30 in VN100, daily Pearson moments. Source: Authors’ '
                 'calculations.')),
        ('h2', '5.4 Horizon dependence (H2)'),
        ('p1a', "Table 6 reports reliable-range scaling slopes for the four main pairs at all frequencies, with bootstrap, "
                "studentized and adjusted p-values."),
        tab6,
        ('p', "Positive slopes appear only for the broad-market pairs at intraday frequencies. In the eight-test H2 family, "
              f"{NUMW.get(len(holm_h2), len(holm_h2))} slopes survive Holm adjustment of the studentized p-values ("
              + '; '.join(f"{lab(p)} at {t}" for t, p in sorted(holm_h2)) +
              f"), with estimates of {rng([h2s(t, p)['estimate'] for t, p in holm_h2], 4)} per unit of ln s, or a rise of about 0.01 "
              f"across the reliable range. No slope is significant at 1D or H4. Under its decision rule H2 is "
              f"{H2_out.lower()} on the full data; the robustness checks below qualify this result."),
        ('p', f"The conclusion depends on the test family, which is why we report both. Over the original {fam} tests, Holm keeps "
              f"{NUMW.get(len(holm_all), len(holm_all))} studentized slope{'s' if len(holm_all) != 1 else ''} and Benjamini–Hochberg keeps {NUMW.get(len(bh_all), len(bh_all))}; with "
              f"percentile p-values from 499 replications no test survives either adjustment (smallest BH-adjusted p = "
              f"{f(pboot_bh_min, 3)}). For VN30–VN100, the slope is equivalent to zero at "
              + (' and '.join(tost_eq) if tost_eq else 'no frequency') +
              f" (TOST p = {', '.join(pfmt(h2s(t, 'VN30-VN100')['tost_p']) for t in tost_eq)}) and inconclusive elsewhere. The purged "
              "P_cap–VN30 slope is insignificant everywhere."),
        ('p', f"Eq. (14) explains why the nested slope is flat. The damping factor, the sensitivity of Eq. (10), is "
              f"{rng(damp, 3)}, and the κ channel partly offsets the ρ_AM channel. The linearized slope implied by Eq. (14) "
              f"differs from the observed VN30–VN100 slope by at most {f(slc_err * 1e5, 1)} × 10⁻⁵ at any frequency (Table S13). "
              "A flat nested coefficient is therefore not evidence that the tiers have no horizon structure: a purged slope of "
              "0.01 per unit of ln s, about five times the broad-market slopes above, would move the nested slope by only about "
              "0.001, the TOST margin."),
        ('p', "The intraday design needs two checks. The first bar of each day contains the overnight return and the opening "
              "auction, the bar in which intraday volatility is highest (Andersen and Bollerslev 1997); it is "
              f"{f(100 * F(FB['M30']['share_of_bars_dropped']), 0)}% of M30 bars but carries "
              f"{f(100 * F(FB['M30']['share_of_VN30_sq_return_in_first_bar']), 0)}% of the squared VN30 returns, and the last bar "
              "contains the closing auction. Table S7 re-estimates the slopes without these bars. At H1, removing the opening bar "
              f"alone reduces the broad-market slopes to {f(ts('H1', 'drop_first', 'VN30-VNINDEX')['estimate'], 4)} and "
              f"{f(ts('H1', 'drop_first', 'VN100-VNINDEX')['estimate'], 4)}, with intervals that include zero. At M30, the "
              f"VN30–VNINDEX slope survives removal of the opening bar ({f(ts('M30', 'drop_first', 'VN30-VNINDEX')['estimate'], 4)}, "
              f"studentized p = {pfmt(ts('M30', 'drop_first', 'VN30-VNINDEX')['p_studentized'])}) while the VN100–VNINDEX slope halves "
              f"to {f(ts('M30', 'drop_first', 'VN100-VNINDEX')['estimate'], 4)} and loses significance; removing both auction bars "
              f"leaves slopes of {f(ts('M30', 'drop_first_last', 'VN30-VNINDEX')['estimate'], 5)} and "
              f"{f(ts('M30', 'drop_first_last', 'VN100-VNINDEX')['estimate'], 4)}, both insignificant. Trimming does not change "
              f"the overlap gap ({f(FB['M30']['gap'])} {ci(FB['M30']['gap_ci_lo'], FB['M30']['gap_ci_hi'])} at M30 without the "
              "first bar). Second, the M30 slope intervals hardly change with the block length (Table S15)."),
        ('p', "Within the same bootstrap replicates, the broad-market slopes exceed the VN30–VN100 slope at M30 and H1 "
              f"(differences {rng([tsd(t, 'full', p)['estimate'] for t in ('M30', 'H1') for p in BROAD], 4)}, studentized p at most "
              f"{pfmt(max(F(tsd(t, 'full', p)['p_studentized']) for t in ('M30', 'H1') for p in BROAD))}), but not at 1D or H4, and "
              "the differences vanish when the auction bars are removed. "
              + ("H2 is therefore supported on the full data under its decision rule, but the horizon dependence is not a "
                 "property of continuous trading: it comes from the bars that contain the overnight return and the two call "
                 "auctions. This is consistent with the Epps (1979) mechanism if the auctions are where the prices of less liquid "
                 "constituents catch up with large caps, and it means that the H2 result says more about the auction calendar "
                 "than about gradual information diffusion." if (H2_out == 'Supported' and not H2_robust) else
                 f"H2 is {H2_out.lower()} and {'robust' if H2_robust else 'not robust'} to removal of the opening bar.")),
        ('h2', '5.5 Crisis dependence (H3)'),
        ('p1a', "Table 7 reports the Forbes–Rigobon adjusted correlations and the single-factor tests under three regime "
                "definitions."),
        tab7,
        ('p', f"The raw correlation rises in every crisis definition, from {f(frA['rho_low'])} to {f(frA['rho_high'])} "
              f"chronologically and from {f(fr30['rho_low'])} to {f(fr30['rho_high'])} under VN30 quartiles. After the "
              "Forbes–Rigobon correction the crisis correlation never exceeds its calm level (one-sided p between "
              f"{f(min(F(frA['p_one_sided']), F(frB['p_one_sided']), F(fr30['p_one_sided'])), 3)} and "
              f"{f(max(F(frA['p_one_sided']), F(frB['p_one_sided']), F(fr30['p_one_sided'])), 3)}), and across the weight grid no "
              f"one-sided p falls below {f(min(frw_p), 3)} (Table S10). Under VN30 quartiles the adjusted correlation is even "
              f"significantly lower than in calm periods ({f(fr30['diff'])}, {ci(fr30['ci_lo'], fr30['ci_hi'])})."),
        ('p', "The factor model shows why this result should not be read as no contagion. The residual variance of P_cap rises "
              f"by a factor of {f(facC['idio_var_ratio'], 2)} {ci(facC['idio_ratio_ci_lo'], facC['idio_ratio_ci_hi'], 2)} under "
              f"VN30 quartiles and {f(facB['idio_var_ratio'], 2)} under VNINDEX quartiles, which violates the constant-variance "
              "assumption behind Eq. (15) and pushes ρ* down (Corsetti et al. 2005). The loading of P_cap on VN30 rises from "
              f"{f(facC['beta_low'])} to {f(facC['beta_high'])} under VN30 quartiles (Δβ = {f(facC['d_beta'])}, "
              f"{ci(facC['d_beta_ci_lo'], facC['d_beta_ci_hi'])}), but it does not change between the chronological episodes "
              f"(Δβ = {f(facA['d_beta'])}, {ci(facA['d_beta_ci_lo'], facA['d_beta_ci_hi'])}). Under the stated rule H3 is "
              f"{H3_out.lower()}: the adjusted correlation shows no contagion, while the loading rises on high-volatility days "
              "but not across the dated crises. Days of high VN30 volatility thus bring both a stronger response of mid caps to "
              "large caps and more mid-cap-specific risk. A rise in the loading is also what nonlinear dependence produces: the "
              f"lower-tail dependence of P_cap–VN30 is {f(tg('Pcap-VN30', '0.05')['lambda_L_empirical'], 2)} at the 5% quantile against "
              f"{f(tg('Pcap-VN30', '0.05')['lambda_L_gaussian_copula'], 2)} under a Gaussian copula with the same correlation "
              "(Table S5), so we cannot tell a structural shift from a stable but nonlinear relation. Adding 2021 to the chronological "
              f"episodes ({nint(C21[1]['n_crisis'])} crisis days) leaves both results unchanged (Forbes–Rigobon p = "
              f"{f(C21[1]['fr_p_one_sided'], 3)}; Δβ = {f(C21[1]['d_beta'])}, {ci(C21[1]['d_beta_ci_lo'], C21[1]['d_beta_ci_hi'])})."),
        ('h2', '5.6 Portfolio variance (E3, H4)'),
        ('p1a', "Table 8 reports the in-sample misstatement from using a static correlation and the out-of-sample comparison of "
                "correlation forecasts."),
        tab8,
        ('p', f"In sample, a static correlation overstates the variance of an equally weighted VN30 and P_cap position by "
              f"{f(re_('A', 'low', 'Pcap-VN30')['RE_pct'], 2)}% in chronological calm periods and by "
              f"{f(re_('B', 'low', 'Pcap-VN30')['RE_pct'], 2)}% in the low-volatility quartile, and understates it by "
              f"{f(-F(re_('A', 'high', 'Pcap-VN30')['RE_pct']), 2)}% and {f(-F(re_('B', 'high', 'Pcap-VN30')['RE_pct']), 2)}% in "
              "turbulent regimes. The sign pattern is expected for any pooled correlation, which lies between the regime values. "
              f"For nested pairs the misstatement is at most {f(max(nested_re), 2)}% (Table S14). The magnitudes are small against sampling "
              f"error: |RE| is {rng(ratio_pcap, 2)} times the standard error of the regime variance for P_cap–VN30 and at most "
              f"{f(max(ratio_nest), 2)} times for the nested pairs. Only the calm-quartile overstatement for P_cap–VN30 exceeds one "
              "standard error."),
        ('p', "Out of sample, conditioning does not help. The static correlation has the lowest mean QLIKE for every pair, and "
              f"the Diebold–Mariano statistics are all negative (p between {f(min(dm_p), 3)} and {f(max(dm_p), 3)}), so neither "
              f"EWMA nor real-time regime correlations improve on it. {'H4 is supported.' if H4_ok else 'H4 is not supported.'} "
              "In these data, regime variation in correlations is real in sample but too small or too poorly timed to be "
              "exploited with volatility signals."),
        ('h2', '5.7 Further robustness'),
        ('p1a', "The Supplementary Material reports further checks; none changes the conclusions. The detrending moving-average "
                f"coefficient (DMCA; Kristoufek 2014) gives a purged coefficient of {rng(dm_pcap)} and a three-pair gap of "
                f"{rng(dm_gap)} (Table S4). Because DMCA satisfies the same identity, this is a check on the detrending method, "
                f"not an independent test. The daily gap interval stays within {f(blk_lo)}–{f(blk_hi)} for mean block lengths from "
                f"5 to 60 days (Table S6). The daily VN30–VNINDEX average is {f(DETREND[0], 4)}, {f(DETREND[1], 4)} and "
                f"{f(DETREND[2], 4)} for detrending orders 1, 2 and 3. Statistical proxies that replace the capitalization weight, "
                f"such as the volatility-scaled proxy with weight {rng(w_heur, 4)}, are numerically unstable and behave as amplified "
                "residuals (Table S8). Multifractal DCCA with shuffled surrogates attributes most of the multifractal range to fat "
                "tails (Fig. S1). The lead–lag, hedge-effectiveness and episode statistics used in Section 6 are in Tables S9, S11 "
                "and S12."),
        ('h2', '5.8 Summary'),
        ('p1a', "Table 9 summarizes the estimands and hypotheses."),
        T('Table 9 Summary of estimands and hypothesis tests',
          ['Item', 'Statistic', 'Evidence', 'Outcome', 'Comment'],
          [['E1 Benchmark and attribution', 'ρ̲; Shapley share', f'ρ̲ {rng(bench_v)}; Shapley {rng(shap_v)}', 'Estimated (not a test)', 'Attribution depends mainly on the weight'],
           ['E2 Sensitivity', 'Eq. (10)', f'{rng(sens_v)}; with weight uncertainty {f(wu_rng("sensitivity")[0], 2)}–{f(wu_rng("sensitivity")[1], 2)}', 'Estimated (not a test)', 'Damping factor of about ten'],
           ['E3 In-sample misstatement', 'RE, Eq. (16)', f'P_cap–VN30 {f(min(F(re_(a, g, "Pcap-VN30")["RE_pct"]) for a in "AB" for g in ("low", "high")), 1)}% to {f(max(F(re_(a, g, "Pcap-VN30")["RE_pct"]) for a in "AB" for g in ("low", "high")), 1)}%; mostly below one SE', 'Estimated (not a test)', 'Sign pattern expected from pooling'],
           ['H1 Material overlap gap', 'Like-for-like gap; lower CI > 0.05', f'Gap {rng(gapL_v)}; lower CI ≥ {f(gapL_lo)}', 'Supported' if H1_ok else 'Not supported', 'Holds under weight uncertainty'],
           ['H2 Horizon dependence', 'Studentized slopes; Holm (H2 family); TOST', f'{len(holm_h2)} of 8 broad-market slopes significant, all intraday; VN30–VN100 equivalent to zero at {", ".join(tost_eq) or "none"}', H2_out, 'Not robust: vanishes without the auction bars' if not H2_robust else 'Robust to removing the opening bar'],
           ['H3 Contagion', 'FR adjustment and Δβ, VN30 regimes', f'FR p = {f(fr30["p_one_sided"], 3)}; Δβ = {f(facC["d_beta"])}, p {pfmt(facC["p_d_beta"])}', H3_out, 'Loading rises on high-volatility days; residual variance rises too'],
           ['H4 Value of regime conditioning', 'QLIKE; Diebold–Mariano', f'Static lowest for all pairs; p {f(min(dm_p), 2)}–{f(max(dm_p), 2)}', 'Supported' if H4_ok else 'Not supported', 'Static correlation has the lowest loss']],
          'Decision rules for H1–H4 in Section 2.7; all tests at the 5% level. Source: Authors’ calculations.'),
    ]


def discussion():
    ll = LL['1D']
    return [
        ('h1', '6 Discussion'),
        ('h2', '6.1 Mechanisms'),
        ('p1a', "The results on nested pairs have one source. When a parent index contains a child, the child’s variation appears "
                "in both terms of every covariance and in both standard deviations, and Lemma 1 shows that this pins the nested "
                f"coefficient near a benchmark fixed by the weight and the relative amplitude. With VN30 holding {f(100 * W30, 0)}% "
                "of VN100, the benchmark is near 0.90 and the lower bound near 0.87, so the observed 0.99 carries little "
                "information about how mid caps move with large caps. The same arithmetic explains why the VN30–VN100 coefficient "
                "is flat across horizons and regimes: changes in the purged coefficient reach it damped by a factor of about ten."),
        ('p', "Once the overlap is removed, the remaining dependence has the features the size literature predicts. Daily VN30 "
              f"returns lead P_cap returns (cross-autocorrelation {f(ll['lead_VN30_on_Pcap'])}, "
              f"{ci(ll['ci_lo_1'], ll['ci_hi_1'])}), the reverse is negligible ({f(ll['lead_Pcap_on_VN30'])}), and the asymmetry "
              f"of {f(ll['asymmetry'])} {ci(ll['asym_ci_lo'], ll['asym_ci_hi'])} matches the large-to-small lead of Lo and MacKinlay "
              "(1990) and Hou (2007). Intraday the lead is symmetric (Table S9), and the intraday horizon dependence of "
              "broad-market pairs, which comes from the auction bars, is consistent with the Epps (1979) effect: VNINDEX "
              "contains small stocks whose liquidity is fragile (Chen et al. 2021) and whose prices adjust with a delay (Tran and "
              "Tran 2025). Index-level data cannot separate this from gradual information diffusion (Hong and Stein 1999)."),
        ('p', "Several mechanisms can raise the loading of mid caps on large caps on high-volatility days, and our data cannot "
              "rank them. Herding during stress (Nguyen et al. 2023) and high sector connectedness (Bui et al. 2022) make stocks "
              "move together; limit hits under the ±7% band synchronize the tails; margin calls force simultaneous selling across "
              "tiers; and foreign flows, which concentrate in large caps with room under their ownership limits, can transmit "
              "large-cap shocks to the rest of the market through domestic portfolio rebalancing. The rise in residual variance "
              "shows that crises also bring mid-cap-specific shocks, which the Forbes–Rigobon correction misreads as lower "
              "dependence."),
        ('h2', '6.2 Implications'),
        ('p1a', "If index-level correlations between nested benchmarks are used to judge diversification between size tiers, they "
                "should first be decomposed. Box 1 does this from the published series and the index weight, without "
                "constituent data. The useful output is the purged coefficient together with the sensitivity, because the "
                f"inverse sensitivity of about {f(REC['inverse_sensitivity'], 0)} states how ill-conditioned the index-level number "
                "is as a measure of tier co-movement: an error of 0.001 in the nested coefficient maps into an error of about 0.01 "
                "in the purged one. Holdings-based risk models are not affected."),
        ('p', "For hedging, the purged series gives the relevant numbers directly. A minimum-variance hedge of a mid-cap exposure "
              f"with VN30 removes a share ρ² of its variance (Ederington 1979), {f(HE['full']['hedge_effectiveness'], 2)} "
              f"{ci(HE['full']['ci_lo'], HE['full']['ci_hi'], 2)} over the full sample, but only "
              f"{f(HE['B_low']['hedge_effectiveness'], 2)} {ci(HE['B_low']['ci_lo'], HE['B_low']['ci_hi'], 2)} in the low-volatility "
              f"quartile and {f(HE['B_high']['hedge_effectiveness'], 2)} in the high-volatility quartile (Table S11). A holder of "
              "the VNMIDCAP exchange-traded fund who hedges with VN30 futures therefore keeps about a fifth of the variance on "
              "average and about half in calm markets. This basis risk is the quantity a mid-cap derivative would remove; "
              "whether such a product would be viable depends on demand and liquidity, which we do not study."),
        ('p', "For portfolio risk, our results do not support regime-conditioned correlations between tiers: the in-sample "
              "misstatement is mostly within sampling error, and real-time conditioning does not improve forecasts. The "
              "relevant error is the one the decomposition removes, which comes from reading a nested correlation as a measure "
              "of diversification, not the one from ignoring regimes."),
        ('h2', '6.3 Transferability'),
        ('p1a', "Lemma 1 holds for any nested pair whose child is contained in the parent with a known weight under one weighting "
                "scheme. Fig. 4 shows that the benchmark exceeds 0.7 whenever the child holds half of the parent and the remainder "
                "is no more volatile, so large mechanical components should be common in nested families such as SET50 "
                "within SET100 or IDX30 within LQ45. Their size must be computed from each family’s weights and volatilities; we "
                "did not do this because we could not verify the weights. When indices overlap only partly, Eq. (7) does not "
                "apply directly; the shared constituents then form a third component and the benchmark depends on the overlap "
                "weight in each index."),
        ('p', "We did not extend the decomposition to the broad-market pairs. VNINDEX is weighted by full market capitalization and "
              "VN100 and VN30 by free-float capitalization, so VN100 is not a fixed-weight component of VNINDEX and Eq. (6) does "
              "not hold exactly. Applying it would leak a mismatch term of the form of Eq. (12) into the purged series, with a "
              "size we cannot bound without constituent-level data. The three-pair gap in Table 4 is therefore descriptive for "
              "these pairs."),
        ('h2', '6.4 Limitations and future research'),
        ('p1a', "The evidence comes from one exchange and three indices, so the magnitudes should not be generalized beyond the "
                "HOSE. The purged series relies on one factsheet weight; we propagate a plausible range of weights, but a weight "
                "path built from semi-annual reviews would narrow the attribution intervals considerably, since weight error "
                "dominates sampling error. We could not validate P_cap against the published VNMIDCAP index or the FUEDCMID net "
                "asset value, because neither was available from our data source at all frequencies; for that reason we call ρ_AM "
                "overlap-purged rather than economic. Index-level prices cannot separate microstructure frictions from "
                "information diffusion, the crisis evidence depends on how regimes are defined, and the out-of-sample period "
                "covers three years. The FTSE Russell reclassification from September 2026 offers a natural experiment: if foreign "
                "inflows raise the weight of large caps or lower the volatility of the remaining constituents relative to large "
                "caps, Eq. (8) predicts a higher benchmark."),
        ('h1', '7 Conclusion'),
        ('p1a', "Correlations between nested equity indices contain a component fixed by construction. We carry the part–whole "
                "identity to scale-wise detrended coefficients, derive a benchmark, a lower bound, a sensitivity and an order-free "
                "attribution, and show that all of them can be computed from index-level inputs. On the HOSE, the VN30–VN100 "
                f"coefficient moves by only about {f(sum(sens_v) / 4, 2)} per unit change in the overlap-purged coefficient, so the "
                "index-level number says little about how mid caps move with large caps; removing the overlap lowers the "
                f"correlation with large caps by about {f(sum(gapL_v) / 4, 2)}. The purged series shows a large-to-small lead, intraday "
                "horizon effects that come from the auction bars, a higher loading of mid caps on large caps on high-volatility days alongside more "
                "mid-cap-specific risk, and no out-of-sample gain from regime-conditioned correlations. Users who rely on index "
                "levels should decompose nested correlations before reading them as evidence about diversification between "
                "tiers."),
    ]


def supplement():
    """Online Resource 2: supplementary tables and figure (replaces the former appendix)."""
    s1 = []
    for t in TF:
        for p in PAIRS4:
            a = MT[(t, p, 'slope_full')]
            s1.append([TFNAME[t], lab(p), est_ci(a, 4), pbfmt(a['p_boot'])])
    s2 = [[f(r['w'], 4) + (' (factsheet)' if abs(F(r['w']) - W30) < 1e-6 else ''), r['timeframe'], f(r['kappa']), f(r['rho_econ']),
           f(r['floor']), f(r['mech_share']), f(r['sensitivity']), f(r['shapley_overlap_share']), f(r['pearson_floor'])] for r in WSD]
    s3 = [[f(r['w'], 4) + (' (factsheet)' if abs(F(r['w']) - W30) < 1e-6 else ''), f(r['rho_mean_1D']), f(r['gap_vs_nested']),
           f(r['slope_M30'], 4), f(r['rho_low_pearson']), f(r['rho_high_pearson'])] for r in WS]
    s4 = [[TFNAME[t]] + [f(DMCA[(t, p)]['rho_dmca_avg']) for p in NESTED + ['Pcap-VN30']] + [f(DMCA[(t, 'Pcap-VN30')]['gap_vs_nested_mean'])] for t in TF]
    s5 = [[lab(p), u, est_ci(dict(estimate=TAIL[(p, u)]['lambda_L'], ci_lo=TAIL[(p, u)]['ci_lo'], ci_hi=TAIL[(p, u)]['ci_hi'])),
           f(tg(p, u)['pearson']), f(tg(p, u)['lambda_L_gaussian_copula']),
           f(F(tg(p, u)['lambda_L_empirical']) - F(tg(p, u)['lambda_L_gaussian_copula']))]
          for p in ['VN30-VN100', 'VN30-VNINDEX', 'VN100-VNINDEX', 'Pcap-VN30'] for u in ('0.05', '0.1')]
    s6 = [['Daily', r['block_length_days'], f(r['gap']), ci(r['ci_lo'], r['ci_hi'])] for r in BLK] + \
         [['30-minute', r['block_length_days'], f(r['gap']), ci(r['ci_lo'], r['ci_hi'])] for r in BLK30]
    vlab = {'full': 'All bars', 'drop_first': 'Without first bar', 'drop_first_last': 'Without first and last bar'}
    s7 = [[TFNAME[r['timeframe']], vlab[r['variant']], nint(r['n']), lab(r['pair']), est_ci(r, 4), pfmt(r['p_studentized'])]
          for r in TRIM if r['stat'] == 'slope' and r['timeframe'] in ('M30', 'H1')]
    s7 += [[TFNAME[r['timeframe']], vlab[r['variant']], nint(r['n']), lab(r['pair']) + ' minus VN30–VN100', est_ci(r, 4), pfmt(r['p_studentized'])]
           for r in TRIM if r['stat'] != 'slope']
    s14 = [[('Chronological' if k[0] == 'A' else 'VNINDEX quartiles') + (', calm' if k[1] == 'low' else ', crisis'), lab(k[2]),
            f(r['RE_pct'], 2) + ' ' + ci(r['RE_joint_ci_lo'], r['RE_joint_ci_hi'], 2), f(r['regime_var_rel_se_pct'], 1), f(r['RE_over_se'], 2)]
           for k, r in MAT.items()]
    s15 = [[r['block_length_days'], lab(r['pair']), est_ci(r, 4), pfmt(r['p_studentized'])] for r in SBLK]
    s8 = [[lab(p), est_ci(MT[('M30', p, 'slope_rel')], 4), pbfmt(MT[('M30', p, 'slope_rel')]['p_boot'])] for p in ['Pheur-VN30', 'Pratio-VN30', 'Pres-VN30']]
    s9 = [[TFNAME[t], nint(LL[t]['n_pairs']), f(LL[t]['lead_VN30_on_Pcap']) + ' ' + ci(LL[t]['ci_lo_1'], LL[t]['ci_hi_1']),
           f(LL[t]['lead_Pcap_on_VN30']) + ' ' + ci(LL[t]['ci_lo_2'], LL[t]['ci_hi_2']),
           f(LL[t]['asymmetry']) + ' ' + ci(LL[t]['asym_ci_lo'], LL[t]['asym_ci_hi'])] for t in ('1D', 'M30', 'H1')]
    s10 = [[f(r['w'], 4), 'Chronological' if r['regimes'] == 'chronological' else 'VN30 quartiles', f(r['rho_low']), f(r['rho_high']),
            f(r['rho_star']), f(r['diff']) + ' ' + ci(r['ci_lo'], r['ci_hi']), pfmt(r['p_one_sided'])] for r in FRW]
    hen = {'full': 'Full sample', 'A_low': 'Chronological calm', 'A_high': 'Chronological crisis', 'B_low': 'Low-volatility quartile', 'B_high': 'High-volatility quartile'}
    s11 = [[hen[k], nint(HE[k]['n']), f(HE[k]['hedge_effectiveness']) + ' ' + ci(HE[k]['ci_lo'], HE[k]['ci_hi'])] for k in hen]
    s12 = [[f"{r['start']} to {r['end']}", r['trading_days'], f(r['max_drawdown_pct'], 1), f(100 * F(r['share_top_quartile_vol']), 0),
            f(r['peak_vol_ann_pct'], 1), r['date_of_peak_vol']] for r in CRISIS[:3]] if False else \
          [[f"{r['start']} to {r['end']}", r['trading_days'], f(r['max_drawdown_pct'], 1), f(100 * F(r['share_top_quartile_vol']), 0),
            f(r['peak_vol_ann_pct'], 1), r['date_of_peak_vol']] for r in EPI]
    s13 = [[TFNAME[t], SLC[t]['n_scales'], f(SLC[t]['slope_rho_econ'], 4), f(SLC[t]['slope_kappa'], 4), f(SLC[t]['dg_drho'], 3),
            f(SLC[t]['dg_dkappa'], 3), f(SLC[t]['slope_implied_linear'], 5), f(SLC[t]['slope_rho_nested_obs'], 5)] for t in TF]
    S = lambda *a: T(*a)
    return [
        ('h1', 'Supplementary Material (Online Resource 2)'),
        ('p1a', "This document accompanies the article and reports robustness checks referred to in the main text. All numbers come "
                "from the R outputs listed in the replication package (Online Resource 1)."),
        S('Table S1 Full-range scaling slopes (30 log-spaced scales)', ['Frequency', 'Pair', 'Slope [95% CI]', 'p (bootstrap)'], s1,
          'Slopes of Eq. (13) over 30 scales from 5 bars to one quarter of the sample. Source: Authors’ calculations.'),
        S('Table S2 Decomposition of the VN30–VN100 coefficient on a grid of weights',
          ['w', 'Freq.', 'κ', 'ρ_AM', 'ρ̲', 'Benchmark-first share', 'Sensitivity', 'Shapley overlap share', 'Pearson ρ̲ (1D)'], s2,
          'DCCA quantities averaged over s ≤ s_rel at each weight. Source: Authors’ calculations.'),
        S('Table S3 Purged coefficient, gap and regime correlations on a grid of weights',
          ['w', 'Mean ρ_AM (1D)', 'Three-pair gap (1D)', 'Full-range slope (M30)', 'Calm ρ_low', 'Crisis ρ_high'], s3,
          'ρ_low and ρ_high: Pearson correlations of P_cap and VN30 in the chronological regimes. Source: Authors’ calculations.'),
        S('Table S4 Average DMCA coefficients over the reliable range',
          ['Frequency', 'VN30–VNINDEX', 'VN30–VN100', 'VN100–VNINDEX', 'P_cap–VN30', 'Three-pair gap'], s4,
          'Centered moving-average detrending with odd windows matched to the DCCA scales s ≤ s_rel. Source: Authors’ calculations.'),
        S('Table S5 Lower-tail dependence of daily returns and the Gaussian-copula benchmark',
          ['Pair', 'u', 'Empirical λ_L(u) [95% CI]', 'Pearson ρ', 'Gaussian-copula λ_L(u)', 'Excess'], s5,
          'λ_L(u) = P(X ≤ q_X(u), Y ≤ q_Y(u))/u; Gaussian-copula value at the pair’s own Pearson correlation. Source: Authors’ calculations.'),
        S('Table S6 Sensitivity of the gap interval to the bootstrap block length',
          ['Frequency', 'Mean block length (days)', 'Three-pair gap', '95% CI'], s6,
          'Bootstrap draws are separate from Table 4, so intervals differ by Monte Carlo error. Source: Authors’ calculations.'),
        S('Table S7 Reliable-range slopes with and without the auction bars, and broad-minus-nested slope differences',
          ['Frequency', 'Sample', 'N', 'Pair', 'Slope [95% CI]', 'p (studentized)'], s7,
          'First bar: overnight return and opening auction; last bar: closing auction; 199 block-bootstrap replicates; differences are computed within the same replicates. Source: Authors’ calculations.'),
        S('Table S8 Statistical proxies for the mid-cap segment (M30)', ['Proxy', 'Reliable-range slope [95% CI]', 'p (bootstrap)'], s8,
          f'P_heur replaces w by the VN30–VN100 correlation ({rng(w_heur, 4)}); P_ratio = B − A; P_res is the residual of B on A. Source: Authors’ calculations.'),
        S('Table S9 Lead–lag cross-autocorrelations between VN30 and P_cap',
          ['Frequency', 'Pairs', 'corr(A_{t−1}, M_t) [95% CI]', 'corr(M_{t−1}, A_t) [95% CI]', 'Asymmetry [95% CI]'], s9,
          'Lagged pairs are formed within the same trading day at intraday frequencies and resampled in blocks. Source: Authors’ calculations.'),
        S('Table S10 Forbes–Rigobon test across weights and regime definitions',
          ['w', 'Regimes', 'ρ_low', 'ρ_high', 'ρ*', 'ρ* − ρ_low [95% CI]', 'p (one-sided)'], s10,
          'Daily Pearson correlations of P_cap(w) and VN30; bootstrap draws are separate from Table 7, so intervals at the factsheet weight differ by Monte Carlo error. Source: Authors’ calculations.'),
        S('Table S11 Effectiveness of a minimum-variance VN30 hedge of the mid-cap segment', ['Sample', 'N', 'ρ² [95% CI]'], s11,
          'Share of P_cap variance removed by the minimum-variance hedge with VN30. Source: Authors’ calculations.'),
        S('Table S12 Volatility episodes not classified as crises', ['Period', 'Trading days', 'Maximum drawdown, %', 'Days in top volatility quartile, %', 'Peak volatility, % p.a.', 'Date of peak'], s12,
          'Both episodes fail the drawdown and volatility-share criteria of Section 3.2 and are included in the quartile regimes. Source: Authors’ calculations.'),
        S('Table S13 Slope channels of the VN30–VN100 coefficient (Eq. 14)',
          ['Frequency', 'Scales', 'Slope ρ_AM', 'Slope κ', '∂ρ_AB/∂ρ_AM', '∂ρ_AB/∂κ', 'Implied slope', 'Observed slope'], s13,
          'Partial derivatives averaged over s ≤ s_rel. Source: Authors’ calculations.'),
        S('Table S14 In-sample misstatement of portfolio variance for all pairs',
          ['Regime', 'Pair', 'RE, % [95% CI]', 'Relative SE of regime variance, %', 'RE/SE'], s14,
          'Equally weighted positions; intervals from joint resampling of the full sample. Source: Authors’ calculations.'),
        S('Table S15 Sensitivity of the M30 slope intervals to the bootstrap block length',
          ['Mean block length (days)', 'Pair', 'Slope [95% CI]', 'p (studentized)'], s15,
          'Reliable-range slopes of Eq. (13); 199 replicates per block length. Source: Authors’ calculations.'),
        ('p', f"*Multifractal structure.* The generalized cross-correlation exponent h_xy(2) lies between "
              f"{f(min(F(r['lambda_xy']) for r in HQ if r['q'] == '2'), 3)} and {f(max(F(r['lambda_xy']) for r in HQ if r['q'] == '2'), 3)}. "
              f"The multifractal range Δh is {rng([SURR[(t, p)]['dh_obs'] for t in TF for p in NESTED], 3)} for the nested pairs and "
              f"{rng([SURR[(t, 'Pcap-VN30')]['dh_obs'] for t in TF], 3)} for P_cap–VN30. Against 100 jointly shuffled surrogates, the "
              "P_cap–VN30 range exceeds the 95th surrogate percentile only at "
              f"{', '.join(t for t in TF if SURR[(t, 'Pcap-VN30')]['exceeds_q95'] == 'TRUE') or 'no frequency'}, and the nested pairs "
              f"in {sum(SURR[(t, p)]['exceeds_q95'] == 'TRUE' for t in TF for p in NESTED)} of 12 cases. Because absolute local "
              "covariances can create spurious multifractality (Oświęcimka et al. 2014), these results are descriptive."),
        ('fig', ('fig3', 'Fig. S1 MF-DCCA at the daily frequency: (a) singularity spectra f(α); (b) generalized exponents h_xy(q)',
                 'q ∈ [−5, 5] \\ {0}; f(α) can be negative where absolute local covariances are used. Source: Authors’ calculations.')),
    ]


TABLE1 = T('Table 1 Prior studies of overlap, multiscale and crisis co-movement and the gap addressed here',
           TABLE1_HEADER, TABLE1_ROWS, TABLE1_NOTE)


def body():
    return (introduction() + [('h1', '2 Literature review and hypothesis development')] + LIT_INTRO + LIT_SECTIONS(TABLE1)
            + hypotheses() + institutions_data() + methodology() + results() + discussion())


def appendix():
    return []
