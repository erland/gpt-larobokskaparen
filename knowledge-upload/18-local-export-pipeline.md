# Lokal exportpipeline

Nya projekt innehåller `scripts/export-book.py` och `scripts/export-book.sh` samt styles för EPUB/PDF.

## Krav
- Export ska kunna köras utan AI.
- `book.yaml` är kanonisk metadata och ska innehålla giltig `book_kind` (`textbook` eller `factbook`).
- Exporten ska inte behandla arbetsfiler i `docs/` som boktext. Källpolicy och faktakontroll får alltså inte följa med av misstag.
- Boktext hämtas från kapitelordningen/kanoniska kapitelfiler.
- Canonical markdown ska valideras före renderering.
- EPUB ska ha navigerbar TOC men ingen synlig TOC-sida i läsflödet.
- PDF ska ha innehållsförteckning före inledningen.

Profilen påverkar innehåll och kvalitetskontroll men inte grundprincipen för EPUB/PDF-export.
