description: 'Execute the evidence-based candidate contract for Development Standards Enforcer.'
---
id: development-standards-enforcer
name: Skill - 047 - Development Standards Enforcer
candidateIds: ["27"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: development
---

# Skill - 047 - Development Standards Enforcer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Development Standards Enforcer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Inconsistent code practices cause defects and maintenance cost; check project standards and report actionable deviations.
- **Behavior; activation/non-activation:** Apply local conventions, linters, error/security rules; do not impose external style or rewrite unrelated code.
- **Inputs/tools/dependencies/handoff:** Repository rules, language/toolchain, changed files; configured linter/compiler and review checklist; depends 02/25/26; hands fixes to feature/refactor/review skills.
- **Procedure/decision:** 1) Discover authoritative rules/config. 2) Check changed scope for naming, modularity, errors, tests, security. 3) Run only approved existing checks. 4) If no rule exists, label recommendation rather than violation.
- **Outputs/acceptance/failure:** Findings with rule/source/severity and exceptions; pass when all scoped findings are fixed, accepted, or explicitly deferred. Tool unavailable is recorded.
- **Security/example/evidence/maintenance:** Never remove validation/auth checks for style. Example: a catch-all suppresses errors; report rule and expected surface behavior. **Status:** partial-clean-code and stack skills. Refresh rule set with project changes.

## Source mapping

- Candidate ID: `27`
- Source status at discovery: `partial-clean-code and stack skills`
- Mapping evidence: `| 27 | Development Standards Enforcer | duplicate | Traceability row 27: clean-code and stack-specific skills | `skills/Skill - 152 - Coding Standards/SKILL.md`; `skills/Skill - 229 - Refactoring Maintenance/SKILL.md` | Unify repository standards discovery and exception evidence without conflating enforcement and refactoring. |`
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

