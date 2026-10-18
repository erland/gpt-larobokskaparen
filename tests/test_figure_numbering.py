#!/usr/bin/env python3
"""Canonical book figure numbering regressions (no Pandoc required)."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "templates/bokprojekt/scripts"))
from book_references import prepare


class FigureNumberingTest(unittest.TestCase):
    def test_numbering_references_and_formats(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            intro = root / "00-inledning.md"
            a = root / "01-webben.md"
            b = root / "02-natverk.md"
            intro.write_text("# Inledning\n\nIntroduktion.\n", encoding="utf-8")
            a.write_text("# 1. Webben\n\nSom Figur [@fig:IMG-01-02].\n\n"
                         "![DNS-flöde](../assets/generated/IMG-01-01.svg)\n\n"
                         "![Figur 9.9 – HTTP-svar](../assets/generated/IMG-01-02.svg)\n", encoding="utf-8")
            b.write_text("# 2. Nätverk\n\n"
                         "![Router och klient](../assets/images/IMG-02-01.png)\n", encoding="utf-8")
            chapters = [intro, a, b]
            epub = prepare(chapters)
            pdf = prepare(chapters, image_transform=lambda text, chapter: text.replace(".svg", ".pdf"))
            for output in (epub, pdf):
                self.assertIn("![Figur 1.1 – DNS-flöde]", output)
                self.assertIn("![Figur 1.2 – HTTP-svar]", output)
                self.assertIn("![Figur 2.1 – Router och klient]", output)
                self.assertIn("Som [Figur 1.2](#fig-img-01-02)", output)
                self.assertNotIn("Figur Figur", output)
                self.assertEqual(output.count("Figur 1.2 – HTTP-svar"), 1)
                self.assertNotIn("Figur 9.9", output)
            a.write_text("# 1. Webben\n\n"
                         "![HTTP-svar](../assets/generated/IMG-01-02.svg)\n\n"
                         "![DNS-flöde](../assets/generated/IMG-01-01.svg)\n", encoding="utf-8")
            reordered = prepare(chapters)
            self.assertIn("![Figur 1.1 – HTTP-svar]", reordered)
            self.assertIn("![Figur 1.2 – DNS-flöde]", reordered)

    def test_missing_reference_fails(self):
        with TemporaryDirectory() as directory:
            p = Path(directory) / "01-test.md"
            p.write_text("# 1. Test\n\nSe [@fig:IMG-01-99].\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "saknar illustration"):
                prepare([p])

    def test_duplicate_stable_id_fails(self):
        with TemporaryDirectory() as directory:
            p = Path(directory) / "01-test.md"
            p.write_text("# 1. Test\n\n![A](IMG-01-01.svg)\n\n![B](IMG-01-01.svg)\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "flera figurer"):
                prepare([p])


if __name__ == "__main__":
    unittest.main()
