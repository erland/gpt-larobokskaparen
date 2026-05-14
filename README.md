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
examples/
  sample-book-project-structure.md
```

## Installation i Custom GPT

1. Skapa en ny GPT.
2. Namn: `Lärobokskaparen`.
3. Klistra in `gpt-configuration/instructions.md` i Instructions.
4. Lägg in starters från `gpt-configuration/conversation-starters.md`.
5. Ladda upp alla filer i `knowledge-upload/` som Knowledge.

## Begränsningskontroll

- Instructions är avsiktligt kortare än 8000 tecken.
- Knowledge består av 14 filer och håller sig under gränsen 20 filer.

## Viktiga förbättringar i denna version

- Guidat startflöde för ovana författare.
- Explicit svårighetsmodell baserad på läsarens förkunskaper.
- Progressionsregler för pedagogisk kvalitet.
- Canon-filer för kontinuitet i längre böcker.
- Boktypsspecifika mönster för teknik-, metod-, workshop- och certifieringsböcker.
- Exportmetadata för reproducerbara exporter.
