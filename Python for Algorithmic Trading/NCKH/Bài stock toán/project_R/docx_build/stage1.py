import re, shutil, os
from lxml import etree
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
src='doc'; dst='clean'
if os.path.exists(dst): shutil.rmtree(dst)
shutil.copytree(src,dst)
tree=etree.parse(dst+'/word/document.xml'); root=tree.getroot()
# 1) deleted paragraph marks -> merge paragraph with next
for rpr_del in list(root.iter(W+'del')):
    par=rpr_del.getparent()
    if par.tag==W+'rPr' and par.getparent().tag==W+'pPr':
        p=par.getparent().getparent(); nxt=p.getnext()
        par.remove(rpr_del)
        if nxt is not None and nxt.tag==W+'p':
            for ch in list(p):
                if ch.tag!=W+'pPr': nxt_first=nxt.find(W+'pPr'); (nxt_first.addnext(ch) if False else None)
            # move p's content (except pPr) to start of nxt (after nxt pPr)
            anchor=nxt.find(W+'pPr')
            items=[c for c in p if c.tag!=W+'pPr']
            for c in reversed(items):
                if anchor is not None: anchor.addnext(c)
                else: nxt.insert(0,c)
            p.getparent().remove(p)
# 2) remove deletions, unwrap insertions
for d in list(root.iter(W+'del')):
    d.getparent().remove(d)
for i in list(root.iter(W+'ins')):
    par=i.getparent()
    if par.tag==W+'rPr': par.remove(i); continue
    idx=par.index(i)
    for c in list(i): par.insert(idx,c); idx+=1
    par.remove(i)
# 3) remove comment anchors
for tag in ('commentRangeStart','commentRangeEnd'):
    for e in list(root.iter(W+tag)): e.getparent().remove(e)
for e in list(root.iter(W+'commentReference')):
    r=e.getparent(); r.getparent().remove(r)
tree.write(dst+'/word/document.xml',xml_declaration=True,encoding='UTF-8',standalone=True)
# 4) drop comment parts
for f in ('comments.xml','commentsExtended.xml','commentsIds.xml','commentsExtensible.xml'):
    os.remove(f'{dst}/word/{f}')
rels=open(dst+'/word/_rels/document.xml.rels').read()
rels=re.sub(r'<Relationship [^>]*Target="comments[^"]*"/>','',rels)
open(dst+'/word/_rels/document.xml.rels','w').write(rels)
ct=open(dst+'/[Content_Types].xml').read()
ct=re.sub(r'<Override [^>]*PartName="/word/comments[^"]*"[^>]*/>','',ct)
open(dst+'/[Content_Types].xml','w').write(ct)
# 5) turn off track changes flag
st=open(dst+'/word/settings.xml').read()
st=re.sub(r'<w:trackRevisions[^>]*/>','',st)
open(dst+'/word/settings.xml','w').write(st)
print('ok')
