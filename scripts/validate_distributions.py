#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
KNOWLEDGE=sorted(p.name for p in (ROOT/'knowledge-upload').glob('*.md'))
EXPECTED=[
"01-purpose-and-workflow.md","02-guided-interview.md","03-difficulty-and-pedagogy-model.md",
"04-book-specification-template.md","05-chapter-plan-template.md","06-chapter-template.md",
"07-canon-and-continuity.md","08-quality-checklist.md","09-project-status-template.md",
"10-export-metadata-template.md","11-book-type-patterns.md","12-bilingual-style-guide.md",
"13-example-prompts.md","14-suggested-project-structure.md","15-export-and-rendering-rules.md",
"16-illustration-and-cover-workflow.md","17-canonical-markdown-and-render-contract.md",
"18-local-export-pipeline.md","19-project-template-bundle.md"]
SEMVER=re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
def digest(data): return hashlib.sha256(data).hexdigest()
def read_zip(path):
    with zipfile.ZipFile(path) as z:
        bad=z.testzip()
        if bad: raise SystemExit(f'Korrupt ZIP {path.name}: {bad}')
        return {n:z.read(n) for n in z.namelist() if not n.endswith('/')}
def main():
    p=argparse.ArgumentParser(); p.add_argument('--dist-dir',default=str(ROOT/'dist')); p.add_argument('--version'); a=p.parse_args()
    version=(a.version or (ROOT/'VERSION').read_text(encoding='utf-8')).strip().removeprefix('v')
    if not SEMVER.fullmatch(version): raise SystemExit(f'Ogiltig version: {version}')
    if KNOWLEDGE!=EXPECTED: raise SystemExit(f'Fel Knowledge-lista: {KNOWLEDGE}')
    instr=(ROOT/'gpt-configuration/instructions.md').read_text(encoding='utf-8')
    if len(instr)>8000: raise SystemExit(f'Instructions är {len(instr)} tecken; max 8000')
    required_instruction_terms=('book_kind','textbook','factbook','docs/kallpolicy.md','docs/faktakontroll.md')
    missing_terms=[term for term in required_instruction_terms if term not in instr]
    if missing_terms: raise SystemExit(f'Instructions saknar steg-2-termer: {missing_terms}')
    template_root=ROOT/'templates/bokprojekt'
    for rel in ('chapters/kapitelmall-larobok.md','chapters/kapitelmall-faktabok.md','docs/kallpolicy.md','docs/faktakontroll.md','docs/innehalls-canon.md'):
        if not (template_root/rel).is_file(): raise SystemExit(f'Saknad steg-2-templatefil: {rel}')
    yaml=(template_root/'book.yaml').read_text(encoding='utf-8')
    if not re.search(r'(?m)^book_kind:\s*"textbook"',yaml): raise SystemExit('book.yaml saknar default book_kind=textbook')
    if (template_root/'chapters/kapitelmall.md').exists() or (template_root/'docs/pedagogisk-canon.md').exists(): raise SystemExit('Utfasade steg-1-templatefiler finns kvar')
    # Verify generated bundle without modifying source.
    import subprocess, sys
    subprocess.run([sys.executable,str(ROOT/'scripts/build_distributions.py'),'--output-dir',str(Path(a.dist_dir)/'.validator-build'),'--version',version],check=True,stdout=subprocess.DEVNULL)
    # Remove temporary nested build outputs immediately; actual dist is validated below.
    import shutil; shutil.rmtree(Path(a.dist_dir)/'.validator-build',ignore_errors=True)
    dist=Path(a.dist_dir); cp=dist/f'larobokskaparen-custom-gpt-v{version}.zip'; pp=dist/f'larobokskaparen-chat-v{version}.zip'
    for x in (cp,pp):
        if not x.is_file(): raise SystemExit(f'Saknad distribution: {x}')
    custom=read_zip(cp); portable=read_zip(pp)
    if custom.get('VERSION')!=(version+'\n').encode() or portable.get('VERSION')!=(version+'\n').encode(): raise SystemExit('VERSION mismatch')
    src_instr=(ROOT/'gpt-configuration/instructions.md').read_bytes(); starters=(ROOT/'gpt-configuration/conversation-starters.md').read_bytes()
    if custom.get('gpt-configuration/instructions.md')!=src_instr or portable.get('assistant/instructions.md')!=src_instr: raise SystemExit('Instructions mismatch')
    if custom.get('gpt-configuration/conversation-starters.md')!=starters: raise SystemExit('Conversation starters mismatch')
    for name in EXPECTED:
        src=(ROOT/'knowledge-upload'/name).read_bytes()
        if custom.get('knowledge-upload/'+name)!=src: raise SystemExit(f'Custom Knowledge mismatch: {name}')
        if portable.get('knowledge/'+name)!=src: raise SystemExit(f'Portable Knowledge mismatch: {name}')
    # Portable template must be byte-identical with source template.
    for path in sorted(p for p in (ROOT/'templates/bokprojekt').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'):
        rel=path.relative_to(ROOT/'templates/bokprojekt').as_posix(); key='templates/bokprojekt/'+rel
        if portable.get(key)!=path.read_bytes(): raise SystemExit(f'Portable template mismatch: {rel}')
    m=json.loads(portable['MANIFEST.json'].decode())
    if m.get('version')!=version or m.get('template_root')!='templates/bokprojekt': raise SystemExit('MANIFEST metadata mismatch')
    if m.get('knowledge')!=['knowledge/'+n for n in EXPECTED]: raise SystemExit('MANIFEST Knowledge mismatch')
    for e in m.get('files',[]):
        if e['path'] not in portable or digest(portable[e['path']])!=e['sha256']: raise SystemExit(f'MANIFEST SHA mismatch: {e["path"]}')
    print(f'OK: distributionerna för {version} är validerade.')
    print(f'OK: Instructions är {len(instr)} tecken (max 8000).')
    print('OK: Conversation starters är byte-identiska med källan; 19 Knowledge-filer och portabel template är byte-identiska med källorna.')
    print('OK: Steg 2-profiler, två kapitelmallar, källpolicy och faktakontroll är validerade.')
    return 0
if __name__=='__main__': raise SystemExit(main())
