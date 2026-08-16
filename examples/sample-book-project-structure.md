# Exempel: kanonisk bokprojektstruktur

Detta är en översikt. Den exakta, genererade mallen finns i Knowledge-filen `project-template-bundle.md` och har företräde för nya projekt.

```text
<bokslug>-projekt/
├── README.md
├── book.yaml
├── project-manifest.json
├── revision-log.md
├── project-index.md
├── docs/
├── chapters/
│   ├── kapitelmall.md
│   ├── 00-inledning.md
│   └── 01-<kapitel-slug>.md
├── exercises/
├── examples/
├── code/
├── assets/
├── styles/
├── scripts/
└── exports/
```

Regler:
- `book.yaml` är kanonisk metadata.
- Kapitel använder tvåsiffrigt nummer och kort slug: `01-introduktion.md`.
- `00-inledning.md` räknas inte som kapitel 1.
- Projektets revision och filhashar skyddas av `project-manifest.json` och `scripts/project_integrity.py`.
- Leveranszippar får revisionsnummer, exempelvis `javaprogrammering-r0003-kapitel-02.zip`.
- Bevara fungerande äldre projekt och migrera bara när det behövs eller uttryckligen önskas.
