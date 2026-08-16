# Mall: bok- och exportmetadata

`book.yaml` är enda kanoniska metadatafilen i nya projekt. `book_kind` är huvudprofil; `book_type` är underformen.

```yaml
title: ""
subtitle: ""
author: ""
language: "sv"
book_kind: "textbook" # textbook | factbook
book_type: "complete_textbook"
difficulty: "beginner" # beginner | basic | experienced | advanced
audience: ""
edition: "1"
version: "0.1"
date: ""
rights: "All rights reserved"
publisher: ""
cover_image: ""
identifier: ""
subject: ""
description: ""
project_slug: ""
chapters:
  - chapters/00-inledning.md
exports:
  epub:
    enabled: true
    include_text_toc: false
    toc_depth: 1
  pdf:
    enabled: true
    include_toc_before_introduction: true
    toc_depth: 3
```

## Tillåtna exempel på `book_type`
`textbook`: `complete_textbook`, `coursebook`, `practical_handbook`, `workshop_book`, `certification_book`, `quick_guide`.

`factbook`: `general_factbook`, `popular_science`, `childrens_factbook`, `narrative_nonfiction`, `subject_overview`, `reference_factbook`.

## Obligatoriskt före EPUB/PDF
- `title`, `author`, `language`, `identifier`, `date` och `version` är ifyllda.
- `book_kind` är giltigt och `book_type` passar profilen.
- `chapters` börjar med `chapters/00-inledning.md` och anger verkliga kapitel i rätt ordning.
