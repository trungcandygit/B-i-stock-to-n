contract_role: eic
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: warn
trigger: "missing or incomplete Springer-required elements such as declarations"

### D6: venue_fit_and_contribution
score: warn
trigger: "novelty claims that are somewhat overstated"

## Review Body

Editorial assessment as associate editor for Asia-Pacific Financial Markets (Springer). The manuscript is clearly in scope: its whole empirical core uses Vietnamese (HOSE) index data at four frequencies, and the question it asks, how much of the measured co-movement between nested size-tier indices comes from shared constituents, matters to regional allocators and index providers. The contribution is set out plainly in three numbered points, and the robustness section qualifies the weaker results honestly. The abstract (198 words), six alphabetical keywords, JEL codes, name-year citations, table notes placed below tables, and "Fig. n" captions all follow the venue instructions. My concerns are about positioning and presentation, not scope. The ASEAN-wide policy framing goes beyond single-market evidence. The paper does not engage with regional literature near this venue. The headline portfolio figure applies to an asset that cannot be traded. On presentation, the Springer declarations are incomplete (no funding statement), the reference list follows APA rather than Springer house style, and several results appear only in the text or in the wrong section. All of these can be fixed in revision. Equation typography could not be judged because the equations were flattened from Word math, so I make no finding on equation rendering itself.

### S1: Unambiguous venue fit through Asia-Pacific multi-frequency data
The empirical analysis rests entirely on HOSE index data at intraday and daily frequencies over 2014–2025, which meets the venue's requirement for empirical analysis of Asia-Pacific financial data.
**Evidence Anchor**: text: Abstract "30-minute, 1-hour, 4-hour and daily data from the Ho Chi Minh City Stock Exchange (2014–2025)"

### S2: Explicit, enumerated contribution statement
The introduction states three distinct contributions (overlap distortion, volatility-conditioned crisis dynamics, portfolio-variance cost), and each maps onto a results subsection. This makes the paper easy for an editor to triage.
**Evidence Anchor**: text: §1 "This study makes three primary contributions to the extant empirical finance and risk management literature."

### S3: Self-contained tables with notes and sources below
Tables carry notes below the body that define constructed quantities (nested group, srel, detrending order) and give sources, as the journal's table-footnote convention requires.
**Evidence Anchor**: table: Table 2 — Notes define the nested group, the s ≤ srel averaging window and m = 1 below the table

### S4: Front matter conforms to venue instructions
The abstract is within 150–250 words (198). The six keywords are in alphabetical order, and JEL codes are supplied.
**Evidence Anchor**: text: Keywords "constituent overlap, DCCA, Forbes–Rigobon adjustment, multiscale correlation, portfolio risk, Vietnam"

### S5: Candid presentation of a weakening robustness result
The robustness table labels the Pcap–VN30 reliable-range slope as weakening, and the text downgrades that claim to "suggestive". This transparency strengthens editorial trust in the other claims.
**Evidence Anchor**: table: Table 6 — Pcap–VN30 row, reliable-range slope 0.0017 (0.0010) labelled "Weakens"

### S6: Dedicated limitations section with concrete remedies
Section 4.2 names the single-snapshot weight, the observational equivalence of the Epps and diffusion channels, and the exogeneity assumption. It pairs each with a concrete future remedy.
**Evidence Anchor**: text: §4.2 "This study has limitations that suggest directions for future research."

### W1: ASEAN-wide implications exceed single-market evidence
**Problem**: The abstract's closing sentence and Section 4.1 draw policy prescriptions for ASEAN capital markets in general, including Malaysian funds and regional pension managers. The evidence, however, comes from Vietnam alone. The introduction frames the Malaysia/Thailand/Indonesia contrast as an "institutional comparative hypothesis", but this hypothesis is never tested and appears again only as future research in Section 4.2.
**Evidence Anchor**: text: Abstract "highlight the imperative for independent mid-cap benchmarks and volatility-regime-sensitive risk budgeting across the capital markets of the Association of Southeast Asian Nations"
**Why it matters**: For a regional journal, overstating how far the findings generalise is the main thing a handling editor and referees will push back on. It also blurs the actual contribution, which is Vietnam-specific evidence under a short-sale ban.
**Suggestion**: Either confine the abstract, contributions and Section 4.1 to Vietnam and present ASEAN relevance as a conjecture, or add at least one comparison market (for example SET50 within SET100) to support the regional claim. Rephrase the "institutional comparative hypothesis" as a motivation rather than a tested proposition.
**Severity**: Major
**Confidence**: 4 — core editorial competence: venue scope and claim–evidence alignment

