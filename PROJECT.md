# Lärobokskaparen

## Syfte

Lärobokskaparen hjälper användare att planera, skriva, underhålla och exportera läroböcker, faktaböcker och närliggande bokformat.

## Canonical projektmodell

GPT Byggaren 1.5.1-modellen definieras i `gpt-project.yaml`. Den kanoniska beteendeinstruktionen är `gpt-configuration/instructions.md`.

Plattformneutrala kontrakt beskriver:

- capabilities,
- artifacts,
- workspace/state,
- verktyg,
- runtime-mål,
- build- och releaseflöde.

`templates/bokprojekt/` är fortsatt single source of truth för genererade bokprojekt och `knowledge-upload/19-project-template-bundle.md` är dess genererade Knowledge-projektion.

## Stateful bokprojektmodell

Genererade bokprojekt är workspace-orienterade och använder bland annat:

- `book.yaml` som canonical bokmetadata och kapitelordning,
- `project-manifest.json` som auktoritativ projektstate och integritetsmanifest,
- `revision-log.md` för revisionshistorik,
- lokala scripts för validering, integritet och export,
- reproducerbar EPUB/PDF-export.

Chatthistorik är inte auktoritativ state för bokprojektet.

## Aktiva runtimes

Projektet bygger och validerar fem aktiva distributioner:

- ChatGPT Chat
- ChatGPT Custom
- Claude Projects
- OpenCode
- OpenAI Plugin

ChatGPT Chat, Claude Projects och OpenCode använder samma canonical instruktion, Knowledge, exempel och bokprojektmall. Custom GPT använder samma canonical instruktion och Knowledge.

OpenAI Plugin använder Agent Plugins 1.0 med skills-first-struktur. `plugin.json` ligger direkt i ZIP-roten. Knowledge paketeras som references, bokprojektmallen som assets och projektets integritets-/validerings-/exportverktyg som deklarerade script resources. Full stateful funktion är `ready_runtime_dependent` och kräver host workspace read/write, code execution och persistent state. Ingen MCP-wrapper genereras.

## Kvalitet och release

CI verifierar:

- GPT Builder 1.5-projektkontrakt,
- project hygiene,
- stateful model/runtime robustness,
- distributionsbygge och struktur,
- runtime parity över fem runtimes,
- exakt release-assetuppsättning,
- SHA-256-checksummor och delivery manifest.

GitHub Release använder release-taggen som versionskälla och publicerar exakt de aktiva runtime-artifacts som deklareras i `gpt-project.yaml`.

Maskinläsbar status finns i `project-status.yaml`; utvecklingsplanen finns i `docs/development-plan.md`.
