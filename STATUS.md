# Status

Migrering till **GPT Byggaren 1.5.0** pågår.

## Nuvarande läge

- Steg 1–6 av 9 är klara.
- Samtliga fem mål-runtimes är nu aktiva: ChatGPT Chat, Custom GPT, Claude Projects, OpenCode och OpenAI Plugin.
- `gpt-configuration/instructions.md` är fortsatt canonical beteendeinstruktion.
- `templates/bokprojekt/` är fortsatt single source of truth för bokprojekt.
- Projektet är fortsatt klassificerat som **stateful**.
- OpenAI Plugin byggs som `larobokskaparen-openai-plugin-v{version}.zip` med skills-first-struktur.
- Pluginen inkluderar canonical bokmetodik, Knowledge, exempel och hela bokprojektmallen.
- Python-skript under pluginens bokprojektmall följer med som **referensinnehåll/projektmall**, inte som påstått körbara pluginverktyg.
- ZIP/workspace-state, project-integrity-scripts och EPUB/PDF-export är explicit beroende av värdklientens faktiska fil-/exekveringsförmåga.
- Pluginen får inte påstå att projekt-ZIP, revision, manifest, EPUB eller PDF har skapats eller verifierats om värdklienten inte faktiskt kan göra det.
- CI passerar kontraktsvalidering, build av fem runtimes, distributionsvalidering, portabel runtime-parity och artifact-upload.

## Nästa steg

**Steg 7 – Runtime parity, hygiene och robustness.**

Inför tvärgående kontroller för alla fem runtimes, verifiera den stateful bokprojektmodellen, projektträdets hygiene och de avsiktliga plugin-avvikelserna innan releaseflödet generaliseras.

Maskinläsbar status finns i `project-status.yaml`.
