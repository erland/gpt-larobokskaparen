# Kvalitetschecklista

## Gemensamt
- [ ] Språk, ton och nivå/djup är konsekventa.
- [ ] Begrepp och fakta motsäger inte canon.
- [ ] Onödiga upprepningar och luckor är hanterade.

## Lärobok (`textbook`)
- [ ] Förkunskaper respekteras.
- [ ] Lärandemål och övningar matchar innehållet när boktypen kräver dem.
- [ ] Begrepp och svårighetsgrad utvecklas i rimlig ordning.

## Faktabok (`factbook`)
- [ ] Ämnestäckning och faktadjup passar målgruppen.
- [ ] Fakta, tolkning och osäkerhet hålls isär.
- [ ] Käll- och faktakontroll är tillräcklig för ämnet.
- [ ] Tidskänsliga uppgifter är aktuella.
- [ ] Engagerande förenklingar är fortfarande sakligt korrekta.

## Teknik
- [ ] Kod är körbar eller märkt som pseudokod.
- [ ] Versioner och antaganden är dokumenterade.

## Export
- [ ] `book.yaml` är komplett och kapitelordningen stämmer.
- [ ] Canonical markdown är validerad.
- [ ] Arbetsnoteringar från `docs/` exporteras inte av misstag.

## Gransknings- och godkännandegrind
Efter kapitelskrivning väljs manuell eller automatisk granskning. Vid automatisk granskning krävs dokumenterat resultat för: `language`, `structure`, `consistency`, `audience`, `sources`, `facts`, `illustrations`, `editorial`. Varje kontroll märks `passed`, `failed` eller `not_applicable` med motivering för käll- och faktakontroll som ej tillämpliga. Blockerande brister tillåter inte automatiskt godkännande. Gör högst två korrigeringsomgångar och rapportera kvarstående hinder.
Granskningsprotokoll finns i `docs/reviews/`, och `scripts/chapter_review.py` kontrollerar godkännandestatus mot kapitlets SHA-256. Kontrollera projektintegriteten efter revisionsuppdatering. Ett internt automatiskt godkännande är inte likvärdigt med oberoende faktagranskning.
