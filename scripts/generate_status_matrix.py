"""Generate the candidate status matrix from the canonical registry."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "registry.json"
OUTPUT = ROOT / "reports" / "SKILL_STATUS_MATRIX.csv"


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8-sig"))
    rows: list[dict[str, str]] = []
    for record in registry["skills"]:
        verification = record["verification"]
        candidate_ids = record["candidateIds"] or [""]
        for candidate_id in candidate_ids:
            rows.append(
                {
                    "CandidateId": candidate_id,
                    "SkillId": record["id"],
                    "Name": record["name"],
                    "LifecycleGroup": record["lifecycleGroup"],
                    "ExecutionOrder": str(record["executionOrder"]),
                    "Status": record["status"],
                    "StructuralVerification": verification["structural"],
                    "FunctionalVerification": verification["functional"],
                    "PlatformVerification": verification["platform"],
                    "CanonicalPath": record["path"].replace("/", "\\"),
                    "ImplementationKind": record["implementationKind"],
                }
            )
    rows.sort(key=lambda row: (int(row["ExecutionOrder"]), row["SkillId"]))
    OUTPUT.parent.mkdir(exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} canonical status rows to {OUTPUT}")


if __name__ == "__main__":
    main()
