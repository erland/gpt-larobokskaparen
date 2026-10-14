#!/usr/bin/env python3
"""Prepare book-global source navigation without modifying original Markdown."""
from __future__ import annotations
import re
from pathlib import Path

ENTRY = re.compile(r'(?m)^(\s*[-*]\s*)\*\*\[(K\d{3})\]\*\*')
REF = re.compile(r'(?<![\w\[])\[(K\d{3})\](?!\(|\])')
URL = re.compile(r'(?<!\]\()https?://[^\s<>)]+')


def prepare(chapters: list[Path]) -> str:
    texts = [path.read_text(encoding='utf-8').strip() for path in chapters]
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
