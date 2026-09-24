# Round-1 revision text (executed inside stage3.py). RR numbers refer to notes/review_full/06_editorial_synthesis.md
g = {tf: BT[(tf, 'nested_mean-minus-Pcap', 'gap')] for tf in TF}
gap_lo = min(float(g[t]['ci_lo']) for t in TF); gap_hi = max(float(g[t]['ci_hi']) for t in TF)
frA, frB = FR[('A', 'Pcap-VN30')], FR[('B', 'Pcap-VN30')]
reAl, reAh = RE[('A', 'Pcap-VN30', 'low')], RE[('A', 'Pcap-VN30', 'high')]
reBl, reBh = RE[('B', 'Pcap-VN30', 'low')], RE[('B', 'Pcap-VN30', 'high')]
nested_re = [r for k, r in RE.items() if k[1] != 'Pcap-VN30']
max_nested = max(nested_re, key=lambda r: abs(float(r['RE_pct'])))
H = H2_pPr = None

# ---------------------------------------------------------------- abstract, keywords (RR6, RR7, RR1-RR4)
set_text(find('Abstract:'), f"Asset allocators in emerging Southeast Asian markets frequently treat large-cap and broad-market indices as separate diversification instruments, even in nested architectures where large-cap stocks dominate the broader market. Standard risk models thereby conflate mechanical constituent overlap with genuine economic co-movement. Utilizing Detrended Cross-Correlation Analysis (DCCA) and its multifractal extension on 30-minute, 1-hour, 4-hour and daily data from the Ho Chi Minh City Stock Exchange (2014–2025), this study illustrates that shared capitalization inflates the near-perfect correlations among nested indices (0.975–0.980). Purging constituent overlap with a capitalization-weighted mid-cap proxy lowers the correlation with large caps by 0.086–0.096, with block-bootstrap intervals that exclude zero at every frequency, although the purged correlation remains high (about 0.88). Correlations involving the broad market rise with the horizon at the 30-minute and 1-hour frequencies, whereas the purged mid-cap correlation shows no significant horizon dependence. Raw cross-tier correlation rises from {f(frB['rho_low'],2)} to {f(frB['rho_high'],2)} in high-volatility regimes, but after Forbes–Rigobon volatility conditioning there is no evidence of a structural increase, consistent with interdependence rather than contagion. Consequently, a static correlation overstates in-sample mid-cap portfolio variance by {f(reAl['RE_pct'],1)}–{f(reBl['RE_pct'],1)}% in calm regimes and understates it by about 2% in turbulent regimes. These findings support independent mid-cap benchmarks and volatility-regime-sensitive risk budgeting in Vietnam, and they motivate tests in other markets of the Association of Southeast Asian Nations (ASEAN) with nested index architectures.", bold_lead='Abstract: ')

