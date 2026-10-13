#!/usr/bin/env python3
"""Verify modern modular, stateful model contracts (GPT Byggaren 1.6.22)."""
from pathlib import Path
import json
import yaml
ROOT=Path(__file__).resolve().parents[1]
def main():
    cfg=yaml.safe_load((ROOT/'gpt-project.yaml').read_text())
    problems=[]
    def check(condition,message):
        if not condition: problems.append(message)
    instructions=cfg.get('instructions',{})
    check(instructions.get('mode')=='modular_skills','modular_skills required')
    core=ROOT/instructions.get('core','__missing__')
    check(core.is_file(),'modular core missing')
    skills=cfg.get('skills',{}).get('definitions',[])
    check(len(skills)>=3,'at least three domain skills required')
    for s in skills:
        check((ROOT/s.get('source','__missing__')).is_file(),f"missing skill source: {s.get('id')}")
    ws=cfg.get('workspace_state',{})
    check(ws.get('state',{}).get('authority')=='workspace_file','workspace_file must be authoritative')
    check(ws.get('state',{}).get('conversation_fallback') is False,'conversation fallback prohibited')
    runtime=cfg.get('runtime',{})
    build=cfg.get('build',{})
    for key,flag in [('chat_zip','build_chat_zip'),('claude','build_claude_project_zip'),('opencode','build_opencode_zip'),('plugin','build_plugin_zip')]:
        check(runtime.get(key,{}).get('enabled') is True,f'{key} must be enabled')
        check(build.get(flag) is True,f'{flag} must be enabled')
    check(build.get('build_claude_skills_zip') is True,'Claude Skills must be built')
    check(runtime.get('custom_gpt',{}).get('enabled') is False,'Custom GPT must be inactive')
    check(build.get('build_custom_gpt_zip') is False,'Custom GPT build must be inactive')
    check(build.get('deterministic') is True,'deterministic build required')
    check(build.get('create_checksums') is True,'checksums required')
    check((ROOT/'templates/bokprojekt/scripts/project_integrity.py').is_file(),'integrity tool missing')
    check((ROOT/'templates/bokprojekt/scripts/validate_project.py').is_file(),'validation tool missing')
    if problems:
        for x in problems: print('FAIL:',x)
        return 1
    print('PASS: modern model robustness contract')
    return 0
if __name__=='__main__': raise SystemExit(main())
