#!/usr/bin/env python3
"""Spårbara kapitelgodkännanden; modellen utför själva sakgranskningen."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("language", "structure", "consistency", "audience", "sources", "facts", "illustrations", "editorial")
STATES = ("review_pending", "reviewing", "changes_needed", "approved_manual", "approved_auto")

def chapter_path(name):
    if not re.fullmatch(r"[0-9]{2}-[a-zA-Z0-9][a-zA-Z0-9-]*\.md", name):
        raise ValueError("Ange en giltig kapitelfil (NN-titel.md)")
    path = ROOT / "chapters" / name
    if not path.is_file(): raise ValueError(f"Kapitlet saknas: {name}")
    return path

def report_path(name):
    return ROOT / "docs" / "reviews" / (Path(name).stem + ".json")

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def timestamp():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def load(name):
    p=report_path(name)
    if not p.is_file(): return {}
    return json.loads(p.read_text(encoding="utf-8"))

def save(name,data):
    p=report_path(name); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")

def revision():
    p=ROOT/"project-manifest.json"
    if not p.is_file(): return None
    data=json.loads(p.read_text(encoding="utf-8"))
    return data.get("revision")

def validate(name,record):
    if not record: return []
    errors=[]
    path=chapter_path(name)
    if record.get("status") not in STATES: errors.append("Ogiltig granskningsstatus")
    if record.get("chapter_sha256")!=digest(path): errors.append("Granskningsprotokollet avser en annan kapitelversion")
    if record.get("status")=="approved_auto":
        checks=record.get("checks",{})
        missing=[k for k in REQUIRED if checks.get(k) not in ("passed","not_applicable")]
        if missing: errors.append("Saknade/underkända automatiska kvalitetskontroller: "+", ".join(missing))
        if checks.get("sources")=="not_applicable" and not record.get("source_justification"):
            errors.append("Källkontroll som ej tillämplig kräver motivering")
        if checks.get("facts")=="not_applicable" and not record.get("fact_justification"):
            errors.append("Faktakontroll som ej tillämplig kräver motivering")
        if record.get("blockers"): errors.append("Öppna blockerare hindrar automatiskt godkännande")
        if not record.get("summary"): errors.append("Sammanfattning krävs")
    if record.get("status")=="approved_manual" and not record.get("approved_by"):
        errors.append("Manuell granskning måste ha angiven godkännare")
    return errors

def main():
    parser=argparse.ArgumentParser()
    sub=parser.add_subparsers(dest="command",required=True)
    for command in ("start","approve","block","check"):
        p=sub.add_parser(command)
        p.add_argument("chapter")
        if command=="start": p.add_argument("--mode",choices=("manual","auto"),required=True)
        if command=="block": p.add_argument("--report",type=Path,required=True)
        if command=="approve":
            p.add_argument("--mode",choices=("manual","auto"),required=True)
            p.add_argument("--report",type=Path,help="JSON-protokoll med utförda kontroller")
            p.add_argument("--approved-by",help="Godkännare vid manuell granskning")
    args=parser.parse_args()
    try:
        path=chapter_path(args.chapter)
        if args.command=="check":
            errors=validate(args.chapter,load(args.chapter))
            if errors: raise ValueError("; ".join(errors))
            print("OK: granskningsstatus giltig"); return 0
        if args.command=="start":
            record={"chapter":args.chapter,"chapter_sha256":digest(path),
                    "status":"review_pending" if args.mode=="manual" else "reviewing",
                    "review_mode":args.mode,"updated_at":timestamp()}
        else:
            old=load(args.chapter)
            if not old: raise ValueError("Starta granskningsflödet med start först")
            if args.command=="block":
                evidence=json.loads(args.report.read_text(encoding="utf-8"))
                record={**old,**evidence,"chapter":args.chapter,"chapter_sha256":digest(path),
                        "status":"changes_needed","updated_at":timestamp()}
                save(args.chapter,record)
                print(f"OK: {args.chapter}: changes_needed"); return 0
            if old.get("review_mode")!=args.mode: raise ValueError("Granskningsläge matchar inte det påbörjade flödet")
            if args.mode=="auto":
                if not args.report: raise ValueError("Automatiskt godkännande kräver granskningsprotokoll --report")
                evidence=json.loads(args.report.read_text(encoding="utf-8"))
                record={**old,**evidence,"chapter":args.chapter,"chapter_sha256":digest(path),
                        "review_mode":"auto","status":"approved_auto","updated_at":timestamp(),
                        "project_revision_at_review":revision()}
            else:
                if not args.approved_by: raise ValueError("Ange --approved-by")
                record={**old,"chapter_sha256":digest(path),"status":"approved_manual",
                        "approved_by":args.approved_by,"updated_at":timestamp(),
                        "project_revision_at_review":revision()}
            errors=validate(args.chapter,record)
            if errors: raise ValueError("; ".join(errors))
        save(args.chapter,record)
        print(f"OK: {args.chapter}: {record['status']}"); return 0
    except (ValueError,OSError,json.JSONDecodeError) as exc:
        parser.exit(1,f"Granskningsfel: {exc}\n")

if __name__=="__main__": raise SystemExit(main())
