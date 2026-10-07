"""Assemble submission/Revised_submission/ for the round-2 manuscript (target journal chosen later by the authors).

Run after build_r2.py.  Produces title page, anonymized manuscript, figures, competing-interest declaration,
replication package (+ zip), generic cover letter, manuscript with author details, highlights and the
response to the previous reviews."""
import os, re, shutil, subprocess, sys, zipfile
S = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, S)
import r2_text as TX
from build_r2 import post, CREDIT

B = os.path.abspath(os.path.join(S, '..', '..'))
PR = os.path.join(B, 'project_R')
OUT = os.path.join(B, 'submission', 'Revised_submission')
REF = os.path.join(S, 'r2', 'reference.docx')
DATE = '7 October 2026'
FIGS = [('Fig1', 'fig1_volatility_regimes', 'Fig1'), ('Fig2', 'fig2_dcca_curves', 'Fig2'),
        ('Fig3', 'fig4_overlap_decomposition', 'Fig4'), ('Fig4', 'fig3_mfdcca', 'Fig3')]   # manuscript no., png stem, eps stem


def md2docx(md, out, postprocess=True):
    p = out[:-5] + '.md'
    open(p, 'w', encoding='utf-8').write(md)
    subprocess.run(['pandoc', p, '-f', 'markdown+fenced_divs+superscript+subscript+pipe_tables', '-t', 'docx',
                    '--reference-doc', REF, '-o', out], check=True)
    os.remove(p)
    if postprocess:
        post(out)


def title_page():
    md = f"""::: {{custom-style="Title"}}
{TX.TITLE}
:::

::: {{custom-style="p1a"}}
Nguyen Thanh Binh^a^, Nguyen Van Trung^a,\\*^, Ha Hong Hanh^b^, Nguyen Bach Diep^a^
:::

::: {{custom-style="Compact"}}
^a^ Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam

^b^ School of Accounting and Auditing, National Economics University, Hanoi, Vietnam

\\* Corresponding author: Nguyen Van Trung, Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam. Email: 15233582\\@st.neu.edu.vn. Tel: +84 355 347 831.
:::

::: {{custom-style="heading2"}}
Author details
:::

::: {{custom-style="p1a"}}
Nguyen Thanh Binh: nguyenthanhbinhapd\\@apd.edu.vn; ORCID 0009-0007-0042-2835. Nguyen Van Trung: 15233582\\@st.neu.edu.vn; ORCID 0009-0008-3307-6569. Ha Hong Hanh: hanhhh\\@neu.edu.vn; ORCID 0000-0003-3581-6571. Nguyen Bach Diep: diepnb\\@apd.edu.vn; ORCID 0009-0003-0967-7528.
:::

::: {{custom-style="heading2"}}
Keywords and JEL classification
:::

::: {{custom-style="p1a"}}
Keywords: {TX.KEYWORDS}. JEL: {TX.JEL}.
:::

::: {{custom-style="heading2"}}
Declarations
:::

::: {{custom-style="p1a"}}
**Acknowledgements** None. **Funding** This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. **Conflict of interest** The authors declare that they have no conflict of interest. **Author contributions (CRediT)** {CREDIT} **Data availability** The index price data were obtained from TradingView (exchange: HOSE) and are subject to the vendor’s terms of use; the merged dataset is available from the corresponding author upon reasonable request. **Code availability** The R code that reproduces every table and figure is provided as Online Resource 1 and will be deposited in a public repository upon acceptance. **Companion work** This manuscript is a substantially revised version of a manuscript previously declined by Asia-Pacific Financial Markets; it is not under consideration elsewhere.
:::
"""
    md2docx(md, os.path.join(OUT, '01_Title_Page.docx'))


def coi():
    md = f"""::: {{custom-style="heading1"}}
Declaration of competing interest
:::

::: {{custom-style="p1a"}}
Manuscript: “{TX.TITLE}”

The authors declare that they have no conflict of interest. No author has a financial relationship with an organization that sponsored the research; the research received no specific funding.

Authors: Nguyen Thanh Binh, Nguyen Van Trung (corresponding author), Ha Hong Hanh, Nguyen Bach Diep. Date: {DATE}.
:::
"""
    md2docx(md, os.path.join(OUT, '04_Declaration_of_Competing_Interest.docx'))


def cover_letter():
    sh = [float(TX.D(t, 'mech_share')['estimate']) for t in TX.TF]
    md = f"""::: {{custom-style="p1a"}}
{DATE}

The Editor-in-Chief

[JOURNAL NAME — to be completed by the authors]

**Submission of manuscript: “{TX.TITLE}”**

Dear Editor,

We submit the enclosed manuscript for consideration as an original research article in [JOURNAL NAME].

Correlations between nested equity indices, such as a large-cap index and the broader index that contains it, are routinely used to measure diversification between size tiers. We prove that such correlations contain a mechanical floor fixed by index weights and relative volatility, and we derive an exact, scale-by-scale decomposition of the detrended cross-correlation coefficient into this floor and an economic component. Applied to the Vietnamese VN30, VN100 and VNINDEX indices at 30-minute to daily frequencies, the floor accounts for {TX.rng(sh, 2)} of the VN30–VN100 coefficient, so the index-level number is almost insensitive to the economic co-movement between large and mid caps.

The paper tests five pre-stated hypotheses with block-bootstrap inference and multiple-testing adjustment: overlap inflation, dominance of the mechanical floor, horizon dependence, crisis contagion after Forbes–Rigobon conditioning, and the cost of static correlations for portfolio variance. The R code that reproduces every number is provided as Online Resource 1.

This manuscript is a substantially revised version of a manuscript declined by Asia-Pacific Financial Markets, whose editor found the earlier version to be mainly a statistical report. The revision adds the analytical result (Proposition 1), hypotheses, an analytical literature review with recent references, multiplicity-adjusted inference, effect sizes and additional robustness checks. The manuscript is not under consideration by another journal, and all authors approve its submission. The authors’ use of generative AI tools is described in the declaration placed before the references.

Sincerely,

Nguyen Van Trung (corresponding author), on behalf of all authors\\
Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam\\
Email: 15233582\\@st.neu.edu.vn; Tel: +84 355 347 831
:::
"""
    md2docx(md, os.path.join(OUT, '06_Cover_Letter.docx'))


