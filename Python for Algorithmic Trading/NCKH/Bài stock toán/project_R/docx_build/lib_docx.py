"""Small helpers for editing the manuscript's document.xml in place (lxml)."""
import copy, re
from lxml import etree

NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math'}
W = '{%s}' % NS['w']
M = '{%s}' % NS['m']
XMLSPACE = '{http://www.w3.org/XML/1998/namespace}space'

TOKEN = re.compile(r'(〈[^〉]+〉|_\{[^}]*\}|\^\{[^}]*\})')


def text_of(p):
    out = []
    for el in p.iter():
        if el.tag == W + 't' and not any(a.tag == M + 'oMath' for a in el.iterancestors()):
            out.append(el.text or '')
        elif el.tag == M + 'oMath' and not any(a.tag == M + 'oMath' for a in el.iterancestors()):
            out.append(''.join(t.text or '' for t in el.iter(M + 't')))
    return ''.join(out)


def base_rpr(p):
    for r in p.iter(W + 'r'):
        if r.find(W + 't') is not None and not any(a.tag == M + 'oMath' for a in r.iterancestors()):
            rpr = r.find(W + 'rPr')
            if rpr is None:
                return etree.Element(W + 'rPr')
            rpr = copy.deepcopy(rpr)
            for tag in ('vertAlign', 'i', 'iCs', 'b', 'bCs', 'rStyle', 'highlight', 'lang'):
                for e in rpr.findall(W + tag):
                    rpr.remove(e)
            return rpr
    return etree.Element(W + 'rPr')


def _run(text, rpr, italic=False, vert=None, bold=False, highlight=None):
    r = etree.Element(W + 'r')
    rp = copy.deepcopy(rpr)
    if bold:
        etree.SubElement(rp, W + 'b')
    if italic:
        etree.SubElement(rp, W + 'i')
    if highlight:
        e = etree.SubElement(rp, W + 'highlight'); e.set(W + 'val', highlight)
    if vert:
        e = etree.SubElement(rp, W + 'vertAlign'); e.set(W + 'val', vert)
    # schema order inside rPr: rFonts,b,i,...,highlight,...,sz,szCs,...,vertAlign ; sort by a canonical order
    order = ['rStyle', 'rFonts', 'b', 'bCs', 'i', 'iCs', 'caps', 'noProof', 'color', 'spacing', 'sz', 'szCs',
             'highlight', 'u', 'vertAlign', 'lang']
    kids = sorted(list(rp), key=lambda e: order.index(etree.QName(e).localname) if etree.QName(e).localname in order else 99)
    for k in list(rp):
        rp.remove(k)
    for k in kids:
        rp.append(k)
    if len(rp):
        r.append(rp)
    t = etree.SubElement(r, W + 't')
    t.text = text
    t.set(XMLSPACE, 'preserve')
    return r


def markup_runs(markup, rpr, bold_lead=None, highlight=None):
    runs = []
    if bold_lead:
        runs.append(_run(bold_lead, rpr, bold=True))
    for tok in TOKEN.split(markup):
        if not tok:
            continue
        if tok.startswith('〈') and tok.endswith('〉'):
            runs.append(_run(tok[1:-1], rpr, italic=True, highlight=highlight))
        elif tok.startswith('_{'):
            runs.append(_run(tok[2:-1], rpr, vert='subscript', highlight=highlight))
        elif tok.startswith('^{'):
            runs.append(_run(tok[2:-1], rpr, vert='superscript', highlight=highlight))
        else:
            runs.append(_run(tok, rpr, highlight=highlight))
    return runs


def set_text(p, markup, bold_lead=None, highlight=None, keep_tabs=False):
    rpr = base_rpr(p)
    ntabs = 0
    if keep_tabs:
        for el in p.iter():
            if el.tag == W + 'tab' and el.getparent().tag == W + 'r':
                ntabs += 1
            if el.tag == W + 't' and (el.text or '').strip():
                break
    for ch in list(p):
        if ch.tag != W + 'pPr':
            p.remove(ch)
    for _ in range(ntabs):
        r = etree.SubElement(p, W + 'r'); r.append(copy.deepcopy(rpr)); etree.SubElement(r, W + 'tab')
    for r in markup_runs(markup, rpr, bold_lead, highlight):
        p.append(r)
    return p


def clone_after(p, markup, template=None, **kw):
    src = template if template is not None else p
    new = copy.deepcopy(src)
    set_text(new, markup, **kw)
    p.addnext(new)
    return new


def clone_before(p, markup, template=None, **kw):
    src = template if template is not None else p
    new = copy.deepcopy(src)
    set_text(new, markup, **kw)
    p.addprevious(new)
    return new


def replace_in(p, old, new):
    """Replace a substring spanning plain w:t nodes (outside math). Returns True if replaced."""
    nodes = [t for t in p.iter(W + 't') if not any(a.tag == M + 'oMath' for a in t.iterancestors())]
    full = ''.join(n.text or '' for n in nodes)
    i = full.find(old)
    if i < 0:
        return False
    j = i + len(old); pos = 0; placed = False
    for n in nodes:
        s = n.text or ''; a, b = pos, pos + len(s); pos = b
        if b <= i or a >= j:
            continue
        lo, hi = max(i, a) - a, min(j, b) - a
        n.text = s[:lo] + ('' if placed else new) + s[hi:]
        n.set(XMLSPACE, 'preserve'); placed = True
    return True


def replace_math(p, old, new):
    done = False
    for t in p.iter(M + 't'):
        if t.text and old in t.text:
            t.text = t.text.replace(old, new); done = True
    return done


def remove(el):
    el.getparent().remove(el)


def cell(tbl, r, c):
    return tbl.findall(W + 'tr')[r].findall(W + 'tc')[c]


def set_cell(tbl, r, c, markup):
    tc = cell(tbl, r, c)
    ps = tc.findall(W + 'p')
    for extra in ps[1:]:
        tc.remove(extra)
    set_text(ps[0], markup)


def delete_row(tbl, r):
    tbl.remove(tbl.findall(W + 'tr')[r])


def delete_col(tbl, c):
    grid = tbl.find(W + 'tblGrid'); gcols = grid.findall(W + 'gridCol')
    wdel = int(gcols[c].get(W + 'w')); grid.remove(gcols[c])
    rest = grid.findall(W + 'gridCol'); add = wdel // len(rest)
    for g in rest: g.set(W + 'w', str(int(g.get(W + 'w')) + add))
    for tr in tbl.findall(W + 'tr'):
        tcs = tr.findall(W + 'tc')
        if len(tcs) == 1:
            gs = tcs[0].find(W + 'tcPr/' + W + 'gridSpan')
            if gs is not None:
                gs.set(W + 'val', str(int(gs.get(W + 'val')) - 1))
            continue
        tr.remove(tcs[c])
        for tc in tr.findall(W + 'tc'):
            tw = tc.find(W + 'tcPr/' + W + 'tcW')
            if tw is not None and tw.get(W + 'type') == 'dxa':
                tw.set(W + 'w', str(int(tw.get(W + 'w')) + add))
