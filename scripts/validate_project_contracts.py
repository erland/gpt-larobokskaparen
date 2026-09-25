#!/usr/bin/env python3
from pathlib import Path
import json
import yaml
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]

def load_yaml(path): return yaml.safe_load(path.read_text(encoding='utf-8'))
def load_json(path): return json.loads(path.read_text(encoding='utf-8'))

def validate(instance, schema_path, label, errors):
    try:
        Draft202012Validator(load_json(ROOT/schema_path)).validate(instance)
    except Exception as exc:
        errors.append(f'{label}: {exc}')

def main():
    errors=[]
    cfg=load_yaml(ROOT/'gpt-project.yaml')
    status=load_yaml(ROOT/'project-status.yaml')
    for key,schema in [
        ('capabilities','schemas/capability-contract.schema.json'),
        ('artifacts','schemas/artifact-contract.schema.json'),
        ('workspace_state','schemas/workspace-state-contract.schema.json'),
        ('tools','schemas/tool-contract.schema.json'),
    ]:
        if key not in cfg: errors.append(f'gpt-project.yaml saknar {key}')
        else: validate(cfg[key],schema,key,errors)
    validate(status,'schemas/project-status.schema.json','project-status.yaml',errors)
    canonical=ROOT/cfg['instructions']['canonical']
    if not canonical.is_file(): errors.append(f'Canonical instruktion saknas: {canonical.relative_to(ROOT)}')
    for marker in cfg['instructions']['core_contract']['required_markers']:
        if marker not in canonical.read_text(encoding='utf-8'): errors.append(f'Canonical instruktion saknar marker: {marker}')
    for tool in cfg['tools']['tools']:
        if tool.get('type')=='script' and not (ROOT/tool['script']).is_file():
            errors.append(f'Deklarerat script saknas: {tool["script"]}')
    ws=cfg['workspace_state']
    if ws['state']['authority']!='workspace_file' or ws['state']['conversation_fallback'] is not False:
        errors.append('Stateful bokprojekt måste ha workspace_file som auktoritet utan conversation fallback')
    if ws['workspace'].get('artifact')!='book_project_zip':
        errors.append('Workspace-kontraktet måste peka på book_project_zip')
    if cfg['knowledge_architecture'].get('template_source_of_truth')!='templates/bokprojekt':
        errors.append('templates/bokprojekt måste vara template source of truth')
    if errors:
        print('FAILED: project contracts')
        for error in errors: print('-',error)
        return 1
    print('OK: GPT Builder 1.5 project contracts')
    print('Validated: capabilities, artifacts, stateful workspace/state, tools, project-status')
    return 0

if __name__=='__main__': raise SystemExit(main())
