# Kanonisk bokprojektstruktur, revision och synk

## Single source of truth
Den verkliga mallen finns i repositoryts `templates/bokprojekt/`. För Custom GPT/portabel distribution återges samma mall automatiskt i `project-template-bundle.md`. Om beskrivande dokument eller äldre exempel skiljer sig från bundlen gäller bundlen för nya projekt.

## Huvudstruktur

```text
<bokslug>-projekt/
├── README.md
├── book.yaml
├── project-manifest.json
├── revision-log.md
├── project-index.md
├── docs/
│   ├── bokspecifikation.md
│   ├── kapitelplan.md
│   ├── pedagogisk-canon.md
│   ├── terminologi.md
│   ├── projektstatus.md
│   ├── quality-checklist.md
│   ├── illustration-plan.md
│   └── export-guide.md
├── chapters/
│   ├── kapitelmall.md
│   └── 00-inledning.md
├── exercises/
├── examples/
├── code/
├── assets/{cover,images,image-prompts}/
├── styles/{epub.css,pdf.css}/
├── scripts/{project_integrity.py,export-book.py,export-book.sh}/
└── exports/
```

Numeriska kapitelfiler skapas först när kapitlet faktiskt finns och heter `NN-kort-slug.md`. Inledningen är `00-inledning.md` och räknas inte som kapitel 1.

## Metadata
`book.yaml` är kanonisk metadata. Skapa inte en andra exportmetadatafil i nya projekt.

## Revisionslås
`project-manifest.json` innehåller stabilt `project_id`, heltalsrevision, källrevision, kanoniskt zipnamn och SHA-256 för spårade filer. `revision-log.md` är läsbar historik. `scripts/project_integrity.py` används för `init`, `verify`, `status` och `commit`.

Arbetsordning vid projektändring:
1. Välj exakt en uttryckligen angiven indata-zip och packa upp i en ny tom katalog.
2. Kör `python scripts/project_integrity.py verify .` före ändringar.
3. Ändra endast beställda filer. Vid nytt/reviderat kapitel får övriga kapitelfiler inte ändras.
4. Kör `status`, sedan `commit` med `--expected-revision` och explicit `--allow` för tillåtna filer.
5. Paketera hela projektet, packa upp leveranszipen i en ny katalog och kör `verify` igen.
6. Leverera zip samt källrevision, ny revision, project-id och exakt lista över ändrade filer.

## Äldre projekt
Ett fungerande äldre projekt ska inte byggas om bara för att det avviker från den nya mallen. Bevara strukturen och komplettera varsamt. Migrera till den nya revisionslåsta strukturen när användaren ber om det eller när migrering krävs för säkert fortsatt arbete; ändra inte manus i onödan.
