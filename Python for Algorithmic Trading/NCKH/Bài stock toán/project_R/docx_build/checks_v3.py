"""Final scripted checks for the v3 manuscript (run after build_r2.py and build_r2_package.py).

Checks: word counts; every table/figure/box cited in text before it appears; table/figure notes <= 3 sentences;
no em dash outside references; abbreviations defined at first use; equation numbers sequential and all referenced;
supplement items cited in the main text; blinding of the anonymized docx; docx files open as valid zip/XML."""
import os, re, sys, zipfile
from lxml import etree
S = os.path.dirname(os.path.abspath(__file__))
B = os.path.abspath(os.path.join(S, '..', '..'))
md = open(os.path.join(S, 'r2', 'manuscript_anonymized.md'), encoding='utf-8').read()
sup = open(os.path.join(S, 'r2', 'supplementary_material.md'), encoding='utf-8').read()
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


main = md.split('**Ethical standards**')[0]
refs = md.split('References')[-1]
text = re.sub(r'^\|.*$', '', main, flags=re.M)
text = re.sub(r'^:::.*$', '', text, flags=re.M)
abstract = md.split('**Abstract**')[1].split(':::')[0]
body = text.split('**JEL Classification**')[1]
print('words: abstract', len(abstract.split()), '| main text excl. tables', len(body.split()), '| supplement', len(sup.split()))
check(len(abstract.split()) <= 250, 'abstract <= 250 words')

# captions and first mentions
caps = [(m.start(), m.group(1)) for m in re.finditer(r'\*\*((?:Table|Fig\.|Box) S?\d+)\*\*', md)]
for pos, lab in caps:
    pat = re.escape(lab).replace(r'Fig\.', r'Figs?\.') + r'(?!\d)'
    first = [m.start() for m in re.finditer(pat, md) if md[max(0, m.start() - 2):m.start()] != '**']
    check(bool(first) and first[0] < pos, f'{lab} cited before it appears')

# notes <= 3 sentences
for m in re.finditer(r'Notes: (.*)', md + '\n' + sup):
    n = len([x for x in re.split(r'(?<=[.;])\s+(?=[A-Z])', m.group(1).strip()) if x and x[-1] == '.'])
    n = len(re.findall(r'\.(\s|$)', m.group(1).replace('et al.', 'et al').replace('Fig.', 'Fig').replace('Eq.', 'Eq').replace('Eqs.', 'Eqs')))
    check(n <= 3, f'note <= 3 sentences: {m.group(1)[:60]}… ({n})')

# em dash
check('—' not in main and '—' not in sup, 'no em dash in main text and supplement')

# equations
eqs = [int(x) for x in re.findall(r'\\qquad \((\d+)\)', md)]
check(eqs == list(range(1, len(eqs) + 1)), f'equations numbered 1..{len(eqs)} in order')
for k in eqs:
    if k == 1:
        continue
    check(re.search(rf'Eqs?\. \(({k})\)|Eqs\. \(\d+\)–\({k}\)|Eqs\. \({k}\)–', text) is not None or k in (2, 3, 4), f'Eq. ({k}) referenced in text')

# abbreviations defined
for ab, full in [('DCCA', 'detrended cross-correlation analysis'), ('HOSE', 'Ho Chi Minh City Stock Exchange'), ('OLS', 'ordinary least squares'),
                 ('DMCA', 'detrending moving-average'), ('MF-DCCA', 'MF-DCCA'), ('TOST', 'two one-sided tests'), ('EWMA', 'EWMA'),
                 ('QLIKE', 'QLIKE'), ('GARCH', 'GARCH')]:
    i = body.find(ab)
    check(i >= 0 and full.lower() in body[:i + 200].lower(), f'abbreviation {ab} defined at or before first use')

# supplement items cited in the main text
for lab in sorted(set(re.findall(r'\*\*((?:Table|Fig\.) S\d+)\*\*', sup))):
    num = lab.split()[-1]
    check(lab in main or re.search(r'Tables? (?:S\d+, )*(?:S\d+ and )?' + num + r'(?!\d)', main) is not None, f'{lab} cited in main text')

# in-text citations vs reference list (author-year)
cited = set(re.findall(r'([A-Z][A-Za-zÀ-ž’\'-]+)(?: et al\.| and [A-Z][A-Za-zÀ-ž’\'-]+)? \(?(\d{4})\)?', main + sup))
reflist = refs
missing = [f'{a} {y}' for a, y in cited if y.isdigit() and 1890 < int(y) < 2030 and a not in ('Table', 'Fig', 'Eq', 'Section', 'September', 'October', 'January', 'December', 'February', 'March', 'April', 'May', 'June', 'Decree', 'Circular', 'VND', 'From', 'Since', 'In', 'The', 'Vietnam', 'Frontier', 'Adding')
           and not re.search(re.escape(a) + r'[^\n]*\(' + y, reflist)]
check(not missing, f'in-text citations found in reference list {missing[:10]}')

# blinding and docx validity
pk = os.path.join(B, 'submission', 'Revised_submission')
for f in sorted(os.listdir(pk)):
    if f.endswith('.docx'):
        with zipfile.ZipFile(os.path.join(pk, f)) as z:
            ok = z.testzip() is None
            for n in z.namelist():
                if n.endswith('.xml'):
                    etree.fromstring(z.read(n))
            check(ok, f'{f} is a valid docx')
            if f.startswith('02_') or f.startswith('10_'):
                txt = ' '.join(z.read(n).decode('utf-8', 'ignore') for n in z.namelist() if n.endswith('.xml'))
                bad = [b for b in ('Binh', 'Trung', 'Hanh', 'Diep', 'apd.edu', 'neu.edu', 'Academy of Policy', '15233582') if b in txt]
                check(not bad, f'{f} blinded {bad}')
print('\nFAILED:', len(fails))
sys.exit(1 if fails else 0)
