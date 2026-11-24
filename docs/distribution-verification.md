# Distributionsverifiering – steg 4

Motor: 1.6.33. Projektversion: 1.0.0 (explicit --version; utan flagga använder motorn 0.0.0-dev). Ingen release.

| Runtime | Filer | Beteendekälla | Resultat |
|---|---:|---|---|
| Chat | 59 | assistant/instructions.md | PASS |
| Plugin | 8 | skills/technology-explanation/SKILL.md | PASS |
| Claude Project | 7 | project/instructions.md | PASS |
| Claude Skills | 7 | skills/technology-explanation/SKILL.md | PASS |
| OpenCode | 11 | AGENTS.md med adapter | PASS |

Originalinstruktion och Knowledge jämförda med ursprunglig ZIP. Instruktionens hela text finns i samtliga paket (normaliserade radslut); båda Knowledge-filerna byte-identiska i alla förekomster. Chat conversation starters bevarade. Capability-, artifact-, workspace_state- och tool-kontrakt identiska mellan runtimes. Inga deklarerade runtimeverktyg. Alla ZIP-integritetskontroller, distributionsvalidator, generated-delivery-validator, förväntade distributionsfiler och SHA-256-kontroller godkända. Ingen aktiv Custom GPT eller .gitignore i runtimepaket. Chat och OpenCode har referens-Skills; huvudbeteendet finns i huvudinstruktionen.

Avvikelse: validate_model_robustness.py returnerar MODEL-ROBUSTNESS-001: workflow.mode must be explicit_state_machine. Validatorn kräver GPT Byggarens egen tillståndsmaskin utan hänsyn till lightweight. Ingen sådan maskin läggs till en enkel engångsassistent; tillämplighet och releasegate måste bedömas i steg 5–6. Detta är inte ett godkänt modellrobusthetstest. Ingen verifiering av installation i faktiska värdmiljöer eller språkmodellsbeteende har utförts. Historisk CI och källdubbletter hanteras i steg 5.
