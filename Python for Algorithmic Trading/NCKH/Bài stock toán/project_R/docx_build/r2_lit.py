"""Section 2.1-2.6 (analytical literature review), Table 1 and the reference list (v3, Stage 4 revision).
New items come from notes/review_r2/newrefs_verified.md and the round-2 review seats; every item passes the
independent Stage 4.5 citation audit before submission."""

LIT_INTRO = [
    ('p1a', "Five literatures bear on the question: part–whole correlation, detrended cross-correlation, index membership, "
            "size-based lead–lag effects and contagion. We review what each establishes and leaves open, then state the gap, "
            "estimands and hypotheses."),
]


def LIT_SECTIONS(table1):
    return [
        ('h2', '2.1 Part–whole correlation and holdings overlap'),
        ('p1a', "Pearson (1897) showed that ratios sharing a denominator correlate even when their numerators are independent. In "
                "psychometrics the same arithmetic inflates the correlation of an item with the total score that contains it, and "
                "Cureton (1966) gave a standard correction. Both results are static Pearson identities; neither measures the "
                "component at different timescales or attaches sampling uncertainty to it. Finance handles overlap through "
                "holdings: Active Share measures how far a fund departs from its benchmark holdings (Cremers and Petajisto 2009), "
                "holdings-based risk models estimate exposures from constituents, and membership studies build comparison "
                "portfolios from stocks outside the index (Barberis et al. 2005). What is missing is a return-based counterpart for "
                "users who observe only index levels."),
        ('h2', '2.2 Multiscale dependence and detrended cross-correlation'),
        ('p1a', "DCCA extends detrended fluctuation analysis (Peng et al. 1994; Kantelhardt et al. 2002) to pairs of nonstationary "
                "series (Podobnik and Stanley 2008); Zebende (2011) normalized it into a bounded coefficient, Podobnik et al. (2011) "
                "proposed tests and Zhou (2008) generalized it to multifractal moments (MF-DCCA). Variants use moving-average "
                "detrending (Jiang and Zhou 2011; Kristoufek 2014), sliding windows (Guedes et al. 2021) or partial correlations (Ge "
                "and Lin 2021), and Oświęcimka et al. (2014) show that absolute local covariances can create spurious "
                "multifractality. Applied work finds horizon-dependent stock–bond and cross-market dependence (Al Rababa’a et al. "
                "2021; Ge and Lin 2021; Chen et al. 2024), uses the coefficient to track contagion (Okorie and Lin 2021; Tilfani et "
                "al. 2021) or information flow (Zhou et al. 2025), and builds scale-aware portfolios (Wang et al. 2021; Kakinaka et "
                "al. 2025). All of it treats the coefficient as a measure of economic dependence between disjoint assets; none "
                "analyzes nested pairs, where the detrended covariance inherits the part–whole arithmetic at every scale."),
        ('h2', '2.3 Index membership and co-movement'),
        ('p1a', "Stocks added to the S&P 500 co-move more with the index (Barberis et al. 2005), Nikkei 225 stocks with larger "
                "weights co-move more with other index stocks (Greenwood 2008), and regression-discontinuity and tracking-demand "
                "designs support the effect (Liao et al. 2022; DeCoste 2025). The evidence is contested: much of the "
                "post-inclusion rise also appears in matched stocks that were not added (Chen et al. 2016), and the S&P 500 index "
                "effect has almost disappeared (Greenwood and Sammon 2025). Index-level co-movement is thus easy to misread even "
                "where indices do not overlap; our concern is the arithmetic overlap, which raises correlations even if no investor "
                "trades differently."),
        ('h2', '2.4 Size, lead–lag and horizon effects'),
        ('p1a', "Large-firm returns lead small-firm returns (Lo and MacKinlay 1990), a pattern Hou (2007) traces to slow diffusion "
                "of industry information. Non-synchronous trading depresses short-horizon correlations (Epps 1979), with a size "
                "that depends on sampling (Chang et al. 2021), and gradual diffusion (Hong and Stein 1999) lets co-movement build "
                "with the horizon. On the HOSE, small-firm liquidity fell after a market surveillance system was introduced (Chen et al. 2021) and price adjustment is "
                "delayed under retail-heavy trading (Tran and Tran 2025), while herding in stress (Nguyen et al. 2023), sector "
                "connectedness above 60%, near 90% during COVID-19 (Bui et al. 2022) and nonlinear regional dependence (Le et al. 2025) raise all "
                "correlations at once."),
        ('h2', '2.5 Volatility, contagion and interdependence'),
        ('p1a', "Equity correlations rise in downturns (Longin and Solnik 2001; Ang and Chen 2002), but they also rise mechanically "
                "with the variance of the conditioning market, so a crisis increase may reflect interdependence rather than "
                "contagion (Forbes and Rigobon 2002). The correction can itself be biased toward no contagion because it restricts "
                "the variance of idiosyncratic shocks; Corsetti et al. (2005) propose testing for a change in the factor loading "
                "instead, and Rigobon (2003) identifies transmission from regime changes in variance. Studies without the "
                "correction report COVID-19 contagion (Akhtaruzzaman et al. 2021; Guo et al. 2021; Benkraiem et al. 2022), a DCCA "
                "test finds it for some commodity pairs but not others (Santana et al. 2023), and ASEAN integration varies with "
                "trade links and volatility (Abdul Karim and Xin Ning 2013; Lean and Teng 2013). No study applies volatility-robust "
                "tests to tiers of one market whose indices overlap."),
        ('h2', '2.6 Research gap'),
        ('p1a', "Table 1 compares representative studies on the dimensions that matter here."),
        table1,
        ('p', "Three gaps follow. The part–whole identity is known for static Pearson correlations but has not been carried to "
              "scale-wise detrended coefficients, given inference under weight uncertainty, or turned into a diagnostic computable "
              "from published series. Multiscale studies of crises rarely use volatility-robust tests, and volatility-conditioned "
              "studies use one horizon and disjoint markets. To our knowledge, no study covers the Vietnamese index system at "
              "intraday and daily frequencies. We searched Google Scholar and publisher databases for 2021–2026, plus the classical "
              "sources these works cite, combining “detrended cross-correlation” with “index”, “overlap”, “nested” or "
              "“constituent”, together with “part–whole” and “item–total correlation”, “contagion” with “Forbes–Rigobon” or "
              "“heteroskedasticity”, and “Vietnam” with “co-movement” or “stock index”."),
    ]


