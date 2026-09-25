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
    for runtime_id,label in [('claude_projects','Claude Projects'),('opencode','OpenCode')]:
        other_files,other_manifest=payload(artifact(cfg,runtime_id,version))
        if set(chat_files)!=set(other_files):
            raise SystemExit(
                f'Runtime parity file mismatch for {label}: '
                f'chat-only={sorted(set(chat_files)-set(other_files))}, '
                f'{runtime_id}-only={sorted(set(other_files)-set(chat_files))}'
            )
        mismatched=[name for name in chat_files if chat_files[name]!=other_files[name]]
        if mismatched:
            raise SystemExit(f'Runtime parity content mismatch for {label}: {mismatched}')
        for key in ('version','entrypoint','instructions','knowledge','template_root'):
            if chat_manifest.get(key)!=other_manifest.get(key):
                raise SystemExit(f'Manifest parity mismatch for {label}/{key}')
    print('OK: ChatGPT Chat, Claude Projects and OpenCode have content parity')

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--version'); a=p.parse_args()
    main(a.version or '0.0.0-dev')
