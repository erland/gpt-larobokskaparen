#!/usr/bin/env python3
"""Run a real isolated file-system smoke test using the built Plugin archive.

This does not prove execution inside the ChatGPT Plugin host.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", required=True, type=Path)
    args = ap.parse_args()
    report = {"host_execution_verified": False, "separate_engine_required": False, "checks": {}, "errors": []}
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        try:
            with zipfile.ZipFile(args.archive) as z:
                if z.testzip():
                    raise ValueError("Plugin ZIP is corrupt")
                prefix = "skills/bokprojekt-publicering/"
                bundle_path = prefix + "assets/19-project-template-bundle.md"
                if bundle_path not in z.namelist():
                    raise ValueError("Packaged project template bundle is missing")
                bundle = z.read(bundle_path).decode("utf-8")
                # Materialize every canonical text file from the packed bundle.
                # No repository template directory is needed at runtime.
                sections = re.findall(
                    r"^## `([^`]+)`\\s*\\n````[^\\n]*\\n(.*?)\\n````",
                    bundle, flags=re.MULTILINE | re.DOTALL,
                )
                if not sections:
                    raise ValueError("Packaged project template bundle has no files")
                target = base / "bokprojekt"
                for name, content in sections:
                    relative = Path(name)
                    if relative.is_absolute() or ".." in relative.parts:
                        raise ValueError("Unsafe template path")
                    dest = target / relative
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_text(content + "\\n", encoding="utf-8")
                report["checks"]["materialize_book_template"] = "pass"
                for script in ("project_integrity.py", "validate_project.py", "export-book.py", "build_book.py"):
                    embedded = prefix + "scripts/" + script
                    if embedded not in z.namelist() or z.read(embedded) != (target / "scripts" / script).read_bytes():
                        raise ValueError(f"Missing or different script: {script}")
                report["checks"]["packaged_scripts_match_template"] = "pass"
            meta = target / "book.yaml"
            source = meta.read_text(encoding="utf-8")
            source = source.replace('title: ""', 'title: "Självtest"').replace('author: ""','author: "Test"').replace('project_slug: ""','project_slug: "självtest"')
            meta.write_text(source, encoding="utf-8")
            intro = target / "chapters" / "00-inledning.md"
            intro.write_text("# Inledning\n\nDetta är ett automatiskt självtest.\n", encoding="utf-8")
            cmd = [sys.executable, str(target / "scripts" / "project_integrity.py")]
            def run(*args):
                p = subprocess.run([*cmd, *args], cwd=target, capture_output=True, text=True)
                if p.returncode:
                    raise RuntimeError((p.stderr or p.stdout).strip())
                return p.stdout.strip()
            run("init", str(target), "--slug", "självtest", "--zip-name", "självtest-projekt.zip")
            run("verify", str(target))
            report["checks"]["init_and_integrity_verify"] = "pass"
            archive = base / "självtest-projekt.zip"
            with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
                for p in sorted(target.rglob("*")):
                    if p.is_file():
                        z.write(p, p.relative_to(target))
            with zipfile.ZipFile(archive) as z:
                if z.testzip() or "project-manifest.json" not in z.namelist():
                    raise ValueError("Produced project ZIP is invalid")
            report["checks"]["create_portable_book_zip"] = "pass"
            report["dependencies"] = {
                "pandoc": bool(shutil.which("pandoc")),
                "xelatex": bool(shutil.which("xelatex")),
            }
            report["checks"]["epub_pdf_export"] = "available_but_not_executed" if all(report["dependencies"].values()) else "unavailable_optional_tools"
        except (OSError, ValueError, RuntimeError, zipfile.BadZipFile) as exc:
            report["errors"].append(str(exc))
    report["result"] = "fail" if report["errors"] else "pass"
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["errors"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
