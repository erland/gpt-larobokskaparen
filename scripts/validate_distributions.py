#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_KNOWLEDGE = [
    "01-purpose-and-workflow.md", "02-guided-interview.md", "03-difficulty-and-pedagogy-model.md",
    "04-book-specification-template.md", "05-chapter-plan-template.md", "06-chapter-template.md",
    "07-canon-and-continuity.md", "08-quality-checklist.md", "09-project-status-template.md",
    "10-export-metadata-template.md", "11-book-type-patterns.md", "12-bilingual-style-guide.md",
    "13-example-prompts.md", "14-suggested-project-structure.md", "15-export-and-rendering-rules.md",
    "16-illustration-and-cover-workflow.md", "17-canonical-markdown-and-render-contract.md",
    "18-local-export-pipeline.md",
]
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_zip(path: Path) -> dict[str, bytes]:
    with zipfile.ZipFile(path) as zf:
        bad = zf.testzip()
        if bad:
            raise SystemExit(f"Korrupt ZIP {path.name}: {bad}")
        return {name: zf.read(name) for name in zf.namelist() if not name.endswith("/")}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dist-dir", default=str(ROOT / "dist"))
    p.add_argument("--version")
    args = p.parse_args()
    version = (args.version or (ROOT / "VERSION").read_text(encoding="utf-8")).strip()
    if version.startswith("v"):
        version = version[1:]
    if not SEMVER.fullmatch(version):
        raise SystemExit(f"Ogiltig version: {version}")

    dist = Path(args.dist_dir)
    custom_path = dist / f"larobokskaparen-custom-gpt-v{version}.zip"
    portable_path = dist / f"larobokskaparen-chat-v{version}.zip"
    for path in (custom_path, portable_path):
        if not path.is_file():
            raise SystemExit(f"Saknad distribution: {path}")

    custom = read_zip(custom_path)
    portable = read_zip(portable_path)

    if custom.get("VERSION") != (version + "\n").encode():
        raise SystemExit("Custom GPT-paketets VERSION matchar inte byggversionen")
    if portable.get("VERSION") != (version + "\n").encode():
        raise SystemExit("Portable-paketets VERSION matchar inte byggversionen")

    src_instr = (ROOT / "gpt-configuration/instructions.md").read_bytes()
    src_starters = (ROOT / "gpt-configuration/conversation-starters.md").read_bytes()
    if custom.get("gpt-configuration/instructions.md") != src_instr:
        raise SystemExit("Custom GPT instructions har ändrats")
    if custom.get("gpt-configuration/conversation-starters.md") != src_starters:
        raise SystemExit("Custom GPT conversation starters har ändrats")
    if portable.get("assistant/instructions.md") != src_instr:
        raise SystemExit("Portable instructions är inte byte-identisk med originalet")

    for name in EXPECTED_KNOWLEDGE:
        source = (ROOT / "knowledge-upload" / name).read_bytes()
        if custom.get(f"knowledge-upload/{name}") != source:
            raise SystemExit(f"Custom GPT Knowledge ändrad: {name}")
        if portable.get(f"knowledge/{name}") != source:
            raise SystemExit(f"Portable Knowledge ändrad: {name}")

    try:
        manifest = json.loads(portable["MANIFEST.json"].decode("utf-8"))
    except Exception as exc:
        raise SystemExit(f"Ogiltigt MANIFEST.json: {exc}")
    if manifest.get("version") != version:
        raise SystemExit("MANIFEST.json version matchar inte")
    expected_manifest_knowledge = [f"knowledge/{n}" for n in EXPECTED_KNOWLEDGE]
    if manifest.get("knowledge") != expected_manifest_knowledge:
        raise SystemExit("MANIFEST.json har fel Knowledge-lista")
    for entry in manifest.get("files", []):
        name = entry["path"]
        data = portable.get(name)
        if data is None:
            raise SystemExit(f"Manifestet refererar saknad fil: {name}")
        if digest(data) != entry["sha256"]:
            raise SystemExit(f"SHA-256 mismatch: {name}")

    print(f"OK: distributionerna för {version} är validerade.")
    print("OK: Instructions, conversation starters och 18 Knowledge-filer är byte-identiska med källorna.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
