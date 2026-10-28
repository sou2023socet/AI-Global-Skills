"""Remove only the duplicate packages created by a non-idempotent generation run."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "registry" / "registry.json"
SOURCE_REGISTRY_PATH = ROOT / "registry" / "source-skills.json"
DECISIONS_PATH = ROOT / "reports" / "SOURCE_MIGRATION_DECISIONS.csv"


def base_id(skill_id: str) -> str:
    return re.sub(r"-\d+$", "", skill_id)


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8-sig"))
    original_ids = {record["id"] for record in registry["skills"]}
    duplicate_ids = {
        skill_id
        for skill_id in original_ids
        if skill_id.endswith(("-2", "-3")) and base_id(skill_id) in original_ids
    }
    if not duplicate_ids:
        print("No generated duplicate packages found.")
        return
    records = []
    by_id = {record["id"]: record for record in registry["skills"]}
    for record in registry["skills"]:
        if record["id"] in duplicate_ids:
            target = by_id[base_id(record["id"])]
            target.setdefault("sourceSkillIds", []).extend(
                record.get("sourceSkillIds", [])
            )
            continue
        records.append(record)
    registry["skills"] = records
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")

    source_registry = json.loads(
        SOURCE_REGISTRY_PATH.read_text(encoding="utf-8-sig")
    )
    for item in source_registry["skills"]:
        if item["canonicalSkillId"] in duplicate_ids:
            item["canonicalSkillId"] = base_id(item["canonicalSkillId"])
            item["canonicalPath"] = f"skills/{item['canonicalSkillId']}/SKILL.md"
            item["disposition"] = "promoted-to-canonical"
    SOURCE_REGISTRY_PATH.write_text(
        json.dumps(source_registry, indent=2) + "\n", encoding="utf-8"
    )

    import csv

    with DECISIONS_PATH.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
        fieldnames = list(rows[0])
    for row in rows:
        if row.get("Canonical_Skill_ID") in duplicate_ids:
            row["Canonical_Skill_ID"] = base_id(row["Canonical_Skill_ID"])
            row["Canonical_Destination"] = (
                f"skills/{row['Canonical_Skill_ID']}/SKILL.md"
            )
    with DECISIONS_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    for duplicate_id in sorted(duplicate_ids):
        duplicate_path = ROOT / "skills" / duplicate_id
        if duplicate_path.is_dir():
            shutil.rmtree(duplicate_path)
    print(f"Removed {len(duplicate_ids)} generated duplicate packages.")


if __name__ == "__main__":
    main()
