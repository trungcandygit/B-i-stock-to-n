"""Language-round gate: the multiset of numeric tokens, citations, table/figure/equation references and
hypothesis outcomes in the rendered manuscript and supplement must be identical before and after a language round.
Usage: python3 numgate.py snapshot <dir>   |   python3 numgate.py compare <dir>"""
import os, re, sys, json, collections
S = os.path.dirname(os.path.abspath(__file__))
FILES = ['r2/manuscript_anonymized.md', 'r2/supplementary_material.md']
PAT = {'number': r'(?<![A-Za-z])[−-]?\d[\d,]*\.?\d*(?:\s?×\s?10[⁻⁰-⁹]+)?%?',
       'citation': r'[A-Z][A-Za-zÀ-ž’\'-]+(?: et al\.| and [A-Z][A-Za-zÀ-ž’\'-]+)? \(?\d{4}\)?',
       'xref': r'(?:Tables?|Figs?\.|Eqs?\.|Box|Section|Sections) S?\(?\d+\)?',
       'outcome': r'\b(?:Supported|Not supported|not supported|supported)\b'}


def grab():
    out = {}
    for fn in FILES:
        t = open(os.path.join(S, fn), encoding='utf-8').read()
        t = t.split('References')[0] if 'manuscript' in fn else t
        for k, p in PAT.items():
            out.setdefault(k, collections.Counter()).update(re.findall(p, t))
    return {k: dict(v) for k, v in out.items()}


mode, d = sys.argv[1], sys.argv[2]
if mode == 'snapshot':
    os.makedirs(d, exist_ok=True); json.dump(grab(), open(os.path.join(d, 'gate.json'), 'w'), ensure_ascii=False)
    print('snapshot saved')
else:
    old = json.load(open(os.path.join(d, 'gate.json'))); new = grab(); bad = 0
    for k in PAT:
        o, n = collections.Counter(old[k]), collections.Counter(new[k])
        lost, gained = o - n, n - o
        if k == 'outcome':
            lost = collections.Counter({x: c for x, c in lost.items()}); gained = collections.Counter({x: c for x, c in gained.items()})
        if lost or gained:
            bad += 1; print(f'[{k}] lost: {dict(lost)}\n[{k}] gained: {dict(gained)}')
    print('GATE PASS' if not bad else 'GATE: differences listed above (review each; numbers must not change)')
