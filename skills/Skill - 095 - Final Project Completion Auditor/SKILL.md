description: 'Execute the evidence-based candidate contract for Final Project Completion Auditor.'
---
id: final-project-completion-auditor
name: Skill - 095 - Final Project Completion Auditor
candidateIds: ["50"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: delivery
---

# Skill - 095 - Final Project Completion Auditor

## Purpose

This canonical instruction package implements the approved candidate contract for
**Final Project Completion Auditor**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Deliverables may be declared complete despite missing requirements/tests/handovers; perform evidence-based closure review.
- **Behavior; activation/non-activation:** Check completeness and report gaps; do not release or claim user acceptance.
- **Inputs/tools/dependencies/handoff:** Approved scope, traceability, test/security/build/docs/release, known issues; evidence links; depends 06/14/15/33-49; hands to 76/79/80.
- **Procedure/decision:** 1) Enumerate acceptance criteria and artifacts. 2) Verify evidence/current status. 3) Classify complete/failed/blocked/deferred/unverified. 4) Any mandatory unmet criterion prevents "complete"; request disposition from owner.
- **Outputs/acceptance/failure:** Closure report and handover checklist; pass means all scope has truthful disposition. Broken/missing evidence remains gap.
- **Security/example/maintenance:** Restrict security artifacts. Example: feature passes tests but release not approved â†’ implementation verified, project release incomplete. **Status:** partial-discovery/SDLC/docs checks; no final audit. Update at each closeout.

## Phase G - Automation and MCP

## Source mapping

- Candidate ID: `50`
- Source status at discovery: `partial-discovery/SDLC/docs checks; no final audit`
- Mapping evidence: `| 50 | Final Project Completion Auditor | indirect | Traceability row 50: project, planning, and docs audit concerns | `skills/Skill - 239 - SDLC Lifecycle Manager/SKILL.md`; `skills/Skill - 219 - Production Readiness Release Management/SKILL.md`; `docs/sdlc/STAGE_GATES.md` | Compose lifecycle, test, release, documentation, and handover criteria without claiming a unified auditor. |`
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

