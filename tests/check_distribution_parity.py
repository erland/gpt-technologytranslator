"""Check built runtime artifacts against the canonical project."""
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
version = sys.argv[1]
canonical = (ROOT/'canonical/instructions.md').read_text().strip()
knowledge = {p.name:p.read_bytes() for p in (ROOT/'knowledge').glob('*.md')}
expected = {'chat':'assistant/instructions.md','plugin':'skills/technology-explanation/SKILL.md','claude-project':'project/instructions.md','claude-skills':'skills/technology-explanation/SKILL.md','opencode':'AGENTS.md'}
contracts = []
for target, instruction in expected.items():
    with zipfile.ZipFile(ROOT/f'dist/technologytranslator-{target}-{version}.zip') as z:
        assert z.testzip() is None, target
        assert canonical in z.read(instruction).decode().replace('\r\n','\n'), target
        for name, data in knowledge.items():
            matches = [p for p in z.namelist() if p.split('/')[-1] == name]
            assert matches and all(z.read(p)==data for p in matches), (target,name)
        paths = [p for p in z.namelist() if p.endswith('/runtime-contract.json') or p=='runtime-contract.json']
        assert len(paths)==1, (target,paths)
        c=json.loads(z.read(paths[0]))
        contracts.append({k:c[k] for k in ('capabilities','artifacts','workspace_state','tools')})
        assert '.gitignore' not in z.namelist(), target
    print(f'{target}: behavior, knowledge, contract and ZIP PASS')
assert all(c==contracts[0] for c in contracts), 'Runtime contracts differ'
print('Structural parity PASS')

with zipfile.ZipFile(ROOT/f'dist/technologytranslator-project-{version}.zip') as z:
    import yaml
    assert z.read('VERSION').decode().strip() == version
    assert yaml.safe_load(z.read('gpt-project.yaml'))['release']['current_version'] == version
    assert not any(p.startswith(('build/', 'dist/')) for p in z.namelist())
print('Project ZIP version and source hygiene PASS')
