"""Round-1 review revision (academic-paper revision mode) applied on top of stage2 output.
Anchors paragraphs by their text so it is robust to earlier index shifts. Numbers come from R outputs."""
import copy, csv, os, re, sys
from lxml import etree
sys.path.insert(0, os.path.dirname(__file__))
from lib_docx import *

S = os.path.dirname(os.path.abspath(__file__))
OUT = '/home/user/B-i-stock-to-n/Python for Algorithmic Trading/NCKH/Bài stock toán/project_R/outputs'
dst = S + '/final'
tree = etree.parse(dst + '/word/document.xml'); root = tree.getroot(); body = root.find(W + 'body')
TOP = lambda: [c for c in body if c.tag == W + 'p']
TBL = lambda: [c for c in body if c.tag == W + 'tbl']

def find(prefix, nth=0):
    hits = [p for p in TOP() if text_of(p).strip().startswith(prefix)]
    assert len(hits) > nth, ('not found', prefix)
    return hits[nth]
def rd(f): return list(csv.DictReader(open(os.path.join(OUT, f))))
def f(x, d): return f'{float(x):.{d}f}'.replace('-', '−')
def star(p):
    p = float(p); return '***' if p < .01 else '**' if p < .05 else '*' if p < .10 else ''

BT = {(r['timeframe'], r['pair'], r['stat']): r for r in rd('R2_bootstrap_dcca.csv')}
FR = {(r['panel'], r['pair']): r for r in rd('R3_forbes_rigobon_pearson_bootstrap.csv')}
RE = {(r['panel'], r['pair'], r['regime']): r for r in rd('R4_portfolio_error_pearson.csv')}
T7 = rd('R5_table7_with_pearson_regimes.csv')
RG = {r['timeframe']: r for r in rd('R6_reliability_garch_t.csv')}
SU = {(r['timeframe'], r['pair']): r for r in rd('R7_mfdcca_shuffle_surrogate.csv')}
TF = ['1D', 'M30', 'H1', 'H4']
def cis(r, d=4): return f"[{f(r['ci_lo'], d)}, {f(r['ci_hi'], d)}]"
def sig(r): return float(r['ci_lo']) > 0 or float(r['ci_hi']) < 0

exec(open(S + '/stage3_text.py').read())

tree.write(dst + '/word/document.xml', xml_declaration=True, encoding='UTF-8', standalone=True)
print('stage3 ok')
