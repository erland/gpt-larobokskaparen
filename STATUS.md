# Status

Migrering till **GPT Byggaren 1.5.0** pågår.

## Nuvarande läge

- Steg 1–2 av 9 är klara.
- `gpt-configuration/instructions.md` är fortsatt canonical beteendeinstruktion.
- `templates/bokprojekt/` är fortsatt single source of truth för bokprojekt.
- Projektet är klassificerat som **stateful**.
- Capability-, artifact-, workspace/state- och tool-kontrakt finns nu i `gpt-project.yaml`.
- Workspace-state är explicit: bokprojektets filer är den långlivade arbetsytan och `project-manifest.json` är auktoritativ state tillsammans med `book.yaml` och revisionsloggen; chatthistorik är inte fallback.
- CI validerar 1.5.0-kontrakten innan befintlig build/distributionsvalidering.
- Befintliga ChatGPT Chat- och Custom GPT-distributioner är fortfarande oförändrade.
- Claude Projects, OpenCode och OpenAI Plugin är planerade men inte aktiverade.

## Nästa steg

**Steg 3 – Migrera distributionsbygget.**

Låt build/validation välja aktiva runtimes och deras källor deklarativt från `gpt-project.yaml`, samtidigt som befintliga ChatGPT-paket behåller kompatibel layout och befintliga bokprojektstester fortsätter passera.

Maskinläsbar status finns i `project-status.yaml`.
