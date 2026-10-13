# Acceptansrapport – Lärobokskaparen 0.6.1

Datum: 2026-10-14. Byggmotor: GPT Byggaren Chat ZIP 1.6.22, originalets `scripts/build_distributions.py`.

## Verifierat

- Sex ZIP-paket byggda från canonical projekt (fem runtime-distributioner samt projekt-ZIP).
- Samtliga ZIP-filer kan läsas utan ZIP-CRC-fel.
- Distributionsvalidering PASS direkt efter bygge, då dess förväntade `build/`-träd finns kvar.
- Äldre `scripts/validate_project_contracts.py`: PASS.
- Separat provbok av typen `textbook` har initierats och validerats, integritet kontrollerats, otillåten ändring upptäckts, auktoriserad kapitelrevision 1→2 gjorts och validerats.
- Riktiga EPUB- och PDF-exporter genomfördes för provbok med Pandoc 3.1.11.1 och XeLaTeX. EPUB har nav.xhtml, PDF har extraherbar text och innehållsförteckning.
- Negativa tester av saknad författare och saknat kapitel gav avslag.
- Kanonisk lint ska köras mot **rent källträd** (utan `build/`, `dist/`, `__pycache__`); byggutdata i källträdet ger GP202-varningar och är inte ett instruktionsfel.

## Kända brister och begränsningar

1. Äldre `scripts/validate_model_robustness.py` fallerar med `MODEL-ROBUSTNESS-001` eftersom dess kontrakt kräver `workflow.mode=explicit_state_machine`. Ny canonical arkitektur från 1.6.22 har inte detta historiska kontrakt. CI:s äldre robusthetstest måste ersättas eller migreras innan release kan göras med grön CI.
2. Strukturell paritet och gemensamma canonical källor har granskats; faktisk körning av de fem distributionerna på ChatGPT, Claude och OpenCode har **inte** utförts här.
3. Testerna är syntetiska och inte en fullständig språkmodellsevaluering. Omslagsbilder, referenser, stora böcker, svensk typografi och bokprojekts revision under samtidiga användare har inte verifierats.
4. PDF har inte genomgått manuell visuell granskning sida för sida. EPUB är inte validerad med EPUBCheck.
5. Produktionsmallens oinitierade `project-manifest.json` är korrekt avsiktligt; den får inte valideras som ett redan påbörjat bokprojekt.

## Rekommendation

Använd som testkandidat, inte slutlig release, tills äldre CI-kontrakt har moderniserats och körtester genomförts i faktiska värdruntimes. Ingen GitHub-skrivning gjord.
