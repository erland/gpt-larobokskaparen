# Bokprojekt

Detta projekt är skapat från Lärobokskaparens kanoniska projektmall.

## Arbetsflöde
1. Håll bokmetadata i `book.yaml`.
2. Planera boken i `docs/bokspecifikation.md` och `docs/kapitelplan.md`.
3. Skriv inledningen i `chapters/00-inledning.md` och övriga kapitel som `NN-kort-slug.md`.
4. Håll pedagogik, terminologi och projektstatus synkroniserade i `docs/`.
5. Verifiera projektet före och efter ändringar med `scripts/project_integrity.py`.
6. Bygg EPUB/PDF reproducerbart med `scripts/export-book.py`.

`project-manifest.json` skapas/aktiveras med `init` när ett nytt konkret projekt instansieras från mallen.
