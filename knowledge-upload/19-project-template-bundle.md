# Bokprojektmall – kanonisk version

Denna Knowledge-fil genereras direkt från `templates/bokprojekt/`, som är single source of truth. Använd filerna nedan som grund när ett nytt bokprojekt skapas. Ändra inte denna bundle manuellt; ändra mallen och generera om den. `project-manifest.json` i mallen är ett template-manifest och ska initieras för det konkreta projektet med `scripts/project_integrity.py init`.

## `README.md`

````markdown
# Bokprojekt

Detta projekt är skapat från Lärobokskaparens kanoniska projektmall och stödjer både lärobok (`textbook`) och faktabok (`factbook`).

## Arbetsflöde
1. Ange `book_kind` och `book_type` samt övrig metadata i `book.yaml`.
2. Planera boken i `docs/bokspecifikation.md` och `docs/kapitelplan.md`.
3. Skriv inledningen i `chapters/00-inledning.md`.
4. Använd `kapitelmall-larobok.md` för lärobok eller `kapitelmall-faktabok.md` för faktabok när nya kapitel skapas.
5. Håll canon, terminologi, källpolicy, faktakontroll och projektstatus synkroniserade vid behov.
6. Verifiera före och efter ändringar med `scripts/project_integrity.py`.
7. Bygg EPUB/PDF reproducerbart med `scripts/export-book.py`.

Arbetsnoteringar i `docs/` är inte boktext och ska inte exporteras om de inte uttryckligen införs i bokens kapitel eller källförteckning.

## GitHub Actions och publicering
- `01-validate.yml` validerar PR/push till `main`.
- `02-build-preview.yml` bygger EPUB/PDF manuellt och laddar upp ett gemensamt preview-artifact.
- `03-release.yml` bygger på `v*`-tagg och publicerar EPUB/PDF som separata GitHub Release-assets.
- `scripts/build_book.py` är CI-wrapper; `scripts/export-book.py` är kanonisk exportmotor.
````

## `book.yaml`

````yaml
title: ""
subtitle: ""
author: ""
language: "sv"
book_kind: "textbook" # textbook | factbook
book_type: "complete_textbook"
difficulty: "beginner" # beginner | basic | experienced | advanced
audience: ""
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

## `project-index.md`

````markdown
# Projektindex

## Projekt
- Titel:
- book_kind:
- book_type:
- Project-id:
- Revision:
- Senaste verifierade zip:

## Kapitel
- Inledning: planerad
- Skapade kapitel: inga

## Faktakontroll
- Policy: `docs/kallpolicy.md`
- Register: `docs/faktakontroll.md`
- Öppna punkter:

## Export
- EPUB: ej skapad
- PDF: ej skapad

## Synkkontroll
- `book.yaml`, bokspecifikation, kapitelplan och projektstatus ska beskriva samma aktuella bokprofil och projektläge.
````

## `docs/bokspecifikation.md`

````markdown
# Bokspecifikation

## Titel och undertitel

## Bokprofil
- book_kind: textbook / factbook
- book_type:
- Motivering:

## Språk och författare

## Ämne och syfte

## Målgrupp

## Nivå eller faktadjup

## Omfattning och avgränsningar

## Ton och stil

## Läroboksspecifikt (om textbook)
- Förkunskaper:
- Övergripande lärandemål:
- Pedagogisk modell:
- Praktik/teori:

## Faktaboksspecifikt (om factbook)
- Ämnesbredd/fördjupning:
- Berättande/förklarande/referens:
- Centrala faktaområden:
- Källkrav:
- Tidskänslighet:
- Synliga referenser: ja/nej

## Omslag och illustrationer

## Återkommande exempel/case/berättargrepp
````

## `docs/kapitelplan.md`

````markdown
# Kapitelplan

## Bokprofil
- book_kind:
- book_type:

## Inledning
- Syfte:
- Status: planerad

## Del 1: [Namn]

### Kapitel 1: [Titel]
- Syfte:
- Nivå/faktadjup:
- Nya huvudbegrepp/faktaområden:
- Exempel/case:
- Status: planerad

#### Lärobok
- Förkunskaper:
- Lärandemål:
- Övning/praktiskt moment:
- Bygger vidare på:

#### Faktabok
- Kärnfråga/nyfikenhetskrok:
- Centrala fakta:
- Fördjupning/faktaruta:
- Käll-/verifieringsbehov:

## Helhetskontroll
### Lärobok
- Progression:
- Repetition:
- Nivåhopp:

