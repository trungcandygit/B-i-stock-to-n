"""Build the round-2 manuscript (anonymized and with author details) from r2_text / r2_lit via pandoc.

Usage (from project_R/docx_build):  python3 build_r2.py
Outputs: r2/manuscript_anonymized.docx, r2/manuscript_with_authors.docx, r2/manuscript.md
Styles come from the authors' uploaded manuscript (reference doc); numbers come from ../outputs (R)."""
import copy, os, re, shutil, subprocess, sys, zipfile
from lxml import etree
S = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, S)
from lib_docx import W, M
import r2_text as TX
from r2_lit import REFERENCES

REF_DOC = os.path.join(S, 'r2', 'reference.docx')     # copy of the authors' uploaded 02_Manuscript_Anonymized.docx
FIG = os.path.join(os.environ.get('R2_OUT') or os.path.join(S, '..', 'outputs'), 'figures')
FIGMAP = {'fig1': 'fig1_volatility_regimes.png', 'fig2': 'fig2_dcca_curves.png',
          'fig4': 'fig4_overlap_decomposition.png', 'fig3': 'fig3_mfdcca.png', 'fig5': 'fig5_floor_contour.png'}
OUTD = os.path.join(S, 'r2')

AUTHORS = 'Nguyen Thanh Binh^a^, Nguyen Van Trung^a,\\*^, Ha Hong Hanh^b^, Nguyen Bach Diep^a^'
AFFIL = ['^a^ Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam',
         '^b^ School of Accounting and Auditing, National Economics University, Hanoi, Vietnam',
         '\\* Corresponding author: Nguyen Van Trung, Academy of Policy and Development, Hanoi, Vietnam. '
         'Email: 15233582\\@st.neu.edu.vn. Tel: +84 355 347 831.']
CREDIT = ('Nguyen Thanh Binh: Conceptualization, Supervision, Validation, Writing – review & editing. Nguyen Van Trung: '
          'Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Software, Visualization, Writing – '
          'original draft, Writing – review & editing. Ha Hong Hanh: Validation, Writing – review & editing. Nguyen Bach Diep: '
          'Methodology, Formal analysis, Writing – original draft.')
AI_USE = ('During the preparation of this work the authors used Claude (Anthropic) for language editing, reference searching '
          'and verification, translation of the analysis code into R and drafting of revisions, and Gemini (Google) to improve '
          'the language and readability of the manuscript. After using these tools, the authors reviewed and edited the content '
          'as needed and take full responsibility for the content of the publication.')


def inline(s):
    """Markdown inline: escape pipes/asterisk runs, convert _sub / ^{sup} tokens."""
    s = s.replace('run_all.R', 'RUNALLR').replace('|', '\\|').replace('***', '\\*\\*\\*')
    s = re.sub(r'\^\{([^}\s]+)\}', r'^\1^', s)
    s = re.sub(r'(?<=[A-Za-zρσεκλα²F\)])_\{([^}]+)\}', lambda m: '~' + m.group(1).replace(' ', '\\ ') + '~', s)
    s = re.sub(r'(?<=[A-Za-zρσεκλα²])_([A-Za-z0-9α-ω]+(?:,[A-Za-z0-9α-ω]+)*)', r'~\1~', s)
    return s.replace('RUNALLR', 'run\\_all.R')


def para(style, text):
    return f'::: {{custom-style="{style}"}}\n{text}\n:::\n'


def table_md(caption, header, body, note):
    out = [para('tablecaption', '**' + ' '.join(caption.split(' ')[:2]) + '** ' + inline(' '.join(caption.split(' ')[2:])))]
    ncol = len(header)
    out.append('| ' + ' | '.join(inline(h) for h in header) + ' |')
    out.append('|' + '|'.join(['---'] * ncol) + '|')
    for r in body:
        out.append('| ' + ' | '.join(inline(str(c)) for c in r) + ' |')
    out.append('')
    out.append(para('Compact', 'Notes: ' + inline(note)))
    return '\n'.join(out)


def figure_md(key, caption, note):
    path = os.path.join(FIG, FIGMAP[key])
    num = ' '.join(caption.split(' ')[:2])
    return (f'![]({path}){{width=6.3in}}\n\n' + para('figurecaption', f'**{num}** ' + inline(' '.join(caption.split(' ')[2:])))
            + para('Compact', 'Notes: ' + inline(note)))


