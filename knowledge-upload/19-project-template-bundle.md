# Bokprojektmall – kanonisk version

Denna Knowledge-fil genereras direkt från `templates/bokprojekt/`, som är single source of truth. Använd filerna nedan som grund när ett nytt bokprojekt skapas. Ändra inte denna bundle manuellt; ändra mallen och generera om den. `project-manifest.json` i mallen är ett template-manifest och ska initieras för det konkreta projektet med `scripts/project_integrity.py init`.

## `README.md`

````markdown
# Bokprojekt

Detta projekt är skapat från Lärobokskaparens kanoniska projektmall.

## Arbetsflöde
1. Håll bokmetadata i `book.yaml`.
2. Planera boken i `docs/bokspecifikation.md` och `docs/kapitelplan.md`.
3. Skriv inledningen i `chapters/00-inledning.md` och övriga kapitel som `NN-kort-slug.md`.
4. Håll pedagogik, terminologi och projektstatus synkroniserade i `docs/`.
5. Verifiera projektet före och efter ändringar med `scripts/project_integrity.py`.
6. Bygg EPUB/PDF reproducerbart med `scripts/export-book.py`.

`project-manifest.json` skapas/aktiveras med `init` när ett nytt konkret projekt instansieras från mallen.
````

## `assets/cover/README.md`

````markdown
# Omslag

Lägg omslagsbild här när den har skapats.
````

## `assets/image-prompts/README.md`

````markdown
# Bildprompter

Spara godkända bildprompter här, en fil per bild-ID.
````

## `assets/images/README.md`

````markdown
# Bilder

Inre illustrationer läggs här endast om användaren har valt att använda dem.
````

## `book.yaml`

````yaml
title: ""
subtitle: ""
author: ""
language: "sv"
difficulty: "beginner"
audience: ""
book_type: "textbook"
edition: "1"
version: "0.1"
date: ""
rights: "All rights reserved"
publisher: ""
cover_image: ""
identifier: ""
subject: ""
description: ""
project_slug: ""
chapters:
  - chapters/00-inledning.md
exports:
  epub:
    enabled: true
    include_text_toc: false
    toc_depth: 1
  pdf:
    enabled: true
    include_toc_before_introduction: true
    toc_depth: 3
````

## `chapters/00-inledning.md`

````markdown
# Inledning

Beskriv vad boken handlar om, vem den är för, vilka förkunskaper som antas, hur boken är upplagd och hur läsaren bör använda den.
````

## `chapters/kapitelmall.md`

````markdown
# X. [Titel]

## Varför detta kapitel finns

## Lärandemål

Efter kapitlet ska läsaren kunna:

- ...

## Innan vi börjar

## Huvudförklaring

## Exempel

## Vanliga misstag

## Övningar

### Övning 1

## Snabb sammanfattning

- ...

## Quiz/reflektionsfrågor

1. ...

## Nästa steg
````

## `code/README.md`

````markdown
# Kod

Körbar kod för teknikböcker kan läggas här.
````

## `docs/bokspecifikation.md`

````markdown
# Bokspecifikation

## Titel och undertitel

## Språk och författare

## Ämne och syfte

## Målgrupp och förkunskaper

## Svårighetsgrad

## Boktyp och pedagogisk stil

## Omfattning

## Avgränsningar

## Återkommande exempel eller projekt

## Ton och stil
````

## `docs/export-guide.md`

````markdown
# Exportguide

Exporten använder `book.yaml`, `scripts/export-book.py` och styles under `styles/`.

```bash
python3 scripts/export-book.py
```

För EPUB/PDF krävs Pandoc. PDF kräver dessutom en Pandoc-kompatibel PDF-engine, som XeLaTeX, om inte exporteraren anpassats till annan engine.
````

## `docs/illustration-plan.md`

````markdown
# Illustrationsplan

Inre illustrationer är avstängda tills användaren uttryckligen önskar dem.

| Bild-ID | Kapitel | Syfte | Fil | Promptfil | Status |
|---|---|---|---|---|---|
````

## `docs/kapitelplan.md`

