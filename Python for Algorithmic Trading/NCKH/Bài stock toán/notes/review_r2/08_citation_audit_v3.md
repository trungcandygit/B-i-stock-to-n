# Citation audit v3 (Stage 4.5 integrity, citation part): independent auditor

- Skill: ARS `academic-paper`, citation-check mode (citation_compliance_agent rules). IRON RULE: a reference counts as verified only if WebSearch finds its metadata in a real source.
- Date: 2026-10-10. Fresh context. `notes/AUDIT_LEDGER.md` was not read.
- Inputs: `project_R/docx_build/r2_lit.py` (REFERENCES, 65 entries), `project_R/docx_build/r2/manuscript_anonymized.md` (body lines 1–753; 65 `referenceitem` blocks, the same list), `project_R/docx_build/r2/supplementary_material.md`.
- Leads used, with every new item re-checked: `notes/review_r2/newrefs_verified.md` and `notes/review_r2/integrity_2p5_citations.md` (the 2.5 audit, 45 references).
- Tooling: the proxy blocks api.crossref.org and doi.org (`curl` returned CONNECT 403). All evidence below comes from WebSearch snippets of publisher pages, IDEAS/RePEc, official Vietnamese legal databases, the LSEG/FTSE Russell site and HOSE notices.

## 1. Summary

| Check | Result |
|---|---|
| References in list | 65 (r2_lit.py and manuscript list are identical) |
| In-text citations with no list entry | 0 |
| List entries cited nowhere in the main text or supplement | 0 |
| Year or author-spelling mismatches between text and list | 0 |
| References whose existence is confirmed | 65 / 65; no fabricated reference found |
| Metadata corrections needed | 2: the FTSE Russell 2025 title and the Circular 120/2020 title. Minor notes on Shapley pages and the Cohen DOI. |
| Claim–source problems | 1 MAJOR (Corsetti et al. 2005 mechanism wording, §2.3 and Table 1). 3 MINOR: the FTSE tense now that the date has passed, Cureton "the correction", and Cohen's q used with dependent correlations. |
| Section 3.1 factual claims | 6 of 7 confirmed. The short-selling claim is confirmed by trade-press and VSDC statements but has no official citation (MINOR). |

## 2. Per-reference table

Status key:
- VERIFIED: authors, year, title, venue, volume, issue, pages and DOI all agree with the search evidence.
- VERIFIED (2.5): verified in the Stage 2.5 audit, re-checked against that audit's evidence, and the corrections it asked for are now in the list.
- CORRECTED: a field must change; the fix is given in the row.

### 2a. New or priority items (re-verified in this round)

