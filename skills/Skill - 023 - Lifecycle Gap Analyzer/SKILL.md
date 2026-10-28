description: 'Execute the evidence-based candidate contract for Lifecycle Gap Analyzer.'
---
id: lifecycle-gap-analyzer
name: Skill - 023 - Lifecycle Gap Analyzer
candidateIds: ["15"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: recovery
---

# Skill - 023 - Lifecycle Gap Analyzer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Lifecycle Gap Analyzer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** A project may omit requirements, QA, security, release, or maintenance controls; identify evidence-backed lifecycle gaps and prioritized actions.
- **Behavior; activation/non-activation:** Assess applicability per project and phase; do not use a generic checklist to claim compliance or maturity.
- **Inputs/tools/dependencies/handoff:** Project phase, requirements, delivery artifacts, policy, evidence; repository docs and traceability matrices; depends 06/14; hands to 22/23/34/42/50/69.
- **Procedure/decision:** 1) Map lifecycle activities to project risk. 2) Mark evidence present/missing/not-applicable with rationale. 3) Rank gaps by impact and dependency. 4) Ask owner before turning recommendations into commitments.
- **Outputs/acceptance/failure:** Gap matrix and action candidates; pass when each "missing" has a checked source scope and each N/A rationale. Incomplete evidence blocks readiness conclusion.
- **Security/example/evidence/maintenance:** Identify security/data-release gaps without exposing findings publicly. Example: no verified rollback doc â†’ release gap, not deployment failure. **Status:** partial-SDLC gates guide planning, no analyzer. Update with lifecycle policy.

## Phase C - Research, requirements, and planning

## Source mapping

- Candidate ID: `15`
- Source status at discovery: `partial-SDLC gates guide planning, no analyzer`
- Mapping evidence: `| 15 | Lifecycle Gap Analyzer | duplicate | Traceability row 15: SDLC planning/governance | `skills/Skill - 239 - SDLC Lifecycle Manager/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/sdlc-and-design-gate-manager/SKILL.md`; `docs/sdlc/STAGE_GATES.md` | Reconcile lifecycle and gate checklists; define evidence-based completeness criteria. |`
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

