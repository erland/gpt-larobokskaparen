#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT / "knowledge-upload"
CONFIG_DIR = ROOT / "gpt-configuration"
EXAMPLES_DIR = ROOT / "examples"
PORTABLE_DIR = ROOT / "portable"
DEFAULT_VERSION_FILE = ROOT / "VERSION"
EXPECTED_KNOWLEDGE = [
    "01-purpose-and-workflow.md",
    "02-guided-interview.md",
    "03-difficulty-and-pedagogy-model.md",
    "04-book-specification-template.md",
    "05-chapter-plan-template.md",
    "06-chapter-template.md",
    "07-canon-and-continuity.md",
    "08-quality-checklist.md",
    "09-project-status-template.md",
    "10-export-metadata-template.md",
    "11-book-type-patterns.md",
    "12-bilingual-style-guide.md",
    "13-example-prompts.md",
    "14-suggested-project-structure.md",
    "15-export-and-rendering-rules.md",
    "16-illustration-and-cover-workflow.md",
    "17-canonical-markdown-and-render-contract.md",
    "18-local-export-pipeline.md",
]
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
ZIP_DT = (1980, 1, 1, 0, 0, 0)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_version(explicit: str | None) -> str:
    version = explicit.strip() if explicit else DEFAULT_VERSION_FILE.read_text(encoding="utf-8").strip()
    if version.startswith("v"):
        version = version[1:]
    if not SEMVER.fullmatch(version):
        raise SystemExit(f"Ogiltig version: {version!r}. Förväntat SemVer, t.ex. 1.0.0.")
    return version


def validate_sources() -> None:
    required = [
        CONFIG_DIR / "instructions.md",
        CONFIG_DIR / "conversation-starters.md",
        PORTABLE_DIR / "START-HERE.md",
    ]
    for path in required:
        if not path.is_file():
            raise SystemExit(f"Saknad källfil: {path.relative_to(ROOT)}")

    actual = sorted(p.name for p in KNOWLEDGE_DIR.glob("*.md"))
    if actual != EXPECTED_KNOWLEDGE:
        missing = sorted(set(EXPECTED_KNOWLEDGE) - set(actual))
        extra = sorted(set(actual) - set(EXPECTED_KNOWLEDGE))
        raise SystemExit(f"Fel Knowledge-uppsättning. Saknas={missing}, extra={extra}")


def copy_tree_files(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    for path in sorted(p for p in src.rglob("*") if p.is_file()):
        target = dst / path.relative_to(src)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def build_custom(stage: Path, version: str) -> None:
    shutil.copy2(ROOT / "README.md", stage / "README.md")
    (stage / "VERSION").write_text(version + "\n", encoding="utf-8")
    copy_tree_files(CONFIG_DIR, stage / "gpt-configuration")
    copy_tree_files(KNOWLEDGE_DIR, stage / "knowledge-upload")
    copy_tree_files(EXAMPLES_DIR, stage / "examples")


def build_portable(stage: Path, version: str) -> None:
    shutil.copy2(PORTABLE_DIR / "START-HERE.md", stage / "START-HERE.md")
    (stage / "VERSION").write_text(version + "\n", encoding="utf-8")
    (stage / "assistant").mkdir(parents=True, exist_ok=True)
    shutil.copy2(CONFIG_DIR / "instructions.md", stage / "assistant" / "instructions.md")
    copy_tree_files(KNOWLEDGE_DIR, stage / "knowledge")
    copy_tree_files(EXAMPLES_DIR, stage / "examples")

    files = []
    for path in sorted(p for p in stage.rglob("*") if p.is_file() and p.name != "MANIFEST.json"):
        files.append({
            "path": path.relative_to(stage).as_posix(),
            "sha256": sha256(path),
        })
    manifest = {
        "package": "larobokskaparen",
        "format": "portable-chat-assistant",
        "version": version,
        "entrypoint": "START-HERE.md",
        "instructions": "assistant/instructions.md",
        "knowledge": [f"knowledge/{name}" for name in EXPECTED_KNOWLEDGE],
        "files": files,
    }
    (stage / "MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def deterministic_zip(source_dir: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(p for p in source_dir.rglob("*") if p.is_file()):
            rel = path.relative_to(source_dir).as_posix()
            info = zipfile.ZipInfo(rel, ZIP_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(ROOT / "dist"))
    parser.add_argument("--version", help="Explicit SemVer. Release-workflow skickar taggens version här.")
    args = parser.parse_args()

    validate_sources()
    version = resolve_version(args.version)
    output_dir = Path(args.output_dir).resolve()
    work = output_dir / ".build"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    custom_stage = work / "custom"
    portable_stage = work / "portable"
    custom_stage.mkdir()
    portable_stage.mkdir()
    build_custom(custom_stage, version)
    build_portable(portable_stage, version)

    custom_zip = output_dir / f"larobokskaparen-custom-gpt-v{version}.zip"
    portable_zip = output_dir / f"larobokskaparen-chat-v{version}.zip"
    deterministic_zip(custom_stage, custom_zip)
    deterministic_zip(portable_stage, portable_zip)
    shutil.rmtree(work)

    print(f"Byggd: {custom_zip}")
    print(f"Byggd: {portable_zip}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
