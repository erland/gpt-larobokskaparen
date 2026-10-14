#!/usr/bin/env python3
"""Regression tests for source navigation, export validation and layout profiles."""
import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT/'templates/bokprojekt/scripts'
sys.path.insert(0, str(SCRIPTS))


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS/filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


references = load('book_references', 'book_references.py')
export = load('book_export', 'export-book.py')
validation = load('export_validation', 'validate_exports.py')
assert export.pdf_size({}) == ('170mm', '240mm')
assert export.pdf_size({'pdf_size': 'a5'}) == ('148mm', '210mm')
try:
    export.pdf_size({'pdf_size': 'letter'})
    raise AssertionError('Unsupported page format must fail')
except SystemExit:
    pass

with TemporaryDirectory() as dirname:
    base = Path(dirname)
    chapter = base/'01-test.md'
    register = base/'99-kallregister.md'
    chapter.write_text('# 1. Test\n\nText [K001] med hänvisning.\n', encoding='utf-8')
    register.write_text('# Källor\n\n- **[K001]** Testkälla. https://example.org/source\n', encoding='utf-8')
    converted = references.prepare([chapter, register])
    assert '[K001](#k001)' in converted
    assert '[]{#k001}' in converted
    assert '[Öppna källan](https://example.org/source)' in converted
    chapter.write_text('# 1. Test\n\n[K999]\n', encoding='utf-8')
    try:
        references.prepare([chapter, register])
        raise AssertionError('Missing global source ID must fail')
    except ValueError:
        pass

    # Tiny valid EPUB3-shaped package; link validation must catch broken anchors.
    epub = base/'sample.epub'
    def sample(href):
        opf = ('<package xmlns="http://www.idpf.org/2007/opf" version="3.0">'
               '<manifest><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>'
               '<item id="chapter" href="chapter.xhtml" media-type="application/xhtml+xml"/></manifest>'
               '<spine><itemref idref="nav" linear="no"/><itemref idref="chapter"/></spine></package>')
        container = ('<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                     '<rootfiles><rootfile full-path="OPS/book.opf" /></rootfiles></container>')
        xhtml = ('<html xmlns="http://www.w3.org/1999/xhtml"><body>'
                 '<h1 id="k001">Source</h1><a href="' + href + '">Jump</a></body></html>')
        with zipfile.ZipFile(epub, 'w') as z:
            z.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
            z.writestr('META-INF/container.xml', container)
            z.writestr('OPS/book.opf', opf)
            z.writestr('OPS/nav.xhtml', '<html xmlns="http://www.w3.org/1999/xhtml"><body/></html>')
            z.writestr('OPS/chapter.xhtml', xhtml)
    sample('#k001')
    assert validation.check_epub(epub)['internal_links'] == 1
    sample('#does-not-exist')
    try:
        validation.check_epub(epub)
        raise AssertionError('Broken reference must fail')
    except ValueError:
        pass

print('PASS: source anchors, layout formats and EPUB link integrity')
