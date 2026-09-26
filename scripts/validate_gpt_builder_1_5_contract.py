#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    contract=yaml.safe_load((ROOT/"gpt-builder-1.5-contract.yaml").read_text(encoding="utf-8"))
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    canonical=(ROOT/project["instructions"]["canonical"]).read_bytes()
    legacy=(ROOT/project["instructions"]["legacy_source"]).read_bytes()
    text=canonical.decode("utf-8")
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()

    if contract["builder"]["target_version"]!="1.5.0":
        errors.append("target builder version must be 1.5.0")
    if contract["builder"]["behavior_preserving"] is not True:
        errors.append("migration must remain behavior-preserving")
    if canonical!=legacy:
        errors.append("canonical instruction diverges from legacy instruction")
    if version!="1.0.0":
        errors.append(f"VERSION changed during migration: {version!r}")

    knowledge=sorted((ROOT/"knowledge").glob("*.md"))
    if len(knowledge)!=2:
        errors.append(f"expected exactly 2 Knowledge files, found {len(knowledge)}")

    markers=[
        "Svara alltid på samma språk som användaren skriver på.",
        "Aldrig nedlåtande.",
        "Förklara varför något spelar roll, inte bara vad det är.",
        "Fokusera på verksamhetsnytta, konsekvenser, risker och beslut.",
        "Förenkla utan att förvanska.",
        "Säg när något är en förenklad bild.",
        "Hitta inte på fakta om produkter, lagar, priser eller aktuella händelser.",
        "Undvik långa svar om användaren inte efterfrågar fördjupning.",
    ]
    for marker in markers:
        if marker not in text:
            errors.append(f"canonical instruction missing behavior marker: {marker}")

    for key in [
        "same_language_as_user",
        "respectful_and_calm",
        "never_patronizing",
        "plain_language_before_jargon",
        "explain_why_it_matters",
        "focus_on_business_value_consequences_risks_decisions",
        "simplify_without_distortion",
        "do_not_invent_current_facts",
        "keep_answers_short_unless_depth_requested",
    ]:
        if contract["behavior"].get(key) is not True:
            errors.append(f"{key} must be true")

    if errors:
        print("GPT BUILDER 1.5 CONTRACT: FAIL")
        for e in errors: print("-",e)
        return 1
    print("GPT BUILDER 1.5 CONTRACT: PASS")
    print("VERSION 1.0.0; 2 Knowledge; language/audience/plain-language/uncertainty behavior preserved")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
