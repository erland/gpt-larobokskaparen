# Status

Migrering till **GPT Byggaren 1.5.0** pågår.

## Nuvarande läge

- Steg 1–4 av 9 är klara.
- `gpt-configuration/instructions.md` är fortsatt canonical beteendeinstruktion.
- `templates/bokprojekt/` är fortsatt single source of truth för bokprojekt.
- Projektet är klassificerat som **stateful**.
- Build och distributionsvalidering väljer aktiva runtimes deklarativt från `gpt-project.yaml`.
- ChatGPT Chat och Custom GPT behåller kompatibel layout.
- **Claude Projects är nu aktiv runtime** och byggs som `larobokskaparen-claude-projects-v{version}.zip`.
- Claude Projects innehåller samma canonical instruktion, Knowledge, exempel och hela bokprojektmallen som ChatGPT Chat.
- CI verifierar byte-identisk runtime-parity mellan ChatGPT Chat och Claude Projects, bortsett från runtime-specifik manifestmetadata.
- Befintlig template-bundle-synk, bokprojektintegritet och exportordning fortsätter passera.
- OpenCode och OpenAI Plugin är planerade men inte aktiverade.

## Nästa steg

**Steg 5 – Lägg till OpenCode.**

Skapa OpenCode-runtime med samma bokprojektmodell och, där runtime stöder det, workspace-/script-orienterad funktionalitet för integritet, revision och export.

Maskinläsbar status finns i `project-status.yaml`.