# ---------------------------------------------------------------- introduction (RR6, RR8, RR14, RR15, RR16)
p = find('Portfolio managers and institutional asset allocators')
replace_in(p, 'In empirical practice, risk models, asset allocation algorithms, and regulatory stress-testing frameworks routinely parameterize', 'Many risk models, asset allocation algorithms and stress-testing frameworks parameterize')
p9 = find('In nested equity index systems').getnext()
set_text(p9, 'VN30 ⊂ VN100 ⊂ VNINDEX.')
pp = p9.find(W + 'pPr'); jc = pp.find(W + 'jc')
if jc is None: jc = etree.SubElement(pp, W + 'jc')
jc.set(W + 'val', 'center')
p = find('To separate multiscale dynamics')
replace_in(p, 'Building on Detrended Fluctuation Analysis (Kantelhardt et al. 2002)', 'Building on Detrended Fluctuation Analysis (Peng et al. 1994) and its multifractal generalization (Kantelhardt et al. 2002)')
replace_in(p, 'while Podobnik et al. (2011) established the analytical finite-sample distribution for hypothesis testing', 'while Podobnik et al. (2011) proposed statistical tests for power-law cross-correlated processes')
replace_in(p, 'remain an unaddressed empirical issue.', 'remain comparatively underexplored.')
p = find('Market regime shifts and microstructure frictions')
replace_in(p, 'In parallel, gradual information diffusion models (Hong and Stein 1999) suggest that market-wide news shocks are incorporated rapidly into liquid large caps before diffusing into less liquid mid-caps.', 'In parallel, gradual information diffusion (Hong and Stein 1999) implies that news is incorporated into prices with a delay, so co-movement between securities that are repriced at different speeds can rise with the horizon.')
replace_in(p, 'Recent empirical evidence from Vietnam confirms that retail dominance and liquidity constraints generate delayed price adjustments and nonlinear volatility spillovers (Le et al. 2025; Tran and Tran 2025).', 'Recent evidence from Vietnam points to delayed price adjustment under retail-heavy participation (Tran and Tran 2025) and to nonlinear dependence on regional markets (Le et al. 2025).')
set_text(find('Regional studies show'), "Regional studies show that financial integration across ASEAN equity markets is time-varying and shaped by trade linkages, market volatility and external shocks (Karim and Ning 2013; Lean and Teng 2013). Unlike markets that permit regulated short selling, Vietnam’s HOSE prohibits cash short selling, so we treat the role of trading restrictions in multiscale price synchronization as a hypothesis for comparative work rather than as a tested result.")
set_text(find('Firstly, we map'), f"Firstly, we quantify the overlap distortion in nested benchmark systems. Headline large-cap and broad-market indices exhibit near-perfect cross-correlations (0.975–0.980) at all frequencies, and extracting shared capitalization through a market-weighted mid-cap proxy lowers the correlation with large caps by 0.086–0.096, a gap whose bootstrap confidence intervals exclude zero at every frequency. Correlations involving the broad market rise with the horizon at the 30-minute and 1-hour frequencies, whereas the purged mid-cap correlation is statistically flat across horizons.")
set_text(find('Secondly, we provide'), f"Secondly, we provide a volatility-conditioned evaluation of crisis dynamics. Raw cross-tier correlations tighten by up to {f(float(frB['rho_high'])-float(frB['rho_low']),2)} correlation points in high-volatility regimes, which would conventionally be read as a correlation breakdown. Applying the Forbes and Rigobon (2002) adjustment under two regime definitions with block-bootstrap inference, we find no evidence that the adjusted crisis correlation exceeds its calm-period level. Mid-cap diversification failure during Vietnamese market stress is therefore consistent with interdependence amplified by volatility, although the test cannot exclude small structural increases.")
set_text(find('Thirdly, we quantify'), f"Thirdly, we quantify the risk-management cost of static correlations. Cash portfolios formed from parent and child indices suffer in-sample variance misstatements of at most {f(abs(float(max_nested['RE_pct'])),1)}%, whereas for a mid-cap factor exposure a static correlation overstates portfolio variance by {f(reAl['RE_pct'],1)}–{f(reBl['RE_pct'],1)}% in calm regimes and understates it by about 2% in turbulent regimes, when volatility itself has multiplied. Because short selling is prohibited, the non-investable mid-cap construct serves as a shadow benchmark for risk attribution, stress testing and index-product development.")
set_text(find('The remainder of the paper'), "The remainder of the paper is organized as follows. Section 1.1 describes the current situation and institutional background of the HOSE. Section 2 presents the data and methods, Section 3 reports the results and robustness checks, and Section 4 discusses the findings, their implications and limitations, and concludes.")
p = find('The primary microstructure constraint')
replace_in(p, 'This price collar truncates empirical return tails, is associated with artificial serial correlation, and coincides with mechanical spikes in cross-correlations as multiple index constituents are locked at the limit.', 'This price collar truncates return tails and can induce serial correlation and synchronized limit hits across index constituents.')
p = find('The second structural feature')
replace_in(p, 'Throughout most of our sample period, equities purchased on the HOSE could not be sold until the afternoon of the second business day.', 'Under the T+2 cycle in force for most of the sample, equities purchased on the HOSE could not be sold before the afternoon of the second business day.')

# ---------------------------------------------------------------- methods (RR2, RR9, RR11, RR12, RR15)
p = find('The dataset comprises closing prices')
replace_in(p, 'which covers all common stocks listed on the HOSE.', 'which covers all common stocks listed on the HOSE and is weighted by full market capitalization.')
p = find('The analysis evaluates four trading frequencies')
replace_in(p, 'and log returns were computed as:', 'and log returns were computed as below; no index price was filled or interpolated:')
p = find('The first definition uses continuous chronological')
replace_in(p, 'the 2018 margin contraction (January–December 2018;', 'the 2018 margin contraction (January–December 2018, including the run-up to the April peak;')
for pre in ('To verify whether the observed co-movement at timescale',):   # RR9: unused Podobnik test removed
    q = find(pre); nxt = q.getnext(); nxt2 = nxt.getnext(); remove(q); remove(nxt); remove(nxt2)
