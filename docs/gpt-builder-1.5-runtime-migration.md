# GPT Byggaren 1.5.0 – migreringsplan

Projekt: **Tekniköversättaren**

## Preserve-first baseline

Migreringen ska bevara:
- version **1.0.0**
- exakt **2 Knowledge-filer**
- slutlig instruktion byte-identiskt som canonical beteendekälla
- svar på samma språk som användaren
- målgruppsanpassning för icke-tekniker
- respektfull och icke-nedlåtande ton
- vardagsspråk framför teknisk jargong
- förenkling utan att förvanska
- fokus på verksamhetsnytta, konsekvenser, risker och beslut
- tydlig separation mellan vad mottagaren behöver förstå och vad tekniker kan hantera
- försiktighet vid tvetydighet och kontextberoende
- inga påhittade fakta om produkter, lagar, priser eller aktuella händelser
- befintliga Chat- och Custom GPT-distributioner

## Steg

1. Etablera canonical instruktion och projektkontrakt.
2. Normalisera capability-, artifact-, workspace/state- och tool-kontrakt.
3. Normalisera Chat och Custom GPT till samma canonical källa.
4. Bedöm Claude Projects och OpenCode.
5. Bedöm OpenAI Plugin.
6. Generalisera build, parity, CI och release via runtime-registry.
7. Slutlig readiness, dokumentationssynk och 7/7-gate.

## Aktivering av nya runtimes

En runtime får bara aktiveras om den kan bevara målgruppsanpassning, samma språk som användaren, förenkling utan förvanskning, osäkerhetshantering och samma canonical behavior.
