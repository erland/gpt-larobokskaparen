# Releasekandidatkontroll v0.6.2

- Migreringskälla: projekt-ZIP v0.6.1, GPT Byggaren originalmotor v1.6.22.
- CI: äldre robusthetskontroll har ersatts med kontroll av modulära Skills, deklarerade byggmål, workspace-state och reproducerbar paketering.
- CI: äldre runtime-paritetskontroll som krävde identiska ZIP och Custom GPT har avförts. Strukturell distributionsvalidering med originalmotorn används i stället.
- CI: korrigerade argument för distributionsvalidering; ny kontroll av leveransmanifest och SHA-256.
- Tester på syntetisk lärobok: initiering, validering, upptäckt av otillåten ändring, revisionscommit, avvisning av saknat kapitel, EPUB/PDF-export godkända i tidigare testomgång och delvis återkörda här. Den senaste fullständiga tvåprofilsomgången avbröts på tidsgräns efter godkänd EPUB/PDF-export av läroboken.
- Kvarstår: faktabokens fullständiga återtest v0.6.2, visuell PDF-granskning, EPUBCheck samt faktiskt beteende i samtliga värdplattformar.
- Status: teknisk releasekandidat, inte slutligt produktionsgodkännande.