p = find('The Forbes–Rigobon identifying assumptions')
replace_in(p, 'We therefore restrict the formal test', 'Regime correlations are Pearson correlations of daily returns within each regime, and δ is the relative increase in the variance of VN30 returns, so that the correction and the correlation refer to the same measure. We restrict the formal test')
q = find('The formal hypothesis test is evaluated as follows')
set_text(q, "Inference uses a stationary block bootstrap (mean block length 20 trading days) applied separately within each regime; each of 1,999 replications recomputes the calm and crisis correlations and δ. We report a percentile 95% interval for the difference between the adjusted crisis correlation and the calm correlation, a one-sided bootstrap p-value for the null of no increase, and the power to detect an increase of 0.05.")
for _ in range(3): remove(q.getnext())                       # old asymptotic SE formula and test statistic
p = find('with the timescale evaluated on 30 logarithmically')
set_text(p, "with the timescale evaluated on 30 logarithmically spaced points between 5 bars and one quarter of the sample length (5 to 5,485 bars at M30), and separately on the reliable range of Section 3.3. Because the DCCA coefficients at different scales are functionals of the same two series, the regression residuals are not independent across scales. Inference therefore resamples the data rather than the scales: a stationary block bootstrap of the bivariate return series (499 replications, mean block length of about 20 trading days) recomputes the whole DCCA curve and its slope in each replicate, and we report percentile 95% intervals. The same bootstrap provides the intervals for the average correlations in Table 2.")
p = find('To capture multifractal heterogeneity')
replace_in(p, 'with the absolute-value operator (Oświęcimka et al. 2014)', 'using absolute local covariances to avoid complex-valued moments, an issue discussed by Oświęcimka et al. (2014)')
set_text(find('The multifractal spectrum width, the difference'), "The range of generalized exponents, Δh = h(−5) − h(5), measures how strongly the scaling differs between small and large fluctuations. Because fat tails alone widen this range, we compare each observed range with 100 surrogates in which the paired returns are jointly shuffled, which preserves the return distributions and their contemporaneous correlation but destroys temporal structure.")

# ---------------------------------------------------------------- results 3.2 (RR3)
tbl2 = [t for t in TBL() if 'Nested group' in ''.join(text_of(x) for x in t.iter(W + 'p'))][0]
rows = {'1D': 7, 'M30': 8, 'H1': 9, 'H4': 10}
for tf, r in rows.items():
    tc = cell(tbl2, r, 3); set_text(tc.findall(W + 'p')[0], f"{f(g[tf]['estimate'],3)} [{f(g[tf]['ci_lo'],3)}, {f(g[tf]['ci_hi'],3)}]")
set_text(find('Notes: Averages of ρ'), "Notes: Averages of ρ_{DCCA}(s) over s ≤ s_{rel} (Table 3), m = 1; nested group = mean of the three parent–child pairs. Brackets: block-bootstrap 95% intervals. Source: Authors’ calculations.")
set_text(find('Across both samples, the original nested group'), f"Across both samples, the original nested group maintains an average correlation of 0.975–0.980 at every frequency. In contrast, P_{{cap}}–VN30 produces a markedly lower correlation of 0.883–0.892, a gap of 0.086–0.096 correlation points whose bootstrap intervals ({f(gap_lo,3)} to {f(gap_hi,3)} across frequencies) exclude zero. The purged correlation nevertheless remains high, so the overlap inflates rather than creates the co-movement. Averages in the synchronized window (Panel A) and the full sample (Panel B) differ by at most 0.007 for every series.")

# ---------------------------------------------------------------- results 3.3 (RR10)
tbl3 = [t for t in TBL() if 'Maximum reliable scale' in ''.join(text_of(x) for x in t.iter(W + 'p'))][0]
add_col(tbl3); set_cell(tbl3, 0, 2, 'Gaussian s_{rel}'); set_cell(tbl3, 0, 3, 'Heavy-tailed s_{rel}')
for r, tf in zip(range(1, 5), TF): set_cell(tbl3, r, 3, RG[tf]['s_rel_garch_t'])
set_text(find('Notes: Worst-case mean absolute error'), "Notes: Largest scale at which the worst-case mean absolute error stays below 0.05; Gaussian: 1,002 white-noise simulations; heavy-tailed: 300 GARCH(1,1) simulations with Student-t (5) innovations. Source: Authors’ calculations.")
p = find('Because the number of segments shrinks')
replace_in(p, 'Table 3 reports the thresholds.', 'Because returns are heavy-tailed and volatility-clustered, we repeat the calibration with GARCH(1,1) surrogates driven by Student-t innovations with five degrees of freedom. Table 3 reports both thresholds.')
p = find('The estimates are insensitive to the detrending order')
nd = [float(RG[t]['nested_avg_conservative']) for t in TF]; pc = [float(RG[t]['pcap_avg_conservative']) for t in TF]
replace_in(p, 'The estimates are insensitive to the detrending order:', f"The heavy-tailed thresholds are markedly smaller, but averaging over them leaves the results intact (nested pairs {f(min(nd),3)}–{f(max(nd),3)}; P_{{cap}}–VN30 {f(min(pc),3)}–{f(max(pc),3)}). The estimates are also insensitive to the detrending order:")
assert p.find('.//' + M + 'oMath') is None
set_text(p, re.sub(r'\bP(?:_\{)?(cap|heur|ratio|res)\}?(?=[\s–,)])', r'P_{\1}', text_of(p)))