````markdown
# Kapitelplan

## Inledning
- Syfte:
- Status: planerad

## Del 1: [Namn]

### Kapitel 1: [Titel]
- Syfte:
- Läsarens förkunskaper:
- Nya huvudbegrepp:
- Praktiskt exempel/scenario:
- Övning:
- Svårighetsgrad:
- Bygger vidare på:
- Status: planerad

## Progressionskontroll
- Begrepp introduceras i rätt ordning:
- För svåra hopp:
- Repetitionstillfällen:
- Slutprojekt/sammanfattande moment:
````

## `docs/pedagogisk-canon.md`

````markdown
# Pedagogisk canon

## Pedagogisk profil
- Språk:
- Svårighetsgrad:
- Läsarprofil:
- Ton:
- Repetitionstakt:

## Introducerade begrepp
| Begrepp | Första kapitel | Definition | Exempel |
|---|---:|---|---|

## Återkommande exempelprojekt/scenario
- Namn:
- Syfte:
- Regler:
- Kod-/metodstil:

## Versions- och faktaval
- Verktyg/ramverk/versioner:
- Antaganden:
- Delar som kräver färsk verifiering:
````

## `docs/projektstatus.md`

````markdown
# Projektstatus

## Bok
- Titel:
- Språk:
- Författare:
- Version:

## Nuvarande fas
Planering

## Kapitelstatus
| Kapitel | Titel | Status | Kommentar |
|---|---|---|---|
| 0 | Inledning | Planerad | |

## Öppna beslut
- ...

## Nästa rekommenderade steg
- ...
````

## `docs/quality-checklist.md`

````markdown
# Kvalitetschecklista

## Språk och målgrupp
- [ ] Språk, ton och nivå är konsekventa.
- [ ] Förkunskaper respekteras.

## Pedagogik och progression
- [ ] Lärandemål och övningar matchar kapitlets innehåll.
- [ ] Begrepp introduceras innan de används.
- [ ] Nivåhopp är rimliga.

## Teknik och fakta
- [ ] Kod är körbar eller märkt som pseudokod.
- [ ] Versioner och antaganden är dokumenterade.
- [ ] Färska/osäkra fakta är verifierade eller markerade.

## Export
- [ ] `book.yaml` är komplett och kapitelordningen stämmer.
- [ ] Canonical markdown är validerad.
````

## `docs/terminologi.md`

````markdown
# Terminologi

| Term | Definition | Första användning | Kommentar |
|---|---|---|---|
````

## `examples/README.md`

````markdown
# Exempel

Scenarier, data och andra icke-kodexempel kan läggas här.
````

## `exercises/README.md`

````markdown
# Övningar

Separata övningsfiler kan läggas här när bokupplägget kräver det.
````

## `exports/README.md`

````markdown
# Exporter

Genererade EPUB/PDF ska normalt inte vara kanoniskt manus. Logga exporter i `exportlogg.md`.
````

## `exports/exportlogg.md`

````markdown
# Exportlogg

| Tidpunkt | Format | Fil | Källrevision | Kommentar |
|---|---|---|---:|---|
````

## `project-index.md`

````markdown
# Projektindex

## Projekt
- Titel:
- Project-id:
- Revision:
- Senaste verifierade zip:

## Kapitel
- Inledning: planerad
- Skapade kapitel: inga

## Export
- EPUB: ej skapad
- PDF: ej skapad

## Synkkontroll
- `book.yaml`, kapitelplan och projektstatus ska beskriva samma aktuella projektläge.
````

## `project-manifest.json`

````json
{
  "schema_version": 1,
  "template": true,
  "project_id": "",
  "project_slug": "",
  "revision": 0,
  "parent_revision": null,
  "canonical_zip_name": "",
  "tracked_files": {},
  "chapters": {},
  "last_operation": null
}
````

## `revision-log.md`

````markdown
# Revisionslogg

| Revision | Tidpunkt (UTC) | Åtgärd | Ändrade filer | Zip-fil |
|---:|---|---|---|---|
````

## `scripts/export-book.py`

````python
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
````