def render(blocks):
    out = []
    for kind, val in blocks:
        if kind == 'h1':
            out.append(para('heading1', val))
        elif kind == 'h2':
            out.append(para('heading2', val))
        elif kind == 'p1a':
            out.append(para('p1a', inline(val)))
        elif kind == 'p':
            out.append(inline(val) + '\n')
        elif kind == 'eq':
            out.append(f'$$\n{val}\n$$\n')
        elif kind == 'table':
            out.append(table_md(*val))
        elif kind == 'fig':
            out.append(figure_md(*val))
    return '\n'.join(out)


def manuscript(anonymized):
    md = [para('Title', TX.TITLE)]
    if not anonymized:
        md.append(para('p1a', AUTHORS))
        md += [para('Compact', a) for a in AFFIL]
    md.append(para('abstract', '**Abstract** ' + inline(TX.ABSTRACT)))
    md.append(para('keywords', '**Keywords** ' + TX.KEYWORDS))
    md.append(para('keywords', '**JEL Classification** ' + TX.JEL))
    md.append(render(TX.body()))
    decl = [('Ethical standards', 'This study uses only publicly available historical index price data from the Ho Chi Minh City '
             'Stock Exchange; it involves no human participants or personal data, therefore required no ethical approval, and '
             'complies with the current laws of Vietnam.'),
            ('Data availability', 'The index price data were obtained from TradingView (exchange: HOSE) and are subject to the '
             'vendor’s terms of use; the merged dataset is available from the corresponding author upon reasonable request.'),
            ('Code availability', 'The R code that reproduces every table and figure, with a map from each reported number to its '
             'output file, is provided as Online Resource 1 and will be deposited in a public repository upon acceptance. '
             'Supplementary tables and figures are provided as Online Resource 2.'),
            ('Funding', 'Funding information is provided on the separate title page in accordance with the journal’s double-blind '
             'review policy.' if anonymized else 'This research did not receive any specific grant from funding agencies in the '
             'public, commercial, or not-for-profit sectors.'),
            ('Conflict of interest', 'The authors declare that they have no conflict of interest.')]
    if not anonymized:
        decl.append(('Author contributions', CREDIT))
    decl.append(('Declaration of generative AI use', AI_USE))
    md += [para('p1a', f'**{k}** {v}') for k, v in decl]
    md.append(para('heading1', 'References'))
    md += [para('referenceitem', r.replace('*', '\\*')) for r in REFERENCES]
    return '\n'.join(md)


# ---------------------------------------------------------------- post-processing
def text_has_words(p):
    return bool(''.join(t.text or '' for t in p.iter(W + 't') if not any(a.tag == M + 'oMath' for a in t.iterancestors())).strip())


