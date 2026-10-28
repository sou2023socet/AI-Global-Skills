---
name: Skill - 222 - Project Discovery and Design Audit
description: 'Use when Before design or substantial UI work on an existing application, or when project structure and current UI behavior are uncertain. Repository, UI, routes, components, themes, APIs, devices, dependencies, and documentation discovery.'
---

# Skill - 222 - Project Discovery and Design Audit

## Metadata
- Skill name and stable identifier: Project Discovery and Design Audit (`project-discovery-and-design-audit`)
- Version: 1.0.0
- Status: active
- Domain: Design Governance and SDLC
- Purpose and expected outcomes: Repository, UI, routes, components, themes, APIs, devices, dependencies, and documentation discovery.
- Relevant project types and technology categories: Web, mobile, desktop, APIs, and full-stack projects; Adapt to the target agent platform and actual design tooling; distinguish live integrations from specifications.
- Trigger conditions: Before design or substantial UI work on an existing application, or when project structure and current UI behavior are uncertain.
- Explicit non-trigger conditions: Do not invoke for unrelated work, routine changes fully owned by a narrower skill, or tasks whose required user approval is pending.
- Prerequisite skills: `design-engineering-governance`
- Related skills: `design-engineering-governance`
- Required tools: Read-only repository inspection and documentation tools; project-native tools only when necessary and approved.
- Optional tools: Static analysis, design tooling, accessibility checks, CI, or platform integrations when present and authorized.
- Risk classification: low
- Required permissions and approval conditions: Obtain explicit approval before production changes, destructive data operations, external cost, or tool-mediated design publication. Honor project-specific build/test/package gates; approval is scoped to named actions.

## Purpose and scope
This skill owns the task-specific workflow for repository, ui, routes, components, themes, apis, devices, dependencies, and documentation discovery. It produces verifiable, project-compatible artifacts without expanding into unrelated implementation. Adapt to the target agent platform and actual design tooling; distinguish live integrations from specifications.

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
- Inspect manifests, routes, screen entry points, shared components, tokens, themes, API clients, tests, and lifecycle documentation.
- Map each user-visible route to its current components, data dependencies, loading/error/empty states, and responsive behavior.
- Record platform, browser/device targets, accessibility evidence, design assets, and any unavailable integrations separately from assumptions.
- Produce a gap and reuse map with evidence, risks, and non-destructive next steps; do not start redesign implementation during discovery.
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
- Repository and UI inventory
- Screen-to-component and API map
- Reuse, gap, and risk register
- Task-specific decision, assumption, or exception records when a decision affects later work.
- Verification evidence and an explicit list of unverified operations.

## Quality gates and acceptance criteria
- Every in-scope route is inventoried or explicitly marked out of scope.
- Framework, build system, and existing design conventions are evidenced from repository files.
- Findings distinguish observed behavior from assumptions and identify reusable components.
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
- Prerequisite/dependent skill identifiers: `01`
- Invoke dependencies only for concrete subtasks; pass their outputs and approval state rather than repeating discovery.
- Send downstream agents the affected paths, decisions, contract version, validation evidence, and unresolved risks.

## Reusable resources
- [Master orchestrator](../../../orchestration/MASTER_ORCHESTRATOR.md)
- [Skill routing](../../../orchestration/SKILL_ROUTING.md)
- [Design approval policy](../../../orchestration/DESIGN_APPROVAL_POLICY.md)
- [Shared standards and templates](../../../references/README.md)
- [Scenario coverage](../../../tests/scenario-matrix.md)

## Example workflow
Before adding account recovery screens, trace the current login route, form controls, auth API, error states, and responsive layout.

## Verification evidence
Record the concrete artifact path, requirement/design identifier, review/test performed, outcome, and date/version. Distinguish automated execution from manual inspection and production evidence.

## Completion reporting
Report: scope completed; deliverables; decisions/assumptions; exact checks run and outcomes; checks not run and why; approvals still needed; residual risks; and next owner/action.

## Versioning and maintenance
Review this skill when its owning platform, framework, policy, or linked contract changes. Update version/changelog and scenario coverage with behavior-changing guidance; keep examples free of secrets and stale commands.
