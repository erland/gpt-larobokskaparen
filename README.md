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

## Nytt i v11

- Frågar alltid om omslagsbild och illustrationer i texten.
- Lägger till standardiserat arbetsflöde för bild-ID:n, promptfiler, illustration-plan och markdown-referenser.
- Rekommenderar att bilder genereras efter kapitel-/bildplanen, en och en eller i små batchar.


## v11-justering

- Omslag frågas alltid om och ska använda titel + författare.
- Inre illustrationer är avstängda som standard och skapas bara efter uttryckligt ja.
- Promptregler för inre bilder styr bort från A4-sidor, ramar, affischer och text.


## Nytt i v11

- Strikt canonical markdown-standard.
- Exportvalidering som fångar `####`, rå markdown, trasiga tabeller och öppna kodblock.
- EPUB-renderingskontrakt för luftig layout.
- PDF-renderingskontrakt med icke-tom innehållsförteckning före inledningen.


## Nytt i v11

- Striktare regler för punktlistor, nästlade listor och tabeller.
- Krav på tomrad före och efter listor/tabeller så markdown-renderare tolkar dem korrekt.
- Förbud mot halvformaterade listor som ser ut som listor i text men inte är giltig markdown.
- Exportvalidering ska kontrollera att nästlade listor blir HTML-listor och tabeller blir riktiga tabeller i EPUB/PDF.


## v12 exportjustering

Denna version förtydligar EPUB-exporten:

- EPUB ska ha navigerbar innehållsförteckning i läsaren men inte en synlig TOC-sida i dokumentflödet.
- EPUB-TOC ska normalt bara innehålla översta kapitelnivån/H1.
- Pandoc-export till EPUB ska använda `--toc --toc-depth=1`.
- `nav.xhtml` ska bevaras men inte visas som vanlig lässida.
- EPUB-CSS ska undvika sidbrytningar/stora top-marginaler på H1 som skapar tom sida före kapitel.
- Kapitelrubriker ska ha bokmässig, centrerad och tajt layout.

---

## Distributionspaket

Repositoryt kan bygga två distributioner från samma källfiler:

- `larobokskaparen-custom-gpt-vX.Y.Z.zip` för installation/uppdatering av Custom GPT:n.
- `larobokskaparen-chat-vX.Y.Z.zip` för användning som portabel Läroboksskapare i en vanlig ChatGPT-konversation.

Custom GPT-distributionen innehåller samma `gpt-configuration/instructions.md`, `gpt-configuration/conversation-starters.md` och samma 18 filer från `knowledge-upload/` som repositoryt. Byggvalideringen kontrollerar att dessa filer är byte-identiska med källorna.

Den portabla distributionen innehåller:

```text
START-HERE.md
VERSION
MANIFEST.json
assistant/instructions.md
knowledge/
examples/
```

`assistant/instructions.md` är en byte-identisk kopia av `gpt-configuration/instructions.md`, och filerna under `knowledge/` är byte-identiska kopior av de 18 Knowledge-filerna.

### Lokal build

Vanliga lokala/preview-byggen använder versionsnumret i `VERSION`:

```bash
python3 scripts/build_distributions.py
python3 scripts/validate_distributions.py
```

En explicit version kan anges utan att ändra repositoryts `VERSION`:

```bash
python3 scripts/build_distributions.py --version 1.1.0
python3 scripts/validate_distributions.py --version 1.1.0
```

### GitHub Release

Vid publicering av en GitHub Release är release-taggen versionskälla. Taggen ska följa `v<SemVer>`, exempelvis:

```text
v1.0.0
v1.1.0
v2.0.0
```

För en release med taggen `v1.1.0` bygger workflowet automatiskt:

```text
larobokskaparen-custom-gpt-v1.1.0.zip
larobokskaparen-chat-v1.1.0.zip
```

Versionen `1.1.0` skrivs också in i `VERSION` inne i båda distributionspaketen och i `MANIFEST.json` i den portabla distributionen. Repositoryts egen `VERSION` ändras inte av releasebygget.

Workflowet laddar upp ZIP-filerna både som tillfälliga GitHub Actions-artifacts och, för publicerade releaser, som permanenta assets på själva GitHub-releasen.

### Använda den portabla versionen

Bifoga `larobokskaparen-chat-vX.Y.Z.zip` i en ny ChatGPT-konversation och skriv exempelvis:

> Använd Läroboksskaparen i den bifogade ZIP-filen för den här konversationen. Läs `START-HERE.md` först.
