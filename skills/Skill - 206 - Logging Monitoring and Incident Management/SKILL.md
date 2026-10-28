---
name: Skill - 206 - Logging Monitoring and Incident Management
description: 'Use when Observability, alerting, incident response, or root-cause analysis is needed across application layers. Cross-layer observability, alerts, incident diagnosis, root-cause analysis, corrective actions, and recovery procedures.'
---

# Skill - 206 - Logging Monitoring and Incident Management

## Metadata
- Skill name and stable identifier: Logging Monitoring and Incident Management (`logging-monitoring-and-incident-management`)
- Version: 1.0.0
- Status: active
- Domain: Separation, Pipelines, and Delivery
- Purpose and expected outcomes: Cross-layer observability, alerts, incident diagnosis, root-cause analysis, corrective actions, and recovery procedures.
- Relevant project types and technology categories: Web, mobile, desktop, APIs, and full-stack projects; Inspect the actual project, delivery platform, and existing conventions before selecting tools or commands.
- Trigger conditions: Observability, alerting, incident response, or root-cause analysis is needed across application layers.
- Explicit non-trigger conditions: Do not invoke for unrelated work, routine changes fully owned by a narrower skill, or tasks whose required user approval is pending.
- Prerequisite skills: `backend-logging-and-request-tracing`, `production-environment-and-deployment-engineering`, `security-privacy-and-data-governance`
- Related skills: `backend-logging-and-request-tracing`, `production-environment-and-deployment-engineering`, `security-privacy-and-data-governance`
- Required tools: Read-only repository inspection and documentation tools; project-native tools only when necessary and approved.
- Optional tools: Static analysis, design tooling, accessibility checks, CI, or platform integrations when present and authorized.
- Risk classification: high
- Required permissions and approval conditions: Obtain explicit approval before production changes, destructive data operations, external cost, or tool-mediated design publication. Honor project-specific build/test/package gates; approval is scoped to named actions.

## Purpose and scope
This skill owns the task-specific workflow for cross-layer observability, alerts, incident diagnosis, root-cause analysis, corrective actions, and recovery procedures. It produces verifiable, project-compatible artifacts without expanding into unrelated implementation. Inspect the actual project, delivery platform, and existing conventions before selecting tools or commands.

## Trigger conditions
Activate when the task matches the trigger in Metadata or when a prerequisite skill routes a directly dependent subtask here.

## Non-trigger conditions
Do not activate solely because a repository contains related technology. Do not use this skill to bypass design approval, project policies, or a more specific operational/security workflow.

## Prerequisites
- Confirm the user goal, scope, and applicable approval state.
- Read the relevant repository instructions and current project conventions.
- Resolve prerequisite skills only when their decision or artifact is needed; do not load the whole library by default.

## Inputs and expected context
- User request, affected feature/platform, target users, acceptance criteria, and known constraints.
- Existing code/design/doc artifacts and any version or approval record relevant to this domain.
- Available tools, integrations, environment, and explicitly permitted operations.
- Required outputs, evidence expectations, and unresolved decisions.

## Discovery checklist
1. Identify the current implementation, source of truth, and owner for the affected area.
2. Inspect the narrowest relevant manifests, routes/contracts, tests, assets, documentation, and history.
3. Record observed behavior separately from assumptions; identify dependencies, risks, and unknowns.
4. Reuse valid components, patterns, decisions, and artifacts; do not overwrite unrelated user work.
5. Confirm whether required external tools or credentials are actually available before relying on them.

## Detailed execution workflow
1. **Scope and readiness:** restate the in-scope outcome, affected platforms, constraints, and required approvals. Stop before gated work when approval is missing.
2. **Baseline:** follow this skill's domain workflow:
- Map critical user journeys to logs, metrics, traces, health signals, privacy boundaries, and ownership/on-call routes.
- Define actionable alerts with symptom, threshold/window, severity, runbook, and noise control; avoid alerts on uncorrelated raw volume.
- During incidents, preserve timeline/evidence, assess impact, mitigate safely, and communicate status without exposing private data.
- After recovery, distinguish trigger/root cause/contributing factors and assign tracked corrective actions with verification.
3. **Plan:** map the intended change to requirements, dependencies, existing conventions, and rollback/recovery needs. Prefer an incremental approach with a clear boundary.
4. **Execute:** create or update only the listed deliverables; use established project tooling and do not fabricate integration or runtime results.
5. **Review:** inspect the resulting artifacts for correctness, security/privacy, compatibility, and consistency with linked contracts.
6. **Verify:** use the measurable gates below. Before any build, test, compile, run, install, package, benchmark, or artifact-generating check, obtain the approval required by the applicable project policy.
7. **Handoff:** pass verified decisions, changed paths, evidence, pending approvals, and unresolved issues to dependent skills/orchestrator.

