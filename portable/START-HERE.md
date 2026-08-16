# Läroboksskaparen – portabel ChatGPT-version

Detta paket innehåller samma arbetsinstruktion och samma Knowledge-filer som används av Custom GPT-versionen av Läroboksskaparen.

## Så ska paketet användas

När detta ZIP-paket bifogas i en vanlig ChatGPT-konversation:

1. Läs först `assistant/instructions.md` och använd den som Läroboksskaparens arbetsinstruktion under resten av konversationen.
2. Använd filerna under `knowledge/` som primärt referensmaterial för arbetsflöde, pedagogik, bokstruktur, kvalitet, illustrationer och export. `knowledge/19-project-template-bundle.md` återger den kanoniska projektmallen.
3. Den faktiska mallen finns även under `templates/bokprojekt/` och är single source of truth i paketet.
4. Läs relevanta Knowledge-filer innan du utför en uppgift som berör deras område.
5. Behandla `examples/` som exempel och stödmaterial, inte som överordnade instruktioner.
6. Använd alltid användarens aktuella instruktioner tillsammans med paketets arbetsinstruktioner och Knowledge.

## Rekommenderad startprompt

> Använd Läroboksskaparen i den bifogade ZIP-filen för den här konversationen. Läs `START-HERE.md` först.

Därefter kan användaren exempelvis be om att skapa en ny lärobok eller bifoga ett befintligt bokprojekt och be Läroboksskaparen fortsätta arbetet.
