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

## Kodgenererade diagram
För Graphviz, PlantUML och handgjord SVG: spara källan under `assets/diagrams/IMG-NN-MM.dot|puml|svg` och kör `python scripts/render_diagrams.py` för att generera SVG i `assets/generated/`. Validera med `python scripts/render_diagrams.py --check`. För PlantUML kan `--plantuml-jar /sökväg/plantuml.jar` eller `PLANTUML_JAR` användas. Om PlantUML saknas: https://github.com/plantuml/plantuml/releases . Uppdatera projektets integritetsmanifest enligt revisionsflödet efter diagramändringar.
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
pdf_size: "170x240" # 170x240 | a5
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

## Gemensamt referensregister
- Använd bokövergripande käll-ID som `K001`, `K002` osv. Ett ID ska betyda samma källa i hela boken.
- Placera ett gemensamt register sist i boken och lista det i `book.yaml`; exempelvis `chapters/99-kallregister.md`.
- Formatera poster som `- **[K001]** Organisation, titel, datum. https://...` och hänvisa med `[K001]` i kapiteltext.
- Projektvalideringen flaggar saknade och dubblerade käll-ID. Kort, klickbar länktext föredras framför utskrivna långa adresser.
- Källreservationen ska vända sig till läsaren: ange tidsavgränsning och att analysen är författarens tolkning. Låt redaktionella instruktioner ligga kvar i `docs/`.
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

Kodgenererade diagram stöds via `assets/diagrams/IMG-NN-MM.dot`, `.puml` eller `.svg`.
Kör `python scripts/render_diagrams.py` före revisionsuppdatering och kontrollera `assets/generated/IMG-NN-MM.svg`.
Registrera diagrammets teknik, källfil, SVG, alt-text, bildtext och granskningsstatus. Befintliga PNG-bilder och prompts fungerar som förut.
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
- Release triggas av `v<SemVer>` och publicerar EPUB/PDF som separata release-assets. Release-taggen bestämmer den publicerade bokversionen (exempelvis `v0.5.2` → `0.5.2`) genom temporära exportmetadata. `book.yaml` ändras inte och får ha ett annat versionsnummer. Förhandsbyggen utan release-tagg använder `book.yaml`-versionen.

Arbetsfiler i `docs/` exporteras aldrig som boktext.

## Bokövergripande källhänvisningar
Om boken har ett källregister under `chapters/` (t.ex. `17-kallor.md` eller `99-kallregister.md`) används poster på formen `- **[K001]** Organisation, titel. https://example.org`. Hänvisa till samma ID från valfritt kapitel med `[K001]`. Exporten skapar automatiskt interna PDF-/EPUB-länkar från hänvisningen till källposten, där originaladressen visas med den korta länktexten "Öppna källan". Källregistrering är valfri för böcker som inte använder Kxxx-hänvisningar; om ID används måste det finnas i registret.

## Layout och publiceringskontroller
`pdf_size: "170x240"` i `book.yaml` väljer standardformat 170 × 240 mm; `pdf_size: "a5"` väljer A5 (148 × 210 mm). Endast dessa två profiler stöds. EPUB är fortsatt omflödesbar enligt läsarens egna typsnittsinställningar.

`python3 scripts/build_book.py --output-dir exports` genererar båda formaten, testar ZIP-struktur, EPUB-navigation, manifest, spine och interna EPUB-länk- och ankarmål, samt att PDF har sidor och extraherbar text. Bygget avbryts vid fel och kontrollsummor skrivs först när filerna godkänts. PDF-kontrollen kräver även `pdfinfo` och `pdftotext` från Poppler; installera `poppler-utils` vid lokal export. Den automatiska kontrollen ersätter inte en visuell granskning av PDF/EPUB i en faktisk läsare.
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
}
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
    count=0; pat=re.compile(r'^\\s*(\\d+)\\.\\s+(.+?)\\s*$')
    for path in base.rglob('*.xhtml'):
        tree=ET.parse(path); changed=False
        for h1 in tree.getroot().findall('.//x:h1',NS):
            text=''.join(h1.itertext()).strip()
            m=pat.match(text) or re.match(r'^\\s*Kapitel\\s+(\\d+):\\s*(.+?)\\s*$',text,re.I)
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

