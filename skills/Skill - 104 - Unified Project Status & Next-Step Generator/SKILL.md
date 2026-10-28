description: 'Execute the evidence-based candidate contract for Unified Project Status & Next-Step Generator.'
---
id: unified-project-status-and-next-step-generator
name: Skill - 104 - Unified Project Status & Next-Step Generator
candidateIds: ["80"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: roadmap-release
---

# Skill - 104 - Unified Project Status & Next-Step Generator

## Purpose

This canonical instruction package implements the approved candidate contract for
**Unified Project Status & Next-Step Generator**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Status updates scatter progress/blockers/decisions; generate a concise, evidence-backed current view and safe next action.
- **Behavior; activation/non-activation:** Reconcile canonical records and freshness; do not infer progress from unverified prose or choose an approval-gated action.
- **Inputs/tools/dependencies/handoff:** Registry, evidence, tasks, roadmap, risks, releases, handover; approved project records; depends 03/05-06/22/58/61-79; hands to 76/user.
- **Procedure/decision:** 1) Load current status sources and timestamps. 2) Reconcile completed/active/blocked/deferred/unknown. 3) Rank next actions by prerequisite, risk and approval. 4) If records conflict or are stale, show conflict and recommend verification first.
- **Outputs/acceptance/failure:** Status summary with evidence links, blockers, decisions, next actions and as-of date; pass when no stale claim is called current. Missing source is disclosed.
- **Security/example/maintenance:** Restrict private project data and redact secrets. Example: build passed but integration tests blocked; next action is resolve test environment, not announce completion. **Status:** partial-global-stage report and SDLC plan; no unified status generator. Refresh on meaningful state changes.

## Completion summary

All **80/80 candidate specifications** are populated against the reusable standard. This is specification completeness only. Implementation/verification dispositions remain as shown in the traceability matrix; no candidate is marked fully covered or released by this catalogue.

## Source mapping

- Candidate ID: `80`
- Source status at discovery: `partial-global-stage report and SDLC plan; no unified status generator`
- Mapping evidence: `| 80 | Unified Project Status & Next-Step Generator | partial | Traceability row 80: global-system and SDLC status guidance | `skills/Skill - 178 - Engineering Orchestrator Continuous Improvement/SKILL.md`; `orchestration/MASTER_ORCHESTRATOR.md`; `orchestration/WORKFLOW_PATTERNS.md` | Define freshness-aware status assembled from canonical evidence and explicit next-action derivation. |`
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

