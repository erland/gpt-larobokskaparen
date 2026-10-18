#!/usr/bin/env python3
"""Check reproducible Engine config and pinned PlantUML metadata."""
from pathlib import Path
import yaml
root = Path(__file__).resolve().parents[1]
cfg = yaml.safe_load((root / "gpt-project.yaml").read_text())
engine = cfg["engine"]
assert engine["enabled"] is True
assert "templates/bokprojekt" in engine["resources"]
assert ".engine-deps/plantuml.jar" in engine["resources"]
assert "scripts/engine_selftest.py" == engine["selftest"]
assert "scripts/engine_selftest.py" in engine["required_files"]
assert (root / engine["selftest"]).is_file()
print("PASS: Engine config and pinned resources")
