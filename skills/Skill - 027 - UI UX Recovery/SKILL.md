description: 'Execute the evidence-based candidate contract for UI/UX Recovery.'
---
id: ui-ux-recovery
name: Skill - 027 - UI UX Recovery
candidateIds: ["12"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: recovery
---

# Skill - 027 - UI UX Recovery

## Purpose

This canonical instruction package implements the approved candidate contract for
**UI/UX Recovery**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Existing screens/flows are unknown; inventory UI, navigation, validation, responsiveness, and accessibility without forcing redesign.
- **Behavior; activation/non-activation:** Inspect authorized UI in available viewports and map observable flows; do not alter visuals or access data beyond test scope.
- **Inputs/tools/dependencies/handoff:** App URL/build, supported devices, authorized account, expected constraints; browser/device tools and screenshots; depends 04/09; hands gaps to 10/20/37/43.
- **Procedure/decision:** 1) Inventory routes/screens and role gates. 2) Exercise representative forms/navigation. 3) Capture viewport/keyboard/validation evidence. 4) If login or tooling is unavailable, report inaccessible areas as unverified, not absent.
- **Outputs/acceptance/failure:** Screen/flow inventory, findings, redacted screenshots; pass when each scoped screen has state and viewport coverage recorded. Broken capture is documented.
- **Security/example/evidence/maintenance:** Use synthetic identity; hide user data. Example: map calculator route and invalid-input feedback at desktop/mobile sizes. **Status:** partial-frontend and functional skills cover implementation/testing, not recovery inventory. Refresh on UI release.

## Source mapping

- Candidate ID: `12`
- Source status at discovery: `partial-frontend and functional skills cover implementation/testing, not recovery inventory`
- Mapping evidence: `| 12 | UI/UX Recovery | duplicate | Traceability row 12: frontend and functional-testing skills | `skills/Skill - 263 - UI UX Research Design/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/ui-ux-research-and-information-architecture/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/project-discovery-and-design-audit/SKILL.md` | Consolidate the recovery workflow while retaining research, accessibility, and platform-specific specialists. |`
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

