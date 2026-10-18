#!/usr/bin/env python3
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'templates/bokprojekt/publishing/pdf-template.tex'
s=p.read_text(encoding='utf-8')
assert r'\setcounter{chapter}{#1}' in s, 'PDF chapter headings must update the actual LaTeX chapter counter'
assert r'\setcounter{section}{0}' in s, 'PDF chapters must reset section numbering'
print('PASS: chapter/section counters synchronized in PDF')