| Reference | Status | Note / correction | Evidence URL |
|---|---|---|---|
| Pearson, K. (1897). Proc. R. Soc. Lond. 60, 489–498, doi 10.1098/rspl.1896.0076 | VERIFIED | Title, volume and pages confirmed. The DOI suffix carries "1896" because volume 60 covers 1896–97. The paper was read on 18 Feb 1897 (Galton's companion note is pp. 498–502, same date), so 1897 is the standard year. Keep it. | https://en.wikipedia.org/wiki/Spurious_correlation_of_ratios ; https://www.homepages.ucl.ac.uk/~ucfbpve/geostats/latex/geostats13.html ; https://galton.org/bib/JournalItem.aspx_action=view_id=264 |
| Cureton, E. E. (1966). Psychometrika 31(1), 93–96, doi 10.1007/BF02289461 | VERIFIED | — | https://ideas.repec.org/a/spr/psycho/v31y1966i1p93-96.html |
| Cremers & Petajisto (2009). RFS 22(9), 3329–3365, doi 10.1093/rfs/hhp057 | VERIFIED | — | https://ideas.repec.org/a/oup/rfinst/v22y2009i9p3329-3365.html |
| Corsetti, Pericoli & Sbracia (2005). JIMF 24(8), 1177–1199, doi 10.1016/j.jimonfin.2005.08.012 | VERIFIED (metadata) | Content wording needs a fix; see C1 | https://ideas.repec.org/a/eee/jimfin/v24y2005i8p1177-1199.html |
| Rigobon, R. (2003). REStat 85(4), 777–792, doi 10.1162/003465303772815727 | VERIFIED | DOI consistent with the MIT Press pattern; not resolved | https://ideas.repec.org/a/tpr/restat/v85y2003i4p777-792.html |
| Lo & MacKinlay (1990). RFS 3(2), 175–205, doi 10.1093/rfs/3.2.175 | VERIFIED | RePEc gives 175–205; the MIT author page says 175–206. Keep 175–205. | https://ideas.repec.org/a/oup/rfinst/v3y1990i2p175-205.html ; https://web.mit.edu/~alo/www/Papers/lo-mackinlay-90b.html |
| Hou, K. (2007). RFS 20(4), 1113–1138, doi 10.1093/rfs/hhm003 | VERIFIED | DOI shown in the RePEc handle | https://ideas.repec.org/a/oup/rfinst/v20y2007i4p1113-1138.html |
| Greenwood, R. (2008). RFS 21(3), 1153–1186, doi 10.1093/rfs/hhm052 | VERIFIED | DOI confirmed via the OUP listing | https://academic.oup.com/rfs/article-abstract/21/3/1153/1563300 ; https://ideas.repec.org/a/oup/rfinst/v21y2008i3p1153-1186.html |
| Chen, Singal & Whitelaw (2016). JFE 121(3), 624–644, doi 10.1016/j.jfineco.2016.05.007 | VERIFIED | — | https://ideas.repec.org/a/eee/jfinec/v121y2016i3p624-644.html ; https://www.nber.org/papers/w21281 |
| Andersen & Bollerslev (1997). JEF 4(2–3), 115–158, doi 10.1016/S0927-5398(97)00004-2 | VERIFIED | — | https://ideas.repec.org/a/eee/empfin/v4y1997i2-3p115-158.html ; https://scholars.duke.edu/publication/761297 |
| Diebold & Mariano (1995). JBES 13(3), 253–263, doi 10.1080/07350015.1995.10524599 | VERIFIED | DOI confirmed by the T&F landing page | https://www.tandfonline.com/doi/abs/10.1080/07350015.1995.10524599 |
| Patton, A. J. (2011). J. Econometrics 160(1), 246–256, doi 10.1016/j.jeconom.2010.03.034 | VERIFIED | — | https://scholars.duke.edu/publication/792433 |
| Schuirmann, D. J. (1987). J. Pharmacokinet. Biopharm. 15(6), 657–680, doi 10.1007/BF01068419 | VERIFIED | — | https://dx.doi.org/10.1007%2FBF01068419 ; https://zenodo.org/record/1232484 |
| Newey & West (1987). Econometrica 55(3), 703–708, doi 10.2307/1913610 | VERIFIED | A "Notes and Comments" item, May 1987 | https://www.econometricsociety.org/publications/econometrica/1987/05/01/notes-and-comments-simple-positive-semi-definite ; https://www.nber.org/papers/t0055 |
| Ederington, L. H. (1979). JF 34(1), 157–170, doi 10.1111/j.1540-6261.1979.tb02077.x | VERIFIED | The DOI follows the Wiley JF pattern; not resolved | https://mpra.ub.uni-muenchen.de/45754 |
| Shapley, L. S. (1953). In Kuhn & Tucker (Eds.), Contributions to the theory of games II, pp. 307–317, doi 10.1515/9781400881970-018 | VERIFIED | The chapter DOI is confirmed: De Gruyter "17. A Value for n-Person Games". The De Gruyter e-chapter shows pp. 307–318; the 1953 print is pp. 307–317. Keep 307–317 (print). Optionally add "Annals of Mathematics Studies 28". | https://www.degruyterbrill.com/document/doi/10.1515/9781400881970-018/html ; https://mathworld.wolfram.com/ShapleyValue.html |
| J.P. Morgan/Reuters (1996). RiskMetrics: Technical document (4th ed.). Morgan Guaranty Trust Company. | VERIFIED | 4th ed., New York, 17 Dec 1996, © Morgan Guaranty Trust Company. Optionally add "of New York" and the MSCI URL. λ = 0.94 for daily data is the document's standard value (shown in secondary snippets). | https://www.msci.com/research-and-insights/paper/1996-riskmetrics-technical-document |
| Government of Vietnam (2020). Decree No. 155/2020/ND-CP of 31 December 2020 ... | VERIFIED | Issued 31/12/2020, effective 01/01/2021 | https://thuvienphapluat.vn/van-ban/chung-khoan/nghi-dinh-155-2020-nd-cp-huong-dan-luat-chung-khoan-461323.aspx |
| Government of Vietnam (2025). Decree No. 245/2025/ND-CP of 11 September 2025 amending ... Decree No. 155/2020/ND-CP | VERIFIED | Issued and effective 11/9/2025 (LuatVietnam, Luat Minh Khue; Công báo 1403–1404, 27/9/2025). One provincial library lists 10/09; the national sources say 11/9. | https://luatvietnam.vn/tin-van-ban-moi/tu-11-9-2025-rut-ngan-thoi-gian-dua-chung-khoan-len-san-giao-dich-186-104047-article.html ; https://luatminhkhue.vn/van-ban/nghi-dinh-so-245-2025-nd-cp.aspx ; https://hcc.nghean.gov.vn/laws/detail/Nghi-dinh-so-245-2025-ND-CP-cua-Chinh-phu-Sua-doi-bo-sung-mot-so-dieu-cua-Nghi-dinh-so-155-2020-ND-CP-ngay-31-thang-12-nam-2020-cua-Chinh-phu-quy-dinh-chi-tiet-thi-hanh-mot-so-dieu-cua-Luat-Chung-khoan-1931/ |
| Ministry of Finance of Vietnam (2020). Circular No. 120/2020/TT-BTC of 31 December 2020 ... | **CORRECTED (title)** | The date (31/12/2020, effective 15/02/2021) is correct. The official title is about **shares**, not "listed securities, registered securities": "quy định giao dịch cổ phiếu niêm yết, đăng ký giao dịch và chứng chỉ quỹ, trái phiếu doanh nghiệp, chứng quyền có bảo đảm niêm yết trên hệ thống giao dịch chứng khoán". Use: "Circular No. 120/2020/TT-BTC of 31 December 2020 on trading of listed and registered shares, fund certificates, corporate bonds and covered warrants listed on the securities trading system. Hanoi." Optional: note "as amended by Circular 68/2024/TT-BTC". | https://thuvienphapluat.vn/van-ban/chung-khoan/circular-120-2020-tt-btc-trading-of-listed-and-registered-shares-on-securities-trading-systems-464506.aspx ; https://caselaw.vn/van-ban-phap-luat/369178-thong-tu-so-120-2020-tt-btc-ngay-31-12-2020-cua-bo-truong-bo-tai-chinh-quy-dinh-ve-giao-dich-co-phieu-niem-yet-dang-ky-giao-dich-va-chung-chi-quy-trai-phieu-doanh-nghiep-chung-quyen-co-bao-dam-niem-yet-tren-he-thong-giao-dich-chung-khoan |
| FTSE Russell (2025). FTSE Equity Country Classification: September 2025 interim announcement. LSEG. | **CORRECTED (title/date)** | In FTSE Russell's terms the September review is the annual or semi-annual review; "interim" means the March review. The real release was published on **7 October 2025** under the title "FTSE Russell announces results of September 2025 semi-annual country classification review". It moves Vietnam from Frontier to Secondary Emerging effective 21 Sep 2026, subject to a March 2026 interim review. Use: "FTSE Russell. (2025, October 7). FTSE Russell announces results of September 2025 semi-annual country classification review [Press release]. London Stock Exchange Group. https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2025/ftse-russell-country-classification-september-2025". The in-text "(FTSE Russell 2025)" stays as it is. | https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2025/ftse-russell-country-classification-september-2025 ; https://mondovisione.com/media-and-resources/news/ftse-russell-announces-results-of-september-2025-semi-annual-country-classificat-2025108/ ; https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2026/ftse-russell-announces-results-march-2026-semi-annual-country-classification-review-equities-fixed-income |
| Cohen, J. (1988). Statistical power analysis ... (2nd ed.). Lawrence Erlbaum Associates. doi 10.4324/9780203771587 | VERIFIED (minor note) | The 1988 Erlbaum 2nd ed. exists. The DOI belongs to the Routledge digital reissue of the same edition. That is acceptable, or write "Lawrence Erlbaum Associates (Routledge reissue)". | https://utstat.toronto.edu/brunner/oldclass/378f16/readings/CohenPower.pdf ; https://data.gesis.org/gesiskg/resource/reference_gesis-ssoar-90553_zis-Cohen1988Statistical_outcite |
| DeCoste, J. (2025). GFJ 65, 101110, doi 10.1016/j.gfj.2025.101110 | VERIFIED | The DOI, which the 2.5 audit had not resolved, is now confirmed | https://ideas.repec.org/a/eee/glofin/v65y2025ics1044028325000377.html |

### 2b. Items carried from the 2.5 audit (corrections now applied)

| Reference | Status | Note | Evidence URL |
|---|---|---|---|
| Abdul Karim & Xin Ning (2013) APJBA 5(3), 186–191 | VERIFIED (2.5) | The name fix is applied in the list and in the text | https://ir.unimas.my/id/eprint/15922/ |
| Akhtaruzzaman, Boubaker & Sensoy (2021) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/finlet/v38y2021ics1544612320305754.html |
| Al Rababa’a, Alomari & McMillan (2021) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/riibaf/v58y2021ics0275531921000568.html |
| Ang & Chen (2002) JFE 63(3) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/jfinec/v63y2002i3p443-494.html |
| Barberis, Shleifer & Wurgler (2005) | VERIFIED (2.5) | | https://shleifer.scholars.harvard.edu/publications/comovement |
| Benjamini & Hochberg (1995) | VERIFIED (2.5) | | https://citedrive.com/en/discovery/controlling-the-false-discovery-rate-a-practical-and-powerful-approach-to-multiple-testing |
| Benkraiem et al. (2022) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/finana/v81y2022ics105752192200103x.html |
| Bui et al. (2022) | VERIFIED (2.5) | | https://ideas.repec.org/a/taf/oaefxx/v10y2022i1p2122188.html |
| Chang, Pienaar & Gebbie (2021) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/phsmap/v583y2021ics0378437121006026.html |
| Chen, Geng, Lin & Nguyen (2021) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/pacfin/v67y2021ics0927538x21000743.html |
| Chen, Zhang, Lu & Xie (2024) Heliyon 10(17) | VERIFIED (2.5) | The issue fix (17) is applied | https://pubmed.ncbi.nlm.nih.gov/39281645/ |
| Epps (1979) | VERIFIED (2.5) | | https://en.wikipedia.org/wiki/Epps_effect |
| Forbes & Rigobon (2002) | VERIFIED (2.5) | | https://ideas.repec.org/a/bla/jfinan/v57y2002i5p2223-2261.html |
| Ge & Lin (2021) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/chsofr/v145y2021ics0960077921000849.html |
| Greenwood & Sammon (2025) | VERIFIED (2.5) | | https://ideas.repec.org/a/bla/jfinan/v80y2025i2p657-698.html |
| Guedes, da Silva Filho & Zebende (2021) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/phsmap/v574y2021ics0378437121002624.html |
| Guo, Li & Li (2021) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/finana/v73y2021ics1057521920302908.html |
| Holm (1979) | VERIFIED (2.5) | Has no DOI; uses the JSTOR stable URL | https://en.wikipedia.org/wiki/Holm%E2%80%93Bonferroni_method |
| Hong & Stein (1999) | VERIFIED (2.5) | | https://www.citedrive.com/en/discovery/a-unified-theory-of-underreaction-momentum-trading-and-overreaction-in-asset-markets |
| Jiang & Zhou (2011) | VERIFIED (2.5) | | https://pubmed.ncbi.nlm.nih.gov/21867256 |
| Kakinaka et al. (2025) | VERIFIED (2.5) | | https://ideas.repec.org/a/taf/apeclt/v32y2025i3p415-421.html |
| Kantelhardt et al. (2002) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/phsmap/v316y2002i1p87-114.html |
| Kristoufek (2014) | VERIFIED (2.5) | | https://ideas.repec.org/p/arx/papers/1311.0657.html |
| Le, Dang & Phan (2025) pp. 535–553 | VERIFIED (2.5) | The page fix is applied | https://ideas.repec.org/a/aac/ijirss/v8y2025i4p535-553id7901.html |
| Lean & Teng (2013) | VERIFIED (2.5) | | https://ideas.repec.org/r/eee/ecmode/v32y2013icp333-342.html |
| Liao, Coakley & Kellard (2022) | VERIFIED (2.5) | | https://repository.essex.ac.uk/33243/ |
| Longin & Solnik (2001) | VERIFIED (2.5) | | https://faculty.essec.edu/en/research/extreme-correlation-of-international-equity-markets |
| Markowitz (1952) | VERIFIED (2.5) | | https://thuvienso.hoasen.edu.vn/items/75016f87-bff7-4dcd-b3c8-7c34158615d2/full |
| Nguyen, Bakry & Vuong (2023) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/beexfi/v38y2023ics2214635023000217.html |
| Okorie & Lin (2021) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/finlet/v38y2021ics1544612320305638.html |
| Oświęcimka et al. (2014) | VERIFIED (2.5) | | https://ideas.repec.org/p/arx/papers/1308.6148.html |
| Peng et al. (1994) | VERIFIED (2.5) | | https://cris.biu.ac.il/en/publications/mosaic-organization-of-dna-nucleotides/ |
| Podobnik, Jiang, Zhou & Stanley (2011) | VERIFIED (2.5) | | https://www.bib.irb.hr/618539 |
| Podobnik & Stanley (2008) | VERIFIED (2.5) | | https://ideas.repec.org/p/arx/papers/0709.0281.html |
| Politis & Romano (1994) | VERIFIED (2.5) | | https://gnosis.library.ucy.ac.cy/handle/7/57533 |
| Santana et al. (2023) | VERIFIED (2.5) | | https://ideas.repec.org/a/gam/jsusta/v15y2023i5p3945-d1076109.html |
| Tilfani, Ferreira & El Boukfaoui (2021) | VERIFIED (2.5) | | https://dspace.uevora.pt/rdpc/handle/10174/28582 |
| Tran & Tran (2025) | VERIFIED (2.5) | | https://jeb.ueb.edu.vn/index.php/jeb/article/view/395 |
| Wang, Ye, Chen & Wu (2021) | VERIFIED (2.5) | | https://ideas.repec.org/a/eee/chsofr/v143y2021ics0960077920310365.html |
| Zebende (2011) | VERIFIED (2.5) | | https://search.r-project.org/CRAN/refmans/DFA/html/rhoDCCA.html |
| Zhou, Huang & Wang (2025) | VERIFIED (2.5) | | https://www.mdpi.com/2504-3110/9/1/14 |
| Zhou, W.-X. (2008) | VERIFIED (2.5) | | https://ideas.repec.org/p/arx/papers/0803.2773.html |

UNVERIFIABLE: none.

## 3. Section 3.1 factual claims

| Claim (manuscript line) | Status | Evidence |
|---|---|---|
| Settlement moved from T+3 to T+2 on 1 January 2016 (l.163) | CONFIRMED | VSD Decision 211/QĐ-VSD (18 Dec 2015). Trades from 29–31 Dec 2015 settled T+3; T+2 took effect 1 Jan 2016 and applied from the first trading day, 4 Jan 2016. https://en.vietstock.vn/2015/12/settlement-of-stock-trades-cut-one-day-36-223461.htm ; https://bizhub.vn/settlement-of-stock-trades-cut-one-day-post14549.html |
| ATO 09:00–09:15, continuous to 11:30, break 11:30–13:00, ATC 14:30–14:45 (l.166) | CONFIRMED | https://fpts.com.vn/customer-service/securities-trading/stock-trading-guide/trading-regulations/hose-trading-regulations/ ; https://shinhansec.com.vn/en/customer-support/underlying-securities.html |
| FUEDCMID listed on HOSE 29 Sep 2022 (l.168) | CONFIRMED | HOSE press release, 29/09/2022: 6,000,000 certificates; first mid-cap ETF. https://static2.vietstock.vn/vietstock/2022/9/29/20220929_3_2__tcbc_niem_yet_quy_etf_dcvfmvnmidcap__eng_final_.pdf ; https://vietnamnews.vn/economy/1339723/first-mid-cap-etf-listed-on-hose.html |
| Foreign ownership limit of 30% for commercial banks (l.170) | CONFIRMED | Decree 01/2014/ND-CP, kept by Decree 69/2025/ND-CP with case-by-case exceptions. https://vietnamnews.vn/economy/1694231/decree-on-foreign-investment-in-vietnamese-financial-institutions-amended.html |
| VN30 index futures trade on HNX (l.168) | CONFIRMED | HNX derivatives market since 10 Aug 2017. https://en.vietstock.vn/2017/08/vietnamese-derivatives-market-to-launch-with-vn30-futures-36-290094.htm |
| Circular 120/2020 provides a framework for covered short sales that is not yet operational (l.168) | CONFIRMED (trade press) | Circular 120 defines covered short sales of securities borrowed through the VSDC lending system. The VSDC chair said in 2025–26 that short selling and T+0 await KRX upgrades, with H2 2026 at the earliest and 2027–28 more likely. https://lawnet.vn/thong-tin-phap-luat/en/chinh-sach-moi/secured-short-selling-on-the-securities-market-in-vietnam-148911.html ; https://vneconomy.vn/chu-tich-vsdc-huong-toi-nang-cap-dung-luong-krx-phuc-vu-t0-ban-khong-ban-chung-khoan-cho-ve.htm . The hedge "to our knowledge" is appropriate. |
| FTSE: announced October 2025, Frontier to Secondary Emerging from 21 Sep 2026 (l.170) | CONFIRMED | The announcement was made on 7 Oct 2025 and confirmed at the March 2026 interim review (LSEG release, 7 Apr 2026). Tense issue: see C2. |

## 4. Claim–source alignment

| # | Severity | Location | Issue | Fix |
|---|---|---|---|---|
| C1 | **MAJOR** | §2.3 l.96; Table 1 l.123 ("common-shock bias") | The text says the FR correction "is biased toward finding no contagion when crises bring common shocks, because the correction assumes that idiosyncratic variance does not change". Corsetti et al. say the "no contagion" result comes from "arbitrary and unrealistic restrictions on the variance of **country-specific** shocks" in the crisis country: the correction treats the whole rise in crisis-country variance as common-factor variance. The bias is therefore tied to country-specific shocks, not to "common shocks". The causal clause is right; the "when" clause reverses it. Lines 148 and 358 already state it correctly. | l.96: "Corsetti et al. (2005) show that it is biased toward finding no contagion because it implicitly restricts the variance of country-specific shocks, which typically rises in a crisis, and they propose testing for a change in the factor loading instead." Table 1 l.123: change "common-shock bias" to "bias from restricted idiosyncratic variance". |
| C2 | MINOR | §3.1 l.170 | "will be reclassified ... from 21 September 2026". As of Oct 2026 that date has passed, and the March 2026 interim review confirmed the move. | "FTSE Russell announced in October 2025 that Vietnam would be reclassified from Frontier to Secondary Emerging status effective 21 September 2026 (FTSE Russell 2025), a decision confirmed at the March 2026 interim review." If the 2026 release is mentioned, cite it as a second reference: FTSE Russell (2026, April 7), press release, LSEG URL above. Otherwise drop the clause. |
| C3 | MINOR | §2.1 l.54 | "Cureton (1966) gave **the** correction that removes the item from the total." Henrysson (1963, Psychometrika 28, 211–218) published a correction earlier. Cureton's is one standard formula (it is the one Lertap uses). | Change to "Cureton (1966) gave a standard correction ...". |
| C4 | MINOR (method, not citation) | §5 l.469 | Cohen's q (Cohen 1988) is defined for **independent** correlations. ρ~AB~ and ρ~AM~ come from the same sample and are dependent. Using q as a descriptive Fisher-scale effect size is acceptable, but q's small/medium/large benchmarks assume independence. | Add "(used descriptively; the two coefficients are estimated on the same sample)". |
| — | OK | Pearson 1897 (l.31, 54, 251) | Two ratios with a common denominator are correlated when their numerators are independent: this matches the source. | — |
| — | OK | Chen, Singal & Whitelaw 2016 (l.29, 79) | Matched controls remove nearly all of the apparent excess comovement, and prior winners show rising betas. The sentence "much of the post-inclusion rise in co-movement also appears in matched stocks that were not added" is fair. Optional: add "with similar prior returns". | — |
| — | OK | Greenwood 2008 (l.76) | Overweighting goes with higher comovement with index stocks and lower comovement with non-index stocks; the source attributes this to commonality in trading. "Points to index-linked demand" is fair. | — |
| — | OK | Cremers & Petajisto 2009 (l.57) | Active Share is the share of holdings that differ from the benchmark: correct. | — |
| — | OK | Lo & MacKinlay 1990; Hou 2007 (l.86, 146, 687) | Large firms lead small firms; Hou finds slow intra-industry information diffusion: correct. | — |
| — | OK | Rigobon 2003 (l.96, 358) | Identification from regime heteroskedasticity, with structural parameters stable across regimes: correct. | — |
| — | OK | Andersen & Bollerslev 1997 (l.576) | Intraday periodicity, with high volatility at the open: correct. | — |
| — | OK | Diebold & Mariano 1995; Newey & West 1987; Patton 2011; Schuirmann 1987; Ederington 1979 (variance reduction = ρ² for the minimum-variance hedge); Shapley 1953 (order-averaged attribution); RiskMetrics λ = 0.94 | Each is cited for the property it actually has. | — |

## 5. Two-way match

A script matched every list entry (first author + year) against the body (lines 1–753) and the supplement, and every author–year pattern in the text against the list.
- Every one of the 65 entries is cited at least once. Oświęcimka et al. 2014 is also cited in the supplement. The supplement cites no work that is missing from the list.
- No in-text citation lacks a list entry. Spellings match: "Abdul Karim and Xin Ning 2013", "Al Rababa’a et al. 2021", "Oświęcimka", "J.P. Morgan/Reuters 1996", "Government of Vietnam 2020/2025", "Ministry of Finance of Vietnam 2020", "FTSE Russell 2025".
- Rodriguez & Alvarez-Ramirez (2021) and Michis (2022), present in the 2.5 version, are gone from both the list and the text, so they leave no orphan.

## 6. Exact fixes

1. **r2_lit.py, Circular entry**, replace with:
   `Ministry of Finance of Vietnam. (2020). Circular No. 120/2020/TT-BTC of 31 December 2020 on trading of listed and registered shares, fund certificates, corporate bonds and covered warrants listed on the securities trading system. Hanoi.`
2. **r2_lit.py, FTSE entry**, replace with:
   `FTSE Russell. (2025, October 7). FTSE Russell announces results of September 2025 semi-annual country classification review [Press release]. London Stock Exchange Group. https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2025/ftse-russell-country-classification-september-2025`
3. **Manuscript l.96**, replace "Corsetti et al. (2005) show that it is biased toward finding no contagion when crises bring common shocks, because the correction assumes that idiosyncratic variance does not change, and they propose testing for a change in the factor loading instead." with "Corsetti et al. (2005) show that it is biased toward finding no contagion because it implicitly restricts the variance of country-specific shocks, which typically rises in a crisis, and they propose testing for a change in the factor loading instead."
4. **Table 1 l.123**: change "common-shock bias" to "bias from restricted idiosyncratic variance".
5. **l.170**: change "will be reclassified ... from 21 September 2026" to "would be reclassified ... effective 21 September 2026". Optionally add "a decision confirmed at the March 2026 interim review".
6. **l.54**: change "gave the correction" to "gave a standard correction".
7. **l.469** (optional): after "Cohen’s q (Cohen 1988)", add "used descriptively, since both coefficients come from the same sample".
8. Optional polish: RiskMetrics publisher "Morgan Guaranty Trust Company of New York". Shapley: add "(Annals of Mathematics Studies 28)".

None of these fixes changes a number, so no R output needs to be re-run.

## 7. Verdict

All 65 references exist, and their metadata matches real sources apart from the two title corrections above. Text and list match in both directions. One MAJOR wording problem remains (C1, the mechanism attributed to Corsetti et al.) plus three MINOR ones. With fixes 1–6 applied, the citation part of Stage 4.5 passes.
