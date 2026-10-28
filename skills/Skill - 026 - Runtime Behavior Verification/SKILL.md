description: 'Execute the evidence-based candidate contract for Runtime Behavior Verification.'
---
id: runtime-behavior-verification
name: Skill - 026 - Runtime Behavior Verification
candidateIds: ["09"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: recovery
---

# Skill - 026 - Runtime Behavior Verification

## Purpose

This canonical instruction package implements the approved candidate contract for
**Runtime Behavior Verification**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Source text does not prove actual behavior; safely compare expected/documented behavior with observed execution.
- **Behavior; activation/non-activation:** Execute only bounded, authorized scenarios; do not claim runtime verification from static inspection.
- **Inputs/tools/dependencies/handoff:** Expected behavior, target/environment identity, inputs, side-effect scope; native test runner/browser/API/log tools; depends 04/06; hands discrepancies to 14/29/33-42.
- **Procedure/decision:** 1) Confirm target, environment, and side effects. 2) Select smallest discriminating scenario and baseline. 3) Run and capture output/evidence. 4) If target safety or expected result is unclear, stop as BLOCKED rather than probing broadly.
- **Outputs/acceptance/failure:** Case-level expected/actual/status and environment; pass only on observed assertion success. Infrastructure/tool failure is BLOCKED/FAILED, not product pass.
- **Security/example/evidence/maintenance:** Synthetic data and redaction; production activity requires explicit scope. Example: documented `/health` is called on approved local service and HTTP result recorded. **Status:** partial-focused, functional, automation test instructions; no unified runtime protocol or skill tests. Preserve runner/version for replay.

## Source mapping

- Candidate ID: `09`
- Source status at discovery: `partial-focused, functional, automation test instructions; no unified runtime protocol or skill tests`
- Mapping evidence: `| 09 | Runtime Behavior Verification | duplicate | Traceability row 09: focused, functional, and automation testing skills | `skills/Skill - 132 - API Database Integration Testing/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/backend-integration-and-api-testing/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/frontend-testing-and-visual-regression/SKILL.md` | Define one expected-vs-observed evidence record and boundaries across API/UI/runtime tests. |`
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

