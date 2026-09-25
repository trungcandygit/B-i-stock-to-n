"""Build the APFM submission package from the final manuscript and the authors' title-page / cover-letter templates."""
import copy, os, re, shutil, subprocess, sys
from lxml import etree
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_docx import *
S = os.path.dirname(os.path.abspath(__file__)); U = '/root/.claude/uploads/5a32a139-cc91-5731-8a96-6f9437c01080/'
B = '/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán'
OUT = B + '/submission/APFM_submission'
TITLE = 'Nested Equity Index Correlations Overstate True Co-Movement: Evidence from Vietnam'
APD = 'Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam'
NEU = 'School of Accounting and Auditing, National Economics University, Hanoi, Vietnam'
AUTH = 'Nguyen Thanh Binh^{a}, Nguyen Van Trung^{a,*}, Ha Hong Hanh^{b}, Nguyen Bach Diep^{a}'
CORR = '* Corresponding author: Nguyen Van Trung, ' + APD + '. Email: 15233582@st.neu.edu.vn. Tel: +84 355 347 831.'
DETAILS = ['Nguyen Thanh Binh: nguyenthanhbinhapd@apd.edu.vn; ORCID 0009-0007-0042-2835',
           'Nguyen Van Trung: 15233582@st.neu.edu.vn; ORCID 0009-0008-3307-6569',
           'Ha Hong Hanh: hanhhh@neu.edu.vn; ORCID 0000-0003-3581-6571',
           'Nguyen Bach Diep: diepnb@apd.edu.vn; ORCID 0009-0003-0967-7528']
COI = 'The authors declare that they have no conflict of interest.'
FUND = 'This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.'
CREDIT = ('Nguyen Thanh Binh: Conceptualization, Supervision, Validation, Writing – review & editing. '
          'Nguyen Van Trung: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Software, Visualization, Writing – original draft, Writing – review & editing. '
          'Ha Hong Hanh: Validation, Writing – review & editing. '
          'Nguyen Bach Diep: Methodology, Formal analysis, Writing – original draft.')
DATA = ('The index price data were obtained from TradingView (exchange: HOSE) and are subject to the vendor’s terms of use; '
        'the merged dataset is available from the corresponding author upon reasonable request.')
CODE = ('The R code that reproduces every table and figure is provided as Online Resource 1 (replication package) '
        'and will be deposited in a public repository upon acceptance.')

def load(src, d):
    shutil.rmtree(d, ignore_errors=True); os.makedirs(d); subprocess.run(['unzip', '-q', src, '-d', d], check=True)
    t = etree.parse(d + '/word/document.xml'); return t, t.getroot().find(W + 'body')
def paras(body): return [p for p in body if p.tag == W + 'p']
def scrub_core(d):
    f = d + '/docProps/core.xml'
    if os.path.exists(f):
        s = open(f, encoding='utf-8').read()
        s = re.sub(r'<dc:creator>[^<]*</dc:creator>', '<dc:creator></dc:creator>', s)
        s = re.sub(r'<cp:lastModifiedBy>[^<]*</cp:lastModifiedBy>', '<cp:lastModifiedBy></cp:lastModifiedBy>', s)
        s = re.sub(r'<dc:title>[^<]*</dc:title>', '<dc:title></dc:title>', s)
        open(f, 'w', encoding='utf-8').write(s)
    ap = d + '/docProps/app.xml'
    if os.path.exists(ap):
        s = open(ap, encoding='utf-8').read(); s = re.sub(r'<Company>[^<]*</Company>', '<Company></Company>', s); open(ap, 'w', encoding='utf-8').write(s)
def drop_people(d):
    """Remove the tracked-change author list (reviewer names) left by the supervisor's edits."""
    if os.path.exists(d + '/word/people.xml'):
        os.remove(d + '/word/people.xml')
        r = d + '/word/_rels/document.xml.rels'; s = open(r, encoding='utf-8').read()
        s = re.sub(r'<Relationship [^>]*Target="people.xml"/>', '', s); open(r, 'w', encoding='utf-8').write(s)
        c = d + '/[Content_Types].xml'; s = open(c, encoding='utf-8').read()
        s = re.sub(r'<Override PartName="/word/people.xml"[^>]*/>', '', s); open(c, 'w', encoding='utf-8').write(s)
