#!/usr/bin/env python3
"""Prepare book-global source navigation without modifying original Markdown."""
from __future__ import annotations
import re
from pathlib import Path

ENTRY = re.compile(r'(?m)^(\s*[-*]\s*)\*\*\[(K\d{3})\]\*\*')
REF = re.compile(r'(?<![\w\[])\[(K\d{3})\](?!\(|\])')
URL = re.compile(r'(?<!\]\()https?://[^\s<>)]+')


def prepare(chapters: list[Path], image_transform=None) -> str:
    texts = [path.read_text(encoding='utf-8').strip() for path in chapters]
    texts = number_figures(texts, chapters)
    if image_transform is not None:
        texts = [image_transform(text, path) for text, path in zip(texts, chapters)]
    registers = [i for i, p in enumerate(chapters)
                 if 'kall' in p.name.lower() or 'käll' in p.name.lower()]
    ids = set()
    for index in registers:
        for match in ENTRY.finditer(texts[index]):
            code = match.group(2)
            if code in ids:
                raise ValueError(f'Dubbelt käll-ID: {code}')
            ids.add(code)
    output = []
    for index, chapter in enumerate(texts):
        if index in registers:
            # The source entry becomes an anchor target; all other occurrences
            # of Kxxx become internal links rather than their own targets.
            chapter = ENTRY.sub(
                lambda m: m.group(1) + '[]{#' + m.group(2).lower() + '} **['
                + m.group(2) + ']**', chapter)
            chapter = URL.sub(lambda m: '[Öppna källan](' + m.group(0) + ')', chapter)
        else:
            def resolve(match):
                code = match.group(1)
                if code not in ids:
                    raise ValueError(f'Saknat käll-ID: {code}')
                return '[' + code + '](#' + code.lower() + ')'
            chapter = REF.sub(resolve, chapter)
        output.append(chapter)
    return '\n\n'.join(output) + '\n'

# Figure captions belong to the publishing representation, never to chapter sources.
# Only standalone Markdown images become numbered figures. The stable IMG ID is
# extracted from the asset name (including diagram SVG/PDF conversions).
FIGURE = re.compile(r'(?m)^(?P<indent>[ \t]*)!\[(?P<alt>[^\]\n]*)\]\((?P<target>[^)\n]+)\)[ \t]*$')
FIGURE_ID = re.compile(r'(?i)(IMG-\d{2}-\d{2})(?=\.[A-Za-z0-9]+(?:\s|$))')
FIGURE_REFERENCE = re.compile(r'\[@fig:(IMG-\d{2}-\d{2})\]', re.I)
OLD_CAPTION = re.compile(r'(?i)^\s*Figur\s+\d+(?:\.\d+)?\s*[-–—:.]\s*')


def number_figures(texts: list[str], chapters: list[Path]) -> list[str]:
    """Number figures per chapter in book.yaml order and resolve stable-ID links.

    The published caption is the image alt/caption string, shared by EPUB and
    PDF. Leave image URLs and source files untouched. Keep descriptive alt text
    after the generated number; never expose internal IMG IDs as caption text.
    """
    labels = {}
    numbered = []
    for chapter_index, (chapter, body) in enumerate(zip(chapters, texts)):
        heading = re.search(r'(?m)^#\s+(?:Kapitel\s+)?(\d+)\s*[.:]\s+', body, re.I)
        chapter_number = int(heading.group(1)) if heading else chapter_index
        count = 0

        def replace(match):
            nonlocal count
            target = match.group('target')
            # Ignore remote links and decorative images embedded within prose.
            count += 1
            label = f'Figur {chapter_number}.{count}'
            name = FIGURE_ID.search(target)
            ident = name.group(1).upper() if name else None
            caption = OLD_CAPTION.sub('', match.group('alt')).strip()
            if not caption:
                raise ValueError(f'Bildtext saknas i {chapter.name}, figur {label}')
            if ident:
                if ident in labels:
                    raise ValueError(f'Bild-ID används för flera figurer: {ident}')
                labels[ident] = (label, f'fig-{ident.lower()}')
            image = f"![{label} – {caption}]({target})"
            if ident:
                return f"[]{{#fig-{ident.lower()}}}\n\n" + image
            return image

        numbered.append(FIGURE.sub(replace, body))

    def resolve(match):
        ident = match.group(1).upper()
        if ident not in labels:
            raise ValueError(f'Figurhänvisning saknar illustration: {ident}')
        label, anchor = labels[ident]
        return f'[{label}](#{anchor})'

    # Figure reference token already includes the Swedish noun 'Figur'.
    # Avoid 'Figur Figur 1.1' in prose written with an explicit prefix.
    return [FIGURE_REFERENCE.sub(resolve, re.sub(r'(?i)\bFigur[ \t]+(?=\[@fig:IMG-\d{2}-\d{2}\])', '', body)) for body in numbered]
