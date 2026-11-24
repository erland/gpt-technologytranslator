# Slutverifiering – motor 1.6.33

Originalvalidatorn för modellrobusthet returnerar `MODEL-ROBUSTNESS-001: workflow.mode must be explicit_state_machine`. Källkoden kräver tio tillstånd och saknar villkor för lightweight. Tekniköversättaren är en engångsassistent utan persistent state, och en sådan maskin införs inte. Ingen originalmotorkod har ändrats. Avvikelsen måste accepteras eller rättas i motorn innan releasegodkännande.

Strukturell paritet kontrolleras av `tests/check_distribution_parity.py` efter varje bygge. Originalinnehåll kontrolleras av regressionstesterna. Faktiska språkmodellssessioner och publicering i GitHub Actions är inte lokalt verifierbara.

Releaseflödet använder publicerad release och manuell trigger, taggens källkod och version, kontrollsummor, separat publiceringsbehörighet och skydd mot överskrivning. Ingen release har publicerats under migreringen.

## Lokalt resultat

- Originalinstruktion, samtalsstarter och båda Knowledge-filer: byte-för-byte jämförda mot ursprunglig ZIP, PASS.
- Originalmotorns självtest: PASS (sex provarkiv). Lint och final hygiene i ren källkatalog: PASS. Tre regressionstester: PASS.
- Fem runtimepaket: komplett instruktion, båda Knowledge-filerna, fyra likvärdiga kontrakt, ZIP-integritet och ingen aktiv .gitignore: PASS. Distributions- och leveransvalidator: PASS.
- Releaseversion: testbyggning med 1.1.0-rc.1 i separat arbetskopia godkänd, inklusive VERSION och release.current_version i projekt-ZIP. Ingen verklig release skapad.
- Workflow: YAML och Bash-syntax kontrollerade; mockad gh-publicering med åtta filer godkänd, befintlig asset blockerad, korrupt ZIP blockerad. GitHub Actions har inte exekverats lokalt.

## Funktionella stickprov som återstår

Kör samma fyra scenarier i aktiverade värdmiljöer; jämför kvalitativt mot originalets instruktion, inte ordalydelse.

| Scenario | Förväntat beteende |
|---|---|
| Vad är en API-gateway? | Förklara på svenska, vardagsspråk, verksamhetsnytta och rimliga förenklingar. |
| Explain event-driven architecture to a finance director. | Engelska, målgruppsanpassning och beslutsrelevans. |
| Förenkla en teknisk text utan att ändra dess innebörd. | Bevara fakta, markera osäkerhet och förenklingar. |
| Jämför två tekniska alternativ för en styrgrupp. | Beskriv konsekvenser, risker och avvägningar utan obestyrkta fakta. |

PR kan granskas som migrationskandidat, men ingen release förklaras godkänd innan kvarstående kontroller och validatoravvikelse bedömts.
