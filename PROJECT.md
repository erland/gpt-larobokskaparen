# Lärobokskaparen

## Syfte

Lärobokskaparen hjälper användare att planera, skriva, underhålla och exportera läroböcker, faktaböcker och närliggande bokformat.

## Canonical källor

- `gpt-configuration/instructions.md` – canonical GPT-beteende.
- `gpt-configuration/conversation-starters.md` – conversation starters.
- `knowledge-upload/` – runtime-Knowledge för GPT-distributionerna.
- `templates/bokprojekt/` – single source of truth för genererade bokprojekt.
- `knowledge-upload/19-project-template-bundle.md` – genererad Knowledge-projektion av bokprojektmallen.

## Stateful bokprojektmodell

Genererade bokprojekt är workspace-orienterade och använder bland annat:

- `book.yaml` som canonical bokmetadata och kapitelordning,
- `project-manifest.json` för integritet och revisionsidentitet,
- `revision-log.md` för revisionshistorik,
- lokala scripts för validering, integritet och export,
- reproducerbar EPUB/PDF-export.

Denna modell ska bevaras i migreringen till GPT Byggaren 1.5.0.

## Migrering

Migreringsstatus finns i `project-status.yaml` och planen i `docs/development-plan.md`. Målet är fem runtime-distributioner: ChatGPT Chat, ChatGPT Custom, Claude Projects, OpenCode och OpenAI Plugin.