def save(t, d, out):
    t.write(d + '/word/document.xml', xml_declaration=True, encoding='UTF-8', standalone=True)
    scrub_core(d); subprocess.run(['bash', S + '/pack.sh', d, out], check=True)

os.makedirs(OUT, exist_ok=True)

# ---------------- 01 Title page (authors' template; Ha Hong Hanh moved to third position)
t, body = load(U + 'e254d304-01_Title_Page.docx', S + '/sub_tp'); P = paras(body)
set_text(P[0], TITLE); set_text(P[1], AUTH)
set_text(P[2], '^{a} ' + APD); set_text(P[3], '^{b} ' + NEU); set_text(P[4], CORR)
for i, s in enumerate(DETAILS): set_text(P[6 + i], s)
jel_h = clone_after(P[9], 'JEL Classification', template=P[10]); jel = clone_after(jel_h, 'C58, G11, G12', template=P[11])
kw_h = clone_after(jel, 'Keywords', template=P[10]); clone_after(kw_h, 'constituent overlap, DCCA, Forbes–Rigobon adjustment, multiscale correlation, portfolio risk, Vietnam', template=P[11])
set_text(P[12], 'Conflict of interest'); set_text(P[13], COI)
set_text(P[15], FUND)
set_text(P[16], 'Author contributions (CRediT)'); set_text(P[17], CREDIT)
set_text(P[19], DATA)
code_h = clone_after(P[19], 'Code availability', template=P[18]); clone_after(code_h, CODE, template=P[19])
save(t, S + '/sub_tp', OUT + '/01_Title_Page.docx')

# ---------------- 02 Anonymized manuscript (final build, metadata and tracked-change author list scrubbed)
d = S + '/sub_ms'; shutil.rmtree(d, ignore_errors=True); shutil.copytree(S + '/final', d)
drop_people(d); t = etree.parse(d + '/word/document.xml')
body_txt = etree.tostring(t).decode()
for name in ['Nguyen', 'Hanh', 'Hạnh', 'Binh', 'Diep', 'Trung', 'neu.edu', 'apd.edu']:
    assert name not in body_txt, ('identifying text in blinded manuscript', name)
save(t, d, OUT + '/02_Manuscript_Anonymized.docx')

# ---------------- 07 Manuscript with author details (same text + author block + real funding/contributions)
d7 = S + '/sub_ms7'; shutil.rmtree(d7, ignore_errors=True); shutil.copytree(d, d7)
t7 = etree.parse(d7 + '/word/document.xml'); b7 = t7.getroot().find(W + 'body'); P7 = paras(b7)
title = P7[0]; tmpl = [p for p in P7 if text_of(p).startswith('Conflict of interest')][0]
def plain_after(anchor, markup):
    n = copy.deepcopy(tmpl); set_text(n, markup); ppr = n.find(W + 'pPr')
    jc = etree.SubElement(ppr, W + 'jc') if ppr.find(W + 'jc') is None else ppr.find(W + 'jc'); jc.set(W + 'val', 'center')
    anchor.addnext(n); return n
a1 = plain_after(title, AUTH); a2 = plain_after(a1, '^{a} ' + APD); a3 = plain_after(a2, '^{b} ' + NEU)
a4 = plain_after(a3, CORR); a4.find(W + 'pPr').find(W + 'jc').set(W + 'val', 'left')
fund = [p for p in P7 if text_of(p).startswith('Funding')][0]; set_text(fund, FUND, bold_lead='Funding ')
coi = [p for p in P7 if text_of(p).startswith('Conflict of interest')][0]
n = copy.deepcopy(coi); set_text(n, CREDIT, bold_lead='Author contributions '); coi.addnext(n)
save(t7, d7, OUT + '/07_Manuscript_with_Author_Details.docx')

# ---------------- 04 Declaration of competing interest
t, body = load(U + 'e254d304-01_Title_Page.docx', S + '/sub_coi'); P = paras(body)
set_text(P[0], 'Declaration of competing interest'); set_text(P[1], 'Manuscript: “' + TITLE + '”')
set_text(P[2], 'Journal: Asia-Pacific Financial Markets'); set_text(P[3], COI + ' No author has a financial relationship with an organization that sponsored the research; the research received no specific funding.')
set_text(P[4], 'Authors: Nguyen Thanh Binh, Nguyen Van Trung (corresponding author), Ha Hong Hanh, Nguyen Bach Diep.')
set_text(P[5], 'Date: 24 September 2026')
for p in P[6:]:
    if p.getparent() is body and p.find('.//' + W + 'sectPr') is None: body.remove(p)
