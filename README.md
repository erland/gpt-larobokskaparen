# Lärobokskaparen GPT

Lärobokskaparen är en Custom GPT-konfiguration för att planera, skriva, underhålla och exportera **läroböcker** och **faktaböcker**. Samma projektformat används för båda profilerna, medan planering, kapitelstruktur och kvalitetskontroll anpassas efter bokens syfte.

Repositoryt har ingen incheckad versionsfil. En publicerad GitHub Release-tagg `v<SemVer>` är auktoritativ versionskälla; lokala/testbyggen använder explicit `--version`.

## Bokprofiler

- `textbook`: pedagogisk progression, lärandemål, exempel och vid behov övningar/kunskapskontroll.
- `factbook`: ämnestäckning, faktadjup, begriplighet, källpolicy och faktakontroll utan krav på övningsprogression.

`book_kind` väljer huvudprofil och `book_type` väljer underform inom profilen.

## Installation som Custom GPT

1. Kopiera `gpt-configuration/instructions.md` till GPT:ns Instructions.
2. Lägg in `gpt-configuration/conversation-starters.md` som conversation starters.
3. Ladda upp alla Markdown-filer i `knowledge-upload/` som Knowledge.
4. Aktivera vid behov Web Browsing, Code Interpreter/Data Analysis och Image Generation.

Byggvalideringen stoppar om Instructions överstiger 8 000 tecken eller om Knowledge-filerna överstiger Custom GPT-gränsen på 20.

## Kanonisk projektmodell

`templates/bokprojekt/` är single source of truth för nya bokprojekt. `knowledge-upload/19-project-template-bundle.md` genereras från denna katalog och ska aldrig redigeras manuellt.

Viktiga principer:

- `book.yaml` är enda kanoniska bokmetadatafilen.
- `book.yaml: chapters` är bindande exportordning.
- Boktext ligger under `chapters/`; arbetsmaterial ligger under `docs/`.
- Lärobok och faktabok har separata kapitelmallar men samma projektstruktur.
- `docs/kallpolicy.md` och `docs/faktakontroll.md` håller källarbete utanför boktexten.
- `project-manifest.json`, `revision-log.md` och `scripts/project_integrity.py` ger revisions- och SHA-256-skydd.
- Två olika filer får inte representera samma kapitelnummer.
- Befintliga äldre projekt bevaras om de fungerar och migreras bara när det behövs.

Ett typiskt projekt ser ut så här:

```text
<bokslug>-projekt/
  README.md
  book.yaml
  project-manifest.json
  revision-log.md
  project-index.md
  docs/
  chapters/
  exercises/
  examples/
  code/
  assets/
  publishing/
  scripts/
  .github/workflows/
  exports/
```

Se `examples/sample-book-project-structure.md` för en kompakt vy och `knowledge-upload/19-project-template-bundle.md` för exakt mallinnehåll.

## Export

Nya projekt innehåller en reproducerbar lokal exportpipeline:

```bash
python3 scripts/export-book.py --format all
```

Pandoc används som standard när det finns. Exportscriptet läser kapitel **i exakt den ordning som anges i `book.yaml`** och stoppar vid saknade, dubbellistade eller olistade numrerade kapitelfiler.

- EPUB: navigerbar EPUB-TOC men ingen synlig TOC-sida i läsflödet.
- PDF: innehållsförteckning före inledningen.
- Arbetsfiler under `docs/` ska aldrig följa med av misstag.

## Distributioner

Repositoryt bygger två ZIP-paket från samma källor:

- `larobokskaparen-custom-gpt-vX.Y.Z.zip` – för installation/uppdatering av Custom GPT.
- `larobokskaparen-chat-vX.Y.Z.zip` – portabel version för en vanlig ChatGPT-konversation.

Den portabla distributionen innehåller:

```text
START-HERE.md
VERSION
MANIFEST.json
assistant/instructions.md
knowledge/
templates/bokprojekt/
examples/
```

Instructions, Knowledge-filer och den portabla projektmallen verifieras byte-identiskt mot repositoryts källfiler.

### Lokal build

Eftersom repositoryt saknar incheckad version anges version explicit om committen inte är exakt taggad:

```bash
python3 scripts/build_distributions.py --version 1.4.0
python3 scripts/validate_distributions.py --version 1.4.0
```

På en exakt `v<SemVer>`-tagg kan buildscriptet även läsa versionen från Git. Distributionernas `VERSION`-fil genereras vid build och är inte källan till versionen.

### GitHub Release

Release-taggen är versionskälla och ska följa `v<SemVer>`, till exempel `v1.4.0`. Workflowet bygger och validerar båda distributionerna med taggens version och bifogar dem som release-assets.

## Portabel användning

Bifoga `larobokskaparen-chat-vX.Y.Z.zip` i en ny konversation och skriv exempelvis:

> Använd Lärobokskaparen i den bifogade ZIP-filen för den här konversationen. Läs `START-HERE.md` först.

## GitHub-publicering i genererade bokprojekt

Projektmallen innehåller från början Validate, Build Preview och Release samt reproducerbar EPUB/PDF-export med Pandoc 3.1.11.1 + XeLaTeX. Därmed behöver publiceringsstödet inte eftermonteras i varje ny bok.
