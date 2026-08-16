#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
NUMBERED_CHAPTER_RE = re.compile(r"^\d{2}-[a-z0-9][a-z0-9-]*\.md$", re.I)


def scalar(text: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(?:\"([^\"]*)\"|'([^']*)'|([^#\n]*))", text)
    if not m:
        return ""
    return next((g for g in m.groups() if g is not None), "").strip()


def read_book_yaml() -> str:
    path = ROOT / "book.yaml"
    if not path.is_file():
        raise SystemExit("Saknar book.yaml")
    return path.read_text(encoding="utf-8")


def metadata(text: str) -> dict[str, str]:
    keys = ("title", "subtitle", "author", "language", "identifier", "date", "version", "book_kind", "book_type")
    values = {key: scalar(text, key) for key in keys}
    missing = [key for key in ("title", "author", "language", "book_kind", "book_type") if not values[key]]
    if missing:
        raise SystemExit("Saknad metadata i book.yaml: " + ", ".join(missing))
    if values["book_kind"] not in ("textbook", "factbook"):
        raise SystemExit("Ogiltig book_kind i book.yaml: " + values["book_kind"])
    return values


def chapter_entries(text: str) -> list[str]:
    lines = text.splitlines()
    start = None
    base_indent = 0
    for i, line in enumerate(lines):
        m = re.match(r"^(\s*)chapters:\s*(?:#.*)?$", line)
        if m:
            start = i + 1
            base_indent = len(m.group(1))
            break
    if start is None:
        raise SystemExit("book.yaml saknar chapters:-lista")

    entries: list[str] = []
    for line in lines[start:]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if indent <= base_indent and not line.lstrip().startswith("-"):
            break
        m = re.match(r"^\s*-\s*(?:\"([^\"]+)\"|'([^']+)'|([^#\n]+?))\s*(?:#.*)?$", line)
        if not m:
            if indent > base_indent:
                raise SystemExit(f"Ogiltig post under chapters: i book.yaml: {line.strip()}")
            break
        value = next(g for g in m.groups() if g is not None).strip()
        entries.append(value)
    if not entries:
        raise SystemExit("chapters: i book.yaml är tom")
    return entries


def resolve_chapters(text: str) -> list[Path]:
    entries = chapter_entries(text)
    if len(entries) != len(set(entries)):
        duplicates = sorted({x for x in entries if entries.count(x) > 1})
        raise SystemExit("Dubbellistade kapitel i book.yaml: " + ", ".join(duplicates))
    if entries[0] != "chapters/00-inledning.md":
        raise SystemExit("Första posten under chapters: ska vara chapters/00-inledning.md")

    paths: list[Path] = []
    for entry in entries:
        pure = PurePosixPath(entry)
        if pure.is_absolute() or ".." in pure.parts or len(pure.parts) != 2 or pure.parts[0] != "chapters":
            raise SystemExit(f"Ogiltig kapitelsökväg i book.yaml: {entry}")
        path = ROOT / pure.as_posix()
        if not path.is_file():
            raise SystemExit(f"Listad kapitelfil saknas: {entry}")
        if path.name.startswith("kapitelmall-"):
            raise SystemExit(f"Kapitelmall får inte exporteras: {entry}")
        paths.append(path)

    listed = {path.relative_to(ROOT).as_posix() for path in paths}
    unlisted = []
    for path in sorted((ROOT / "chapters").glob("*.md")):
        if not NUMBERED_CHAPTER_RE.fullmatch(path.name):
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel not in listed:
            unlisted.append(rel)
    if unlisted:
        raise SystemExit("Numrerade kapitelfiler finns men saknas i book.yaml: " + ", ".join(unlisted))
    return paths


def validate_markdown(paths: list[Path]) -> None:
    errors = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        if re.search(r"(?m)^#{4,}\s", text):
            errors.append(f"{path.name}: H4 eller djupare rubrik")
        if text.count("```") % 2:
            errors.append(f"{path.name}: obalanserade kodblock")
    if errors:
        raise SystemExit("Markdown-validering misslyckades:\n- " + "\n- ".join(errors))


def run(cmd: list[str]) -> None:
    print("+", " ".join(str(x) for x in cmd))
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=["epub", "pdf", "all"], default="all")
    args = parser.parse_args()
    if not shutil.which("pandoc"):
        raise SystemExit("Pandoc saknas. Installera Pandoc och kör igen.")

    book_yaml = read_book_yaml()
    metadata(book_yaml)
    chapters = resolve_chapters(book_yaml)
    validate_markdown(chapters)
    (ROOT / "exports").mkdir(exist_ok=True)

    with tempfile.TemporaryDirectory() as td:
        merged = Path(td) / "book.md"
        merged.write_text("\n\n".join(path.read_text(encoding="utf-8").strip() for path in chapters) + "\n", encoding="utf-8")
        common = ["pandoc", str(merged), "--from=gfm", "--metadata-file", str(ROOT / "book.yaml")]
        if args.format in ("epub", "all"):
            run(common + ["--to=epub3", "--toc", "--toc-depth=1", "--css", str(ROOT / "styles/epub.css"), "--output", str(ROOT / "exports/book.epub")])
        if args.format in ("pdf", "all"):
            run(common + ["--toc", "--toc-depth=3", "--output", str(ROOT / "exports/book.pdf")])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
