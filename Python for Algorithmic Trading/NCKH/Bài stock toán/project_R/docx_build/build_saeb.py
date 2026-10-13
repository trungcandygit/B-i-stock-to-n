"""Scientific Annals of Economics and Business (SAEB) package: blinded manuscript (.docx), separate title page (author,
affiliation, e-mail, Acknowledgments with the AI statement, conflict of interest, funding), supplementary material.

SAEB rules applied (author guidelines, 2026-10): A4, Times New Roman 10 pt, justified, 0.75 cm indent, single spacing;
abstract <= 250 words; at most 5 keywords; JEL codes with two digits; endnotes, not footnotes; in-text citations
"(Levine, 2007)", "Eichengreen and Hausmann (1999)", "(Frankel et al., 2001)"; APA reference list; <= 30 pages.
Single author at the author's request: Nguyen Van Trung, National Economics University, Vietnam.

Usage (from project_R/docx_build):  python3 build_saeb.py
Outputs: ../../submission/SAEB_submission/"""
import os, re, shutil, subprocess, sys, zipfile
from lxml import etree
S = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, S)
import build_r2 as B
import r2_text as TX
from r2_lit import REFERENCES
from lib_docx import W

OUT = os.path.join(S, '..', '..', 'submission', 'SAEB_submission')
FMT = 'markdown+subscript+superscript+tex_math_dollars+pipe_tables+fenced_divs+link_attributes'
P = B.para

AUTHOR = 'Nguyen Van Trung'
AFFIL = 'National Economics University, Hanoi, Vietnam'
EMAIL = r'kontrungcany\@gmail.com'
KEYWORDS = 'constituent overlap; detrended cross-correlation; part–whole correlation; contagion; Vietnam'
JEL = 'C14, C58, G11, G15'
AI_USE = ('Use of AI tools: during the preparation of this work the author used Claude (Anthropic) [add model version] for '
          'language editing, reference searching and verification, translation of the analysis code into R and drafting of '
          'revised passages, and Gemini (Google) [add model version] to improve the language and readability of the '
          'manuscript. The research design, data, analysis and conclusions are the author’s own. The author reviewed and '
          'edited all AI-assisted content and takes full responsibility for the publication.')
DECL = [('Acknowledgments', AI_USE),
        ('Conflict of interest', 'The author declares no conflict of interest.'),
        ('Funding', 'This research did not receive any specific grant from funding agencies in the public, commercial, or '
                    'not-for-profit sectors.'),
        ('Data availability', 'The index price data were obtained from TradingView (exchange: HOSE) and are subject to the '
                              'vendor’s terms of use; the merged dataset is available from the author upon reasonable '
                              'request. The R code that reproduces every table and figure is available from the author and '
                              'will be deposited in a public repository upon acceptance.'),
        ('Ethics', 'The study uses only publicly available historical index prices and involves no human participants.')]

MONTHS = 'January|February|March|April|May|June|July|August|September|October|November|December'
# A capitalised word (or "al.") followed by a year inside parentheses is a parenthetical citation: insert the comma.
CIT = re.compile(r'(?<![\w])((?:[A-Z][A-Za-zÀ-ž’\'\-]*|al\.)) ((?:1[89]|20)\d\d[a-z]?)(?=[);,])')


def apa_intext(md):
    def fix(m):
        return m.group(0) if re.fullmatch(MONTHS, m.group(1)) else f'{m.group(1)}, {m.group(2)}'
    return CIT.sub(fix, md)


def manuscript_md():
    body = B.render(TX.body()).replace('Further checks are in Online Resource 2.',
                                       'Further checks are in the Supplementary Material.')
    md = [P('Title', TX.TITLE), P('abstract', '**Abstract** ' + B.inline(TX.ABSTRACT)),
          P('keywords', '**Keywords:** ' + KEYWORDS), P('keywords', '**JEL classification:** ' + JEL),
          apa_intext(body), P('heading1', 'References')]
    md += [P('referenceitem', r.replace('*', '\\*')) for r in REFERENCES]
    return '\n'.join(md)


def title_page_md():
    md = [P('Title', TX.TITLE), P('p1a', f'**{AUTHOR}**'), P('Compact', AFFIL), P('Compact', f'E-mail: {EMAIL}')]
    for k, v in DECL:
        md += [P('heading1', k), P('p1a', v)]
    return '\n'.join(md)


