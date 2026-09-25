#!/usr/bin/env python3
from pathlib import Path
import argparse
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
    if a.print_paths:
        for name in expected: print(str(a.dist/name))
    else:
        print(f'OK: {len(expected)} release assets verified')
    return 0

if __name__=='__main__': raise SystemExit(main())
