description: 'Execute the evidence-based candidate contract for Test Failure & Root-Cause Analyzer.'
---
id: test-failure-and-root-cause-analyzer
name: Skill - 081 - Test Failure & Root-Cause Analyzer
candidateIds: ["41"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: quality
---

# Skill - 081 - Test Failure & Root-Cause Analyzer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Test Failure & Root-Cause Analyzer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Failing tests are misattributed to code when caused by fixtures, environment, or flakiness; classify failure with evidence and safe recovery.
- **Behavior; activation/non-activation:** Analyze runner output and reproduction; do not rerun costly/destructive tests without approval.
- **Inputs/tools/dependencies/handoff:** Failure output, test/commit, environment, baseline; logs, runner, targeted reproduction; depends 06/35/40; hands code defects to 29, strategy issues to 34.
- **Procedure/decision:** 1) Preserve first failure/output. 2) Classify assertion/product, test, environment, dependency, flaky, unknown. 3) Compare baseline and isolate minimum case. 4) If rerun changes side effects/cost, ask; otherwise one bounded diagnostic rerun may be proposed.
- **Outputs/acceptance/failure:** Root-cause report with confidence and next action; pass when classification evidence and unresolved alternatives are explicit. Unknown remains unknown.
- **Security/example/maintenance:** Redact test data/secrets. Example: connection refused plus healthy unit tests maps to environment failure, not code fix. **Status:** partial-general diagnostic skill only. Track recurrent failure pattern.

## Source mapping

- Candidate ID: `41`
- Source status at discovery: `partial-general diagnostic skill only`
- Mapping evidence: `| 41 | Test Failure & Root-Cause Analyzer | duplicate | Traceability row 41: diagnostic and QA skills | `skills/Skill - 205 - Logging Error Diagnostics/SKILL.md`; `skills/Skill - 202 - Incident Response Root Cause/SKILL.md` | Add test-specific flaky/environment/product classification and one-run/approval limits. |`
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