### Faktabok
- Ämnestäckning:
- Balans bredd/djup:
- Upprepningar/luckor:
- Faktakontroll:
````

## `docs/projektstatus.md`

````markdown
# Projektstatus

## Bok
- Titel:
- Språk:
- Författare:
- Version:
- book_kind:
- book_type:

## Nuvarande fas
Planering

## Kapitelstatus
| Kapitel | Titel | Status | Kommentar |
|---|---|---|---|
| 0 | Inledning | Planerad | |

## Faktakontroll
- Öppna verifieringspunkter:
- Senast genomgången:

## Öppna beslut
- ...

## Nästa rekommenderade steg
- ...
````

## `docs/innehalls-canon.md`

````markdown
# Innehålls-canon

## Gemensam profil
- Språk:
- book_kind:
- book_type:
- Nivå/faktadjup:
- Läsarprofil:
- Ton:

## Terminologi och fasta definitioner
| Begrepp | Första kapitel | Definition | Kommentar |
|---|---:|---|---|

## Återkommande exempel, case eller berättargrepp
- Namn:
- Syfte:
- Regler:

## Läroboksspecifikt
- Pedagogisk progression:
- Kod-/metodstil:
- Förkunskaper som senare kapitel får anta:

## Faktaboksspecifikt
- Fasta sakförhållanden som återkommer:
- Kända osäkerheter/tolkningar:
- Tidskänsliga delar:

## Versions- och faktaval
- Verktyg/ramverk/versioner:
- Antaganden:
- Delar som kräver färsk verifiering:
````

## `docs/terminologi.md`

````markdown
# Terminologi

| Term | Definition | Första användning | Kommentar |
|---|---|---|---|
````

## `docs/kallpolicy.md`

````markdown
# Källpolicy

## Syfte
Beskriv vilken källnivå boken behöver. Policyn används särskilt för faktaböcker och för aktuellt/omstritt innehåll.

## Grundkrav
- Primärkällor prioriteras när det är praktiskt och relevant.
- Aktuella påståenden ska verifieras nära skriv-/publiceringstillfället.
- Statistik ska ha källa, årtal och tydlig definition.
- Om trovärdiga källor skiljer sig ska skillnaden beskrivas sakligt.
- Osäkerhet får inte skrivas om till säker fakta.

## Projektets val
- Kravnivå: låg / normal / hög / akademisk
- Synliga referenser i boktext: ja / nej
- Källförteckning i slutet: ja / nej
- Referensstil:
- Maximal ålder på tidskänsliga källor:
- Särskilt betrodda källtyper/domäner:
- Källtyper som bör undvikas:

## Anteckning
Källarbetsmaterial hör normalt hemma i `docs/faktakontroll.md` och ska inte exporteras som boktext av misstag.
````

## `docs/faktakontroll.md`

````markdown
# Faktakontroll

Använd detta som arbetsregister. Det är inte automatiskt en publicerad källförteckning.

| ID | Kapitel | Påstående/faktaområde | Status | Källa/verifiering | Kontrollerad | Kommentar |
|---|---|---|---|---|---|---|
| F001 | | | Ej kontrollerad | | | |

## Statusvärden
- Ej kontrollerad
- Verifierad
- Behöver uppdateras
- Osäker/omstridd
- Ej relevant

## Öppna verifieringspunkter
- ...

## Publiceringskontroll
- [ ] Alla högprioriterade påståenden är verifierade.
- [ ] Statistik har årtal/definition där det behövs.
- [ ] Tidskänsliga uppgifter har kontrollerats på nytt.
- [ ] Källnoteringar som inte ska publiceras ligger utanför kapiteltexten.
````

## `docs/quality-checklist.md`

````markdown
# Kvalitetschecklista

## Gemensamt
- [ ] Språk, ton och nivå/djup är konsekventa.
- [ ] Begrepp och fakta motsäger inte canon.
- [ ] Onödiga upprepningar och luckor är hanterade.

## Lärobok (`textbook`)
- [ ] Förkunskaper respekteras.
- [ ] Lärandemål och övningar matchar innehållet när boktypen kräver dem.
- [ ] Begrepp och svårighetsgrad utvecklas i rimlig ordning.

## Faktabok (`factbook`)
- [ ] Ämnestäckning och faktadjup passar målgruppen.
- [ ] Fakta, tolkning och osäkerhet hålls isär.
- [ ] Käll- och faktakontroll är tillräcklig för ämnet.
- [ ] Tidskänsliga uppgifter är aktuella.
- [ ] Engagerande förenklingar är fortfarande sakligt korrekta.