## `scripts/export-book.sh`

````bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/export-book.py "$@"
````

## `scripts/project_integrity.py`

````python
#!/usr/bin/env python3
from __future__ import annotations
import argparse, fnmatch, hashlib, json, re, sys, uuid
from datetime import datetime, timezone
from pathlib import Path

MANIFEST='project-manifest.json'; LOG='revision-log.md'; IGNORED={'.git','.DS_Store','__MACOSX'}
CHAPTER_RE=re.compile(r'^chapters/(\d{2})-[a-z0-9][a-z0-9-]*\.md$',re.I)

def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def digest(p):
    h=hashlib.sha256();
    with p.open('rb') as f:
        for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
    return h.hexdigest()
def inventory(root):
    out={}
    for p in sorted(root.rglob('*')):
        if not p.is_file(): continue
        r=p.relative_to(root)
        if r.as_posix()==MANIFEST or any(x in IGNORED for x in r.parts): continue
        out[r.as_posix()]={'sha256':digest(p),'bytes':p.stat().st_size}
    return out
def summary(files):
    items={}
    for path,info in files.items():
        m=CHAPTER_RE.fullmatch(path)
        if m and m.group(1)!='00': items[path]=info['sha256']
    nums=sorted(int(CHAPTER_RE.fullmatch(p).group(1)) for p in items)
    return {'count':len(nums),'latest':nums[-1] if nums else None,'hashes':items}
