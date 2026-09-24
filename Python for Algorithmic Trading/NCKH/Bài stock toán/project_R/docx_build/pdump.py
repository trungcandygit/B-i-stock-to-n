import sys; sys.path.insert(0,'.')
from lib_docx import *
from lxml import etree
root=etree.parse('final/word/document.xml').getroot(); body=root.find(W+'body')
for i,c in enumerate(body):
    if c.tag==W+'p':
        t=text_of(c).strip()
        if t: print(i, 'M' if c.find('.//'+M+'oMath') is not None else '-', t)