# ---------------------------------------------------------------- results 3.4 (RR11)
exc = [tf for tf in TF if SU[(tf, 'Pcap-VN30')]['exceeds_q95'] == 'TRUE']
nexc = sum(SU[(tf, pr)]['exceeds_q95'] == 'TRUE' for tf in TF for pr in ('VN30-VNINDEX', 'VN30-VN100', 'VN100-VNINDEX'))
set_text(find('The generalized Hurst exponent at the second order'), f"The generalized Hurst exponent at the second order, h(2), lies within 0.527–0.544 for all series and frequencies, indicating weak positive persistence. The range of generalized exponents is 0.252–0.431 for the nested pairs and 0.435–0.656 for P_{{cap}}–VN30, but shuffled surrogates show that much of this range reflects fat tails rather than temporal cross-correlation: the P_{{cap}}–VN30 range exceeds the 95th surrogate percentile only at {', '.join(exc) if exc else 'no frequency'} (observed {f(SU[('1D','Pcap-VN30')]['dh_obs'],3)} against a 95th percentile of {f(SU[('1D','Pcap-VN30')]['dh_shuffled_q95'],3)}), and the nested pairs exceed it in {nexc} of 12 cases. The multifractal evidence therefore supports only a modest, mainly daily, nonlinear cross-correlation structure in the purged series.")
replace_in(find('Notes: q ∈'), 'Notes: q ∈ [−5, 5]\\{0}.', 'Notes: q ∈ [−5, 5]\\{0}; daily data.')

# ---------------------------------------------------------------- results 3.5 Forbes-Rigobon (RR2)
tbl4 = [t for t in TBL() if 'Asymp. SE' in ''.join(text_of(x) for x in t.iter(W + 'p'))][0]
for c, v in enumerate(['Asset pair', 'ρ_{low}', 'ρ_{high}', 'δ', 'ρ^{*}', 'ρ^{*} − ρ_{low} [95% CI]', 'p-value', 'Power']): set_cell(tbl4, 0, c, v)
for r, d in ((2, frA), (4, frB)):
    for c, v in enumerate(['P_{cap}–VN30', f(d['rho_low'],3), f(d['rho_high'],3), f(d['delta'],2), f(d['rho_star'],3),
                           f"{f(d['diff'],3)} [{f(d['ci_lo'],3)}, {f(d['ci_hi'],3)}]", f(d['p_one_sided'],3), f(d['power_at_0.05'],2)]):
        set_cell(tbl4, r, c, v)
