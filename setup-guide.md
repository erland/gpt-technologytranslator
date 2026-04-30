# Så skapar du GPT:n “Tekniköversättaren”

## 1. Skapa en ny GPT

1. Gå till GPT-byggaren i ChatGPT.
2. Skapa en ny GPT.
3. Ange namn: **Tekniköversättaren**.
4. Använd beskrivningen från `gpt-profile.md`.

## 2. Lägg in instruktionerna

1. Öppna filen `gpt-instructions.md`.
2. Kopiera hela innehållet.
3. Klistra in det i GPT:ns instruktionsfält.

## 3. Lägg till conversation starters

Använd starters från `conversation-starters.md`.

Rekommenderade starters:

- Förklara en teknisk term för mig
- Hjälp mig förstå en teknik utan tekniska detaljer
- Gör en teknisk fråga begriplig för icke-tekniker
- Hjälp mig förklara teknik för en ledningsgrupp

Dessa starters ska inte innehålla en specifik term. Tanken är att GPT:n först frågar användaren vad som ska förklaras.

## 4. Lägg till kunskapsfiler

Ladda upp filerna i katalogen `knowledge/` som kunskapsfiler:

- `explanation-patterns.md`
- `examples.md`

## 5. Rekommenderade funktioner

Den här GPT:n behöver normalt inte:

- bildgenerering
- kodtolkning
- webbsökning som standard

Om du vill att den även ska kunna förklara aktuella produkter, trender, lagar eller nyligen ändrade tekniska plattformar kan webbsökning vara användbart. Annars räcker instruktionerna och kunskapsfilerna långt.

## 6. Testa GPT:n

Testa exempelvis:

- Förklara API för en verksamhetschef
- Förklara teknisk skuld för en ledningsgrupp
- Förklara Kubernetes utan tekniska detaljer
- Gör denna tekniska text begriplig för en jurist: [klistra in text]
- Jämför molndrift och egen drift för en styrgrupp

## 7. Kontrollera önskat beteende

GPT:n bör:

- svara på samma språk som frågan
- fråga vad som ska förklaras när en generell starter används
- inte börja med tekniska detaljer
- använda vardagliga liknelser
- fokusera på verksamhetsnytta, konsekvens och beslut
- hålla en respektfull ton
