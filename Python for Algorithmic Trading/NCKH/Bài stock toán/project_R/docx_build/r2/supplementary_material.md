::: {custom-style="Title"}
Supplementary Material (Online Resource 2): How Much of a Nested Index Correlation Is Construction? A Scale-Wise Part–Whole Decomposition with Evidence from Vietnam
:::

::: {custom-style="heading1"}
Supplementary Material (Online Resource 2)
:::

::: {custom-style="p1a"}
This document accompanies the article and reports robustness checks referred to in the main text. All numbers come from the R outputs listed in the replication package (Online Resource 1).
:::

::: {custom-style="tablecaption"}
**Table S1** Full-range scaling slopes (30 log-spaced scales)
:::

| Frequency | Pair | Slope [95% CI] | p (bootstrap) |
|---|---|---|---|
| Daily (1D) | VN30–VNINDEX | 0.0020 [−0.0064, 0.0043] | 0.836 |
| Daily (1D) | VN100–VNINDEX | 0.0005 [−0.0052, 0.0026] | 0.928 |
| Daily (1D) | VN30–VN100 | 0.0001 [−0.0030, 0.0012] | 0.704 |
| Daily (1D) | P~cap~–VN30 | 0.0014 [−0.0255, 0.0118] | 0.908 |
| 30-minute (M30) | VN30–VNINDEX | 0.0016 [−0.0025, 0.0034] | 0.464 |
| 30-minute (M30) | VN100–VNINDEX | 0.0009 [−0.0010, 0.0021] | 0.312 |
| 30-minute (M30) | VN30–VN100 | 0.0001 [−0.0015, 0.0010] | 0.968 |
| 30-minute (M30) | P~cap~–VN30 | 0.0025 [−0.0102, 0.0093] | 0.820 |
| 1-hour (H1) | VN30–VNINDEX | 0.0015 [−0.0027, 0.0040] | 0.424 |
| 1-hour (H1) | VN100–VNINDEX | 0.0007 [−0.0021, 0.0025] | 0.604 |
| 1-hour (H1) | VN30–VN100 | −0.0001 [−0.0016, 0.0009] | 0.968 |
| 1-hour (H1) | P~cap~–VN30 | −0.0003 [−0.0137, 0.0089] | 0.928 |
| 4-hour (H4) | VN30–VNINDEX | 0.0014 [−0.0056, 0.0039] | 0.752 |
| 4-hour (H4) | VN100–VNINDEX | 0.0005 [−0.0043, 0.0025] | 0.900 |
| 4-hour (H4) | VN30–VN100 | −0.0000 [−0.0022, 0.0010] | 0.868 |
| 4-hour (H4) | P~cap~–VN30 | 0.0001 [−0.0176, 0.0103] | 0.916 |

::: {custom-style="Compact"}
Notes: Slopes of Eq. (13) over 30 scales from 5 bars to one quarter of the sample. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S2** Decomposition of the VN30–VN100 coefficient on a grid of weights
:::

| w | Freq. | κ | ρ~AM~ | ρ̲ | Benchmark-first share | Sensitivity | Shapley overlap share | Pearson ρ̲ (1D) |
|---|---|---|---|---|---|---|---|---|
| 0.6000 | 1D | 0.675 | 0.924 | 0.829 | 0.839 | 0.164 | 0.452 | 0.833 |
| 0.6500 | 1D | 0.553 | 0.903 | 0.875 | 0.886 | 0.127 | 0.486 | 0.879 |
| 0.6826 (factsheet) | 1D | 0.484 | 0.884 | 0.900 | 0.911 | 0.106 | 0.508 | 0.903 |
| 0.7200 | 1D | 0.414 | 0.855 | 0.924 | 0.936 | 0.084 | 0.535 | 0.927 |
| 0.7500 | 1D | 0.363 | 0.824 | 0.940 | 0.952 | 0.069 | 0.559 | 0.943 |
| 0.6000 | M30 | 0.697 | 0.923 | 0.821 | 0.831 | 0.170 | 0.448 | 0.827 |
| 0.6500 | M30 | 0.573 | 0.901 | 0.868 | 0.879 | 0.133 | 0.483 | 0.873 |
| 0.6826 (factsheet) | M30 | 0.503 | 0.883 | 0.893 | 0.905 | 0.112 | 0.505 | 0.898 |
| 0.7200 | M30 | 0.431 | 0.855 | 0.918 | 0.930 | 0.090 | 0.532 | 0.922 |
| 0.7500 | M30 | 0.381 | 0.825 | 0.935 | 0.947 | 0.074 | 0.555 | 0.938 |