def load(root): return json.loads((root/MANIFEST).read_text(encoding='utf-8'))
def save(root,m): (root/MANIFEST).write_text(json.dumps(m,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
def compare(a,b):
    A=set(a); B=set(b)
    return sorted(B-A),sorted(A-B),sorted(p for p in A&B if a[p]!=b[p])
def append_log(root,rev,op,changed,zname):
    p=root/LOG
    if not p.exists(): p.write_text('# Revisionslogg\n\n| Revision | Tidpunkt (UTC) | Åtgärd | Ändrade filer | Zip-fil |\n|---:|---|---|---|---|\n',encoding='utf-8')
    files=', '.join(f'`{x}`' for x in changed) or 'Inga'
    with p.open('a',encoding='utf-8') as f: f.write(f'| {rev} | {now()} | {op.replace("|","/")} | {files} | `{zname}` |\n')
def root(v):
    p=Path(v).resolve()
    if not p.is_dir(): raise ValueError(f'Projektkatalog saknas: {p}')
    return p

def verify(r):
    m=load(r)
    if m.get('template'): raise ValueError('Manifestet är fortfarande en mall. Kör init för ett konkret projekt.')
    if not m.get('project_id') or not isinstance(m.get('revision'),int) or m['revision']<1: raise ValueError('Manifestet saknar giltigt project_id/revision')
    actual=inventory(r); add,rem,chg=compare(m.get('tracked_files',{}),actual)
    if add or rem or chg: raise ValueError(f'Integritetsfel: tillagda={add}, borttagna={rem}, ändrade={chg}')
    if summary(actual)!=m.get('chapters'): raise ValueError('Kapitelöversikten matchar inte filerna')
    return m

def cmd_init(a):
    r=root(a.root); mp=r/MANIFEST
    if mp.exists():
        old=json.loads(mp.read_text(encoding='utf-8'))
        if not old.get('template'): raise ValueError('init får inte köras på redan initierat projekt')
    files=inventory(r); rev=a.revision
    m={'schema_version':1,'template':False,'project_id':str(uuid.uuid4()),'project_slug':a.slug,'revision':rev,'parent_revision':None,'created_at':now(),'updated_at':now(),'canonical_zip_name':a.zip_name,'tracked_files':files,'chapters':summary(files),'last_operation':{'operation':a.operation,'source_revision':None,'changed_files':sorted(files)}}
    save(r,m); append_log(r,rev,a.operation,sorted(files),a.zip_name); m['tracked_files']=inventory(r); m['chapters']=summary(m['tracked_files']); save(r,m)
    print(f'OK: init revision {rev}, project_id={m["project_id"]}'); return 0

def cmd_verify(a):
    m=verify(root(a.root)); print(f'OK: revision {m["revision"]}, project_id={m["project_id"]}, kapitel={m["chapters"]["count"]}'); return 0

def cmd_status(a):
    r=root(a.root); m=load(r); actual=inventory(r); add,rem,chg=compare(m.get('tracked_files',{}),actual)
    print(json.dumps({'revision':m.get('revision'),'added':add,'removed':rem,'changed':chg},ensure_ascii=False,indent=2)); return 1 if rem else 0

def cmd_commit(a):
    r=root(a.root); m=load(r)
    if m.get('template'): raise ValueError('Kör init först')
    if m.get('revision')!=a.expected_revision: raise ValueError(f'Förväntade revision {a.expected_revision}, fick {m.get("revision")}')
    actual=inventory(r); add,rem,chg=compare(m['tracked_files'],actual); changed=sorted(add+rem+chg)
    disallowed=[p for p in changed if not any(fnmatch.fnmatch(p,x) for x in a.allow)]
    if disallowed: raise ValueError('Ej tillåtna ändringar: '+', '.join(disallowed))
    old_hashes=m.get('chapters',{}).get('hashes',{})
    for p,h in old_hashes.items():
        if p not in changed and actual.get(p,{}).get('sha256')!=h: raise ValueError(f'Oavsiktlig kapiteländring: {p}')
    newrev=m['revision']+1; append_log(r,newrev,a.operation,changed,a.zip_name); actual=inventory(r)
    m.update({'parent_revision':a.expected_revision,'revision':newrev,'updated_at':now(),'canonical_zip_name':a.zip_name,'tracked_files':actual,'chapters':summary(actual),'last_operation':{'operation':a.operation,'source_revision':a.expected_revision,'changed_files':changed}}); save(r,m)
    print(f'OK: revision {newrev}; ändrade={changed}'); return 0

def main():
    p=argparse.ArgumentParser(); s=p.add_subparsers(dest='cmd',required=True)
    x=s.add_parser('init'); x.add_argument('root'); x.add_argument('--slug',required=True); x.add_argument('--revision',type=int,default=1); x.add_argument('--zip-name',required=True); x.add_argument('--operation',default='Initierade bokprojekt'); x.set_defaults(fn=cmd_init)
    x=s.add_parser('verify'); x.add_argument('root'); x.set_defaults(fn=cmd_verify)
    x=s.add_parser('status'); x.add_argument('root'); x.set_defaults(fn=cmd_status)
    x=s.add_parser('commit'); x.add_argument('root'); x.add_argument('--expected-revision',type=int,required=True); x.add_argument('--operation',required=True); x.add_argument('--zip-name',required=True); x.add_argument('--allow',action='append',default=[]); x.set_defaults(fn=cmd_commit)
    a=p.parse_args()
    try: return a.fn(a)
    except (ValueError,FileNotFoundError,json.JSONDecodeError) as e: print('FEL:',e,file=sys.stderr); return 2
if __name__=='__main__': raise SystemExit(main())
````

## `styles/epub.css`

````css
body { line-height: 1.6; }
p { margin: 0 0 0.8em; }
h1, h2, h3 { line-height: 1.2; }
h1 { text-align: center; margin: 1.2em 0 0.7em; }
img { max-width: 100%; height: auto; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #999; padding: 0.35em 0.5em; vertical-align: top; }
pre { white-space: pre-wrap; padding: 0.7em; }
````

## `styles/pdf.css`

````css
@page { margin: 22mm 20mm 22mm 20mm; }
body { line-height: 1.5; }
h1 { break-before: page; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #999; padding: 0.35em 0.5em; vertical-align: top; }
img { max-width: 100%; height: auto; }
````

## Obligatoriskt projektbeteende

- Välj exakt en indata-zip för varje filbaserad ändring.
- Verifiera före ändring och verifiera den färdiga leveranszipen igen.
- Ändra endast uttryckligen tillåtna filer; skydda övriga kapitelfiler.
- Leverera monoton revision och revisionskvittens.