TABLE1_ROWS = [
    ['Pearson (1897); Cureton (1966)', 'Ratios with a common component; test items', 'Pearson correlation', 'Yes (static)', 'No', 'No', 'Correlation of a whole with its part is inflated'],
    ['Cremers and Petajisto (2009)', 'US mutual funds', 'Holdings overlap (Active Share)', 'Yes (holdings)', 'No', 'No', 'Overlap with benchmark holdings measures activity'],
    ['Barberis et al. (2005); Greenwood (2008); Chen et al. (2016)', 'S&P 500; Nikkei 225', 'Event study; index weights', 'Membership, not overlap', 'No', 'No', 'Membership effect on co-movement is contested'],
    ['Podobnik and Stanley (2008); Zebende (2011)', 'Methodological', 'DCCA; ρDCCA', 'No', 'Yes', 'No', 'Scale-wise detrended covariance and coefficient'],
    ['Okorie and Lin (2021); Tilfani et al. (2021)', 'Stock markets, COVID-19', 'DCCA, DMCA; sliding windows', 'No', 'Yes', 'No', 'Fractal contagion that fades with the horizon'],
    ['Ge and Lin (2021); Chen et al. (2024)', 'China and United States', 'MF-DCCA; partial MF-DCCA', 'No', 'Yes', 'No', 'Scale- and size-dependent cross-correlation'],
    ['Wang et al. (2021); Kakinaka et al. (2025)', 'Stock portfolios', 'Mean-MF-X-DMA; mean-DCCA', 'No', 'Yes', 'No', 'Scale-aware rules improve portfolio performance'],
    ['Santana et al. (2023)', 'Crude oil and precious metals', 'ΔρDCCA test', 'No', 'Yes', 'No', 'Contagion depends on the pair'],
    ['Forbes and Rigobon (2002); Corsetti et al. (2005)', 'International stock markets', 'Adjusted correlation; factor model', 'No', 'No', 'Yes', 'Interdependence versus contagion; bias from restricted idiosyncratic variance'],
    ['Lo and MacKinlay (1990); Hou (2007)', 'US size portfolios', 'Cross-autocorrelation', 'No', 'No', 'No', 'Large caps lead small caps'],
    ['Bui et al. (2022); Tran and Tran (2025)', 'Vietnamese sectors; intraday HOSE', 'Spillover connectedness; high-frequency', 'No', 'No', 'No', 'High connectedness; delayed adjustment'],
    ['This study', 'VN30, VN100, VNINDEX; M30 to daily, 2014–2025', 'Scale-wise part–whole identity; DCCA', 'Yes (scale-wise, with weight uncertainty)', 'Yes', 'Yes', 'Purged correlation is invisible in the nested one'],
]
TABLE1_HEADER = ['Study', 'Market and data', 'Method', 'Overlap treated?', 'Scale-wise?', 'Volatility-robust test?', 'Main finding']
TABLE1_NOTE = ('Overlap treated: whether the study separates dependence created by shared constituents; scale-wise: whether '
               'dependence is measured by timescale; volatility-robust test: whether crisis comparisons correct for '
               'heteroskedasticity or common shocks. Source: Authors’ compilation.')

