# Exportguide

Exporten använder `book.yaml`, `scripts/export-book.py` och styles under `styles/`.

```bash
python3 scripts/export-book.py
```

För EPUB/PDF krävs Pandoc. PDF kräver dessutom en Pandoc-kompatibel PDF-engine, som XeLaTeX, om inte exporteraren anpassats till annan engine.
