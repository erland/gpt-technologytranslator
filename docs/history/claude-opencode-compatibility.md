# Claude Projects och OpenCode – runtime compatibility

Projekt: **Tekniköversättaren**  
GPT Byggaren: **1.5.0**

## Slutsats

Både Claude Projects och OpenCode bedöms som **equivalent candidates** för Tekniköversättarens kärnroll.

Projektets kritiska beteende består främst av:
- canonical instruktion,
- två Knowledge-filer,
- samma språk som användaren,
- målgruppsanpassning,
- förenkling utan att förvanska,
- verksamhetsnytta/konsekvenser/risker/beslut,
- respektfull ton,
- osäkerhetshantering,
- försiktighet med aktuella fakta.

Det finns inga kritiska krav på kodkörning, zip-paketering eller plattformsspecifik build/test för att leverera kärnnyttan.

Båda runtimes lämnas ändå **not active** tills faktiska distributioner och regressionstester finns.

## Parity-bedömning

| Område | Claude Projects | OpenCode |
|---|---|---|
| Behavior | equivalent | equivalent |
| Capability | equivalent | equivalent |
| Artifact | equivalent | equivalent |
| Workspace/state | equivalent | equivalent |
| Tool | equivalent with optional current-fact verification | equivalent with optional current-fact verification |

## Claude Projects

Bedömning:
- compatibility: `equivalent`
- activation: `not_active`
- blocker: `distribution_and_regression_not_implemented`

## OpenCode

Bedömning:
- compatibility: `equivalent`
- activation: `not_active`
- blocker: `distribution_and_regression_not_implemented`

## Aktiveringsregel

En runtime får aktiveras först när:
1. canonical instruktion paketeras deterministiskt,
2. 2/2 Knowledge-filer eller verifierat equivalent representation ingår,
3. samma språk som användaren regressionstestas,
4. målgruppsanpassning regressionstestas,
5. förenkling utan förvanskning verifieras,
6. respektfull/icke-nedlåtande ton verifieras,
7. osäkerhet och aktuella fakta hanteras utan fabricering,
8. runtime-distributionen byggs och valideras i CI.

Ingen canonical produktregel ändras av denna bedömning.
