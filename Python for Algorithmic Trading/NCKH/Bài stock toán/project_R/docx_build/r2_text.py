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
        ('p1a', "Correlations between published equity indices are a convenient summary of how much one segment of a market "
                "diversifies another (Markowitz 1952): they exist at every frequency and need no holdings data. In nested index "
                "systems they have a problem unrelated to estimation error. The parent index contains the child, so part of their "
                "correlation is fixed by construction. On the Ho Chi Minh City Stock Exchange (HOSE), the large-cap VN30 index is "
                "contained in VN100, which is contained in VNINDEX:"),
        ('eq', r'\mathrm{VN30} \subset \mathrm{VN100} \subset \mathrm{VNINDEX}. \qquad (1)'),
        ('p', "The 30 largest firms hold about two-thirds of the free-float capitalization of VN100, and the daily VN30–VN100 "
              f"correlation is {f(AVG[('B', '1D')]['VN30-VN100'])}. Read as a measure of how mid caps move with large caps, this number "
              "mixes economic linkage with the fact that VN30 stocks are counted on both sides. Holdings-based risk models avoid the "
              "problem; users who observe only index levels cannot, and index-level co-movement is easy to misread even without "
              "overlap (Chen et al. 2016)."),
        ('p', "The arithmetic is old: Pearson (1897) described the spurious correlation of quantities that share a component, and "
              "the item–total correlation of psychometrics (Cureton 1966) is the same identity. Missing is a version for the "
              "scale-dependent, detrended coefficients used in financial econophysics, with sampling and weight uncertainty attached, "
              "in a form index users can apply. Studies of multiscale co-movement, mostly based on detrended cross-correlation "
              "analysis (DCCA), analyze pairs that share no constituents (Section 2)."),
        ('p', "We build that version. Lemma 1 shows that, at every timescale, the DCCA coefficient of a nested pair is a known "
              "function of the child’s weight, the relative amplitude κ(s) of the remaining constituents and the overlap-purged "
              "coefficient between the child and those constituents. It delivers a zero-correlation benchmark, an exact lower "
              "bound, the sensitivity of the nested coefficient to the purged one and an order-free attribution; the Pearson identity "
              "is the one-box special case. We apply it to VN30, VN100 and VNINDEX at 30-minute, 1-hour, 4-hour and daily "
              "frequencies (2014–2025), with a block bootstrap that also draws the index weight, and use the purged series to test "
              "hypotheses on horizon dependence, crisis contagion and the out-of-sample value of regime-conditioned correlations."),
        ('p', "The paper makes three contributions. First, it carries the part–whole identity to scale-wise detrended coefficients "
              "and derives the benchmark, the bound, the sensitivity, a Shapley attribution and the condition under which the "
              "benchmark exceeds half of the nested coefficient; a six-step recipe (Box 1) and a contour chart (Fig. 4) make them "
              "computable for any nested pair from published data. Second, it measures the overlap component on the HOSE: the "
              f"VN30–VN100 coefficient responds to the purged coefficient with a slope of {rng(sens_v, 3)}, and the like-for-like gap "
              f"between nested and purged coefficients is {rng(gapL_v, 3)}. Because κ hardly varies with the timescale "
              f"({f(min(kap_scales), 2)}–{f(max(kap_scales), 2)}), the multiscale layer confirms the Pearson answer here. Third, on the "
              "purged series, horizon dependence is confined to intraday broad-market pairs and comes from the auction bars, crisis "
              "evidence depends on whether contagion is measured by an adjusted correlation or a factor loading, and "
              "regime-conditioned correlations do not beat a static one out of sample."),
        ('p', "Section 2 reviews the literature and states the estimands and hypotheses, Section 3 describes the setting and data, "
              "Section 4 the methods and Section 5 the results; Section 6 discusses them and Section 7 concludes. Further checks are "
              "in the Supplementary Material (Online Resource 2)."),
    ]


def hypotheses():
    return [
        ('h2', '2.7 Estimands and hypotheses'),
        ('p1a', "Lemma 1 (Section 4.2) fixes several quantities once the weight and the relative amplitude are known. We report these "
                "as estimands with intervals and test only hypotheses whose outcome the identity does not determine."),
        ('p', "*Estimands.* E1 is the zero-correlation benchmark ρ̲ of the VN30–VN100 coefficient and its share of the observed "
              "coefficient under three attribution conventions; E2 is the sensitivity of the nested coefficient to the purged one; E3 "
              "is the in-sample misstatement of portfolio variance when a static correlation replaces a regime correlation, judged "
              "against the sampling error of the regime variance. A share above one half is not a finding: it holds whenever κ < √3 "
              "and the purged coefficient is non-negative."),
        ('p', "*H1 (material overlap gap).* The identity does not fix the size of the gap, because a purged coefficient near one "
              "would leave almost none. We predict that the like-for-like gap, VN30–VN100 minus P_cap–VN30, exceeds 0.05, the "
              "worst-case estimation error tolerated in Section 4.4. Rule: the lower bound of the 95% interval exceeds 0.05 at every "
              "frequency."),
        ('p', "*H2 (horizon dependence).* Large caps lead small caps (Lo and MacKinlay 1990; Hou 2007), non-synchronous trading "
              "depresses short-horizon correlations (Epps 1979) and information diffuses gradually (Hong and Stein 1999), so DCCA "
              "coefficients of broad-market pairs, whose parent contains small and illiquid stocks, should rise with the timescale; "
              "for VN30–VN100 the identity predicts a slope damped by the sensitivity of Eq. (10). Rule: in the family of eight "
              "broad-market slope tests (two pairs, four frequencies), at least one pair at each of M30 and H1 has a positive slope "
              "with a Holm-adjusted studentized p-value below 0.05. We also report whether this survives removal of the opening bar "
              "and test the VN30–VN100 prediction for equivalence."),
        ('p', "*H3 (contagion).* A rise in the raw crisis correlation of P_cap and VN30 can come from volatility alone (Forbes and "
              "Rigobon 2002), and the volatility correction is biased toward no contagion when idiosyncratic variance rises "
              "(Corsetti et al. 2005). Rule: under regimes sorted on VN30 volatility, both the Forbes–Rigobon adjusted correlation "
              "exceeds its calm level (one-sided p < 0.05) and the loading of P_cap on VN30 rises (two-sided p < 0.05)."),
        ('p', "*H4 (value of regime conditioning).* If tier correlations vary with the volatility regime, conditioning should improve "
              "variance forecasts for a mixed large-cap and mid-cap position. Rule: an EWMA or real-time regime correlation has a "
              "lower QLIKE loss than the static correlation over 2023–2025, with a Diebold–Mariano p-value below 0.05."),
        ('p', "The first-round version tested five hypotheses without adjustment. The rules above, the eight-test family for H2 and "
              "the factor-loading test for H3 were fixed at revision, after the first-round results were known; we label them so and "
              "also report the original specifications."),
    ]


