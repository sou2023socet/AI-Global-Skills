description: 'Execute the evidence-based candidate contract for Automation Workflow Designer.'
---
id: automation-workflow-designer
name: Skill - 116 - Automation Workflow Designer
candidateIds: ["52"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: automation
---

# Skill - 116 - Automation Workflow Designer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Automation Workflow Designer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Automation actions lack explicit triggers, checkpoints, and failure branches; design repeatable, bounded workflows.
- **Behavior; activation/non-activation:** Model triggerâ†’conditionsâ†’actionsâ†’approvalsâ†’outputs; not a scheduler implementation or permission override.
- **Inputs/tools/dependencies/handoff:** Goal, events, actor, policies, dependencies, idempotency needs; workflow diagram/schema; depends 02/20/23/24/51/57; hands runtime to 53-59.
- **Procedure/decision:** 1) Define start condition and guards. 2) Specify action order, idempotency, timeout/retry, approval and compensation. 3) Model success/failure/disable paths. 4) If an action is unsafe to retry/compensate, require manual checkpoint.
- **Outputs/acceptance/failure:** Workflow spec/state diagram and test cases; pass when every transition has owner/result and duplicate-run behavior. Unavailable trigger is marked unsupported.
- **Security/example/maintenance:** Human approval for consequential external side effects. Example: nightly report runs only with fresh approved project manifest and emits a status artifact. **Status:** partial-workflow scheduling/global system skills cover pieces. Version and monitor workflow changes.

## Source mapping

- Candidate ID: `52`
- Source status at discovery: `partial-workflow scheduling/global system skills cover pieces`
- Mapping evidence: `| 52 | Automation Workflow Designer | duplicate | Traceability row 52: workflow scheduling and global-system skills | `skills/Skill - 267 - Workflow Automation Scheduling/SKILL.md`; `orchestration/WORKFLOW_PATTERNS.md`; `orchestration/MASTER_ORCHESTRATOR.md` | Reconcile workflow design vs scheduling; define triggers, idempotency, recovery, and side effects. |`
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