def post(docx_path):
    tmp = docx_path + '.d'
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    with zipfile.ZipFile(docx_path) as z:
        z.extractall(tmp)
    f = os.path.join(tmp, 'word', 'document.xml')
    t = etree.parse(f); body = t.getroot().find(W + 'body')
    for tbl in body.iter(W + 'tbl'):
        tp = tbl.find(W + 'tblPr')
        st = tp.find(W + 'tblStyle')
        if st is None:
            st = etree.SubElement(tp, W + 'tblStyle')
        st.set(W + 'val', 'TableGrid')
        # panel label rows (text in the first cell only) span the full table width
        for tr in tbl.findall(W + 'tr'):
            tcs = tr.findall(W + 'tc')
            if len(tcs) > 1 and text_has_words(tcs[0]) and not any(text_has_words(c) for c in tcs[1:]):
                for c in tcs[1:]:
                    tr.remove(c)
                tcp = tcs[0].find(W + 'tcPr')
                if tcp is None:
                    tcp = etree.Element(W + 'tcPr'); tcs[0].insert(0, tcp)
                for e in tcp.findall(W + 'tcW'):
                    tcp.remove(e)
                gs = etree.SubElement(tcp, W + 'gridSpan'); gs.set(W + 'val', str(len(tcs)))
        # column widths from content: never narrower than the longest word, extra width shared by text length
        grid = tbl.find(W + 'tblGrid'); cols = grid.findall(W + 'gridCol') if grid is not None else []
        nc = len(cols)
        if nc > 1:
            CH, PAD, TOT = 104, 230, 9360
            lw, lt = [0] * nc, [0] * nc
            for tr in tbl.findall(W + 'tr'):
                tcs = tr.findall(W + 'tc')
                if len(tcs) != nc:
                    continue
                for j, c in enumerate(tcs):
                    s = ''.join(x.text or '' for x in c.iter(W + 't'))
                    lw[j] = max([lw[j]] + [len(w) for w in re.split(r'[\s\-–/]+', s) if w])
                    lt[j] = max(lt[j], len(s))
            if sum(l * CH + PAD for l in lw) > TOT:      # wide table: 9 pt text so that no word is split
                CH = int(CH * 0.98)
                for e in tbl.iter(W + 'sz', W + 'szCs'):
                    e.set(W + 'val', '18')
            mn = [l * CH + PAD for l in lw]; mx = [max(a, l * CH + PAD) for a, l in zip(mn, lt)]
            if sum(mx) <= TOT:
                wd = [m * TOT / sum(mx) for m in mx]
            elif sum(mn) >= TOT:
                wd = [m * TOT / sum(mn) for m in mn]
            else:
                ex = [b - a for a, b in zip(mn, mx)]
                wd = [a + e * (TOT - sum(mn)) / sum(ex) for a, e in zip(mn, ex)]
            wd = [int(round(x)) for x in wd]
            for col, x in zip(cols, wd):
                col.set(W + 'w', str(x))
            for tr in tbl.findall(W + 'tr'):
                j = 0
                for c in tr.findall(W + 'tc'):
                    tcp = c.find(W + 'tcPr')
                    if tcp is None:
                        tcp = etree.Element(W + 'tcPr'); c.insert(0, tcp)
                    g = tcp.find(W + 'gridSpan'); span = int(g.get(W + 'val')) if g is not None else 1
                    for e in tcp.findall(W + 'tcW'):
                        tcp.remove(e)
                    cw = etree.Element(W + 'tcW'); cw.set(W + 'w', str(sum(wd[j:j + span]))); cw.set(W + 'type', 'dxa')
                    tcp.insert(0, cw); j += span
        for p in tbl.iter(W + 'p'):
            pp = p.find(W + 'pPr')
            if pp is None:
                pp = etree.Element(W + 'pPr'); p.insert(0, pp)
            for e in pp.findall(W + 'pStyle'):
                pp.remove(e)
            sp = etree.Element(W + 'spacing'); sp.set(W + 'before', '0'); sp.set(W + 'after', '0'); sp.set(W + 'line', '240'); sp.set(W + 'lineRule', 'auto')
            for e in pp.findall(W + 'spacing'):
                pp.remove(e)
            pp.insert(0, sp)
            for r in p.iter(W + 'r'):
                rp = r.find(W + 'rPr')
                if rp is None:
                    rp = etree.Element(W + 'rPr'); r.insert(0, rp)
                for tag in ('sz', 'szCs'):
                    e = rp.find(W + tag)
                    if e is None:
                        e = etree.SubElement(rp, W + tag)
                    e.set(W + 'val', '20')
    def set_sz(p, val, bold=None, font=None):
        for r in p.iter(W + 'r'):
            if any(a.tag == M + 'oMath' for a in r.iterancestors()):
                continue
            rp = r.find(W + 'rPr')
            if rp is None:
                rp = etree.Element(W + 'rPr'); r.insert(0, rp)
            if font:
                for e in rp.findall(W + 'rFonts'):
                    rp.remove(e)
                fe = etree.Element(W + 'rFonts')
                for a in ('ascii', 'hAnsi', 'cs', 'eastAsia'):
                    fe.set(W + a, font)
                rp.insert(0, fe)
            if bold:
                if rp.find(W + 'b') is None:
                    rp.insert(1 if font else 0, etree.Element(W + 'b'))
            for tag in ('sz', 'szCs'):
                e = rp.find(W + tag)
                if e is None:
                    e = etree.SubElement(rp, W + tag)
                e.set(W + 'val', val)

    def ppr(p):
        pp = p.find(W + 'pPr')
        if pp is None:
            pp = etree.Element(W + 'pPr'); p.insert(0, pp)
        return pp

    for p in body.iter(W + 'p'):
        if any(a.tag == W + 'tbl' for a in p.iterancestors()):
            continue
        ps = p.find(W + 'pPr/' + W + 'pStyle'); sv = ps.get(W + 'val') if ps is not None else ''
        if sv in ('heading1', 'heading20', 'heading30'):
            pp = ppr(p)
            for e in pp.findall(W + 'numPr'):
                pp.remove(e)
            npr = etree.Element(W + 'numPr'); il = etree.SubElement(npr, W + 'ilvl'); il.set(W + 'val', '0')
            ni = etree.SubElement(npr, W + 'numId'); ni.set(W + 'val', '0')
            pp.insert(1, npr)
            set_sz(p, '24', bold=True, font='Times New Roman')
        elif sv in ('p1a', 'BodyText', 'FirstParagraph', ''):
            pp = ppr(p)
            for e in pp.findall(W + 'spacing'):
                pp.remove(e)
            sp = etree.Element(W + 'spacing'); sp.set(W + 'before', '0'); sp.set(W + 'after', '120'); sp.set(W + 'line', '300'); sp.set(W + 'lineRule', 'auto')
            pp.insert(1 if pp.find(W + 'pStyle') is not None else 0, sp)
            if p.find('.//' + M + 'oMath') is None or text_has_words(p):
                jc = pp.find(W + 'jc')
                if jc is None:
                    jc = etree.SubElement(pp, W + 'jc')
                jc.set(W + 'val', 'both')
            set_sz(p, '24', font='Times New Roman')
        elif sv == 'Title':
            set_sz(p, '32', bold=True, font='Times New Roman')
        elif sv in ('abstract0', 'keywords', 'referenceitem'):
            set_sz(p, '22', font='Times New Roman')
    # note paragraphs (Compact) at 10 pt
    for p in body.iter(W + 'p'):
        ps = p.find(W + 'pPr/' + W + 'pStyle')
        if ps is not None and ps.get(W + 'val') == 'Compact' and not any(a.tag == W + 'tbl' for a in p.iterancestors()):
            for r in p.iter(W + 'r'):
                rp = r.find(W + 'rPr')
                if rp is None:
                    rp = etree.Element(W + 'rPr'); r.insert(0, rp)
                for tag in ('sz', 'szCs'):
                    e = rp.find(W + tag)
                    if e is None:
                        e = etree.SubElement(rp, W + tag)
                    e.set(W + 'val', '20')
    t.write(f, xml_declaration=True, encoding='UTF-8', standalone=True)
    os.remove(docx_path)
    subprocess.run(['bash', os.path.join(S, 'pack.sh'), tmp, docx_path], check=True, stdout=subprocess.DEVNULL)
    shutil.rmtree(tmp)


