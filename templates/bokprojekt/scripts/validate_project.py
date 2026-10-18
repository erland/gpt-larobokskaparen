#!/usr/bin/env python3
from __future__ import annotations
import re, subprocess, sys
sys.dont_write_bytecode=True
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MARKERS=('TODO','TBD','[SKRIV','[FYLL I','Lorem ipsum')
EDITORIAL_PATTERNS=(
    r'fortsatta bokarbetet', r'inför (?:färdigställandet|publicering|utgivning)',
    r'innan publicering', r'redaktionell (?:anmärkning|notering|kommentar)',
    r'återstår att (?:faktagranska|verifiera|kontrollera)',
    r'(?:behöver|måste|ska) (?:kontrolleras|verifieras|uppdateras) (?:före|inför) (?:publicering|utgivning)',
)
EDITORIAL_HEADING_PATTERNS=(
    r'redaktionell(?:a|t)?\s+(?:granskning|noteringar?|anmärkningar?|kommentarer?)',
    r'redaktionell(?:a|t)?\s+källanmärkning',
    r'kapitel(?:noteringar?|anmärkningar?)',
    r'granskningsanteckningar?',
    r'arbetsanteckningar?',
    r'kvarstående\s+faktakontroll',
    r'att\s+kontrollera\s+inför\s+publicering',
)
EDITORIAL_PROSE_WARNINGS=(
    r'redaktionell(?:a|t)?\s+granskning',
    r'kapitelnoteringar?',
    r'granskningsanteckningar?',
    r'arbetsanteckningar?',
)

def editorial_quality_findings(text):
    """Return (blocking errors, nonblocking warnings) as (line, phrase) pairs."""
    errors=[]; warnings=[]
    heading_re=re.compile(r'^[ \t]{0,3}#{1,6}[ \t]+([^\r\n]+)',re.MULTILINE)
    heading_lines=set()
    for heading in heading_re.finditer(text):
        line=text.count('\n',0,heading.start())+1
        heading_lines.add(line)
        title=re.sub(r'[*_`]', '', heading.group(1))
        for pattern in EDITORIAL_HEADING_PATTERNS:
            if re.search(pattern,title,re.IGNORECASE):
                errors.append((line,title.strip()));break
    for pattern in EDITORIAL_PATTERNS:
        for match in re.finditer(pattern,text,re.IGNORECASE):
            errors.append((text.count('\n',0,match.start())+1,match.group(0)))
    for pattern in EDITORIAL_PROSE_WARNINGS:
        for match in re.finditer(pattern,text,re.IGNORECASE):
            line=text.count('\n',0,match.start())+1
            if line not in heading_lines and not any(x[0]==line for x in errors):
                warnings.append((line,match.group(0)))
    return list(dict.fromkeys(errors)),list(dict.fromkeys(warnings))

SOURCE_REF=re.compile(r'(?<!\w)\[(K\d{3})\](?!\()')
SOURCE_ENTRY=re.compile(r'(?m)^\s*[-*]\s*\*\*\[(K\d{3})\]\*\*')

def source_register_errors(chapters):
    """Check global reference IDs if the optional source register exists."""
    errors=[]; entries={}; used=set()
    for path in chapters:
        body=path.read_text(encoding='utf-8')
        if 'kall' in path.name.lower() or 'käll' in path.name.lower():
            for match in SOURCE_ENTRY.finditer(body):
                code=match.group(1)
                if code in entries: errors.append(f'Dubbelt käll-ID {code} i {path.name}')
                entries[code]=path.name
        else:
            used.update(SOURCE_REF.findall(body))
    if used and not entries: errors.append('Källhänvisningar finns men globalt källregister saknas')
    for code in sorted(used-set(entries)):
        errors.append(f'Källhänvisning {code} saknas i källregistret')
    return errors


