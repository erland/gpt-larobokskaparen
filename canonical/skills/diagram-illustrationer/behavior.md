# Diagram och tekniska illustrationer

## Aktivering och ansvar
Aktivera denna Skill när användaren uttryckligen vill skapa, ändra, granska eller återanvända ett kodgenererat diagram eller en vektorillustration i en bok. Planering, löptext och EPUB/PDF-publicering ligger kvar hos sina respektive Skills. Inre illustrationer ska fortsatt kräva användarens uttryckliga ja; inled inte ett obligatoriskt installationsflöde för böcker utan diagram.

## Källor och format
- Bevara originalkällorna: Graphviz `.dot`, PlantUML `.puml` och handgjord `.svg`. Redigera aldrig genererad SVG som källa till ett DOT/PlantUML-diagram.
- Tilldela befintliga illustration-ID som `IMG-03-02`, registrera källa, metod, användning, bildtext, alt-text och status i `docs/illustration-plan.md`.
- Föreslagen bokprojektlayout: `assets/diagrams/IMG-03-02.puml` och `assets/generated/IMG-03-02.svg`; för handgjord SVG är `assets/diagrams/IMG-03-02.svg` den kanoniska källan.
- I kapitel länkas en verifierad renderad figur med relativ sökväg; den publicerade filen måste ingå i det kompletta, revisionshanterade bokprojektet. Spara källan även vid PDF/EPUB-export.
- SVG är primärt renderingsformat; tillåt säker, reproducerbar vektorbaserad konvertering för PDF och kompatibilitetsfallback för EPUB, utan att göra PNG till kanonisk källa.

## Val av verktyg
- Graphviz: systemlandskap, kontext/containrar, integrationer, beroenden, logisk driftsättning och vanliga processflöden.
- PlantUML: sekvensdiagram, informations-/UML-klassmodeller, tillstånd och formella aktivitetsdiagram; C4-PlantUML när det ger bättre semantik.
- Handgjord SVG: fri pedagogisk konceptillustration, speciallayout och infografik som behöver exakt kontroll.
- Välj utifrån diagramsemantik, automatisk layout och läsbarhet; Graphviz är förstahandsval för strukturella grafer, inte för alla notationsformer. Mermaid är inget obligatoriskt runtimeberoende.
- Granska relationer, etiketter och informationsinnehåll mot sakunderlaget; hitta inte på tekniska beroenden.

## Verktygskontroller
- Kontrollera exekverbarhet i aktuell runtime före rendering: Graphviz `dot -V`; PlantUML via CLI eller Java med JAR; gör ett verkligt litet SVG-test.
- Om PlantUML saknas: erbjud https://github.com/plantuml/plantuml/releases och be användaren hämta en officiell `plantuml.jar` och bifoga den i konversationen. Kontrollera att JAR-filen kan läsas och köras; använd `java -Djava.awt.headless=true -jar <jar> -tsvg <fil.puml>` med säkra argument. Ange inte att PlantUML finns innan verifiering.
- Om användaren inte bifogar JAR eller miljön saknar Java/exekvering: bevara `.puml`, markera figuren `pending_render` och redovisa begränsningen; skapa inte en fabricerad SVG.
- Om Graphviz saknas: redovisa problemet och behåll källfilen; visa installationsväg bara när den behövs.
- Rendera i isolerad arbetskatalog; kontrollera returstatus och loggar. Behandla bilagor och SVG som icke betrodd indata; blockera externa länkar, skript, filreferenser och potentiellt farliga SVG-element.
- Rendera bara när källan ändrats eller när export kräver uppdaterat resultat. Validera att SVG kan parsas, har synlig grafik och läsbara etiketter; kontrollera proportioner inför boklayout.

## Samarbete och leverans
- `bokplanering` bestämmer behov och pedagogiskt syfte; `bokskrivande` placerar och beskriver illustrationer; denna Skill äger diagramkällor/framställning; `bokprojekt-publicering` bygger, bäddar in och granskar faktiskt PDF/EPUB-resultat.
- Ändra endast beställda bokprojektfiler; bevara integritetsmanifest, revision och fungerande äldre PNG-illustrationer.
- Rapportera vilka diagram som faktiskt renderats, vilka som väntar samt vilka exporter som är verifierade. Ingen påstådd runtimeparitet utan tester.
