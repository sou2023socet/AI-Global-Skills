description: 'Execute the evidence-based candidate contract for User Acceptance & Sign-Off Manager.'
---
id: user-acceptance-and-sign-off-manager
name: Skill - 101 - User Acceptance & Sign-Off Manager
candidateIds: ["49"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: delivery
---

# Skill - 101 - User Acceptance & Sign-Off Manager

## Purpose

This canonical instruction package implements the approved candidate contract for
**User Acceptance & Sign-Off Manager**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** UAT feedback and sign-off are informal or fabricated; record real stakeholder decisions against agreed acceptance scenarios.
- **Behavior; activation/non-activation:** Prepare sessions/cases and capture authorized feedback; do not sign on user's behalf.
- **Inputs/tools/dependencies/handoff:** Approved criteria, user/stakeholder identity/authority, safe environment, feedback channel; test evidence and decision record; depends 20/33/37/42-45/48; handoff to 50/79.
- **Procedure/decision:** 1) Confirm approver and scope. 2) Run or facilitate agreed scenarios. 3) Record pass/defect/defer and actual response. 4) No response or unresolved critical defect means no sign-off.
- **Outputs/acceptance/failure:** UAT cases, feedback, decision and date; pass means explicit authorized sign-off with scope. If stakeholder unavailable, mark pending.
- **Security/example/maintenance:** Minimize personal data and use approved accounts. Example: owner accepts calculator scope but defers mobile support; record only that scope. **Status:** partial-functional testing/SDLC gates, no sign-off record. Retain per policy.

## Source mapping

- Candidate ID: `49`
- Source status at discovery: `partial-functional testing/SDLC gates, no sign-off record`
- Mapping evidence: `| 49 | User Acceptance & Sign-Off Manager | partial | Traceability row 49: functional testing and planning | `enterprise-ui-fullstack-skills/.github/skills/end-to-end-quality-and-acceptance-management/SKILL.md`; `docs/sdlc/STAGE_GATES.md` | Require authorized stakeholder decision, explicit acceptance/rejection, and audit record. |`
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

