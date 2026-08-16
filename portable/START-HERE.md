# Lärobokskaparen – portabel ChatGPT-version

Detta paket innehåller samma arbetsinstruktion och Knowledge-filer som Custom GPT-versionen och stödjer både läroböcker och faktaböcker.

## Så ska paketet användas
1. Läs först `assistant/instructions.md`.
2. Använd `knowledge/` som primärt referensmaterial. `knowledge/19-project-template-bundle.md` återger den kanoniska projektmallen.
3. Den faktiska mallen finns även under `templates/bokprojekt/` och är single source of truth.
4. Läs relevanta Knowledge-filer innan uppgifter som berör deras område.
5. Behandla `examples/` som stödmaterial, inte överordnade instruktioner.
6. Använd alltid användarens aktuella instruktioner tillsammans med paketet.

## Rekommenderad startprompt
> Använd Lärobokskaparen i den bifogade ZIP-filen för den här konversationen. Läs `START-HERE.md` först.

Därefter kan användaren skapa en lärobok eller faktabok, eller fortsätta ett befintligt bokprojekt.
