#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, shutil, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def scalar(text: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(?:\"([^\"]*)\"|'([^']*)'|([^#\n]*))", text)
    if not m: return ""
    return next((g for g in m.groups() if g is not None), "").strip()

def metadata():
    p=ROOT/'book.yaml'
    if not p.is_file(): raise SystemExit('Saknar book.yaml')
    t=p.read_text(encoding='utf-8')
    values={k:scalar(t,k) for k in ('title','subtitle','author','language','identifier','date','version')}
    missing=[k for k in ('title','author','language') if not values[k]]
    if missing: raise SystemExit('Saknad metadata i book.yaml: '+', '.join(missing))
    return values

def chapters():
    intro=ROOT/'chapters/00-inledning.md'
    if not intro.is_file(): raise SystemExit('Saknar chapters/00-inledning.md')
    numbered=[]
    for p in (ROOT/'chapters').glob('*.md'):
        m=re.match(r'^(\d{2})-[a-z0-9][a-z0-9-]*\.md$', p.name, re.I)
        if m and m.group(1)!='00': numbered.append((int(m.group(1)),p))
    numbered.sort()
    return [intro]+[p for _,p in numbered]

def validate_markdown(paths):
    errors=[]
    for p in paths:
        t=p.read_text(encoding='utf-8')
        if re.search(r'(?m)^#{4,}\s',t): errors.append(f'{p.name}: H4 eller djupare rubrik')
        if t.count('```') % 2: errors.append(f'{p.name}: obalanserade kodblock')
    if errors: raise SystemExit('Markdown-validering misslyckades:\n- '+'\n- '.join(errors))

def run(cmd):
    print('+',' '.join(str(x) for x in cmd)); subprocess.run(cmd,check=True)

def main():
    a=argparse.ArgumentParser(); a.add_argument('--format',choices=['epub','pdf','all'],default='all'); args=a.parse_args()
    if not shutil.which('pandoc'): raise SystemExit('Pandoc saknas. Installera Pandoc och kör igen.')
    md=metadata(); ch=chapters(); validate_markdown(ch); (ROOT/'exports').mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        merged=Path(td)/'book.md'; merged.write_text('\n\n'.join(p.read_text(encoding='utf-8').strip() for p in ch)+'\n',encoding='utf-8')
        common=['pandoc',str(merged),'--from=gfm','--metadata-file',str(ROOT/'book.yaml')]
        if args.format in ('epub','all'):
            run(common+['--to=epub3','--toc','--toc-depth=1','--css',str(ROOT/'styles/epub.css'),'--output',str(ROOT/'exports/book.epub')])
        if args.format in ('pdf','all'):
            run(common+['--toc','--toc-depth=3','--output',str(ROOT/'exports/book.pdf')])
    return 0
if __name__=='__main__': raise SystemExit(main())
