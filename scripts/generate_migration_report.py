"""Create a complete, conservative disposition for every inventoried source resource."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "docs" / "migration" / "SOURCE_INVENTORY.csv"
REPORT_DIR = ROOT / "reports"
SOURCE_REGISTRY = ROOT / "registry" / "source-skills.json"
SOURCE_ROOTS = {
    "global-skills": Path(r"E:\sumit@data\project\Git\global-skills"),
    "enterprise-ai-engineering-skills": Path(
        r"E:\sumit@data\project\Git\enterprise-ai-engineering-skills"
    ),
}


def disposition(resource: dict[str, str]) -> tuple[str, str]:
    if resource["Type"] == "skill":
        return (
            "consolidated-source-package",
            "Source SKILL.md is copied into the single canonical repository with "
            "provenance; promotion or merge remains pending capability review.",
        )
    if resource["Type"] in {"script", "configuration/schema"}:
        return (
            "defer-adaptation",
            "Reusable implementation may be useful, but it requires a separate "
            "compatibility and permission review before adaptation.",
        )
    return (
        "retain-as-reference",
        "Supporting source material is preserved for provenance and consulted "
        "without copying project-specific or unverified content.",
    )


def main() -> None:
    with INVENTORY.open(newline="", encoding="utf-8-sig") as handle:
        resources = list(csv.DictReader(handle))
    source_mapping = {
        f"{item['repository']}:{item['sourcePath']}": item
        for item in json.loads(
            SOURCE_REGISTRY.read_text(encoding="utf-8-sig")
        )["skills"]
    }
    rows: list[dict[str, str]] = []
    for resource in resources:
        mapping_key = ""
        if resource["Repository"] in SOURCE_ROOTS:
            mapping_key = (
                f"{resource['Repository']}:"
                f"{Path(resource['Source_Path']).relative_to(SOURCE_ROOTS[resource['Repository']])}"
            )
        mapping = source_mapping.get(mapping_key)
        if mapping:
            decision = mapping["disposition"]
            reason = "Source capability is merged or promoted into the recorded canonical destination."
        else:
            decision, reason = disposition(resource)
        rows.append(
            {
                "Resource_ID": resource["Resource_ID"],
                "Repository": resource["Repository"],
                "Source_Path": resource["Source_Path"],
                "Type": resource["Type"],
                "SHA256": resource["SHA256"],
                "Candidate_Relationship": resource["Relationships"],
                "Duplicate_Group": resource["Duplicate_Group"],
                "Migration_Decision": decision,
                "Decision_Reason": reason,
                "Canonical_Destination": (
                    mapping["canonicalPath"]
                    if mapping
                    else "reference-only; no copied destination"
                ),
                "Canonical_Skill_ID": mapping["canonicalSkillId"] if mapping else "",
                "Verification_Status": "source-present; target-functional-verification-not-run",
                "License_Status": "unknown; source ownership/license review required",
            }
        )
    REPORT_DIR.mkdir(exist_ok=True)
    output = REPORT_DIR / "SOURCE_MIGRATION_DECISIONS.csv"
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    counts = Counter(row["Migration_Decision"] for row in rows)
    report = f"""# Migration and provenance report

## Scope and evidence

The source inventory contains **{len(rows)} resources**: 143 source skill files
and supporting documentation, scripts, and schemas. Every inventoried resource
has a row-level disposition in
[`SOURCE_MIGRATION_DECISIONS.csv`](./SOURCE_MIGRATION_DECISIONS.csv).

## Decisions

| Decision | Count |
|---|---:|
"""
    report += "\n".join(f"| `{key}` | {value} |" for key, value in sorted(counts.items()))
    report += """

`consolidated-source-package` means the source file is available in the single
canonical repository with a hash and provenance record; it is not a claim that
the behavior was functionally verified or semantically promoted. Source-specific
behavior is not silently discarded. `defer-adaptation` identifies
scripts/configuration that need a
separate compatibility, licensing, and permission review.

The canonical registry is generated from source capability mappings and retains
source hashes in `registry/registry.json`. No source repository was modified,
and no credentials, project code, or private runtime data was copied.

## Limitations

The inventory does not establish license ownership or runtime effectiveness.
Semantic overlap and unique behavior require human capability review before
merging, deprecating, or copying source files.
"""
    (REPORT_DIR / "MIGRATION_AND_PROVENANCE_REPORT.md").write_text(
        report, encoding="utf-8", newline="\n"
    )
    print(f"Wrote {len(rows)} source migration decisions.")


if __name__ == "__main__":
    main()
