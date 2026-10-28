description: 'Execute the evidence-based candidate contract for UI/UX & Accessibility Tester.'
---
id: ui-ux-and-accessibility-tester
name: Skill - 083 - UI UX & Accessibility Tester
candidateIds: ["37"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: quality
---

# Skill - 083 - UI UX & Accessibility Tester

## Purpose

This canonical instruction package implements the approved candidate contract for
**UI/UX & Accessibility Tester**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Visual/interaction defects and inaccessible flows block users; verify usability/accessibility against defined criteria.
- **Behavior; activation/non-activation:** Test keyboard, semantics, focus, contrast and viewport under supported tools; do not claim WCAG conformance without appropriate audit scope.
- **Inputs/tools/dependencies/handoff:** Screens, user flows, target devices, criteria; browser accessibility tree, keyboard, screen reader if available; depends 12/20/31/33/34; defects to 40/42/49.
- **Procedure/decision:** 1) Map key user journeys and roles. 2) Check keyboard/focus/form labels/error announcements. 3) Check responsive/contrast criteria using selected tools. 4) If assistive tech unavailable, label untested criteria and do not infer pass.
- **Outputs/acceptance/failure:** Reproducible findings with device/tool/criterion; pass only for checked criteria. Tool coverage is disclosed.
- **Security/example/maintenance:** Use synthetic identities and redact screenshots. Example: error message is visually shown but not announced; record screen-reader finding with reproduction. **Status:** partial-functional/frontend/mobile skills. Keep supported WCAG version explicit.

## Source mapping

- Candidate ID: `37`
- Source status at discovery: `partial-functional/frontend/mobile skills`
- Mapping evidence: `| 37 | UI/UX & Accessibility Tester | duplicate | Traceability row 37: functional/frontend/mobile skills | `skills/Skill - 126 - Accessibility Responsive Quality/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/accessibility-and-inclusive-design/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/frontend-testing-and-visual-regression/SKILL.md` | Reconcile accessibility procedures and define observable WCAG/keyboard evidence by tool/platform. |`
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

