# Canonical markdown och renderingskontrakt

Denna fil är styrande när Lärobokskaparen skapar EPUB, PDF, DOCX och Markdown. Målet är konsekventa exporter där markdown alltid blir riktig typografi.

## 1. Tillåten bok-markdown

Använd endast denna standard i kapitel:

```md
# Kapitelrubrik

## Huvudsektion

### Undersektion

Vanlig brödtext med **fet stil** och *kursiv stil*.

- Punktlista
- Punktlista

1. Numrerat steg
2. Numrerat steg

| Kolumn | Kolumn |
|---|---|
| A | B |

> Kort citat eller markerad princip.

```java
System.out.println("exempel");
```
```

## 2. Rubrikregler

- Använd H1 (`#`) exakt en gång per kapitel.
- Använd H2 (`##`) för huvudsektioner.
- Använd H3 (`###`) för undersektioner.
- Använd inte H4 (`####`) eller lägre i boktext.
- Om utkast innehåller `####`: konvertera före export till antingen H3, fet inledningsrad eller punktlista.

Exempel:

```md
#### Fallgrop 1: För mycket teori
```

Ska bli något av:

```md
### Fallgrop 1: För mycket teori
```

eller:

```md
- **Fallgrop 1: För mycket teori.** Förklaring...
```

## 3. Exportvalidering före EPUB/PDF

Kontrollera alltid innan export:

- Inga rader börjar med `####`, `#####` eller `######`.
- Inga markdownmarkörer visas av misstag i brödtext: `**`, `###`, `|---|`, ``` eller rå HTML.
- Kodblock har både start och slut.
- Tabeller har korrekt header och separatorrad.
- Listor har tomrad före och efter när det behövs för stabil rendering.
- Kapitelordning följer `book.yaml`.
- Alla bildlänkar pekar på existerande filer.

## 4. EPUB-standard

EPUB ska vara luftig och läsbar:

- Ingen innehållsförteckning som eget textkapitel.
- Navigerbar TOC ska finnas i EPUB-metadata/navigation och ska normalt bara omfatta H1/översta kapitelnivån.
- Vid Pandoc-export till EPUB: använd `--toc --toc-depth=1`.
- Behåll `nav.xhtml`; den ska inte visas som vanlig lässida i bokflödet. Om den finns i spine ska den sättas som icke-linjär (`linear="no"`) i stället för att navigationen tas bort.
- CSS ska sätta generösa marginaler, tydligt radavstånd och styckeavstånd.
- EPUB-CSS får inte använda `page-break-before`, `break-before` eller stora top-marginaler på H1 som kan skapa tom sida före kapitelankaret.
- Kapitelrubriker ska vara bokmässiga och centrerade. Om H1 är `1. Kapitelrubrik` får exporten visa numret och rubriken på två rader men TOC-texten ska vara `1. Kapitelrubrik`.
- Avståndet mellan kapitelnummer och kapitelrubrik ska vara tajt; avståndet mellan rubrik och brödtext ska vara tydligt men inte överdrivet.
- Rubriker, tabeller, kodblock, listor, blockcitat, bilder och bildtexter ska ha definierad styling.
- Tabeller får inte lämnas som rå markdown.

Rekommenderad EPUB-känsla: `line-height` ca 1.55–1.7, styckesmarginal ca 0.7–1.0em, maxbredd för text där formatet tillåter.

## 5. PDF-standard

PDF ska ha en mer trycklik men fortfarande luftig layout:

- Innehållsförteckning ska ligga före `chapters/00-inledning.md`.
- TOC ska skapas från H1–H3 och får inte vara tom, om användaren inte uttryckligen vill ha endast översta nivån även i PDF.
- Markdown ska renderas semantiskt till rubriker, fetstil, kursiv, tabeller, listor och kodblock.
- Använd sidbrytning före varje kapitel.
- Använd läsbara marginaler och radavstånd.

## 6. Felhantering

Om exportverktyget inte kan rendera markdown korrekt ska Lärobokskaparen inte låtsas att exporten är färdig. Den ska rapportera problemet och skapa en korrigerad markdown-/HTML-mellanrepresentation eller föreslå verifieringssteg.


## 6. Punktlistor och nästlade punktlistor

Punktlistor måste skrivas som strikt markdown med tomrad före och efter listblocket. Detta är särskilt viktigt för EPUB/PDF eftersom vissa renderare annars kan tolka punkterna som vanlig text.

Korrekt:

```md

- **Misstag: Att försöka förstå alla Unity-fönster samtidigt.**
  - Varför det händer: Editorn visar mycket information direkt.
  - Hur du undviker det: Fokusera först på Scene view, Game view, Hierarchy, Inspector och Project.

```

Regler:

- Lägg en tomrad före första `-` när listan följer efter brödtext eller rubrik.
- Lägg en tomrad efter sista listpunkten innan nästa stycke/rubrik/tabell.
- Underpunkter ska indenteras konsekvent med två mellanslag före `-`.
- Blanda inte `-`, `*` och `+` i samma lista; använd `-`.
- Skriv inte flera listnivåer som separata stycken utan korrekt indentering.
- Om en föräldrapunkt har underpunkter ska underpunkterna ligga direkt efter föräldrapunkten.
- Om listpunkten blir lång, håll efterföljande rader indenterade minst två mellanslag så de hör till samma punkt.

## 7. Tabeller

Markdown-tabeller måste vara enkla och konsekventa.

Korrekt:

```md

| Begrepp | Betydelse | Exempel |
|---|---|---|
| Scene view | Där du bygger banan | Placera objekt |
| Game view | Där du testar spelet | Spela scenen |

```

Regler:

- Lägg tomrad före och efter varje tabell.
- Använd alltid rubrikrad och separatorrad.
- Varje rad ska ha samma antal celler.
- Undvik radbrytningar inuti tabellceller.
- Undvik nästlade listor inne i tabeller; lägg i stället listan före eller efter tabellen.
- Om en tabell blir bred i EPUB/PDF, gör om den till en punktlista eller dela den i två tabeller.

## 8. EPUB/PDF-validering för listor och tabeller

Före export ska GPT:n göra en snabb renderingskontroll:

- Kontrollera att varje listblock har tomrad före och efter.
- Kontrollera att nästlade listor har konsekvent indentering.
- Kontrollera att tabeller har separatorrad och lika många celler per rad.
- Om exporten använder HTML mellanformat: kontrollera att punktlistor blir `<ul><li>`, nästlade punktlistor blir `<ul><li><ul><li>`, och tabeller blir `<table>`.
- Om en renderare inte stöder tabeller tillförlitligt ska GPT:n konvertera tabellen till semantisk HTML-tabell eller till en tydlig punktlista innan EPUB/PDF skapas.

## 9. Korrigering före export

Om ett kapitel innehåller en lista som riskerar att renderas fel ska GPT:n normalisera den före export och även uppdatera projekt-zippen. Visa som standard endast vilka filer som ändrats, inte hela filinnehållet.
