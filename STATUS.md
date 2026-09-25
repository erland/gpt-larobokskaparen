# Status

Migrering till **GPT Byggaren 1.5.0** pågår.

## Nuvarande läge

- Steg 1–8 av 9 är klara.
- Samtliga fem mål-runtimes är aktiva: ChatGPT Chat, Custom GPT, Claude Projects, OpenCode och OpenAI Plugin.
- `gpt-configuration/instructions.md` är fortsatt canonical beteendeinstruktion.
- `templates/bokprojekt/` är fortsatt single source of truth för bokprojekt.
- Projektet är fortsatt klassificerat som **stateful**.
- CI validerar GPT Builder-kontrakt, project hygiene, stateful model/runtime robustness, distributionsstruktur, runtime parity och exakt release-assetuppsättning.
- Release-assets härleds deklarativt från de runtimes som har `status: active` i `gpt-project.yaml`.
- CI stoppar om en aktiv runtime saknar sitt ZIP-paket eller om oväntade ZIP-filer ligger i `dist/`.
- GitHub Release laddar upp exakt den verifierade uppsättningen aktiva runtime-paket.
- Pluginens avsiktliga runtime-gap för ZIP/workspace-state, scriptkörning och EPUB/PDF är explicit dokumenterade.
- Senaste CI-körningen passerade kontrakt, hygiene, robustness, build, distributionsvalidering, parity och release-assetkontroll.

## Nästa steg

**Steg 9 – Slutlig release-readiness.**

Verifiera README, PROJECT, STATUS, projektstatus, kvarvarande varningar, PR-status och den senaste CI-körningen. Om allt är grönt markeras migreringen klar och PR #5 kan mergas.

Maskinläsbar status finns i `project-status.yaml`.
