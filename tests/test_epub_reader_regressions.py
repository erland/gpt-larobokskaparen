#!/usr/bin/env python3
"""Regressions for dark mode, excessive pages and duplicate figure captions."""
from __future__ import annotations
import importlib.util
import re
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
POST=ROOT/'templates/bokprojekt/publishing/fix-epub-after-pandoc.py'
EXPORT=ROOT/'templates/bokprojekt/scripts/export-book.py'

class EpubRegressionTests(unittest.TestCase):
    def test_pandoc_implicit_figures_are_disabled_for_both_exports(self):
        text=EXPORT.read_text(encoding="utf-8")
        self.assertGreaterEqual(text.count("-implicit_figures"),2)
        self.assertIn("image_transform_for('epub'",text)
        self.assertIn("image_transform_for('pdf'",text)
    def test_css_is_valid_and_readers_control_colours(self):
        s=(ROOT/'templates/bokprojekt/publishing/epub.css').read_text(encoding="utf-8")
        self.assertEqual(s.count('{'),s.count('}'))
        self.assertNotRegex(s,r'#[0-9a-fA-F]{6}')
    def test_postprocessing_removes_forced_colours_and_h1_pagebreak(self):
        spec=importlib.util.spec_from_file_location("epub_fix",POST)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/"EPUB/styles/stylesheet1.css";p.parent.mkdir(parents=True)
            p.write_text("""html {color: #1a1a1a; background-color: #fdfdfd;}
html {
 color: #1a1a1a;
 background-color: #fdfdfd;
}
h1 { page-break-before: always; }
h1 {
 page-break-before: always;
}
a { color: #1a1a1a; }
""",encoding="utf-8")
            self.assertEqual(mod.normalize_reader_css(Path(t)),1)
            s=p.read_text(encoding="utf-8")
            self.assertNotIn("color: #1a1a1a",s)
            self.assertNotIn("background-color: #fdfdfd",s)
            self.assertNotIn("page-break-before: always",s)
    def test_no_implicit_figures_caption_in_pandoc_integration(self):
        import shutil,subprocess
        pandoc=shutil.which("pandoc")
        if not pandoc: self.skipTest("Pandoc not installed")
        with tempfile.TemporaryDirectory() as t:
            p=Path(t);(p/'picture.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"><rect width="20" height="20" fill="white"/></svg>')
            md=p/'test.md';md.write_text('# Provkapitel\n\n![Beskrivande alt-text](picture.svg)\n\n*Figur 1. Avsedd bildtext.*\n',encoding="utf-8")
            ep=p/'test.epub'
            subprocess.run([pandoc,str(md),'--from=markdown+pipe_tables+fenced_code_blocks+fenced_divs-implicit_figures','--to=epub3','--output',str(ep)],check=True)
            with zipfile.ZipFile(ep) as z:
                html="\n".join(z.read(n).decode() for n in z.namelist() if n.endswith('.xhtml'))
            self.assertEqual(html.count('Figur 1. Avsedd bildtext.'),1)
            self.assertIn('alt="Beskrivande alt-text"',html)
            self.assertNotIn('<figcaption',html)
if __name__=='__main__':unittest.main()
