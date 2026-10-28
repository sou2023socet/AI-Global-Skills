description: 'Execute the evidence-based candidate contract for Requirements-to-Test Traceability.'
---
id: requirements-to-test-traceability
name: Skill - 079 - Requirements-to-Test Traceability
candidateIds: ["33"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: quality
---

# Skill - 079 - Requirements-to-Test Traceability

## Purpose

This canonical instruction package implements the approved candidate contract for
**Requirements-to-Test Traceability**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Requirements are mistaken for covered without tests; create bidirectional links from acceptance criteria to cases and results.
- **Behavior; activation/non-activation:** Maintain IDs/status and reveal gaps; do not equate line coverage with requirement verification.
- **Inputs/tools/dependencies/handoff:** Approved requirements, test inventory/results; spreadsheet/Markdown/test manager; depends 06/20/28-31; hands gaps to 34/35 and readiness to 42.
- **Procedure/decision:** 1) Assign stable IDs to criteria. 2) Link one or more tests and evidence. 3) Mark verified/failed/blocked/missing with run context. 4) If a criterion lacks an observable test, report uncovered rather than infer pass.
- **Outputs/acceptance/failure:** RTM with requirementâ†”testâ†”result; pass when every in-scope criterion has disposition. Preserve historical run results.
- **Security/example/maintenance:** Keep test data synthetic; redact reports. Example: role restriction maps to unauthorized and authorized cases with separate evidence. **Status:** partial-SDLC/QA mention traceability, no maintained mapping/test integration. Update with requirement changes.

## Source mapping

- Candidate ID: `33`
- Source status at discovery: `partial-SDLC/QA mention traceability, no maintained mapping/test integration`
- Mapping evidence: `| 33 | Requirements-to-Test Traceability | partial | Traceability row 33: SDLC and QA skills | `skills/Skill - 226 - Project Planning Traceability/SKILL.md`; `docs/sdlc/REQUIREMENTS_TRACEABILITY.md`; `templates/sdlc/LIFECYCLE_AND_TRACEABILITY_TEMPLATE.md` | Define bidirectional requirement/test/result IDs and freshness/update rules. |`
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

