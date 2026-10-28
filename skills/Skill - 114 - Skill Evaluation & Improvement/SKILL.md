description: 'Execute the evidence-based candidate contract for Skill Evaluation & Improvement.'
---
id: skill-evaluation-and-improvement
name: Skill - 114 - Skill Evaluation & Improvement
candidateIds: ["66"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: maintenance
---

# Skill - 114 - Skill Evaluation & Improvement

## Purpose

This canonical instruction package implements the approved candidate contract for
**Skill Evaluation & Improvement**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Skill quality is assumed from metadata; evaluate correctness, usefulness, reliability, cost and failures on controlled scenarios.
- **Behavior; activation/non-activation:** Maintain versioned fixtures and compare outcomes; do not use automated judge as sole release authority.
- **Inputs/tools/dependencies/handoff:** Skill versions, trigger/output contracts, representative and adversarial cases; validator, test harness, human review; depends 01/06/33-42/53/58; feedback to skill owner.
- **Procedure/decision:** 1) Separate static schema checks from behavior tests. 2) Execute safe scenarios including negative/ambiguous inputs. 3) Score required outputs, safety and regressions. 4) Failure blocks "verified"; propose targeted change and rerun same baseline.
- **Outputs/acceptance/failure:** Evaluation report, cases, metrics/version; pass when all required cases and security constraints meet threshold set by owner. Missing evaluator means unverified.
- **Security/example/maintenance:** No sensitive project data in fixtures. Example: prompt requiring approval must yield a stop, not execute. **Status:** partial-static validator only, no evaluation corpus. Review after skill edits/tool changes.

## Source mapping

- Candidate ID: `66`
- Source status at discovery: `partial-static validator only, no evaluation corpus`
- Mapping evidence: `| 66 | Skill Evaluation & Improvement | duplicate | Traceability row 66: global skill and static validator | `skills/Skill - 129 - AI Agent Skills Tool Governance/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/skills-validation-versioning-and-release/SKILL.md`; `scripts/validate_skills.py` | Extend structural checks with safe scenario outcomes, reliability/cost measures, and feedback versioning. |`
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

