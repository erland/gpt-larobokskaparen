#!/usr/bin/env python3
"""Render and check book diagram sources. No network dependencies."""
from __future__ import annotations
import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"assets"/"diagrams"
OUTPUT=ROOT/"assets"/"generated"
SVG_NS="{http://www.w3.org/2000/svg}"
PROHIBITED={"script","foreignObject","iframe","object","embed","image","use","animate","set"}
EXTERNAL=re.compile(r"(?:https?:|file:|data:|javascript:|//)",re.I)

def check_svg(path:Path)->None:
    if not path.is_file() or path.stat().st_size==0:
        raise ValueError(f"SVG saknas eller är tom: {path}")
    data=path.read_text(encoding="utf-8")
    if "<!DOCTYPE" in data.upper() or "<!ENTITY" in data.upper():
        raise ValueError(f"DOCTYPE/ENTITY tillåts inte: {path.name}")
    tree=ET.fromstring(data)
    if tree.tag not in (SVG_NS+"svg","svg"):
        raise ValueError(f"Roten måste vara svg: {path.name}")
    if len(list(tree.iter()))<2:
        raise ValueError(f"SVG innehåller ingen synlig grafik: {path.name}")
    for el in tree.iter():
        local=el.tag.split("}")[-1]
        if local in PROHIBITED:
            raise ValueError(f"Otillåtet SVG-element {local}: {path.name}")
        for key,value in el.attrib.items():
            attr=key.split("}")[-1].lower()
            if attr.startswith("on") or attr in ("href","src") and value.strip() or EXTERNAL.search(value):
                raise ValueError(f"Osäker SVG-referens/attribut i {path.name}: {key}")

def render_one(source:Path, jar:Path|None)->Path:
    target=OUTPUT/(source.stem+".svg")
    OUTPUT.mkdir(parents=True,exist_ok=True)
    if source.suffix==".svg":
        check_svg(source)
        shutil.copyfile(source,target)
    elif source.suffix==".dot":
        dot=shutil.which("dot")
        if not dot: raise RuntimeError("Graphviz saknas: dot hittades inte")
        with target.open("wb") as f:
            subprocess.run([dot,"-Tsvg",str(source)],stdout=f,check=True,timeout=60)
    else:
        exe=shutil.which("plantuml")
        if jar:
            if not jar.is_file(): raise RuntimeError(f"PlantUML JAR saknas: {jar}")
            java=shutil.which("java")
            if not java: raise RuntimeError("Java saknas för PlantUML JAR")
            cmd=[java,"-Djava.awt.headless=true","-jar",str(jar),"-tsvg","-pipe"]
        elif exe: cmd=[exe,"-tsvg","-pipe"]
        else:
            raise RuntimeError("PlantUML saknas. Hämta officiell JAR från https://github.com/plantuml/plantuml/releases och bifoga filen.")
        with target.open("wb") as out:
            raw=source.read_text(encoding="utf-8")
            subprocess.run(cmd,input=source.read_bytes(),stdout=out,check=True,timeout=90)
    # Graphviz/PlantUML kan skriva en SVG 1.1-DOCTYPE. Ta bort den lokalt,
    # så att slutartefakten blir fristående och passerar säkerhetsvalideringen.
    if source.suffix in (".dot",".puml"):
        data=target.read_text(encoding="utf-8")
        data=re.sub(r'<!DOCTYPE[\s\S]*?>', '', data, count=1)
        target.write_text(data,encoding="utf-8")
    check_svg(target)
    return target

def sources()->list[Path]:
    if not SOURCE.exists(): return []
    files=sorted(p for p in SOURCE.iterdir() if p.is_file() and p.suffix.lower() in {".dot",".puml",".svg"})
    ids={}
    for p in files:
        if not re.fullmatch(r"IMG-\d{2}-\d{2}",p.stem):
            raise ValueError(f"Ogiltigt diagram-ID: {p.name}")
        if p.stem in ids: raise ValueError(f"Duplicerat diagram-ID: {p.stem}")
        ids[p.stem]=p
    return files

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",action="store_true",help="Validera redan genererade SVG, utan att ändra filer")
    ap.add_argument("--plantuml-jar",type=Path,default=Path(os.environ["PLANTUML_JAR"]) if os.environ.get("PLANTUML_JAR") else None)
    args=ap.parse_args()
    try:
        files=sources()
        for source in files:
            target=OUTPUT/(source.stem+".svg")
            if args.check: check_svg(target)
            else: render_one(source,args.plantuml_jar)
            print(f"OK {source.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        print(f"Godkända diagram: {len(files)}")
        return 0
    except (ValueError,ET.ParseError,RuntimeError,subprocess.SubprocessError,OSError) as exc:
        print(f"Diagramfel: {exc}",file=sys.stderr)
        return 1

if __name__=="__main__": raise SystemExit(main())
