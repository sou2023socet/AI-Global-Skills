description: 'Execute the evidence-based candidate contract for Regression & Change Impact Analyzer.'
---
id: regression-and-change-impact-analyzer
name: Skill - 078 - Regression & Change Impact Analyzer
candidateIds: ["40"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: quality
---

# Skill - 078 - Regression & Change Impact Analyzer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Regression & Change Impact Analyzer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Changes break dependents that are not retested; map diff to affected behaviors and select regression coverage.
- **Behavior; activation/non-activation:** Analyze diff, callers, contracts and tests; do not claim full regression based on changed files only.
- **Inputs/tools/dependencies/handoff:** Base/head diff, dependency graph, requirements/tests; Git/search/LSP and test inventory; depends 06/28-33; hands tests to 35-39 and readiness to 42.
- **Procedure/decision:** 1) Identify changed symbols/contracts/data. 2) Trace downstream callers and user paths. 3) Rank tests by impact/risk. 4) If graph/tooling incomplete, add uncertainty and broaden or block test selection.
- **Outputs/acceptance/failure:** Change-impact map and regression plan/results; pass when changed public/data paths have rationale-backed coverage. Missing test is a gap.
- **Security/example/maintenance:** Avoid touching unrelated state. Example: DTO field change triggers API serialization and UI parsing tests. **Status:** partial-unit/refactor/test skills advise regressions, no impact engine. Keep test map current.

## Source mapping

- Candidate ID: `40`
- Source status at discovery: `partial-unit/refactor/test skills advise regressions, no impact engine`
- Mapping evidence: `| 40 | Regression & Change Impact Analyzer | duplicate | Traceability row 40: unit/automation/refactor skills | `skills/Skill - 146 - Build Regression Verification/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/project-continuity-and-change-impact-management/SKILL.md` | Define diff-to-impact evidence and risk-based verification; preserve regression and continuity boundaries. |`
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

