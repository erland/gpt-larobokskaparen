# Export- och renderingsregler v12

## Allmänt

All export ska utgå från `book.yaml`, `chapters/00-inledning.md` och kapitelordningen i `chapters` eller metadatafilen.

Markdown ska renderas, inte kopieras rått. Följande ska visas som riktig formatering i EPUB/PDF/DOCX:

- `#`, `##`, `###` som rubriker
- `**fet stil**` som fet stil
- `*kursiv*` som kursiv
- punktlistor och numrerade listor som listor
- markdown-tabeller som riktiga tabeller
- kodblock som kodblock
- citat som citat

## Metadata före export
Innan EPUB eller PDF skapas ska GPT:n kontrollera `book.yaml`. Om `author` saknas ska användaren tillfrågas vem som ska stå som författare. Exporten ska använda metadata för titel, författare, språk, datum/version, rättigheter, identifierare och kapitelordning. EPUB ska innehålla korrekt dc:title, dc:creator, dc:language och identifierare. PDF-titelsida eller dokumentmetadata ska använda samma titel/författare där det är praktiskt möjligt.

## EPUB

EPUB ska vara luftig och lättläst men utan synlig innehållsförteckningssida i bokflödet:

- Ingen innehållsförteckning som eget textkapitel i början.
- EPUB ska ändå ha navigerbar TOC/index i EPUB-läsaren.
- Navigerbar TOC ska normalt bara innehålla översta kapitelnivån: H1-rubriker. Använd `--toc --toc-depth=1` vid Pandoc-export till EPUB.
- Behåll `nav.xhtml`/EPUB-navigation. Om den hamnar i spine ska den sättas som icke-linjär (`linear="no"`) eller annars döljas från läsflödet utan att navigationen försvinner.
- Använd CSS med tydliga styckeavstånd, rimlig radlängd, läsbar brödtextstorlek, luft före/efter rubriker och bra tabell-/kodblocksstil.
- Kapitelstart får inte skapa tom ankarsida före kapitlet. Undvik `page-break-before`, `break-before` och stora top-marginaler på H1 i EPUB-CSS.
- H1 med formatet `1. Kapitelrubrik` får typograferas som två centrerade rader: `1.` och `Kapitelrubrik`. Numret och rubriken ska vara tydliga och bokmässiga, med tajt avstånd: cirka 25 % av tidigare luft mellan nummer och rubrik och cirka 50 % mindre luft mellan rubrik och brödtext.
- Undvik kompakt layout där långa stycken trycks ihop.

## PDF

PDF ska alltid ha en innehållsförteckning i början, före inledningen.

Regler:
- Innehållsförteckningen ska genereras från rubrikerna och får inte vara tom.
- Inledningen ska komma efter innehållsförteckningen.
- Markdown-stil ska vara korrekt renderad.
- Rubriker, tabeller, listor och kodblock ska vara visuellt tydliga.

## Exportfelsökning

Om en export blir tom, kompakt eller visar rå markdown:

1. Kontrollera att rätt projekt-zip användes.
2. Kontrollera att `chapters/00-inledning.md` och kapitel finns.
3. Kontrollera att exporteraren använder markdown-rendering/pandoc-liknande konvertering, inte ren textkopiering.
4. Kontrollera att PDF-innehållsförteckningen bygger på rubrikstrukturen efter markdown-rendering.
5. Skapa om filen och returnera både uppdaterad projekt-zip och exportfil om projektfiler ändrats.


## v9-tillägg: strikt markdownrendering

Se även `17-canonical-markdown-and-render-contract.md`. Den filen är styrande för rubriknivåer, exportvalidering och hur rå markdown som `####`, `**` och tabeller ska hanteras före EPUB/PDF-export.


## Särskilda regler för listor och tabeller

EPUB/PDF-export ska aldrig acceptera att listor och tabeller blir vanlig text. Innan export ska GPT:n normalisera markdown:

- tomrad före och efter listor
- två mellanslag för nästlade listor
- konsekvent `-` för punktlistor
- korrekt tabellseparator `|---|---|`
- lika många tabellceller i alla rader

Exempel på godkänd nästlad lista:

```md

- **Misstag: Att försöka förstå alla Unity-fönster samtidigt.**
  - Varför det händer: Editorn visar mycket information direkt.
  - Hur du undviker det: Fokusera först på Scene view, Game view, Hierarchy, Inspector och Project.

```

Om exportverktyget ändå tappar nästling eller tabellformat ska GPT:n använda ett robust mellanformat, exempelvis HTML genererad från markdown, så att EPUB/PDF innehåller riktiga `<ul>`, `<li>` och `<table>`-element.