## Teknik
- [ ] Kod är körbar eller märkt som pseudokod.
- [ ] Versioner och antaganden är dokumenterade.

## Export
- [ ] `book.yaml` är komplett och kapitelordningen stämmer.
- [ ] Canonical markdown är validerad.
- [ ] Arbetsnoteringar från `docs/` exporteras inte av misstag.
````

## `docs/illustration-plan.md`

````markdown
# Illustrationsplan

Inre illustrationer är avstängda tills användaren uttryckligen önskar dem.

| Bild-ID | Kapitel | Syfte | Fil | Promptfil | Status |
|---|---|---|---|---|---|
````

## `docs/export-guide.md`

````markdown
# Exportguide

`book.yaml` är enda kanoniska metadata- och kapitelordningskällan.

## Lokalt
```bash
python3 scripts/validate_project.py .
python3 scripts/export-book.py --format all
```
Pandoc 3.1.11.1 rekommenderas. PDF kräver XeLaTeX och TeX Gyre Pagella.

## GitHub
- Validate körs på pull request och push till `main`.
- Build Preview startas manuellt och ger ett gemensamt artifact med EPUB, PDF och SHA256SUMS.
- Release triggas av `v<SemVer>` och publicerar EPUB/PDF som separata release-assets.

Arbetsfiler i `docs/` exporteras aldrig som boktext.
````

## `chapters/00-inledning.md`

````markdown
# Inledning

Beskriv vad boken handlar om, vem den är för, vilka förkunskaper eller vilken läsarnivå som antas, hur boken är upplagd och hur läsaren kan använda den.
````

## `chapters/kapitelmall-larobok.md`

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

## `chapters/kapitelmall-faktabok.md`

````markdown
# X. [Titel]

[Ingress eller nyfikenhetsväckare]

## [Huvudavsnitt]

Förklara ämnet sammanhängande, konkret och anpassat till målgruppen.

## [Fördjupning eller nästa del]

## Konkreta exempel eller fall

## Centrala fakta

- ...

## Visste du att? (valfritt)

## Begrepp att känna till (vid behov)

## Sammanfattning (valfritt)
````

## `exercises/README.md`

````markdown
# Övningar

Separata övningsfiler kan läggas här när bokupplägget kräver det.
````

## `examples/README.md`

````markdown
# Exempel

Scenarier, data och andra icke-kodexempel kan läggas här.
````

## `code/README.md`

````markdown
# Kod

Körbar kod för teknikböcker kan läggas här.
````

## `assets/cover/README.md`

````markdown
# Omslag

Lägg omslagsbild här när den har skapats.
````

## `assets/images/README.md`

````markdown
# Bilder

Inre illustrationer läggs här endast om användaren har valt att använda dem.
````

## `assets/image-prompts/README.md`

````markdown
# Bildprompter

Spara godkända bildprompter här, en fil per bild-ID.
````

## `publishing/epub.css`

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

## `publishing/fix-epub-after-pandoc.py`

````python
#!/usr/bin/env python3
from __future__ import annotations
import re, sys, tempfile, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
OPF="http://www.idpf.org/2007/opf"; XHTML="http://www.w3.org/1999/xhtml"; EPUB="http://www.idpf.org/2007/ops"
NS={"opf":OPF,"x":XHTML,"epub":EPUB}

def rootfile(base: Path) -> Path:
    tree=ET.parse(base/'META-INF/container.xml')
    node=tree.find('.//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile')
    if node is None: raise RuntimeError('EPUB container saknar rootfile')
    return Path(node.attrib['full-path'])

def split_headings(base: Path)->int:
    count=0; pat=re.compile(r'^\s*(\d+)\.\s+(.+?)\s*$')
    for path in base.rglob('*.xhtml'):
        tree=ET.parse(path); changed=False
        for h1 in tree.getroot().findall('.//x:h1',NS):
            text=''.join(h1.itertext()).strip(); m=pat.match(text)
            if not m: continue
            ident=h1.attrib.get('id'); h1.clear()
            if ident: h1.set('id',ident)
            a=ET.SubElement(h1,f'{{{XHTML}}}span',{'class':'chapter-number'}); a.text=m.group(1)
            b=ET.SubElement(h1,f'{{{XHTML}}}span',{'class':'chapter-title'}); b.text=m.group(2)
            changed=True
        if changed: tree.write(path,encoding='utf-8',xml_declaration=True); count+=1
    return count

