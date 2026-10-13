# Lärobokskaparen 0.6.3 – kompletterad releasekontroll

Datum: 2026-10-14. Byggmotor: GPT Byggaren 1.6.22 (från projektets medföljande engine).

## Genomförda kontroller

- Migrerat projektkontrakt: PASS (`scripts/validate_project_contracts.py`).
- Modern modellrobusthet: PASS (`scripts/validate_model_robustness.py`).
- Faktaboksprojekt: PASS initialisering med `project_integrity.py`, PASS `validate_project.py` med 2 textfiler.
- Faktaboks-EPUB: PASS export med Pandoc; ZIP-struktur och `nav.xhtml` finns.
- Faktaboks-PDF: PASS export med XeLaTeX; `pdfinfo` godkänner PDF 1.5, 4 sidor; `pdftotext` visar titel, författare, innehållsförteckning före inledning.
- Läroboksexport: tidigare genomförd och omtestad i aktuell session; EPUB och PDF har genererats, EPUB har `nav.xhtml`.
- Sex distributionsfiler: skapade med `scripts/build_distributions.py --version 0.6.3`, validerade med projektets distributionsvaliderare samt release-assets/checksums.

## Begränsningar

- Det utökade kombinerade end-to-end-testet av båda profilerna överskred körtidsgränsen, varför det inte räknas som helt godkänt.
- EPUBCheck har inte körts. Navigeringsfilens närvaro är inte liktydig med full EPUBCheck-validering.
- Visuell PDF-inspektion och beteendetest i skarpa ChatGPT-, Claude- och OpenCode-miljöer är inte genomförda.
- Lint ska köras på rent källträd. Genererade `build/` och `dist/` medför GP202-varningar om de ligger kvar; de är inte källfel.
- GitHub Actions har inte körts på GitHub. Repositoryt har inte uppdaterats.

## Beslut

Teknisk releasekandidat för användartest. Ingen produktions- eller hostparitetsgaranti.
