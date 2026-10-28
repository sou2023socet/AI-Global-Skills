# Source candidate specification

- **Purpose/problem; goal/outcome:** Status updates scatter progress/blockers/decisions; generate a concise, evidence-backed current view and safe next action.
- **Behavior; activation/non-activation:** Reconcile canonical records and freshness; do not infer progress from unverified prose or choose an approval-gated action.
- **Inputs/tools/dependencies/handoff:** Registry, evidence, tasks, roadmap, risks, releases, handover; approved project records; depends 03/05–06/22/58/61–79; hands to 76/user.
- **Procedure/decision:** 1) Load current status sources and timestamps. 2) Reconcile completed/active/blocked/deferred/unknown. 3) Rank next actions by prerequisite, risk and approval. 4) If records conflict or are stale, show conflict and recommend verification first.
- **Outputs/acceptance/failure:** Status summary with evidence links, blockers, decisions, next actions and as-of date; pass when no stale claim is called current. Missing source is disclosed.
- **Security/example/maintenance:** Restrict private project data and redact secrets. Example: build passed but integration tests blocked; next action is resolve test environment, not announce completion. **Status:** partial—global-stage report and SDLC plan; no unified status generator. Refresh on meaningful state changes.

## Completion summary

All **80/80 candidate specifications** are populated against the reusable standard. This is specification completeness only. Implementation/verification dispositions remain as shown in the traceability matrix; no candidate is marked fully covered or released by this catalogue.
