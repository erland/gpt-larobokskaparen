# Status

Migrering till **GPT Byggaren 1.5.0** pågår.

## Nuvarande läge

- Steg 1–7 av 9 är klara.
- Samtliga fem mål-runtimes är aktiva: ChatGPT Chat, Custom GPT, Claude Projects, OpenCode och OpenAI Plugin.
- `gpt-configuration/instructions.md` är fortsatt canonical beteendeinstruktion.
- `templates/bokprojekt/` är fortsatt single source of truth för bokprojekt.
- Projektet är fortsatt klassificerat som **stateful**.
- CI validerar nu GPT Builder-kontrakt, project hygiene, stateful model/runtime robustness, distributionsstruktur och runtime parity.
- Project hygiene verifierar att genererade build-/cachefiler inte spåras och att aktiva runtimes matchar både build targets och migrationsmål.
- Stateful robustness verifierar bland annat att bokprojektets state ligger i workspace-filer, att chatthistorik inte är fallback, att `book_project_zip` är den portabla workspace-artefakten och att kritiska bokprojektregler finns kvar i canonical instruktion.
- Runtime parity omfattar samtliga fem runtimes: ChatGPT Chat, Claude Projects och OpenCode innehållsmatchas; Custom GPT verifieras mot canonical instruktion; OpenAI Plugin måste bädda in canonical instruktion, samma Knowledge och samma bokprojektmall.
- Pluginens avsiktliga runtime-gap för ZIP/workspace-state, scriptkörning och EPUB/PDF är explicit dokumenterade.
- Senaste CI-körningen passerade alla nya kvalitetskontroller, build, distributionsvalidering, parity och artifact-upload.

## Nästa steg

**Steg 8 – CI och release.**

Generalisera releaseflödet så att exakt de aktiva runtime-assets som deklareras i `gpt-project.yaml` verifieras och publiceras, i stället för att release-steget endast förlitar sig på ett generiskt `dist/*.zip`.

Maskinläsbar status finns i `project-status.yaml`.