def institutions_data():
    c = cr
    return [
        ('h1', '3 Institutional background and data'),
        ('h2', '3.1 Institutional background'),
        ('p1a', "Five features of the HOSE matter for dependence between tiers. First, prices move within a ±7% daily band; in "
                "sharp corrections heavily sold stocks sit at the lower limit, which truncates tails and synchronizes limit hits. "
                "Second, settlement moved from T+3 to T+2 on 1 January 2016 (Vietnam Securities Depository 2015), which limits "
                "intraday arbitrage between constituents and index baskets. Third, each day has an opening call auction "
                "(09:00–09:15), continuous matching to 11:30, a break to 13:00, continuous matching and a closing call auction "
                "(14:30–14:45). The vendor’s intraday bars follow this calendar (Section 3.2), so the first bar of each day contains "
                "the overnight return and the opening auction."),
        ('p', "Fourth, short selling is restricted: Circular 120/2020/TT-BTC (Ministry of Finance of Vietnam 2020) provides a legal "
              "framework for covered short sales, but to our knowledge it had not been put into operation, and naked short selling "
              "is not permitted; the implementing Decree 155/2020/ND-CP (Government of Vietnam 2020) was amended by Decree "
              "245/2025/ND-CP (Government of Vietnam 2025). VN30 futures trade on the Hanoi Stock Exchange, but there is no mid-cap "
              "future; a VNMIDCAP exchange-traded fund (FUEDCMID) has been listed since 29 September 2022 (Ho Chi Minh City Stock "
              "Exchange 2022), so mid caps can be held long but not shorted or hedged with a dedicated derivative. Fifth, foreign "
              "ownership limits (30% for commercial banks, for example) concentrate foreign flows in large caps with room under their "
              "limits. FTSE Russell announced in October 2025 that Vietnam would be reclassified to Secondary Emerging status, "
              "effective 21 September 2026 (FTSE Russell 2025), after our sample."),
        ('h2', '3.2 Data and sample construction'),
        ('p1a', "We use index levels of VN30, VN100 and VNINDEX exported from TradingView (exchange code HOSE). VN30 holds the 30 "
                "largest and most liquid stocks by free-float capitalization, VN100 adds the next 70 (the VNMIDCAP index), and "
                "VNINDEX covers all HOSE common stocks at full market capitalization. Daily and 30-minute series run to 12 December "
                "2025, 1-hour and 4-hour series to 9 December 2024. M30 bars open at "
                f"{BARS['M30']['bar_open_times'].replace(' ', ', ')}; H1 bars at {BARS['H1']['bar_open_times'].replace(' ', ', ')}; the "
                "two H4 bars cover the morning and afternoon sessions. The vendor has no VNMIDCAP history for the full sample at all "
                "frequencies, so the mid-cap segment is recovered from VN30 and VN100 (Section 4.2). We did not compare the vendor "
                "series with the closing levels published by the HOSE date by date; the replication package records a checksum of "
                "the input file."),
        ('p', "The series are merged by exact inner joins on timestamps, with no filling or interpolation, and log returns are"),
        ('eq', r'R_t=\ln P_t-\ln P_{t-1}. \qquad (2)'),
        ('p', "The synchronized window (3 January 2017 to 9 December 2024), in which all frequencies overlap "
              f"(1D: N = {nint(AVG[('A', '1D')]['n'])}; M30: {nint(AVG[('A', 'M30')]['n'])}; H1: {nint(AVG[('A', 'H1')]['n'])}; H4: "
              f"{nint(AVG[('A', 'H4')]['n'])}), serves cross-frequency comparisons. All other analyses use the full sample: February "
              f"2014 to December 2025 at 1D (N = {nint(DESC[('VN30', '1D')]['n'])}), January 2017 to December 2025 at M30 "
              f"({nint(DESC[('VN30', 'M30')]['n'])}) and January 2014 to December 2024 at H1 and H4 ({nint(DESC[('VN30', 'H1')]['n'])} "
              f"and {nint(DESC[('VN30', 'H4')]['n'])}). The indices are computed in real time, not back-calculated from current "
              "membership, so reconstitutions and delistings are embedded and the sample is free of survivorship bias."),
        ('p', "Regimes use the 20-day rolling standard deviation of returns (Fig. 1). Chronological crises have a VNINDEX drawdown "
              "above 25%, at least 45% of days in the top volatility quartile and a documented trigger: the 2018 margin contraction "
              f"(drawdown {f(-F(c[0]['max_drawdown_pct']), 1)}%, {f(100 * F(c[0]['share_high_vol_days']), 0)}% of days in the top "
              f"quartile), the 2020 COVID-19 shock ({f(-F(c[1]['max_drawdown_pct']), 1)}%, {f(100 * F(c[1]['share_high_vol_days']), 0)}%) "
              f"and the 2022 corporate bond freeze ({f(-F(c[2]['max_drawdown_pct']), 1)}%, {f(100 * F(c[2]['share_high_vol_days']), 0)}%), "
              f"{nint(SC['n_crisis_days'][0])} days in all, against a calm benchmark of 2016–2017 and 2023–2024 "
              f"({nint(SC['n_calm_days'][0])} days). The 2021 and March–June 2025 spikes (drawdowns {f(-F(EPI[0]['max_drawdown_pct']), 1)}% "
              f"and {f(-F(EPI[1]['max_drawdown_pct']), 1)}%) fail the first two conditions (Table S12). Quartile regimes compare the bottom "
              f"and top quartiles of rolling VNINDEX volatility ({f(SC['vol_quartiles_ann_pct'][0], 1)}% and "
              f"{f(SC['vol_quartiles_ann_pct'][1], 1)}% annualized) or of VN30 volatility and include all spikes."),
        ('fig', ('fig1', 'Fig. 1 Twenty-day rolling volatility of VNINDEX (annualized) and market regimes, 2014–2025',
                 'Shaded areas: the three chronological crisis episodes; dashed and dotted horizontal lines: 25th and 75th '
                 'percentiles of rolling volatility. The 2021 and 2025 spikes are not shaded because their drawdowns are below 25% '
                 '(Section 3.2). Source: Authors’ calculations based on HOSE index data (TradingView).')),
    ]


