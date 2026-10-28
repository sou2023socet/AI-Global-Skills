# Migration and Preservation Strategy

**Status:** Proposed and intentionally non-executing. Owner review is required before any source skill is copied, modified, merged, renamed, or deprecated.

## Source baseline

The prior discovery examined:

- `E:\sumit@data\project\Git\global-skills` — reported 28 `SKILL.md` files and an already dirty Git worktree.
- `E:\sumit@data\project\Git\enterprise-ai-engineering-skills` — reported 115 `SKILL.md` files; the path did not identify as a Git repository.

The combined count of 143 skills and 443 curated resources is an inventory snapshot, not proof of quality, completeness, current ownership, license compatibility, or runtime verification. Consult the source registry and duplicate/overlap report for exact paths/hashes and evidence limitations.

## Non-destructive rules

1. Treat both source roots as immutable inputs during proposal and pilot planning.
2. Never move, delete, rename, or overwrite source files. Do not repair source-library issues in this project.
3. Avoid writes into the pre-existing dirty global repository; this project is a sibling directory.
4. Do not activate source copies as duplicates. Build one reviewed canonical
   destination per source capability, merging overlaps and promoting genuinely
   distinct skills while retaining source references for provenance.
5. Before any approved copy, confirm destination does not exist, source hash is current, source ownership/license is known or explicitly unresolved, and the copy adds value beyond a link.
6. Keep platform-specific content in adapters or source variants until compatibility tests establish a safe common core.
7. Never copy secrets, project code, private runtime data, or sensitive logs into the global project.

## Migration record for each resource

Each migration record should include:

- Change ID, owner, approval date/scope, and review status.
- Source repository, exact relative/absolute source path, source hash, resource type, version, and license/ownership evidence or `unknown`.
- Candidate IDs and source coverage status.
- Overlap group and alternatives reviewed.
- Proposed target path and whether operation is reference-only, copy, adaptation, split, or deprecation.
- Transformation diff, preserved platform behavior, dependencies, and consumer impact.
- Static/scenario/platform verification evidence and known gaps.
- Rollback action and exact target resources that rollback is permitted to remove/restore.

## Decision workflow

1. Start with a traceable source reference, not a file copy.
2. Compare purpose, triggers, inputs/outputs, dependency graph, permissions, failure paths, and validation—not names alone.
3. Choose one disposition: keep source reference, reuse as-is after review, adapt, merge, split, defer, or deprecate.
4. Obtain owner approval for the specific resource and target, with an explicit preservation/rollback scope.
5. Apply the operation only inside this project and only after checking no destination conflict exists.
6. Validate the migrated result and update the registry, candidate crosswalk, version history, and migration record together.
7. Do not mark the source deprecated until consumer discovery and a compatibility period are complete and reviewed.

## Rollback

Rollback applies only to artifacts created by an approved migration in this new project. Preserve the migration record and source hashes. Do not run broad cleanup or reset operations. If a target is changed by another contributor or ownership is uncertain, stop and request review rather than overwrite or delete it.

## Initial dispositions

- Reuse existing discovery, requirements, architecture, security, testing, documentation, DevOps, MCP, and orchestration skills by provenance links first.
- Compare near-overlap groups before selecting canonical content; identical hashes are not assumed and semantic overlap does not authorize deletion.
- Treat project registry, evidence/status, approval, and audit as contracts before considering services.
- Consider only candidates 16 (problem analysis) and 17 (general research) as potential new standalone skills in the initial proposal; require validation design and owner approval before authoring.
- Keep knowledge ingestion, dashboards, queues, parallel execution, and persistent audit storage deferred until data/permission and operational requirements are accepted.

## Review gate

No source skill migration or consolidation starts until the owner approves this strategy, the registry contract, a specific pilot resource, and its verification/rollback plan.
