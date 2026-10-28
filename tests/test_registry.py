import json
import unittest
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from orchestration.select_skills import select


class RegistryContractTests(unittest.TestCase):
    def test_registry_covers_all_candidates(self):
        registry = json.loads((ROOT / "registry" / "registry.json").read_text(encoding="utf-8-sig"))
        records = registry["skills"]
        self.assertGreaterEqual(len(records), 80)
        self.assertEqual(
            {candidate for record in records for candidate in record["candidateIds"]},
            {f"{number:02d}" for number in range(1, 81)},
        )

    def test_every_registered_skill_has_instruction_file(self):
        registry = json.loads((ROOT / "registry" / "registry.json").read_text(encoding="utf-8-sig"))
        for record in registry["skills"]:
            skill_file = ROOT / "skills" / record["id"] / "SKILL.md"
            self.assertTrue(skill_file.is_file(), record["id"])
            content = skill_file.read_text(encoding="utf-8")
            for section in ("## Purpose", "## Activation", "## Required procedure"):
                self.assertIn(section, content, record["id"])

    def test_selection_requires_project_context(self):
        with self.assertRaises(ValueError):
            select("project discovery", project_context=False)

    def test_selection_is_deterministic(self):
        first = select("project discovery", project_context=True)
        second = select("project discovery", project_context=True)
        self.assertEqual(
            [record["id"] for record in first],
            [record["id"] for record in second],
        )

    def test_selection_rejects_empty_task(self):
        with self.assertRaises(ValueError):
            select("   ", project_context=True)

    def test_selection_orders_dependencies_before_selected_skills(self):
        selected = select("project discovery", project_context=True)
        positions = {record["id"]: index for index, record in enumerate(selected)}
        for record in selected:
            for dependency in record["dependencies"]:
                self.assertLess(positions[dependency["skillId"]], positions[record["id"]])

    def test_promoted_source_skills_have_canonical_destinations(self):
        source = json.loads(
            (ROOT / "registry" / "source-skills.json").read_text(encoding="utf-8")
        )
        self.assertTrue(source["skills"])
        for record in source["skills"]:
            self.assertTrue(record["canonicalSkillId"])
            self.assertTrue(
                (ROOT / "skills" / record["canonicalSkillId"] / "SKILL.md").is_file()
            )


if __name__ == "__main__":
    unittest.main()
