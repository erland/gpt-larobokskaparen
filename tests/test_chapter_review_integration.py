#!/usr/bin/env python3
"""Integration: chapter review choices, correction cycle and revision tracking."""
from __future__ import annotations
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TEMPLATE=Path(__file__).resolve().parents[1]/"templates/bokprojekt"
CHECKS=("language","structure","consistency","audience","sources","facts","illustrations","editorial")

class ReviewIntegration(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)/"book"
        shutil.copytree(TEMPLATE,self.root)
        self.name="03-provkapitel.md"
        (self.root/"chapters"/self.name).write_text("# 3. Provkapitel\n\nEtt första utkast.\n",encoding="utf-8")
        (self.root/"book.yaml").write_text(
            (self.root/"book.yaml").read_text(encoding="utf-8").replace('title: ""','title: "Provbok"')
            .replace('author: ""','author: "Test"').replace('project_slug: ""','project_slug: "provbok"')
            .replace("  - chapters/00-inledning.md","  - chapters/00-inledning.md\n  - chapters/03-provkapitel.md"),encoding="utf-8")
        self.run_script("project_integrity.py","init",".","--slug","provbok","--zip-name","revision-1.zip")
    def tearDown(self): self.tmp.cleanup()
    def run_script(self,file,*args,success=True):
        p=subprocess.run([sys.executable,str(self.root/"scripts"/file),*args],cwd=self.root,capture_output=True,text=True)
        if success and p.returncode: self.fail(f"{file} {args}: {p.stdout}\n{p.stderr}")
        return p
    def report(self,**changes):
        record={"checks":{k:"passed" for k in CHECKS},"blockers":[],"summary":"Kapitlet granskat och korrigerat."}
        record.update(changes)
        dest=Path(self.tmp.name)/"evidence.json"
        dest.write_text(json.dumps(record),encoding="utf-8")
        return dest
    def commit(self,expected):
        self.run_script("project_integrity.py","commit",".","--expected-revision",str(expected),
            "--operation","Kapitelgranskning","--zip-name",f"revision-{expected+1}.zip",
            "--allow","chapters/03-provkapitel.md","--allow","docs/reviews/**")
        self.run_script("project_integrity.py","verify",".")
        self.run_script("validate_project.py",".")
    def test_auto_review_corrects_approves_and_revisions(self):
        self.run_script("chapter_review.py","start",self.name,"--mode","auto")
        path=self.root/"chapters"/self.name
        path.write_text("# 3. Provkapitel\n\nGranskat och korrigerat innehåll.\n",encoding="utf-8")
        self.run_script("chapter_review.py","approve",self.name,"--mode","auto","--report",str(self.report()))
        record=json.loads((self.root/"docs/reviews/03-provkapitel.json").read_text())
        self.assertEqual(record["status"],"approved_auto")
        self.assertEqual(record["chapter_sha256"],__import__("hashlib").sha256(path.read_bytes()).hexdigest())
        self.commit(1)
        path.write_text("# 3. Provkapitel\n\nÄndrad efter godkännande.\n",encoding="utf-8")
        result=self.run_script("chapter_review.py","check",self.name,success=False)
        self.assertNotEqual(result.returncode,0)
    def test_manual_requires_explicit_approval(self):
        self.run_script("chapter_review.py","start",self.name,"--mode","manual")
        result=self.run_script("chapter_review.py","approve",self.name,"--mode","manual",success=False)
        self.assertNotEqual(result.returncode,0)
        self.run_script("chapter_review.py","approve",self.name,"--mode","manual","--approved-by","Användaren")
        self.commit(1)
        record=json.loads((self.root/"docs/reviews/03-provkapitel.json").read_text())
        self.assertEqual(record["status"],"approved_manual")
    def test_blockers_stop_approval_and_record_changes_needed(self):
        self.run_script("chapter_review.py","start",self.name,"--mode","auto")
        blocked=self.report(blockers=["Källa saknas"])
        result=self.run_script("chapter_review.py","approve",self.name,"--mode","auto","--report",str(blocked),success=False)
        self.assertNotEqual(result.returncode,0)
        self.run_script("chapter_review.py","block",self.name,"--report",str(blocked))
        record=json.loads((self.root/"docs/reviews/03-provkapitel.json").read_text())
        self.assertEqual(record["status"],"changes_needed")
        self.commit(1)
    def test_legacy_no_review_record(self):
        self.run_script("validate_project.py",".")

if __name__=="__main__": unittest.main()
