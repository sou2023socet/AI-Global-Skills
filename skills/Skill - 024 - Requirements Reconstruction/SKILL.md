description: 'Execute the evidence-based candidate contract for Requirements Reconstruction.'
---
id: requirements-reconstruction
name: Skill - 024 - Requirements Reconstruction
candidateIds: ["10"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: recovery
---

# Skill - 024 - Requirements Reconstruction

## Purpose

This canonical instruction package implements the approved candidate contract for
**Requirements Reconstruction**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Existing behavior and artifacts imply missing requirements; recover traceable functional/NFR candidates with fact/inference distinction.
- **Behavior; activation/non-activation:** Compare UI, API, schema, tests, docs, and runtime; do not invent stakeholder intent or silently convert inference to approved requirement.
- **Inputs/tools/dependencies/handoff:** Project context, artifacts, stakeholder notes, runtime evidence; source search and trace table; depends 04/08/09; hands candidates to 20 and validation links to 33.
- **Procedure/decision:** 1) Extract observable rules from each source. 2) Correlate duplicates/conflicts with source precedence. 3) Label observed/inferred/unknown and confidence. 4) Ask owner to resolve material conflicts before implementation.
- **Outputs/acceptance/failure:** Recovered requirements with source citations, assumptions, and questions; pass when each requirement is testable or explicitly unresolved. No stakeholder evidence means no approval claim.
- **Security/example/evidence/maintenance:** Exclude PII from recovered examples. Example: UI validates a required field, test confirms error, docs omit it; record fact and docs discrepancy. **Status:** partial-SDLC traceability only. Update when code or stakeholder evidence changes.

## Source mapping

- Candidate ID: `10`
- Source status at discovery: `partial-SDLC traceability only`
- Mapping evidence: `| 10 | Requirements Reconstruction | duplicate | Traceability row 10: SDLC planning/traceability skill | `skills/Skill - 232 - Requirements Engineering (Legacy Source Record)/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/requirements-and-user-journey-engineering/SKILL.md` | Separate requirements recovery from new requirements authoring; preserve inference provenance. |`
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

