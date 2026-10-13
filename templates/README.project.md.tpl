# {{GPT_NAME}}

{{PROJECT_DESCRIPTION}}

## Distributioner

Projektets aktiva mål är fem runtime-distributioner från samma kanoniska kontrakt:

- Chat ZIP
- ChatGPT Plugin
- Claude Project
- Claude Skills
- OpenCode

Därutöver byggs en komplett projekt-ZIP. Custom GPT är inte ett aktivt distributionsmål.

## Verktygsnivåer

Skript i repositoryts `scripts/` används för att bygga, linta och validera **GPT-distributionerna**. Bokprojekt som skapas med GPT:n använder i stället `templates/bokprojekt/scripts/` som källmall; i det genererade bokprojektet finns dessa skript under `scripts/`.

## Lokal validering

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_project_contracts.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_model_robustness.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/lint_gpt_project.py --project-root . --json
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_distributions.py --version 0.0.0-dev
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_distributions.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_release_assets.py --version 0.0.0-dev
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_release_readiness.py
```

## GitHub Actions

CI körs vid push och pull request. En publicerad GitHub Release med tagg `v1.0.0` bygger releaseartefakterna med version från taggen och bifogar dem till releasen.
