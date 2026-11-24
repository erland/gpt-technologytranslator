#!/usr/bin/env bash
set -euo pipefail
engine="$1"
version="$2"
export PYTHONDONTWRITEBYTECODE=1
# Keep source archive metadata aligned with the requested release version.
python - "$version" <<'VERSION_PY'
import re, sys, yaml
from pathlib import Path
version = sys.argv[1]
if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.-]+)?', version):
    raise SystemExit('Invalid version: ' + version)
p = Path('gpt-project.yaml')
cfg = yaml.safe_load(p.read_text())
if cfg['release']['current_version'] != version:
    cfg['release']['current_version'] = version
    p.write_text(yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False))
Path('VERSION').write_text(version + '\n')
VERSION_PY
python "$engine/scripts/lint_gpt_project.py" --project-root .
python -m unittest discover -s tests -v
python scripts/build_distributions.py --project-root . --version "$version"
python scripts/validate_distributions.py --project-root .
python "$engine/scripts/verify_distribution_outputs.py" --project-root . --version "$version"
python tests/check_distribution_parity.py "$version"
python "$engine/scripts/validate_generated_delivery.py" --project-root . --dist-dir dist --project-zip "dist/technologytranslator-project-${version}.zip"
(cd dist && sha256sum -c SHA256SUMS.txt)
