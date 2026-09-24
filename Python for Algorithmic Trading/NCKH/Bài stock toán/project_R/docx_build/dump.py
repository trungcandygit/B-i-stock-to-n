import sys
from lxml import etree
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
M='{http://schemas.openxmlformats.org/officeDocument/2006/math}'
doc=etree.parse(sys.argv[1]+'/word/document.xml')
body=doc.getroot().find(W+'body')
def ptext(p):
    out=[]
    for el in p.iter():
        if el.tag==W+'t':
            if any(a.tag==W+'del' for a in el.iterancestors()): continue
            if any(a.tag==M+'oMath' for a in el.iterancestors()): continue
            out.append(el.text or '')
        elif el.tag==M+'oMath':
            if any(a.tag==M+'oMath' for a in el.iterancestors()): continue
            out.append('$'+''.join(t.text or '' for t in el.iter(M+'t'))+'$')
        elif el.tag==W+'tab': out.append('\t')
        elif el.tag==W+'drawing': out.append('[IMG]')
    return ''.join(out)
i=0
for child in body:
    if child.tag==W+'p':
        i+=1
        st=child.find(W+'pPr/'+W+'pStyle')
        s=st.get(W+'val') if st is not None else ''
        print(f"P{i} [{s}] {ptext(child)}")
    elif child.tag==W+'tbl':
        print("<TABLE>")
        for tr in child.iter(W+'tr'):
            print(' | '.join(''.join(ptext(p) for p in tc.iter(W+'p')) for tc in tr.iter(W+'tc')))
            i+=sum(1 for _ in tr.iter(W+'p'))
        print("</TABLE>")
