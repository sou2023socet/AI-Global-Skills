description: 'Execute the evidence-based candidate contract for Roadmap & Future Feature Manager.'
---
id: roadmap-and-future-feature-manager
name: Skill - 103 - Roadmap & Future Feature Manager
candidateIds: ["78"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: roadmap-release
---

# Skill - 103 - Roadmap & Future Feature Manager

## Purpose

This canonical instruction package implements the approved candidate contract for
**Roadmap & Future Feature Manager**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Ideas and commitments are mixed; maintain approved goals, proposals, deferred work, debt and future options as distinct states.
- **Behavior; activation/non-activation:** Classify and prioritize roadmap items with rationale; do not imply approval or schedule unapproved ideas.
- **Inputs/tools/dependencies/handoff:** Stakeholder goals, backlog, risks, dependencies, capacity; roadmap/index; depends 20/22-23/62/68-70; hands approved items to 22 and release/status to 79-80.
- **Procedure/decision:** 1) Deduplicate and label idea/proposed/approved/deferred/cancelled. 2) Link evidence, owner, dependencies and outcome. 3) Prioritize only using agreed criteria. 4) If owner/capacity/approval missing, keep uncommitted.
- **Outputs/acceptance/failure:** Roadmap with rationale, states and review dates; pass when no proposal is represented as commitment. Unknown dates remain unset.
- **Security/example/maintenance:** Restrict commercial/roadmap data appropriately. Example: "mobile app" stays proposed until scope and owner approval. **Status:** partial-SDLC roadmap exists, commitment state model incomplete. Reassess quarterly/at decision points.

## Source mapping

- Candidate ID: `78`
- Source status at discovery: `partial-SDLC roadmap exists, commitment state model incomplete`
- Mapping evidence: `| 78 | Roadmap & Future Feature Manager | partial | Traceability row 78: SDLC roadmap guidance | `skills/Skill - 226 - Project Planning Traceability/SKILL.md`; `skills/Skill - 201 - Implementation Planner/SKILL.md` | Distinguish ideas/proposals/approved commitments and record deferral reasons. |`
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

