# Kodgenererade diagram – verktygsval och källkontrakt

Detta är referensmaterial till Skillen `diagram-illustrationer`. Kritiska regler finns i Skill-beteendet.

| Typ | Standard | Alternativ |
|---|---|---|
| Systemlandskap, C4-struktur och integrationer | Graphviz DOT | PlantUML/C4 |
| Beroenden och logisk driftsättning | Graphviz DOT | PlantUML |
| Process- och beslutsflöden | Graphviz DOT | PlantUML |
| Informationsmodell / UML-klasser | PlantUML | Graphviz med explicita kardinaliteter |
| Sekvensdiagram | PlantUML | – |
| Tillstånd och formell UML-aktivitet | PlantUML | Graphviz för enkla flöden |
| Konceptbilder, illustrationer och infografik | Handgjord SVG | – |

## Registerpost i docs/illustration-plan.md
Ange: `id`, `chapter`, `purpose`, `kind`, `renderer`, `source`, `svg`, `caption`, `alt`, `status` (`planned|source_ready|pending_render|rendered|approved|replace`). Gamla poster med PNG och bildprompt fortsätter vara giltiga.

## Exempel
```yaml
id: IMG-03-02
chapter: chapters/03-mikrotjanster.md
purpose: Visa sambandet mellan ordertjänst och betaltjänst
kind: sequence
renderer: plantuml
source: assets/diagrams/IMG-03-02.puml
svg: assets/generated/IMG-03-02.svg
caption: Betalningsflödet vid skapande av order.
alt: Sekvensdiagram med klient, ordertjänst och betaltjänst.
status: source_ready
```

## Renderingskontrakt
1. Rendera DOT/PlantUML till SVG vid förändring eller publicering. Egen SVG kopieras/valideras utan dubbel källa.
2. Validera syntax, säkerhet, innehåll, läsbarhet, dimensionsförhållande och figur-ID.
3. Kapitel refererar den genererade SVG-filen, men export kan skapa formatanpassad kopia i tillfällig byggkatalog.
4. För XeLaTeX: använd en verifierad vektorväg (t.ex. SVG till PDF som infogas via lämplig filter-/mellanformatslösning); SVG i Markdown garanterar inte automatiskt vektor-PDF.
5. För EPUB: prova SVG i EPUB-paketet och verifiera läsbarhet/EPUB-validering. Skapa PNG-fallback där det behövs. Aldrig tyst formatbyte.
6. Källor följer med bokprojekt-ZIP, byggprodukter hanteras av exportflödet och kan återskapas.
