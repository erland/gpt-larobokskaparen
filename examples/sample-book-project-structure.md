# Standardiserad bokprojektstruktur och namngivning

Använd alltid exakt denna struktur i projekt-zippar, även när projektet växer:

```text
<bokslug>-projekt/
├── README.md
├── docs/
│   ├── bokspecifikation.md
│   ├── kapitelplan.md
│   ├── pedagogisk-canon.md
│   ├── terminologi.md
│   ├── projektstatus.md
│   ├── export-metadata.yaml
│   └── export-guide.md
├── chapters/
│   ├── 00-inledning.md
│   ├── 01-<kapitel-slug>.md
│   └── 02-<kapitel-slug>.md
├── exercises/
│   └── chapter-01-exercises.md
├── examples/        # scenarier, figurer, data eller icke-kodexempel
├── code/            # körbar kod för teknikböcker
├── assets/          # bilder, omslag, diagram, CSS
└── exports/         # genererade EPUB/PDF/DOCX/HTML/Markdown
```

## Filnamn för projekt-zippar

När ett projekt startas:

```text
<bokslug>-projekt.zip
```

Efter att ett nytt kapitel har lagts till:

```text
<bokslug>-projekt-kapitel-NN.zip
```

Exempel:

```text
javaprogrammering-projekt-kapitel-03.zip
agilt-arbetssatt-projekt-kapitel-08.zip
```

Regler:
- Använd tvåsiffrigt kapitelnummer: 01, 02, 03.
- Räkna inte in `00-inledning.md` som kapitel.
- Bevara befintliga filnamn och kataloger vid uppdatering.
- Lägg inte kapitel i roten, docs/ eller blandade kataloger.
- Visa normalt bara ändrade filer i chatten, inte filinnehållet.


## Metadataregel
`docs/export-metadata.yaml` ska innehålla författare, titel, språk, identifierare, datum/version, rättigheter, kapitelordning och exportregler innan EPUB/PDF skapas. Om författare saknas ska GPT:n fråga användaren innan export.

## Illustrationer och omslag

Om projektet använder omslag eller illustrationer ska följande ingå:

```text
assets/
  cover/
    cover.png
  images/
    IMG-01-01.png
  image-prompts/
    COVER.md
    IMG-01-01.md
docs/
  illustration-plan.md
```
