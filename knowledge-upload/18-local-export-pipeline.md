# Lokal export och GitHub-publicering

Nya projekt innehåller en gemensam lokal/CI-pipeline. `book.yaml` är enda kanoniska metadatafilen.

## Scripts
- `scripts/validate_project.py`: snabb deterministisk CI-validering och integritetskontroll.
- `scripts/export-book.py`: enda kanoniska exportmotor för EPUB/PDF.
- `scripts/build_book.py`: tunn CI-wrapper som validerar, bygger båda formaten och skriver SHA256SUMS.

## Publishing
`publishing/` innehåller EPUB-CSS, EPUB-efterbearbetning, XeLaTeX-template, Lua-filter och build-noteringar. Pandoc 3.1.11.1 används i GitHub Actions.

## GitHub Actions
- `01-validate.yml`: PR/push till `main`, utan tung verktygsinstallation.
- `02-build-preview.yml`: manuell preview; ett artifact innehåller EPUB + PDF + SHA256SUMS.
- `03-release.yml`: `v<SemVer>`-tagg; skapar/uppdaterar GitHub Release och bifogar EPUB/PDF som separata assets.

## Krav
- Exporten följer exakt `book.yaml: chapters`.
- Saknade, dubbellistade eller olistade numrerade kapitelfiler stoppar export.
- `docs/` exporteras aldrig som boktext.
- EPUB har navigerbar TOC men ingen vanlig TOC-sida i läsflödet.
- PDF har omslag om angivet, separat titelsida och synlig klickbar innehållsförteckning.
- Samma pipeline gäller `textbook` och `factbook`.
