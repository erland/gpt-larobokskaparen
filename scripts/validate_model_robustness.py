#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

CRITICAL=[
  '## Bokplan före projekt',
  '`book.yaml` är kanonisk metadata',
  '`project-manifest.json`, `revision-log.md` och `scripts/project_integrity.py` skyddar projektversioner och filer.',
  'Vid filändringar: välj exakt en indata-zip',
  'Vid nytt/reviderat kapitel får andra kapitelfiler inte ändras.',
  'Kapitelordningen i `book.yaml` är bindande för export.',
]

def main():
    errors=[]
    cfg=yaml.safe_load((ROOT/'gpt-project.yaml').read_text(encoding='utf-8'))
    canonical=(ROOT/cfg['instructions']['canonical']).read_text(encoding='utf-8')
    for marker in CRITICAL:
        if marker not in canonical: errors.append(f'Canonical instruktion saknar: {marker}')
    ws=cfg['workspace_state']
    if ws['state']['authority']!='workspace_file': errors.append('State authority måste vara workspace_file')
    if ws['state'].get('conversation_fallback') is not False: errors.append('Conversation fallback måste vara false')
    if ws['workspace'].get('portable') is not True: errors.append('Workspace måste vara portable')
    if ws['workspace'].get('artifact')!='book_project_zip': errors.append('Workspace måste peka på book_project_zip')
    for rid in ('chatgpt_chat','claude_projects','opencode'):
        src=cfg['runtime'][rid]['source']
        if src['instructions']!=cfg['instructions']['canonical']: errors.append(f'{rid} använder inte canonical instruction')
        if src['template_root']!='templates/bokprojekt': errors.append(f'{rid} använder fel template root')
    if cfg['runtime']['custom_gpt']['instruction']['source']!=cfg['instructions']['canonical']:
        errors.append('Custom GPT använder inte canonical instruction')
    plugin=cfg['runtime']['openai_plugin']['compatibility']
    if plugin.get('workspace_zip_state')!='host_capability_dependent': errors.append('Plugin workspace gap saknas')
    if plugin.get('bundled_script_execution')!='not_assumed': errors.append('Plugin script gap saknas')
    if plugin.get('epub_pdf_export')!='host_capability_dependent': errors.append('Plugin export gap saknas')
    if not plugin.get('behavior_gap'): errors.append('Plugin behavior_gap saknas')
    if errors:
        print('FAILED: model/runtime robustness')
        for e in errors: print('-',e)
        return 1
    print('OK: stateful model/runtime robustness')
    return 0

if __name__=='__main__': raise SystemExit(main())
