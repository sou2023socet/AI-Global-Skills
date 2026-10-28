# Source candidate specification

- **Purpose/problem; goal/outcome:** Lessons/assets are duplicated or leak between projects; enable permission-aware reuse with provenance and isolation.
- **Behavior; activation/non-activation:** Search approved metadata/templates/patterns, classify reusable vs project-specific; do not export source/secrets by default.
- **Inputs/tools/dependencies/handoff:** Project identities, allowed knowledge sources, reuse goal, licenses; registry/index; depends 03/06/58/73/77; informs 18/19/28/53/68.
- **Procedure/decision:** 1) Verify source project and access. 2) Search metadata and approved reusable artifacts. 3) Check license, context assumptions and secret scan. 4) If transfer rights or sensitivity unclear, exclude and ask owner.
- **Outputs/acceptance/failure:** Reuse candidate report with provenance/constraints; pass when no unauthorized content crosses boundary. Failed access is not treated as no match.
- **Security/example/maintenance:** Enforce tenant/project isolation and consent. Example: share a generic test checklist, not a project’s private API schema. **Status:** partial—principle in global system skill only. Revalidate permissions on each reuse.

## Phase H — Maintenance and continuous improvement