::: {custom-style="Compact"}
Notes: DCCA quantities averaged over s ≤ s~rel~ at each weight. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S3** Purged coefficient, gap and regime correlations on a grid of weights
:::

| w | Mean ρ~AM~ (1D) | Three-pair gap (1D) | Full-range slope (M30) | Calm ρ~low~ | Crisis ρ~high~ |
|---|---|---|---|---|---|
| 0.6000 | 0.924 | 0.052 | 0.0014 | 0.899 | 0.952 |
| 0.6500 | 0.903 | 0.074 | 0.0019 | 0.871 | 0.937 |
| 0.6826 (factsheet) | 0.884 | 0.093 | 0.0025 | 0.847 | 0.924 |
| 0.7200 | 0.855 | 0.122 | 0.0033 | 0.812 | 0.904 |
| 0.7500 | 0.824 | 0.153 | 0.0043 | 0.775 | 0.881 |

::: {custom-style="Compact"}
Notes: ρ~low~ and ρ~high~: Pearson correlations of P~cap~ and VN30 in the chronological regimes. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S4** Average DMCA coefficients over the reliable range
:::

| Frequency | VN30–VNINDEX | VN30–VN100 | VN100–VNINDEX | P~cap~–VN30 | Three-pair gap |
|---|---|---|---|---|---|
| Daily (1D) | 0.966 | 0.987 | 0.976 | 0.882 | 0.094 |
| 30-minute (M30) | 0.969 | 0.987 | 0.982 | 0.883 | 0.096 |
| 1-hour (H1) | 0.965 | 0.988 | 0.975 | 0.890 | 0.086 |
| 4-hour (H4) | 0.966 | 0.988 | 0.975 | 0.891 | 0.086 |

::: {custom-style="Compact"}
Notes: Centered moving-average detrending with odd windows matched to the DCCA scales s ≤ s~rel~. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S5** Lower-tail dependence of daily returns and the Gaussian-copula benchmark
:::

| Pair | u | Empirical λ~L~(u) [95% CI] | Pearson ρ | Gaussian-copula λ~L~(u) | Excess |
|---|---|---|---|---|---|
| VN30–VN100 | 0.05 | 0.904 [0.874, 0.958] | 0.988 | 0.876 | 0.029 |
| VN30–VN100 | 0.1 | 0.921 [0.901, 0.954] | 0.988 | 0.894 | 0.027 |
| VN30–VNINDEX | 0.05 | 0.850 [0.817, 0.931] | 0.967 | 0.789 | 0.061 |
| VN30–VNINDEX | 0.1 | 0.847 [0.813, 0.891] | 0.967 | 0.819 | 0.028 |
| VN100–VNINDEX | 0.05 | 0.864 [0.830, 0.945] | 0.976 | 0.820 | 0.044 |
| VN100–VNINDEX | 0.1 | 0.864 [0.834, 0.908] | 0.976 | 0.846 | 0.018 |
| P~cap~–VN30 | 0.05 | 0.749 [0.702, 0.830] | 0.889 | 0.617 | 0.132 |
| P~cap~–VN30 | 0.1 | 0.766 [0.717, 0.803] | 0.889 | 0.671 | 0.095 |

::: {custom-style="Compact"}
Notes: λ~L~(u) = P(X ≤ q~X~(u), Y ≤ q~Y~(u))/u; Gaussian-copula value at the pair’s own Pearson correlation. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S6** Sensitivity of the gap interval to the bootstrap block length
:::

