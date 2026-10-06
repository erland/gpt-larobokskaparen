# Status

Plugin-distributionen är moderniserad mot **GPT Byggaren 1.5.1** och valideras i aktuell PR.

## Release-readiness

- Steg 1–9 av 9 är klara.
- Samtliga fem mål-runtimes är aktiva: ChatGPT Chat, Custom GPT, Claude Projects, OpenCode och OpenAI Plugin.
- `gpt-configuration/instructions.md` är canonical beteendeinstruktion.
- `templates/bokprojekt/` är single source of truth för genererade bokprojekt.
- Projektet är fortsatt **stateful**: bokprojektets workspace-filer är auktoritativ state och chatthistorik är inte fallback.
- Build, validering och release-assets väljs deklarativt från `gpt-project.yaml`.
- CI validerar projektkontrakt, project hygiene, stateful model/runtime robustness, distributionsstruktur, runtime parity, release-assetuppsättning och slutlig release-readiness.
- GitHub Release publicerar exakt de aktiva runtime-ZIP-filerna samt checksummor/delivery manifest.
- README, PROJECT, STATUS och maskinläsbar projektstatus är synkroniserade.
- OpenAI Plugin har `plugin.json` direkt i ZIP-roten, explicit `runtime-contract.json`, assets/references-separation och deklarerade runtime-scripts.
- Full pluginfunktion är `ready_runtime_dependent`; workspace/state/execution måste finnas i hosten och chattminne är inte state-fallback.

## Nästa åtgärd

När aktuell PR-CI är grön kan pluginmoderniseringen mergas. Därefter kan nästa stabila GitHub Release skapas med en semantisk release-tagg.

Maskinläsbar status finns i `project-status.yaml`.