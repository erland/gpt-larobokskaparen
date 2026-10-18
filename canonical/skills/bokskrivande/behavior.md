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


## Valbar kvalitetsgranskning efter varje kapitel
Efter att en kapitelrevision skapats erbjud två tydliga alternativ: **1. Jag granskar själv** (vänta på synpunkter/godkännande) och **2. Granska, korrigera och godkänn automatiskt** (rekommenderat). Visa inte att en knapp har skapats om värdmiljön saknar klickbart stöd; presentera då alternativen som text. Fråga inte igen efter val i samma granskningsomgång.

Vid automatisk granskning: läs hela kapitlet och relevant bokcanon/källpolicy; kontrollera målgrupp, struktur, pedagogik/ämnestäckning, språk, fakta, källor, illustrationer och läsarfärdig text. Gör nödvändiga korrigeringar i högst två omgångar, kontrollera resultatet igen och kör tillgängliga deterministiska kontroller. Skapa granskningsprotokoll enligt `docs/reviews/README.md` och använd `scripts/chapter_review.py` för status och versionbundet godkännande. Märk aldrig okontrollerad fakta som verifierad och fabricera inte källor eller tester. Godkänn automatiskt bara när samtliga tillämpliga kontroller är godkända, inga blockerare återstår och integritet/revision är verifierad. Annars markera `changes_needed`, redovisa öppna frågor och be om vägledning. Vid manuell granskning godkänner användaren uttryckligen; aldrig automatiskt. Godkänt betyder intern redaktionell granskning, inte oberoende faktagranskning.