## Decision tables and conditional behavior
| Condition | Required decision |
| --- | --- |
| Existing compatible convention or artifact | Reuse it; extend only when a documented gap remains. |
| Conflicting standard or unclear ownership | Record evidence and impact; request a decision before a material or irreversible change. |
| External integration/tool unavailable | Complete feasible offline work, state the limitation, and do not claim live integration. |
| User approval or execution approval absent | Pause the gated action; continue only with safe, permitted discovery or drafting. |
| Validation failure | Preserve output, diagnose the smallest root cause, and request any newly required approval before retrying. |

## Project-specific adaptation rules
- Honor existing framework, platform, localization, accessibility, security, naming, and testing conventions unless the request explicitly changes them.
- Adapt examples and deliverable paths to repository conventions; do not create empty directories solely to match a sample tree.
- For cross-platform work, document platform-specific behavior rather than assuming identical capabilities.
- Keep assumptions and exceptions visible, owned, and reviewable.

## Commands and configuration examples
- Prefer inspection and project-native commands; verify the command from manifests or documentation before proposing it.
- Commands that execute code, build, test, install, run, package, or create generated verification artifacts are subject to the project approval gate.
- Use placeholders for environment values; never include real credentials or tokens in docs, command history, fixtures, or examples.
- Record command, working directory, approval scope, outcome, and generated paths when execution is authorized.

## Required deliverables
- Observability coverage map
- Alert and runbook definitions
- Incident timeline and corrective actions
- Task-specific decision, assumption, or exception records when a decision affects later work.
- Verification evidence and an explicit list of unverified operations.

## Quality gates and acceptance criteria
- Critical paths have owner, signal, alert threshold, and response procedure.
- Logs/telemetry exclude secrets and use correlation IDs where supported.
- Incident actions are evidence-linked, prioritized, and have follow-up verification.
- Deliverables are scoped, readable, linked to evidence, and consistent with project conventions.
- No undocumented destructive action, fabricated result, or success-shaped fallback is introduced.

## Security and privacy safeguards
- Apply least privilege and minimize collection, exposure, and retention of sensitive data.
- Never place credentials, OTPs, session tokens, encryption keys, or production secrets in source, generated examples, logs, screenshots, or public responses.
- Validate inputs at the authoritative backend boundary; use client-side controls only as usability support.
- Treat design files, telemetry, diagnostics, and archived artifacts as potentially sensitive; inspect access and contents before sharing.

## Failure handling and recovery
- If scope, permission, or a required design approval is unclear, pause the gated action and request a specific decision.
- If a tool or service is unavailable, provide the closest supported deliverable and explicitly mark the blocked step unverified.
- If implementation or validation fails, preserve user changes and diagnostic evidence; do not hide errors or silently switch approaches.
- For risky changes, define rollback/recovery before execution and stop if data safety cannot be established.

## Dependencies and handoffs
- Prerequisite/dependent skill identifiers: `33`, `48`, `56`
- Invoke dependencies only for concrete subtasks; pass their outputs and approval state rather than repeating discovery.
- Send downstream agents the affected paths, decisions, contract version, validation evidence, and unresolved risks.

## Reusable resources
- [Master orchestrator](../../../orchestration/MASTER_ORCHESTRATOR.md)
- [Skill routing](../../../orchestration/SKILL_ROUTING.md)
- [Design approval policy](../../../orchestration/DESIGN_APPROVAL_POLICY.md)
- [Shared standards and templates](../../../references/README.md)
- [Scenario coverage](../../../tests/scenario-matrix.md)

## Example workflow
Investigate increased OTP delivery failures through sanitized metrics and request IDs without logging OTP content.

## Verification evidence
Record the concrete artifact path, requirement/design identifier, review/test performed, outcome, and date/version. Distinguish automated execution from manual inspection and production evidence.

## Completion reporting
Report: scope completed; deliverables; decisions/assumptions; exact checks run and outcomes; checks not run and why; approvals still needed; residual risks; and next owner/action.

## Versioning and maintenance
Review this skill when its owning platform, framework, policy, or linked contract changes. Update version/changelog and scenario coverage with behavior-changing guidance; keep examples free of secrets and stale commands.
