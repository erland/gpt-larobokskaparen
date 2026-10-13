# Lärobokskaparen GPT

Lärobokskaparen är en portabel GPT-assistent för att planera, skriva, underhålla och exportera **läroböcker** och **faktaböcker**. Samma projektformat används för båda profilerna, medan planering, kapitelstruktur och kvalitetskontroll anpassas efter bokens syfte.

Repositoryt har ingen incheckad versionsfil. En publicerad GitHub Release-tagg `v<SemVer>` är auktoritativ versionskälla; lokala/testbyggen använder explicit `--version`.

## Bokprofiler

- `textbook`: pedagogisk progression, lärandemål, exempel och vid behov övningar/kunskapskontroll.
- `factbook`: ämnestäckning, faktadjup, begriplighet, källpolicy och faktakontroll utan krav på övningsprogression.

`book_kind` väljer huvudprofil och `book_type` väljer underform inom profilen.

## Installation och användning

Aktiva distributioner är Chat ZIP, ChatGPT Plugin, Claude Project, Claude Skills och OpenCode. Custom GPT är inte längre ett aktivt distributionsmål.

För Chat ZIP: bifoga distributionens ZIP-fil i en ny ChatGPT-konversation och läs `START-HERE.md`. För övriga plattformar används respektive distributions README och runtimekontrakt.

**Kanoniska instruktioner:** `canonical/core.md` tillsammans med `canonical/skills/**/behavior.md`. Den äldre `gpt-configuration/instructions.md` behålls som källreferens för migreringsjämförelser.

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

Bygg och validering styrs av `gpt-project.yaml`. Projektet levererar sex ZIP-filer: projektpaketet samt dessa fem aktiva runtimepaket:

- `larobokskaparen-chat-<version>.zip`
- `larobokskaparen-plugin-<version>.zip`
- `larobokskaparen-claude-project-<version>.zip`
- `larobokskaparen-claude-skills-<version>.zip`
- `larobokskaparen-opencode-<version>.zip`

## Byggarverktyg respektive bokprojektverktyg

Repositoryts `scripts/build_distributions.py`, `scripts/validate_distributions.py` och `scripts/lint_gpt_project.py` körs **i GPT-projektets rot** för att bygga och kontrollera distributionspaket.

Den kanoniska bokprojektmallen finns däremot i `templates/bokprojekt/`. Dess egna `scripts/project_integrity.py`, `scripts/validate_project.py`, `scripts/export-book.py` och `scripts/build_book.py` följer med nya bokprojekt och körs **i respektive bokprojekts rot**. Repositoryts generiska `scripts/` får inte förväxlas med mallens bokprojektsverktyg.

### Lokalt distributionsbygge

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/lint_gpt_project.py --project-root . --json
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_distributions.py --version 0.6.3
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_distributions.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_release_assets.py --version 0.6.3
```

### GitHub Release

En publicerad tagg `v<SemVer>` utlöser distributionsbygge, verifiering av checksumma och uppladdning av aktiva assets. PR-körningar använder automatiskt en utvecklingsversion.

## Portabel användning

Bifoga `larobokskaparen-chat-vX.Y.Z.zip` i en ny konversation och skriv exempelvis:

> Använd Lärobokskaparen i den bifogade ZIP-filen för den här konversationen. Läs `START-HERE.md` först.

## GitHub-publicering i genererade bokprojekt

Projektmallen innehåller från början Validate, Build Preview och Release samt reproducerbar EPUB/PDF-export med Pandoc 3.1.11.1 + XeLaTeX. Därmed behöver publiceringsstödet inte eftermonteras i varje ny bok.


## Migreringsunderlag

Se `MIGRATION.md` och `MIGRATION-VALIDATION.md` för moderniseringen enligt GPT Byggaren v1.6.22.
