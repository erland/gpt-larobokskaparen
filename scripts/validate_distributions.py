#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
    "01-purpose-and-workflow.md", "02-guided-interview.md", "03-difficulty-and-pedagogy-model.md",
    "04-book-specification-template.md", "05-chapter-plan-template.md", "06-chapter-template.md",
    "07-canon-and-continuity.md", "08-quality-checklist.md", "09-project-status-template.md",
    "10-export-metadata-template.md", "11-book-type-patterns.md", "12-bilingual-style-guide.md",
    "13-example-prompts.md", "14-suggested-project-structure.md", "15-export-and-rendering-rules.md",
    "16-illustration-and-cover-workflow.md", "17-canonical-markdown-and-render-contract.md",
    "18-local-export-pipeline.md", "19-project-template-bundle.md",
]
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
STALE_TERMS = ("docs/pedagogisk-canon.md", "docs/export-metadata.yaml", "docs/book-specification.md", "docs/chapter-plan.md", "chapters/kapitelmall.md")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_zip(path: Path) -> dict[str, bytes]:
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad:
            raise SystemExit(f"Korrupt ZIP {path.name}: {bad}")
        return {name: archive.read(name) for name in archive.namelist() if not name.endswith("/")}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Kan inte läsa Python-modul: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_export_order(template_root: Path) -> None:
    with tempfile.TemporaryDirectory() as td:
        work = Path(td) / "book"
        shutil.copytree(template_root, work)
        (work / "chapters/01-ett.md").write_text("# Ett\n", encoding="utf-8")
        (work / "chapters/02-tva.md").write_text("# Två\n", encoding="utf-8")
        yaml = (work / "book.yaml").read_text(encoding="utf-8")
        yaml = yaml.replace(
            "chapters:\n  - chapters/00-inledning.md",
            "chapters:\n  - chapters/00-inledning.md\n  - chapters/02-tva.md\n  - chapters/01-ett.md",
        )
        (work / "book.yaml").write_text(yaml, encoding="utf-8")
        module = load_module(work / "scripts/export-book.py", "test_export_book")
        paths = module.resolve_chapters(module.read_book_yaml())
        got = [path.name for path in paths]
        expected = ["00-inledning.md", "02-tva.md", "01-ett.md"]
        if got != expected:
            raise SystemExit(f"Exportordningen följer inte book.yaml: {got}")


