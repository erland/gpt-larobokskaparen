# Bokprojekt

Detta projekt är skapat från Lärobokskaparens kanoniska projektmall och stödjer både lärobok (`textbook`) och faktabok (`factbook`).

## Arbetsflöde
1. Ange `book_kind` och `book_type` samt övrig metadata i `book.yaml`.
2. Planera boken i `docs/bokspecifikation.md` och `docs/kapitelplan.md`.
3. Skriv inledningen i `chapters/00-inledning.md`.
4. Använd `kapitelmall-larobok.md` för lärobok eller `kapitelmall-faktabok.md` för faktabok när nya kapitel skapas.
5. Håll canon, terminologi, källpolicy, faktakontroll och projektstatus synkroniserade vid behov.
6. Verifiera före och efter ändringar med `scripts/project_integrity.py`.
7. Bygg EPUB/PDF reproducerbart med `scripts/export-book.py`.

Arbetsnoteringar i `docs/` är inte boktext och ska inte exporteras om de inte uttryckligen införs i bokens kapitel eller källförteckning.
