#!/usr/bin/env python3
"""Regression test for canonical PDF image placement. Run: python3 tests/test_pdf_illustrations.py"""
from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILTER = ROOT / "templates/bokprojekt/publishing/pdf-filter.lua"
TEMPLATE = ROOT / "templates/bokprojekt/publishing/pdf-template.tex"


@unittest.skipUnless(shutil.which("pandoc"), "Pandoc required for Lua integration")
class PDFIllustrationTests(unittest.TestCase):
    def test_images_stay_in_source_order_with_one_caption_each(self):
        md = """# 1. Exempel

Text före första bilden.

![Första bildtexten](first.pdf)

Text mellan bilderna.

![Andra bildtexten](second.pdf)

Text efter andra bilden.
"""
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "book.md"
            source.write_text(md, encoding="utf-8")
            result = subprocess.run(
                ["pandoc", str(source), "--from=markdown-implicit_figures",
                 "--to=latex", "--lua-filter", str(FILTER)],
                capture_output=True, text=True, check=True,
            )
        tex = result.stdout
        self.assertEqual(tex.count(r"\bookinlineillustration{"), 2, tex)
        self.assertNotIn(r"\begin{figure}", tex)
        self.assertNotIn(r"\caption{", tex)
        self.assertEqual(tex.count("Första bildtexten"), 1)
        self.assertEqual(tex.count("Andra bildtexten"), 1)
        tokens = ["Text före första bilden", "first.pdf", "Text mellan bilderna",
                  "second.pdf", "Text efter andra bilden"]
        positions = [tex.index(item) for item in tokens]
        self.assertEqual(positions, sorted(positions), tex)

    def test_template_keeps_figure_and_caption_together(self):
        tex = TEMPLATE.read_text(encoding="utf-8")
        start = tex.index(r"\newcommand{\bookinlineillustration}")
        end = tex.index(r"\begin{document}", start)
        implementation = tex[start:end]
        self.assertIn(r"\begin{minipage}", implementation)
        self.assertIn(r"\end{minipage}", implementation)
        self.assertIn(r"keepaspectratio", implementation)
        self.assertIn(r"\textheight", implementation)
        self.assertNotIn(r"\begin{figure}", implementation)


if __name__ == "__main__":
    unittest.main()