````latex
\documentclass[11pt,openany]{book}
\usepackage{fontspec}
\defaultfontfeatures{Ligatures=TeX}
$if(pdf-font-dir)$
\setmainfont[Path=$pdf-font-dir$/,Extension=.otf,UprightFont=texgyrepagella-regular,BoldFont=texgyrepagella-bold,ItalicFont=texgyrepagella-italic,BoldItalicFont=texgyrepagella-bolditalic]{texgyrepagella}
$else$
\setmainfont{TeXGyrePagella}
$endif$
\usepackage[paperwidth=$if(bookpaperwidth)$bookpaperwidth$else$170mm$endif$,paperheight=$if(bookpaperheight)$bookpaperheight$else$240mm$endif$,inner=20mm,outer=18mm,top=20mm,bottom=22mm,headsep=5mm,footskip=9mm]{geometry}
\usepackage{graphicx}\usepackage{microtype}\usepackage{setspace}\usepackage{parskip}\usepackage{fancyhdr}\usepackage[hidelinks]{hyperref}\usepackage{bookmark}\usepackage{tocloft}\usepackage{ragged2e}\usepackage{xcolor}\usepackage{longtable}\usepackage{booktabs}\usepackage{array}\usepackage{calc}\usepackage{etoolbox}
\hypersetup{pdfkeywords={Version $version$}}
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

````lua
-- PDF: numrerade H1 får kompakt tvådelad kapitelstart; övriga H1 (t.ex. Inledning) blir onumrerade kapitel.
function Header(el)
  if el.level ~= 1 then return nil end
  local text = pandoc.utils.stringify(el.content)
  local number, title = text:match("^%s*(%d+)%.%s+(.+)%s*$")
  if not number then number, title = text:match("^%s*[Kk]apitel%s+(%d+):%s*(.+)%s*$") end
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
````

## `scripts/export-book.py`

````python
#!/usr/bin/env python3
from __future__ import annotations
import argparse, os, re, shutil, subprocess, tempfile, sys
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
    keys=('title','subtitle','author','language','identifier','date','version','book_kind','book_type','cover_image','project_slug','subject','description','pdf_size')
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
    if not re.search(r'inledning|introduktion|preface|foreword',Path(entries[0]).stem,re.I): raise SystemExit('Första posten bör vara en inledning (filnamn med inledning/introduktion)')
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
        if not p.name.startswith('kapitelmall-') and p.relative_to(ROOT).as_posix() not in listed: unlisted.append(p.relative_to(ROOT).as_posix())
    if unlisted: raise SystemExit('Markdownfiler saknas i book.yaml: '+', '.join(unlisted))
    return paths
def validate_markdown(paths):
    errors=[]
    for p in paths:
        t=p.read_text(encoding='utf-8')
        if re.search(r'(?m)^#{4,}\s',t): errors.append(p.name+': H4 eller djupare rubrik')
        if t.count('```')%2: errors.append(p.name+': obalanserade kodblock')
    if errors: raise SystemExit('Markdown-validering misslyckades:\n- '+'\n- '.join(errors))
