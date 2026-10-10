"""Section 2.1-2.4 (analytical literature review), Table 1 and the reference list for the round-2 manuscript.
New 2021-2026 items come from notes/review_r2/newrefs_verified.md (independent search) and pass the independent
citation audit before submission."""

LIT_INTRO = [
    ('p1a', "Three literatures bear on our question: multiscale dependence measured by detrended cross-correlation, the effect "
            "of index construction and membership on co-movement, and the separation of contagion from volatility-driven "
            "interdependence. We review each analytically, identifying where findings agree, where they conflict and what they "
            "leave unresolved, and then state the gap and the hypotheses."),
]


def LIT_SECTIONS(table1):
    return [
        ('h2', '2.1 Multiscale dependence and detrended cross-correlation'),
        ('p1a', "Detrended cross-correlation analysis (DCCA) extends detrended fluctuation analysis (Peng et al. 1994; Kantelhardt "
                "et al. 2002) to pairs of nonstationary series (Podobnik and Stanley 2008). Zebende (2011) normalized the "
                "detrended covariance into a bounded coefficient, Podobnik et al. (2011) proposed tests for power-law "
                "cross-correlations, and Zhou (2008) generalized the method to multifractal moments (MF-DCCA). Later variants "
                "replace polynomial detrending by moving averages (Jiang and Zhou 2011; Kristoufek 2014), compute the coefficient in "
                "sliding windows (Guedes et al. 2021) or partial out third variables (Ge and Lin 2021). The methods disagree on one "
                "technical point that matters for finance: MF-DCCA must handle negative local covariances, and Oświęcimka et al. "
                "(2014) show that taking their absolute values, as many implementations do, can create spurious multifractality; "
                "they propose a sign-preserving alternative."),
        ('p', "Applied work agrees that financial dependence is scale-dependent. Stock–bond correlations differ across horizons "
              "(Al Rababa’a et al. 2021), cross-market correlations between China and the United States vary with scale and "
              "fluctuation size (Ge and Lin 2021; Chen et al. 2024), and combining MF-DCCA with transfer entropy reveals both "
              "multifractal cross-correlations and the direction of information flow among individual US stocks (Zhou et al. 2025). Two strands then use these coefficients for "
              "decisions. One measures crisis transmission: Okorie and Lin (2021) find fractal contagion in the stock markets of 32 "
              "economies during COVID-19 that diminishes over time, in the medium and long run, and Tilfani et al. (2021) track contagion with the "
              "DCCA coefficient in sliding windows. The other builds portfolios: a multifractal mean-MF-X-DMA rule outperforms "
              "the mean-variance model (Wang et al. 2021), and mean-DCCA portfolios perform better when the investor’s preferred "
              "scale adapts to market conditions (Kakinaka et al. 2025)."),
        ('p', "These strands share an assumption that is rarely stated. They treat the DCCA coefficient between two series as a "
              "measure of economic dependence, which is reasonable for disjoint assets such as stocks and bonds or two national "
              "markets. When one series contains the other, the coefficient also contains an arithmetic component that a "
              "portfolio optimizer or a contagion test would misread. None of the studies above analyzes nested pairs or "
              "separates such a component."),
        ('h2', '2.2 Index construction, constituent overlap and co-movement'),
        ('p1a', "A separate literature shows that index membership itself changes co-movement. Barberis et al. (2005) find that "
                "stocks added to the S&P 500 co-move more with the index afterwards, a result they attribute to trading frictions "
                "and investor habitats rather than to fundamentals. Recent work confirms the effect with sharper designs: DeCoste "
                "(2025) uses a regression discontinuity around the membership threshold and finds higher co-movement with no "
                "change in fundamentals, and Liao et al. (2022) attribute part of it to common demand from index trackers and beta "
                "arbitrageurs. The evidence is not uniform, however: Greenwood and Sammon (2025) document that the price effect of "
                "S&P 500 additions has almost disappeared, which suggests that membership effects depend on market structure and "
                "may weaken as indexing grows."),
        ('p', "This literature concerns behavioral co-movement among stocks. Our concern is the arithmetic overlap between indices: when VN30 is part of VN100, their correlation is "
              "high even if no investor behaves differently because of index membership. Multiscale studies that address "
              "redundant exposures do so with statistical tools, such as wavelet partial correlations for clusters of stocks "
              "(Michis 2022), or study volume–return rather than index–index dependence (Rodriguez and Alvarez-Ramirez 2021), so "
              "the arithmetic overlap has not been isolated."),
        ('p', "Vietnamese evidence suggests that both mechanisms could matter on the HOSE. Liquidity fell after the introduction of a "
              "market surveillance system, especially for small firms (Chen et al. 2021), herding appears on the "
              "HOSE during stress (Nguyen et al. 2023), sector connectedness exceeds 60% and rose to about 90% during COVID-19 "
              "(Bui et al. 2022), price adjustment is delayed under retail-heavy trading (Tran and Tran 2025), and dependence on "
              "regional markets is nonlinear (Le et al. 2025). High connectedness and herding raise all correlations, which makes "
              "it harder, not easier, to read index-level correlations as evidence about the tiers."),
        ('h2', '2.3 Volatility, contagion and interdependence'),
        ('p1a', "Equity correlations rise in downturns (Longin and Solnik 2001; Ang and Chen 2002), but Forbes and Rigobon (2002) "
                "show that unadjusted correlations rise mechanically with the variance of the conditioning market, so a crisis "
                "increase may reflect interdependence rather than contagion. The COVID-19 literature illustrates the resulting "
                "disagreement. Studies that do not apply the Forbes–Rigobon correction report contagion: conditional correlations between "
                "Chinese and G7 firms rose, especially for financial firms (Akhtaruzzaman et al. 2021), contagion channels "
                "multiplied in a network of 19 markets (Guo et al. 2021) and copula dependence intensified across Asian and "
                "American indices (Benkraiem et al. 2022). A DCCA-based test on commodities that compares coefficients before and "
                "during the crisis finds no contagion between two crude-oil benchmarks that were already highly interdependent, but "
                "contagion between crude oil and precious metals (Santana et al. 2023). Whether a crisis increase is structural "
                "thus depends on the pair and on how volatility is treated, and no study applies "
                "the correction to tiers of the same market whose indices overlap."),
        ('p', "Horizon effects add a further layer. Non-synchronous trading depresses correlations at short horizons (Epps 1979), "
              "and the size of this Epps effect depends on how prices are sampled (Chang et al. 2021). Gradual information "
              "diffusion (Hong and Stein 1999) can make co-movement build up with the horizon among stocks that adjust at "
              "different speeds. In ASEAN markets integration varies over time with trade links and volatility (Abdul Karim and Xin Ning "
              "2013; Lean and Teng 2013), so horizon and regime effects can interact."),
        ('h2', '2.4 Research gap'),
        ('p1a', "Table 1 compares representative studies on the dimensions relevant to our question."),
        table1,
        ('p', "Three gaps follow. First, no study we found separates the mechanical component of correlations between "
              "overlapping indices from economic co-movement, and none derives that component exactly. Second, multiscale "
              "studies of crisis transmission rarely apply volatility conditioning, while volatility-conditioned studies use a "
              "single horizon. Third, to our knowledge no DCCA study covers the Vietnamese index system at intraday and daily "
              "frequencies. Our search covered the outlets listed in Table 1 and indexed finance and econophysics journals for "
              "2021–2026; the closest prior work is Barberis et al. (2005) and DeCoste (2025) on membership-induced co-movement "
              "and Santana et al. (2023) on DCCA-based contagion tests."),
    ]


