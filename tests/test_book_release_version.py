#!/usr/bin/env python3
"""Release tag controls effective build metadata, not tracked book.yaml."""
import importlib.util
from pathlib import Path
root=Path(__file__).resolve().parents[1]
path=root/'templates/bokprojekt/scripts/export-book.py'
spec=importlib.util.spec_from_file_location('book_export_release',path)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
original='title: Test\nversion: "0.4.3"\nauthor: Example\n'
assert mod.export_metadata(original,None)==original
effective=mod.export_metadata(original,'v0.5.2')
assert 'version: "0.5.2"' in effective
assert 'version: "0.4.3"' not in effective
assert 'version: "0.4.3"' in original
assert mod.export_metadata('title: Test\n','v1.2.3').startswith('version: "1.2.3"')
try:
    mod.export_metadata(original,'not-a-tag')
    raise AssertionError('Invalid release tag must be rejected')
except SystemExit:
    pass
workflow=(root/'templates/bokprojekt/.github/workflows/03-release.yml').read_text(encoding='utf-8')
assert 'BOOK_RELEASE_TAG:' in workflow
assert 'Verify release version matches book.yaml' not in workflow
print('PASS: release metadata follows tag without modifying book.yaml')
