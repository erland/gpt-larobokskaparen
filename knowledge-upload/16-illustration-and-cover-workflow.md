# Illustration- och omslagsarbetsflöde

Syfte: stödja professionella omslagsbilder och illustrationer utan att göra kapitelproduktionen instabil.

## Frågor i onboarding
Fråga alltid:
1. Vill du ha en genererad omslagsbild?
2. Vill du ha professionella illustrationer på relevanta ställen i texten?

Om användaren är osäker, föreslå standardval:
- Omslag: ja för färdig bok/EPUB/PDF, nej för snabbt utkast.
- Illustrationer: ja för pedagogiska/tekniska böcker där bilder förklarar modeller, processer, arkitektur, flöden eller begrepp.

## Rekommenderat arbetssätt
1. Skapa bokplan och kapitelplan först.
2. Identifiera rimliga bildplatser i planen.
3. Skapa bild-ID:n, bildtexter och promptar.
4. Lägg markdown-referenser i kapitlen.
5. Generera bilder senare en och en eller i små batchar.
6. Granska/ersätt bilder innan slutexport.

## Struktur
- `assets/cover/cover.png`
- `assets/image-prompts/COVER.md`
- `assets/images/IMG-NN-MM.png`
- `assets/image-prompts/IMG-NN-MM.md`
- `docs/illustration-plan.md`

## ID-regler
- Omslag: `COVER`
- Kapitelbilder: `IMG-NN-MM`, där `NN` är kapitelnummer och `MM` löpnummer i kapitlet.
- Exempel: `IMG-04-01` är första illustrationen i kapitel 4.

## Illustration plan
`docs/illustration-plan.md` ska innehålla:
- ID
- kapitel/fil
- föreslagen placering
- pedagogiskt syfte
- bildtext
- bildfil
- promptfil
- status: `planned`, `prompted`, `generated`, `approved`, `replace`

## Markdown i kapitel
Använd relativ bildreferens och separat figurtext:

```md
![Kort alt-text](../assets/images/IMG-03-02.png)

*Figur 3.2: Förklarande bildtext som hör till resonemanget i kapitlet.*
```

## Promptregler
Varje promptfil ska innehålla:
- ID och kapitel
- Syfte i kapitlet
- Målgrupp och svårighetsgrad
- Motiv/scene
- Visuell stil
- Komposition och format
- Negativ instruktion: ingen text i bilden om det inte är absolut nödvändigt

Föredra professionell, modern, redaktionell läroboksstil med konsekvent färgpalett, tydlig komposition, luft, hög läsbarhet och utan plottriga detaljer.

## Exportregler
Vid EPUB/PDF-export:
- kontrollera att alla refererade bilder finns
- rapportera saknade bilder
- skala bilder så de passar sidan/läsaren
- rendera bildtexter som riktig kursiv text, inte rå markdown
- behåll luftig EPUB-layout