def highlights():
    sh = [float(TX.D(t, 'mech_share')['estimate']) for t in TX.TF]
    sens = [float(TX.D(t, 'sensitivity')['estimate']) for t in TX.TF]
    items = [
        'Nested index correlations contain a mechanical floor set by index weights',
        'An exact scale-wise identity splits the DCCA coefficient into floor and economics',
        f'The floor is {TX.rng(sh, 2)} of the VN30–VN100 coefficient in Vietnam',
        f'Nested coefficients respond to economic correlation with slope {TX.rng(sens, 2)} only',
        'No crisis contagion between size tiers after Forbes–Rigobon conditioning',
    ]
    md = '::: {custom-style="heading1"}\nHighlights\n:::\n\n' + '\n\n'.join(f'::: {{custom-style="p1a"}}\n• {i}\n:::' for i in items)
    for i in items:
        assert len(i) <= 85, (len(i), i)
    md2docx(md, os.path.join(OUT, '08_Highlights.docx'))


def response():
    src = os.path.join(B, 'notes', 'review_r2', 'response_to_reviewers.md')
    out = os.path.join(OUT, '09_Response_to_Reviewers.docx')
    subprocess.run(['pandoc', src, '-f', 'markdown+pipe_tables', '-t', 'docx', '--reference-doc', REF, '-o', out], check=True)


def figures():
    d = os.path.join(OUT, '03_Figures'); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    for num, png, eps in FIGS:
        shutil.copy(os.path.join(PR, 'outputs', 'figures', png + '.png'), os.path.join(d, num + '.png'))
        shutil.copy(os.path.join(PR, 'outputs', 'figures', eps + '.eps'), os.path.join(d, num + '.eps'))


def replication():
    d = os.path.join(OUT, '05_Replication_Package'); shutil.rmtree(d, ignore_errors=True)
    os.makedirs(os.path.join(d, 'data')); os.makedirs(os.path.join(d, 'R'))
    for f in ('run_all.R', 'run_revision.R', 'run_round2.R'):
        s = open(os.path.join(PR, f), encoding='utf-8').read().replace('../project/data/', 'data/')
        open(os.path.join(d, f), 'w', encoding='utf-8').write(s)
    shutil.copy(os.path.join(PR, 'R', 'dcca.R'), os.path.join(d, 'R', 'dcca.R'))
    shutil.copytree(os.path.join(PR, 'outputs'), os.path.join(d, 'outputs'))
    shutil.copy(os.path.join(B, 'notes', 'review_r2', 'replication_README.md'), os.path.join(d, 'README.md'))
    open(os.path.join(d, 'data', 'PLACE_DATA_HERE.txt'), 'w').write('Place vn_indices_merged_filled.csv and vn_indices_merged_raw.csv here (see README).\n')
    z = os.path.join(OUT, '05_Replication_Package.zip')
    if os.path.exists(z):
        os.remove(z)
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(d):
            for f in sorted(files):
                p = os.path.join(root, f); zf.write(p, os.path.relpath(p, OUT))


def manuscripts():
    shutil.copy(os.path.join(S, 'r2', 'manuscript_anonymized.docx'), os.path.join(OUT, '02_Manuscript_Anonymized.docx'))
    shutil.copy(os.path.join(S, 'r2', 'manuscript_with_authors.docx'), os.path.join(OUT, '07_Manuscript_with_Author_Details.docx'))
    # anonymize metadata of the blinded manuscript
    z = os.path.join(OUT, '02_Manuscript_Anonymized.docx'); tmp = z + '.d'
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    with zipfile.ZipFile(z) as zf:
        zf.extractall(tmp)
    core = os.path.join(tmp, 'docProps', 'core.xml')
    if os.path.exists(core):
        s = open(core, encoding='utf-8').read()
        for tag in ('dc:creator', 'cp:lastModifiedBy', 'dc:title'):
            s = re.sub(rf'<{tag}>[^<]*</{tag}>', f'<{tag}></{tag}>', s)
        open(core, 'w', encoding='utf-8').write(s)
    for f in ('people.xml', 'comments.xml'):
        assert not os.path.exists(os.path.join(tmp, 'word', f)), f
    os.remove(z); subprocess.run(['bash', os.path.join(S, 'pack.sh'), tmp, z], check=True); shutil.rmtree(tmp)
    # assert blinding
    with zipfile.ZipFile(z) as zf:
        txt = ' '.join(zf.read(n).decode('utf-8', 'ignore') for n in zf.namelist() if n.endswith('.xml'))
    for bad in ('Binh', 'Trung', 'Hanh', 'Diep', 'apd.edu', 'neu.edu', 'Academy of Policy', 'National Economics University', '15233582'):
        assert bad not in txt, bad


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    manuscripts(); title_page(); figures(); coi(); replication(); cover_letter(); highlights(); response()
    print('package ->', OUT)
