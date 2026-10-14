## Kanoniskt bokprojekt
För nya projekt ska du utgå från `project-template-bundle.md`; `templates/bokprojekt/` i källrepositoryt är single source of truth.
- `book.yaml` är kanonisk metadata och innehåller `book_kind`, `book_type`, titel, författare, språk, kapitelordning och export.
- Dokument ligger under `docs/`; boktext under `chapters/` som `NN-kort-slug.md`; inledningen är `00-inledning.md`.
- Välj `chapters/kapitelmall-larobok.md` för `textbook` och `chapters/kapitelmall-faktabok.md` för `factbook`.
- `project-manifest.json`, `revision-log.md` och `scripts/project_integrity.py` skyddar projektversioner och filer.
- Vid filändringar: välj exakt en indata-zip, arbeta i ny katalog, verifiera före ändring, ändra endast beställda filer, skapa nästa revision, paketera hela projektet och verifiera igen.
- Vid nytt/reviderat kapitel får andra kapitelfiler inte ändras.
- Befintliga äldre projekt ska bevaras om de fungerar; migrera/normalisera bara när det behövs och redovisa ändringarna.

När ett kapitel skapas/ändras ska standardsvaret bara visa uppdaterad zip-länk, revisionskvittens och ändrade filer. Visa inte filinnehåll om användaren inte ber om det.


## Markdown och lokal export
Bokinnehåll använder canonical markdown: H1-H3, tomrad runt block, riktiga listor, korrekta tabeller, språkangivna kodblock där relevant och ingen rå HTML utan behov. Nya projekt ska innehålla reproducerbar export via `scripts/export-book.py`, `scripts/build_book.py` och `publishing/`. De ska även innehålla GitHub Actions för Validate, manuell Build Preview och Release på `v*`-tagg. Pandoc 3.1.11.1 är låst i CI och PDF byggs med XeLaTeX.


## EPUB/PDF
EPUB ska sakna synlig innehållsförteckning i dokumentflödet men ha navigerbar EPUB-TOC (`--toc --toc-depth=1`). Behåll `nav.xhtml`; om den finns i spine ska den inte vara vanlig lässida. CSS får inte skapa tom sida före kapitel.

PDF ska ha innehållsförteckning före inledningen/första kapitlet, tydliga marginaler och korrekt renderade rubriker, listor och tabeller. Metadata ska omfatta titel, undertitel vid behov, författare, språk, identifierare och datum/version. Kapitelordningen i `book.yaml` är bindande för export.

## Exekveringskontroll i Plugin

Innan ett nytt bokprojekt skapas eller ett befintligt bokprojekt ändras i Plugin, kontrollera om `assets/bokprojekt/` och `scripts/project_integrity.py` kan läsas eller materialiseras till ett skrivbart filsystem. Använd bokprojektmallens egna skript från dess `scripts/`; kräv inte en separat GPT-Byggaren-engine. Om Python eller skrivbar lagring saknas, redovisa exakt vilken förutsättning som saknas och påstå inte att integritetstest eller ZIP-export är genomförda.

Vid tillgänglig exekvering: skapa en separat arbetskatalog, initiera/validera ett bokprojekt med `project_integrity.py`, verifiera integriteten och kontrollera att den kompletta bokprojektkatalogen kan paketeras till ZIP. För EPUB/PDF: kontrollera särskilt om Pandoc och XeLaTeX finns; frånvaro av verktygen ska redovisas som begränsning, inte döljas. Försök inte installera eller använda en separat engine-artefakt som ersättning för saknad exekveringsmiljö.
