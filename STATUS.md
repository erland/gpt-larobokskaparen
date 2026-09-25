# Status

Migrering till **GPT Byggaren 1.5.0** pågår.

## Nuvarande läge

- Steg 1 av 9 är klart.
- `gpt-configuration/instructions.md` är fortsatt canonical beteendeinstruktion.
- `templates/bokprojekt/` är fortsatt single source of truth för bokprojekt.
- Befintliga ChatGPT Chat- och Custom GPT-distributioner är ännu inte ändrade.
- Projektet är klassificerat som **stateful** eftersom bokskapandet bygger på ZIP-/workspace-state, manifest, revisionslogg och deterministiska projektverktyg.
- Claude Projects, OpenCode och OpenAI Plugin är planerade men inte aktiverade.

## Nästa steg

**Steg 2 – Inför plattformsneutrala kontrakt och scheman.**

Modellera capabilities, artifacts, workspace/state och tools för både runtime och genererade bokprojekt innan distributionsbygget migreras.

Maskinläsbar status finns i `project-status.yaml`.
