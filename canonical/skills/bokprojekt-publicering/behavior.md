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

Vid tillgänglig exekvering: skapa en separat arbetskatalog, initiera/validera ett bokprojekt med `project_integrity.py`, verifiera integriteten och kontrollera att den kompletta bokprojektkatalogen kan paketeras till ZIP. För EPUB/PDF: kontrollera särskilt om Pandoc och XeLaTeX finns; frånvaro av verktygen ska redovisas som begränsning, inte döljas. Engine ZIP ersätter aldrig en saknad exekveringsmiljö, men används som versionsmatchad fallback när de installerade resurserna kan läsas men inte materialiseras.


### Publiceringsgrind för läsarkvalitet
Innan en bok anges som publiceringsklar ska både PDF och EPUB granskas som faktiska leveranser, inte enbart genom framgångsrik körning av exportverktyg. Kontrollera minst PDF-sidhuvuden, kapitelstarter, tabellavskiljare och sidbrytningar samt EPUB-navigation, spine, omslag och eventuell oavsiktligt synlig innehållsförteckning. Kontrollera källregister, interna navigationslänkar och att långa webbadresser är klickbara. Redovisa vad som har verifierats automatiskt respektive visuellt och gör ingen obestyrkt publiceringsutfästelse. Vid release är GitHub-releasetaggen auktoritativ för versionen i de publicerade EPUB-/PDF-filerna. Versionsmetadata hämtas från taggen under bygget utan att `book.yaml` ändras. Vid förhandsbyggen används versionen i `book.yaml`; kräv inte att den matchar en senare releasetagg. Använd ändrings-PR och provexport före release när ett GitHub-projekt finns.


## Diagramkällor och publicering
Om bokprojektet innehåller diagramkällor: samarbeta med `diagram-illustrationer` och kräv verifierad SVG-rendering innan PDF/EPUB markeras klara. Bevara `.dot`, `.puml` och handgjord `.svg` i revisions- och ZIP-flödet. PDF ska använda verifierad vektorbaserad konvertering/inbäddning där det är möjligt; EPUB ska använda fungerande SVG eller dokumenterad kompatibilitetsfallback. Genererade SVG är återskapbara men måste finnas när kapitelreferenser valideras. Om renderare saknas: rapportera `pending_render` och blockera publicering av böcker med olösta figurreferenser. Den faktiska exportintegrationen tillkommer i separat implementeringssteg.


## Kapitelgranskning och revisionsspår
Granskningsprotokoll under `docs/reviews/` och skriptet `scripts/chapter_review.py` tillhör bokprojektet. Skapa protokoll först efter användarens val av manuell eller automatisk granskning. En ändring i kapiteltexten ogiltigförklarar automatiskt det äldre godkännandet via kontroll mot kapitel-SHA. Före automatisk slutrapport: uppdatera normal projektrevision med både kapitel och protokoll, verifiera projektmanifest och genomför `chapter_review.py check`. Påstå aldrig att filen är reviderad/godkänd om miljön inte faktiskt kunde köra kontrollerna. Äldre projekt utan granskningsprotokoll ska fortfarande kunna valideras.


## Work-first och Engine ZIP-fallback
Försök först materialisera installerad kanonisk mall och skript. Om pluginen endast exponerar textresurser: använd `larobokskaparen-engine-X.Y.Z.zip` från motsvarande GitHub-release. Verifiera `engine-package.json` och kör `python3 scripts/engine_selftest.py --render` i ett isolerat skrivbart arbetsområde före projektinitiering. Kopiera samma `templates/bokprojekt/`, aldrig ersättningsskript. Om Engine inte kan nås eller köras: ge versionsmatchad release-länk, begär att användaren bifogar ZIP och ange `EJ VERIFIERAT`, inte `PASS`. Versionsmatchning är ett hårt krav.
