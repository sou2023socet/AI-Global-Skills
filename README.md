# Project Universal Global AI Skills

This repository is a reusable, evidence-first catalogue of AI-agent skills and
workflow contracts. It separates global instructions from project-specific
context and preserves the two source libraries as provenance-only inputs.

## What is implemented

- 124 active canonical skill packages under [`skills/`](./skills/), including
  80 candidate-linked capabilities and 41 source-promoted specializations.
- 143 source-preserving packages are included in the same numbered skill
  directory convention; their registry records identify them as provenance
  records rather than active duplicate capabilities.
- Machine-readable registry at [`registry/registry.json`](./registry/registry.json).
- Source package registry at [`registry/source-skills.json`](./registry/source-skills.json).
- Candidate crosswalk at [`registry/candidates.json`](./registry/candidates.json).
- Ordered canonical index at [`registry/canonical-index.json`](./registry/canonical-index.json).
- Dependency graph at [`registry/dependency-map.json`](./registry/dependency-map.json).
- JSON Schema contract at [`schemas/skill-registry.schema.json`](./schemas/skill-registry.schema.json).
- Deterministic lifecycle contract at
  [`workflows/lifecycle/workflow-contract.json`](./workflows/lifecycle/workflow-contract.json).
- Deterministic selector at
  [`orchestration/select_skills.py`](./orchestration/select_skills.py).
- Permission and project-isolation rules in
  [`shared/policies/permission-policy.md`](./shared/policies/permission-policy.md).
- Source inventory and provenance report in
  [`docs/migration/`](./docs/migration/).
- Standard-library structural validator at
  [`scripts/validate_registry.py`](./scripts/validate_registry.py).
- Reusable skill creation workflow at
  [`scripts/create_skill.py`](./scripts/create_skill.py), governed by
  [`AGENTS.md`](./AGENTS.md) and documented in
  [`docs/operations/SKILL_CREATION.md`](./docs/operations/SKILL_CREATION.md).

## Quick start

From the repository root:

```powershell
python scripts\validate_registry.py
python scripts\generate_status_matrix.py
python -m unittest discover -s tests -v
python orchestration\select_skills.py "project discovery" --project-context
```

Open the registry record and matching
`skills\Skill - NNN - Skill Purpose\SKILL.md` before using a skill. A registry
entry describes capability and evidence; it does not grant permission to
execute tools, access external systems, or change production.

Legacy packages are available in the same repository and retain source
provenance. They are marked `pending-capability-review` until their unique
behavior is merged into a canonical skill or promoted to a new canonical
package.

Use [`templates/project-workspace/project.yaml`](./templates/project-workspace/project.yaml)
to record project identity and freshness without copying project code or secrets.
See [`docs/operations/SETUP_AND_VALIDATION.md`](./docs/operations/SETUP_AND_VALIDATION.md)
for the operating boundary.

## Verification status

The generated packages are implemented as reusable instruction contracts, but
functional and platform verification is not claimed for source-promoted
packages. Structural validation must be run and recorded separately. See the
[final completion report](./reports/FINAL_COMPLETION_REPORT.md) and
[known limitations](./reports/KNOWN_LIMITATIONS_AND_NEXT_STEPS.md).

The verified release archive is
[`releases/project-universal-global-ai-skills.zip`](./releases/project-universal-global-ai-skills.zip).

## Provenance and source preservation

Discovery covered:

- `E:\sumit@data\project\Git\global-skills`
- `E:\sumit@data\project\Git\enterprise-ai-engineering-skills`

The target contains a copy of the source inventory for auditability. The source
repositories were not edited, renamed, deleted, or overwritten. See
[`docs/migration/MIGRATION_AND_PROVENANCE_REPORT.md`](./docs/migration/MIGRATION_AND_PROVENANCE_REPORT.md).

## Repository map

| Path | Responsibility |
|---|---|
| `skills/` | Candidate-linked reusable instruction packages |
| `registry/` | Machine-readable catalogue and candidate crosswalk |
| `workflows/` | Composable lifecycle contracts |
| `orchestration/` | Selection and failure-closed execution rules |
| `shared/` | Cross-skill policies and contracts |
| `scripts/` | Generation and structural validation |
| `docs/` | Architecture, operations, migration, and roadmap guidance |
| `reports/` | Evidence-backed status and limitations |

## Safety boundary

Read-only inspection is the default. Builds, tests, package installation,
application launches, external access, and artifact-producing checks require
explicit command-scoped approval from the host environment. Unknown project
identity, permission, or provenance is reported as a blocker rather than
silently inferred.
