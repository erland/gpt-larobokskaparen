#!/usr/bin/env python3
from pathlib import Path
import subprocess
import yaml

ROOT=Path(__file__).resolve().parents[1]

def tracked():
    r=subprocess.run(['git','ls-files'],cwd=ROOT,text=True,capture_output=True,check=True)
    return [x.strip() for x in r.stdout.splitlines() if x.strip()]

def main():
    errors=[]
    files=tracked()
    for required in ['gpt-project.yaml','project-status.yaml','STATUS.md','PROJECT.md','README.md']:
        if required not in files: errors.append(f'Saknad spårad projektfil: {required}')
    for p in files:
        n=p.replace('\\\\','/')
        if n.startswith(('dist/','.build-dist/','.build/')) or '/__pycache__/' in n or n.startswith('__pycache__/'):
            errors.append(f'Genererad fil är spårad: {p}')
        if n.endswith(('.pyc','.pyo','.DS_Store')):
            errors.append(f'Oönskad artefakt är spårad: {p}')
    cfg=yaml.safe_load((ROOT/'gpt-project.yaml').read_text(encoding='utf-8'))
    active={rid for rid,rcfg in cfg['runtime'].items() if isinstance(rcfg,dict) and rcfg.get('status')=='active'}
    targets=set(cfg['build_system']['current']['targets'])
    migration=set(cfg['build_system']['migration_target']['runtimes'])
    if active!=targets: errors.append(f'active != build targets: {sorted(active)} != {sorted(targets)}')
    if active!=migration: errors.append(f'active != migration targets: {sorted(active)} != {sorted(migration)}')
    if len(active)!=5: errors.append(f'Förväntade fem aktiva runtimes, fick {len(active)}')
    if errors:
        print('FAILED: project hygiene')
        for e in errors: print('-',e)
        return 1
    print(f'OK: project hygiene ({len(files)} tracked files, {len(active)} active runtimes)')
    return 0

if __name__=='__main__': raise SystemExit(main())