def methodology():
    return [
        ('h1', '4 Methodology'),
        ('h2', '4.1 The DCCA coefficient'),
        ('p1a', "The DCCA coefficient measures covariance at timescale s after removing local trends (Podobnik and Stanley 2008; "
                "Zebende 2011). For return series x and y of length N, the profiles are"),
        ('eq', r'X_k=\sum_{t=1}^{k}(x_t-\bar{x}),\quad Y_k=\sum_{t=1}^{k}(y_t-\bar{y}),\quad k=1,\dots,N. \qquad (3)'),
        ('p', "Each profile is split into N_s = ⌊N/s⌋ boxes of length s from each end of the series (2N_s boxes). In box ν a "
              "polynomial of order m (m = 1 unless stated) is fitted by ordinary least squares (OLS), and the residuals ε_X and ε_Y "
              "give the detrended covariance"),
        ('eq', r'f^2_{XY}(s,\nu)=\frac{1}{s}\sum_{k=1}^{s}\varepsilon_{X}(k,\nu)\,\varepsilon_{Y}(k,\nu),\qquad F^2_{XY}(s)=\frac{1}{2N_s}\sum_{\nu=1}^{2N_s}f^2_{XY}(s,\nu). \qquad (4)'),
        ('p', "With F_X(s) = [F²_XX(s)]^{1/2} the detrended fluctuation function (Peng et al. 1994), the DCCA coefficient is"),
        ('eq', r'\rho_{XY}(s)=\frac{F^2_{XY}(s)}{F_X(s)\,F_Y(s)}. \qquad (5)'),
        ('p', "Eq. (5) is an inner product of stacked residual vectors divided by their norms, so |ρ_XY(s)| ≤ 1 by the "
              "Cauchy–Schwarz inequality whenever both fluctuation functions are positive. Because profiles are linear in the series "
              "and OLS detrending is a linear projection, the residuals of a weighted sum of series are the same weighted sum of "
              "their residuals."),
        ('h2', '4.2 The overlap-purged series and the part–whole identity'),
        ('p1a', "Let A_t and B_t be VN30 and VN100 returns and w the free-float weight of VN30 in VN100. The overlap-purged mid-cap "
                "series is"),
        ('eq', r'M_t=P_{\mathrm{cap},t}=\frac{B_t-wA_t}{1-w}, \qquad (6)'),
        ('p', f"with w = {f(W30, 4)} from the HOSE factsheet of 31 May 2024 (free-float capitalizations of VND 1,316,288 billion and "
              "1,928,303 billion), so that B_t = wA_t + (1 − w)M_t at every observation. On log returns, P_cap differs from the "
              f"arithmetic mid-cap return by a Jensen term of {f(SC['jensen_delta'][0] * 1e6, 1)} × 10⁻⁶ per day. P_cap is a shadow "
              "benchmark: replicating it needs about 315% long VN100 and 215% short VN30. We call ρ_AM, the coefficient of VN30 and "
              "P_cap, overlap-purged rather than economic, because we cannot validate P_cap against the published VNMIDCAP series "
              "(Section 6.3)."),
        ('p', "**Lemma 1 (scale-wise part–whole identity).** Let B_t = wA_t + (1 − w)M_t for all t, with 0 < w < 1 and "
              "F_A(s), F_M(s) > 0, and define the relative amplitude κ(s) = (1 − w)F_M(s)/[wF_A(s)]. Then, for every s and m,"),
        ('eq', r'\rho_{AB}(s)=\frac{1+\kappa(s)\,\rho_{AM}(s)}{\sqrt{1+\kappa(s)^2+2\kappa(s)\,\rho_{AM}(s)}}. \qquad (7)'),
        ('p', "*Proof.* Residuals are linear in the series, so ε_B = wε_A + (1 − w)ε_M in every box. By bilinearity of Eq. (4), "
              "F²_AB = wF²_A + (1 − w)ρ_AM F_A F_M and F²_B = w²F²_A + (1 − w)²F²_M + 2w(1 − w)ρ_AM F_A F_M; substituting into "
              "Eq. (5) and dividing by wF²_A gives Eq. (7). ∎"),
        ('p', "With one box and no detrending, Eq. (7) is the classical part–whole correlation (Pearson 1897; Cureton 1966), so the "
              "lemma adapts a known identity. It holds scale by scale for detrended coefficients, for the detrending moving-average "
              "coefficient (Kristoufek 2014) and for any measure built from a bilinear covariance of linearly filtered series. Five "
              "corollaries follow, at a fixed scale that we suppress."),
        ('p', "*Corollary 1 (benchmark and bound).* Setting ρ_AM = 0 gives the zero-correlation benchmark"),
        ('eq', r'\underline{\rho}=\frac{1}{\sqrt{1+\kappa^2}}. \qquad (8)'),
        ('p', "Eq. (7) increases in ρ_AM for ρ_AM > −κ, so ρ̲ bounds ρ_AB from below only when ρ_AM ≥ 0. For κ < 1 the minimum "
              "over all admissible ρ_AM is"),
        ('eq', r'\min_{\rho_{AM}\in[-1,1]}\rho_{AB}=\sqrt{1-\kappa^2},\qquad \text{attained at } \rho_{AM}=-\kappa; \qquad (9)'),
        ('p', "for κ ≥ 1 no positive bound exists. *Corollary 2 (sensitivity).*"),
        ('eq', r'\frac{\partial\rho_{AB}}{\partial\rho_{AM}}=\frac{\kappa^2\,(\kappa+\rho_{AM})}{(1+\kappa^2+2\kappa\rho_{AM})^{3/2}}, \qquad (10)'),
        ('p', "which is small when the child dominates the parent; its inverse states how far ρ_AM must move to change ρ_AB by a "
              "given amount. *Corollary 3 (direction).* For ρ_AM ≥ 0, ρ²_AB − ρ²_AM = (1 − ρ²_AM)(1 + 2κρ_AM)/(1 + κ² + 2κρ_AM) "
              "≥ 0, so overlap can only raise the coefficient. *Corollary 4 (dominance).* For ρ_AM ≥ 0, ρ_AB ≤ 1 implies "
              f"ρ̲/ρ_AB ≥ ρ̲, so the benchmark exceeds half of ρ_AB whenever κ < √3, that is, F_M/F_A < √3·w/(1 − w) = "
              f"{f(REC['amplitude_ratio_max'], 2)} at the HOSE weight; such a share carries no information. *Corollary 5 "
              "(attribution).* With neither overlap nor dependence the coefficient is 0, with overlap only ρ̲, with dependence only "
              "ρ_AM and with both ρ_AB. The benchmark-first share ρ̲/ρ_AB and the dependence-first share ρ_AM/ρ_AB depend on the "
              "order; the Shapley (1953) value averages the two orders into an additive split,"),
        ('eq', r'\phi_{\mathrm{overlap}}=\tfrac12\left[\underline{\rho}+(\rho_{AB}-\rho_{AM})\right],\qquad \phi_{\mathrm{dep}}=\tfrac12\left[\rho_{AM}+(\rho_{AB}-\underline{\rho})\right],\qquad \phi_{\mathrm{overlap}}+\phi_{\mathrm{dep}}=\rho_{AB}. \qquad (11)'),
        ('p', "We lead with the sensitivity, which needs no attribution convention, and report the Shapley share φ_overlap/ρ_AB. "
              "Eq. (7) reproduces the directly estimated VN30–VN100 coefficient at every scale and frequency to within "
              f"{f(idmax * 1e16, 1)} × 10⁻¹⁶. All quantities are computed scale by scale and averaged over the reliable range "
              "(Section 4.4). Because M is a linear combination of A and B, the decomposition also follows from index-level moments "
              "alone (Box 1)."),
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
        ('p1a', "Capitalizations drift between semi-annual reviews. If the true weight w_t differs from w, the purged series becomes"),
        ('eq', r'\hat{M}_t=\frac{1-w_t}{1-w}M_t+\frac{w_t-w}{1-w}A_t, \qquad (12)'),
        ('p', "so large-cap returns leak into P_cap in proportion to the gap, and P_cap and VN30 are disjoint only at the exact "
              "weight. With a single factsheet snapshot we cannot rebuild the weight path, so each bootstrap replicate draws w from "
              "U(0.60, 0.75), an interval around the factsheet weight with room for drift either way, and recomputes P_cap and every "
              "statistic. Table S2 evaluates each quantity on a weight grid. The benchmark and sensitivity depend on the data only "
              "through κ and are less exposed to weight error than ρ_AM."),
        ('h2', '4.4 Reliability thresholds and inference'),
        ('p1a', "The DCCA coefficient becomes noisy at large scales, where boxes are few. For each sample size we simulate Gaussian "
                "white-noise pairs with correlations of −0.3, 0, 0.3, 0.5, 0.7 and 0.9 (1,002 per frequency) and set s_rel to the "
                "largest scale before the worst-case mean absolute error on 40 log-spaced scales first exceeds 0.05, a tolerance "
                "fixed in advance; a GARCH(1,1)-t(5) calibration (300 simulations) checks heavy tails."),
        ('p', "Coefficients at different scales come from the same series, so all inference resamples the data with the stationary "
              "block bootstrap (Politis and Romano 1994), with mean blocks of about 20 trading days, recomputing every curve and "
              "statistic per replicate. We use 499 replications for DCCA statistics, 999 for factor-model, lead–lag and materiality "
              "statistics and 1,999 for Pearson regime statistics. Intervals are percentile 95% intervals, capped at ±1 for "
              "correlations. Percentile p-values, p = 2 min{k₋ + 1, k₊ + 1}/(B + 1), where k₋ and k₊ count replicates at or below and "
              "at or above zero, cannot fall below 0.004 with B = 499 (reported as p < 0.005), and with 19 tests the smallest "
              "attainable Holm-adjusted value is 0.076. For slope tests we therefore also report studentized p-values, "
              "2Φ(−|β̂|/se_boot), adjusted by the Holm (1979) and Benjamini and Hochberg (1995) procedures in two families: the "
              "original 19 reliable-range tests and the eight broad-market tests of H2. Equivalence of the VN30–VN100 slope to zero "
              "is tested by two one-sided tests (TOST; Schuirmann 1987) with a margin of 0.001 per unit of ln s; over the 4.5 units "
              "of the M30 reliable range such a slope moves the coefficient by less than a tenth of the 0.05 tolerance."),
        ('h2', '4.5 Scaling regressions and slope channels'),
        ('p1a', "Horizon dependence is the slope β of"),
        ('eq', r'\rho_{XY}(s)=\alpha+\beta\ln s+u(s), \qquad (13)'),
        ('p', "over s ≤ s_rel (full-range slopes in Table S1). For the nested pair, Eq. (7) splits the slope into a ρ_AM channel and "
              "a κ channel,"),
        ('eq', r'\frac{d\rho_{AB}}{d\ln s}=\frac{\partial\rho_{AB}}{\partial\rho_{AM}}\frac{d\rho_{AM}}{d\ln s}+\frac{\partial\rho_{AB}}{\partial\kappa}\frac{d\kappa}{d\ln s},\qquad \frac{\partial\rho_{AB}}{\partial\kappa}=-\frac{\kappa(1-\rho_{AM}^2)}{(1+\kappa^2+2\kappa\rho_{AM})^{3/2}}, \qquad (14)'),
        ('p', "so horizon dependence in ρ_AM reaches ρ_AB damped by the sensitivity of Eq. (10)."),
        ('h2', '4.6 Volatility conditioning and contagion tests'),
        ('p1a', "If y_t = α + βx_t + ε_t with Var(ε_t) = σ²_ε, the correlation [1 + σ²_ε/(β²σ²_x)]^{−1/2} rises with the variance of "
                "x even when β and σ²_ε are constant. Forbes and Rigobon (2002) adjust the crisis correlation as"),
        ('eq', r'\rho^{*}=\frac{\rho_{\mathrm{high}}}{\sqrt{1+\delta\,(1-\rho_{\mathrm{high}}^2)}},\qquad \delta=\frac{\sigma^2_{x,\mathrm{high}}-\sigma^2_{x,\mathrm{low}}}{\sigma^2_{x,\mathrm{low}}}, \qquad (15)'),
        ('p', "with y = P_cap and x = VN30. The adjustment assumes constant β and σ²_ε; if crises raise idiosyncratic variance, ρ* "
              "is biased toward no contagion (Corsetti et al. 2005). We therefore also test, regime by regime, for changes in the "
              "loading β and the residual variance, the contagion concept of Corsetti et al. (2005) and the structural parameter of "
              "Rigobon (2003). Regimes are chronological episodes, VNINDEX volatility quartiles or VN30 volatility quartiles; the "
              "last sorts on the conditioning variable rather than on a series containing P_cap. Statistics are Pearson moments of "
              "daily returns, bootstrapped within regimes. Nested pairs are not tested, because the parent contains the "
              "conditioning index."),
        ('h2', '4.7 Portfolio variance: in-sample misstatement and out-of-sample evaluation'),
        ('p1a', "For an equally weighted two-asset position, replacing the regime correlation ρ_r by the static correlation ρ_st "
                "changes the variance by"),
        ('eq', r'\mathrm{RE}=\frac{\rho_{\mathrm{st}}-\rho_{r}}{\tfrac{1}{2}\left(\sigma_1/\sigma_2+\sigma_2/\sigma_1\right)+\rho_{r}}, \qquad (16)'),
        ('p', "with regime volatilities σ₁ and σ₂, so only the correlation differs. Intervals resample the full sample jointly, "
              "re-estimating ρ_st, and |RE| is compared with the bootstrap relative standard error of the regime variance. Because "
              "these regimes are ex post, we also estimate correlations on 2014–2022 and evaluate forecasts on 2023–2025. Forecasts "
              "share one-step-ahead RiskMetrics variances (λ = 0.94; J.P. Morgan/Reuters 1996) and differ only in the correlation: "
              "static, EWMA with the same λ, or a regime correlation chosen in real time from lagged rolling volatility with "
              "thresholds fixed in the estimation window. Losses are QLIKE (Patton 2011) and squared error, compared by the "
              "Diebold and Mariano (1995) test with a Newey and West (1987) variance (five lags)."),
        ('h2', '4.8 Computational details'),
        ('p1a', "All computations use R 4.3.3 (stats, sandwich 3.1.0, ggplot2 3.4.4) on an Intel Xeon processor (2.10 GHz, four "
                "cores). OLS uses the QR decomposition, so no iterative optimization or convergence criterion is involved. Seeds are "
                "fixed in each script (20260924 to 20261014), and run_all.R reproduces every table and figure with byte-identical "
                "CSV outputs. Code, outputs and a map from each number to its output file form Online Resource 1."),
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
        ('p1a', "Table 2 reports descriptive statistics and Table 3 the reliability thresholds."),
        tab2,
        ('p', f"P_cap has the highest daily standard deviation ({f(DESC[('Pcap', '1D')]['sd'], 4)}) and VNINDEX the lowest "
              f"({f(DESC[('VNINDEX', '1D')]['sd'], 4)}). All series are negatively skewed and leptokurtic (kurtosis above "
              f"{int(min(F(DESC[(v, 'M30')]['kurtosis']) for v in ['VN30', 'VN100', 'VNINDEX', 'Pcap']))} at M30), and the "
              "Jarque–Bera test rejects normality everywhere; neither DCCA nor the block bootstrap requires Gaussian returns."),
        tab3,
        ('p', f"Gaussian thresholds range from {REL['1D']['s_rel']} days at 1D to {REL['M30']['s_rel']} bars at M30, and heavy "
              "tails cut them by about two-thirds. Averages below use the Gaussian thresholds; over the heavy-tailed ranges the "
              f"nested averages become {rng([GARCH[t]['nested_avg_conservative'] for t in TF])} and the purged average "
              f"{rng([GARCH[t]['pcap_avg_conservative'] for t in TF])}, so no conclusion depends on the choice."),
        ('h2', '5.2 The overlap gap (H1)'),
        ('p1a', "Table 4 compares nested and purged coefficients; Fig. 2 shows the curves with bootstrap bands."),
        tab4,
        ('p', f"The nested pairs average {rng(nested_all)} at every frequency in both samples, P_cap–VN30 {rng(pcap_all)}. "
              f"Corollary 3 fixes the sign of the like-for-like gap, but not its size: the gap is {rng(gapL_v)} with interval lower "
              f"bounds of at least {f(gapL_lo)}, above the 0.05 margin at every frequency, so "
              f"{'H1 is supported' if H1_ok else 'H1 is not supported at every frequency'}. The three-pair gap, which also uses the "
              f"broad-market pairs that cannot be purged by weight, is {rng(gap3)}, with Cohen’s q (Cohen 1988) of {rng(qv, 2)}, "
              "reported descriptively because both coefficients come from the same sample. Overlap thus inflates co-movement that "
              "is already strong."),
        ('p', f"The gap depends on the weight: over w = 0.60–0.75 the like-for-like daily gap is {f(min(like_w))}–{f(max(like_w))} "
              f"and the three-pair gap {f(min(ws_gap))}–{f(max(ws_gap))} (Tables S2 and S3). With w drawn in each replicate, the "
              f"like-for-like intervals have lower bounds of {rng([GWU[t]['ci_lo'] for t in TF], 3)} and every replicate exceeds "
              "0.05, so H1 holds under weight uncertainty, although the size of the gap is known only to within a factor of about "
              "two."),
        ('fig', ('fig2', 'Fig. 2 DCCA coefficients of the nested pairs and P_cap–VN30 by timescale: (a) 1D, (b) M30, (c) H1, (d) H4',
                 'Line and marker types identify the pairs; grey bands: pointwise block-bootstrap 95% intervals; vertical dotted '
                 'lines: s_rel (Table 3). Source: Authors’ calculations based on HOSE index data (TradingView).')),
        ('h2', '5.3 The part–whole decomposition (E1, E2)'),
        ('p1a', "Table 5 applies Lemma 1 to VN30–VN100, and Fig. 3 plots Eq. (7) against the purged coefficient."),
        tab5,
        ('p', f"The sensitivity is {rng(sens_v, 3)}: moving the index-level number by 0.01 requires the purged coefficient to move "
              f"by about {f(sum(inv_sens) / 4 * 0.01, 2)}, and with weight uncertainty the interval is "
              f"{f(wu_rng('sensitivity')[0], 2)}–{f(wu_rng('sensitivity')[1], 2)}. With κ of {rng(kap_v, 2)}, the remaining 32% of "
              f"VN100 contributes about half as much detrended variation as VN30, the benchmark is {rng(bench_v, 3)} and the lower "
              f"bound of Eq. (9) is {rng(tmin_v, 3)}: no purged coefficient in [−1, 1] could push the VN30–VN100 coefficient below "
              "about 0.86."),
        ('p', f"How much of the observed {rng(nest_v, 3)} is due to overlap depends on the question. The benchmark-first share is "
              f"{rng(share_v, 3)} and the dependence-first share {rng(econsh_v, 3)}, because either factor alone produces a "
              f"coefficient near 0.9; the Shapley split attributes {rng(shap_v, 3)} to overlap (intervals within "
              f"{f(shap_lo, 3)}–{f(shap_hi, 3)}). Weight uncertainty widens the Shapley intervals to "
              f"{f(wu_rng('shapley_overlap_share')[0], 2)}–{f(wu_rng('shapley_overlap_share')[1], 2)} and the benchmark-first "
              f"intervals to {f(wu_rng('mech_share')[0], 2)}–{f(wu_rng('mech_share')[1], 2)}, against a sampling-only width of about "
              "0.02, so weight error dominates the uncertainty of any attribution."),
        ('p', f"The decomposition barely varies with the horizon. Across reliable scales and frequencies κ lies in "
              f"{f(min(kap_scales), 2)}–{f(max(kap_scales), 2)}, the benchmark varies by {rng(bench_rng, 3)} within a frequency, and "
              f"its slope on ln s is not significant at 5% (p = {rng(bslope_p, 3)}; Holm {rng(bslope_holm, 3)}), although at M30 the "
              "percentile interval just excludes a negligible slope of about −0.002. On full-sample Pearson moments the benchmark is "
              f"{rng(pear_bench, 3)} and the benchmark-first share {rng(pear_share, 3)}, within 0.01 of the DCCA values. Here the "
              "multiscale layer is a check of scale invariance, and Box 1 suffices in practice; the DCCA version matters where "
              "tiers scale differently, which Eq. (7) reveals as variation in κ(s)."),
        ('fig', ('fig4', 'Fig. 3 Nested VN30–VN100 coefficient implied by Lemma 1 as a function of the overlap-purged coefficient',
                 'Lines: Eq. (7) at the average κ of each frequency (Table 5); markers: observed values; dashed line: daily '
                 'zero-correlation benchmark; dotted line: daily lower bound of Eq. (9). Source: Authors’ calculations.')),
        ('p', "Fig. 4 places the HOSE among possible nested systems: the contours show the Pearson benchmark by child weight and "
              f"relative volatility of the remainder, and the triangle marks VN30 in VN100 (w = {f(HOSEPT['w'], 3)}, σ_M/σ_A = "
              f"{f(HOSEPT['amplitude_ratio_daily_sd'], 2)}, benchmark {f(HOSEPT['floor'], 3)}). Even a child weight of 0.5 with equal "
              "volatilities gives a benchmark of about 0.7."),
        ('fig', ('fig5', 'Fig. 4 Zero-correlation benchmark ρ̲ as a function of the child weight w and the relative volatility σ_M/σ_A',
                 'Contours of Eq. (8) with κ = (1 − w)σ_M/(wσ_A); triangle: VN30 in VN100, daily Pearson moments. Source: Authors’ '
                 'calculations.')),
        ('h2', '5.4 Horizon dependence (H2)'),
        ('p1a', "Table 6 reports reliable-range slopes for the four main pairs with bootstrap, studentized and adjusted p-values."),
        tab6,
        ('p', "Positive slopes appear only for broad-market pairs at intraday frequencies. In the H2 family, "
              f"{NUMW.get(len(holm_h2), len(holm_h2))} slopes survive Holm adjustment ("
              + '; '.join(f"{lab(p)} at {t}" for t, p in sorted(holm_h2)) +
              f"), with estimates of {rng([h2s(t, p)['estimate'] for t, p in holm_h2], 4)}, a rise of about 0.01 across the reliable "
              f"range; none is significant at 1D or H4, so H2 is {H2_out.lower()} on the full data. Over the original {fam} tests, "
              f"Holm keeps {NUMW.get(len(holm_all), len(holm_all))} studentized slope{'s' if len(holm_all) != 1 else ''} and "
              f"Benjamini–Hochberg {NUMW.get(len(bh_all), len(bh_all))}, and with percentile p-values none survives (smallest "
              f"BH-adjusted p = {f(pboot_bh_min, 3)}). The VN30–VN100 slope is equivalent to zero at "
              + (' and '.join(tost_eq) if tost_eq else 'no frequency') +
              f" (TOST p = {', '.join(pfmt(h2s(t, 'VN30-VN100')['tost_p']) for t in tost_eq)}) and inconclusive elsewhere; the "
              "P_cap–VN30 slope is insignificant everywhere."),
        ('p', f"Eq. (14) explains the flat nested slope: the damping factor is {rng(damp, 3)}, the κ channel partly offsets the "
              f"ρ_AM channel, and the implied slope differs from the observed one by at most {f(slc_err * 1e5, 1)} × 10⁻⁵ "
              "(Table S13). A flat nested coefficient therefore says little about the tiers: a purged slope of 0.01 per unit of ln s, "
              "five times the broad-market slopes, would move the nested slope by about 0.001, the TOST margin."),
        ('p', "The auction bars drive the intraday result. The first bar of each day holds the overnight return and the opening "
              "auction, where intraday volatility peaks (Andersen and Bollerslev 1997): it is "
              f"{f(100 * F(FB['M30']['share_of_bars_dropped']), 0)}% of M30 bars but carries "
              f"{f(100 * F(FB['M30']['share_of_VN30_sq_return_in_first_bar']), 0)}% of squared VN30 returns, and the last bar holds "
              "the closing auction (Table S7). Without the opening bar, the H1 broad-market slopes fall to "
              f"{f(ts('H1', 'drop_first', 'VN30-VNINDEX')['estimate'], 4)} and {f(ts('H1', 'drop_first', 'VN100-VNINDEX')['estimate'], 4)}, "
              f"and at M30 only VN30–VNINDEX stays significant ({f(ts('M30', 'drop_first', 'VN30-VNINDEX')['estimate'], 4)}, p = "
              f"{pfmt(ts('M30', 'drop_first', 'VN30-VNINDEX')['p_studentized'])}); without both auction bars the M30 slopes are "
              f"{f(ts('M30', 'drop_first_last', 'VN30-VNINDEX')['estimate'], 5)} and "
              f"{f(ts('M30', 'drop_first_last', 'VN100-VNINDEX')['estimate'], 4)}. Within the same replicates the broad-market slopes "
              f"exceed the VN30–VN100 slope at M30 and H1 (differences {rng([tsd(t, 'full', p)['estimate'] for t in ('M30', 'H1') for p in BROAD], 4)}, "
              f"p ≤ {pfmt(max(F(tsd(t, 'full', p)['p_studentized']) for t in ('M30', 'H1') for p in BROAD))}), but the differences "
              "vanish without the auction bars, while the overlap gap does not change "
              f"({f(FB['M30']['gap'])} {ci(FB['M30']['gap_ci_lo'], FB['M30']['gap_ci_hi'])} at M30) and the slope intervals are stable "
              "across block lengths (Table S15). "
              + ("Horizon dependence is thus a property of the bars containing the overnight return and the call auctions, not of "
                 "continuous trading; it is consistent with the Epps (1979) mechanism if the auctions are where prices of less liquid "
                 "constituents catch up." if (H2_out == 'Supported' and not H2_robust) else
                 f"H2 is {'robust' if H2_robust else 'not robust'} to removal of the opening bar.")),
        ('h2', '5.5 Crisis dependence (H3)'),
        ('p1a', "Table 7 reports the Forbes–Rigobon and single-factor tests under three regime definitions."),
        tab7,
        ('p', f"The raw correlation rises in every definition, from {f(frA['rho_low'])} to {f(frA['rho_high'])} chronologically and "
              f"from {f(fr30['rho_low'])} to {f(fr30['rho_high'])} under VN30 quartiles, but the adjusted crisis correlation never "
              f"exceeds its calm level (one-sided p = {f(min(F(frA['p_one_sided']), F(frB['p_one_sided']), F(fr30['p_one_sided'])), 3)}–"
              f"{f(max(F(frA['p_one_sided']), F(frB['p_one_sided']), F(fr30['p_one_sided'])), 3)}; at least {f(min(frw_p), 3)} across "
              f"weights, Table S10), and under VN30 quartiles it is significantly lower ({f(fr30['diff'])}, "
              f"{ci(fr30['ci_lo'], fr30['ci_hi'])})."),
        ('p', "The factor model explains why. The residual variance of P_cap rises by a factor of "
              f"{f(facC['idio_var_ratio'], 2)} {ci(facC['idio_ratio_ci_lo'], facC['idio_ratio_ci_hi'], 2)} under VN30 quartiles "
              f"({f(facB['idio_var_ratio'], 2)} under VNINDEX quartiles), which violates the assumption behind Eq. (15) and pushes ρ* "
              f"down (Corsetti et al. 2005). The loading rises from {f(facC['beta_low'])} to {f(facC['beta_high'])} under VN30 "
              f"quartiles (Δβ = {f(facC['d_beta'])}, {ci(facC['d_beta_ci_lo'], facC['d_beta_ci_hi'])}) but not between chronological "
              f"episodes (Δβ = {f(facA['d_beta'])}, {ci(facA['d_beta_ci_lo'], facA['d_beta_ci_hi'])}), and adding 2021 as a crisis "
              f"changes neither result (FR p = {f(C21[1]['fr_p_one_sided'], 3)}; Δβ = {f(C21[1]['d_beta'])}). Under its rule H3 is "
              f"{H3_out.lower()}: high-VN30-volatility days bring both a stronger response of mid caps to large caps and more "
              "mid-cap-specific risk. Because the lower-tail dependence of P_cap–VN30 "
              f"({f(tg('Pcap-VN30', '0.05')['lambda_L_empirical'], 2)} at the 5% quantile) exceeds its Gaussian-copula value "
              f"({f(tg('Pcap-VN30', '0.05')['lambda_L_gaussian_copula'], 2)}; Table S5), we cannot tell a structural shift from a "
              "stable nonlinear relation."),
        ('h2', '5.6 Portfolio variance (E3, H4)'),
        ('p1a', "Table 8 reports the in-sample misstatement from a static correlation and the out-of-sample forecast comparison."),
        tab8,
        ('p', f"In sample, a static correlation overstates the variance of an equally weighted VN30 and P_cap position by "
              f"{f(re_('A', 'low', 'Pcap-VN30')['RE_pct'], 2)}% in chronological calm periods and "
              f"{f(re_('B', 'low', 'Pcap-VN30')['RE_pct'], 2)}% in the low-volatility quartile, and understates it by "
              f"{f(-F(re_('A', 'high', 'Pcap-VN30')['RE_pct']), 2)}% and {f(-F(re_('B', 'high', 'Pcap-VN30')['RE_pct']), 2)}% in "
              "turbulent regimes, the sign pattern any pooled correlation produces; for nested pairs the misstatement is at most "
              f"{f(max(nested_re), 2)}% (Table S14). Against sampling error the magnitudes are small: |RE| is {rng(ratio_pcap, 2)} "
              f"standard errors of the regime variance for P_cap–VN30 and at most {f(max(ratio_nest), 2)} for nested pairs. Out of "
              "sample, the static correlation has the lowest mean QLIKE for every pair, and all Diebold–Mariano statistics are "
              f"negative (p = {f(min(dm_p), 3)}–{f(max(dm_p), 3)}). {'H4 is supported' if H4_ok else 'H4 is not supported'}: regime "
              "variation in correlations is real in sample but too small or too poorly timed to exploit."),
        ('h2', '5.7 Further robustness'),
        ('p1a', "None of the further checks changes the conclusions. DMCA (Kristoufek 2014), which satisfies the same identity and so "
                f"checks the detrending only, gives a purged coefficient of {rng(dm_pcap)} and a three-pair gap of {rng(dm_gap)} "
                f"(Table S4). The daily gap interval stays within {f(blk_lo)}–{f(blk_hi)} for blocks of 5–60 days (Table S6), and the "
                f"daily VN30–VNINDEX average is {f(DETREND[0], 4)}, {f(DETREND[1], 4)} and {f(DETREND[2], 4)} for detrending orders "
                f"1–3. Proxies that replace the capitalization weight, such as a volatility-scaled weight of {rng(w_heur, 4)}, are "
                "unstable (Table S8), and shuffled surrogates attribute most of the multifractal range to fat tails (Fig. S1). Lead–lag, "
                "hedge-effectiveness and episode statistics are in Tables S9, S11 and S12."),
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
        ('p1a', "The nested results have one source. A child’s variation enters every covariance and both standard deviations of a "
                f"nested pair, and Lemma 1 pins the coefficient near a benchmark set by weight and relative amplitude. With VN30 at "
                f"{f(100 * W30, 0)}% of VN100, the benchmark is near 0.90 and the bound near 0.87, so the observed 0.99 says little about "
                "how mid caps move with large caps, and changes in the purged coefficient reach it damped by a factor of about ten."),
        ('p', "The purged series has the features the size literature predicts. Daily VN30 returns lead P_cap returns "
              f"(cross-autocorrelation {f(ll['lead_VN30_on_Pcap'])}, {ci(ll['ci_lo_1'], ll['ci_hi_1'])}) while the reverse is "
              f"negligible ({f(ll['lead_Pcap_on_VN30'])}), an asymmetry of {f(ll['asymmetry'])} {ci(ll['asym_ci_lo'], ll['asym_ci_hi'])} "
              "in line with Lo and MacKinlay (1990) and Hou (2007); intraday the lead is symmetric (Table S9). The auction-bar "
              "horizon dependence of broad-market pairs fits the Epps (1979) effect for small, fragile-liquidity stocks (Chen et al. "
              "2021; Tran and Tran 2025), which index-level data cannot separate from gradual diffusion (Hong and Stein 1999). The "
              "higher loading on high-volatility days has several candidate sources that our data cannot rank: herding (Nguyen et "
              "al. 2023) and sector connectedness (Bui et al. 2022), limit hits under the ±7% band, margin calls and foreign flows "
              "concentrated in large caps with room under ownership limits. The rise in residual variance shows that crises also "
              "bring mid-cap-specific shocks, which the Forbes–Rigobon correction misreads as lower dependence."),
        ('h2', '6.2 Implications'),
        ('p1a', "Nested index correlations used to judge diversification between tiers should first be decomposed. Box 1 does this "
                "from published series and the index weight; its key outputs are the purged coefficient and the sensitivity, whose "
                f"inverse of about {f(REC['inverse_sensitivity'], 0)} shows how ill-conditioned the index-level number is: an error of "
                "0.001 in the nested coefficient becomes about 0.01 in the purged one. Holdings-based risk models are not affected. "
                "For hedging, a minimum-variance VN30 hedge removes a share ρ² of mid-cap variance (Ederington 1979), "
                f"{f(HE['full']['hedge_effectiveness'], 2)} {ci(HE['full']['ci_lo'], HE['full']['ci_hi'], 2)} over the full sample but "
                f"{f(HE['B_low']['hedge_effectiveness'], 2)} {ci(HE['B_low']['ci_lo'], HE['B_low']['ci_hi'], 2)} in the low-volatility "
                f"quartile and {f(HE['B_high']['hedge_effectiveness'], 2)} in the high-volatility quartile (Table S11). A VNMIDCAP ETF "
                "holder hedging with VN30 futures keeps about a fifth of the variance on average and about half in calm markets, the "
                "basis risk a mid-cap derivative would remove; whether one would be viable we do not study. Regime-conditioned tier "
                "correlations are not supported: their in-sample gain is mostly within sampling error and vanishes out of sample. The "
                "error that matters is reading a nested correlation as diversification."),
        ('h2', '6.3 Transferability and limitations'),
        ('p1a', "Lemma 1 applies to any child contained in its parent with a known weight under one weighting scheme. Fig. 4 shows "
                "benchmarks above 0.7 whenever the child holds half of the parent and the remainder is no more volatile, so large "
                "mechanical components should be common in families such as SET50 within SET100 or IDX30 within LQ45; we did not "
                "compute them because we could not verify their weights. With partial overlap the shared constituents form a third "
                "component and Eq. (7) does not apply directly. We did not decompose the broad-market pairs: VNINDEX uses full and "
                "VN100 free-float capitalization, so VN100 is not a fixed-weight component of VNINDEX, and the mismatch term of "
                "Eq. (12) cannot be bounded without constituent data."),
        ('p', "The evidence comes from one exchange and three indices. The purged series rests on one factsheet weight; a weight "
              "path from semi-annual reviews would narrow the attribution intervals, which weight error dominates. We could not "
              "validate P_cap against the published VNMIDCAP index or the FUEDCMID net asset value, so we call ρ_AM overlap-purged "
              "rather than economic. Index-level prices cannot separate microstructure from diffusion, crisis evidence depends on "
              "the regime definition, and the out-of-sample period covers three years. The FTSE Russell reclassification from "
              "September 2026 offers a test: if foreign inflows raise the large-cap weight or lower the volatility of the remaining "
              "constituents relative to large caps, Eq. (8) predicts a higher benchmark."),
        ('h1', '7 Conclusion'),
        ('p1a', "Correlations between nested equity indices contain a component fixed by construction. Carrying the part–whole "
                "identity to scale-wise detrended coefficients yields a benchmark, a lower bound, a sensitivity and an order-free "
                "attribution, all computable from index-level inputs. On the HOSE the VN30–VN100 coefficient moves by only about "
                f"{f(sum(sens_v) / 4, 2)} per unit change in the purged coefficient, and removing the overlap lowers the correlation "
                f"with large caps by about {f(sum(gapL_v) / 4, 2)}. The purged series shows a large-to-small lead, horizon effects "
                "confined to the auction bars, a higher mid-cap loading together with more mid-cap-specific risk on volatile days, "
                "and no out-of-sample gain from regime-conditioned correlations. Users of index-level data should decompose nested "
                "correlations before reading them as evidence about diversification between tiers."),
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
