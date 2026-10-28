"""Generate the canonical candidate catalogue from the approved source catalogue.

The source repositories are inputs only. This generator creates target-owned
metadata and instruction packages; it never edits either source repository.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
from pathlib import Path


TARGET = Path(__file__).resolve().parents[1]
GLOBAL_ROOT = Path(r"E:\sumit@data\project\Git\global-skills")
ENTERPRISE_ROOT = Path(r"E:\sumit@data\project\Git\enterprise-ai-engineering-skills")
CATALOGUE = GLOBAL_ROOT / "SKILL_CANDIDATE_CATALOGUE.md"
MAPPING = GLOBAL_ROOT / "SKILL_TO_80_CANDIDATE_MAPPING.md"
SOURCE_REGISTRY = GLOBAL_ROOT / "SKILL_SOURCE_REGISTRY.csv"


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def read_candidates() -> list[dict[str, object]]:
    lines = CATALOGUE.read_text(encoding="utf-8").splitlines()
    candidates: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    body: list[str] = []
    heading = re.compile(r"^###\s+(\d{2})\.\s+(.+?)\s*$")
    for line in lines:
        match = heading.match(line)
        if match:
            if current is not None:
                current["specification"] = "\n".join(body).strip()
                candidates.append(current)
            current = {
                "id": match.group(1),
                "name": match.group(2).strip(),
                "skillId": slugify(match.group(2)),
            }
            body = []
        elif current is not None:
            body.append(line)
    if current is not None:
        current["specification"] = "\n".join(body).strip()
        candidates.append(current)
    if len(candidates) != 80 or [c["id"] for c in candidates] != [
        f"{number:02d}" for number in range(1, 81)
    ]:
        raise ValueError("The source catalogue did not contain exactly candidates 01-80")
    return candidates


def mapping_evidence(candidate_id: str) -> str:
    lines = MAPPING.read_text(encoding="utf-8").splitlines()
    prefix = f"| {int(candidate_id):02d} |"
    for line in lines:
        if line.startswith(prefix):
            return line
    return "No mapping row found; treat source coverage as unknown."


def lifecycle(candidate_id: int) -> str:
    if candidate_id <= 6:
        return "foundation"
    if candidate_id <= 15:
        return "recovery"
    if candidate_id <= 24:
        return "research-planning"
    if candidate_id <= 32:
        return "development"
    if candidate_id <= 42:
        return "quality"
    if candidate_id <= 50:
        return "delivery"
    if candidate_id <= 60:
        return "automation"
    if candidate_id <= 70:
        return "maintenance"
    if candidate_id <= 77:
        return "project-knowledge"
    return "roadmap-release"


def write_skill(candidate: dict[str, object]) -> None:
    skill_dir = TARGET / "skills" / str(candidate["skillId"])
    skill_dir.mkdir(parents=True, exist_ok=True)
    specification = str(candidate["specification"])
    status_match = re.search(r"\*\*Status:\*\*\s*([^.\n]+)", specification)
    source_status = status_match.group(1).strip() if status_match else "candidate specification"
    content = f"""---
id: {candidate["skillId"]}
name: {candidate["name"]}
candidateIds: ["{candidate["id"]}"]
version: 0.1.0
status: implemented
verification: structurally-unvalidated
lifecycleGroup: {lifecycle(int(str(candidate["id"])))}
---

# {candidate["name"]}

## Purpose

This canonical instruction package implements the approved candidate contract for
**{candidate["name"]}**. It is reusable guidance, not an autonomous runtime or
permission grant.

## Activation

Use this skill when the task intent matches the candidate purpose and the project
context has been identified. Do not activate it for unrelated work or to bypass
project-specific policies, approvals, or security controls.

## Required procedure

1. Establish the project and task scope from current, evidence-linked inputs.
2. Apply the candidate procedure below, preserving unknowns instead of guessing.
3. Record decisions, inputs, outputs, assumptions, and failures in the project
   evidence location.
4. Validate acceptance criteria with the least-invasive available evidence.
5. Hand off only the declared outputs and unresolved questions.

## Candidate contract

{specification}

## Source mapping

- Candidate ID: `{candidate["id"]}`
- Source status at discovery: `{source_status}`
- Mapping evidence: `{mapping_evidence(str(candidate["id"]))}`
- Canonical source of truth: `registry/registry.json`

## Safety and failure handling

