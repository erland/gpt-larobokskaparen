#!/usr/bin/env python3
"""Legacy chapter naming and unnumbered appendix regression tests."""
import importlib.util
import tempfile
from pathlib import Path

base = Path(__file__).resolve().parents[1]/'templates/bokprojekt'
spec = importlib.util.spec_from_file_location('legacy_export',base/'scripts/export-book.py')
export = importlib.util.module_from_spec(spec)
spec.loader.exec_module(export)
original_root = export.ROOT
try:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root/'chapters').mkdir()
        files = {
            '00-inledning.md':'# Inledning\n',
            'varfor-arkitektur-01.md':'# Kapitel 1: Varför arkitektur\n',
            'design-02.md':'# Kapitel 2: Design\n',
            'appendix-a-verktyg.md':'# Appendix A: Verktyg\n',
            'bilaga-b-checklista.md':'# Bilaga B: Checklista\n',
            '99-kallregister.md':'# Källor\n'
        }
        for name,body in files.items():
            (root/'chapters'/name).write_text(body,encoding='utf-8')
        (root/'book.yaml').write_text('chapters:\n'+''.join('  - chapters/'+name+'\n' for name in files),encoding='utf-8')
        export.ROOT = root
        paths=export.resolve_chapters(export.read_book_yaml())
        assert [p.name for p in paths]==list(files)
        (root/'chapters'/'extra.md').write_text('# Extra\n',encoding='utf-8')
        try:
            export.resolve_chapters(export.read_book_yaml())
            raise AssertionError('Unlisted chapter should fail')
        except SystemExit:
            pass
finally:
    export.ROOT = original_root
print('PASS: legacy filenames, appendix order and book.yaml precedence')
