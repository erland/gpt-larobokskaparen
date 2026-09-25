# Status

Migrering till **GPT Byggaren 1.5.0** pågår.

## Nuvarande läge

- Steg 1–5 av 9 är klara.
- `gpt-configuration/instructions.md` är fortsatt canonical beteendeinstruktion.
- `templates/bokprojekt/` är fortsatt single source of truth för bokprojekt.
- Projektet är klassificerat som **stateful**.
- Build och distributionsvalidering väljer aktiva runtimes deklarativt från `gpt-project.yaml`.
- ChatGPT Chat, Custom GPT och Claude Projects är fortsatt aktiva.
- **OpenCode är nu aktiv runtime** och byggs som `larobokskaparen-opencode-v{version}.zip`.
- OpenCode använder samma canonical instruktion, Knowledge, exempel och hela bokprojektmallen som ChatGPT Chat.
- OpenCode är deklarerad som workspace-/script-orienterad med stöd för project integrity och lokal export när runtime-miljön har nödvändiga beroenden.
- CI verifierar byte-identisk parity mellan ChatGPT Chat, Claude Projects och OpenCode, bortsett från runtime-specifik manifestmetadata.
- Befintlig template-bundle-synk, bokprojektintegritet och exportordning fortsätter passera.
- OpenAI Plugin är planerad men inte aktiverad.

## Nästa steg

**Steg 6 – Lägg till OpenAI Plugin.**

Skapa en skills-first plugin-distribution som bevarar bokmetodik, Knowledge och bokprojektmodell, men dokumenterar att ZIP/workspace-state, scriptkörning och EPUB/PDF-export är beroende av värdklientens faktiska förmågor.

Maskinläsbar status finns i `project-status.yaml`.
