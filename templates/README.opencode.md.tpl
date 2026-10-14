# {{GPT_NAME}} – OpenCode

OpenCode-paketet gör det möjligt att planera, skriva, revidera och publicera läroböcker och faktaböcker med Lärobokskaparens kanoniska Skills.

## Installera

1. Packa upp denna distribution till en egen katalog och öppna den i OpenCode.
2. Läs `AGENTS.md` för arbetsprinciper. De tre arbetsflödena ligger under `.opencode/skills/`.
3. Använd `knowledge/` som referensmaterial för bokplanering, skrivande och export.
4. För ett nytt bokprojekt: kopiera den kompletta mallen från `.opencode/skills/bokprojekt-publicering/assets/bokprojekt/` till en **separat bokprojektkatalog** och fyll i `book.yaml`.
5. När du använder anpassade OpenCode-verktyg under `.opencode/tools/`, ange `projectRoot` som sökvägen till bokprojektet. Om parametern utelämnas används aktuell OpenCode-katalog.

## Projektverktyg

Verktyg för projektintegritet, validering, bokbygge och EPUB/PDF-export använder bokprojektets egna `scripts/` och förutsätter att relevanta Python-/Pandoc-/XeLaTeX-verktyg finns installerade.

Verktyg märkta `distribution-build` och `distribution-validation` hör till GPT-distributionsprojektet, **inte** den vanliga bokredigeringen. Använd dem bara när du verkligen arbetar med GPT-distributionskällan.

## Begränsningar

- Skill-filerna är tillgängliga, men automatisk aktivering måste verifieras i en riktig OpenCode-session.
- `AGENTS.md` är instruktionen för OpenCode, medan `.opencode/runtime-contract.json` beskriver adapterkontraktet.
- Paketet innehåller projektmallen som filer; ett **nytt** bokprojekt behöver fortfarande initieras och verifieras innan revisioner och export används.
- `opencode.json` innehåller verktygsbehörigheter; granska kommandon som modifierar filer.

## Version

{{VERSION}}
