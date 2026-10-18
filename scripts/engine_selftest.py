#!/usr/bin/env python3
"""Verify an extracted Lärobokskaparen Engine ZIP, optionally render with PlantUML."""
from __future__ import annotations
import argparse, hashlib, json, shutil, subprocess, tempfile, zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
JAR = ROOT / ".engine-deps" / "plantuml.jar"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--render", action="store_true")
    args = p.parse_args()
    manifest = json.loads((ROOT / "engine-package.json").read_text(encoding="utf-8"))
    assert manifest["engine_id"] == "larobokskaparen"
    assert manifest["version"]
    listed = manifest["files"]
    assert listed and all(not Path(name).is_absolute() and ".." not in Path(name).parts for name in listed)
    for name, expected in listed.items():
        actual = ROOT / name
        assert actual.is_file(), f"Missing Engine file: {name}"
        assert hashlib.sha256(actual.read_bytes()).hexdigest() == expected, f"Hash mismatch: {name}"
    for name in manifest["required_files"]:
        assert name in listed, f"Required Engine resource missing: {name}"
    for name in ("templates/bokprojekt/scripts/export-book.py",
                 "templates/bokprojekt/scripts/render_diagrams.py",
                 "templates/bokprojekt/scripts/project_integrity.py"):
        assert name in listed
    assert JAR.is_file()
    assert hashlib.sha256(JAR.read_bytes()).hexdigest() == "aa4a1d06f8911c4b842beff4828dd955be431692b631a312d04c0e9fab9581de"
    with zipfile.ZipFile(JAR) as z:
        assert z.testzip() is None
        assert "META-INF/MANIFEST.MF" in z.namelist()
    if args.render:
        java = shutil.which("java")
        if not java:
            print("PENDING: Java is unavailable; Engine hashes PASS, rendering not verified")
            return 0
        with tempfile.TemporaryDirectory() as d:
            cmd = [java, "-Djava.awt.headless=true", "-jar", str(JAR), "-tsvg", "-pipe"]
            source = b"@startuml\nskinparam backgroundColor white\nAlice -> Bob: Test\n@enduml\n"
            result = subprocess.run(cmd, input=source, capture_output=True, timeout=90, check=True)
            node = ET.fromstring(result.stdout)
            assert node.tag.endswith("svg"), "No SVG returned"
    print("PASS: canonical Engine resources, PlantUML SHA-256 and optional rendering")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
