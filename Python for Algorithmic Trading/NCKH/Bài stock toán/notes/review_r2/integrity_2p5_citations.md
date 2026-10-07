# Citation integrity audit, Stage 2.5 (independent auditor)

- Manuscript audited: `project_R/docx_build/r2/manuscript_with_authors.md` (body lines 1–769; reference list lines 770–end, 45 `referenceitem` entries)
- Skill: ARS `academic-paper`, citation-check mode (citation_compliance_agent rules; IRON RULE: a reference passes only when found by WebSearch with matching metadata)
- Date: 2026-10-07
- Auditor context: no prior context; `notes/` and AUDIT_LEDGER were not read.
- **Tooling limitation (disclosed):** the egress proxy blocked every WebFetch and API host (doi.org, api.crossref.org, api.openalex.org, Semantic Scholar, IDEAS, ScienceDirect, MDPI, PMC, arXiv, journal sites). Verification therefore relies on **WebSearch result snippets only** (publisher/IDEAS/PubMed/repository snippets). DOI strings could not be resolved. Where a snippet showed the DOI, or the IDEAS/publisher handle fixed the volume, issue and article number, the DOI is marked confirmed. Otherwise the DOI is recorded as "consistent, not resolved".

## 1. Summary

| Check | Result |
|---|---|
| References in list | 45 |
| In-text citations without a reference (orphans in text) | 0 |
| References never cited in text | 0 |
| Year or spelling mismatches between text and list | 0 |
| References confirmed to exist | 45 / 45 (no fabricated reference found) |
| References needing metadata correction | 3 (Le et al. 2025 pages; Chen, Zhang, Lu & Xie 2024 issue; Karim & Ning 2013 author names) |
| Claim–source alignment issues | 0 CRITICAL, 4 MAJOR, 7 MINOR |
| Format issues | 1 MAJOR (Table 1 column headers), 4 MINOR |

## 2. Per-reference verification table

Status key: VERIFIED = authors, year, title, venue, volume/issue/pages and DOI match the search evidence. VERIFIED* = existence and core metadata confirmed, but one field (usually the DOI string or the article number) appeared in no snippet and could not be resolved, though it is consistent with the publisher's pattern. CORRECTED = a field is wrong (correction given).

