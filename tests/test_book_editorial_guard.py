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

# Headings that describe editorial process must be blocking, including variants.
for heading in ('## Redaktionell granskning', '### Kapitelnoteringar',
                '## Redaktionell källanmärkning', '### Granskningsanteckningar',
                '## Arbetsanteckningar', '## Kvarstående faktakontroll',
                '## Att kontrollera inför publicering'):
    errs,warns=mod.editorial_quality_findings('# Kapitel 1\n'+heading+'\n')
    assert errs, heading

# Ordinary prose is not necessarily a defect: warn without failing.
errs,warns=mod.editorial_quality_findings(
    '# Kapitel 1\nRapporten genomgick redaktionell granskning under 2026.\n')
assert not errs and warns
# Actual subject-matter recommendations must not trigger a false positive.
errs,warns=mod.editorial_quality_findings(
    '# Kapitel 1\nMyndigheten behöver kontrollera behörighet och följa rättsläget.\n')
assert not errs and not warns

print('PASS: editorial and global source reference regressions')
