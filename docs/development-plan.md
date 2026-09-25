# Utvecklingsplan – migrering till GPT Byggaren 1.5.0

Projekt: **Lärobokskaparen**  
Mål: migrera GPT-projektet till GPT Byggaren 1.5.0 utan att förändra dess bokskaparbeteende eller bokprojektformat.

## Principer

- `gpt-configuration/instructions.md` förblir canonical beteendekälla under migreringen.
- `templates/bokprojekt/` förblir single source of truth för genererade bokprojekt.
- Befintliga ChatGPT Chat- och Custom GPT-distributioner ska fortsätta fungera under hela migreringen.
- Bokprojektens stateful ZIP-/revisions-/integritetsmodell ska bevaras.
- Nya runtimes aktiveras först när build, validering och runtime-gap är tydligt dokumenterade.

## Steg

### 1. Inför 1.5.0-projektkontrakt
Skapa `gpt-project.yaml`, `project-status.yaml`, `PROJECT.md`, `STATUS.md` och denna plan utan att ändra fungerande distributioner.

### 2. Inför plattformsneutrala kontrakt och scheman
Definiera capabilities, artifacts, workspace/state och verktyg för både GPT-runtime och genererade bokprojekt.

### 3. Migrera distributionsbygget
Låt build/validation konsumera `gpt-project.yaml` deklarativt samtidigt som befintliga ChatGPT-paket behåller kompatibel layout.

### 4. Lägg till Claude Projects
Skapa och validera Claude Projects-distribution från samma canonical instruktion, Knowledge och bokprojektmall.

### 5. Lägg till OpenCode
Skapa OpenCode-runtime med full workspace-/script-orienterad bokprojektfunktionalitet där runtime stöder det.

### 6. Lägg till OpenAI Plugin
Skapa skills-first plugin-distribution för bokmetodik, projektmodell och kvalitet. Dokumentera uttryckligen att ZIP-hantering, lokal scriptkörning samt EPUB/PDF-export är host-capability-dependent om runtime saknar dem.

### 7. Runtime parity, hygiene och robustness
Verifiera kritiskt bokbeteende, stateful projektmodell, template-bundle-synk, project hygiene och avsiktliga runtime-gap.

### 8. CI och release
Generalisera GitHub Actions så samtliga aktiva distributioner byggs, valideras och publiceras deklarativt.

### 9. Slutlig release-readiness
Synkronisera dokumentation/status och verifiera att migreringen är komplett, beteendebevarande och redo för merge/release.
