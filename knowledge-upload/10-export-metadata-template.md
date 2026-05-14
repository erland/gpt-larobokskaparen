# Mall: Exportmetadata

```yaml
title: ""
subtitle: ""
author: "" # obligatoriskt för EPUB/PDF; fråga användaren om det saknas
language: "sv" # sv eller en; ska matcha bokens språk och EPUB lang
difficulty: "beginner" # beginner, basic, experienced, advanced
audience: ""
book_type: "textbook"
edition: "1"
version: "0.1"
date: "" # YYYY-MM-DD
rights: "All rights reserved"
publisher: ""
cover_image: "" # valfritt
identifier: "" # t.ex. urn:uuid:<uuid>; krävs för robust EPUB-metadata
creator_role: "aut"
subject: ""
description: "" # kort bokbeskrivning för metadata
project_slug: ""
zip_naming:
  initial: "<bokslug>-projekt.zip"
  chapter_update: "<bokslug>-projekt-kapitel-NN.zip"
chapters:
  - chapters/00-inledning.md
  - chapters/01-forsta-kapitlet.md
exports:
  epub:
    enabled: true
    include_text_toc: false
    airy_layout: true
    render_markdown_styles: true
  pdf:
    enabled: true
    include_toc_before_introduction: true
    render_markdown_styles: true
  docx:
    enabled: true
    render_markdown_styles: true
  markdown:
    enabled: true
```

Använd metadata för reproducerbara exporter. Kapitelordning, titel, författare, språk och exportregler ska kunna återskapas från denna fil.

## Obligatoriskt innan EPUB/PDF-export
- `title` är ifylld.
- `author` är ifylld eller uttryckligen lämnat tomt av användaren.
- `language` är `sv` eller `en` och matchar bokens innehåll.
- `identifier` finns, helst `urn:uuid:<uuid>`.
- `date` och `version` är ifyllda.
- `chapters` innehåller `chapters/00-inledning.md` först och sedan kapitel i rätt ordning.
- Exportreglerna för EPUB/PDF är satta enligt projektets standard.