def nav_non_linear(base: Path, opf_rel: Path)->bool:
    path=base/opf_rel; tree=ET.parse(path); manifest=tree.getroot().find('opf:manifest',NS); spine=tree.getroot().find('opf:spine',NS)
    if manifest is None or spine is None: raise RuntimeError('EPUB OPF saknar manifest/spine')
    nav_ids={i.attrib['id'] for i in manifest.findall('opf:item',NS) if 'nav' in i.attrib.get('properties','').split()}
    changed=False
    for item in spine.findall('opf:itemref',NS):
        if item.attrib.get('idref') in nav_ids and item.attrib.get('linear')!='no': item.set('linear','no'); changed=True
    if changed: tree.write(path,encoding='utf-8',xml_declaration=True)
    return changed

def repack(base:Path,out:Path)->None:
    if out.exists(): out.unlink()
    with zipfile.ZipFile(out,'w') as z:
        mime=base/'mimetype'; z.write(mime,'mimetype',compress_type=zipfile.ZIP_STORED)
        for p in sorted(base.rglob('*')):
            if p.is_file() and p!=mime: z.write(p,p.relative_to(base).as_posix(),compress_type=zipfile.ZIP_DEFLATED)

def validate(path:Path)->None:
    with zipfile.ZipFile(path) as z:
        if not z.namelist() or z.namelist()[0]!='mimetype' or z.getinfo('mimetype').compress_type!=zipfile.ZIP_STORED:
            raise RuntimeError('EPUB-fel: mimetype måste ligga först och vara okomprimerad')
        if 'META-INF/container.xml' not in z.namelist(): raise RuntimeError('EPUB-fel: container.xml saknas')

def main()->int:
    if len(sys.argv)!=2: print('Användning: fix-epub-after-pandoc.py <fil.epub>',file=sys.stderr); return 2
    epub=Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory(prefix='fix-epub-') as td:
        base=Path(td)
        with zipfile.ZipFile(epub) as z: z.extractall(base)
        opf=rootfile(base); headings=split_headings(base); nav=nav_non_linear(base,opf); repack(base,epub)
    validate(epub); print(f'Efterbearbetad EPUB: kapitelfiler={headings}, nav linear=no={nav}'); return 0
if __name__=='__main__': raise SystemExit(main())
````

## `publishing/pdf-template.tex`

