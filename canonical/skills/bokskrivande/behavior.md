## Profilregler
För `textbook`: anpassa efter förkunskaper, introducera begrepp i kontrollerad ordning och använd normalt lärandemål, exempel, vanliga misstag, övning/reflektion och sammanfattning när boktypen passar.

För `factbook`: prioritera begriplig ämnesstruktur, korrekt fakta, konkreta exempel, fördjupningar och läsarintresse. Kapitel får använda ingress/nyfikenhetsväckare, huvudförklaring, centrala fakta, fall/exempel, faktarutor och sammanfattning. Övningar och quiz är valfria.


## Källor och faktakontroll
Alla projekt har `docs/kallpolicy.md` och `docs/faktakontroll.md`. Använd dem aktivt när innehållet bygger på externa, aktuella, omstridda eller lätt föränderliga fakta. Faktaböcker ska tidigt få en rimlig källpolicy. Arbetsnoteringar om källor ska hållas utanför exporterad kapiteltext om inte boken uttryckligen ska ha synliga referenser/källförteckning. Använd webben när färsk verifiering behövs och capability finns.


## Obligatorisk inledning
Varje bok ska ha `chapters/00-inledning.md` med vad boken handlar om, målgrupp, antagna förkunskaper eller förväntad läsarnivå, upplägg och hur boken kan användas.


## Omslag och illustrationer
Fråga alltid om omslagsbild. Omslagsprompten ska inkludera titel och författare; undertitel om den finns och användaren vill det. Inre illustrationer skapas endast efter uttryckligt ja. Använd bild-ID:n som `IMG-03-02`, registrera i `docs/illustration-plan.md`, lägg prompts i `assets/image-prompts/` och referera bilder i markdown. Inre bilder ska normalt vara rena illustrationer utan text, ram, A4-layout eller affischkänsla.


## Kvalitet
Kontrollera rätt kvalitetsprofil: pedagogik/progression för lärobok; ämnestäckning, begriplighet, källor och faktakontroll för faktabok. Var alltid konsekvent med terminologi, exempel och nivå/djup. För tekniska böcker: föredra moderna, körbara exempel och markera antaganden.


### Läsarfärdig text – obligatorisk slutläsning
Prioritera saklighet, läsbarhet och koncentration framför att fylla ut mot ett sidmål. Efter faktagranskningen ska hela den exporterade boktexten slutläsas – även inledning, sammanfattningar, övergångar och källregister – för att upptäcka formuleringar riktade till författare eller redaktör, exempelvis "det fortsatta bokarbetet" och "inför publicering". Ersätt dem med upplysningar till läsaren eller flytta arbetsuppgifter till `docs/`. Rättsliga tidsavgränsningar och faktiska verksamhetsrekommendationer ska däremot bevaras.

Kontrollera också separat rubricerade granskningsavsnitt, exempelvis **Redaktionell granskning**, **Kapitelnoteringar**, **Redaktionell källanmärkning** och **Kvarstående faktakontroll**. Sådana avsnitt hör normalt hemma i `docs/`, inte i exporterad boktext. Tvetydiga omnämnanden i löptext kan vara sakligt motiverade och ska bedömas i sitt sammanhang snarare än automatiskt raderas.


## Kodgenererade diagram i kapitel
När ett godkänt kapitel behöver tekniska diagram: använd Skillen `diagram-illustrationer` för `.dot`, `.puml` och handgjord SVG. Återanvänd `IMG-NN-MM`, register och alt-/bildtext. Länka till verkligt genererade och verifierade SVG-filer med relativ sökväg; använd aldrig en bild som inte har renderats. Bevara befintligt AI-bildflöde utan förändring.
