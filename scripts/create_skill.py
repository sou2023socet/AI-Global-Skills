"""Create and register one canonical skill without renumbering existing skills."""

from __future__ import annotations

import argparse
import copy
import json
import os
import re
import shutil
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REGISTRY_PATH = ROOT / "registry" / "registry.json"
SOURCE_REGISTRY_PATH = ROOT / "registry" / "source-skills.json"
TEMPLATE = ROOT / "templates" / "skill-authoring" / "SKILL.md"
RESERVED_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
NAME_PATTERN = re.compile(r"^Skill - \d{3} - [A-Z][A-Za-z0-9&'(). ]*$")
LIFECYCLE_ORDERS = {
    "foundation": 10,
    "recovery": 20,
    "research-planning": 30,
    "development": 40,
    "testing": 50,
    "security": 60,
    "quality": 70,
    "project-knowledge": 80,
    "delivery": 90,
    "roadmap-release": 100,
    "maintenance": 110,
    "automation": 120,
}
LOCK_PATH = ROOT / ".skill-creation.lock"


@contextmanager
def creation_lock():
    try:
        descriptor = os.open(str(LOCK_PATH), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise ValueError("another skill creation operation is already in progress") from exc
    try:
        os.write(descriptor, str(os.getpid()).encode("ascii"))
        os.close(descriptor)
        yield
    finally:
        LOCK_PATH.unlink(missing_ok=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--purpose", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--lifecycle-group", choices=sorted(LIFECYCLE_ORDERS), required=True)
    parser.add_argument("--provenance-repository", required=True)
    parser.add_argument("--provenance-path", required=True)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def atomic_write(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def validate_title(purpose: str) -> str:
    purpose = re.sub(r"\s+", " ", purpose.strip())
    if not purpose or RESERVED_CHARS.search(purpose) or purpose.endswith((".", " ")):
        raise ValueError("purpose is empty or contains invalid directory characters")
    if purpose.casefold() in {"general skill", "miscellaneous", "utility"}:
        raise ValueError("purpose is too generic")
    return purpose


def allocate_name(purpose: str, registry: dict[str, object]) -> tuple[str, str, int]:
    directories = [path.name for path in SKILLS.iterdir() if path.is_dir()]
    numbers = []
    for directory in directories:
        match = re.fullmatch(r"Skill - (\d{3}) - .+", directory)
        if not match:
            raise ValueError(f"invalid existing skill directory: {directory}")
        numbers.append(int(match.group(1)))
    registry_records = registry.get("skills", [])
    existing_names = {
        directory.casefold()
        for directory in directories
        if directory.casefold().startswith("skill - ")
    }
    existing_purposes = {
        re.sub(r"^Skill - \d{3} - ", "", name, flags=re.IGNORECASE).casefold()
        for name in existing_names
    }
    if purpose.casefold() in existing_purposes:
        raise ValueError(f"an existing skill already has purpose {purpose!r}")
    number = max(numbers, default=0) + 1
    name = f"Skill - {number:03d} - {purpose}"
    if not NAME_PATTERN.fullmatch(name) or name in directories:
        raise ValueError(f"invalid or conflicting generated skill name: {name}")
    return name, re.sub(r"[^a-z0-9]+", "-", purpose.casefold()).strip("-"), number


def make_skill_text(name: str, description: str) -> str:
    template = TEMPLATE.read_text(encoding="utf-8-sig")
    text = template.replace("Skill - NNN - Skill Purpose", name)
    text = text.replace("Describe the skill purpose and when it should be used.", description)
    return text


def _main() -> int:
    args = parse_args()
    purpose = validate_title(args.purpose)
    description = re.sub(r"\s+", " ", args.description.strip())
    if not description:
        raise ValueError("description must not be empty")
    registry = read_json(REGISTRY_PATH)
    source_registry = read_json(SOURCE_REGISTRY_PATH)
    if not isinstance(registry, dict) or not isinstance(source_registry, dict):
        raise ValueError("registry files must contain JSON objects")
    name, slug, number = allocate_name(purpose, registry)
    skill_id = f"skill-{slug}"
    records = registry["skills"]
    if any(record.get("id") == skill_id for record in records):
        raise ValueError(f"generated skill ID already exists: {skill_id}")
    path = f"skills/{name}/SKILL.md"
    source_id = f"local-{skill_id}"
    record = {
        "id": skill_id,
        "name": name,
        "version": "1.0.0",
        "contractVersion": "1.0",
        "status": "authored",
        "verification": {"structural": "not-run", "functional": "not-run", "platform": "not-run"},
        "implementationKind": "skill",
        "lifecycleGroup": args.lifecycle_group,
        "purpose": description,
        "description": description,
        "triggers": [f"task requires {purpose}"],
        "nonTriggers": ["unrelated work", "missing project identity", "permission bypass"],
        "provenance": [{
            "repository": args.provenance_repository,
            "path": args.provenance_path,
            "reviewStatus": "unknown",
        }],
        "dependencies": [],
        "inputs": [],
        "outputs": [{"name": "capabilityResult", "description": "Actionable result with evidence and limitations.", "required": True, "sensitivity": "internal"}],
        "tools": [{"name": "repository-inspection-and-approved-project-tools", "permission": "read-only", "requiresApproval": False, "sideEffects": "none by default"}],
        "validationCriteria": [{"criterion": "Package metadata, procedure, and registry path are structurally valid.", "evidenceType": "static"}],
        "candidateIds": [],
        "sourceSkillIds": [source_id],
        "executionOrder": LIFECYCLE_ORDERS[args.lifecycle_group],
        "canonical": True,
        "path": path,
    }
    source_record = {
        "id": source_id,
        "name": purpose,
        "repository": args.provenance_repository,
        "sourcePath": args.provenance_path,
        "canonicalPath": path,
        "disposition": "promoted-to-canonical",
        "promotionStatus": "canonical",
        "canonicalSkillId": skill_id,
    }
    if args.dry_run:
        print(json.dumps({"name": name, "id": skill_id, "path": path}, indent=2))
        return 0

    package = SKILLS / name
    staging = SKILLS / f".skill-create-{os.getpid()}"
    if package.exists() or staging.exists():
        raise ValueError(f"refusing to overwrite an existing package or staging path: {package}")
    registry_before = copy.deepcopy(registry)
    source_before = copy.deepcopy(source_registry)
    staging.mkdir()
    staged_package = staging / name
    staged_package.mkdir()
    try:
        (staged_package / "SKILL.md").write_text(make_skill_text(name, description), encoding="utf-8")
        records.append(record)
        records.sort(key=lambda item: (item["executionOrder"], item["name"]))
        source_registry["skills"].append(source_record)
        staged_package.replace(package)
        staging.rmdir()
        atomic_write(REGISTRY_PATH, registry)
        atomic_write(SOURCE_REGISTRY_PATH, source_registry)
        commands = [
            [sys.executable, str(ROOT / "scripts" / "generate_canonical_catalogue.py")],
            [sys.executable, str(ROOT / "scripts" / "generate_status_matrix.py")],
            [sys.executable, str(ROOT / "scripts" / "validate_registry.py")],
        ]
        for command in commands:
            subprocess.run(command, cwd=ROOT, check=True)
    except Exception:
        if package.exists():
            shutil.rmtree(package)
        if staging.exists():
            shutil.rmtree(staging)
        atomic_write(REGISTRY_PATH, registry_before)
        atomic_write(SOURCE_REGISTRY_PATH, source_before)
        raise
    print(f"Created and registered {name} at {path}")
    return 0


def main() -> int:
    with creation_lock():
        return _main()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Skill creation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
