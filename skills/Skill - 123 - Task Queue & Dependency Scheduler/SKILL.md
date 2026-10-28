description: 'Execute the evidence-based candidate contract for Task Queue & Dependency Scheduler.'
---
id: task-queue-and-dependency-scheduler
name: Skill - 123 - Task Queue & Dependency Scheduler
candidateIds: ["55"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: automation
---

# Skill - 123 - Task Queue & Dependency Scheduler

## Purpose

This canonical instruction package implements the approved candidate contract for
**Task Queue & Dependency Scheduler**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Tasks start before prerequisites or become orphaned; maintain dependency-aware queue and readiness states.
- **Behavior; activation/non-activation:** Order tasks by approved priority, dependencies and constraints; do not schedule blocked or unapproved mutations.
- **Inputs/tools/dependencies/handoff:** Task IDs, priorities, dependencies, owners, status, deadlines; task store/graph; depends 06/22/23/53-54; dispatches eligible work, failures to 56.
- **Procedure/decision:** 1) Validate unique task/dependency IDs and cycles. 2) Compute ready vs blocked states. 3) Select by approved priority/fairness rule. 4) Cycle/unknown dependency prevents dispatch until resolved.
- **Outputs/acceptance/failure:** Queue snapshot, dependency graph, ready/block reasons; pass when every task has valid state and no dependency is bypassed. Store failure blocks autonomous scheduling.
- **Security/example/maintenance:** Access scoped to project; record approval prerequisites. Example: integration test waits for API contract and service implementation. **Status:** partial-SDLC/task scheduling instructions, no common scheduler schema. Reconcile statuses periodically.

## Source mapping

- Candidate ID: `55`
- Source status at discovery: `partial-SDLC/task scheduling instructions, no common scheduler schema`
- Mapping evidence: `| 55 | Task Queue & Dependency Scheduler | partial | Traceability row 55: scheduling/planning guidance | `skills/Skill - 267 - Workflow Automation Scheduling/SKILL.md`; `orchestration/DEPENDENCY_GRAPH.md` | Define shared task schema, prerequisite readiness, priority, idempotency, and fairness. |`
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