set_text(find('Notes: DCCA correlations at s'), "Notes: Pearson correlations of daily returns; δ = relative increase in VN30 return variance; one-sided bootstrap p-value for H_{0}: ρ^{*} ≤ ρ_{low}; power to detect an increase of 0.05. Panel A: 1,000 calm and 539 crisis days; Panel B: 739 days per regime. Source: Authors’ calculations.")
set_text(find('Table 4 presents the unadjusted'), "Table 4 presents the unadjusted and Forbes–Rigobon conditioned correlations to assess whether the surge in co-movement during market turmoil reflects a structural change or volatility expansion.")
nA = [FR[('A', p_)] for p_ in ('VN30-VNINDEX', 'VN30-VN100', 'VN100-VNINDEX')]; nB = [FR[('B', p_)] for p_ in ('VN30-VNINDEX', 'VN30-VN100', 'VN100-VNINDEX')]
rng = lambda L, k: f"{f(min(float(x[k]) for x in L),3)}–{f(max(float(x[k]) for x in L),3)}"
set_text(find('The formal test in Table 4'), f"The formal test in Table 4 is restricted to the disjoint pair P_{{cap}}–VN30, because nested pairs embed the conditioning asset in the dependent series and violate the exogeneity condition of Forbes and Rigobon (2002). For diagnostic comparison only, raw correlations for the nested pairs rise from {rng(nA,'rho_low')} in calm periods to {rng(nA,'rho_high')} in crisis episodes, and from {rng(nB,'rho_low')} to {rng(nB,'rho_high')} across rolling-volatility regimes.")
set_text(find('In Panel A, regimes correspond'), f"In Panel A, raw cross-tier correlation rises from {f(frA['rho_low'],3)} in calm years to {f(frA['rho_high'],3)} during the three crisis episodes, while the variance of VN30 returns increases by {f(float(frA['delta'])*100,0)}%. After conditioning, the adjusted crisis correlation is {f(frA['rho_star'],3)}, and the difference from the calm level ({f(frA['diff'],3)}; 95% interval {f(frA['ci_lo'],3)} to {f(frA['ci_hi'],3)}) provides no evidence of a structural increase (p = {f(frA['p_one_sided'],3)}). Because the interval also includes zero, the data do not support a structural decrease either. The power to detect an increase of 0.05 is {f(frA['power_at_0.05'],2)}, so moderate structural increases are unlikely, whereas small ones cannot be excluded.")
set_text(find('Panel B sorts days by the rolling'), f"Panel B sorts days by the rolling 20-day volatility of VNINDEX, producing a larger variance expansion (δ = {f(frB['delta'],2)}). The raw correlation rises from {f(frB['rho_low'],3)} to {f(frB['rho_high'],3)}, but the adjusted crisis correlation ({f(frB['rho_star'],3)}) again does not exceed the calm level (difference {f(frB['diff'],3)}, 95% interval {f(frB['ci_lo'],3)} to {f(frB['ci_hi'],3)}; p = {f(frB['p_one_sided'],3)}), although this test has low power ({f(frB['power_at_0.05'],2)}). Both definitions therefore point to interdependence amplified by volatility rather than contagion, a conclusion that rests on the absence of evidence for an increase rather than on proof of its absence. Because the regimes are sorted on VNINDEX, which contains the mid-caps, and are classified ex post, the comparison describes in-sample regimes rather than a real-time signal.")

# ---------------------------------------------------------------- results 3.6 portfolio (RR4)
set_text(find('When the two assets have equal volatility'), "All figures use regime-specific volatilities and Pearson correlations in the exact expression, so the static and regime-specific cases differ only in the correlation. Evaluating this relative variance error across regimes reveals a sharp distinction between tradable cash portfolios and underlying factor exposures.")
cash = RE[('B', 'VN30-VN100', 'low')], RE[('B', 'VN30-VN100', 'high')]
set_text(find('For cash portfolios formed from parent'), f"For cash portfolios formed from parent and child indices (such as VN30–VN100), co-movement is dominated by constituent overlap. The static daily correlation of {f(cash[0]['rho_static'],3)} compares with rolling-regime correlations of {f(cash[0]['rho_regime'],3)} and {f(cash[1]['rho_regime'],3)}, so the static model overstates portfolio variance by {f(cash[0]['RE_pct'],2)}% in the calm regime and understates it by {f(abs(float(cash[1]['RE_pct'])),2)}% in the turbulent regime. Across the three parent–child pairs and both regime definitions, the largest absolute error is {f(abs(float(max_nested['RE_pct'])),2)}%, which is negligible for operational risk management.")
set_text(find('Conversely, for the mid-cap factor exposure'), f"Conversely, for the mid-cap factor exposure, static correlation models produce material distortion. The static model overstates portfolio variance by {f(reAl['RE_pct'],2)}% (95% interval {f(reAl['ci_lo'],2)} to {f(reAl['ci_hi'],2)}) in the chronological calm regime and by {f(reBl['RE_pct'],2)}% ({f(reBl['ci_lo'],2)} to {f(reBl['ci_hi'],2)}) in the rolling low-volatility regime, whose quietest days exaggerate the effect. Because P_{{cap}} is a non-investable construct, these figures describe the risk of a mid-cap factor exposure (for example, one obtained through a mid-cap index fund) combined with large caps, not a portfolio that can be held directly.")
set_text(find('In the turbulent regime, the static model'), f"In the turbulent regime, the static model understates portfolio variance by {f(abs(float(reAh['RE_pct'])),2)}% (chronological) and {f(abs(float(reBh['RE_pct'])),2)}% (rolling). Although modest, these errors arise when the variance of the underlying assets has risen by {f(float(frA['delta'])*100,0)}% to {f(float(frB['delta'])*100,0)}% (Table 4). All regimes are identified ex post, so the figures measure the in-sample cost of ignoring regime dependence rather than the performance of a real-time risk-budgeting rule.")

