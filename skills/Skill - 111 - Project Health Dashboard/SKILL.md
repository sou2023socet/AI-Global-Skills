description: 'Execute the evidence-based candidate contract for Project Health Dashboard.'
---
id: project-health-dashboard
name: Skill - 111 - Project Health Dashboard
candidateIds: ["61"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: maintenance
---

# Skill - 111 - Project Health Dashboard

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Health Dashboard**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Status is fragmented or stale; summarize progress, blockers, risk, quality, and release state with source freshness.
- **Behavior; activation/non-activation:** Aggregate verified metrics and missing data; do not estimate project health from file count or stale status text.
- **Inputs/tools/dependencies/handoff:** Registry, evidence/status, test/release/risk data and timestamps; report/dashboard renderer; depends 03/06/58/72-75/79-80; informs 62/69/70.
- **Procedure/decision:** 1) Load allowed sources and freshness thresholds. 2) Reconcile conflicting states. 3) Show metric source and missingness. 4) If critical source stale/unavailable, mark dashboard partial and do not score as healthy.
- **Outputs/acceptance/failure:** Timestamped status view and source links; pass when each metric has definition/source/freshness. Aggregation failure visible.
- **Security/example/maintenance:** Role-based access; no sensitive details in broad dashboards. Example: tests green last month â†’ stale, not current green. **Status:** proposed new capability; no dashboard service. Review metric definitions.

## Source mapping

- Candidate ID: `61`
- Source status at discovery: `proposed new capability; no dashboard service`
- Mapping evidence: `| 61 | Project Health Dashboard | missing | Traceability row 61: no dashboard/report capability found | `skills/Skill - 212 - Observability Monitoring Alerting/SKILL.md` is adjacent only | Define freshness-aware project metrics and source adapters before creating a dashboard capability. |`
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

