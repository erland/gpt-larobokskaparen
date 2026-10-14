#!/usr/bin/env python3
"""Regressionstest för redaktionella arbetsmarkörer och globala käll-ID."""
import importlib.util
import re
from pathlib import Path
from tempfile import TemporaryDirectory

root=Path(__file__).resolve().parents[1]
path=root/'templates/bokprojekt/scripts/validate_project.py'
spec=importlib.util.spec_from_file_location('book_validation',path)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

for bad in ('under det fortsatta bokarbetet', 'måste kontrolleras inför publicering',
            'redaktionell anmärkning'):
    assert any(re.search(pattern,bad,re.I) for pattern in mod.EDITORIAL_PATTERNS),bad

with TemporaryDirectory() as td:
    chapter=Path(td)/'01-inledning.md'
    sources=Path(td)/'99-kallregister.md'
    chapter.write_text('# 1. Inledning\n\n[K001] och [K002]\n',encoding='utf-8')
    sources.write_text('# Källor\n\n- **[K001]** Källa 1\n',encoding='utf-8')
    assert any('K002' in e for e in mod.source_register_errors([chapter,sources]))
    sources.write_text('# Källor\n\n- **[K001]** Källa 1\n- **[K002]** Källa 2\n',encoding='utf-8')
    assert not mod.source_register_errors([chapter,sources])
    sources.write_text(sources.read_text(encoding='utf-8')+'- **[K001]** Dubblett\n',encoding='utf-8')
    assert any('Dubbelt' in e for e in mod.source_register_errors([chapter,sources]))
print('PASS: editorial and global source reference regressions')
