#!/usr/bin/env python3
"""Verify exactly seven project/runtime artifacts and checksums for a release."""
from pathlib import Path
import argparse,hashlib,sys
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--version',required=True);p.add_argument('--print-paths',action='store_true');p.add_argument('--dist',type=Path,default=R/'dist');a=p.parse_args()
labels=('project','chat','plugin','claude-project','claude-skills','opencode','engine')
expected={f'larobokskaparen-{label}-{a.version}.zip' for label in labels}
actual={p.name for p in a.dist.glob('*.zip')}
issues=[]
if expected!=actual:issues.append(f'artifact mismatch: missing={sorted(expected-actual)}, extra={sorted(actual-expected)}')
check=a.dist/'SHA256SUMS.txt'
if not check.is_file():issues.append('missing SHA256SUMS.txt')
else:
    sums={line.split('  ',1)[1]:line.split('  ',1)[0] for line in check.read_text().splitlines() if '  ' in line}
    for name in expected&actual:
        if sums.get(name)!=hashlib.sha256((a.dist/name).read_bytes()).hexdigest():issues.append('checksum mismatch '+name)
if not (a.dist/'DELIVERY-MANIFEST.json').is_file():issues.append('missing delivery manifest')
if issues:
    for i in issues:print('FAIL:',i,file=sys.stderr)
    sys.exit(1)
if a.print_paths:
    for name in sorted(expected):print(a.dist/name)
else:print('PASS: seven release artifacts and checksums')