### W2: Thin engagement with regional and venue-adjacent literature
**Problem**: Regional literature is limited to two 2013 integration studies and two 2025 Vietnam papers. There is no engagement with recent Asia-Pacific DCCA/MF-DCCA or size-tier co-movement work, including work published in this journal. The novelty claim that nested architectures "remain an unaddressed empirical issue" therefore rests on a narrow search.
**Evidence Anchor**: absence: §1 Introduction and References — expected recent Asia-Pacific or venue-published multiscale or size-tier co-movement studies positioning the novelty claim; checked §1, §4.1, §4.2, References
**Why it matters**: Referees at this journal will judge originality against the regional literature. An unsupported gap claim invites a desk-level request for repositioning.
**Suggestion**: Add a short positioning paragraph covering recent Asia-Pacific multiscale cross-correlation and index-overlap studies, and soften the "unaddressed" claim to match what the search supports.
**Severity**: Minor
**Confidence**: 3 — editorial judgement: positioning, not an exhaustive literature audit

### W3: Headline portfolio-variance figure refers to a non-investable construct
**Problem**: The abstract and conclusion headline a static-correlation variance overstatement of up to 15.6% for "mid-cap portfolio variance". Yet Section 2.2 states that Pcap requires a 315%/215% long–short position and cannot be held under the short-sale ban. For the portfolios that can actually be held (parent–child cash portfolios), the error is at most 2.7%.
**Evidence Anchor**: text: §2.2 "the proxy cannot be executed in cash portfolios under the short-sale prohibition"
**Why it matters**: Practitioner readers of the venue may read the 15.6% as an achievable risk-management gain. The framing weakens the credibility of the third contribution.
**Suggestion**: In the abstract and Section 4, state that the 15.6% applies to a shadow mid-cap factor exposure, report the investable-portfolio figure alongside it, and link the implication to a tradable VNMIDCAP-based instrument.
**Severity**: Minor
**Confidence**: 4 — core editorial competence: abstract–body consistency

### W4: Springer declarations incomplete — no funding statement
**Problem**: The declarations block includes ethics, data availability, code availability, conflict of interest and AI use, but has no Funding statement. Springer's standard declarations require one, even if it is "No funding was received".
**Evidence Anchor**: absence: declarations block after §4.2 — expected a Funding statement required by Springer declarations; checked §4.2 declarations, front matter, References
**Why it matters**: A missing mandatory declaration usually triggers a technical return from the editorial office before review.
**Suggestion**: Add a "Funding" declaration. Consider also depositing the R code in a repository rather than making it available only on request, in line with Springer's research-data policy.
**Severity**: Minor
**Confidence**: 4 — core editorial competence: Springer submission conventions

### W5: Reference list follows APA rather than Springer name-year style
**Problem**: References use APA formatting (ampersands, parenthesised year after the authors, full DOI URLs). Springer's name-year (Basic) reference style differs in punctuation and author separators.
**Evidence Anchor**: text: References "Ang, A., & Chen, J. (2002). Asymmetric correlations of equity portfolios."
**Why it matters**: Inconsistency with the journal's style is flagged at technical check, and it signals that the manuscript was not prepared for this venue.
**Suggestion**: Reformat the reference list to the Springer Basic (name-year) style from the journal's LaTeX/Word template.
**Severity**: Minor
**Confidence**: 3 — editorial convention knowledge; the exact template variant should be confirmed

