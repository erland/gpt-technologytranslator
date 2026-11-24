import hashlib
import json
from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]

class BehaviorRegression(unittest.TestCase):
    def test_original_content(self):
        baseline = json.loads((ROOT/'tests/baseline.json').read_text())
        for path, digest in baseline.items():
            with self.subTest(path=path):
                self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(), digest)
        self.assertEqual(len(list((ROOT/'knowledge').glob('*.md'))), 2)

    def test_behavior_markers(self):
        text = (ROOT/'canonical/instructions.md').read_text()
        for marker in ['Svara alltid på samma språk som användaren skriver på.', 'Aldrig nedlåtande.', 'Förklara varför något spelar roll, inte bara vad det är.', 'Fokusera på verksamhetsnytta, konsekvenser, risker och beslut.', 'Förenkla utan att förvanska.', 'Säg när något är en förenklad bild.', 'Hitta inte på fakta om produkter, lagar, priser eller aktuella händelser.', 'Undvik långa svar om användaren inte efterfrågar fördjupning.']:
            self.assertIn(marker, text)

    def test_targets(self):
        cfg = yaml.safe_load((ROOT/'gpt-project.yaml').read_text())
        self.assertEqual(set(cfg['build_system']['targets']), {'project','chat','plugin','claude_project','claude_skills','opencode'})
        self.assertFalse(cfg['runtime']['custom_gpt']['enabled'])
        self.assertEqual(cfg['tools']['tools'], [])
        self.assertEqual(cfg['model_robustness']['level'], 'lightweight')
