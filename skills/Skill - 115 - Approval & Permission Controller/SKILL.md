description: 'Execute the evidence-based candidate contract for Approval & Permission Controller.'
---
id: approval-and-permission-controller
name: Skill - 115 - Approval & Permission Controller
candidateIds: ["57"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: automation
---

# Skill - 115 - Approval & Permission Controller

## Purpose

This canonical instruction package implements the approved candidate contract for
**Approval & Permission Controller**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Policy statements alone do not enforce least privilege; resolve authorization and gate actions with traceable scope.
- **Behavior; activation/non-activation:** Evaluate actor/action/resource/environment/approval; never infer permission from task context.
- **Inputs/tools/dependencies/handoff:** Identity, requested action, target, risk, approval record, policy; host auth/policy store; depends 02/24; gates 25-80.
- **Procedure/decision:** 1) Classify action and resource. 2) Verify actor permission and current approval conditions. 3) Allow only exact authorized scope and log outcome. 4) Deny/unknown/error defaults to blocked; request human resolution.
- **Outputs/acceptance/failure:** Allow/deny decision, scope, expiry, audit reference; pass when negative tests prove unauthorized actions are denied. Policy service outage fails closed.
- **Security/example/maintenance:** Protect identities and approvals; no privilege escalation. Example: staging approval cannot authorize production deploy. **Status:** partial-`SECURITY.md` mandates approvals, no enforcement controller found. Review policy and revocation tests.

## Source mapping

- Candidate ID: `57`
- Source status at discovery: `partial-`SECURITY`
- Mapping evidence: `| 57 | Approval & Permission Controller | partial | Traceability row 57: security policy and test-account guidance | `skills/Skill - 177 - Engineering Governance/SKILL.md`; `skills/Skill - 145 - Build and Test Approval Gate/SKILL.md`; `docs/sdlc/RISK_AND_APPROVAL_POLICY.md` | Specify enforcement separately from prose policy; scope, expiry, denial, revocation, and audit. |`
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

