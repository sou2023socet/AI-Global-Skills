"""Validate the complete canonical registry and source-to-capability coverage."""

from __future__ import annotations

import json
import csv
import re
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "registry.json"
CANDIDATES = ROOT / "registry" / "candidates.json"
INVENTORY = ROOT / "docs" / "migration" / "SOURCE_INVENTORY.csv"
DECISIONS = ROOT / "reports" / "SOURCE_MIGRATION_DECISIONS.csv"
SOURCE_REGISTRY = ROOT / "registry" / "source-skills.json"
REQUIRED_SECTIONS = ("# ", "## Purpose", "## Activation", "## Required procedure")
SKILL_DIRECTORY_PATTERN = re.compile(r"^Skill - (?P<number>\d{3}) - (?P<purpose>.+)$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"{path.relative_to(ROOT)}: unable to read valid JSON: {exc}")
        return None


def validate_source_coverage(errors: list[str]) -> None:
    try:
        with INVENTORY.open(newline="", encoding="utf-8-sig") as handle:
            inventory = list(csv.DictReader(handle))
        with DECISIONS.open(newline="", encoding="utf-8-sig") as handle:
            decisions = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        fail(errors, f"source migration coverage is unreadable: {exc}")
        return
    inventory_ids = [row.get("Resource_ID", "") for row in inventory]
    decision_ids = [row.get("Resource_ID", "") for row in decisions]
    if not inventory_ids or len(inventory_ids) != len(set(inventory_ids)):
        fail(errors, "source inventory must contain unique Resource_ID values")
    if set(inventory_ids) != set(decision_ids):
        fail(errors, "source migration decisions must cover exactly the source inventory")
    required_columns = {
        "Migration_Decision",
        "Decision_Reason",
        "Canonical_Destination",
        "Verification_Status",
    }
    if decisions and not required_columns.issubset(decisions[0]):
        fail(errors, "source migration decisions are missing required disposition columns")


def validate_source_registry(errors: list[str]) -> None:
    source_data = load_json(SOURCE_REGISTRY, errors)
    if not isinstance(source_data, dict) or not isinstance(source_data.get("skills"), list):
        return
    records = source_data["skills"]
    if not records:
        fail(errors, "source skill registry must contain source skill records")
    ids: set[str] = set()
    destinations: dict[str, list[str]] = defaultdict(list)
    for record in records:
        if not isinstance(record, dict):
            fail(errors, "source skill registry contains a non-object record")
            continue
        skill_id = record.get("id")
        if not isinstance(skill_id, str) or skill_id in ids:
            fail(errors, f"invalid or duplicate source skill ID: {skill_id!r}")
            continue
        ids.add(skill_id)
        skill_path = ROOT / str(record.get("canonicalPath", ""))
        if not skill_path.is_file():
            fail(errors, f"{skill_id}: missing consolidated source package")
        provenance = skill_path.with_name("source-provenance.json")
        if record.get("canonicalSkillId") not in {None, skill_id}:
            target = ROOT / str(record.get("canonicalPath", ""))
            if not target.is_file():
                fail(errors, f"{skill_id}: missing canonical destination {record['canonicalSkillId']}")
            destinations[str(record["canonicalSkillId"])].append(skill_id)
        elif not provenance.is_file():
            fail(errors, f"{skill_id}: missing source provenance")
    if len(destinations) == 0:
        fail(errors, "source skills must record canonical destinations")


def validate_skill_directories(errors: list[str]) -> None:
    directories = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
    numbers: list[int] = []
    names: set[str] = set()
    for directory in directories:
        match = SKILL_DIRECTORY_PATTERN.fullmatch(directory.name)
        if not match:
            fail(errors, f"invalid skill directory name: {directory.name}")
            continue
        number = int(match.group("number"))
        if number in numbers:
            fail(errors, f"duplicate skill directory number: {number:03d}")
        numbers.append(number)
        if directory.name.casefold() in names:
            fail(errors, f"duplicate skill directory name: {directory.name}")
        names.add(directory.name.casefold())
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            fail(errors, f"{directory.name}: missing SKILL.md")
            continue
        content = skill_file.read_text(encoding="utf-8-sig")
        name_match = re.search(r"^name:\s*(.+?)\s*$", content, re.MULTILINE)
        description_match = re.search(r"^description:\s*(.+?)\s*$", content, re.MULTILINE)
        heading_match = re.search(r"^#\s+(.+?)\s*$", content, re.MULTILINE)
        if not name_match or name_match.group(1).strip() != directory.name:
            fail(errors, f"{directory.name}: name metadata must match directory")
        if not description_match or not description_match.group(1).strip():
            fail(errors, f"{directory.name}: missing non-empty description metadata")
        if not heading_match or heading_match.group(1).strip() != directory.name:
            fail(errors, f"{directory.name}: primary H1 must match directory")
    if sorted(numbers) != list(range(1, len(directories) + 1)):
        fail(errors, "skill directory numbers must be continuous from 001")


def main() -> int:
    errors: list[str] = []
    validate_skill_directories(errors)
    data = load_json(REGISTRY, errors)
    candidates = load_json(CANDIDATES, errors)
    if not isinstance(data, dict):
        return 1
    records = data.get("skills")
    if not isinstance(records, list):
        fail(errors, "registry.skills must be an array")
        records = []
    ids = [record.get("id") for record in records if isinstance(record, dict)]
    if len(ids) != len(set(ids)):
        fail(errors, "registry contains duplicate skill IDs")
    candidate_ids: list[str] = []
    dependencies: dict[str, list[str]] = {}
    registry_by_candidate: dict[str, str] = {}
    for record in records:
        if not isinstance(record, dict):
            fail(errors, "registry contains a non-object skill record")
            continue
        skill_id = record.get("id")
        if not isinstance(skill_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_id):
            fail(errors, f"invalid skill id: {skill_id!r}")
            continue
        if not isinstance(record.get("description"), str) or not record["description"].strip():
            fail(errors, f"{skill_id}: registry description is missing")
        registry_path = record.get("path")
        if not isinstance(registry_path, str) or not registry_path.startswith("skills/"):
            fail(errors, f"{skill_id}: registry path is missing or invalid")
            skill_path = ROOT / "skills" / "__missing__" / "SKILL.md"
        else:
            skill_path = ROOT / Path(registry_path)
        if not skill_path.is_file():
            fail(errors, f"{skill_id}: missing {skill_path.relative_to(ROOT)}")
        else:
            content = skill_path.read_text(encoding="utf-8")
            for section in REQUIRED_SECTIONS:
                if section not in content:
                    fail(errors, f"{skill_id}: missing section {section!r}")
            if not re.search(rf"^id:\s*{re.escape(skill_id)}\s*$", content, re.MULTILINE):
                fail(errors, f"{skill_id}: front matter id does not match registry")
        record_candidates = record.get("candidateIds", [])
        if not isinstance(record_candidates, list):
            fail(errors, f"{skill_id}: candidateIds must be an array")
            record_candidates = []
        for candidate_id in record_candidates:
            if candidate_id in candidate_ids:
                fail(errors, f"candidate {candidate_id}: mapped more than once")
            candidate_ids.append(candidate_id)
            registry_by_candidate[candidate_id] = skill_id
        record_dependencies = record.get("dependencies", [])
        if not isinstance(record_dependencies, list):
            fail(errors, f"{skill_id}: dependencies must be an array")
            record_dependencies = []
        dependency_ids: list[str] = []
        for dependency in record_dependencies:
            if not isinstance(dependency, dict) or not isinstance(dependency.get("skillId"), str):
                fail(errors, f"{skill_id}: dependency must contain a skillId")
                continue
            dependency_ids.append(dependency["skillId"])
            if dependency["skillId"] not in ids:
                fail(errors, f"{skill_id}: unknown dependency {dependency.get('skillId')!r}")
        dependencies[skill_id] = dependency_ids
    expected = {f"{number:02d}" for number in range(1, 81)}
    actual = set(candidate_ids)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing:
        fail(errors, f"missing candidate IDs: {', '.join(missing)}")
    if extra:
        fail(errors, f"invalid candidate IDs: {', '.join(extra)}")
    names = [str(record.get("name", "")).casefold().strip() for record in records]
    if len(names) != len(set(names)):
        fail(errors, "registry contains duplicate canonical names")
    orders = [record.get("executionOrder") for record in records]
    if any(not isinstance(order, int) for order in orders):
        fail(errors, "every canonical skill requires an integer executionOrder")
    if any(record.get("canonical") is not True for record in records):
        fail(errors, "every registry record must be explicitly canonical")
    if isinstance(candidates, list):
        candidate_catalogue_ids = [item.get("id") for item in candidates if isinstance(item, dict)]
        if len(candidates) != 80 or set(candidate_catalogue_ids) != expected:
            fail(errors, "candidate catalogue must contain exactly IDs 01 through 80")
        for item in candidates:
            if isinstance(item, dict) and item.get("id") in registry_by_candidate:
                if item.get("skillId") != registry_by_candidate[item["id"]]:
                    fail(errors, f"candidate {item['id']}: catalogue and registry skill IDs differ")
            else:
                fail(errors, f"candidate catalogue contains invalid or unmapped entry: {item!r}")
    validate_source_coverage(errors)
    validate_source_registry(errors)
    tokens: dict[str, set[str]] = {}
    for record in records:
        name = re.sub(r"[^a-z0-9 ]", " ", str(record.get("name", "")).casefold())
        tokens[record["id"]] = {token for token in name.split() if len(token) > 2}
    overlaps = []
    for left, right in combinations(records, 2):
        a = tokens[left["id"]]
        b = tokens[right["id"]]
        similarity = len(a & b) / max(1, len(a | b))
        if similarity >= 0.8:
            overlaps.append(f"{left['id']} ~ {right['id']} ({similarity:.2f})")
    if overlaps:
        fail(errors, "likely duplicate canonical names require review: " + "; ".join(overlaps[:20]))
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(skill_id: str) -> None:
        if skill_id in visiting:
            fail(errors, f"dependency cycle detected at {skill_id}")
            return
        if skill_id in visited:
            return
        visiting.add(skill_id)
        for dependency_id in dependencies.get(skill_id, []):
            visit(dependency_id)
        visiting.remove(skill_id)
        visited.add(skill_id)

    for skill_id in dependencies:
        visit(skill_id)
    if errors:
        print("Registry validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Registry validation passed: {len(records)} canonical skills, source coverage, and dependencies are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
