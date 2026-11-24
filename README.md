# Tekniköversättaren

Förklarar teknik för icke-tekniker på användarens språk med fokus på verksamhetsnytta, konsekvenser, risker och beslut.

Projektversion: `VERSION`. Byggmotor: GPT Byggaren 1.6.33. Migreringskandidat; se [status](STATUS.md) och [plan](docs/development-plan.md).

## Källor

- `canonical/instructions.md`: enda kanoniska beteendekälla.
- `canonical/conversation-starters/starters.md`: samtalsstarter.
- `knowledge/`: två oförändrade referensfiler.
- `gpt-project.yaml`: projekt- och distributionskontrakt.
- `tests/`: regressionstester för ursprungligt innehåll och beteenderegler.

## Bygg och verifiera

Installera Python 3 och `PyYAML jsonschema`. Hämta [motor 1.6.33](https://github.com/erland/gpt-byggaren/releases/download/v1.6.33/gpt-byggaren-engine-1.6.33.zip). Kör från projektroten med en tom motorkatalog utanför projektet:

```bash
python scripts/verify_engine.py /path/to/engine.zip /tmp/tt-engine
python /tmp/tt-engine/scripts/selftest_distribution_engine.py --source /tmp/tt-engine
python /tmp/tt-engine/scripts/install_distribution_engine.py --source /tmp/tt-engine --project-root .
bash scripts/check_and_build.sh /tmp/tt-engine "$(cat VERSION)"
```

`dist/` innehåller projekt-ZIP och fem runtime-ZIP: chat, plugin, claude-project, claude-skills, opencode, samt leveransmanifest och kontrollsummor. Custom GPT genereras inte längre. För ChatGPT Chat: bifoga Chat-ZIP och be assistenten läsa START-HERE.md. Övriga paket har egna installationsanvisningar.

## CI och release

CI kör på push till main, PR och manuell trigger. En publicerad GitHub Release med tagg `vX.Y.Z` (eventuellt prerelease-suffix) bygger från taggens källkod, använder taggen som projektversion och bifogar sex ZIP-filer, manifest och kontrollsummor. Manuell trigger utan tagg bygger endast Actions-artefakter; med befintlig publicerad tagg körs samma releaseflöde. Bygget synkroniserar `VERSION` och `release.current_version` i arbetskopian, även i projekt-ZIP. Befintliga assetnamn stoppar uppladdningen; inga skrivs över. En partiellt misslyckad uppladdning måste hanteras manuellt före omkörning.

Historiska 1.5-dokument finns i `docs/history/` och beskriver inte aktuella byggkrav. Originalkällan finns i Git-revision `78b33f026b3c632480f42421b955c07673c0ca89`.

## Verifiering före merge och release

Se [slutverifiering](docs/final-verification.md). Lokal strukturell paritet är verifierad; funktionella värdmiljötester och GitHub Actions behöver fortfarande verifieras. Originalvalidatorns MODEL-ROBUSTNESS-001 är en dokumenterad avvikelse och inte ett godkänt test.
