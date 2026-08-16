# Mall: bok- och exportmetadata

`book.yaml` är den enda kanoniska metadatafilen i nya projekt. Skapa inte en parallell `docs/export-metadata.yaml`. Äldre projekt som redan använder sådan metadata får behållas och migreras först när det behövs.

```yaml
title: ""
subtitle: ""
author: "" # obligatoriskt för EPUB/PDF; fråga användaren om det saknas
language: "sv" # sv eller en
difficulty: "beginner" # beginner, basic, experienced, advanced
audience: ""
book_type: "textbook"
edition: "1"
version: "0.1"
date: "" # YYYY-MM-DD
rights: "All rights reserved"
publisher: ""
cover_image: "" # valfritt
identifier: "" # t.ex. urn:uuid:<uuid>
creator_role: "aut"
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

## Obligatoriskt före EPUB/PDF
- `title`, `author`, `language`, `identifier`, `date` och `version` är ifyllda.
- `chapters` börjar med `chapters/00-inledning.md` och anger verkliga kapitel i rätt ordning.
- Exporten använder metadata från `book.yaml` och projektets styles/pipeline.