- Read-only discovery is the default.
- Never copy credentials, private project data, or secrets into this package.
- Do not claim functional verification from the presence of this file.
- Stop and report an explicit blocker when identity, permissions, required inputs,
  or acceptance evidence are missing.
- Make changes only after the applicable project and tool approval rules allow
  them, and preserve a rollback reference for consequential changes.

## Acceptance criteria

- Inputs and project scope are identified and provenance is recorded.
- The outputs named by the candidate contract are present or explicitly blocked.
- Unknowns, skipped checks, and unavailable external dependencies are reported.
- No stronger verification status is recorded without matching evidence.
"""
    (skill_dir / "SKILL.md").write_text(content, encoding="utf-8", newline="\n")
    (skill_dir / "references").mkdir(exist_ok=True)
    (skill_dir / "references" / "candidate-spec.md").write_text(
        f"# Source candidate specification\n\n{specification}\n",
        encoding="utf-8",
        newline="\n",
    )


def registry_record(candidate: dict[str, object]) -> dict[str, object]:
    cid = int(str(candidate["id"]))
    skill_id = str(candidate["skillId"])
    return {
        "id": skill_id,
        "name": candidate["name"],
        "version": "0.1.0",
        "contractVersion": "1.0",
        "status": "implemented",
        "verification": {
            "structural": "pending",
            "functional": "not-run",
            "platform": "not-run",
        },
        "implementationKind": "skill",
        "lifecycleGroup": lifecycle(cid),
        "purpose": f"Execute the evidence-based candidate contract for {candidate['name']}.",
        "triggers": [f"task explicitly requires {str(candidate['name']).lower()}"],
        "nonTriggers": ["unrelated work", "missing project identity", "permission bypass"],
        "provenance": [
            {
                "repository": "global-skills",
                "path": "SKILL_CANDIDATE_CATALOGUE.md",
                "sha256": hashlib.sha256(CATALOGUE.read_bytes()).hexdigest(),
                "reviewStatus": "reviewed",
            },
            {
                "repository": "global-skills",
                "path": "SKILL_TO_80_CANDIDATE_MAPPING.md",
                "sha256": hashlib.sha256(MAPPING.read_bytes()).hexdigest(),
                "reviewStatus": "reviewed",
            },
        ],
        "dependencies": [],
        "inputs": [
            {
                "name": "projectContext",
                "description": "Current project identity, scope, constraints, and evidence.",
                "required": True,
                "sensitivity": "internal",
                "freshnessRequired": True,
            }
        ],
        "outputs": [
            {
                "name": "evidenceRecord",
                "description": "Candidate-specific outputs, decisions, limitations, and acceptance evidence.",
                "required": True,
                "sensitivity": "internal",
            }
        ],
        "tools": [
            {
                "name": "filesystem-and-documentation-inspection",
                "permission": "read-only",
                "requiresApproval": False,
                "sideEffects": "none",
            }
        ],
        "validationCriteria": [
            {"criterion": "SKILL.md has required metadata and sections", "evidenceType": "static"},
            {"criterion": "Candidate outputs and blockers are recorded", "evidenceType": "manual-review"},
        ],
        "candidateIds": [str(candidate["id"])],
        "sourceMapping": mapping_evidence(str(candidate["id"])),
    }


def main() -> None:
    candidates = read_candidates()
    (TARGET / "skills").mkdir(exist_ok=True)
    for candidate in candidates:
        write_skill(candidate)
    registry = {
        "registryVersion": "1.0",
        "generatedFrom": {
            "catalogue": str(CATALOGUE),
            "mapping": str(MAPPING),
        },
        "skills": [registry_record(candidate) for candidate in candidates],
    }
    registry_dir = TARGET / "registry"
    registry_dir.mkdir(exist_ok=True)
    (registry_dir / "registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    if SOURCE_REGISTRY.exists():
        migration_dir = TARGET / "docs" / "migration"
        migration_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SOURCE_REGISTRY, migration_dir / "SOURCE_INVENTORY.csv")
    (TARGET / "registry" / "candidates.json").write_text(
        json.dumps(
            [
                {
                    "id": candidate["id"],
                    "name": candidate["name"],
                    "skillId": candidate["skillId"],
                    "status": "mapped",
                    "canonicalPath": f"skills/{candidate['skillId']}/SKILL.md",
                    "sourceMapping": mapping_evidence(str(candidate["id"])),
                }
                for candidate in candidates
            ],
            indent=2,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Generated {len(candidates)} candidate packages and registry records.")


if __name__ == "__main__":
    main()
