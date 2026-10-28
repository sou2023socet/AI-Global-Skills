"""Deterministic, fail-closed registry selection for local orchestration."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "registry.json"


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def select(task: str, *, project_context: bool) -> list[dict[str, object]]:
    if not project_context:
        raise ValueError("project identity and context are required before selection")
    if not task.strip():
        raise ValueError("task intent must not be empty")
    registry = json.loads(REGISTRY.read_text(encoding="utf-8-sig"))
    task_tokens = _tokens(task)
    selected: dict[str, dict[str, object]] = {}
    for record in registry["skills"]:
        trigger_tokens = set().union(*(_tokens(trigger) for trigger in record["triggers"]))
        if trigger_tokens & task_tokens:
            selected[record["id"]] = record
    for record in list(selected.values()):
        for dependency in record["dependencies"]:
            dependency_id = dependency["skillId"]
            dependency_record = next(
                (item for item in registry["skills"] if item["id"] == dependency_id), None
            )
            if dependency_record is None:
                raise ValueError(f"unknown dependency: {dependency_id}")
            selected[dependency_id] = dependency_record
    ordered: list[dict[str, object]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(record: dict[str, object]) -> None:
        skill_id = str(record["id"])
        if skill_id in visiting:
            raise ValueError(f"dependency cycle detected at {skill_id}")
        if skill_id in visited:
            return
        visiting.add(skill_id)
        for dependency in record["dependencies"]:
            if dependency["skillId"] in selected:
                visit(selected[dependency["skillId"]])
        visiting.remove(skill_id)
        visited.add(skill_id)
        ordered.append(record)

    for record in sorted(selected.values(), key=lambda item: str(item["id"])):
        visit(record)
    return ordered


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task")
    parser.add_argument("--project-context", action="store_true")
    args = parser.parse_args()
    try:
        selected = select(args.task, project_context=args.project_context)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))
    print(json.dumps({"selectedSkills": [record["id"] for record in selected]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
