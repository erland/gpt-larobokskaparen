#!/usr/bin/env python3
from pathlib import Path
import argparse
import json
import zipfile
import yaml

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'

def config(): return yaml.safe_load((ROOT/'gpt-project.yaml').read_text(encoding='utf-8'))

def artifact(cfg,runtime_id,version):
    return DIST/cfg['runtime'][runtime_id]['artifact_name'].format(version=version)

def payload(path):
    with zipfile.ZipFile(path) as z:
        files={i.filename:z.read(i.filename) for i in z.infolist() if not i.is_dir() and i.filename!='MANIFEST.json'}
        manifest=json.loads(z.read('MANIFEST.json'))
    return files,manifest

def main(version):
    cfg=config()
    chat_files,chat_manifest=payload(artifact(cfg,'chatgpt_chat',version))
    claude_files,claude_manifest=payload(artifact(cfg,'claude_projects',version))
    if set(chat_files)!=set(claude_files):
        raise SystemExit(
            'Runtime parity file mismatch: '
            f'chat-only={sorted(set(chat_files)-set(claude_files))}, '
            f'claude-only={sorted(set(claude_files)-set(chat_files))}'
        )
    mismatched=[name for name in chat_files if chat_files[name]!=claude_files[name]]
    if mismatched:
        raise SystemExit(f'Runtime parity content mismatch: {mismatched}')
    for key in ('version','entrypoint','instructions','knowledge','template_root'):
        if chat_manifest.get(key)!=claude_manifest.get(key):
            raise SystemExit(f'Manifest parity mismatch for {key}')
    print('OK: ChatGPT Chat and Claude Projects have content parity')

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--version'); a=p.parse_args()
    main(a.version or '0.0.0-dev')