REFERENCES = [
    "Abdul Karim, B., & Xin Ning, H. (2013). Driving forces of the ASEAN-5 stock markets integration. Asia-Pacific Journal of Business Administration, 5(3), 186–191. https://doi.org/10.1108/APJBA-07-2012-0053",
    "Akhtaruzzaman, M., Boubaker, S., & Sensoy, A. (2021). Financial contagion during COVID–19 crisis. Finance Research Letters, 38, 101604. https://doi.org/10.1016/j.frl.2020.101604",
    "Al Rababa’a, A. R., Alomari, M., & McMillan, D. (2021). Multiscale stock-bond correlation: Implications for risk management. Research in International Business and Finance, 58, 101435. https://doi.org/10.1016/j.ribaf.2021.101435",
    "Andersen, T. G., & Bollerslev, T. (1997). Intraday periodicity and volatility persistence in financial markets. Journal of Empirical Finance, 4(2–3), 115–158. https://doi.org/10.1016/S0927-5398(97)00004-2",
    "Ang, A., & Chen, J. (2002). Asymmetric correlations of equity portfolios. Journal of Financial Economics, 63(3), 443–494. https://doi.org/10.1016/S0304-405X(02)00068-5",
    "Barberis, N., Shleifer, A., & Wurgler, J. (2005). Comovement. Journal of Financial Economics, 75(2), 283–317. https://doi.org/10.1016/j.jfineco.2004.04.003",
    "Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. Journal of the Royal Statistical Society: Series B (Methodological), 57(1), 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x",
    "Benkraiem, R., Garfatta, R., Lakhal, F., & Zorgati, I. (2022). Financial contagion intensity during the COVID-19 outbreak: A copula approach. International Review of Financial Analysis, 81, 102136. https://doi.org/10.1016/j.irfa.2022.102136",
    "Bui, H. Q., Tran, T., Pham, T. T., Nguyen, H. L.-P., & Vo, D. H. (2022). Market volatility and spillover across 24 sectors in Vietnam. Cogent Economics & Finance, 10(1), 2122188. https://doi.org/10.1080/23322039.2022.2122188",
    "Chang, P., Pienaar, E., & Gebbie, T. (2021). The Epps effect under alternative sampling schemes. Physica A: Statistical Mechanics and its Applications, 583, 126329. https://doi.org/10.1016/j.physa.2021.126329",
    "Chen, H., Singal, V., & Whitelaw, R. F. (2016). Comovement revisited. Journal of Financial Economics, 121(3), 624–644. https://doi.org/10.1016/j.jfineco.2016.05.007",
    "Chen, R., Geng, H., Lin, H., & Nguyen, P. T. L. (2021). Liquidity, informed trading, and a market surveillance system: Evidence from the Vietnamese stock market. Pacific-Basin Finance Journal, 67, 101567. https://doi.org/10.1016/j.pacfin.2021.101567",
    "Chen, Y., Zhang, J., Lu, L., & Xie, Z. (2024). Cross-correlation and multifractality analysis of the Chinese and American stock markets based on the MF-DCCA model. Heliyon, 10(17), e36537. https://doi.org/10.1016/j.heliyon.2024.e36537",
    "Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Lawrence Erlbaum Associates. https://doi.org/10.4324/9780203771587",
    "Corsetti, G., Pericoli, M., & Sbracia, M. (2005). ‘Some contagion, some interdependence’: More pitfalls in tests of financial contagion. Journal of International Money and Finance, 24(8), 1177–1199. https://doi.org/10.1016/j.jimonfin.2005.08.012",
    "Cremers, K. J. M., & Petajisto, A. (2009). How active is your fund manager? A new measure that predicts performance. The Review of Financial Studies, 22(9), 3329–3365. https://doi.org/10.1093/rfs/hhp057",
    "Cureton, E. E. (1966). Corrected item-test correlations. Psychometrika, 31(1), 93–96. https://doi.org/10.1007/BF02289461",
    "DeCoste, J. (2025). Comovement and S&P 500 membership. Global Finance Journal, 65, 101110. https://doi.org/10.1016/j.gfj.2025.101110",
    "Diebold, F. X., & Mariano, R. S. (1995). Comparing predictive accuracy. Journal of Business & Economic Statistics, 13(3), 253–263. https://doi.org/10.1080/07350015.1995.10524599",
    "Ederington, L. H. (1979). The hedging performance of the new futures markets. The Journal of Finance, 34(1), 157–170. https://doi.org/10.1111/j.1540-6261.1979.tb02077.x",
    "Epps, T. W. (1979). Comovements in stock prices in the very short run. Journal of the American Statistical Association, 74(366), 291–298. https://doi.org/10.1080/01621459.1979.10482508",
    "Forbes, K. J., & Rigobon, R. (2002). No contagion, only interdependence: Measuring stock market comovements. The Journal of Finance, 57(5), 2223–2261. https://doi.org/10.1111/0022-1082.00494",
    "FTSE Russell. (2025, October 7). FTSE Russell announces results of September 2025 semi-annual country classification review [Press release]. London Stock Exchange Group. https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2025/ftse-russell-country-classification-september-2025",
    "Ge, X., & Lin, A. (2021). Multiscale multifractal detrended partial cross-correlation analysis of Chinese and American stock markets. Chaos, Solitons & Fractals, 145, 110731. https://doi.org/10.1016/j.chaos.2021.110731",
    "Government of Vietnam. (2020). Decree No. 155/2020/ND-CP of 31 December 2020 detailing and guiding the implementation of a number of articles of the Law on Securities. Hanoi.",
    "Government of Vietnam. (2025). Decree No. 245/2025/ND-CP of 11 September 2025 amending and supplementing a number of articles of Decree No. 155/2020/ND-CP. Hanoi.",
    "Greenwood, R. (2008). Excess comovement of stock returns: Evidence from cross-sectional variation in Nikkei 225 weights. The Review of Financial Studies, 21(3), 1153–1186. https://doi.org/10.1093/rfs/hhm052",
    "Greenwood, R., & Sammon, M. (2025). The disappearing index effect. The Journal of Finance, 80(2), 657–698. https://doi.org/10.1111/jofi.13410",
    "Guedes, E. F., da Silva Filho, A. M., & Zebende, G. F. (2021). Detrended multiple cross-correlation coefficient with sliding windows approach. Physica A: Statistical Mechanics and its Applications, 574, 125990. https://doi.org/10.1016/j.physa.2021.125990",
    "Guo, Y., Li, P., & Li, A. (2021). Tail risk contagion between international financial markets during COVID-19 pandemic. International Review of Financial Analysis, 73, 101649. https://doi.org/10.1016/j.irfa.2020.101649",
    "Ho Chi Minh City Stock Exchange. (2022, September 29). Listing and official trading of DCVFMVNMIDCAP ETF fund certificates [Press release]. HOSE.",
    "Holm, S. (1979). A simple sequentially rejective multiple test procedure. Scandinavian Journal of Statistics, 6(2), 65–70. https://www.jstor.org/stable/4615733",
    "Hong, H., & Stein, J. C. (1999). A unified theory of underreaction, momentum trading, and overreaction in asset markets. The Journal of Finance, 54(6), 2143–2184. https://doi.org/10.1111/0022-1082.00184",
    "Hou, K. (2007). Industry information diffusion and the lead-lag effect in stock returns. The Review of Financial Studies, 20(4), 1113–1138. https://doi.org/10.1093/rfs/hhm003",
    "J.P. Morgan/Reuters. (1996). RiskMetrics: Technical document (4th ed.). Morgan Guaranty Trust Company.",
    "Jiang, Z.-Q., & Zhou, W.-X. (2011). Multifractal detrending moving-average cross-correlation analysis. Physical Review E, 84(1), 016106. https://doi.org/10.1103/PhysRevE.84.016106",
    "Kakinaka, S., Hayakawa, T., Kato, D., & Umeno, K. (2025). Fractal portfolio strategies: Does scale preference of investors matter? Applied Economics Letters, 32(3), 415–421. https://doi.org/10.1080/13504851.2023.2274298",
    "Kantelhardt, J. W., Zschiegner, S. A., Koscielny-Bunde, E., Havlin, S., Bunde, A., & Stanley, H. E. (2002). Multifractal detrended fluctuation analysis of nonstationary time series. Physica A: Statistical Mechanics and its Applications, 316(1–4), 87–114. https://doi.org/10.1016/S0378-4371(02)01383-3",
    "Kristoufek, L. (2014). Detrending moving-average cross-correlation coefficient: Measuring cross-correlations between non-stationary series. Physica A: Statistical Mechanics and its Applications, 406, 169–175. https://doi.org/10.1016/j.physa.2014.03.015",
    "Le, T. T. V., Dang, T. P. T., & Phan, T. H. N. (2025). The nonlinear dependence of the Vietnam stock market on the Asian stock market: Evidence from a quantile-on-quantile regression. International Journal of Innovative Research and Scientific Studies, 8(4), 535–553. https://doi.org/10.53894/ijirss.v8i4.7901",
    "Lean, H. H., & Teng, K. T. (2013). Integration of world leaders and emerging powers into the Malaysian stock market: A DCC-MGARCH approach. Economic Modelling, 32, 333–342. https://doi.org/10.1016/j.econmod.2013.02.013",
    "Liao, Y., Coakley, J., & Kellard, N. (2022). Index tracking and beta arbitrage effects in comovement. International Review of Financial Analysis, 83, 102330. https://doi.org/10.1016/j.irfa.2022.102330",
    "Lo, A. W., & MacKinlay, A. C. (1990). When are contrarian profits due to stock market overreaction? The Review of Financial Studies, 3(2), 175–205. https://doi.org/10.1093/rfs/3.2.175",
    "Longin, F., & Solnik, B. (2001). Extreme correlation of international equity markets. The Journal of Finance, 56(2), 649–676. https://doi.org/10.1111/0022-1082.00340",
    "Markowitz, H. (1952). Portfolio selection. The Journal of Finance, 7(1), 77–91. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x",
    "Ministry of Finance of Vietnam. (2020). Circular No. 120/2020/TT-BTC of 31 December 2020 on trading of listed and registered shares, fund certificates, corporate bonds and covered warrants listed on the securities trading system. Hanoi.",
    "Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica, 55(3), 703–708. https://doi.org/10.2307/1913610",
    "Nguyen, H. M., Bakry, W., & Vuong, T. H. G. (2023). COVID-19 pandemic and herd behavior: Evidence from a frontier market. Journal of Behavioral and Experimental Finance, 38, 100807. https://doi.org/10.1016/j.jbef.2023.100807",
    "Okorie, D. I., & Lin, B. (2021). Stock markets and the COVID-19 fractal contagion effects. Finance Research Letters, 38, 101640. https://doi.org/10.1016/j.frl.2020.101640",
    "Oświęcimka, P., Drożdż, S., Forczek, M., Jadach, S., & Kwapień, J. (2014). Detrended cross-correlation analysis consistently extended to multifractality. Physical Review E, 89(2), 022805. https://doi.org/10.1103/PhysRevE.89.022805",
    "Patton, A. J. (2011). Volatility forecast comparison using imperfect volatility proxies. Journal of Econometrics, 160(1), 246–256. https://doi.org/10.1016/j.jeconom.2010.03.034",
    "Pearson, K. (1897). Mathematical contributions to the theory of evolution.—On a form of spurious correlation which may arise when indices are used in the measurement of organs. Proceedings of the Royal Society of London, 60, 489–498. https://doi.org/10.1098/rspl.1896.0076",
    "Peng, C.-K., Buldyrev, S. V., Havlin, S., Simons, M., Stanley, H. E., & Goldberger, A. L. (1994). Mosaic organization of DNA nucleotides. Physical Review E, 49(2), 1685–1689. https://doi.org/10.1103/PhysRevE.49.1685",
    "Podobnik, B., Jiang, Z.-Q., Zhou, W.-X., & Stanley, H. E. (2011). Statistical tests for power-law cross-correlated processes. Physical Review E, 84(6), 066118. https://doi.org/10.1103/PhysRevE.84.066118",
    "Podobnik, B., & Stanley, H. E. (2008). Detrended cross-correlation analysis: A new method for analyzing two nonstationary time series. Physical Review Letters, 100(8), 084102. https://doi.org/10.1103/PhysRevLett.100.084102",
    "Politis, D. N., & Romano, J. P. (1994). The stationary bootstrap. Journal of the American Statistical Association, 89(428), 1303–1313. https://doi.org/10.1080/01621459.1994.10476870",
    "Rigobon, R. (2003). Identification through heteroskedasticity. The Review of Economics and Statistics, 85(4), 777–792. https://doi.org/10.1162/003465303772815727",
    "Santana, T. P., Horta, N., Revez, C., Dias, R. M. T. S., & Zebende, G. F. (2023). Effects of interdependence and contagion on crude oil and precious metals according to ρDCCA: A COVID-19 case study. Sustainability, 15(5), 3945. https://doi.org/10.3390/su15053945",
    "Schuirmann, D. J. (1987). A comparison of the two one-sided tests procedure and the power approach for assessing the equivalence of average bioavailability. Journal of Pharmacokinetics and Biopharmaceutics, 15(6), 657–680. https://doi.org/10.1007/BF01068419",
    "Shapley, L. S. (1953). A value for n-person games. In H. W. Kuhn & A. W. Tucker (Eds.), Contributions to the theory of games II (pp. 307–317). Princeton University Press. https://doi.org/10.1515/9781400881970-018",
    "Tilfani, O., Ferreira, P., & El Boukfaoui, M. Y. (2021). Dynamic cross-correlation and dynamic contagion of stock markets: A sliding windows approach with the DCCA correlation coefficient. Empirical Economics, 60(3), 1127–1156. https://doi.org/10.1007/s00181-019-01806-1",
    "Tran, M. H., & Tran, N. M. (2025). High-frequency dynamics of the Vietnam stock market. VNU Journal of Economics and Business, 5(2), 51–59. https://doi.org/10.57110/vnu-jeb.v5i2.395",
    "Vietnam Securities Depository. (2015). Decision No. 211/QĐ-VSD of 18 December 2015 promulgating the Regulation on clearing and settlement of securities transactions. Hanoi.",
    "Wang, F., Ye, X., Chen, H., & Wu, C. (2021). A portfolio strategy of stock market based on mean-MF-X-DMA model. Chaos, Solitons & Fractals, 143, 110645. https://doi.org/10.1016/j.chaos.2020.110645",
    "Zebende, G. F. (2011). DCCA cross-correlation coefficient: Quantifying level of cross-correlation. Physica A: Statistical Mechanics and its Applications, 390(4), 614–618. https://doi.org/10.1016/j.physa.2010.10.022",
    "Zhou, W., Huang, J., & Wang, M. (2025). Multifractal characteristics and information flow analysis of stock markets based on multifractal detrended cross-correlation analysis and transfer entropy. Fractal and Fractional, 9(1), 14. https://doi.org/10.3390/fractalfract9010014",
    "Zhou, W.-X. (2008). Multifractal detrended cross-correlation analysis for two nonstationary signals. Physical Review E, 77(6), 066211. https://doi.org/10.1103/PhysRevE.77.066211",
]