TABLE1_ROWS = [
    ['Podobnik and Stanley (2008); Zebende (2011)', 'Methodological', 'DCCA; ρDCCA', 'No', 'No', 'Defines scale-wise detrended covariance and its normalized coefficient'],
    ['Al Rababa’a et al. (2021)', 'Stock and bond markets', 'Multiscale correlation', 'No (disjoint assets)', 'No', 'Stock–bond correlation differs across horizons'],
    ['Okorie and Lin (2021)', '32 stock markets, COVID-19', 'DCCA, DMCA', 'No', 'No', 'Fractal contagion that diminishes over time'],
    ['Tilfani et al. (2021)', 'Stock market indices', 'Sliding-window ρDCCA', 'No', 'No', 'Time-varying cross-correlation and contagion'],
    ['Ge and Lin (2021); Chen et al. (2024)', 'China and United States', 'MF-DCCA; partial MF-DCCA', 'No', 'No', 'Scale- and size-dependent cross-correlation'],
    ['Wang et al. (2021); Kakinaka et al. (2025)', 'Stock portfolios', 'Mean-MF-X-DMA / mean-DCCA portfolios', 'No', 'No', 'Scale-aware rules improve portfolio performance'],
    ['Santana et al. (2023)', 'Crude oil and precious metals, COVID-19', 'ΔρDCCA test', 'No', 'No', 'No contagion between WTI and Brent; contagion between oil and precious metals'],
    ['Forbes and Rigobon (2002)', 'International stock markets', 'Heteroskedasticity-adjusted correlation', 'No', 'Yes', 'Crisis increases reflect interdependence'],
    ['Akhtaruzzaman et al. (2021)', 'China and G7 firms, COVID-19', 'Dynamic conditional correlation', 'No', 'No Forbes–Rigobon correction', 'Contagion concentrated in financial firms'],
    ['Barberis et al. (2005); DeCoste (2025)', 'S&P 500 additions and membership', 'Event study; regression discontinuity', 'Membership, not overlap', 'No', 'Index membership raises co-movement'],
    ['Bui et al. (2022)', '24 Vietnamese sectors, 2012–2021', 'Spillover connectedness', 'No', 'No', 'Connectedness 60–90%, highest in COVID-19'],
    ['This study', 'VN30, VN100, VNINDEX; M30 to daily, 2014–2025', 'DCCA, MF-DCCA, exact decomposition', 'Yes (exact, scale-wise)', 'Yes', 'Mechanical floor dominates nested correlations'],
]
TABLE1_NOTE = ('Overlap treated: whether the study separates the dependence created by shared constituents; volatility conditioning: '
               'whether crisis comparisons correct for heteroskedasticity bias. Source: Authors’ compilation.')