| # | Reference (as in manuscript) | Status | Correction / note | Source URL |
|---|---|---|---|---|
| 1 | Akhtaruzzaman, Boubaker & Sensoy (2021) FRL 38, 101604 | VERIFIED* | Title, authors, vol., article no. confirmed; DOI 10.1016/j.frl.2020.101604 consistent, not resolved. "COVID–19" with en dash matches the published title. | https://ideas.repec.org/a/eee/finlet/v38y2021ics1544612320305754.html ; https://acuresearchbank.acu.edu.au/item/8wqyy/financial-contagion-during-covid-19-crisis |
| 2 | Al Rababa'a, Alomari & McMillan (2021) RIBAF 58, 101435 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://ideas.repec.org/a/eee/riibaf/v58y2021ics0275531921000568.html ; https://www.storre.stir.ac.uk/handle/1893/32588 |
| 3 | Ang & Chen (2002) JFE 63(3), 443–494 | VERIFIED | IDEAS handle v63y2002i3p443-494 confirms issue 3. One secondary snippet says 63(2); that snippet is wrong. | https://ideas.repec.org/a/eee/jfinec/v63y2002i3p443-494.html |
| 4 | Barberis, Shleifer & Wurgler (2005) JFE 75(2), 283–317 | VERIFIED* | Confirmed; DOI 10.1016/j.jfineco.2004.04.003 consistent, not resolved | https://shleifer.scholars.harvard.edu/publications/comovement |
| 5 | Benjamini & Hochberg (1995) JRSS B 57(1), 289–300 | VERIFIED | DOI 10.1111/j.2517-6161.1995.tb02031.x confirmed | https://citedrive.com/en/discovery/controlling-the-false-discovery-rate-a-practical-and-powerful-approach-to-multiple-testing |
| 6 | Benkraiem, Garfatta, Lakhal & Zorgati (2022) IRFA 81, 102136 | VERIFIED | DOI 10.1016/j.irfa.2022.102136 confirmed | https://ideas.repec.org/a/eee/finana/v81y2022ics105752192200103x.html |
| 7 | Bui, Tran, Pham, Nguyen & Vo (2022) Cogent Econ. Finance 10(1), 2122188 | VERIFIED* | IDEAS handle v10y2022i1p2122188 fixes vol./issue/article; DOI consistent, not resolved | https://ideas.repec.org/a/taf/oaefxx/v10y2022i1p2122188.html |
| 8 | Chang, Pienaar & Gebbie (2021) Physica A 583, 126329 | VERIFIED | Vol. 583, p. 126329 and DOI 10.1016/j.physa.2021.126329 confirmed (author research page snippet) | https://sites.google.com/view/patrickchang/research ; https://arxiv.org/pdf/2011.11281 |
| 9 | Chen, Geng, Lin & Nguyen (2021) PBFJ 67, 101567 | VERIFIED* | Authors, title, vol. 67 confirmed (IDEAS PII S0927538X21000743); article no. and DOI consistent, not resolved | https://ideas.repec.org/a/eee/pacfin/v67y2021ics0927538x21000743.html |
| 10 | Chen, Zhang, Lu & Xie (2024) Heliyon **10(15)**, e36537 | **CORRECTED** | Issue is **17**, not 15: Heliyon 10(17), e36537 (15 Sep 2024). DOI 10.1016/j.heliyon.2024.e36537 confirmed. Author given names: Yijun Chen, Jun-hao Zhang, Lei Lu, Zi-miao Xie. | https://pubmed.ncbi.nlm.nih.gov/39281645/ ; https://www.sciencedirect.com/science/article/pii/S2405844024125686 |
| 11 | DeCoste (2025) GFJ 65, 101110 | VERIFIED* | Author, title, vol. 65 (May 2025) confirmed (PII S1044028325000377); article no. 101110 / DOI not shown in any snippet. Check on ScienceDirect. | https://www.sciencedirect.com/science/article/pii/S1044028325000377 ; https://ideas.repec.org/a/eee/glofin/v65y2025ics1044028325000377.html |
| 12 | Epps (1979) JASA 74(366), 291–298 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://en.wikipedia.org/wiki/Epps_effect ; https://katalog.dhi-paris.fr/vufind/Record/JST044029462 |
| 13 | Forbes & Rigobon (2002) JF 57(5), 2223–2261 | VERIFIED | DOI 10.1111/0022-1082.00494 confirmed (Wiley URL) | https://ideas.repec.org/a/bla/jfinan/v57y2002i5p2223-2261.html |
| 14 | Ge & Lin (2021) CSF 145, 110731 | VERIFIED | DOI 10.1016/j.chaos.2021.110731 confirmed | https://ideas.repec.org/a/eee/chsofr/v145y2021ics0960077921000849.html |
| 15 | Greenwood & Sammon (2025) JF 80(2), 657–698 | VERIFIED | DOI 10.1111/jofi.13410 confirmed | https://ideas.repec.org/a/bla/jfinan/v80y2025i2p657-698.html |
| 16 | Guedes, da Silva Filho & Zebende (2021) Physica A 574, 125990 | VERIFIED | DOI 10.1016/j.physa.2021.125990 confirmed | https://ideas.repec.org/a/eee/phsmap/v574y2021ics0378437121002624.html |
| 17 | Guo, Li & Li (2021) IRFA 73, 101649 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://ideas.repec.org/a/eee/finana/v73y2021ics1057521920302908.html |
| 18 | Holm (1979) Scand. J. Stat. 6(2), 65–70, JSTOR 4615733 | VERIFIED | Has no DOI; the stable JSTOR URL is correct | https://en.wikipedia.org/wiki/Holm%E2%80%93Bonferroni_method |
| 19 | Hong & Stein (1999) JF 54(6), 2143–2184 | VERIFIED | DOI 10.1111/0022-1082.00184 confirmed | https://www.citedrive.com/en/discovery/a-unified-theory-of-underreaction-momentum-trading-and-overreaction-in-asset-markets |
| 20 | Jiang & Zhou (2011) PRE 84(1), 016106 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://pubmed.ncbi.nlm.nih.gov/21867256 |
| 21 | Kakinaka, Hayakawa, Kato & Umeno (2025) AEL 32(3), 415–421 | VERIFIED | DOI 10.1080/13504851.2023.2274298 confirmed (online 31 Oct 2023) | https://ideas.repec.org/a/taf/apeclt/v32y2025i3p415-421.html |
| 22 | Kantelhardt et al. (2002) Physica A 316(1–4), 87–114 | VERIFIED* | Confirmed; DOI consistent, not resolved. Check the order of Havlin and Bunde against the published PDF (snippets differ). | https://ideas.repec.org/a/eee/phsmap/v316y2002i1p87-114.html |
| 23 | Karim, B. A., & Ning, H. X. (2013) APJBA 5(3), 186–191 | **CORRECTED (names)** | The authors are **Bakri Abdul Karim** and **Hoe Xin Ning** (UNIMAS lists "Hoe, Xin Ning"). Neither "Karim, B. A." nor "Ning, H. X." matches. Use either "Abdul Karim, B., & Hoe, X. N." (family names) or the publisher's form "Abdul Karim, B., & Xin Ning, H.", and change the in-text citation to match ("Abdul Karim and Hoe 2013" or "Abdul Karim and Xin Ning 2013"). Volume, issue, pages and DOI 10.1108/APJBA-07-2012-0053 are confirmed. | https://emeraldinsight.com/insight/content/doi/10.1108/APJBA-07-2012-0053/full/html ; https://ir.unimas.my/id/eprint/15922/ |
| 24 | Kristoufek (2014) Physica A 406, 169–175 | VERIFIED | DOI 10.1016/j.physa.2014.03.015 confirmed | https://ideas.repec.org/p/arx/papers/1311.0657.html |
| 25 | Le, Dang & Phan (2025) IJIRSS 8(4), **7901–7914** | **CORRECTED** | Pages are **535–553**. "7901" is the article ID, not a page number (IDEAS handle v8y2025i4p535-553id7901). Authors (Le Thi Thuy Van, Dang Thi Phuong Thao, Phan Thi Hang Nga), title and 8(4) are confirmed. DOI 10.53894/ijirss.v8i4.7901 follows the journal's pattern but was not resolved. | https://ideas.repec.org/a/aac/ijirss/v8y2025i4p535-553id7901.html ; https://ijirss.com/index.php/ijirss/article/view/7901 |
| 26 | Lean & Teng (2013) Econ. Modelling 32, 333–342 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://ideas.repec.org/r/eee/ecmode/v32y2013icp333-342.html |
| 27 | Liao, Coakley & Kellard (2022) IRFA 83, 102330 | VERIFIED | DOI 10.1016/j.irfa.2022.102330 confirmed | https://repository.essex.ac.uk/33243/ |
| 28 | Longin & Solnik (2001) JF 56(2), 649–676 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://faculty.essec.edu/en/research/extreme-correlation-of-international-equity-markets |
| 29 | Markowitz (1952) JF 7(1), 77–91 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://thuvienso.hoasen.edu.vn/items/75016f87-bff7-4dcd-b3c8-7c34158615d2/full |
| 30 | Michis (2022) JRFM 15(1), 24 | VERIFIED* | Confirmed (MDPI 1911-8074/15/1/24); DOI consistent, not resolved | https://www.mdpi.com/1911-8074/15/1/24/reprints |
| 31 | Nguyen, Bakry & Vuong (2023) JBEF 38, 100807 | VERIFIED | DOI 10.1016/j.jbef.2023.100807 confirmed | https://ideas.repec.org/a/eee/beexfi/v38y2023ics2214635023000217.html |
| 32 | Okorie & Lin (2021) FRL 38, 101640 | VERIFIED | DOI 10.1016/j.frl.2020.101640 confirmed | https://ideas.repec.org/a/eee/finlet/v38y2021ics1544612320305638.html |
| 33 | Oświęcimka, Drożdż, Forczek, Jadach & Kwapień (2014) PRE 89(2), 022805 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://ideas.repec.org/p/arx/papers/1308.6148.html |
| 34 | Peng et al. (1994) PRE 49(2), 1685–1689 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://cris.biu.ac.il/en/publications/mosaic-organization-of-dna-nucleotides/ |
| 35 | Podobnik & Stanley (2008) PRL 100(8), 084102 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://ideas.repec.org/p/arx/papers/0709.0281.html |
| 36 | Podobnik, Jiang, Zhou & Stanley (2011) PRE 84(6), 066118 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://www.bib.irb.hr/618539 |
| 37 | Politis & Romano (1994) JASA 89(428), 1303–1313 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://gnosis.library.ucy.ac.cy/handle/7/57533 |
| 38 | Rodriguez & Alvarez-Ramirez (2021) Physica A 581, 126211 | VERIFIED | DOI 10.1016/j.physa.2021.126211 confirmed | https://ideas.repec.org/a/eee/phsmap/v581y2021ics0378437121004842.html |
| 39 | Santana, Horta, Revez, Dias & Zebende (2023) Sustainability 15(5), 3945 | VERIFIED | DOI 10.3390/su15053945 confirmed | https://ideas.repec.org/a/gam/jsusta/v15y2023i5p3945-d1076109.html |
| 40 | Tilfani, Ferreira & El Boukfaoui (2021) Emp. Econ. 60(3), 1127–1156 | VERIFIED | DOI 10.1007/s00181-019-01806-1 confirmed | https://dspace.uevora.pt/rdpc/handle/10174/28582 |
| 41 | Tran & Tran (2025) VNU JEB 5(2), 51–59 | VERIFIED | Tran Manh Ha and Tran Ngoc Mai (Banking Academy of Vietnam); pages 51–59; DOI 10.57110/vnu-jeb.v5i2.395 confirmed | https://jeb.ueb.edu.vn/index.php/jeb/article/view/395 ; https://www.researchgate.net/publication/391206343_High-frequency_dynamics_of_the_Vietnam_stock_market |
| 42 | Wang, Ye, Chen & Wu (2021) CSF 143, 110645 | VERIFIED | DOI 10.1016/j.chaos.2020.110645 confirmed | https://ideas.repec.org/a/eee/chsofr/v143y2021ics0960077920310365.html |
| 43 | Zebende (2011) Physica A 390(4), 614–618 | VERIFIED* | Confirmed; DOI consistent, not resolved | https://search.r-project.org/CRAN/refmans/DFA/html/rhoDCCA.html |
| 44 | Zhou, W.-X. (2008) PRE 77(6), 066211 | VERIFIED | DOI 10.1103/PhysRevE.77.066211 confirmed | https://ideas.repec.org/p/arx/papers/0803.2773.html |
| 45 | Zhou, Huang & Wang (2025) Fractal Fract. 9(1), 14 | VERIFIED | DOI 10.3390/fractalfract9010014 confirmed (published 30 Dec 2024, vol. 2025) | https://www.mdpi.com/2504-3110/9/1/14 |