| Frequency | Mean block length (days) | Three-pair gap | 95% CI |
|---|---|---|---|
| Daily | 5 | 0.093 | [0.079, 0.110] |
| Daily | 10 | 0.093 | [0.077, 0.111] |
| Daily | 20 | 0.093 | [0.074, 0.117] |
| Daily | 40 | 0.093 | [0.073, 0.119] |
| Daily | 60 | 0.093 | [0.070, 0.119] |
| 30-minute | 5 | 0.096 | [0.084, 0.112] |
| 30-minute | 40 | 0.096 | [0.076, 0.119] |

::: {custom-style="Compact"}
Notes: Bootstrap draws are separate from Table 4, so intervals differ by Monte Carlo error. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S7** Intraday results without the first bar of each day
:::

| Frequency | Bars kept | Bars dropped, % | Share of squared VN30 returns in first bar, % | Three-pair gap [95% CI] | Slope VN30–VNINDEX | Slope VN100–VNINDEX | Slope VN30–VN100 | Slope P~cap~–VN30 |
|---|---|---|---|---|---|---|---|---|
| 30-minute (M30) | 19,709 | 10.2 | 36.8 | 0.107 [0.094, 0.127] | 0.0020 | 0.0010 | 0.0001 | 0.0011 |
| 1-hour (H1) | 10,818 | 20.0 | 38.2 | 0.096 [0.082, 0.112] | 0.0003 | −0.0005 | −0.0004 | −0.0053 |

::: {custom-style="Compact"}
Notes: Reliable-range slopes of Eq. (13) after dropping the opening bar, which contains the overnight return and the opening auction. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S8** Statistical proxies for the mid-cap segment (M30)
:::

| Proxy | Reliable-range slope [95% CI] | p (bootstrap) |
|---|---|---|
| P~heur~–VN30 | 0.0289 [−0.0033, 0.0534] | 0.080 |
| P~ratio~–VN30 | 0.0291 [−0.0030, 0.0531] | 0.076 |
| P~res~–VN30 | 0.0283 [−0.0029, 0.0526] | 0.080 |

::: {custom-style="Compact"}
Notes: P~heur~ replaces w by the VN30–VN100 correlation (0.9865–0.9885); P~ratio~ = B − A; P~res~ is the residual of B on A. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S9** Lead–lag cross-autocorrelations between VN30 and P~cap~
:::

| Frequency | Pairs | corr(A~t−1~, M~t~) [95% CI] | corr(M~t−1~, A~t~) [95% CI] | Asymmetry [95% CI] |
|---|---|---|---|---|
| Daily (1D) | 2,962 | 0.084 [0.028, 0.136] | 0.007 [−0.036, 0.046] | 0.076 [0.048, 0.102] |
| 30-minute (M30) | 19,708 | 0.003 [−0.021, 0.027] | 0.007 [−0.030, 0.042] | −0.004 [−0.024, 0.017] |
| 1-hour (H1) | 10,817 | 0.054 [0.025, 0.085] | 0.064 [0.034, 0.093] | −0.010 [−0.028, 0.008] |

::: {custom-style="Compact"}
Notes: Lagged pairs are formed within the same trading day at intraday frequencies and resampled in blocks. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S10** Forbes–Rigobon test across weights and regime definitions
:::

| w | Regimes | ρ~low~ | ρ~high~ | ρ* | ρ* − ρ~low~ [95% CI] | p (one-sided) |
|---|---|---|---|---|---|---|
| 0.6000 | Chronological | 0.899 | 0.952 | 0.866 | −0.033 [−0.067, 0.002] | 0.968 |
| 0.6000 | VN30 quartiles | 0.833 | 0.956 | 0.743 | −0.090 [−0.137, −0.041] | 1.000 |
| 0.6500 | Chronological | 0.871 | 0.937 | 0.832 | −0.039 [−0.073, −0.002] | 0.988 |
| 0.6500 | VN30 quartiles | 0.785 | 0.943 | 0.695 | −0.091 [−0.144, −0.034] | 1.000 |
| 0.6826 | Chronological | 0.847 | 0.924 | 0.803 | −0.044 [−0.082, −0.005] | 0.990 |
| 0.6826 | VN30 quartiles | 0.744 | 0.932 | 0.657 | −0.087 [−0.144, −0.018] | 0.998 |
| 0.7200 | Chronological | 0.812 | 0.904 | 0.762 | −0.050 [−0.090, −0.000] | 0.989 |
| 0.7200 | VN30 quartiles | 0.683 | 0.913 | 0.606 | −0.077 [−0.143, 0.004] | 0.985 |
| 0.7500 | Chronological | 0.775 | 0.881 | 0.721 | −0.054 [−0.096, 0.002] | 0.988 |
| 0.7500 | VN30 quartiles | 0.621 | 0.893 | 0.560 | −0.061 [−0.135, 0.032] | 0.935 |

