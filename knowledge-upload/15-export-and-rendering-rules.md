# Export- och renderingsregler

## Allmänt

All export ska utgå från `docs/export-metadata.yaml`, `chapters/00-inledning.md` och kapitelordningen i `chapters` eller metadatafilen.

Markdown ska renderas, inte kopieras rått. Följande ska visas som riktig formatering i EPUB/PDF/DOCX:

- `#`, `##`, `###` som rubriker
- `**fet stil**` som fet stil
- `*kursiv*` som kursiv
- punktlistor och numrerade listor som listor
- markdown-tabeller som riktiga tabeller
- kodblock som kodblock
- citat som citat

## Metadata före export
Innan EPUB eller PDF skapas ska GPT:n kontrollera `docs/export-metadata.yaml`. Om `author` saknas ska användaren tillfrågas vem som ska stå som författare. Exporten ska använda metadata för titel, författare, språk, datum/version, rättigheter, identifierare och kapitelordning. EPUB ska innehålla korrekt dc:title, dc:creator, dc:language och identifierare. PDF-titelsida eller dokumentmetadata ska använda samma titel/författare där det är praktiskt möjligt.

## EPUB

EPUB ska vara luftig och lättläst:

- Ingen innehållsförteckning som eget textkapitel i början.
- Navigeringsfil/metadata får finnas enligt EPUB-standard.
- Använd CSS med tydliga styckeavstånd, rimlig radlängd, läsbar brödtextstorlek, luft före/efter rubriker och bra tabell-/kodblocksstil.
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