def supplement_md():
    blocks = TX.supplement()
    blocks[0] = ('h1', 'Supplementary Material')
    blocks[1] = ('p1a', 'This document accompanies the article and reports the robustness checks and the tables cited in the '
                 'main text as Tables S1–S17 and Fig. S1. All numbers come from the R outputs of the replication code.')
    return '\n'.join([P('Title', 'Supplementary Material: ' + TX.TITLE), apa_intext(B.render(blocks))])


BODY_STYLES = {'Normal', 'BodyText', 'FirstParagraph', 'p', 'p1a', 'Compact', 'abstract0', 'keywords', 'referenceitem'}
INDENT = {'p', 'p1a', 'BodyText', 'FirstParagraph'}


def saeb_styles(docx_path):
    """Times New Roman 10 pt, justified, single spacing, 0.75 cm first-line indent, A4 page."""
    tmp = docx_path + '.s'
    shutil.rmtree(tmp, ignore_errors=True)
    with zipfile.ZipFile(docx_path) as z:
        z.extractall(tmp)
    sf = os.path.join(tmp, 'word', 'styles.xml'); st = etree.parse(sf); root = st.getroot()

    def font(rpr):
        for e in rpr.findall(W + 'rFonts'):
            rpr.remove(e)
        f = etree.Element(W + 'rFonts')
        for a in ('ascii', 'hAnsi', 'cs', 'eastAsia'):
            f.set(W + a, 'Times New Roman')
        rpr.insert(0, f)

    def size(rpr, v):
        for tag in ('sz', 'szCs'):
            for e in rpr.findall(W + tag):
                rpr.remove(e)
            e = etree.SubElement(rpr, W + tag); e.set(W + 'val', str(v))

    dd = root.find(W + 'docDefaults').find(W + 'rPrDefault').find(W + 'rPr')
    font(dd); size(dd, 20)
    for s in root.iter(W + 'style'):
        rpr = s.find(W + 'rPr')
        if rpr is None:
            rpr = etree.SubElement(s, W + 'rPr')
        font(rpr)
        sid = s.get(W + 'styleId') or ''
        if s.get(W + 'type') != 'paragraph':
            continue
        if sid != 'Title':
            size(rpr, 20)
        if sid in BODY_STYLES or sid.lower().startswith('heading'):
            ppr = s.find(W + 'pPr')
            if ppr is None:
                ppr = etree.Element(W + 'pPr'); s.insert(min(len(s), 3), ppr)
            for tag in ('spacing', 'ind', 'jc'):
                for e in ppr.findall(W + tag):
                    ppr.remove(e)
            sp = etree.SubElement(ppr, W + 'spacing'); sp.set(W + 'line', '240'); sp.set(W + 'lineRule', 'auto')
            sp.set(W + 'before', '120' if sid.lower().startswith('heading') else '0')
            sp.set(W + 'after', '60' if sid.lower().startswith('heading') else '0')
            if sid in INDENT:
                ind = etree.SubElement(ppr, W + 'ind'); ind.set(W + 'firstLine', '425')
            if sid in BODY_STYLES - {'Compact'}:
                jc = etree.SubElement(ppr, W + 'jc'); jc.set(W + 'val', 'both')
    st.write(sf, xml_declaration=True, encoding='UTF-8', standalone=True)
    df = os.path.join(tmp, 'word', 'document.xml'); dt = etree.parse(df)
    for pg in dt.getroot().iter(W + 'pgSz'):
        pg.set(W + 'w', '11906'); pg.set(W + 'h', '16838')
    dt.write(df, xml_declaration=True, encoding='UTF-8', standalone=True)
    os.remove(docx_path)
    with zipfile.ZipFile(docx_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for d, _, fs in os.walk(tmp):
            for f in fs:
                p = os.path.join(d, f); z.write(p, os.path.relpath(p, tmp))
    shutil.rmtree(tmp)


def pandoc(md, name, keep_md=False):
    mdp = os.path.join(OUT, name + '.md'); open(mdp, 'w', encoding='utf-8').write(md)
    out = os.path.join(OUT, name + '.docx')
    subprocess.run(['pandoc', mdp, '-f', FMT, '-t', 'docx', '--reference-doc', B.REF_DOC, '-o', out], check=True)
    B.post(out)
    saeb_styles(out)
    if not keep_md:
        os.remove(mdp)
    print('built', out)


def build():
    os.makedirs(OUT, exist_ok=True)
    pandoc(title_page_md(), '01_Title_page')
    pandoc(manuscript_md(), '02_Manuscript_blinded', keep_md=True)
    pandoc(supplement_md(), '03_Supplementary_material')


if __name__ == '__main__':
    build()
