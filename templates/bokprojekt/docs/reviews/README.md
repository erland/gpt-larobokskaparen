# Kapitelgranskningar

Varje kapitel kan ha ett versionsbundet JSON-protokoll, `NN-titel.json`.
`scripts/chapter_review.py` skapar och validerar protokollet. Protokollet är arbetsmaterial och exporteras inte som boktext.

Automatisk kvalitetsgranskning utförs av assistenten, inte av Python-skriptet. Assistenten ska faktiskt läsa, kontrollera, korrigera och återkontrollera kapitlet. Protokollet anger vad som verifierades; okontrollerade fakta får aldrig märkas som verifierade.

Status: `review_pending`, `reviewing`, `changes_needed`, `approved_manual`, `approved_auto`. Ändrad kapiteltext ogiltigförklarar ett äldre godkännande genom SHA-256-kontroll. Integritetsmanifestet ska uppdateras via normalt revisionsflöde efter kapitel- och protokolländringar.
