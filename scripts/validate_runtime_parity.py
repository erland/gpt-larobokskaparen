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
    canonical=(ROOT/cfg['instructions']['canonical']).read_bytes()

    custom_path=artifact(cfg,'custom_gpt',version)
    with zipfile.ZipFile(custom_path) as z:
        custom_instruction=z.read(cfg['runtime']['custom_gpt']['instruction']['source'])
        if custom_instruction!=canonical:
            raise SystemExit('Custom GPT canonical instruction mismatch')

    plugin_cfg=cfg['runtime']['openai_plugin']
    plugin_path=artifact(cfg,'openai_plugin',version)
    root=plugin_cfg['manifest']['name']+'/'
    skill_path=root+'skills/'+plugin_cfg['skill']['id']+'/SKILL.md'
    with zipfile.ZipFile(plugin_path) as z:
        skill=z.read(skill_path)
        if canonical.decode('utf-8').strip().encode('utf-8') not in skill:
            raise SystemExit('OpenAI Plugin skill does not embed canonical instruction')
        knowledge_root=ROOT/plugin_cfg['skill']['knowledge']
        prefix=root+'skills/'+plugin_cfg['skill']['id']+'/references/knowledge/'
        for p in sorted(knowledge_root.glob('*.md')):
            if z.read(prefix+p.name)!=p.read_bytes():
                raise SystemExit(f'Plugin Knowledge mismatch: {p.name}')
        template_root=ROOT/plugin_cfg['skill']['template_root']
        tprefix=root+'skills/'+plugin_cfg['skill']['id']+'/references/templates/bokprojekt/'
        for p in sorted(x for x in template_root.rglob('*') if x.is_file() and '__pycache__' not in x.parts and x.suffix!='.pyc'):
            rel=p.relative_to(template_root).as_posix()
            if z.read(tprefix+rel)!=p.read_bytes():
                raise SystemExit(f'Plugin template mismatch: {rel}')

    print('OK: runtime parity verified across all five active runtimes')

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--version'); a=p.parse_args()
    main(a.version or '0.0.0-dev')
