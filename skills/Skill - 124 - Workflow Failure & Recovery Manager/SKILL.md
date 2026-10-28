description: 'Execute the evidence-based candidate contract for Workflow Failure & Recovery Manager.'
---
id: workflow-failure-and-recovery-manager
name: Skill - 124 - Workflow Failure & Recovery Manager
candidateIds: ["56"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: automation
---

# Skill - 124 - Workflow Failure & Recovery Manager

## Purpose

This canonical instruction package implements the approved candidate contract for
**Workflow Failure & Recovery Manager**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Interrupted workflows repeat side effects or lose progress; classify state and resume from verified checkpoints safely.
- **Behavior; activation/non-activation:** Recover failed/interrupted tasks; do not retry non-idempotent action automatically or conceal original failure.
- **Inputs/tools/dependencies/handoff:** Workflow/task ID, last checkpoint, logs, side effects, approval; audit/task state; depends 06/52-55/57-58; returns to orchestrator/owner.
- **Procedure/decision:** 1) Freeze/reconcile current external state. 2) Identify last verified checkpoint and actions with uncertain completion. 3) Resume only idempotent/reconciled work; otherwise request owner action. 4) Bound retries and retain original diagnostics.
- **Outputs/acceptance/failure:** Recovery decision, checkpoint, retry/rollback record; pass when no duplicate irreversible action occurs and remaining state is explicit. Unknown side effect blocks.
- **Security/example/maintenance:** Require fresh approval for changed/repeated consequential commands. Example: timeout after account creation requires existence check before retry. **Status:** partial-RCA and worker error state only. Test interruption/idempotency paths.

## Source mapping

- Candidate ID: `56`
- Source status at discovery: `partial-RCA and worker error state only`
- Mapping evidence: `| 56 | Workflow Failure & Recovery Manager | duplicate | Traceability row 56: scheduling and RCA skills | `skills/Skill - 230 - Reliability Fault Recovery/SKILL.md`; `skills/Skill - 202 - Incident Response Root Cause/SKILL.md`; `orchestration/CONFLICT_RESOLUTION.md` | Compose checkpoints/resume and safe recovery; prevent duplicate non-idempotent actions. |`
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

