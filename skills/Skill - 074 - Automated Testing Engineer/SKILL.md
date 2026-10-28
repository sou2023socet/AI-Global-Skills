description: 'Execute the evidence-based candidate contract for Automated Testing Engineer.'
---
id: automated-testing-engineer
name: Skill - 074 - Automated Testing Engineer
candidateIds: ["35"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: quality
---

# Skill - 074 - Automated Testing Engineer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Automated Testing Engineer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Manual checks are not repeatable; create or maintain reliable automated verification and authentic evidence.
- **Behavior; activation/non-activation:** Use native runners and stable fixtures; not only manual UAT or a one-off unit test.
- **Inputs/tools/dependencies/handoff:** Scenarios, test framework/config, safe environment/data; browser/API/device/native runner; depends 25/31/33/34; results to 40-42.
- **Procedure/decision:** 1) Inspect current runner and fixture lifecycle. 2) Implement assertions that prove user outcome. 3) Run bounded suite and capture diagnostics. 4) If flaky/external dependency fails, isolate/classify; do not rerun repeatedly to manufacture a pass.
- **Outputs/acceptance/failure:** Reusable tests, command/results, artifacts, cleanup record; pass when deterministic outcomes and no leaked test data/processes. Failed runner remains failure.
- **Security/example/maintenance:** No production credentials or external side effects. Example: automated login-to-calculation workflow asserts response and visible result. **Status:** partial-new automation/unit skills are instruction-only; no test artifacts. Keep suite versioned.

## Source mapping

- Candidate ID: `35`
- Source status at discovery: `partial-new automation/unit skills are instruction-only; no test artifacts`
- Mapping evidence: `| 35 | Automated Testing Engineer | duplicate | Traceability row 35: automation, unit, and QA skills | `skills/Skill - 254 - Test Automation Engineering/SKILL.md`; `skills/Skill - 132 - API Database Integration Testing/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/frontend-testing-and-visual-regression/SKILL.md` | Consolidate boundaries and safe fixture/cleanup policy; no runtime test suite was executed. |`
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