save(t, S + '/sub_coi', OUT + '/04_Declaration_of_Competing_Interest.docx')

# ---------------- 06 Cover letter (authors' template, rewritten for APFM and this manuscript)
t, body = load(U + '9c18859e-06_Cover_Letter.docx', S + '/sub_cl'); P = paras(body)
set_text(P[2], 'Asia-Pacific Financial Markets')
set_text(P[3], 'Submission of manuscript: “' + TITLE + '”', bold_lead=None)
for r in P[3].iter(W + 'r'):
    rp = r.find(W + 'rPr') if r.find(W + 'rPr') is not None else etree.SubElement(r, W + 'rPr'); r.remove(rp); r.insert(0, rp)
    if rp.find(W + 'b') is None: etree.SubElement(rp, W + 'b')
set_text(P[5], 'We submit the enclosed manuscript for consideration as an original research article in Asia-Pacific Financial Markets.')
set_text(P[6], 'Vietnam’s main equity benchmarks are nested: the large-cap VN30 is contained in the VN100, which is contained in the broad VNINDEX. '
         'Their headline correlations are 0.975–0.980 at every frequency from 30-minute to daily data, and risk models that use these figures treat constituent overlap as economic co-movement. '
         'Using detrended cross-correlation analysis and its multifractal extension on Ho Chi Minh City Stock Exchange data for 2014–2025, the paper separates the two with a capitalization-weighted mid-cap proxy.')
set_text(P[7], 'Removing the overlap lowers the correlation with large caps by 0.086–0.096, with block-bootstrap intervals that exclude zero, although the purged correlation stays near 0.88. '
         'After the Forbes–Rigobon volatility adjustment there is no evidence that cross-tier correlation rises structurally in crises, and a static correlation misstates the variance of a mid-cap factor exposure by 2.2–9.4% in calm regimes and by about 2% in turbulent regimes.')
set_text(P[8], 'The paper falls within the journal’s scope of financial engineering as it defines the term: it is an empirical study of Asia-Pacific market data that combines financial time series methods (multiscale and multifractal cross-correlation analysis of intraday and daily returns) with portfolio analysis and risk management (the variance cost of static correlations for multi-capitalization allocations). It reports its null results (no horizon dependence for the purged pair; no evidence of contagion) and its limitations (a single capitalization-weight snapshot; no exchange-published mid-cap series at all frequencies) alongside the main findings. The R code that reproduces every table and figure is supplied as Online Resource 1.')
set_text(P[9], 'The manuscript has not been published elsewhere and is not under consideration by another journal. All authors have approved the manuscript and agree with its submission to Asia-Pacific Financial Markets. '
         'The authors used a generative AI assistant as described in the declaration placed before the reference list; they reviewed and verified all content and take full responsibility for it. '
         'The manuscript is prepared for double-blind review: author names, affiliations, contributions and funding information are on the separate title page.')
save(t, S + '/sub_cl', OUT + '/06_Cover_Letter.docx')

# ---------------- 08 Highlights (optional for APFM; each bullet at most 85 characters)
HL = ['Shared constituents inflate nested Vietnamese index correlations to 0.975–0.980',
      'A cap-weighted mid-cap proxy lowers the correlation with large caps by about 0.09',
      'Horizon dependence appears only for broad-market pairs at 30-minute and 1-hour data',
      'Volatility-adjusted crisis correlations give no evidence of contagion',
      'Static correlations misstate mid-cap factor variance by 2.2–9.4% in calm regimes']
assert all(len(h) <= 85 for h in HL), [len(h) for h in HL]
t, body = load(U + 'e254d304-01_Title_Page.docx', S + '/sub_hl'); P = paras(body)
set_text(P[0], 'Highlights')
for i, h in enumerate(HL): set_text(P[1 + i], '• ' + h)
for p in P[1 + len(HL):]:
    if p.find('.//' + W + 'sectPr') is None: body.remove(p)
save(t, S + '/sub_hl', OUT + '/08_Highlights.docx')
print('built', sorted(os.listdir(OUT)))
