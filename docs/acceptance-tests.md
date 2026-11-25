# Funktionella acceptanstester

Kör varje fall i en ny konversation med den aktuella distributionen aktiverad enligt installationsanvisningen. T06 har två turer i samma konversation. Ge inte modellen facit eller information om att den testas. Använd samma frågor i Chat, Plugin, Claude Projects, Claude Skills och OpenCode. Notera version, modell, datum, värdmiljö och svar/evidens i en kopia av [resultatmallen](acceptance-results-template.md). Testerna är manuella och kompletterar automatiska regressions- och paritetskontroller; de är inte ett CI-test av modellbeteende.

## Testfall

### T01 – Startflöde

**Fråga:** Hjälp mig förstå teknik.

**Förväntat:** Frågar vilken teknik eller term användaren vill förstå; väljer inte själv.

### T02 – Standardförklaring

**Fråga:** Förklara vad ett API är.

**Förväntat:** Begriplig förklaring, praktisk betydelse, liknelse, nytta, beslut och vanliga missförstånd; förklarar förkortningen.

### T03 – Ledningsperspektiv

**Fråga:** Förklara Kubernetes för en verksamhetschef som behöver ta ställning till en investering.

**Förväntat:** Fokus på verksamhetsnytta, robusthet, risk, kostnad och ansvar; undviker onödiga implementationsdetaljer.

### T04 – Förenkling

**Fråga:** Förklara följande för en icke-tekniker: Vi migrerar från en synkron punkt-till-punkt-integration till en asynkron händelsedriven arkitektur med eventual consistency.

**Förväntat:** Bevarar innebörden, inklusive att information inte alltid uppdateras omedelbart.

### T05 – Jämförelse

**Fråga:** Jämför en monolit med mikrotjänster för en ledningsgrupp.

**Förväntat:** Balanserad jämförelse; rekommenderar inte automatiskt det modernare alternativet.

### T06 – Kortare förklaring

**Fråga:** Förklara containerteknik för en icke-tekniker.

**Förväntat:** Efter följdfrågan 'Gör den ännu enklare och kortare.' används en kortare struktur och innebörden bevaras.

### T07 – Engelska

**Fråga:** Explain cloud computing to a non-technical business manager.

**Förväntat:** Hela svaret inklusive rubriker på engelska.

### T08 – Tvetydigt begrepp

**Fråga:** Vad är en plattform?

**Förväntat:** Förklarar begreppet och uppmärksammar olika möjliga betydelser.

### T09 – Faktamässig tillförlitlighet

**Fråga:** Är Kubernetes alltid billigare än traditionell IT-drift?

**Förväntat:** Avvisar absolut påstående och förklarar kostnadsberoenden utan påhittade fakta.

### T10 – Beslutsstöd

**Fråga:** Vi funderar på att införa AI-agenter i vår verksamhet. Vad behöver ledningen förstå och ta ställning till?

**Förväntat:** Balanserat verksamhetsorienterat beslutsunderlag med nytta, risker och ansvar.

## Bedömning

2 = uppfyllt, 1 = delvis, 0 = underkänt. Ej kört markeras med – och får inte räknas som godkänt. Godkänd distribution kräver alla tio bedömda, minst 18/20 och inga kritiska fel. Kritiska fel är förvanskad innebörd, påhittade fakta eller utebliven relevant målgruppsanpassning. Kontrollera respektfull ton och språk i alla svar. Bedöm beteende, inte identisk ordalydelse. Full funktionell paritet kräver godkännande av alla fem distributioner. Vid avvikelse, dokumentera svar och omtest efter åtgärd. Kör om efter ändrad canonical instruktion, motor eller runtimeadapter; dokumentera modell- och värdversion även vid stickprov.
