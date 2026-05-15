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
- Kapitelordning följer `docs/export-metadata.yaml`.
- Alla bildlänkar pekar på existerande filer.

## 4. EPUB-standard

EPUB ska vara luftig och läsbar:

- Ingen innehållsförteckning som eget textkapitel.
- Navigerbar TOC får finnas i EPUB-metadata/navigation.
- CSS ska sätta generösa marginaler, tydligt radavstånd och styckeavstånd.
- Rubriker, tabeller, kodblock, listor, blockcitat, bilder och bildtexter ska ha definierad styling.
- Tabeller får inte lämnas som rå markdown.

Rekommenderad EPUB-känsla: `line-height` ca 1.55–1.7, styckesmarginal ca 0.7–1.0em, maxbredd för text där formatet tillåter.

## 5. PDF-standard

PDF ska ha en mer trycklik men fortfarande luftig layout:

- Innehållsförteckning ska ligga före `chapters/00-inledning.md`.
- TOC ska skapas från H1–H3 och får inte vara tom.
- Markdown ska renderas semantiskt till rubriker, fetstil, kursiv, tabeller, listor och kodblock.
- Använd sidbrytning före varje kapitel.
- Använd läsbara marginaler och radavstånd.

## 6. Felhantering

Om exportverktyget inte kan rendera markdown korrekt ska Lärobokskaparen inte låtsas att exporten är färdig. Den ska rapportera problemet och skapa en korrigerad markdown-/HTML-mellanrepresentation eller föreslå verifieringssteg.