::: {custom-style="Compact"}
Notes: Daily Pearson correlations of P~cap~(w) and VN30. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S11** Effectiveness of a minimum-variance VN30 hedge of the mid-cap segment
:::

| Sample | N | ρ² [95% CI] |
|---|---|---|
| Full sample | 2,963 | 0.790 [0.754, 0.820] |
| Chronological calm | 1,000 | 0.718 [0.670, 0.761] |
| Chronological crisis | 539 | 0.854 [0.824, 0.885] |
| Low-volatility quartile | 739 | 0.528 [0.449, 0.608] |
| High-volatility quartile | 739 | 0.862 [0.834, 0.887] |

::: {custom-style="Compact"}
Notes: Share of P~cap~ variance removed by the minimum-variance hedge with VN30. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S12** Volatility episodes not classified as crises
:::

| Period | Trading days | Maximum drawdown, % | Days in top volatility quartile, % | Peak volatility, % p.a. | Date of peak |
|---|---|---|---|---|---|
| 2021-01-01 to 2021-12-31 | 250 | −14.3 | 32 | 49.1 | 2021-02-18 |
| 2025-03-01 to 2025-06-30 | 82 | −18.1 | 30 | 48.8 | 2025-05-06 |

::: {custom-style="Compact"}
Notes: Both episodes fail the drawdown and volatility-share criteria of Section 3.2 and are included in the quartile regimes. Source: Authors’ calculations.
:::

::: {custom-style="tablecaption"}
**Table S13** Slope channels of the VN30–VN100 coefficient (Eq. 14)
:::

| Frequency | Scales | Slope ρ~AM~ | Slope κ | ∂ρ~AB~/∂ρ~AM~ | ∂ρ~AB~/∂κ | Implied slope | Observed slope |
|---|---|---|---|---|---|---|---|
| Daily (1D) | 14 | −0.0040 | 0.0099 | 0.106 | −0.035 | −0.00077 | −0.00077 |
| 30-minute (M30) | 19 | 0.0017 | 0.0069 | 0.112 | −0.035 | −0.00006 | −0.00007 |
| 1-hour (H1) | 18 | 0.0020 | 0.0044 | 0.107 | −0.033 | 0.00007 | 0.00006 |
| 4-hour (H4) | 15 | −0.0020 | 0.0044 | 0.106 | −0.033 | −0.00036 | −0.00036 |

::: {custom-style="Compact"}
Notes: Partial derivatives averaged over s ≤ s~rel~. Source: Authors’ calculations.
:::

*Multifractal structure.* The generalized cross-correlation exponent h~xy~(2) lies between 0.526 and 0.542. The multifractal range Δh is 0.252–0.431 for the nested pairs and 0.435–0.656 for P~cap~–VN30. Against 100 jointly shuffled surrogates, the P~cap~–VN30 range exceeds the 95th surrogate percentile only at 1D, and the nested pairs in 2 of 12 cases. Because absolute local covariances can create spurious multifractality (Oświęcimka et al. 2014), these results are descriptive.

![](/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/docx_build/../outputs/figures/fig3_mfdcca.png){width=6.3in}

::: {custom-style="figurecaption"}
**Fig. S1** MF-DCCA at the daily frequency: (a) singularity spectra f(α); (b) generalized exponents h~xy~(q)
:::
::: {custom-style="Compact"}
Notes: q ∈ [−5, 5] \ {0}; f(α) can be negative where absolute local covariances are used. Source: Authors’ calculations.
:::
