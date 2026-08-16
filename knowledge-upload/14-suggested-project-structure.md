# Kanonisk projektstruktur

För nya projekt är `templates/bokprojekt/` single source of truth och återges i `19-project-template-bundle.md`.

```text
<bokslug>-projekt/
  README.md
  book.yaml
  project-manifest.json
  revision-log.md
  project-index.md
  docs/
    bokspecifikation.md
    kapitelplan.md
    innehalls-canon.md
    kallpolicy.md
    faktakontroll.md
    projektstatus.md
    quality-checklist.md
    illustration-plan.md
    export-guide.md
  chapters/
    00-inledning.md
    kapitelmall-larobok.md
    kapitelmall-faktabok.md
    NN-kort-slug.md
  exercises/
  examples/
  code/
  assets/
  styles/
  scripts/
  exports/
```

## Profilregler
- `book.yaml: book_kind` väljer `textbook` eller `factbook`.
- `book_type` anger underform inom profilen.
- Båda profilerna använder samma projektformat och revisionsmodell.
- Endast relevant kapitelmall används när boktext skapas.
- `docs/kallpolicy.md` och `docs/faktakontroll.md` finns i alla projekt men används särskilt aktivt för faktaböcker och tidskänsligt innehåll.

## Äldre projekt
Fungerande äldre struktur behöver inte migreras enbart för kosmetisk enhetlighet. Normalisering görs när användaren ber om det eller när en ny funktion kräver den.
