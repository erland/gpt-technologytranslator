# Tekniköversättaren

Repository för Custom GPT:n **Tekniköversättaren** och dess portabla ChatGPT-distribution.

## Nuvarande GPT-konfiguration

- `gpt-instructions.md` – instruktioner som klistras in i GPT Builder.
- `conversation-starters.md` – conversation starters.
- `gpt-profile.md` – namn, beskrivning och välkomsttext.
- `knowledge/explanation-patterns.md` – Knowledge.
- `knowledge/examples.md` – Knowledge.
- `setup-guide.md` – installationsguide.

De ursprungliga GPT-filerna är kanoniska och kopieras utan innehållsförändring till Custom GPT-distributionen.

## Bygga distributioner lokalt

```bash
python3 scripts/build_distributions.py
python3 scripts/validate_distributions.py
```

Det skapar:

- `dist/technologytranslator-custom-gpt-vX.Y.Z.zip`
- `dist/technologytranslator-chat-vX.Y.Z.zip`

Vid vanliga byggen används `VERSION`.

## GitHub Release

När en GitHub Release publiceras måste taggen följa `v<semver>`, exempelvis `v1.0.0` eller `v1.1.0`.

Release-taggen är då versionskälla och används för:

- ZIP-filernas namn,
- `VERSION` inne i båda paketen,
- `MANIFEST.json` i portable-paketet.

Workflowen validerar båda paketen och bifogar dem automatiskt som assets på GitHub Releasen.

## Portabel ChatGPT-version

Bifoga `technologytranslator-chat-vX.Y.Z.zip` i en vanlig ChatGPT-konversation och be ChatGPT läsa `START-HERE.md` först.
