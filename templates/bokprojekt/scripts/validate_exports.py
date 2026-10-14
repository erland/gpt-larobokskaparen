#!/usr/bin/env python3
"""Structural publication checks on the actual EPUB and PDF artifacts."""
from __future__ import annotations
import posixpath
import subprocess
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET

OPF = '{http://www.idpf.org/2007/opf}'
XHTML = '{http://www.w3.org/1999/xhtml}'
CONTAINER = '{urn:oasis:names:tc:opendocument:xmlns:container}'


def check_epub(path: Path) -> dict[str, int]:
    with zipfile.ZipFile(path) as z:
        if z.testzip() is not None:
            raise ValueError('EPUB ZIP CRC-fel')
        names = set(z.namelist())
        if z.namelist()[0] != 'mimetype' or z.getinfo('mimetype').compress_type != 0:
            raise ValueError('EPUB mimetype saknas eller är komprimerad')
        root = ET.fromstring(z.read('META-INF/container.xml'))
        ref = root.find('.//' + CONTAINER + 'rootfile')
        if ref is None:
            raise ValueError('EPUB saknar OPF-rootfile')
        opfpath = ref.attrib['full-path']
        package = ET.fromstring(z.read(opfpath))
        manifest = package.find(OPF + 'manifest')
        spine = package.find(OPF + 'spine')
        if manifest is None or spine is None:
            raise ValueError('EPUB saknar manifest eller spine')
        items = {item.attrib['id']: item for item in manifest.findall(OPF + 'item')}
        navigations = [i for i in items.values()
                       if 'nav' in i.attrib.get('properties', '').split()]
        if len(navigations) != 1:
            raise ValueError('EPUB behöver exakt ett navigeringsdokument')
        nav_ids = {i.attrib['id'] for i in navigations}
        if not all(item.attrib.get('linear') == 'no' for item in spine.findall(OPF+'itemref')
                   if item.attrib.get('idref') in nav_ids):
            raise ValueError('Navigeringsdokumentet får inte visas som lässida')
        for item in spine.findall(OPF + 'itemref'):
            if item.attrib['idref'] not in items:
                raise ValueError('Spine refererar till saknad manifest-post')
        parsed = {}
        for name in names:
            if name.endswith(('.xhtml', '.html')):
                parsed[name] = ET.fromstring(z.read(name))
        if not parsed:
            raise ValueError('EPUB saknar XHTML')
        anchors = {name: {node.attrib['id'] for node in tree.iter() if 'id' in node.attrib}
                   for name, tree in parsed.items()}
        checked = 0
        for name, tree in parsed.items():
            for node in tree.iter():
                href = node.attrib.get('href', '')
                if not href or href.startswith(('https:', 'http:', 'mailto:', 'tel:')):
                    continue
                parts = urlsplit(href)
                if parts.scheme:
                    continue
                target = posixpath.normpath(posixpath.join(posixpath.dirname(name),
                                                          unquote(parts.path))) if parts.path else name
                if target not in names:
                    raise ValueError(f'EPUB-länk utan mål: {name} → {href}')
                if parts.fragment and target in anchors and unquote(parts.fragment) not in anchors[target]:
                    raise ValueError(f'EPUB-ankare saknas: {name} → {href}')
                checked += 1
        return {'xhtml': len(parsed), 'internal_links': checked}


def check_pdf(path: Path) -> int:
    result = subprocess.run(['pdfinfo', str(path)], capture_output=True, text=True,
                            check=True)
    pages = next((int(line.split(':', 1)[1].strip())
                  for line in result.stdout.splitlines() if line.startswith('Pages:')), 0)
    if pages < 1:
        raise ValueError('PDF saknar sidor')
    text = subprocess.run(['pdftotext', str(path), '-'], check=True,
                          capture_output=True, text=True).stdout
    if not text.strip():
        raise ValueError('PDF saknar extraherbar boktext')
    return pages


def main() -> int:
    if len(sys.argv) != 3:
        print('Använd: validate_exports.py book.epub book.pdf', file=sys.stderr)
        return 2
    epub, pdf = map(Path, sys.argv[1:])
    summary = check_epub(epub)
    pages = check_pdf(pdf)
    print(f"PASS: EPUB {summary['xhtml']} dokument, {summary['internal_links']} interna länkar; PDF {pages} sidor")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
