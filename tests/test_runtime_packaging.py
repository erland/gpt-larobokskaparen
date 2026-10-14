#!/usr/bin/env python3
"""Regression checks for real delivered resources, not merely declared Skills."""
from pathlib import Path
import json
import re
import sys
import zipfile
import yaml

ROOT = Path(__file__).resolve().parents[1]
version = sys.argv[1]
cfg = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
dist = ROOT / "dist"
errors = []
script_names = ("project_integrity.py", "validate_project.py", "export-book.py", "build_book.py")
for name in script_names:
    expected = ROOT / "templates" / "bokprojekt" / "scripts" / name
    if not expected.is_file():
        errors.append(f"Missing book template tool: {expected}")

for target in ("plugin", "claude-skills", "opencode"):
    f = dist / f"larobokskaparen-{target}-{version}.zip"
    with zipfile.ZipFile(f) as z:
        names = set(z.namelist())
        skill_prefix = ".opencode/skills" if target == "opencode" else "skills"
        publication = f"{skill_prefix}/bokprojekt-publicering/"
        if publication + "assets/19-project-template-bundle.md" not in names:
            errors.append(f"{target}: canonical full project template asset missing")
        template_root = ROOT / "templates" / "bokprojekt"
        for source in template_root.rglob("*"):
            if not source.is_file() or "__pycache__" in source.parts or source.suffix in {".pyc", ".pyo"}:
                continue
            packaged = publication + "assets/bokprojekt/" + source.relative_to(template_root).as_posix()
            if packaged not in names:
                errors.append(f"{target}: missing actual project template file {packaged}")
            elif z.read(packaged) != source.read_bytes():
                errors.append(f"{target}: template file differs from source {packaged}")
        for name in script_names:
            found = publication + "scripts/" + name
            if found not in names:
                errors.append(f"{target}: {found} missing")
            elif z.read(found) != (ROOT / "templates" / "bokprojekt" / "scripts" / name).read_bytes():
                errors.append(f"{target}: {name} does not match canonical book template")
        if target in ("plugin", "claude-skills"):
            extra = [n for n in names if n.startswith(publication + "scripts/lib/")]
            if extra:
                errors.append(f"{target}: unexpected GPT Builder helpers {extra}")
        if target == "opencode":
            checks = {
                "gpt_book_build.ts": ['"--output-dir"', 'cwd: projectRoot'],
                "gpt_book_export.ts": ['"--format"', '"--output-dir"'],
                "gpt_project_integrity.ts": ['"verify"', 'projectRoot'],
                "gpt_project_validation.ts": ['projectRoot'],
            }
            for name, markers in checks.items():
                path = ".opencode/tools/" + name
                if path not in names:
                    errors.append(f"Missing OpenCode adapter: {path}")
                    continue
                body = z.read(path).decode("utf-8")
                if '"--project-root"' in body:
                    errors.append(f"OpenCode adapter has unsupported global flag: {name}")
                for marker in markers:
                    if marker not in body:
                        errors.append(f"OpenCode adapter {name} missing {marker}")

print(json.dumps({"result": "fail" if errors else "pass", "package_checks": 3,
                  "manual_host_execution_verified": False, "errors": errors},
                 ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)
