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

## Två vägar för kapitelgranskning
Efter kapitelutkast erbjuds användaren **Granska själv** eller **Granska, korrigera och godkänn automatiskt**. Assistenten genomför kvalitetsgranskningen; Python-skriptet registrerar status och validerar granskningsprotokollets fullständighet och versionsbindning.

Exempel på kommandon (kör i bokprojektets rot):
```sh
python scripts/chapter_review.py start 03-exempel.md --mode auto
python scripts/chapter_review.py approve 03-exempel.md --mode auto --report /tmp/03-review.json
python scripts/chapter_review.py check 03-exempel.md
```
Manuellt alternativ: `start ... --mode manual` följt av `approve ... --mode manual --approved-by <namn>` efter uttryckligt godkännande. Kör normal revision och projektintegritetsverifiering innan slutleverans. Befintliga kapitel utan granskningsprotokoll berörs inte.