# ---------------------------------------------------------------- results 3.7 scaling (RR1)
set_text(find('Table 5 presents the log-linear'), "Table 5 presents the scaling slopes of the DCCA coefficients at the M30 frequency over the full and reliable scale ranges, with block-bootstrap intervals, to quantify the sensitivity of cross-asset co-movement to the investment horizon.")
tbl5 = [t for t in TBL() if 'Intercept' in ''.join(text_of(x) for x in t.iter(W + 'p'))][0]
delete_col(tbl5, 6); delete_col(tbl5, 5)
for c, v in enumerate(['Pair', 'Full-range slope', '95% CI', 'Reliable-range slope', '95% CI']): set_cell(tbl5, 0, c, v)
P5 = [('VN30-VNINDEX', 'VN30–VNINDEX'), ('VN100-VNINDEX', 'VN100–VNINDEX'), ('VN30-VN100', 'VN30–VN100'), ('Pcap-VN30', 'P_{cap}–VN30'),
      ('Pheur-VN30', 'P_{heur}–VN30'), ('Pratio-VN30', 'P_{ratio}–VN30'), ('Pres-VN30', 'P_{res}–VN30')]
for r, (k, lab) in enumerate(P5, start=1):
    a, b = BT[('M30', k, 'slope_full')], BT[('M30', k, 'slope_rel')]
    for c, v in enumerate([lab, f(a['estimate'],4), cis(a), f(b['estimate'],4), cis(b)]): set_cell(tbl5, r, c, v)
set_text(find('Notes: 30 log-spaced scales'), "Notes: Slopes of ρ_{DCCA}(s) on ln s; full range: 30 scales from 5 to 5,485 bars; reliable range: s ≤ 444. Brackets: block-bootstrap 95% intervals (499 replications). Source: Authors’ calculations.")
vi, vr = BT[('M30', 'VN30-VNINDEX', 'slope_rel')], BT[('M30', 'VN100-VNINDEX', 'slope_rel')]
pr = BT[('M30', 'Pcap-VN30', 'slope_rel')]; pf = BT[('M30', 'Pcap-VN30', 'slope_full')]
set_text(find('The regression results reveal'), "The resampling results separate three patterns:")
set_text(find('First, for the fully nested pair'), f"First, for the fully nested pair VN30–VN100, the slope is essentially zero in both ranges: because VN30 constituents dominate VN100 capitalization, their mechanical co-movement is invariant to the timescale.")
set_text(find('Second, pairs that contain a genuine'), f"Second, the pairs involving the broad market rise significantly with the horizon within the reliable range: VN30–VNINDEX ({f(vi['estimate'],4)}, 95% interval {cis(vi)}) and VN100–VNINDEX ({f(vr['estimate'],4)}, {cis(vr)}). Over the reliable M30 range (5 to 444 bars) this corresponds to a rise of about {f(float(vi['estimate'])*4.49,3)} in the correlation. Over the full range, where long scales rest on few segments, the intervals include zero.")
set_text(find('Third, for the statistical residual proxies'), f"Third, the purged mid-cap correlation shows no significant horizon dependence: the P_{{cap}}–VN30 slope is {f(pf['estimate'],4)} {cis(pf)} over the full range and {f(pr['estimate'],4)} {cis(pr)} over the reliable range. The statistical residual proxies have larger but imprecise slopes, consistent with amplified noise.")
set_text(find('This positive scaling behavior'), "The horizon dependence of the broad-market pairs is consistent with two complementary mechanisms. Under the Epps (1979) effect, non-synchronous trading in less liquid constituents dampens correlations over the shortest intervals, roughly the first ten bars, and temporal aggregation removes this dampening. Beyond that range, gradual information diffusion (Hong and Stein 1999) can sustain a further rise if prices of different constituents adjust to common news at different speeds. That the purged mid-cap series shows no significant rise suggests that these effects are weaker than index-level sampling noise once the overlap is removed.")
set_text(find('A critical identification boundary'), "A critical identification boundary arises here: microstructure frictions and gradual information diffusion are observationally equivalent in index-level closing data. Disentangling them would require tick-by-tick order-book data and firm-level news timestamps, which lie beyond the scope of this study.")

# ---------------------------------------------------------------- results 3.8 robustness (RR1 other frequencies)
heading = find('3.8.1 Full-Range'); set_text(heading, '3.8.1 Scaling Slopes at the Other Frequencies', keep_tabs=True)
set_text(find('Table 6 compares the scaling slopes'), "Table 6 reports the same slopes at the daily, 1-hour and 4-hour frequencies for the broad-market pair VN30–VNINDEX and the purged pair P_{cap}–VN30.")
tbl6 = [t for t in TBL() if 'Stability' in ''.join(text_of(x) for x in t.iter(W + 'p'))][0]
delete_row(tbl6, 7)
for c, v in enumerate(['Frequency and pair', 'Full-range slope [95% CI]', 'Reliable-range slope [95% CI]', 'Assessment']): set_cell(tbl6, 0, c, v)
def assess(a, b):
    if sig(b) and float(b['estimate']) > 0: return 'Rises (reliable range)'
    if sig(b) or sig(a): return 'Mixed'
    return 'Flat'