def validate_duplicate_chapter_guard(template_root: Path) -> None:
    module = load_module(template_root / "scripts/project_integrity.py", "test_project_integrity")
    files = {
        "chapters/01-ett.md": {"sha256": "a"},
        "chapters/01-annat.md": {"sha256": "b"},
    }
    try:
        module.summary(files)
    except ValueError:
        return
    raise SystemExit("project_integrity.py stoppar inte dubbla kapitelnummer")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist-dir", default=str(ROOT / "dist"))
    parser.add_argument("--version")
    args = parser.parse_args()

    build_module = load_module(ROOT / "scripts/build_distributions.py", "build_distributions_for_validation")
    version = build_module.resolve_version(args.version)


    if (ROOT / "VERSION").exists():
        raise SystemExit("Repositoryt får inte ha en incheckad VERSION-fil; release-taggen är versionskälla")
    root_workflow=(ROOT / ".github/workflows/build-distributions.yml").read_text(encoding="utf-8")
    if "github.event.release.tag_name" not in root_workflow or "< VERSION" in root_workflow:
        raise SystemExit("Distributionsworkflowet använder inte release-taggen som versionskälla")

    knowledge = sorted(path.name for path in (ROOT / "knowledge-upload").glob("*.md"))
    if len(knowledge) > 20:
        raise SystemExit(f"Custom GPT har {len(knowledge)} Knowledge-filer; max är 20")
    if knowledge != EXPECTED:
        raise SystemExit(f"Fel Knowledge-lista: {knowledge}")

    instructions = (ROOT / "gpt-configuration/instructions.md").read_text(encoding="utf-8")
    if len(instructions) > 8000:
        raise SystemExit(f"Instructions är {len(instructions)} tecken; max 8000")
    required_instruction_terms = ("book_kind", "textbook", "factbook", "docs/kallpolicy.md", "docs/faktakontroll.md", "book.yaml")
    missing_terms = [term for term in required_instruction_terms if term not in instructions]
    if missing_terms:
        raise SystemExit(f"Instructions saknar centrala termer: {missing_terms}")
    if re.search(r"GPT-instruktioner\s+v\d+", instructions):
        raise SystemExit("Instructions innehåller en separat intern versionsetikett; release-taggen ska vara enda distributionsversionskälla")

    guidance_files = [ROOT / "gpt-configuration/instructions.md", ROOT / "examples/sample-book-project-structure.md"]
    guidance_files += [path for path in (ROOT / "knowledge-upload").glob("*.md") if path.name != "19-project-template-bundle.md"]
    stale = []
    for path in guidance_files:
        text = path.read_text(encoding="utf-8")
        for term in STALE_TERMS:
            if term in text:
                stale.append(f"{path.relative_to(ROOT)}: {term}")
    if stale:
        raise SystemExit("Utfasade strukturreferenser finns kvar: " + "; ".join(stale))

    template_root = ROOT / "templates/bokprojekt"
    for rel in (
        "chapters/kapitelmall-larobok.md", "chapters/kapitelmall-faktabok.md",
        "docs/kallpolicy.md", "docs/faktakontroll.md", "docs/innehalls-canon.md",
        "scripts/export-book.py", "scripts/project_integrity.py", "scripts/validate_project.py", "scripts/build_book.py",
        "publishing/epub.css", "publishing/fix-epub-after-pandoc.py", "publishing/pdf-template.tex", "publishing/pdf-filter.lua",
        ".github/workflows/01-validate.yml", ".github/workflows/02-build-preview.yml", ".github/workflows/03-release.yml",
    ):
        if not (template_root / rel).is_file():
            raise SystemExit(f"Saknad templatefil: {rel}")

    yaml = (template_root / "book.yaml").read_text(encoding="utf-8")
    if not re.search(r'(?m)^book_kind:\s*"textbook"', yaml):
        raise SystemExit("book.yaml saknar default book_kind=textbook")
    if "chapters:\n  - chapters/00-inledning.md" not in yaml:
        raise SystemExit("book.yaml saknar kanonisk inledning som första kapitelpost")

    preview=(template_root / ".github/workflows/02-build-preview.yml").read_text(encoding="utf-8")
    release=(template_root / ".github/workflows/03-release.yml").read_text(encoding="utf-8")
    if "workflow_dispatch" not in preview or "actions/upload-artifact@v4" not in preview or "*.epub" not in preview or "*.pdf" not in preview:
        raise SystemExit("Preview-workflowet saknar gemensamt EPUB/PDF-artifact")
    if 'tags: ["v*"]' not in release or "gh release" not in release or "*.epub" not in release or "*.pdf" not in release:
        raise SystemExit("Release-workflowet saknar v*-tagg eller separata EPUB/PDF-assets")

    validate_export_order(template_root)
    validate_duplicate_chapter_guard(template_root)

    # Build-scriptet validerar samtidigt exakt templatefiluppsättning och bundle-synk.
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/build_distributions.py"), "--output-dir", str(Path(args.dist_dir) / ".validator-build"), "--version", version],
        check=True,
        stdout=subprocess.DEVNULL,
    )
    shutil.rmtree(Path(args.dist_dir) / ".validator-build", ignore_errors=True)

    dist = Path(args.dist_dir)
    custom_path = dist / f"larobokskaparen-custom-gpt-v{version}.zip"
    portable_path = dist / f"larobokskaparen-chat-v{version}.zip"
    for path in (custom_path, portable_path):
        if not path.is_file():
            raise SystemExit(f"Saknad distribution: {path}")

    custom = read_zip(custom_path)
    portable = read_zip(portable_path)
    if custom.get("VERSION") != (version + "\n").encode() or portable.get("VERSION") != (version + "\n").encode():
        raise SystemExit("VERSION mismatch")

    src_instructions = (ROOT / "gpt-configuration/instructions.md").read_bytes()
    starters = (ROOT / "gpt-configuration/conversation-starters.md").read_bytes()
    if custom.get("gpt-configuration/instructions.md") != src_instructions or portable.get("assistant/instructions.md") != src_instructions:
        raise SystemExit("Instructions mismatch")
    if custom.get("gpt-configuration/conversation-starters.md") != starters:
        raise SystemExit("Conversation starters mismatch")

    for name in EXPECTED:
        src = (ROOT / "knowledge-upload" / name).read_bytes()
        if custom.get("knowledge-upload/" + name) != src:
            raise SystemExit(f"Custom Knowledge mismatch: {name}")
        if portable.get("knowledge/" + name) != src:
            raise SystemExit(f"Portable Knowledge mismatch: {name}")

    for path in sorted(p for p in template_root.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"):
        rel = path.relative_to(template_root).as_posix()
        if portable.get("templates/bokprojekt/" + rel) != path.read_bytes():
            raise SystemExit(f"Portable template mismatch: {rel}")

    manifest = json.loads(portable["MANIFEST.json"].decode())
    if manifest.get("version") != version or manifest.get("template_root") != "templates/bokprojekt":
        raise SystemExit("MANIFEST metadata mismatch")
    if manifest.get("knowledge") != ["knowledge/" + name for name in EXPECTED]:
        raise SystemExit("MANIFEST Knowledge mismatch")
    for entry in manifest.get("files", []):
        if entry["path"] not in portable or digest(portable[entry["path"]]) != entry["sha256"]:
            raise SystemExit(f"MANIFEST SHA mismatch: {entry['path']}")

    print(f"OK: distributionerna för {version} är validerade.")
    print(f"OK: Instructions är {len(instructions)} tecken (max 8000); {len(knowledge)} Knowledge-filer (max 20).")
    print("OK: Custom/portable-filer och portabel template är byte-identiska med källorna.")
    print("OK: book.yaml styr exportordningen; dubbla kapitelnummer stoppas; utfasade strukturreferenser saknas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