def main()->int:
    errors=[]; warnings=[]
    integrity=subprocess.run([sys.executable,'scripts/project_integrity.py','verify','.'],cwd=ROOT,text=True,capture_output=True)
    if integrity.returncode!=0: errors.append('Projektets integritetsverifiering misslyckades: '+(integrity.stderr or integrity.stdout).strip())
    sys.path.insert(0,str(ROOT/'scripts'))
    import importlib.util
    spec=importlib.util.spec_from_file_location('export_book',ROOT/'scripts/export-book.py'); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    try:
        text=mod.read_book_yaml(); meta=mod.metadata(text); chapters=mod.resolve_chapters(text); mod.validate_markdown(chapters)
    except SystemExit as exc: errors.append(str(exc)); chapters=[]; meta={}
    if meta and not meta.get('project_slug'): errors.append('book.yaml saknar project_slug')
    if meta and not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',meta.get('project_slug','')): errors.append('project_slug måste vara en gemen kebab-case slug')
    diagram_check=subprocess.run([sys.executable,'scripts/render_diagrams.py','--check'],cwd=ROOT,text=True,capture_output=True)
    if diagram_check.returncode!=0: errors.append('Diagramvalidering misslyckades: '+(diagram_check.stderr or diagram_check.stdout).strip())
    errors.extend(source_register_errors(chapters))
    for path in chapters:
        text=path.read_text(encoding='utf-8')
        if not text.strip(): errors.append(f'{path.relative_to(ROOT)} är tom')
        if sum(1 for line in text.splitlines() if re.match(r'^#\s+',line))!=1: errors.append(f'{path.relative_to(ROOT)} ska ha exakt en H1')
        # Accept NN-title.md and title-NN.md, with "1. Titel" or "Kapitel 1: Titel".
        # Intro, appendices and source registers intentionally have unnumbered H1.
        first=next((line.strip() for line in text.splitlines() if line.strip()), '')
        name=path.stem.lower()
        special=bool(re.search(r'inledning|introduktion|appendix|bilaga|kall|käll|register',name,re.I))
        filename_num=re.match(r'^(\d{2})-',path.name) or re.search(r'-(\d{2})\.md$',path.name)
        title_num=re.fullmatch(r'#\s*(?:Kapitel\s+)?(\d+)\s*[.:]\s+.+',first,re.I)
        if not special and filename_num and title_num:
            if int(filename_num.group(1))!=int(title_num.group(1)):
                errors.append(f'{path.relative_to(ROOT)} har olika kapitelnummer i filnamn och H1')
        editorial_errors, editorial_warnings=editorial_quality_findings(text)
        for line,phrase in editorial_errors:
            errors.append(f'{path.relative_to(ROOT)}:{line} innehåller redaktionell arbetsmarkör: {phrase}')
        for line,phrase in editorial_warnings:
            warnings.append(f'{path.relative_to(ROOT)}:{line} möjlig redaktionell notering: {phrase}')
        for marker in MARKERS:
            if marker.lower() in text.lower(): errors.append(f'{path.relative_to(ROOT)} innehåller arbetsmarkören {marker}')
        for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)',text):
            ref=m.group(1).split()[0].strip('<>')
            if ref.startswith(('http://','https://')): continue
            target=(path.parent/ref).resolve()
            try: target.relative_to(ROOT.resolve())
            except ValueError: errors.append(f'{path.relative_to(ROOT)} har bildreferens utanför projektet: {ref}'); continue
            if not target.exists(): errors.append(f'{path.relative_to(ROOT)} saknar bildfil: {ref}')
    if warnings:
        print('Editorial warnings:\n- '+'\n- '.join(warnings),file=sys.stderr)
    if errors:
        print('Validation failed:\n- '+'\n- '.join(errors),file=sys.stderr); return 1
    print(f"OK: projektvalidering godkänd. {len(chapters)} boktextfiler, profil={meta.get('book_kind')}."); return 0
if __name__=='__main__': raise SystemExit(main())
