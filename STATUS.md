# Status

Migreringen till **GPT Byggaren 1.5.0** är klar.

## Release-readiness

- Steg 1–9 av 9 är klara.
- Samtliga fem mål-runtimes är aktiva: ChatGPT Chat, Custom GPT, Claude Projects, OpenCode och OpenAI Plugin.
- `gpt-configuration/instructions.md` är canonical beteendeinstruktion.
- `templates/bokprojekt/` är single source of truth för genererade bokprojekt.
- Projektet är fortsatt **stateful**: bokprojektets workspace-filer är auktoritativ state och chatthistorik är inte fallback.
- Build, validering och release-assets väljs deklarativt från `gpt-project.yaml`.
- CI validerar projektkontrakt, project hygiene, stateful model/runtime robustness, distributionsstruktur, runtime parity, release-assetuppsättning och slutlig release-readiness.
- GitHub Release publicerar exakt de aktiva runtime-ZIP-filerna.
- README, PROJECT, STATUS och maskinläsbar projektstatus är synkroniserade.
- OpenAI Plugins avsiktliga runtime-gap är dokumenterade: ZIP/workspace-state, scriptkörning och EPUB/PDF används endast när värdklienten faktiskt erbjuder motsvarande förmågor.

## Nästa åtgärd

När PR-CI är grön kan **PR #5 mergas**. Därefter kan nästa stabila GitHub Release skapas med en semantisk release-tagg; taggen styr versionsnumret i samtliga fem distributionspaket.

Maskinläsbar status finns i `project-status.yaml`.
