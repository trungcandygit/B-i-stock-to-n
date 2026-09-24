"""Shared loader for post-stage3 text rounds. Edits anchor on paragraph text prefixes."""
import copy, os, re, sys
from lxml import etree
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_docx import *
S = os.path.dirname(os.path.abspath(__file__)); dst = S + '/final'
tree = etree.parse(dst + '/word/document.xml'); root = tree.getroot(); body = root.find(W + 'body')
TOP = lambda: [c for c in body if c.tag == W + 'p']
LOG = []
def find(prefix):
    hits = [p for p in TOP() if text_of(p).strip().startswith(prefix)]
    assert len(hits) == 1, ('anchor', prefix, len(hits))
    return hits[0]
def E(prefix, old, new, why=''):
    p = find(prefix)
    nb = lambda x: re.sub(r'(et al\.|Fig\.|Table|Section) (?=[(0-9])', lambda m: m.group(1) + '\xa0', x)
    ok = replace_in(p, old, new) or replace_in(p, nb(old), nb(new))
    assert ok, ('text', prefix, old)
    LOG.append((why, old, new))
def T(prefix, markup, why=''):
    p = find(prefix); assert p.find('.//' + M + 'oMath') is None, ('math in', prefix)
    old = text_of(p); set_text(p, markup); LOG.append((why, old, markup))
def DROP(prefix, why=''):
    p = find(prefix); LOG.append((why, text_of(p), '')); body.remove(p)
def save(logfile):
    tree.write(dst + '/word/document.xml', xml_declaration=True, encoding='UTF-8', standalone=True)
    with open(logfile, 'w') as fh:
        for why, o, n in LOG: fh.write(f'- [{why}] “{o}” → “{n}”\n')
    print('edits', len(LOG))
