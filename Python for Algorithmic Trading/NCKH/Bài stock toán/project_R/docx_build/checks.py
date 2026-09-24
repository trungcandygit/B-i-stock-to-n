import re,sys
L=[l.rstrip('\n') for l in open(sys.argv[1])]
txt=[(int(l.split(' ',2)[0]),l.split(' ',2)[2]) for l in L if len(l.split(' ',2))==3]
ref_i=[i for i,t in txt if t.startswith('Al Rababa')][0]
body=[(i,t) for i,t in txt if i<ref_i]; refs=[t for i,t in txt if i>=ref_i]
B=' \n'.join(t for i,t in body)
print('== adverbs (non-technical)')
keep={'daily','only','statistically','significantly','separately','logarithmically','jointly','respectively','annually','equally','negatively','publicly','rely','Finally','Firstly','Secondly','Thirdly','unlikely','roughly','mainly','perfectly','partially','observationally'}
from collections import Counter
c=Counter(w for w in re.findall(r'\b[A-Za-z]+ly\b',B) if w not in keep); print(dict(c))
print('== slop words'); 
for w in ['genuine','critical','crucial','robust','substantial','markedly','strictly','directly','explicitly','inevitably','essentially','fundamental','sharp','leverag','utiliz','deploy','foster','paramount','ensure','guarantee','prove','verify','delve','pivotal','landscape','underscore','notabl','seamless','intricate','showcase','furthermore','moreover','additionally']:
    n=len(re.findall(w,B,re.I)); 
    if n: print(w,n)
print('== possessive ’s', re.findall(r"\w+[’']s \w+",B))
print('== em dash', B.count('—'), '== e.g./i.e. w/o comma', re.findall(r'\b(?:e\.g\.|i\.e\.)(?!,)',B))
print('== Wh- sentence starts', re.findall(r'(?:^|\. )((?:What|Which|Why|How|Where|Who)\b[^.]{0,40})',B))
print('== not X but Y', re.findall(r'[^.]{0,30}\bnot [^.,]{0,40}, but [^.]{0,30}',B))
# citations vs refs
cites=set()
for m in re.finditer(r'([A-Z][A-Za-zÀ-ž’\-]+)(?: et al\.| and [A-Z][A-Za-zÀ-ž\-]+)?[\s\xa0]\(?(\d{4})\)?',B):
    cites.add((m.group(1),m.group(2)))
rk=set((re.match(r"([^,]+),",r).group(1).split()[-1], re.search(r'\((\d{4})\)',r).group(1)) for r in refs if re.search(r'\((\d{4})\)',r))
print('== refs not cited', [k for k in rk if not any(k[0].endswith(c[0]) or c[0].endswith(k[0].split()[-1]) for c in cites if c[1]==k[1])])
print('== cites not in refs', sorted(c for c in cites if int(c[1])<2026 and int(c[1])>1900 and not any(c[1]==k[1] and (c[0] in k[0] or k[0] in c[0]) for k in rk)))
# figure/table order
for lab,rx in [('Table',r'Table[\s\xa0](\d)'),('Fig',r'(?:Fig\.|Figure)[\s\xa0](\d)')]:
    first={}; cap={}
    for i,t in body:
        if re.match(rf'(Table|Fig\.) \d',t) and (t.startswith(lab)):
            cap.setdefault(re.match(r'\S+ (\d)',t).group(1),i)
        else:
            for n in re.findall(rx,t): first.setdefault(n,i)
    print('==',lab,'first-cite vs caption', {k:(first.get(k),cap[k]) for k in sorted(cap)}, 'BAD' if any(first.get(k,1e9)>cap[k] for k in cap) else 'ok')
# abbreviations first use
abbr=Counter(re.findall(r'\b[A-Z]{2,}[0-9]*\b',B))
print('== abbrevs', ' '.join(sorted(abbr)))
