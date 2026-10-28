description: 'Execute the evidence-based candidate contract for Architecture & Design Implementation.'
---
id: architecture-and-design-implementation
name: Skill - 038 - Architecture & Design Implementation
candidateIds: ["26"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: development
---

# Skill - 038 - Architecture & Design Implementation

## Purpose

This canonical instruction package implements the approved candidate contract for
**Architecture & Design Implementation**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Approved architecture is not consistently reflected in implementation; translate decisions into module boundaries and contracts.
- **Behavior; activation/non-activation:** Preserve approved ADR/contracts and detect design gaps; do not redesign without review or treat proposal as approved.
- **Inputs/tools/dependencies/handoff:** Approved diagrams/ADRs, requirements, coding standards, environment; code search and native build/test tools; depends 11/19/20/22/24/25; hands to 27-33.
- **Procedure/decision:** 1) Map design elements to modules/interfaces. 2) Identify existing reusable components and violations. 3) Plan incremental changes with compatibility tests. 4) If code reality conflicts with approved design, stop for decision before structural rewrite.
- **Outputs/acceptance/failure:** Implementation map, bounded code changes, updated diagrams; pass when tests/contracts show intended boundaries. Preserve baseline if build fails.
- **Security/example/evidence/maintenance:** Approval for data/interface breaking changes. Example: add service interface behind approved bounded context; integration tests verify contract. **Status:** partial as workflow across architecture/backend/frontend skills, no generic trace loop. Maintain ADR links.

## Source mapping

- Candidate ID: `26`
- Source status at discovery: `partial as workflow across architecture/backend/frontend skills, no generic trace loop`
- Mapping evidence: `| 26 | Architecture & Design Implementation | indirect | Traceability row 26: architecture plus frontend/backend skills | `skills/Skill - 136 - Architecture Design/SKILL.md`; `skills/Skill - 190 - Frontend Engineering (Legacy Source Record)/SKILL.md`; `skills/Skill - 140 - Backend Engineering (Legacy Source Record)/SKILL.md` | Compose approved-design traceability with implementation/review/test handoffs; no generic workflow is established. |`
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

