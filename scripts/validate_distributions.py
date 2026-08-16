#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
KNOWLEDGE = [
    Path("knowledge/examples.md"),
    Path("knowledge/explanation-patterns.md"),
]
ORIGINAL_CUSTOM = [
    Path("gpt-instructions.md"),
    Path("conversation-starters.md"),
    Path("gpt-profile.md"),
    Path("setup-guide.md"),
    *KNOWLEDGE,
]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def expected_version(arg: str | None) -> str:
    v = arg or (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(v):
        raise SystemExit(f"Ogiltig version: {v}")
    return v


def read_zip(path: Path) -> dict[str, bytes]:
    if not path.is_file():
        raise SystemExit(f"ZIP saknas: {path}")
    with zipfile.ZipFile(path) as z:
        bad = z.testzip()
        if bad:
            raise SystemExit(f"Korrupt ZIP {path}: {bad}")
        return {n: z.read(n) for n in z.namelist() if not n.endswith("/")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version")
    ap.add_argument("--dist-dir", default=str(ROOT / "dist"))
    args = ap.parse_args()
    v = expected_version(args.version)
    dist = Path(args.dist_dir).resolve()
    c = read_zip(dist / f"technologytranslator-custom-gpt-v{v}.zip")
    p = read_zip(dist / f"technologytranslator-chat-v{v}.zip")

    originals = {rel.as_posix(): (ROOT / rel).read_bytes() for rel in ORIGINAL_CUSTOM}
    for name, data in originals.items():
        if c.get(name) != data:
            raise SystemExit(f"Custom GPT-filen avviker från källan: {name}")

    portable_map = {
        "assistant/instructions.md": originals["gpt-instructions.md"],
        "assistant/conversation-starters.md": originals["conversation-starters.md"],
        "assistant/profile.md": originals["gpt-profile.md"],
        **{rel.as_posix(): originals[rel.as_posix()] for rel in KNOWLEDGE},
    }
    for name, data in portable_map.items():
        if p.get(name) != data:
            raise SystemExit(f"Portable-filen avviker från originalet: {name}")

    expected_version_bytes = (v + "\n").encode()
    if c.get("VERSION") != expected_version_bytes:
        raise SystemExit("Fel VERSION i custom-paketet")
    if p.get("VERSION") != expected_version_bytes:
        raise SystemExit("Fel VERSION i portable-paketet")

    try:
        manifest = json.loads(p["MANIFEST.json"])
    except Exception as exc:
        raise SystemExit(f"Ogiltig MANIFEST.json: {exc}")
    if manifest.get("version") != v:
        raise SystemExit("Fel version i MANIFEST.json")
    if manifest.get("knowledge") != [x.as_posix() for x in KNOWLEDGE]:
        raise SystemExit("Fel Knowledge-lista i MANIFEST.json")
    for name, meta in manifest.get("files", {}).items():
        if name not in p or digest(p[name]) != meta.get("sha256"):
            raise SystemExit(f"Manifest-hash stämmer inte: {name}")
        if len(p[name]) != meta.get("bytes"):
            raise SystemExit(f"Manifest-storlek stämmer inte: {name}")

    print(f"OK: technologytranslator v{v} validerad; Custom GPT-kärnan är byte-identisk med källorna")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
