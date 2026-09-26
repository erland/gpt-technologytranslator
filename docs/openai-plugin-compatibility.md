# OpenAI Plugin – compatibility assessment

Projekt: **Tekniköversättaren**  
GPT Byggaren: **1.5.0**

## Slutsats

OpenAI Plugin bedöms som **equivalent candidate**, med **skills-first** arkitektur, och lämnas **not active** tills en faktisk plugin-distribution och regressionstester finns.

Tekniköversättarens kärnroll är textcentrerad och kräver inte kritiskt stöd för kodkörning, filsystem, zip-paketering eller plattformsspecifik build/test. Därför kan canonical beteende mappas väl till skills.

## Parity-bedömning

| Område | Bedömning |
|---|---|
| Behavior | equivalent |
| Capability | equivalent |
| Artifact | equivalent |
| Workspace/state | equivalent |
| Tool | equivalent with optional current-fact verification |

## Skills-first upplägg

En framtida Plugin v1 bör minst ha skills för:
- målgruppsanpassad teknikförklaring,
- förenkling utan att förvanska,
- verksamhetsnytta, konsekvens, risk och beslut,
- teknisk text till vardagsspråk,
- icke-tekniska jämförelser,
- vardagliga men respektfulla liknelser,
- akronym- och begreppsförklaring,
- osäkerhets- och tvetydighetshantering,
- kort respektive fördjupad förklaringsstruktur.

## Kritiska regler som måste bevaras

- svar på samma språk som användaren,
- respektfull och aldrig nedlåtande ton,
- vanligt språk före teknisk jargong,
- förenkling utan att förvanska,
- fokus på varför något spelar roll,
- verksamhetsnytta, konsekvenser, risker och beslut,
- tydlig gräns mellan vad mottagaren behöver förstå och specialistdetaljer,
- inga fabricerade aktuella fakta,
- korta svar som standard om fördjupning inte efterfrågas,
- 2/2 Knowledge-filer eller verifierat equivalent representation.

## Aktiveringsbeslut

- status: `assessed_not_active`
- compatibility: `equivalent`
- architecture: `skills_first`
- activation: `not_active`
- blocker: `distribution_and_regression_not_implemented`

Ingen Plugin-distribution byggs eller publiceras i denna migrering.

## Aktiveringsregel

Plugin får aktiveras först när:
1. skills-strukturen är implementerad,
2. canonical instruktion och 2/2 Knowledge representeras deterministiskt,
3. språkparity regressionstestas,
4. målgruppsanpassning verifieras,
5. förenkling utan förvanskning verifieras,
6. respektfull/icke-nedlåtande ton verifieras,
7. aktuella fakta hanteras utan fabricering,
8. plugin-distributionen byggs och valideras i CI.

Ingen canonical produktregel ändras av denna bedömning.
