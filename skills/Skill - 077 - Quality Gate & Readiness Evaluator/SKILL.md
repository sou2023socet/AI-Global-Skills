description: 'Execute the evidence-based candidate contract for Quality Gate & Readiness Evaluator.'
---
id: quality-gate-and-readiness-evaluator
name: Skill - 077 - Quality Gate & Readiness Evaluator
candidateIds: ["42"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: quality
---

# Skill - 077 - Quality Gate & Readiness Evaluator

## Purpose

This canonical instruction package implements the approved candidate contract for
**Quality Gate & Readiness Evaluator**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Release decisions use incomplete or inconsistent evidence; provide ready/conditional/not-ready evaluation against agreed criteria.
- **Behavior; activation/non-activation:** Aggregate requirements/tests/security/docs/build/release evidence; do not waive criteria or release on behalf of owner.
- **Inputs/tools/dependencies/handoff:** Approved gates, status/evidence records, risks, release target; links to reports and CI results; depends 06/15/33-41/43; hands to 47-50.
- **Procedure/decision:** 1) Load gate criteria and evidence freshness. 2) Mark each pass/fail/blocked/missing/N/A. 3) Evaluate critical blockers and accepted risks. 4) Missing mandatory evidence means not-ready; conditional status requires named owner/expiry.
- **Outputs/acceptance/failure:** Gate report and recommendation; pass means all criterion results reconciled, not necessarily ready. Conflicting records are escalated.
- **Security/example/maintenance:** Private security findings remain access-controlled. Example: tests pass but migration rollback unverified â†’ not ready for deployment. **Status:** partial-SDLC, security, deployment gates exist separately. Version thresholds with approved release policy.

## Phase F - Documentation and delivery

## Source mapping

- Candidate ID: `42`
- Source status at discovery: `partial-SDLC, security, deployment gates exist separately`
- Mapping evidence: `| 42 | Quality Gate & Readiness Evaluator | duplicate | Traceability row 42: SDLC, deployment, appsec skills | `skills/Skill - 151 - Code Review Quality Gate/SKILL.md`; `skills/Skill - 256 - Test Strategy Management/SKILL.md`; `skills/Skill - 219 - Production Readiness Release Management/SKILL.md`; `skills/Skill - 145 - Build and Test Approval Gate/SKILL.md` | Compose required evidence without conflating readiness assessment and release authority. |`
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