r = 1
for tf, lab in (('1D', 'Daily'), ('H1', '1-hour'), ('H4', '4-hour')):
    for k, pl in (('VN30-VNINDEX', 'VN30–VNINDEX'), ('Pcap-VN30', 'P_{cap}–VN30')):
        a, b = BT[(tf, k, 'slope_full')], BT[(tf, k, 'slope_rel')]
        set_cell(tbl6, r, 0, f"{lab}: {pl}")
        for c, d in ((1, a), (2, b)):
            ps = cell(tbl6, r, c).findall(W + 'p'); set_text(ps[0], f(d['estimate'], 4))
            if len(ps) > 1: set_text(ps[1], cis(d))
        set_cell(tbl6, r, 3, assess(a, b)); r += 1
set_text(find('Notes: HAC standard errors'), "Notes: Block-bootstrap 95% intervals (499 replications); reliable ranges from Table 3 (Gaussian). Source: Authors’ calculations.")
h1 = BT[('H1', 'VN30-VNINDEX', 'slope_rel')]
set_text(find('The positive slopes of VN30–VNINDEX'), f"At the 1-hour frequency, VN30–VNINDEX again rises significantly within the reliable range ({f(h1['estimate'],4)}, {cis(h1)}), whereas at the daily and 4-hour frequencies no slope is distinguishable from zero. The P_{{cap}}–VN30 slope is insignificant at every frequency. The horizon dependence documented in this study is therefore confined to broad-market pairs at the two shortest intraday frequencies.")

# ---------------------------------------------------------------- results 3.8.2 weights (Table 7 consistent with RR2)
tbl7 = [t for t in TBL() if 'Calm ρ' in ''.join(text_of(x) for x in t.iter(W + 'p'))][0]
set_cell(tbl7, 0, 2, 'Slope β_{scale} (M30, full range)')
for r, d in enumerate(T7, start=1):
    set_cell(tbl7, r, 2, f(d['slope_M30'], 4)); set_cell(tbl7, r, 3, f(d['rho_low_pearson'], 3)); set_cell(tbl7, r, 4, f(d['rho_high_pearson'], 3))
set_text(find('Notes: ρ_{low} and ρ_{high} use') if False else find('Notes: ρlow and ρhigh use'), "Notes: ρ_{low} and ρ_{high} are Pearson correlations in the chronological regimes (Table 4, Panel A); slopes are point estimates (inference in Table 5). Source: Authors’ calculations.")
gl = min(float(d['gap_vs_nested']) for d in T7); th = [float(d['rho_high_pearson']) - float(d['rho_low_pearson']) for d in T7]
set_text(find('Table 7 shows that a higher'), f"Table 7 shows that a higher large-cap weight removes more of the VN30 component and therefore lowers the P_{{cap}}–VN30 correlation (from 0.924 at a weight of 0.60 to 0.824 at 0.75). The level of the purged correlation is thus conditional on the assumed weight, but the qualitative conclusions are not: in every specification the P_{{cap}} correlation remains at least {f(gl,3)} below the 0.977 average of the nested daily pairs, and the raw crisis tightening ({f(min(th),3)}–{f(max(th),3)}) remains modest relative to the accompanying volatility expansion.")

