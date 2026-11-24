"""Verify pinned Engine archive contents before executing its scripts."""
import hashlib, json, sys, zipfile
from pathlib import Path, PurePosixPath
archive, target = map(Path, sys.argv[1:])
with zipfile.ZipFile(archive) as z:
    names = z.namelist()
    assert len(names) == len(set(names)), 'Duplicate archive paths'
    for name in names:
        p = PurePosixPath(name)
        assert not p.is_absolute() and '..' not in p.parts and '\\' not in name, name
    manifest = json.loads(z.read('engine-package.json'))
    assert manifest['version'] == '1.6.33' and manifest['engine_id'] == 'gpt-byggaren'
    assert set(names) == set(manifest['files']) | {'engine-package.json'}
    for name, digest in manifest['files'].items():
        assert hashlib.sha256(z.read(name)).hexdigest() == digest, name
    z.extractall(target)
print('Engine integrity PASS')
