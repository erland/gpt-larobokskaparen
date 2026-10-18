#!/usr/bin/env python3
"""Regression för manuellt/automatiskt versionsbundet kapitelgodkännande."""
from __future__ import annotations
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT=Path(__file__).resolve().parents[1]/"templates/bokprojekt/scripts/chapter_review.py"
spec=importlib.util.spec_from_file_location("chapter_review",SCRIPT)
review=importlib.util.module_from_spec(spec)
spec.loader.exec_module(review)

class ChapterReviewTest(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        (self.root/"chapters").mkdir()
        (self.root/"docs"/"reviews").mkdir(parents=True)
        self.filename="03-test.md"
        (self.root/"chapters"/self.filename).write_text("# Kapitel 3\n\nText.\n",encoding="utf-8")
        self.previous=review.ROOT
        review.ROOT=self.root
    def tearDown(self):
        review.ROOT=self.previous
        self.temp.cleanup()
    def test_auto_requires_all_controls(self):
        record={"status":"approved_auto","chapter_sha256":review.digest(review.chapter_path(self.filename)),
                "checks":{k:"passed" for k in review.REQUIRED},"summary":"Granskat","blockers":[]}
        self.assertEqual(review.validate(self.filename,record),[])
        record["checks"]["facts"]="failed"
        self.assertTrue(review.validate(self.filename,record))
        record["checks"]["facts"]="passed"
        record["blockers"]=["Faktauppgift ej verifierad"]
        self.assertTrue(review.validate(self.filename,record))
    def test_hash_invalidates_approval(self):
        record={"status":"approved_manual","approved_by":"Läsaren",
                "chapter_sha256":review.digest(review.chapter_path(self.filename))}
        self.assertFalse(review.validate(self.filename,record))
        review.chapter_path(self.filename).write_text("# Kapitel 3\n\nNy text.\n",encoding="utf-8")
        self.assertIn("Granskningsprotokollet avser en annan kapitelversion",review.validate(self.filename,record))
    def test_optional_review_and_source_justification(self):
        self.assertEqual(review.validate(self.filename,{}),[])
        record={"status":"approved_auto","chapter_sha256":review.digest(review.chapter_path(self.filename)),
                "checks":{k:"passed" for k in review.REQUIRED},"summary":"Granskat","blockers":[]}
        record["checks"]["sources"]="not_applicable"
        self.assertTrue(review.validate(self.filename,record))
        record["source_justification"]="Kapitlet innehåller inga externa påståenden."
        self.assertFalse(review.validate(self.filename,record))

if __name__=="__main__": unittest.main()
