# Lokal exportpipeline för bokprojekt

Syfte: varje bokprojekt ska kunna exporteras till EPUB och PDF lokalt utan AI. GPT:n ska generera manus, metadata och projektstruktur, men exporten ska vara reproducerbar med scripts och styles som följer med projekt-zippen.

## När pipeline ska skapas
- Nya bokprojekt: inkludera alltid `scripts/`, `styles/` och `exports/` när kapitelproduktion börjar.
- Befintliga projekt-zippar: om användaren ber om exportstöd, komplettera zippen med saknade exportfiler utan att skriva om manus i onödan.
- Om projektet redan har exportscript: uppdatera varsamt och bevara lokala anpassningar om de inte strider mot renderkontraktet.

## Standardfiler i bokprojekt

```text
scripts/export-book.py
scripts/export-book.sh
styles/epub.css
styles/pdf.css
exports/
```

## Rekommenderad lokal verktygskedja
Standard: Pandoc.

För PDF kan scriptet använda:
1. Pandoc + valfri installerad PDF-engine, eller
2. Pandoc till HTML + CSS och därefter användarens lokala HTML→PDF-verktyg om tillgängligt.

Scriptet ska vara tydligt med vad som saknas om Pandoc eller PDF-engine inte är installerad.

## Validering före export
Scriptet ska stoppa eller varna vid:
- saknad `book.yaml` eller `docs/export-metadata.yaml`,
- saknad titel, författare eller språk,
- kapitel som inte följer ordningen `00-inledning.md`, `*-01.md`, `*-02.md`,
- H4 eller djupare rubriker (`####`),
- tabeller utan separatorrad,
- tabellrader med olika antal celler,
- bildreferenser till filer som saknas,
- rå markdown som sannolikt kommer synas i exporten.

## EPUB-regler
- Ingen innehållsförteckning som kapitel i dokumentflödet.
- Använd navigerbar TOC om verktyget genererar det.
- Använd `styles/epub.css`.
- Luftig layout: generöst radavstånd, marginaler, avstånd efter stycken, tydliga rubriker.
- Bilder ska skalas responsivt och inte spränga sidbredd.

## PDF-regler
- PDF ska ha innehållsförteckning före första kapitel/inledning.
- Använd `styles/pdf.css` eller motsvarande PDF-layout.
- Tydliga sidmarginaler, läsbart radavstånd, sidbrytning före kapitel.
- Tabeller ska vara läsbara och inte komprimeras för hårt.

## Mall för export-book.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/export-book.py "$@"
```

## Mallprinciper för export-book.py
Python-scriptet bör:
- hitta projektroten,
- läsa metadata från `book.yaml` och/eller `docs/export-metadata.yaml`,
- samla kapitel i korrekt ordning,
- validera markdown,
- skapa temporär sammanslagen markdown,
- köra Pandoc för EPUB och PDF,
- skriva filer till `exports/`,
- ge tydliga felmeddelanden och installationsråd.

## Minimal Pandoc-kommandostruktur

EPUB:

```bash
pandoc build/book.md \
  --from=gfm \
  --to=epub3 \
  --metadata title="..." \
  --metadata author="..." \
  --metadata lang="sv-SE" \
  --css=styles/epub.css \
  --output=exports/book.epub
```

PDF:

```bash
pandoc build/book.md \
  --from=gfm \
  --pdf-engine=xelatex \
  --toc \
  --toc-depth=3 \
  --metadata title="..." \
  --metadata author="..." \
  --metadata lang="sv-SE" \
  --output=exports/book.pdf
```

Om xelatex saknas ska scriptet ge tydligt besked och föreslå installation av MacTeX/TinyTeX eller annan Pandoc-kompatibel PDF-engine.

## CSS-principer
EPUB CSS ska prioritera läsbarhet:
- `line-height` cirka 1.55–1.7,
- tydligt avstånd mellan stycken,
- luftiga rubriker,
- listor med marginaler och fungerande nested lists,
- kodblock med bakgrund och padding,
- tabeller med cellpadding och kantlinjer.

PDF CSS/layout ska prioritera:
- tydliga sidmarginaler,
- rubrikhierarki,
- sidbrytning före H1,
- tabeller med läsbar cellpadding,
- bildtexter och bilder som håller sig inom sidbredd.
