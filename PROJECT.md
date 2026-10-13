# Lärobokskaparen

## Syfte

Lärobokskaparen hjälper till att planera, skriva, underhålla och exportera läroböcker, faktaböcker och närliggande bokformat.

## Kanonisk arkitektur

Projektet är migrerat till **GPT Byggaren v1.6.22**. Projektprofilen finns i `gpt-project.yaml`; gemensamma arbetsprinciper finns i `canonical/core.md` och beteendet är uppdelat i tre Skills under `canonical/skills/`: bokplanering, bokskrivande och bokprojekt/publicering.

`gpt-configuration/instructions.md` finns kvar som ursprunglig beteendereferens. `templates/bokprojekt/` är fortsatt single source of truth för *genererade bokprojekt*. `knowledge-upload/19-project-template-bundle.md` är den genererade Knowledge-projektionen.

## Två skilda verktygsnivåer

**GPT-distributionsprojektet** (detta repository) använder `scripts/build_distributions.py`, `scripts/validate_distributions.py`, `scripts/lint_gpt_project.py` och övriga `scripts/validate_*.py` för att skapa och kontrollera GPT-paket. Det är **inte** dessa skript som ska köras inne i ett genererat bokprojekt.

**Bokprojekten** utgår från `templates/bokprojekt/`. Deras integritet, kapitelvalidering och export styrs av `templates/bokprojekt/scripts/project_integrity.py`, `validate_project.py`, `export-book.py` och `build_book.py`. När mallen kopieras till ett bokprojekt ligger filerna i dess lokala `scripts/`. De generiska motsvarigheterna i repositoryts rot är byggarresurser och får inte ersätta bokprojektmallens verktyg utan särskild verifiering.

Auktoritativt bokprojektstillstånd är `book.yaml`, `project-manifest.json` och `revision-log.md`; chattminnet är inte en fallback.

## Distributioner

Fem aktiva mål byggs och valideras från projektprofilen:

- Chat ZIP
- ChatGPT Plugin
- Claude Project
- Claude Skills
- OpenCode

Dessutom skapas projekt-ZIP. Custom GPT är **inaktiverat** och ingår inte i leveransen. Runtimeberoende funktioner (exempelvis persistent workspace och kodexekvering) kan inte garanteras enbart av ett distributionspaket. Plugin använder skills-first utan MCP-wrapper.

## Kvalitet och release

GitHub Actions kontrollerar projektkontrakt, modellrobusthet, kanonisk lint, distributionsbygge, distributionsvalidering, sex leverans-ZIP (projekt + fem runtimepaket), checksumma och release-readiness.

Release-taggen är versionskälla vid publicerad GitHub Release. CI-bygg på PR använder utvecklingsversion. Testrapporter finns i `ACCEPTANCE-REPORT.md` och `RELEASE-TEST-0.6.3.md`; återstående värdplattformstester beskrivs där. Maskinläsbar status: `project-status.yaml`.

## Migrering

Se `MIGRATION.md` och `MIGRATION-VALIDATION.md` för detaljer.