````text
\documentclass[11pt,openany]{book}
\usepackage{fontspec}
\defaultfontfeatures{Ligatures=TeX}
$if(pdf-font-dir)$
\setmainfont[Path=$pdf-font-dir$/,Extension=.otf,UprightFont=texgyrepagella-regular,BoldFont=texgyrepagella-bold,ItalicFont=texgyrepagella-italic,BoldItalicFont=texgyrepagella-bolditalic]{texgyrepagella}
$else$
\setmainfont{TeXGyrePagella}
$endif$
\usepackage[paperwidth=170mm,paperheight=240mm,inner=20mm,outer=18mm,top=20mm,bottom=22mm,headsep=5mm,footskip=9mm]{geometry}
\usepackage{graphicx}\usepackage{microtype}\usepackage{setspace}\usepackage{parskip}\usepackage{fancyhdr}\usepackage[hidelinks]{hyperref}\usepackage{bookmark}\usepackage{tocloft}\usepackage{ragged2e}\usepackage{xcolor}\usepackage{longtable}\usepackage{booktabs}\usepackage{array}\usepackage{calc}\usepackage{etoolbox}
\setstretch{1.24}\setlength{\parindent}{0pt}\setlength{\parskip}{0.5em plus 0.08em minus 0.04em}\setlength{\emergencystretch}{1.5em}\widowpenalty=10000\clubpenalty=10000\displaywidowpenalty=10000\raggedbottom
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\pagestyle{fancy}\fancyhf{}\fancyfoot[C]{\small\thepage}\renewcommand{\headrulewidth}{0pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\small\thepage}\renewcommand{\headrulewidth}{0pt}}
\renewcommand{\contentsname}{Innehåll}\setcounter{tocdepth}{2}\setlength{\cftbeforechapskip}{0.35em}
\newcommand{\bookfrontchapter}[1]{\clearpage\phantomsection\addcontentsline{toc}{chapter}{#1}\thispagestyle{plain}\vspace*{8mm}\begin{center}{\fontsize{18}{21}\selectfont\bfseries #1\par}\end{center}\vspace{7mm}}
\newcommand{\bookchapter}[2]{\clearpage\phantomsection\addcontentsline{toc}{chapter}{#1.\ #2}\markboth{#1.\ #2}{#1.\ #2}\thispagestyle{plain}\vspace*{8mm}\begin{center}{\fontsize{13}{15}\selectfont #1\par}\vspace{1.5mm}{\fontsize{16}{19}\selectfont\bfseries #2\par}\end{center}\vspace{7mm}}
\begin{document}
$if(cover-image)$
\thispagestyle{empty}\newgeometry{margin=0pt}\noindent\includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio]{$cover-image$}\restoregeometry\clearpage
$endif$
\thispagestyle{empty}\vspace*{0.20\textheight}\begin{center}{\fontsize{24}{28}\selectfont\bfseries $title$\par}$if(subtitle)$\vspace{0.6em}{\large $subtitle$\par}$endif$\vfill{\large $author$\par}\end{center}\clearpage
\pagenumbering{roman}\setcounter{page}{1}\tableofcontents\clearpage\pagenumbering{arabic}\setcounter{page}{1}
$body$
\end{document}
````

## `publishing/pdf-filter.lua`

````text
-- PDF: numrerade H1 får kompakt tvådelad kapitelstart; övriga H1 (t.ex. Inledning) blir onumrerade kapitel.
function Header(el)
  if el.level ~= 1 then return nil end
  local text = pandoc.utils.stringify(el.content)
  local number, title = text:match("^%s*(%d+)%.%s+(.+)%s*$")
  if number then
    local blocks = pandoc.read(title, "markdown").blocks
    local inlines = (#blocks > 0 and blocks[1].content) or {pandoc.Str(title)}
    local title_tex = pandoc.write(pandoc.Pandoc({pandoc.Para(inlines)}), "latex"):gsub("%s+$", "")
    return pandoc.RawBlock("latex", "\\bookchapter{" .. number .. "}{" .. title_tex .. "}")
  end
  local escaped = pandoc.write(pandoc.Pandoc({pandoc.Para(el.content)}), "latex"):gsub("%s+$", "")
  return pandoc.RawBlock("latex", "\\bookfrontchapter{" .. escaped .. "}")
end
````

## `publishing/build-notes.md`

````markdown
# Build notes

Markdown under `chapters/` är kanonisk boktext. `book.yaml` styr metadata, kapitelordning och exportval.

## Reproducerbar build
- Pandoc är låst till 3.1.11.1 i GitHub Actions.
- PDF byggs med XeLaTeX och TeX Gyre Pagella.
- EPUB efterbearbetas av `fix-epub-after-pandoc.py`.
- Preview och Release använder `scripts/build_book.py`; workflow-YAML innehåller ingen boklogik.
- Arbetsfiler under `docs/` exporteras inte.
````

## `scripts/project_integrity.py`

````python
#!/usr/bin/env python3
from __future__ import annotations
import argparse, fnmatch, hashlib, json, re, sys, uuid
from datetime import datetime, timezone
from pathlib import Path

MANIFEST='project-manifest.json'; LOG='revision-log.md'; IGNORED={'.git','.DS_Store','__MACOSX','__pycache__'}
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
        if r.as_posix()==MANIFEST or any(x in IGNORED for x in r.parts) or p.suffix=='.pyc': continue
        out[r.as_posix()]={'sha256':digest(p),'bytes':p.stat().st_size}
    return out
def summary(files):
    items={}
    by_number={}
    for path,info in files.items():
        m=CHAPTER_RE.fullmatch(path)
        if not m or m.group(1)=='00':
            continue
        number=int(m.group(1))
        if number in by_number:
            raise ValueError(f'Dubbla kapitelfiler för kapitel {number:02d}: {by_number[number]}, {path}')
        by_number[number]=path
        items[path]=info['sha256']
    nums=sorted(by_number)
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

## `scripts/validate_project.py`

````python
#!/usr/bin/env python3
from __future__ import annotations
import re, subprocess, sys
sys.dont_write_bytecode=True
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MARKERS=('TODO','TBD','[SKRIV','[FYLL I','Lorem ipsum')

def main()->int:
    errors=[]
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
    for path in chapters:
        text=path.read_text(encoding='utf-8')
        if not text.strip(): errors.append(f'{path.relative_to(ROOT)} är tom')
        if sum(1 for line in text.splitlines() if re.match(r'^#\s+',line))!=1: errors.append(f'{path.relative_to(ROOT)} ska ha exakt en H1')
        mfile=re.match(r'^(\d{2})-', path.name)
        first=next((line.strip() for line in text.splitlines() if line.strip()), '')
        if mfile and mfile.group(1)!='00':
            mh1=re.fullmatch(r'#\s+(\d+)\.\s+.+', first)
            if not mh1 or int(mh1.group(1))!=int(mfile.group(1)): errors.append(f'{path.relative_to(ROOT)} ska börja med H1 som matchar kapitelnumret')
        for marker in MARKERS:
            if marker.lower() in text.lower(): errors.append(f'{path.relative_to(ROOT)} innehåller arbetsmarkören {marker}')
        for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)',text):
            ref=m.group(1).split()[0].strip('<>')
            if ref.startswith(('http://','https://')): continue
            target=(path.parent/ref).resolve()
            try: target.relative_to(ROOT.resolve())
            except ValueError: errors.append(f'{path.relative_to(ROOT)} har bildreferens utanför projektet: {ref}'); continue
            if not target.exists(): errors.append(f'{path.relative_to(ROOT)} saknar bildfil: {ref}')
    if errors:
        print('Validation failed:\n- '+'\n- '.join(errors),file=sys.stderr); return 1
    print(f"OK: projektvalidering godkänd. {len(chapters)} boktextfiler, profil={meta.get('book_kind')}."); return 0
if __name__=='__main__': raise SystemExit(main())
````

## `scripts/export-book.py`

````python
#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, shutil, subprocess, tempfile
from pathlib import Path, PurePosixPath
ROOT=Path(__file__).resolve().parents[1]
NUMBERED_CHAPTER_RE=re.compile(r'^\d{2}-[a-z0-9][a-z0-9-]*\.md$',re.I)
PANDOC_VERSION='3.1.11.1'

def scalar(text,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*(?:"([^"]*)"|\'([^\']*)\'|([^#\n]*))',text)
    return next((g for g in m.groups() if g is not None),'').strip() if m else ''
def read_book_yaml():
    p=ROOT/'book.yaml'
    if not p.is_file(): raise SystemExit('Saknar book.yaml')
    return p.read_text(encoding='utf-8')
def metadata(text):
    keys=('title','subtitle','author','language','identifier','date','version','book_kind','book_type','cover_image','project_slug','subject','description')
    v={k:scalar(text,k) for k in keys}; missing=[k for k in ('title','author','language','book_kind','book_type','project_slug') if not v[k]]
    if missing: raise SystemExit('Saknad metadata i book.yaml: '+', '.join(missing))
    if v['book_kind'] not in ('textbook','factbook'): raise SystemExit('Ogiltig book_kind: '+v['book_kind'])
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',v['project_slug']): raise SystemExit('project_slug måste vara gemen kebab-case')
    return v
def chapter_entries(text):
    lines=text.splitlines(); start=None; base=0
    for i,line in enumerate(lines):
        m=re.match(r'^(\s*)chapters:\s*(?:#.*)?$',line)
        if m: start=i+1; base=len(m.group(1)); break
    if start is None: raise SystemExit('book.yaml saknar chapters:-lista')
    out=[]
    for line in lines[start:]:
        if not line.strip() or line.lstrip().startswith('#'): continue
        indent=len(line)-len(line.lstrip())
        if indent<=base and not line.lstrip().startswith('-'): break
        m=re.match(r'^\s*-\s*(?:"([^"]+)"|\'([^\']+)\'|([^#\n]+?))\s*(?:#.*)?$',line)
        if not m: raise SystemExit('Ogiltig chapters-post: '+line.strip())
        out.append(next(g for g in m.groups() if g is not None).strip())
    if not out: raise SystemExit('chapters: är tom')
    return out
def resolve_chapters(text):
    entries=chapter_entries(text)
    if len(entries)!=len(set(entries)): raise SystemExit('Dubbellistade kapitel i book.yaml')
    if entries[0]!='chapters/00-inledning.md': raise SystemExit('Första chapters-posten ska vara chapters/00-inledning.md')
    paths=[]
    for e in entries:
        pure=PurePosixPath(e)
        if pure.is_absolute() or '..' in pure.parts or len(pure.parts)!=2 or pure.parts[0]!='chapters': raise SystemExit('Ogiltig kapitelsökväg: '+e)
        p=ROOT/pure.as_posix()
        if not p.is_file(): raise SystemExit('Listad kapitelfil saknas: '+e)
        if p.name.startswith('kapitelmall-'): raise SystemExit('Kapitelmall får inte exporteras: '+e)
        paths.append(p)
    listed={p.relative_to(ROOT).as_posix() for p in paths}; unlisted=[]
    for p in sorted((ROOT/'chapters').glob('*.md')):
        if NUMBERED_CHAPTER_RE.fullmatch(p.name) and p.relative_to(ROOT).as_posix() not in listed: unlisted.append(p.relative_to(ROOT).as_posix())
    if unlisted: raise SystemExit('Numrerade kapitelfiler saknas i book.yaml: '+', '.join(unlisted))
    return paths
def validate_markdown(paths):
    errors=[]
    for p in paths:
        t=p.read_text(encoding='utf-8')
        if re.search(r'(?m)^#{4,}\s',t): errors.append(p.name+': H4 eller djupare rubrik')
        if t.count('```')%2: errors.append(p.name+': obalanserade kodblock')
    if errors: raise SystemExit('Markdown-validering misslyckades:\n- '+'\n- '.join(errors))
def run(cmd): print('+',' '.join(map(str,cmd))); subprocess.run(cmd,cwd=ROOT,check=True)
def find_font_dir():
    for base in (Path('/usr/share/fonts'),Path('/usr/local/share/fonts')):
        if base.exists():
            for p in base.rglob('texgyrepagella-regular.otf'):
                names=['texgyrepagella-regular.otf','texgyrepagella-bold.otf','texgyrepagella-italic.otf','texgyrepagella-bolditalic.otf']
                if all((p.parent/n).is_file() for n in names): return p.parent
    return None
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--format',choices=['epub','pdf','all'],default='all'); ap.add_argument('--output-dir',default=str(ROOT/'exports')); args=ap.parse_args()
    if not shutil.which('pandoc'): raise SystemExit('Pandoc saknas')
    text=read_book_yaml(); meta=metadata(text); chapters=resolve_chapters(text); validate_markdown(chapters)
    out=Path(args.output_dir).resolve(); out.mkdir(parents=True,exist_ok=True); slug=meta['project_slug']
    with tempfile.TemporaryDirectory() as td:
        td=Path(td); body='\n\n'.join(p.read_text(encoding='utf-8').strip() for p in chapters)+'\n'; merged=td/'book.md'; merged.write_text(body,encoding='utf-8')
        common=['pandoc',str(merged),'--from=markdown+pipe_tables+fenced_code_blocks+fenced_divs','--standalone','--metadata-file',str(ROOT/'book.yaml')]
        if args.format in ('epub','all'):
            epub=out/f'{slug}.epub'
            cmd=['pandoc',str(merged),'--from=markdown+pipe_tables+fenced_code_blocks+fenced_divs','--to=epub3','--standalone','--toc','--toc-depth=1','--metadata-file',str(ROOT/'book.yaml'),'--css',str(ROOT/'publishing/epub.css')]
            cover=meta['cover_image'];
            if cover:
                cp=ROOT/cover
                if not cp.is_file(): raise SystemExit('Angiven omslagsbild saknas: '+cover)
                cmd += ['--epub-cover-image',str(cp)]
            run(cmd+['--output',str(epub)]); run([sys.executable,str(ROOT/'publishing/fix-epub-after-pandoc.py'),str(epub)])
        if args.format in ('pdf','all'):
            if not shutil.which('xelatex'): raise SystemExit('XeLaTeX saknas för PDF-export')
            pdf=out/f'{slug}.pdf'; cmd=common+['--top-level-division=chapter','--pdf-engine=xelatex','--template',str(ROOT/'publishing/pdf-template.tex'),'--lua-filter',str(ROOT/'publishing/pdf-filter.lua')]
            fontdir=find_font_dir()
            if fontdir: cmd += ['--metadata',f'pdf-font-dir={fontdir.as_posix()}/']
            cover=meta['cover_image']
            if cover:
                cp=ROOT/cover
                if not cp.is_file(): raise SystemExit('Angiven omslagsbild saknas: '+cover)
                cmd += ['--metadata',f'cover-image={cp.as_posix()}']
            run(cmd+['--output',str(pdf)])
    return 0
if __name__=='__main__':
    import sys
    raise SystemExit(main())
````

## `scripts/export-book.sh`

````bash
#!/usr/bin/env bash
set -euo pipefail
exec python3 "$(dirname "$0")/export-book.py" "$@"
````

## `scripts/build_book.py`

````python
#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, shutil, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sha(path):
    h=hashlib.sha256();
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',required=True); args=ap.parse_args(); out=Path(args.output_dir).resolve(); out.mkdir(parents=True,exist_ok=True)
    subprocess.run([sys.executable,'scripts/validate_project.py','.'],cwd=ROOT,check=True)
    # export-book.py reads project_slug from book.yaml and writes directly to the requested directory.
    subprocess.run([sys.executable,'scripts/export-book.py','--format','all','--output-dir',str(out)],cwd=ROOT,check=True)
    files=sorted(list(out.glob('*.epub'))+list(out.glob('*.pdf')))
    if len([p for p in files if p.suffix=='.epub'])!=1 or len([p for p in files if p.suffix=='.pdf'])!=1: raise SystemExit('Bygget ska ge exakt en EPUB och en PDF')
    (out/'SHA256SUMS.txt').write_text('\n'.join(f'{sha(p)}  {p.name}' for p in files)+'\n',encoding='utf-8')
    print('Bygge klart:',', '.join(p.name for p in files)); return 0
if __name__=='__main__': raise SystemExit(main())
````

## `.github/workflows/01-validate.yml`

````yaml
name: Validate

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@v4
      - name: Validate project
        run: python3 scripts/validate_project.py .
````

## `.github/workflows/02-build-preview.yml`

````yaml
name: Build Preview

on:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  build-preview:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
      - name: Install pinned Pandoc
        uses: pandoc/actions/setup@v1
        with:
          version: "3.1.11.1"
      - name: Install XeLaTeX and PDF tools
        run: |
          sudo apt-get update
          sudo apt-get install -y --no-install-recommends texlive-xetex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended lmodern fonts-texgyre
          fc-cache -f
          find /usr/share/fonts -iname 'texgyrepagella-regular.otf' -print -quit | grep .
      - name: Build EPUB and PDF
        run: python3 scripts/build_book.py --output-dir "${RUNNER_TEMP}/book-dist"
      - name: Upload preview package
        uses: actions/upload-artifact@v4
        with:
          name: ${{ github.event.repository.name }}-preview
          path: |
            ${{ runner.temp }}/book-dist/*.epub
            ${{ runner.temp }}/book-dist/*.pdf
            ${{ runner.temp }}/book-dist/SHA256SUMS.txt
          if-no-files-found: error
          retention-days: 7
````

## `.github/workflows/03-release.yml`

````yaml
name: Release

on:
  push:
    tags: ["v*"]

permissions:
  contents: write

jobs:
  release:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
      - name: Install pinned Pandoc
        uses: pandoc/actions/setup@v1
        with:
          version: "3.1.11.1"
      - name: Install XeLaTeX and PDF tools
        run: |
          sudo apt-get update
          sudo apt-get install -y --no-install-recommends texlive-xetex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended lmodern fonts-texgyre
          fc-cache -f
          find /usr/share/fonts -iname 'texgyrepagella-regular.otf' -print -quit | grep .
      - name: Validate release tag
        shell: bash
        run: |
          [[ "${GITHUB_REF_NAME}" =~ ^v[0-9]+\.[0-9]+\.[0-9]+([+-][0-9A-Za-z.-]+)?$ ]] || { echo "Taggen måste vara v<SemVer>" >&2; exit 1; }
      - name: Build EPUB and PDF
        run: python3 scripts/build_book.py --output-dir "${RUNNER_TEMP}/book-dist"
      - name: Create or update GitHub Release
        env:
          GH_TOKEN: ${{ github.token }}
        shell: bash
        run: |
          set -euo pipefail
          tag="${GITHUB_REF_NAME}"
          if gh release view "$tag" >/dev/null 2>&1; then
            gh release upload "$tag" "${RUNNER_TEMP}"/book-dist/*.epub "${RUNNER_TEMP}"/book-dist/*.pdf "${RUNNER_TEMP}"/book-dist/SHA256SUMS.txt --clobber
          else
            gh release create "$tag" "${RUNNER_TEMP}"/book-dist/*.epub "${RUNNER_TEMP}"/book-dist/*.pdf "${RUNNER_TEMP}"/book-dist/SHA256SUMS.txt --title "$tag" --generate-notes
          fi
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

## Obligatoriskt projektbeteende

- Välj exakt en indata-zip för varje filbaserad ändring.
- Verifiera före ändring och verifiera den färdiga leveranszipen igen.
- Ändra endast uttryckligen tillåtna filer; skydda övriga kapitelfiler.
- Leverera monoton revision och revisionskvittens.
