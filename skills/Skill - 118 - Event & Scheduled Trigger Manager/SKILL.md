description: 'Execute the evidence-based candidate contract for Event & Scheduled Trigger Manager.'
---
id: event-and-scheduled-trigger-manager
name: Skill - 118 - Event & Scheduled Trigger Manager
candidateIds: ["59"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: automation
---

# Skill - 118 - Event & Scheduled Trigger Manager

## Purpose

This canonical instruction package implements the approved candidate contract for
**Event & Scheduled Trigger Manager**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Scheduled/event runs may duplicate or violate permissions; register triggers and execution constraints safely.
- **Behavior; activation/non-activation:** Configure supported triggers, deduplication, pause/disable, windows; not an assumption that host can schedule jobs.
- **Inputs/tools/dependencies/handoff:** Trigger source, schedule, timezone, task, permission, dedup key; platform scheduler/event API; depends 52/55/57/58; failures to 56.
- **Procedure/decision:** 1) Verify platform trigger capability and identity. 2) Define schedule/window, condition and idempotency key. 3) Test disabled/read-only path. 4) Unsupported capability, ambiguous timezone, or missing permission means do not activate.
- **Outputs/acceptance/failure:** Trigger registry, run ledger, disable instructions; pass when duplicate events produce at most one authorized run per key. Missed run must be visible.
- **Security/example/maintenance:** Do not schedule production mutations without explicit approval; protect tokens. Example: daily audit starts only if registry freshness check succeeds. **Status:** partial-workflow scheduling has cron examples, no trigger manager. Monitor drift/timezone.

## Source mapping

- Candidate ID: `59`
- Source status at discovery: `partial-workflow scheduling has cron examples, no trigger manager`
- Mapping evidence: `| 59 | Event & Scheduled Trigger Manager | duplicate | Traceability row 59: workflow scheduling skill | `skills/Skill - 267 - Workflow Automation Scheduling/SKILL.md`; `orchestration/WORKFLOW_PATTERNS.md` | Add trigger registry, permissions, deduplication, pause/disable, and replay contract. |`
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

