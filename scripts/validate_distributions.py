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

import yaml

ROOT = Path(__file__).resolve().parents[1]
CFG_PATH = ROOT / "gpt-project.yaml"
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

def load_config() -> dict:
    data=yaml.safe_load(CFG_PATH.read_text(encoding="utf-8"))
    if not isinstance(data,dict):
        raise SystemExit("Ogiltig gpt-project.yaml")
    return data

def active_runtimes(cfg: dict) -> list[str]:
    return [
        runtime_id
        for runtime_id,runtime_cfg in (cfg.get("runtime") or {}).items()
        if isinstance(runtime_cfg,dict) and runtime_cfg.get("status")=="active"
    ]

def artifact_path(cfg: dict, runtime_id: str, version: str, dist: Path) -> Path:
    pattern=cfg["runtime"][runtime_id].get("artifact_name")
    if not pattern:
        raise SystemExit(f"Runtime {runtime_id} saknar artifact_name")
    return dist/pattern.format(version=version)


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

    cfg=load_config()
    build_module = load_module(ROOT / "scripts/build_distributions.py", "build_distributions_for_validation")
    version = build_module.resolve_version(args.version)
    runtimes=active_runtimes(cfg)
    unsupported=sorted(set(runtimes)-{"custom_gpt","chatgpt_chat","claude_projects","opencode","openai_plugin"})
    if unsupported:
        raise SystemExit("Aktiv runtime saknar valideringsadapter: " + ", ".join(unsupported))


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
    expected_paths={runtime_id: artifact_path(cfg,runtime_id,version,dist) for runtime_id in runtimes}
    expected_names={p.name for p in expected_paths.values()}
    actual_names={p.name for p in dist.glob("*.zip")}
    if actual_names != expected_names:
        raise SystemExit(f"Fel distributionsmängd: actual={sorted(actual_names)} expected={sorted(expected_names)}")
    custom_path=expected_paths["custom_gpt"]
    portable_path=expected_paths["chatgpt_chat"]
    claude_path=expected_paths["claude_projects"]
    opencode_path=expected_paths["opencode"]
    plugin_path=expected_paths["openai_plugin"]
    custom = read_zip(custom_path)
    portable = read_zip(portable_path)
    claude = read_zip(claude_path)
    opencode = read_zip(opencode_path)
    plugin = read_zip(plugin_path)
    if custom.get("VERSION") != (version + "\n").encode() or portable.get("VERSION") != (version + "\n").encode() or claude.get("VERSION") != (version + "\n").encode() or opencode.get("VERSION") != (version + "\n").encode():
        raise SystemExit("VERSION mismatch")

    custom_cfg=cfg["runtime"]["custom_gpt"]
    chat_cfg=cfg["runtime"]["chatgpt_chat"]
    src_instructions = (ROOT / custom_cfg["instruction"]["source"]).read_bytes()
    starters = (ROOT / custom_cfg["conversation_starters"]).read_bytes()
    claude_cfg=cfg["runtime"]["claude_projects"]
    opencode_cfg=cfg["runtime"]["opencode"]
    if custom.get(custom_cfg["instruction"]["source"]) != src_instructions or portable.get("assistant/instructions.md") != (ROOT/chat_cfg["source"]["instructions"]).read_bytes() or claude.get("assistant/instructions.md") != (ROOT/claude_cfg["source"]["instructions"]).read_bytes() or opencode.get("assistant/instructions.md") != (ROOT/opencode_cfg["source"]["instructions"]).read_bytes():
        raise SystemExit("Instructions mismatch")
    if custom.get(custom_cfg["conversation_starters"]) != starters:
        raise SystemExit("Conversation starters mismatch")

    for name in EXPECTED:
        src = (ROOT / "knowledge-upload" / name).read_bytes()
        if custom.get("knowledge-upload/" + name) != src:
            raise SystemExit(f"Custom Knowledge mismatch: {name}")
        if portable.get("knowledge/" + name) != src:
            raise SystemExit(f"Portable Knowledge mismatch: {name}")
        if claude.get("knowledge/" + name) != src:
            raise SystemExit(f"Claude Knowledge mismatch: {name}")
        if opencode.get("knowledge/" + name) != src:
            raise SystemExit(f"OpenCode Knowledge mismatch: {name}")

    for path in sorted(p for p in template_root.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"):
        rel = path.relative_to(template_root).as_posix()
        if portable.get("templates/bokprojekt/" + rel) != path.read_bytes():
            raise SystemExit(f"Portable template mismatch: {rel}")
        if claude.get("templates/bokprojekt/" + rel) != path.read_bytes():
            raise SystemExit(f"Claude template mismatch: {rel}")
        if opencode.get("templates/bokprojekt/" + rel) != path.read_bytes():
            raise SystemExit(f"OpenCode template mismatch: {rel}")

    manifest = json.loads(portable["MANIFEST.json"].decode())
    claude_manifest = json.loads(claude["MANIFEST.json"].decode())
    opencode_manifest = json.loads(opencode["MANIFEST.json"].decode())
    plugin_cfg=cfg["runtime"]["openai_plugin"]
    plugin_root=plugin_cfg["manifest"]["name"] + "/"
    plugin_manifest=json.loads(plugin[plugin_root+"plugin.json"].decode())
    skill_path=plugin_root+"skills/"+plugin_cfg["skill"]["id"]+"/SKILL.md"
    if plugin_manifest.get("$schema")!="https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        raise SystemExit("Plugin schema mismatch")
    if plugin_manifest.get("version")!=version or plugin_manifest.get("name")!=plugin_cfg["manifest"]["name"]:
        raise SystemExit("Plugin manifest metadata mismatch")
    if skill_path not in plugin:
        raise SystemExit("Plugin SKILL.md saknas")
    skill_text=plugin[skill_path].decode("utf-8")
    if "## Kanoniskt beteendekontrakt" not in skill_text or "Påstå aldrig att ett ZIP-projekt" not in skill_text:
        raise SystemExit("Plugin skill saknar canonical/runtime-gap-kontrakt")
    allowed_script_prefix=plugin_root+"skills/"+plugin_cfg["skill"]["id"]+"/references/templates/bokprojekt/"
    unexpected_python=[name for name in plugin if name.endswith(".py") and not name.startswith(allowed_script_prefix)]
    if unexpected_python:
        raise SystemExit("Plugin-distributionen innehåller Python utanför bokprojektmallen: "+", ".join(sorted(unexpected_python)))
    if plugin_root+"mcp.json" in plugin:
        raise SystemExit("Plugin-distributionen får inte påstå en MCP-integration som inte finns")
    if manifest.get("version") != version or manifest.get("template_root") != "templates/bokprojekt":
        raise SystemExit("MANIFEST metadata mismatch")
    if claude_manifest.get("version") != version or claude_manifest.get("format") != "claude-projects" or claude_manifest.get("template_root") != "templates/bokprojekt":
        raise SystemExit("Claude MANIFEST metadata mismatch")
    if opencode_manifest.get("version") != version or opencode_manifest.get("format") != "opencode" or opencode_manifest.get("template_root") != "templates/bokprojekt":
        raise SystemExit("OpenCode MANIFEST metadata mismatch")
    if manifest.get("knowledge") != ["knowledge/" + name for name in EXPECTED]:
        raise SystemExit("MANIFEST Knowledge mismatch")
    for entry in manifest.get("files", []):
        if entry["path"] not in portable or digest(portable[entry["path"]]) != entry["sha256"]:
            raise SystemExit(f"MANIFEST SHA mismatch: {entry['path']}")

    # Pluginen ska bära samma Knowledge, exempel och bokprojektmall som baslinjen.
    skill_ref=plugin_root+"skills/"+plugin_cfg["skill"]["id"]+"/references/"
    for name in EXPECTED:
        src=(ROOT/"knowledge-upload"/name).read_bytes()
        if plugin.get(skill_ref+"knowledge/"+name)!=src:
            raise SystemExit(f"Plugin Knowledge mismatch: {name}")
    for path in sorted(p for p in template_root.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"):
        rel=path.relative_to(template_root).as_posix()
        if plugin.get(skill_ref+"templates/bokprojekt/"+rel)!=path.read_bytes():
            raise SystemExit(f"Plugin template mismatch: {rel}")
    canonical=(ROOT/plugin_cfg["skill"]["source_instruction"]).read_text(encoding="utf-8").strip()
    if canonical not in skill_text:
        raise SystemExit("Plugin skill bäddar inte in canonical instruktion")

    print(f"OK: distributionerna för {version} är validerade.")
    print(f"OK: Instructions är {len(instructions)} tecken (max 8000); {len(knowledge)} Knowledge-filer (max 20).")
    print("OK: Custom/portable-filer och portabel template är byte-identiska med källorna.")
    print("OK: book.yaml styr exportordningen; dubbla kapitelnummer stoppas; utfasade strukturreferenser saknas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