def supplement_md():
    md = [para('Title', 'Supplementary Material (Online Resource 2): ' + TX.TITLE)]
    md.append(render(TX.supplement()))
    return '\n'.join(md)


def build():
    os.makedirs(OUTD, exist_ok=True)
    mdp = os.path.join(OUTD, 'supplementary_material.md'); open(mdp, 'w', encoding='utf-8').write(supplement_md())
    out = os.path.join(OUTD, 'supplementary_material.docx')
    subprocess.run(['pandoc', mdp, '-f', 'markdown+subscript+superscript+tex_math_dollars+pipe_tables+fenced_divs+link_attributes',
                    '-t', 'docx', '--reference-doc', REF_DOC, '-o', out], check=True)
    post(out); print('built', out)
    for anon, name in ((True, 'manuscript_anonymized'), (False, 'manuscript_with_authors')):
        md = manuscript(anon)
        mdp = os.path.join(OUTD, name + '.md')
        open(mdp, 'w', encoding='utf-8').write(md)
        out = os.path.join(OUTD, name + '.docx')
        subprocess.run(['pandoc', mdp, '-f', 'markdown+subscript+superscript+tex_math_dollars+pipe_tables+fenced_divs+link_attributes',
                        '-t', 'docx', '--reference-doc', REF_DOC, '-o', out], check=True)
        post(out)
        print('built', out)


if __name__ == '__main__':
    build()
