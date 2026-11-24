# Steg 5 – dokumentation och filhygien

Fem föråldrade validatorer avvecklade: validate_claude_opencode_compatibility, validate_openai_plugin_compatibility, validate_runtime_distribution_registry, validate_gpt_builder_1_5_contract, validate_gpt_builder_1_5_migration. Deras aktiva distributionskontroller ersätts av originalmotorn, och beteendekontroller av tre regressionstester (SHA-256 från ursprunglig ZIP, åtta beteendemarkörer, målkonfiguration). Versionslåset till projekt 1.0.0 är ett historiskt migrationskrav, inte permanent regressionstest.

Tre källdubbletter avvecklade; gammal setup-guide och portable START-HERE ersätts av runtimegenererade guider. Historiska kontrakt och bedömningar arkiverade i history; originalet finns i Git. README, STATUS, plan, projektmodell och CI uppdaterade. Motorn versionslåst, manifestkontroll och originalinstallerare i CI. Release från tagg, manuell trigger, separata läs-/skrivbehörigheter och förhandskontroll av assetnamn utan clobber.

Lokalt: lint 0/0, tre regressionstester PASS, build och distributions-/leveransvalidator PASS, kontrollsummor PASS. GitHub Actions inte exekverad. MODEL-ROBUSTNESS-001 kvarstår som dokumenterad avvikelse; inga funktionella språkmodellstester.
