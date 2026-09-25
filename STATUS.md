# Status

Migrering till **GPT Byggaren 1.5.0** pågår.

## Nuvarande läge

- Steg 1–3 av 9 är klara.
- `gpt-configuration/instructions.md` är fortsatt canonical beteendeinstruktion.
- `templates/bokprojekt/` är fortsatt single source of truth för bokprojekt.
- Projektet är klassificerat som **stateful**.
- Capability-, artifact-, workspace/state- och tool-kontrakt finns i `gpt-project.yaml`.
- Build och distributionsvalidering väljer nu aktiva runtimes, artifact-namn och runtime-källor deklarativt från `gpt-project.yaml`.
- ChatGPT Chat och Custom GPT behåller sina befintliga ZIP-namn och layout.
- Befintlig template-bundle-synk, bokprojektintegritet, exportordning och distributionsvalidering fortsätter passera i CI.
- Claude Projects, OpenCode och OpenAI Plugin är planerade men inte aktiverade.

## Nästa steg

**Steg 4 – Lägg till Claude Projects.**

Skapa en Claude Projects-distribution från samma canonical instruktion, Knowledge och bokprojektmall och verifiera parity mot ChatGPT Chat innan runtime markeras som aktiv.

Maskinläsbar status finns i `project-status.yaml`.