### W6: Announced subset relation is not displayed
**Problem**: The introduction announces a formal subset relation for VN30 within VN100 within VNINDEX, but no expression follows. This may be a Word-math flattening artifact.
**Evidence Anchor**: text: §1 "satisfying the strict subset relation:"
**Why it matters**: The paper's framing depends on the nesting, and a dangling colon before a new paragraph reads as an omission.
**Suggestion**: Confirm that the display equation (VN30 ⊂ VN100 ⊂ VNINDEX) renders in the submitted file, or state the relation in the text.
**Severity**: Minor
**Confidence**: 2 — possible conversion artifact; cannot verify the source file

### W7: Results placed outside their natural sections
**Problem**: Section 3.3 (reliability thresholds) also reports detrending-order robustness and correlations between Pcap and the statistical proxies. Section 2.2 (methods) reports estimated results: auxiliary-regression R², the Pheur standard deviation, and inter-proxy correlations.
**Evidence Anchor**: text: §3.3 "The estimates are insensitive to the detrending order"
**Why it matters**: A reader looking for robustness evidence will look in Section 3.8, and results in the methods section blur the line between design and findings.
**Suggestion**: Move the detrending-order and proxy-comparison results into Section 3.8 (or a new 3.8.3), and keep Section 2.2 to definitions with at most a forward reference to the results.
**Severity**: Minor
**Confidence**: 4 — core editorial competence: manuscript organisation

### W8: Some reported statistics appear only in the text, not in any table
**Problem**: Several quantitative results that support claims are given only in the prose. These are the daily-frequency scaling slopes, the nested-pair regime correlations used for diagnostic comparison, and the reliable-range p = 0.102. Table 4 has only one row per panel.
**Evidence Anchor**: text: §3.7 "at the daily frequency, the Pcap–VN30 slope is insignificant (0.0014, p = 0.47)"
**Why it matters**: Numbers given only in the text are harder for referees to verify, and the daily-versus-intraday contrast is part of the first contribution.
**Suggestion**: Add a daily-frequency panel to Table 5, add nested-pair diagnostic rows (marked as not formally tested) to Table 4, and add p-values to Table 6.
**Severity**: Minor
**Confidence**: 4 — core editorial competence: table/figure presentation

### W9: Redundant institutional passages in the introduction
**Problem**: The Bursa Malaysia RSS/IDSS contrast appears almost word for word in two introduction paragraphs (paragraphs 2 and 6), and it overlaps with the institutional material in Section 1.1.
**Evidence Anchor**: text: §1 paragraph 6 "While mature regional platforms such as Bursa Malaysia provide market-completeness mechanisms"
**Why it matters**: The repetition makes the introduction longer without adding content and delays the statement of the research gap.
**Suggestion**: Keep one concise mention, preferably in Section 1.1, and shorten the introduction accordingly.
**Severity**: Minor
**Confidence**: 4 — core editorial competence: exposition

### W10: Heading hierarchy and roadmap inconsistencies
**Problem**: Subsections 3.8.1 and 3.8.2 are formatted at the same level as 3.8. The roadmap says "Section 2 presents the data and methods", but the heading reads "2 Methods". Institutional background sits as 1.1 inside the Introduction.
**Evidence Anchor**: text: §3.8 "3.8.1 Full-Range versus Reliable-Range Stability"
**Why it matters**: The journal requires decimal headings of no more than three levels with a consistent hierarchy, and inconsistent levels cause problems at typesetting.
**Suggestion**: Apply heading styles consistently (3.8 → 3.8.1 as level 3), rename Section 2 "Data and Methods", and consider promoting institutional background to its own Section 2.
**Severity**: Minor
**Confidence**: 3 — heading levels may partly reflect conversion; hierarchy text is verbatim

### W11: Displayed equations are unnumbered and referenced only positionally
**Problem**: None of the displayed equations carries a number. The text refers to them as "the auxiliary regression above" or "the exact expression".
**Evidence Anchor**: absence: §2.2–§3.6 displayed equations — expected numbered equations for cross-reference; checked §2.1, §2.2, §2.3, §2.4, §2.5, §2.6, §3.6
**Why it matters**: Referees cannot cite specific formulas precisely, and Springer typesetting expects numbered display equations when they are referenced.
**Suggestion**: Number all display equations, (1) to (n), and replace positional references with equation numbers.
**Severity**: Minor
**Confidence**: 2 — flattened Word math may have stripped existing numbers
