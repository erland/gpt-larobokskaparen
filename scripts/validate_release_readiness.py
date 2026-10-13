#!/usr/bin/env python3
"""Validate release candidate metadata for the current architecture."""
from pathlib import Path
import sys,json,zipfile,yaml
R=Path(__file__).resolve().parents[1]
def main():
    cfg=yaml.safe_load((R/'gpt-project.yaml').read_text())
    expected=['chat','plugin','claude-project','claude-skills','opencode']
    issues=[]
    if cfg['workspace_state']['state']['conversation_fallback'] is not False: issues.append('conversation fallback')
    if cfg['runtime']['custom_gpt']['enabled'] is not False: issues.append('custom GPT still active')
    dist=R/'dist'
    zips=[p for p in dist.glob('*.zip') if not p.name.startswith('larobokskaparen-project-')]
    for label in expected:
        found=[p for p in zips if p.name.startswith('larobokskaparen-'+label+'-')]
        if len(found)!=1: issues.append(f'{label}: expected 1 zip, got {len(found)}')
        elif zipfile.ZipFile(found[0]).testzip() is not None:issues.append(f'{label}: broken ZIP')
    if not (dist/'SHA256SUMS.txt').exists():issues.append('checksums absent')
    if not (dist/'DELIVERY-MANIFEST.json').exists():issues.append('manifest absent')
    for issue in issues:print('FAIL:',issue)
    if issues:return 1
    print('PASS: release candidate structural readiness (not host-runtime approval)');return 0
if __name__=='__main__':raise SystemExit(main())
