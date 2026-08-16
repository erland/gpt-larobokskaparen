# Kapitelmallar

Välj mall efter `book_kind`. Tvinga inte sektioner från den andra profilen.

## Lärobok (`textbook`)

```markdown
# X. [Titel]

## Varför detta kapitel finns

## Lärandemål
Efter kapitlet ska läsaren kunna:
- ...

## Innan vi börjar

## Huvudförklaring

## Exempel

## Vanliga misstag

## Övningar

## Snabb sammanfattning
- ...

## Quiz/reflektionsfrågor
1. ...

## Nästa steg
```

Sektioner kan anpassas efter `book_type`; workshopbok, snabbguide och referensverk behöver inte följa allt mekaniskt.

## Faktabok (`factbook`)

```markdown
# X. [Titel]

[Ingress eller nyfikenhetsväckare]

## [Huvudavsnitt]
Förklara ämnet sammanhängande och begripligt.

## [Fördjupning eller nästa del]

## Konkreta exempel eller fall

## Centrala fakta
- ...

## Visste du att? (valfritt)

## Begrepp att känna till (vid behov)

## Sammanfattning (valfritt)
```

Rubrikerna i faktabok är innehållsdrivna; använd inte identiska mekaniska underrubriker i varje kapitel om berättarflödet blir sämre. Käll-/faktanoteringar hålls normalt i `docs/faktakontroll.md`, inte i kapiteltexten.
