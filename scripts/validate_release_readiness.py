#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main():
    errors=[]
    cfg=yaml.safe_load((ROOT/'gpt-project.yaml').read_text(encoding='utf-8'))
    status=yaml.safe_load((ROOT/'project-status.yaml').read_text(encoding='utf-8'))
    if status.get('progress',{}).get('last_completed_step')!=9:
        errors.append('project-status.yaml markerar inte steg 9 som klart')
    if status.get('state',{}).get('overall')!='pass':
        errors.append('project-status.yaml har inte overall: pass')
    active=[rid for rid,rcfg in cfg.get('runtime',{}).items() if isinstance(rcfg,dict) and rcfg.get('status')=='active']
    if len(active)!=5:
        errors.append(f'Förväntade 5 aktiva runtimes, fick {len(active)}: {active}')
    for doc in ['README.md','PROJECT.md','STATUS.md']:
        text=(ROOT/doc).read_text(encoding='utf-8')
        for marker in ['ChatGPT','Claude Projects','OpenCode','OpenAI Plugin']:
            if marker not in text:
                errors.append(f'{doc} saknar runtime-markör: {marker}')
    if cfg['workspace_state']['state'].get('authority')!='workspace_file':
        errors.append('State authority är inte workspace_file')
    if cfg['workspace_state']['state'].get('conversation_fallback') is not False:
        errors.append('Conversation fallback måste vara false')
    if errors:
        print('FAILED: release readiness')
        for e in errors: print('-',e)
        return 1
    print('OK: release readiness metadata and stateful contract')
    return 0

if __name__=='__main__': raise SystemExit(main())
