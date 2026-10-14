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
