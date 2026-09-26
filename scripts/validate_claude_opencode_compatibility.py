#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    contract=yaml.safe_load((ROOT/"gpt-builder-1.5-contract.yaml").read_text(encoding="utf-8"))
    assessment=(ROOT/"docs/claude-opencode-compatibility.md").read_text(encoding="utf-8")

    for runtime in ("claude","opencode"):
        r=project["runtime"][runtime]
        if r.get("enabled") is not False:
            errors.append(f"{runtime} must remain disabled")
        if r.get("compatibility")!="equivalent":
            errors.append(f"{runtime} compatibility must be equivalent")
        if r.get("activation")!="not_active":
            errors.append(f"{runtime} activation must be not_active")
        if r.get("blocker")!="distribution_and_regression_not_implemented":
            errors.append(f"{runtime} blocker mismatch")
        c=contract["runtime_policy"]["inactive"][runtime]
        if c.get("compatibility")!="equivalent" or c.get("activation")!="not_active":
            errors.append(f"{runtime} contract status mismatch")

    for marker in [
        "Både Claude Projects och OpenCode bedöms som **equivalent candidates**",
        "samma språk som användaren",
        "förenkling utan att förvanska",
        "inga kritiska krav på kodkörning, zip-paketering",
        "distributionen byggs och valideras i CI",
    ]:
        if marker not in assessment:
            errors.append(f"assessment missing marker: {marker}")

    if errors:
        print("CLAUDE/OPENCODE COMPATIBILITY: FAIL")
        for e in errors: print("-",e)
        return 1
    print("CLAUDE/OPENCODE COMPATIBILITY: PASS")
    print("Claude=equivalent/not active; OpenCode=equivalent/not active.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
