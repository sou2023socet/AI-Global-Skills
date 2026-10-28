description: 'Execute the evidence-based candidate contract for User Approval & Decision Manager.'
---
id: user-approval-and-decision-manager
name: Skill - 036 - User Approval & Decision Manager
candidateIds: ["24"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: research-planning
---

# Skill - 036 - User Approval & Decision Manager

## Purpose

This canonical instruction package implements the approved candidate contract for
**User Approval & Decision Manager**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Decisions and approvals are implicit or lost; capture who authorized what, scope, conditions, and expiry.
- **Behavior; activation/non-activation:** Identify decision gates and record explicit response; do not infer consent from silence or prior unrelated approval.
- **Inputs/tools/dependencies/handoff:** Proposed action/options, risk, affected target, user/owner response; approval record; depends 02/57; gates 20/22/26/47-50.
- **Procedure/decision:** 1) Classify reversible/destructive/external/production/paid action. 2) Present exact action, target, impact, rollback, alternatives. 3) Obtain explicit scoped approval/denial. 4) If scope changes or approval expires, re-request; never proceed on ambiguity.
- **Outputs/acceptance/failure:** Decision record and gated task state; pass when action matches approval exactly. Missing owner/response marks BLOCKED.
- **Security/example/evidence/maintenance:** Least privilege and auditable, privacy-aware records. Example: approval for a staging migration does not authorize production. **Status:** partial-policy and text gates exist; no decision ledger/enforcement. Review approvals before execution.

## Phase D - Development

## Source mapping

- Candidate ID: `24`
- Source status at discovery: `partial-policy and text gates exist; no decision ledger/enforcement`
- Mapping evidence: `| 24 | User Approval & Decision Manager | partial | Traceability row 24: approval guidance and `SECURITY.md` | `skills/Skill - 177 - Engineering Governance/SKILL.md`; `skills/Skill - 145 - Build and Test Approval Gate/SKILL.md`; `docs/sdlc/RISK_AND_APPROVAL_POLICY.md` | Specify decision ledger, command/action scope, expiry, denial, and revocation; no controller is proven. |`
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