REFERENCES = [
    "Abdul Karim, B., & Xin Ning, H. (2013). Driving forces of the ASEAN-5 stock markets integration. Asia-Pacific Journal of Business Administration, 5(3), 186–191. https://doi.org/10.1108/APJBA-07-2012-0053",
    "Akhtaruzzaman, M., Boubaker, S., & Sensoy, A. (2021). Financial contagion during COVID–19 crisis. Finance Research Letters, 38, 101604. https://doi.org/10.1016/j.frl.2020.101604",
    "Al Rababa’a, A. R., Alomari, M., & McMillan, D. (2021). Multiscale stock-bond correlation: Implications for risk management. Research in International Business and Finance, 58, 101435. https://doi.org/10.1016/j.ribaf.2021.101435",
    "Ang, A., & Chen, J. (2002). Asymmetric correlations of equity portfolios. Journal of Financial Economics, 63(3), 443–494. https://doi.org/10.1016/S0304-405X(02)00068-5",
    "Barberis, N., Shleifer, A., & Wurgler, J. (2005). Comovement. Journal of Financial Economics, 75(2), 283–317. https://doi.org/10.1016/j.jfineco.2004.04.003",
    "Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. Journal of the Royal Statistical Society: Series B (Methodological), 57(1), 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x",
    "Benkraiem, R., Garfatta, R., Lakhal, F., & Zorgati, I. (2022). Financial contagion intensity during the COVID-19 outbreak: A copula approach. International Review of Financial Analysis, 81, 102136. https://doi.org/10.1016/j.irfa.2022.102136",
    "Bui, H. Q., Tran, T., Pham, T. T., Nguyen, H. L.-P., & Vo, D. H. (2022). Market volatility and spillover across 24 sectors in Vietnam. Cogent Economics & Finance, 10(1), 2122188. https://doi.org/10.1080/23322039.2022.2122188",
    "Chang, P., Pienaar, E., & Gebbie, T. (2021). The Epps effect under alternative sampling schemes. Physica A: Statistical Mechanics and its Applications, 583, 126329. https://doi.org/10.1016/j.physa.2021.126329",
    "Chen, R., Geng, H., Lin, H., & Nguyen, P. T. L. (2021). Liquidity, informed trading, and a market surveillance system: Evidence from the Vietnamese stock market. Pacific-Basin Finance Journal, 67, 101567. https://doi.org/10.1016/j.pacfin.2021.101567",
    "Chen, Y., Zhang, J., Lu, L., & Xie, Z. (2024). Cross-correlation and multifractality analysis of the Chinese and American stock markets based on the MF-DCCA model. Heliyon, 10(17), e36537. https://doi.org/10.1016/j.heliyon.2024.e36537",
    "Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Lawrence Erlbaum Associates. https://doi.org/10.4324/9780203771587",
    "DeCoste, J. (2025). Comovement and S&P 500 membership. Global Finance Journal, 65, 101110. https://doi.org/10.1016/j.gfj.2025.101110",
    "Epps, T. W. (1979). Comovements in stock prices in the very short run. Journal of the American Statistical Association, 74(366), 291–298. https://doi.org/10.1080/01621459.1979.10482508",
    "Forbes, K. J., & Rigobon, R. (2002). No contagion, only interdependence: Measuring stock market comovements. The Journal of Finance, 57(5), 2223–2261. https://doi.org/10.1111/0022-1082.00494",
    "Ge, X., & Lin, A. (2021). Multiscale multifractal detrended partial cross-correlation analysis of Chinese and American stock markets. Chaos, Solitons & Fractals, 145, 110731. https://doi.org/10.1016/j.chaos.2021.110731",
    "Greenwood, R., & Sammon, M. (2025). The disappearing index effect. The Journal of Finance, 80(2), 657–698. https://doi.org/10.1111/jofi.13410",
    "Guedes, E. F., da Silva Filho, A. M., & Zebende, G. F. (2021). Detrended multiple cross-correlation coefficient with sliding windows approach. Physica A: Statistical Mechanics and its Applications, 574, 125990. https://doi.org/10.1016/j.physa.2021.125990",
    "Guo, Y., Li, P., & Li, A. (2021). Tail risk contagion between international financial markets during COVID-19 pandemic. International Review of Financial Analysis, 73, 101649. https://doi.org/10.1016/j.irfa.2020.101649",
    "Holm, S. (1979). A simple sequentially rejective multiple test procedure. Scandinavian Journal of Statistics, 6(2), 65–70. https://www.jstor.org/stable/4615733",
    "Hong, H., & Stein, J. C. (1999). A unified theory of underreaction, momentum trading, and overreaction in asset markets. The Journal of Finance, 54(6), 2143–2184. https://doi.org/10.1111/0022-1082.00184",
    "Jiang, Z.-Q., & Zhou, W.-X. (2011). Multifractal detrending moving-average cross-correlation analysis. Physical Review E, 84(1), 016106. https://doi.org/10.1103/PhysRevE.84.016106",
    "Kakinaka, S., Hayakawa, T., Kato, D., & Umeno, K. (2025). Fractal portfolio strategies: Does scale preference of investors matter? Applied Economics Letters, 32(3), 415–421. https://doi.org/10.1080/13504851.2023.2274298",
    "Kantelhardt, J. W., Zschiegner, S. A., Koscielny-Bunde, E., Havlin, S., Bunde, A., & Stanley, H. E. (2002). Multifractal detrended fluctuation analysis of nonstationary time series. Physica A: Statistical Mechanics and its Applications, 316(1–4), 87–114. https://doi.org/10.1016/S0378-4371(02)01383-3",
    "Kristoufek, L. (2014). Detrending moving-average cross-correlation coefficient: Measuring cross-correlations between non-stationary series. Physica A: Statistical Mechanics and its Applications, 406, 169–175. https://doi.org/10.1016/j.physa.2014.03.015",
    "Le, T. T. V., Dang, T. P. T., & Phan, T. H. N. (2025). The nonlinear dependence of the Vietnam stock market on the Asian stock market: Evidence from a quantile-on-quantile regression. International Journal of Innovative Research and Scientific Studies, 8(4), 535–553. https://doi.org/10.53894/ijirss.v8i4.7901",
    "Lean, H. H., & Teng, K. T. (2013). Integration of world leaders and emerging powers into the Malaysian stock market: A DCC-MGARCH approach. Economic Modelling, 32, 333–342. https://doi.org/10.1016/j.econmod.2013.02.013",
    "Liao, Y., Coakley, J., & Kellard, N. (2022). Index tracking and beta arbitrage effects in comovement. International Review of Financial Analysis, 83, 102330. https://doi.org/10.1016/j.irfa.2022.102330",
    "Longin, F., & Solnik, B. (2001). Extreme correlation of international equity markets. The Journal of Finance, 56(2), 649–676. https://doi.org/10.1111/0022-1082.00340",
    "Markowitz, H. (1952). Portfolio selection. The Journal of Finance, 7(1), 77–91. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x",
    "Michis, A. A. (2022). Multiscale partial correlation clustering of stock market returns. Journal of Risk and Financial Management, 15(1), 24. https://doi.org/10.3390/jrfm15010024",
    "Nguyen, H. M., Bakry, W., & Vuong, T. H. G. (2023). COVID-19 pandemic and herd behavior: Evidence from a frontier market. Journal of Behavioral and Experimental Finance, 38, 100807. https://doi.org/10.1016/j.jbef.2023.100807",
    "Okorie, D. I., & Lin, B. (2021). Stock markets and the COVID-19 fractal contagion effects. Finance Research Letters, 38, 101640. https://doi.org/10.1016/j.frl.2020.101640",
    "Oświęcimka, P., Drożdż, S., Forczek, M., Jadach, S., & Kwapień, J. (2014). Detrended cross-correlation analysis consistently extended to multifractality. Physical Review E, 89(2), 022805. https://doi.org/10.1103/PhysRevE.89.022805",
    "Peng, C.-K., Buldyrev, S. V., Havlin, S., Simons, M., Stanley, H. E., & Goldberger, A. L. (1994). Mosaic organization of DNA nucleotides. Physical Review E, 49(2), 1685–1689. https://doi.org/10.1103/PhysRevE.49.1685",
    "Podobnik, B., Jiang, Z.-Q., Zhou, W.-X., & Stanley, H. E. (2011). Statistical tests for power-law cross-correlated processes. Physical Review E, 84(6), 066118. https://doi.org/10.1103/PhysRevE.84.066118",
    "Podobnik, B., & Stanley, H. E. (2008). Detrended cross-correlation analysis: A new method for analyzing two nonstationary time series. Physical Review Letters, 100(8), 084102. https://doi.org/10.1103/PhysRevLett.100.084102",
    "Politis, D. N., & Romano, J. P. (1994). The stationary bootstrap. Journal of the American Statistical Association, 89(428), 1303–1313. https://doi.org/10.1080/01621459.1994.10476870",
    "Rodriguez, E., & Alvarez-Ramirez, J. (2021). Time-varying cross-correlation between trading volume and returns in US stock markets. Physica A: Statistical Mechanics and its Applications, 581, 126211. https://doi.org/10.1016/j.physa.2021.126211",
    "Santana, T. P., Horta, N., Revez, C., Dias, R. M. T. S., & Zebende, G. F. (2023). Effects of interdependence and contagion on crude oil and precious metals according to ρDCCA: A COVID-19 case study. Sustainability, 15(5), 3945. https://doi.org/10.3390/su15053945",
    "Tilfani, O., Ferreira, P., & El Boukfaoui, M. Y. (2021). Dynamic cross-correlation and dynamic contagion of stock markets: A sliding windows approach with the DCCA correlation coefficient. Empirical Economics, 60(3), 1127–1156. https://doi.org/10.1007/s00181-019-01806-1",
    "Tran, M. H., & Tran, N. M. (2025). High-frequency dynamics of the Vietnam stock market. VNU Journal of Economics and Business, 5(2), 51–59. https://doi.org/10.57110/vnu-jeb.v5i2.395",
    "Wang, F., Ye, X., Chen, H., & Wu, C. (2021). A portfolio strategy of stock market based on mean-MF-X-DMA model. Chaos, Solitons & Fractals, 143, 110645. https://doi.org/10.1016/j.chaos.2020.110645",
    "Zebende, G. F. (2011). DCCA cross-correlation coefficient: Quantifying level of cross-correlation. Physica A: Statistical Mechanics and its Applications, 390(4), 614–618. https://doi.org/10.1016/j.physa.2010.10.022",
    "Zhou, W., Huang, J., & Wang, M. (2025). Multifractal characteristics and information flow analysis of stock markets based on multifractal detrended cross-correlation analysis and transfer entropy. Fractal and Fractional, 9(1), 14. https://doi.org/10.3390/fractalfract9010014",
    "Zhou, W.-X. (2008). Multifractal detrended cross-correlation analysis for two nonstationary signals. Physical Review E, 77(6), 066211. https://doi.org/10.1103/PhysRevE.77.066211",
]
