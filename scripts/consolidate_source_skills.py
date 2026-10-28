"""Copy every source SKILL.md into the single canonical repository.

The copied packages remain source-preserving legacy packages until a capability
review promotes or merges them into a canonical candidate. Source repositories
are read-only inputs and are never modified.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path


TARGET = Path(__file__).resolve().parents[1]
SOURCE_ROOTS = {
    "global-skills": Path(r"E:\sumit@data\project\Git\global-skills"),
    "enterprise-ai-engineering-skills": Path(
        r"E:\sumit@data\project\Git\enterprise-ai-engineering-skills"
    ),
}
DESTINATION = TARGET / "skills"
OUTPUT = TARGET / "registry" / "source-skills.json"


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def package_id(repository: str, source_path: Path, used: set[str]) -> str:
    base = f"legacy-{slugify(repository)}-{slugify(source_path.parent.name)}"
    candidate = base
    suffix = 2
    while candidate in used:
        candidate = f"{base}-{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def main() -> None:
    records: list[dict[str, object]] = []
    used: set[str] = set()
    for repository, root in SOURCE_ROOTS.items():
        if not root.is_dir():
            raise FileNotFoundError(f"source repository is missing: {root}")
        for source_file in sorted(root.rglob("SKILL.md")):
            relative = source_file.relative_to(root)
            skill_id = package_id(repository, source_file, used)
            destination = DESTINATION / skill_id
            destination.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source_file, destination / "SKILL.md")
            digest = hashlib.sha256(source_file.read_bytes()).hexdigest()
            (destination / "source-provenance.json").write_text(
                json.dumps(
                    {
                        "repository": repository,
                        "sourcePath": str(relative),
                        "sha256": digest,
                        "disposition": "consolidated-source-package",
                        "promotionStatus": "pending-capability-review",
                    },
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            records.append(
                {
                    "id": skill_id,
                    "name": source_file.parent.name,
                    "repository": repository,
                    "sourcePath": str(relative),
                    "canonicalPath": f"skills/{skill_id}/SKILL.md",
                    "sha256": digest,
                    "disposition": "consolidated-source-package",
                    "promotionStatus": "pending-capability-review",
                }
            )
    OUTPUT.write_text(
        json.dumps(
            {
                "version": "1.0",
                "description": (
                    "All source SKILL.md files copied into the canonical repository. "
                    "These packages remain source-preserving until capability review."
                ),
                "sourceRepositories": list(SOURCE_ROOTS),
                "skills": records,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Consolidated {len(records)} source skill packages into {DESTINATION}")


if __name__ == "__main__":
    main()
