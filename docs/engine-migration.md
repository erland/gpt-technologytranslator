# Motorinstallation 1.6.33

Originalmotorn från bifogad engine-ZIP (manifestversion 1.6.33) har installerats med dess oförändrade installerare. Självtest: 62 filer SHA-256-verifierade, installerare och sex provarkiv PASS. Samtliga sju installerade motorfiler matchar manifestets SHA-256. Projektets instruktion, Knowledge och starters är oförändrade. Projektversion 1.0.0 är separat från motorversion 1.6.33. Vid CI-migreringen ska motorn versionslås till release v1.6.33, aldrig latest/main.

## Inventering av äldre skript

| Skript | Bedömning |
|---|---|
| build_distributions.py | Ersatt av originalmotorn; tidigare byggde bara Chat och Custom GPT. Original finns i Git och steg 2. |
| validate_distributions.py | Ersatt av originalmotorns validator; tidigare kontrollerade två arkiv, byteidentitet och innehåll. Kontrollera motsvarande innehåll i steg 4/6. |
| validate_claude_opencode_compatibility.py | Behåll tills steg 5; kräver historiskt avaktiverade mål, ersätt med faktisk distributionsvalidering. |
| validate_openai_plugin_compatibility.py | Behåll tills steg 5; kräver historiskt avaktiverad Plugin, ersätt med faktisk distributionsvalidering. |
| validate_runtime_distribution_registry.py | Behåll tills steg 5; kräver historisk tvåmålsregistrering. Ny projektmodell och exakt artefaktuppsättning ska valideras. |
| validate_gpt_builder_1_5_contract.py | PASS även efter installation. Bevara beteendemarkerare och kontroll av instruktion/Knowledge/version i ny regressionstest innan borttagning. |
| validate_gpt_builder_1_5_migration.py | Historisk 7/7-gate; bevara relevanta beteende- och innehållskontroller i ny regressionstest innan borttagning. |

Fem äldre valideringsskript finns fortfarande kvar. Gamla CI-anrop och releaseuppladdning med --clobber ersätts i steg 5. Ingen release eller merge rekommenderas före slutverifiering. Inga nya runtimepaket för Tekniköversättaren har byggts i detta steg.

## Kontroller
- Motor-selftest PASS, installerare PASS, SHA-256 7/7 PASS.
- CLI-start för byggare och båda installerade validatorer PASS.
- Lint: 0 fel, 2 tidigare kända varningar om duplicerade instruktioner/starters.
- Checkpoint hygiene PASS.
- Äldre beteendekontrakt PASS.
