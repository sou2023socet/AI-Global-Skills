"""Generate the authoritative canonical index, dependency map, and review report."""

from __future__ import annotations

import csv
import json
import re
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "registry.json"
SOURCES = ROOT / "registry" / "source-skills.json"


def tokens(value: str) -> set[str]:
    return {
        token
        for token in re.sub(r"[^a-z0-9 ]", " ", value.casefold()).split()
        if len(token) > 2
    }


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8-sig"))
    source_registry = json.loads(SOURCES.read_text(encoding="utf-8-sig"))
    records = registry["skills"]
    source_counts = {}
    for source in source_registry["skills"]:
        target = source["canonicalSkillId"]
        source_counts[target] = source_counts.get(target, 0) + 1

    index = {
        "version": "2.0",
        "description": "Authoritative ordered index of active canonical capabilities.",
        "skillCount": len(records),
        "sourceSkillCount": len(source_registry["skills"]),
        "skills": [
            {
                "id": record["id"],
                "name": record["name"],
                "lifecycleGroup": record["lifecycleGroup"],
                "executionOrder": record["executionOrder"],
                "candidateIds": record.get("candidateIds", []),
                "sourceSkillCount": source_counts.get(record["id"], 0),
                "dependencies": [item["skillId"] for item in record["dependencies"]],
                "status": record["status"],
                "path": record["path"],
            }
            for record in records
        ],
    }
    (ROOT / "registry" / "canonical-index.json").write_text(
        json.dumps(index, indent=2) + "\n", encoding="utf-8"
    )
    dependency_map = {
        "version": "2.0",
        "nodes": [record["id"] for record in records],
        "edges": [
            {"from": record["id"], "to": dependency["skillId"], "required": dependency["required"]}
            for record in records
            for dependency in record["dependencies"]
        ],
    }
    (ROOT / "registry" / "dependency-map.json").write_text(
        json.dumps(dependency_map, indent=2) + "\n", encoding="utf-8"
    )

    overlaps: list[dict[str, object]] = []
    for left, right in combinations(records, 2):
        left_tokens = tokens(left["name"] + " " + left["purpose"])
        right_tokens = tokens(right["name"] + " " + right["purpose"])
        score = len(left_tokens & right_tokens) / max(1, len(left_tokens | right_tokens))
        if score >= 0.35:
            overlaps.append({
                "SkillA": left["id"],
                "SkillB": right["id"],
                "Similarity": f"{score:.3f}",
                "Disposition": "review-evidence-not-automatic-duplicate",
            })
    with (ROOT / "reports" / "SKILL_OVERLAP_REVIEW.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["SkillA", "SkillB", "Similarity", "Disposition"],
        )
        writer.writeheader()
        writer.writerows(overlaps)
    print(f"Generated canonical index for {len(records)} skills and {len(overlaps)} overlap review pairs.")


if __name__ == "__main__":
    main()
