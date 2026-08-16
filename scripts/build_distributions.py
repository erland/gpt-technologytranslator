#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, shutil, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
KNOWLEDGE = [
    Path("knowledge/examples.md"),
    Path("knowledge/explanation-patterns.md"),
]
CORE_FILES = [
    Path("gpt-instructions.md"),
    Path("conversation-starters.md"),
    Path("gpt-profile.md"),
    *KNOWLEDGE,
]


def version_from(args: argparse.Namespace) -> str:
    v = args.version.strip() if args.version else (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(v):
        raise SystemExit(f"Ogiltig version: {v!r}. Förväntat SemVer, t.ex. 1.0.0")
    return v


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def write_zip(src: Path, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    epoch = (2020, 1, 1, 0, 0, 0)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted(x for x in src.rglob("*") if x.is_file()):
            rel = p.relative_to(src).as_posix()
            info = zipfile.ZipInfo(rel, epoch)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, p.read_bytes())


def build_custom(version: str, stage: Path) -> Path:
    dst = stage / "custom"
    dst.mkdir(parents=True, exist_ok=True)
    # Preserve the original installation package content byte-for-byte.
    for rel in [Path("gpt-instructions.md"), Path("conversation-starters.md"), Path("gpt-profile.md"), Path("setup-guide.md"), *KNOWLEDGE]:
        copy_file(ROOT / rel, dst / rel)
    (dst / "VERSION").write_text(version + "\n", encoding="utf-8")
    return dst


def build_chat(version: str, stage: Path) -> Path:
    dst = stage / "chat"
    copy_file(ROOT / "portable/START-HERE.md", dst / "START-HERE.md")
    copy_file(ROOT / "gpt-instructions.md", dst / "assistant/instructions.md")
    copy_file(ROOT / "conversation-starters.md", dst / "assistant/conversation-starters.md")
    copy_file(ROOT / "gpt-profile.md", dst / "assistant/profile.md")
    for rel in KNOWLEDGE:
        copy_file(ROOT / rel, dst / rel)
    (dst / "VERSION").write_text(version + "\n", encoding="utf-8")
    files = {}
    for p in sorted(x for x in dst.rglob("*") if x.is_file() and x.name != "MANIFEST.json"):
        rel = p.relative_to(dst).as_posix()
        files[rel] = {"sha256": sha256(p), "bytes": p.stat().st_size}
    manifest = {
        "package": "technologytranslator",
        "display_name": "Tekniköversättaren",
        "format": "portable-chat-assistant",
        "version": version,
        "entrypoint": "START-HERE.md",
        "instructions": "assistant/instructions.md",
        "conversation_starters": "assistant/conversation-starters.md",
        "profile": "assistant/profile.md",
        "knowledge": [p.as_posix() for p in KNOWLEDGE],
        "files": files,
    }
    (dst / "MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return dst


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version")
    ap.add_argument("--output-dir", default=str(ROOT / "dist"))
    args = ap.parse_args()
    version = version_from(args)
    for rel in CORE_FILES + [Path("setup-guide.md"), Path("portable/START-HERE.md")]:
        if not (ROOT / rel).is_file():
            raise SystemExit(f"Obligatorisk fil saknas: {rel}")
    out = Path(args.output_dir).resolve()
    stage = out / ".stage"
    shutil.rmtree(stage, ignore_errors=True)
    stage.mkdir(parents=True)
    custom = build_custom(version, stage)
    chat = build_chat(version, stage)
    czip = out / f"technologytranslator-custom-gpt-v{version}.zip"
    pzip = out / f"technologytranslator-chat-v{version}.zip"
    write_zip(custom, czip)
    write_zip(chat, pzip)
    shutil.rmtree(stage)
    print(czip)
    print(pzip)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
