# Lärobokskaparen GPT-paket

Detta paket innehåller material för att skapa en Custom GPT som hjälper användaren skapa läroböcker, handböcker, kursböcker och praktiska guider om teknologier, metoder och arbetssätt.

## Innehåll

```text
gpt-configuration/
  instructions.md
  conversation-starters.md
knowledge-upload/
  01-purpose-and-workflow.md
  02-guided-interview.md
  03-difficulty-and-pedagogy-model.md
  04-book-specification-template.md
  05-chapter-plan-template.md
  06-chapter-template.md
  07-canon-and-continuity.md
  08-quality-checklist.md
  09-project-status-template.md
  10-export-metadata-template.md
  11-book-type-patterns.md
  12-bilingual-style-guide.md
  13-example-prompts.md
  14-suggested-project-structure.md
  15-export-and-rendering-rules.md
examples/
  sample-book-project-structure.md
```

## Installation i Custom GPT

1. Skapa en ny GPT.
2. Namn: `Lärobokskaparen`.
3. Klistra in `gpt-configuration/instructions.md` i Instructions.
4. Lägg in starters från `gpt-configuration/conversation-starters.md`.
5. Ladda upp alla filer i `knowledge-upload/` som Knowledge.
6. Rekommenderade capabilities: Web Browsing, Code Interpreter/Data Analysis och eventuellt Image Generation.

## Begränsningskontroll

- Instructions är avsiktligt kortare än 8000 tecken.
- Knowledge består av 15 filer och håller sig under gränsen 20 filer.

## Viktiga förbättringar i denna version

- Standardiserad projekt-zip-struktur.
- Stabil zip-namngivning: `<bokslug>-projekt-kapitel-NN.zip` efter nytt kapitel.
- GPT:n ska skapa projekt-zip när kapitelproduktionen börjar.
- GPT:n ska normalt bara visa ändrade filer, inte filinnehåll, vid kapitelgenerering.
- Obligatorisk inledning i `chapters/00-inledning.md`.
- EPUB utan innehållsförteckning som textkapitel och med luftig layout.
- PDF med innehållsförteckning före inledningen.
- Tydliga regler för att markdown-stilar ska renderas korrekt i EPUB/PDF/DOCX.
- GPT:n ska fråga vem som ska stå som författare och skapa komplett exportmetadata för EPUB/PDF.
