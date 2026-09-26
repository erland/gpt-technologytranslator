#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    contract=yaml.safe_load((ROOT/"gpt-builder-1.5-contract.yaml").read_text(encoding="utf-8"))
    assessment=(ROOT/"docs/openai-plugin-compatibility.md").read_text(encoding="utf-8")

    plugin=project["runtime"]["openai_plugin"]
    if plugin.get("enabled") is not False:
        errors.append("OpenAI Plugin must remain disabled")
    if plugin.get("compatibility")!="equivalent":
        errors.append("OpenAI Plugin compatibility must be equivalent")
    if plugin.get("status")!="assessed_not_active":
        errors.append("OpenAI Plugin status must be assessed_not_active")
    if plugin.get("architecture")!="skills_first":
        errors.append("OpenAI Plugin architecture must be skills_first")
    if plugin.get("activation")!="not_active":
        errors.append("OpenAI Plugin activation must be not_active")
    if plugin.get("blocker")!="distribution_and_regression_not_implemented":
        errors.append("OpenAI Plugin blocker mismatch")

    c=contract["runtime_policy"]["inactive"]["openai_plugin"]
    if c.get("compatibility")!="equivalent" or c.get("activation")!="not_active":
        errors.append("OpenAI Plugin contract status mismatch")
    if c.get("architecture")!="skills_first":
        errors.append("OpenAI Plugin contract architecture mismatch")

    for marker in [
        "skills-first",
        "Tekniköversättarens kärnroll är textcentrerad",
        "förenkling utan att förvanska",
        "inga fabricerade aktuella fakta",
        "Ingen Plugin-distribution byggs",
    ]:
        if marker not in assessment:
            errors.append(f"Plugin assessment missing marker: {marker}")

    if errors:
        print("OPENAI PLUGIN COMPATIBILITY: FAIL")
        for e in errors: print("-",e)
        return 1
    print("OPENAI PLUGIN COMPATIBILITY: PASS")
    print("Plugin is an equivalent skills-first candidate and remains not active until distribution/regression exists.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