Unverifiable: none. All 45 exist. The 21 VERIFIED* items need a DOI-resolver pass from a network that can reach doi.org before submission (this is a tooling gap; no error is suspected).

## 3. Two-way matching (text and reference list)

All 45 references are cited in the text. Every author–year citation in the text appears in the list with the same spelling and year. Holm (1979) and Benjamini and Hochberg (1995) are cited formally in Section 4 (inference paragraph) and appear elsewhere as eponyms only, which is acceptable.

| Severity | Issue |
|---|---|
| MINOR | Karim and Ning (2013): the in-text form follows the incorrect reference names (see #23). Update both together. |
| MINOR | "Cohen's q" (H1 and Table 4 text) is used without a source. Optionally add Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Erlbaum. Verify it before adding. |

## 4. Claim–source alignment issues

| # | Severity | Location | Claim in manuscript | What the source says | Fix |
|---|---|---|---|---|---|
| A1 | **MAJOR** | §2.1 para 2 | "multifractal cross-correlations carry information about the direction of information flow between markets (Zhou et al. 2025)" | The study covers daily prices of **eight individual U.S. sector stocks** (JPM, XOM, AAPL, PG, SPG...), not markets. The **direction** of information flow comes from **transfer entropy**; MFDCCA only gives the strength of multifractal cross-correlation. | E.g., "...and multifractal cross-correlations can be combined with transfer entropy to map directional information flow among stocks (Zhou et al. 2025)." |
| A2 | **MAJOR** | §2.3 para 1; Table 1 row | "A DCCA-based test ... finds instead that pairs that were already highly interdependent showed no contagion (Santana et al. 2023)", presented as counter-evidence to COVID contagion | Santana et al. find no contagion **only for WTI–Brent** (already highly interdependent). For the **crude oil–precious metals** pairs they report greater interdependence and "clearly positive contagion". The sample is commodities, not equities. | Report both results: "...finds no contagion between the two crude-oil benchmarks, which were already highly interdependent, but positive contagion between oil and precious metals." Change the Table 1 finding to match. |
| A3 | **MAJOR** | §4.8, Eq. (14) | "MF-DCCA ... with absolute local covariances, which avoids complex-valued moments (Oświęcimka et al. 2014)" | Oświęcimka et al. propose MFCCA, which **keeps the sign** of local covariances. They show that existing MF-DXA variants, including those that take absolute values, "often indicate multifractal cross-correlations when there are none". Citing them to support the absolute-value choice inverts their recommendation. (§2.1 describes their critique correctly.) | Either adopt the sign-preserving MFCCA estimator, or keep |f²| and cite Oświęcimka et al. as a caveat: "we use absolute local covariances (Zhou 2008); Oświęcimka et al. (2014) show that this choice can overstate multifractality, so Δh is benchmarked against shuffled surrogates." |
| A4 | **MAJOR** (format and content) | Table 1 header | Header columns: "Overlap treated? / Main finding / Limitation for our question" | The Notes define a **volatility conditioning** column. The data rows hold Yes/No in the "Main finding" column and the findings in the "Limitation" column. Reading the headers as printed, the attributions are wrong (e.g., Forbes–Rigobon "Main finding: Yes"). | Rename the headers to "Overlap treated? / Volatility conditioning / Main finding". Add a "Limitation for our question" column only if it is filled in. |
| A5 | MINOR | §2.1 para 2; Table 1 | Okorie and Lin: contagion "that fades at medium and long horizons" | Abstract: the effect "diminishes over time in the middle and long run", i.e. over calendar time after the outbreak, not across DCCA timescales | "...that diminishes over time in the medium and long run" |
| A6 | MINOR | §2.1 para 2; Table 1 | "mean-DCCA and multifractal portfolio rules outperform mean-variance rules (Wang et al. 2021; Kakinaka et al. 2025)" | Wang et al. do report that Mean-MF-X-DMA beats traditional models. Kakinaka et al. compare **scale preferences within mean-DCCA** (short scales help in uncertain markets, long scales in steady markets) and do not claim superiority over mean-variance in the abstract. | Attribute outperformance to Wang et al. only, and cite Kakinaka et al. for scale-dependent performance |
| A7 | MINOR | §2.2 para 3; §6.1 | "Liquidity is concentrated in large firms ... (Chen et al. 2021)"; small stocks' "liquidity is thinner than that of large caps (Chen et al. 2021)" | Abstract: market liquidity **decreased after the MSS, more so for small firms**. The source does not establish the cross-sectional concentration claim. | "liquidity fell after the introduction of market surveillance, more so for small firms (Chen et al. 2021)". In §6.1 cite this only as "small firms' liquidity is more fragile". |
| A8 | MINOR | §2.3 para 1 | "Studies that do not condition on volatility report contagion: ... (Akhtaruzzaman et al. 2021)" | DCC correlations are computed from GARCH-standardized residuals, so they do condition on volatility. They do not apply the Forbes–Rigobon heteroskedasticity adjustment. | "Studies that do not apply a heteroskedasticity correction report contagion" |
| A9 | MINOR | Table 1, Santana row | Volatility conditioning: "Partly (pre/post comparison)" | A pre/post ΔρDCCA comparison does not correct for volatility | Change to "No" |
| A10 | MINOR | §2.2 para 1 | Greenwood and Sammon cited as evidence that "membership effects ... may weaken" | Their result concerns the **price (announcement) effect** of S&P 500 additions, which fell despite more indexing. The paper is not about co-movement. | State explicitly that the evidence concerns the price effect, and soften the inference about co-movement |
| A11 | MINOR | §2.2 para 2 | "its effects are small relative to the overlap we study" | No source; this is a comparative claim | Support it with the paper's own numbers or remove "small relative to" |

Checked and fairly attributed: Peng 1994; Kantelhardt 2002; Podobnik & Stanley 2008; Zebende 2011; Podobnik et al. 2011; Zhou 2008; Jiang & Zhou 2011; Kristoufek 2014; Guedes 2021; Ge & Lin 2021; Oświęcimka 2014 (in §2.1); Al Rababa'a 2021; Chen et al. 2024; Tilfani 2021; Barberis 2005; DeCoste 2025 (fuzzy RD, excess co-movement without change in fundamentals); Liao 2022; Michis 2022 (wavelet partial correlation); Rodriguez & Alvarez-Ramirez 2021; Nguyen et al. 2023 (herding on HOSE under falling prices); Bui et al. 2022 (>60% connectedness, about 90% in COVID-19, 24 sectors, 2012–2021); Tran & Tran 2025 (delayed diffusion, retail-heavy); Le et al. 2025 (nonlinear QQ dependence); Longin & Solnik 2001; Ang & Chen 2002; Forbes & Rigobon 2002; Guo 2021 (19 markets, more channels); Benkraiem 2022 (Asian and American indices, copula); Epps 1979; Chang 2021; Hong & Stein 1999; Karim & Ning 2013; Lean & Teng 2013; Politis & Romano 1994; Holm 1979; Benjamini & Hochberg 1995; Markowitz 1952.

## 5. Format (Springer author–year, APA-like)

| Severity | Issue | Fix |
|---|---|---|
| MAJOR | Table 1 header mismatch (A4) | as above |
| MINOR | The order of multiple citations inside parentheses is inconsistent: chronological in "(Longin and Solnik 2001; Ang and Chen 2002)" and "(Peng et al. 1994; Kantelhardt et al. 2002)", alphabetical in "(Chen et al. 2024; Ge and Lin 2021)" | Pick one convention (Springer Basic: chronological) and apply it throughout |
| MINOR | List order: "Podobnik, B., & Stanley, H. E. (2008)" precedes "Podobnik, B., Jiang, Z.-Q., ... (2011)". In APA-like sorting the second author decides, and Jiang < Stanley. | Swap the two entries (or follow Springer's rule of one-author, then two-author, then et al. chronologically, and state it consistently) |
| MINOR | "Zhou, W.-X. (2008)" precedes "Zhou, W., Huang, J., & Wang, M. (2025)". Initial "W." sorts before "W.-X.". | Swap them, or keep them if the journal's style sorts by year |
| MINOR | Le et al. pages (#25), Chen et al. 2024 issue (#10), Karim & Ning names (#23) | Correct them as in Section 2 |

All references with a DOI carry one. Holm (1979) correctly uses a stable JSTOR URL because it has no DOI. The DOIs use the https://doi.org/ form throughout.

## 6. Verdict

No fabricated or unverifiable reference was found. The reference list and the text match in both directions. Before submission: (1) apply the three metadata corrections; (2) fix the four MAJOR alignment and format problems (Zhou et al. 2025 misattribution, selective Santana et al. 2023 reporting, Oświęcimka et al. 2014 cited for the opposite of their recommendation, Table 1 headers); (3) resolve the 21 VERIFIED* DOIs from a network that can reach doi.org.