# ---------------------------------------------------------------- 4 Discussion (journal structure; RR6, RR7, RR15)
h4 = find('4 Discussion and Conclusion'); set_text(h4, '4 Discussion', keep_tabs=True)
imp = find('4.1 Implications'); h41 = copy.deepcopy(imp); h4.addnext(h41); set_text(h41, '4.1 Principal Findings', keep_tabs=True)
set_text(imp, '4.2 Implications for Capital Markets', keep_tabs=True)
lim = find('4.2 Limitations'); set_text(lim, '4.3 Limitations and Future Research', keep_tabs=True)
set_text(find('First, conventional index pairs that embed'), "First, index pairs that embed large-cap constituents within broader benchmarks exhibit cross-correlations inflated by index engineering. Purging shared constituent capitalization through a market-weighted proxy lowers the correlation by about 0.09, a robust gap, although the purged co-movement remains high. Horizon dependence is confined to broad-market pairs at the shortest intraday frequencies; the purged mid-cap correlation is statistically flat across horizons.")
set_text(find('Second, volatility conditioning shows'), "Second, once volatility is conditioned on, there is no evidence that cross-tier co-movement rises structurally during market turmoil. Systemic stress raises volatility across capitalization tiers, so diversification benefits shrink when they are most needed even though the underlying dependence appears stable; small structural increases cannot be excluded given the power of the test.")
set_text(find('Third, while cash portfolios composed'), f"Third, cash portfolios composed of nested parent–child indices experience negligible variance misstatement, whereas static correlations materially misstate the risk of mid-cap factor exposures: in-sample, they overstate variance by {f(reAl['RE_pct'],1)}–{f(reBl['RE_pct'],1)}% in calm regimes and understate it by about 2% during crises.")
set_text(find('These findings carry concrete implications'), "These findings carry implications for institutional investors, index providers and regulators in Vietnam; for other ASEAN markets with nested architectures, such as Malaysia, Thailand and Indonesia, they are hypotheses to be tested rather than established results.")
p = find('For institutional portfolio management')
replace_in(p, 'asset allocators operating in ASEAN markets (such as Malaysian institutional funds, regional pension managers, and private wealth allocators) must recognize', 'allocators investing in Vietnam should recognize')
p = find('Regarding index architecture and product innovation')
replace_in(p, 'listing dedicated mid-cap exchange-traded funds based on standalone benchmarks such as VNMIDCAP (VN70) provides', 'expanding exchange-traded funds that track standalone benchmarks such as VNMIDCAP (VN70) would provide')
p = find('Finally, for market development')
replace_in(p, 'would substantially enhance market completeness', 'could enhance market completeness')
set_text(find('Second, index-level closing prices cannot separate'), "Second, index-level closing prices cannot separate microstructure frictions (Epps 1979) from gradual information diffusion (Hong and Stein 1999); constituent-level tick data would allow these channels to be disentangled. Third, the Forbes and Rigobon (2002) adjustment assumes exogenous large-cap shocks, which forced deleveraging may weaken, and its power against small structural changes is limited; regime-switching or heteroskedasticity-based identification could provide complementary evidence. Fourth, regimes are classified ex post, so an out-of-sample evaluation of regime-conditioned risk budgets is needed before the portfolio results can guide practice. Finally, applying the framework to the nested index systems of Malaysia, Thailand and Indonesia would test the hypothesis that trading restrictions shape multiscale price synchronization.")
last_lim = find('Second, index-level closing prices cannot separate')
concl_h = copy.deepcopy(lim); spacer = copy.deepcopy(last_lim.getprevious())
last_lim.addnext(spacer); spacer.addnext(concl_h); set_text(concl_h, '4.4 Conclusion', keep_tabs=True)
concl = clone_after(concl_h, "Nested equity indices on the HOSE overstate the co-movement between large caps and the rest of the market because they share constituents. A capitalization-weighted decomposition removes about 0.09 of correlation, the remaining cross-tier dependence shows no structural increase in crises once volatility is accounted for, and static correlations misstate the risk of mid-cap exposures by amounts that depend on the volatility regime. Independent mid-cap benchmarks and volatility-regime-conditioned risk budgets are the natural responses.", template=last_lim)

# ---------------------------------------------------------------- declarations (RR13, RR16)
set_text(find('Code availability'), "The R code that reproduces every table and figure is provided as Online Resource 1 and will be deposited in a public repository upon acceptance.", bold_lead='Code availability ')
fund = clone_after(find('Code availability').getnext() if False else find('Code availability'), "Funding information is provided on the separate title page in accordance with the journal’s double-blind review policy.", template=find('Code availability'), bold_lead='Funding ')
fund.addprevious(copy.deepcopy(find('Code availability').getprevious()))

# ---------------------------------------------------------------- references: Newey–West no longer cited (RR1)
remove(find('Newey, W. K., & West, K. D. (1987)'))

# ---------------------------------------------------------------- equation numbers (RR16)
n = 0
for q in TOP():
    t = text_of(q).strip()
    has_math = q.find('.//' + M + 'oMath') is not None
    plain = ''.join((x.text or '') for x in q.iter(W + 't') if not any(a.tag == M + 'oMath' for a in x.iterancestors())).strip()
    if (has_math and plain == '') or t in ('VN30 ⊂ VN100 ⊂ VNINDEX.',) or t.startswith('Pheur,t = '):
        n += 1
        r = etree.SubElement(q, W + 'r'); tt = etree.SubElement(r, W + 't'); tt.text = f' ({n})'; tt.set(XMLSPACE, 'preserve')
print('equations numbered:', n)

# Table 6 caption now describes the other-frequency grid
set_text(find('Table 6 Full-range'), 'Scaling slopes of DCCA coefficients at the daily, 1-hour and 4-hour frequencies', bold_lead='Table 6 ')
