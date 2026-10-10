"""Journal of Emerging Market Finance (Sage) package: anonymized manuscript (no declarations), separate title page with
Sage 'Statements and Declarations', supplementary material, figure files (>= 300 dpi) and cover letter.

Usage (from project_R/docx_build):  python3 build_jemf.py
Outputs: ../../submission/JEMF_submission/"""
import os, shutil, subprocess, sys
S = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, S)
import build_r2 as B
import r2_text as TX
from r2_lit import REFERENCES

OUT = os.path.join(S, '..', '..', 'submission', 'JEMF_submission')
FMT = 'markdown+subscript+superscript+tex_math_dollars+pipe_tables+fenced_divs+link_attributes'
P = B.para

ACK = 'Writing assistance and use of generative AI: ' + B.AI_USE
SD = [('Ethical considerations', 'Not applicable. The study uses only publicly available historical index prices and involves '
       'no human or animal participants.'),
      ('Consent to participate', 'Not applicable.'),
      ('Consent for publication', 'Not applicable.'),
      ('Declaration of conflicting interest', 'The author(s) declared no potential conflicts of interest with respect to the '
       'research, authorship, and/or publication of this article.'),
      ('Funding statement', 'The author(s) received no financial support for the research, authorship, and/or publication of '
       'this article.'),
      ('Data availability', 'The index price data were obtained from TradingView (exchange: HOSE) and are subject to the '
       'vendor’s terms of use; the merged dataset is available from the corresponding author upon reasonable request. The R '
       'code that reproduces every table and figure, with a map from each reported number to its output file, is provided '
       'with the submission and will be deposited in a public repository upon acceptance.')]


def manuscript_md():
    md = [P('Title', TX.TITLE), P('abstract', '**Abstract** ' + B.inline(TX.ABSTRACT)),
          P('keywords', '**Keywords** ' + TX.KEYWORDS), P('keywords', '**JEL Classification** ' + TX.JEL),
          B.render(TX.body()), P('heading1', 'References')]
    md += [P('referenceitem', r.replace('*', '\\*')) for r in REFERENCES]
    return '\n'.join(md)


def title_page_md():
    md = [P('Title', TX.TITLE), P('p1a', B.AUTHORS)] + [P('Compact', a) for a in B.AFFIL]
    md += [P('heading1', 'Acknowledgments'), P('p1a', ACK),
           P('heading1', 'Author Contributions'), P('p1a', B.CREDIT),
           P('heading1', 'Statements and Declarations')]
    for k, v in SD:
        md += [P('heading2', k), P('p1a', v)]
    return '\n'.join(md)


def supplement_md():
    blocks = TX.supplement()
    blocks[0] = ('h1', 'Supplementary Material')
    blocks[1] = ('p1a', 'This document accompanies the article and reports the robustness checks and the tables cited in the '
                 'main text as Tables S1–S17 and Fig. S1. All numbers come from the R outputs of the replication code.')
    return '\n'.join([P('Title', 'Supplementary Material: ' + TX.TITLE), B.render(blocks)])


def pandoc(md, name, post=True):
    mdp = os.path.join(OUT, name + '.md'); open(mdp, 'w', encoding='utf-8').write(md)
    out = os.path.join(OUT, name + '.docx')
    subprocess.run(['pandoc', mdp, '-f', FMT, '-t', 'docx', '--reference-doc', B.REF_DOC, '-o', out], check=True)
    if post:
        B.post(out)
    os.remove(mdp) if name != '02_Manuscript_anonymized' else None
    print('built', out)


def build():
    os.makedirs(OUT, exist_ok=True)
    pandoc(title_page_md(), '01_Title_page')
    pandoc(manuscript_md(), '02_Manuscript_anonymized')
    pandoc(supplement_md(), '03_Supplementary_material')
    figs = [('fig1', 'Figure1'), ('fig2', 'Figure2'), ('fig4', 'Figure3'), ('fig5', 'Figure4'), ('fig3', 'FigureS1')]
    for k, n in figs:
        shutil.copy(os.path.join(B.FIG, B.FIGMAP[k]), os.path.join(OUT, f'04_{n}.png'))
    cl = os.path.join(S, 'jemf_cover_letter.md')
    if os.path.exists(cl):
        subprocess.run(['pandoc', cl, '-t', 'docx', '-o', os.path.join(OUT, '00_Cover_letter.docx')], check=True)
        print('built cover letter')


if __name__ == '__main__':
    build()
