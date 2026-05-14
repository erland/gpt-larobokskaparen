# Illustration- och omslagsarbetsflöde

Syfte: stödja professionella omslag och frivilliga illustrationer utan att kapitelproduktionen blir instabil.

## Grundprincip
- Omslag ska alltid tas upp i onboarding: fråga om användaren vill ha genererad omslagsbild.
- Titel och författare ska alltid användas på omslaget när omslag skapas.
- Illustrationer inne i boken är avstängda som standard.
- Planera eller generera inre illustrationer endast om användaren uttryckligen vill ha dem.

## Frågor i onboarding
Fråga alltid:
1. Vill du ha en genererad omslagsbild?
2. Vilken titel och vilket författarnamn ska stå på omslaget?
3. Vill du även ha illustrationer inne i boken, eller ska vi hålla oss till text och eventuellt omslag?

Om användaren är osäker, föreslå standardval:
- Omslag: ja om boken ska exporteras som EPUB/PDF för läsning; nej för snabbt textutkast.
- Inre illustrationer: nej som standard. Ja endast när användaren vill ha en mer illustrerad lärobok eller när bilder tydligt hjälper förståelsen.

## Omslag
Struktur:
- `assets/cover/cover.png`
- `assets/image-prompts/COVER.md`

Omslagsprompten ska ange:
- bokens titel
- författarnamn
- ämne och målgrupp
- önskad stämning
- professionell bokomslagslayout
- att endast titel och författare ska synas som text, om inte användaren uttryckligen ber om mer

## Inre illustrationer
Använd endast om användaren uttryckligen tackat ja.

Struktur:
- `assets/images/IMG-NN-MM.png`
- `assets/image-prompts/IMG-NN-MM.md`
- `docs/illustration-plan.md`

ID-regler:
- Omslag: `COVER`
- Kapitelbilder: `IMG-NN-MM`, där `NN` är kapitelnummer och `MM` löpnummer i kapitlet.

## Viktigt: undvik A4-/affischbilder i kapitlen
Inre illustrationer ska normalt vara rena bilder som kan bäddas in i texten, inte kompletta sidor.

Promptar för inre illustrationer ska uttryckligen säga:
- fristående illustration, inte A4-sida
- ingen ram runt bilden
- ingen affischlayout
- ingen bakgrundsplansch
- ingen text i bilden om det inte är absolut nödvändigt
- ingen titel, rubrik, sidfot eller marginaldesign
- ren komposition med transparent, vit eller diskret bakgrund
- professionell redaktionell läroboksillustration

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

## Rekommenderat arbetssätt
1. Skapa bokplan och kapitelplan först.
2. Skapa omslagsprompt om användaren vill ha omslag.
3. Planera inre illustrationer endast om användaren uttryckligen valt det.
4. Lägg bild-ID:n, bildtexter och promptar i projektet.
5. Generera bilder senare en och en eller i små batchar.
6. Granska/ersätt bilder innan slutexport.

## Exportregler
Vid EPUB/PDF-export:
- kontrollera att alla refererade bilder finns
- rapportera saknade bilder
- skala bilder så de passar sidan/läsaren
- rendera bildtexter som riktig kursiv text, inte rå markdown
- behåll luftig EPUB-layout
