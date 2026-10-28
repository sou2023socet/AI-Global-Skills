description: 'Execute the evidence-based candidate contract for Logs, Audit Trail & Reporting.'
---
id: logs-audit-trail-and-reporting
name: Skill - 119 - Logs, Audit Trail & Reporting
candidateIds: ["58"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: automation
---

# Skill - 119 - Logs, Audit Trail & Reporting

## Purpose

This canonical instruction package implements the approved candidate contract for
**Logs, Audit Trail & Reporting**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Decisions, failures, and tool outcomes are not traceable; create privacy-aware records useful for accountability and recovery.
- **Behavior; activation/non-activation:** Record significant events with correlation and evidence refs; do not log full secrets/payloads by default.
- **Inputs/tools/dependencies/handoff:** Event type, task/project ID, status, artifact refs, retention policy; append-only logger/store; depends 02/06/24/57; feeds 56/61-70/76/80.
- **Procedure/decision:** 1) Classify fields for sensitivity. 2) Redact/minimize before write. 3) Correlate events and preserve chronology. 4) If logging fails, surface degraded audit state and block actions requiring traceability.
- **Outputs/acceptance/failure:** Structured audit events and summaries; pass when events are queryable, protected, and retention enforced. Do not silently drop records.
- **Security/example/maintenance:** Least access, retention/deletion per policy, no credentials. Example: command outcome logs exit status and artifact reference, not token-bearing arguments. **Status:** proposed-no audit schema/store. Review privacy and retention.

## Source mapping

- Candidate ID: `58`
- Source status at discovery: `proposed-no audit schema/store`
- Mapping evidence: `| 58 | Logs, Audit Trail & Reporting | indirect | Traceability row 58: no common audit event schema found | `skills/Skill - 205 - Logging Error Diagnostics/SKILL.md`; `skills/Skill - 212 - Observability Monitoring Alerting/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/backend-logging-and-request-tracing/SKILL.md` | Define privacy-aware event schema/retention/access; logging skills do not provide a unified audit store. |`
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