def image_transform_for(fmt, workdir):
    """Resolve image references per source chapter. Convert SVG to PDF only for XeLaTeX."""
    def transform(text, chapter):
        def replace(match):
            alt, raw=match.group(1), match.group(2)
            ref=raw.strip().split()[0].strip('<>')
            if ref.startswith(('http://','https://','#')): return match.group(0)
            src=(chapter.parent/ref).resolve()
            try: src.relative_to(ROOT.resolve())
            except ValueError: raise SystemExit('Bildreferens utanför projektet: '+ref)
            if not src.is_file(): raise SystemExit('Bildfil saknas: '+str(src))
            if src.suffix.lower()=='.svg' and fmt=='pdf':
                target=workdir/(src.stem+'-'+str(len(list(workdir.glob('*.pdf'))))+'.pdf')
                if shutil.which('inkscape'):
                    subprocess.run(['inkscape',str(src),'--export-type=pdf','--export-filename='+str(target)],check=True,timeout=90,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                else:
                    try: import cairosvg
                    except ImportError: raise SystemExit('SVG till vektor-PDF kräver Inkscape eller CairoSVG')
                    cairosvg.svg2pdf(url=str(src),write_to=str(target))
                resolved=target
            else: resolved=src
            return '!['+alt+']('+resolved.as_posix()+')'
        return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',replace,text)
    return transform

def run(cmd): print('+',' '.join(map(str,cmd))); subprocess.run(cmd,cwd=ROOT,check=True)
def find_font_dir():
    for base in (Path('/usr/share/fonts'),Path('/usr/local/share/fonts')):
        if base.exists():
            for p in base.rglob('texgyrepagella-regular.otf'):
                names=['texgyrepagella-regular.otf','texgyrepagella-bold.otf','texgyrepagella-italic.otf','texgyrepagella-bolditalic.otf']
                if all((p.parent/n).is_file() for n in names): return p.parent
    return None
PDF_SIZES = {'170x240': ('170mm', '240mm'), 'a5': ('148mm', '210mm')}

def pdf_size(meta):
    requested=meta.get('pdf_size', '').lower() or '170x240'
    if requested not in PDF_SIZES:
        raise SystemExit('pdf_size ska vara a5 eller 170x240')
    return PDF_SIZES[requested]

def export_metadata(text, tag):
    if not tag: return text
    if not re.fullmatch('v[0-9]+[.][0-9]+[.][0-9]+', tag):
        raise SystemExit('Ogiltig releasetagg')
    line = 'version: "' + tag[1:] + '"'
    rows = text.splitlines()
    for i, value in enumerate(rows):
        if value.startswith('version:'):
            rows[i] = line
            break
    else:
        rows.insert(0, line)
    return chr(10).join(rows) + chr(10)

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--format',choices=['epub','pdf','all'],default='all'); ap.add_argument('--output-dir',default=str(ROOT/'exports')); args=ap.parse_args()
    if not shutil.which('pandoc'): raise SystemExit('Pandoc saknas')
    text=read_book_yaml(); meta=metadata(text); chapters=resolve_chapters(text); validate_markdown(chapters)
    effective_yaml=export_metadata(text,os.environ.get('BOOK_RELEASE_TAG'))
    out=Path(args.output_dir).resolve(); out.mkdir(parents=True,exist_ok=True); slug=meta['project_slug']
    with tempfile.TemporaryDirectory() as td:
        td=Path(td); metadata_path=td/'book-metadata.yaml'; metadata_path.write_text(effective_yaml,encoding='utf-8'); from book_references import prepare
        merged=td/'book.md'
        common=['pandoc',str(merged),'--from=markdown+pipe_tables+fenced_code_blocks+fenced_divs','--standalone','--metadata-file',str(metadata_path)]
        if args.format in ('epub','all'):
            merged.write_text(prepare(chapters,image_transform=image_transform_for('epub',td)),encoding='utf-8')
            epub=out/f'{slug}.epub'
            cmd=['pandoc',str(merged),'--from=markdown+pipe_tables+fenced_code_blocks+fenced_divs','--to=epub3','--standalone','--toc','--toc-depth=1','--metadata-file',str(metadata_path),'--css',str(ROOT/'publishing/epub.css')]
            cover=meta['cover_image'];
            if cover:
                cp=ROOT/cover
                if not cp.is_file(): raise SystemExit('Angiven omslagsbild saknas: '+cover)
                cmd += ['--epub-cover-image',str(cp)]
            run(cmd+['--output',str(epub)]); run([sys.executable,str(ROOT/'publishing/fix-epub-after-pandoc.py'),str(epub)])
        if args.format in ('pdf','all'):
            merged.write_text(prepare(chapters,image_transform=image_transform_for('pdf',td)),encoding='utf-8')
            if not shutil.which('xelatex'): raise SystemExit('XeLaTeX saknas för PDF-export')
            width,height=pdf_size(meta)
            pdf=out/f'{slug}.pdf'; cmd=common+['--variable',f'bookpaperwidth={width}','--variable',f'bookpaperheight={height}','--top-level-division=chapter','--pdf-engine=xelatex','--template',str(ROOT/'publishing/pdf-template.tex'),'--lua-filter',str(ROOT/'publishing/pdf-filter.lua')]
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
    subprocess.run([sys.executable,'scripts/validate_exports.py',str(next(p for p in files if p.suffix=='.epub')),str(next(p for p in files if p.suffix=='.pdf'))],cwd=ROOT,check=True)
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
          sudo apt-get install -y --no-install-recommends texlive-xetex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended lmodern fonts-texgyre poppler-utils
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
          sudo apt-get install -y --no-install-recommends texlive-xetex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended lmodern fonts-texgyre poppler-utils
          fc-cache -f
          find /usr/share/fonts -iname 'texgyrepagella-regular.otf' -print -quit | grep .
      - name: Validate release tag
        shell: bash
        run: |
          [[ "${GITHUB_REF_NAME}" =~ ^v[0-9]+\.[0-9]+\.[0-9]+([+-][0-9A-Za-z.-]+)?$ ]] || { echo "Taggen måste vara v<SemVer>" >&2; exit 1; }
      - name: Build EPUB and PDF
        env:
          BOOK_RELEASE_TAG: ${{ github.ref_name }}
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

## `scripts/render_diagrams.py`

````python
#!/usr/bin/env python3
"""Render and check book diagram sources. No network dependencies."""
from __future__ import annotations
import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"assets"/"diagrams"
OUTPUT=ROOT/"assets"/"generated"
SVG_NS="{http://www.w3.org/2000/svg}"
PROHIBITED={"script","foreignObject","iframe","object","embed","image","use","animate","set"}
EXTERNAL=re.compile(r"(?:https?:|file:|data:|javascript:|//)",re.I)

def check_svg(path:Path)->None:
    if not path.is_file() or path.stat().st_size==0:
        raise ValueError(f"SVG saknas eller är tom: {path}")
    data=path.read_text(encoding="utf-8")
    if "<!DOCTYPE" in data.upper() or "<!ENTITY" in data.upper():
        raise ValueError(f"DOCTYPE/ENTITY tillåts inte: {path.name}")
    tree=ET.fromstring(data)
    if tree.tag not in (SVG_NS+"svg","svg"):
        raise ValueError(f"Roten måste vara svg: {path.name}")
    if len(list(tree.iter()))<2:
        raise ValueError(f"SVG innehåller ingen synlig grafik: {path.name}")
    for el in tree.iter():
        local=el.tag.split("}")[-1]
        if local in PROHIBITED:
            raise ValueError(f"Otillåtet SVG-element {local}: {path.name}")
        for key,value in el.attrib.items():
            attr=key.split("}")[-1].lower()
            if attr.startswith("on") or attr in ("href","src") and value.strip() or EXTERNAL.search(value):
                raise ValueError(f"Osäker SVG-referens/attribut i {path.name}: {key}")

def render_one(source:Path, jar:Path|None)->Path:
    target=OUTPUT/(source.stem+".svg")
    OUTPUT.mkdir(parents=True,exist_ok=True)
    if source.suffix==".svg":
        check_svg(source)
        shutil.copyfile(source,target)
    elif source.suffix==".dot":
        dot=shutil.which("dot")
        if not dot: raise RuntimeError("Graphviz saknas: dot hittades inte")
        with target.open("wb") as f:
            subprocess.run([dot,"-Tsvg","-Gbgcolor=white",str(source)],stdout=f,check=True,timeout=60)
    else:
        exe=shutil.which("plantuml")
        if jar:
            if not jar.is_file(): raise RuntimeError(f"PlantUML JAR saknas: {jar}")
            java=shutil.which("java")
            if not java: raise RuntimeError("Java saknas för PlantUML JAR")
            cmd=[java,"-Djava.awt.headless=true","-jar",str(jar),"-tsvg","-pipe"]
        elif exe: cmd=[exe,"-tsvg","-pipe"]
        else:
            raise RuntimeError("PlantUML saknas. Hämta officiell JAR från https://github.com/plantuml/plantuml/releases och bifoga filen.")
        with target.open("wb") as out:
            raw=source.read_text(encoding="utf-8")
            # Keep white background explicit even when a different renderer theme is active.
            if "@startuml" in raw and not re.search(r"(?im)^\s*skinparam\s+backgroundColor\b",raw):
                raw=raw.replace("@startuml","@startuml\nskinparam backgroundColor white",1)
            subprocess.run(cmd,input=raw.encode("utf-8"),stdout=out,check=True,timeout=90)
    # Graphviz/PlantUML kan skriva en SVG 1.1-DOCTYPE. Ta bort den lokalt,
    # så att slutartefakten blir fristående och passerar säkerhetsvalideringen.
    if source.suffix in (".dot",".puml"):
        data=target.read_text(encoding="utf-8")
        data=re.sub(r'<!DOCTYPE[\s\S]*?>', '', data, count=1)
        target.write_text(data,encoding="utf-8")
    check_svg(target)
    return target

def sources()->list[Path]:
    if not SOURCE.exists(): return []
    files=sorted(p for p in SOURCE.iterdir() if p.is_file() and p.suffix.lower() in {".dot",".puml",".svg"})
    ids={}
    for p in files:
        if not re.fullmatch(r"IMG-\d{2}-\d{2}",p.stem):
            raise ValueError(f"Ogiltigt diagram-ID: {p.name}")
        if p.stem in ids: raise ValueError(f"Duplicerat diagram-ID: {p.stem}")
        ids[p.stem]=p
    return files

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",action="store_true",help="Validera redan genererade SVG, utan att ändra filer")
    ap.add_argument("--plantuml-jar",type=Path,default=Path(os.environ["PLANTUML_JAR"]) if os.environ.get("PLANTUML_JAR") else None)
    args=ap.parse_args()
    try:
        files=sources()
        for source in files:
            target=OUTPUT/(source.stem+".svg")
            if args.check: check_svg(target)
            else:
                try: render_one(source,args.plantuml_jar)
                except Exception:
                    target.unlink(missing_ok=True)
                    raise
            print(f"OK {source.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        print(f"Godkända diagram: {len(files)}")
        return 0
    except (ValueError,ET.ParseError,RuntimeError,subprocess.SubprocessError,OSError) as exc:
        print(f"Diagramfel: {exc}",file=sys.stderr)
        return 1

if __name__=="__main__": raise SystemExit(main())
````


## `scripts/book_references.py`

````python
#!/usr/bin/env python3
"""Prepare book-global source navigation without modifying original Markdown."""
from __future__ import annotations
import re
from pathlib import Path

ENTRY = re.compile(r'(?m)^(\s*[-*]\s*)\*\*\[(K\d{3})\]\*\*')
REF = re.compile(r'(?<![\w\[])\[(K\d{3})\](?!\(|\])')
URL = re.compile(r'(?<!\]\()https?://[^\s<>)]+')


def prepare(chapters: list[Path], image_transform=None) -> str:
    texts = [path.read_text(encoding='utf-8').strip() for path in chapters]
    if image_transform is not None:
        texts = [image_transform(text, path) for text, path in zip(texts, chapters)]
    registers = [i for i, p in enumerate(chapters)
                 if 'kall' in p.name.lower() or 'käll' in p.name.lower()]
    ids = set()
    for index in registers:
        for match in ENTRY.finditer(texts[index]):
            code = match.group(2)
            if code in ids:
                raise ValueError(f'Dubbelt käll-ID: {code}')
            ids.add(code)
    output = []
    for index, chapter in enumerate(texts):
        if index in registers:
            # The source entry becomes an anchor target; all other occurrences
            # of Kxxx become internal links rather than their own targets.
            chapter = ENTRY.sub(
                lambda m: m.group(1) + '[]{#' + m.group(2).lower() + '} **['
                + m.group(2) + ']**', chapter)
            chapter = URL.sub(lambda m: '[Öppna källan](' + m.group(0) + ')', chapter)
        else:
            def resolve(match):
                code = match.group(1)
                if code not in ids:
                    raise ValueError(f'Saknat käll-ID: {code}')
                return '[' + code + '](#' + code.lower() + ')'
            chapter = REF.sub(resolve, chapter)
        output.append(chapter)
    return '\n\n'.join(output) + '\n'
````

## `scripts/validate_exports.py`

````python
#!/usr/bin/env python3
"""Structural publication checks on the actual EPUB and PDF artifacts."""
from __future__ import annotations
import posixpath
import subprocess
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET

OPF = '{http://www.idpf.org/2007/opf}'
XHTML = '{http://www.w3.org/1999/xhtml}'
CONTAINER = '{urn:oasis:names:tc:opendocument:xmlns:container}'


def check_epub(path: Path) -> dict[str, int]:
    with zipfile.ZipFile(path) as z:
        if z.testzip() is not None:
            raise ValueError('EPUB ZIP CRC-fel')
        names = set(z.namelist())
        if z.namelist()[0] != 'mimetype' or z.getinfo('mimetype').compress_type != 0:
            raise ValueError('EPUB mimetype saknas eller är komprimerad')
        root = ET.fromstring(z.read('META-INF/container.xml'))
        ref = root.find('.//' + CONTAINER + 'rootfile')
        if ref is None:
            raise ValueError('EPUB saknar OPF-rootfile')
        opfpath = ref.attrib['full-path']
        package = ET.fromstring(z.read(opfpath))
        manifest = package.find(OPF + 'manifest')
        spine = package.find(OPF + 'spine')
        if manifest is None or spine is None:
            raise ValueError('EPUB saknar manifest eller spine')
        items = {item.attrib['id']: item for item in manifest.findall(OPF + 'item')}
        navigations = [i for i in items.values()
                       if 'nav' in i.attrib.get('properties', '').split()]
        if len(navigations) != 1:
            raise ValueError('EPUB behöver exakt ett navigeringsdokument')
        nav_ids = {i.attrib['id'] for i in navigations}
        if not all(item.attrib.get('linear') == 'no' for item in spine.findall(OPF+'itemref')
                   if item.attrib.get('idref') in nav_ids):
            raise ValueError('Navigeringsdokumentet får inte visas som lässida')
        for item in spine.findall(OPF + 'itemref'):
            if item.attrib['idref'] not in items:
                raise ValueError('Spine refererar till saknad manifest-post')
        parsed = {}
        for name in names:
            if name.endswith(('.xhtml', '.html')):
                parsed[name] = ET.fromstring(z.read(name))
        if not parsed:
            raise ValueError('EPUB saknar XHTML')
        anchors = {name: {node.attrib['id'] for node in tree.iter() if 'id' in node.attrib}
                   for name, tree in parsed.items()}
        checked = 0
        for name, tree in parsed.items():
            for node in tree.iter():
                href = node.attrib.get('href', '')
                if not href or href.startswith(('https:', 'http:', 'mailto:', 'tel:')):
                    continue
                parts = urlsplit(href)
                if parts.scheme:
                    continue
                target = posixpath.normpath(posixpath.join(posixpath.dirname(name),
                                                          unquote(parts.path))) if parts.path else name
                if target not in names:
                    raise ValueError(f'EPUB-länk utan mål: {name} → {href}')
                if parts.fragment and target in anchors and unquote(parts.fragment) not in anchors[target]:
                    raise ValueError(f'EPUB-ankare saknas: {name} → {href}')
                checked += 1
        return {'xhtml': len(parsed), 'internal_links': checked}


def check_pdf(path: Path) -> int:
    result = subprocess.run(['pdfinfo', str(path)], capture_output=True, text=True,
                            check=True)
    pages = next((int(line.split(':', 1)[1].strip())
                  for line in result.stdout.splitlines() if line.startswith('Pages:')), 0)
    if pages < 1:
        raise ValueError('PDF saknar sidor')
    text = subprocess.run(['pdftotext', str(path), '-'], check=True,
                          capture_output=True, text=True).stdout
    if not text.strip():
        raise ValueError('PDF saknar extraherbar boktext')
    return pages


def main() -> int:
    if len(sys.argv) != 3:
        print('Använd: validate_exports.py book.epub book.pdf', file=sys.stderr)
        return 2
    epub, pdf = map(Path, sys.argv[1:])
    summary = check_epub(epub)
    pages = check_pdf(pdf)
    print(f"PASS: EPUB {summary['xhtml']} dokument, {summary['internal_links']} interna länkar; PDF {pages} sidor")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
````
