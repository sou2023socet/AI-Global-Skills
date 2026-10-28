description: 'Execute the evidence-based candidate contract for Code Review & Refactoring Agent.'
---
id: code-review-and-refactoring-agent
name: Skill - 042 - Code Review & Refactoring Agent
candidateIds: ["32"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: development
---

# Skill - 042 - Code Review & Refactoring Agent

## Purpose

This canonical instruction package implements the approved candidate contract for
**Code Review & Refactoring Agent**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Defects, risky changes, duplication, and unnecessary diffs escape review; deliver prioritized findings and optional safe refactor plan.
- **Behavior; activation/non-activation:** Inspect diff for correctness/security/maintainability; do not silently make changes during review-only request.
- **Inputs/tools/dependencies/handoff:** Base/head diff, requirements, local standards, tests; Git diff and static analysis; depends 06/20/27/28; findings to 29/38/40.
- **Procedure/decision:** 1) Read scope and surrounding code. 2) Check requirement, edge/error paths, security, compatibility. 3) Rank actionable findings with evidence/confidence. 4) If no high-confidence issue, state review boundary; do not invent findings.
- **Outputs/acceptance/failure:** Findings with file/line/severity, rationale and fix suggestion; pass when all changed scope reviewed or limitations named. No automatic refactor.
- **Security/example/maintenance:** Protect sensitive code/logs and avoid public disclosure. Example: review detects missing ownership check in newly changed repository lookup. **Status:** partial-clean-code refactoring and appsec guidance, not review protocol. Preserve independent reviewer role where required.

## Phase E - Quality assurance

## Source mapping

- Candidate ID: `32`
- Source status at discovery: `partial-clean-code refactoring and appsec guidance, not review protocol`
- Mapping evidence: `| 32 | Code Review & Refactoring Agent | duplicate | Traceability row 32: clean-code and security skills | `skills/Skill - 229 - Refactoring Maintenance/SKILL.md`; `skills/Skill - 151 - Code Review Quality Gate/SKILL.md`; `skills/Skill - 249 - Technical Debt Management/SKILL.md` | Keep review-only outputs separate from approved refactoring; share severity/confidence/finding format. |`
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

