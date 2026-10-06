#!/usr/bin/env python3
from pathlib import Path
import argparse
import hashlib
import json
import sys
import yaml

ROOT=Path(__file__).resolve().parents[1]
DEFAULT_DIST=ROOT/'dist'

def load_config():
    data=yaml.safe_load((ROOT/'gpt-project.yaml').read_text(encoding='utf-8'))
    if not isinstance(data,dict): raise SystemExit('Ogiltig gpt-project.yaml')
    return data

def expected_assets(cfg,version):
    assets=[]
    for runtime_id,rcfg in (cfg.get('runtime') or {}).items():
        if not isinstance(rcfg,dict) or rcfg.get('status')!='active': continue
        pattern=rcfg.get('artifact_name')
        if not pattern: raise SystemExit(f'Aktiv runtime saknar artifact_name: {runtime_id}')
        assets.append(pattern.format(version=version))
    return sorted(assets)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--version',required=True)
    p.add_argument('--dist',type=Path,default=DEFAULT_DIST)
    p.add_argument('--print-paths',action='store_true')
    a=p.parse_args()
    expected=expected_assets(load_config(),a.version)
    actual=sorted(x.name for x in a.dist.glob('*.zip') if x.is_file())
    if actual!=expected:
        print('FAILED: release assets',file=sys.stderr)
        print('expected:',*expected,sep='\n- ',file=sys.stderr)
        print('actual:',*actual,sep='\n- ',file=sys.stderr)
        return 1
    sums_path=a.dist/'SHA256SUMS.txt'
    delivery_path=a.dist/'DELIVERY-MANIFEST.json'
    if not sums_path.is_file() or not delivery_path.is_file():
        print('FAILED: release metadata missing',file=sys.stderr)
        return 1
    sums={}
    for line in sums_path.read_text(encoding='utf-8').splitlines():
        digest,name=line.split(None,1)
        sums[name.strip()]=digest
    def sha(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()
    for name in expected:
        if sums.get(name)!=sha(a.dist/name):
            print(f'FAILED: checksum mismatch {name}',file=sys.stderr)
            return 1
    delivery=json.loads(delivery_path.read_text(encoding='utf-8'))
    delivered=sorted(item.get('file') for item in delivery.get('artifacts',[]))
    if delivered!=expected:
        print('FAILED: delivery manifest asset set differs',file=sys.stderr)
        return 1
    if a.print_paths:
        for name in expected: print(str(a.dist/name))
        print(str(sums_path))
        print(str(delivery_path))
    else:
        print(f'OK: {len(expected)} release assets plus checksums/delivery manifest verified')
    return 0

if __name__=='__main__': raise SystemExit(main())
