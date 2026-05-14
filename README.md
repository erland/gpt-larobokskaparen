# Lärobokskaparen GPT v6

Detta paket innehåller konfigurationsmaterial för en Custom GPT som hjälper användaren skapa läroböcker, handböcker, kursböcker och praktiska guider om teknologier, metoder och arbetssätt.

## Viktig ändring i v6
v6 kombinerar:
- v2:s coachande onboarding för ovana författare
- v5:s strikta projektstruktur, zip-namngivning och exportregler

GPT:n ska alltså inte börja med att skapa en zip när användaren bara vill planera en bok. Den ska först hjälpa användaren att välja målgrupp, förkunskaper, nivå, boktyp, längd, pedagogisk stil, språk och författare. Därefter ska den presentera kapitelplanen direkt i chatten. Projekt-zip skapas först när planen är godkänd eller användaren ber den gå vidare.

## Rekommenderad installation i Custom GPT
1. Kopiera innehållet i `gpt-configuration/instructions.md` till GPT:ns Instructions.
2. Lägg in texten från `gpt-configuration/conversation-starters.md` som conversation starters.
3. Ladda upp alla filer i `knowledge-upload/` som Knowledge.
4. Aktivera rekommenderade capabilities:
   - Web Browsing
   - Code Interpreter / Data Analysis
   - Image Generation valfritt

## Begränsningskontroll
- Instructions är under 8000 tecken.
- Antalet knowledge-filer är under 20.

## Viktiga beteenden
- Stötta ovana författare med max tre frågor per tur.
- Presentera kapitelplan i chatten innan zip skapas.
- Fråga vem som ska stå som författare.
- Skapa alltid en inledning i `chapters/00-inledning.md`.
- Använd alltid samma projektstruktur.
- Namnge uppdaterade zippar med kapitelnummer i slutet.
- Visa normalt bara ändrade filer vid kapitelgenerering.
- EPUB ska vara luftig och utan innehållsförteckning som textkapitel.
- PDF ska ha innehållsförteckning före inledningen.
- Markdown-stilar ska renderas korrekt i EPUB/PDF/DOCX.

## Nytt i v7

- Frågar alltid om omslagsbild och illustrationer i texten.
- Lägger till standardiserat arbetsflöde för bild-ID:n, promptfiler, illustration-plan och markdown-referenser.
- Rekommenderar att bilder genereras efter kapitel-/bildplanen, en och en eller i små batchar.
