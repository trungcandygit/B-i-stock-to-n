"""JEMF word count (run build_jemf.py first): everything in the anonymized manuscript (title, abstract, keywords, text, captions, notes, tables,
references), equations excluded. Usage: python3 jemf_count.py"""
import os, re
S = os.path.dirname(os.path.abspath(__file__))
md = open(os.path.join(S, '..', '..', 'submission', 'JEMF_submission', '02_Manuscript_anonymized.md'), encoding='utf-8').read()
md = re.sub(r'\$\$.*?\$\$', ' ', md, flags=re.S)
md = re.sub(r'!\[\]\([^)]*\)\{[^}]*\}', ' ', md)
md = re.sub(r'^:::.*$', ' ', md, flags=re.M)
parts = {'text': 0, 'tables': 0, 'references': 0}
body, refs = md.split('References', 1) if False else (md[:md.rfind('References')], md[md.rfind('References'):])
def words(s):
    s = re.sub(r'[|*~^\\#]', ' ', s); s = re.sub(r'(?m)^\|?-{3,}.*$', ' ', s)
    return len([w for w in s.split() if re.search(r'\w', w)])
tab = '\n'.join(l for l in body.splitlines() if l.startswith('|'))
txt = '\n'.join(l for l in body.splitlines() if not l.startswith('|'))
abs_ = re.search(r'\*\*Abstract\*\* (.*)', body).group(1)
parts.update(text=words(txt), tables=words(tab), references=words(refs))
print(parts, 'TOTAL', sum(parts.values()), '| abstract', words(abs_))
