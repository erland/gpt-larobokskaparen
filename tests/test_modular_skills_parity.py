#!/usr/bin/env python3
"""Deterministic structural and behavioral-contract tests for five distributions.

This deliberately does not claim to execute model responses inside the five hosts.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from lib.canonical_skill_sources import modules, projected_instruction
from lib.verify_modular_migration import inspect

EXPECTED = {"bokplanering", "bokskrivande", "bokprojekt-publicering"}
CASES = {
    "bokplanering": [
        ("book_kind", "textbook"),
        ("book_kind", "factbook"),
        ("Bokplan före projekt", "Skapa inte projekt-zip"),
        ("Välj bokprofil först", "Tvinga aldrig faktaböcker"),
    ],
    "bokskrivande": [
        ("Profilregler", "För `textbook`"),
        ("Profilregler", "För `factbook`"),
        ("Källor och faktakontroll", "docs/faktakontroll.md"),
        ("Omslag och illustrationer", "uttryckligt ja"),
    ],
    "bokprojekt-publicering": [
        ("Kanoniskt bokprojekt", "project-manifest.json"),
        ("Kanoniskt bokprojekt", "revisions"),
        ("Markdown och lokal export", "scripts/export-book.py"),
        ("EPUB/PDF", "XeLaTeX"),
    ],
}

def main():
    cfg = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    definitions = cfg["skills"]["definitions"]
    ids = [x["id"] for x in definitions]
    errors = []
    if len(ids) != len(set(ids)) or set(ids) != EXPECTED:
        errors.append("Wrong, duplicate, or missing canonical Skill IDs")
    if cfg["instructions"].get("mode") != "modular_skills":
        errors.append("Not in modular_skills mode")
    if cfg.get("runtime", {}).get("custom_gpt", {}).get("enabled"):
        errors.append("Legacy Custom GPT must not be active")
    for target in ("chat_zip", "plugin", "claude", "opencode"):
        if not cfg.get("runtime", {}).get(target, {}).get("enabled"):
            errors.append(f"Missing active runtime: {target}")
    core, parts = modules(ROOT, cfg, definitions)
    bodies = {item["id"]: body for item, body in parts}
    for skill, cases in CASES.items():
        body = bodies.get(skill, "")
        for heading, phrase in cases:
            if heading not in body or phrase not in body:
                errors.append(f"{skill}: missing behavioral invariant {heading!r}/{phrase!r}")
    projected = projected_instruction(ROOT, cfg, definitions)
    for skill, body in bodies.items():
        if body not in projected:
            errors.append(f"Canonical assembled instruction excludes {skill}")
    # Each skill body is owned exactly once. Merely packaging a copy does not
    # prove automatic Skill selection by a language model.
    for skill, body in bodies.items():
        for other, otherbody in bodies.items():
            if skill != other and body in otherbody:
                errors.append(f"Duplicate ownership: {skill} in {other}")
    version = sys.argv[1] if len(sys.argv) > 1 else None
    if version:
        archive = inspect(ROOT, cfg, version)
        errors += archive.get("errors", [])
        if archive.get("status") != "archive_content_verified_pending_host":
            errors.append(f"Archive-level parity not verified: {archive.get('status')}")
        if set(archive.get("checked_targets", {})) != {"chat", "plugin", "claude_project", "claude_skills", "opencode"}:
            errors.append("Not all five runtime archives checked")
    report = {
        "result": "fail" if errors else "pass",
        "level": "static behavioral contracts and distribution archive contents",
        "host_runtime_execution_verified": False,
        "skills": ids,
        "targets": ["chat", "plugin", "claude_project", "claude_skills", "opencode"],
        "checks": sum(len(v) for v in CASES.values()),
        "errors": errors,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
