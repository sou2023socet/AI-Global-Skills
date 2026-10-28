description: 'Execute the evidence-based candidate contract for Project Memory & Handover.'
---
id: project-memory-and-handover
name: Skill - 012 - Project Memory & Handover
candidateIds: ["05"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: foundation
---

# Skill - 012 - Project Memory & Handover

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Memory & Handover**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Decisions and blockers are repeatedly rediscovered; preserve concise, verified, project-scoped state so future work resumes without assuming stale notes are true.
- **Behavior; activation/non-activation:** Capture/restore task state with provenance; do not store credentials, unrelated project context, or speculative facts as decisions.
- **Inputs/tools/dependencies/handoff:** Approved project ID, current task, decisions, changed files, tests, blockers; canonical docs/session storage; depends 06/72/77; hands verified resume brief to 76/80.
- **Procedure/decision:** 1) Gather current Git/status and task evidence. 2) Separate decisions, facts, assumptions, and pending approvals. 3) Write/update only the authorized handover location. 4) On resume, recheck volatile facts; if notes contradict workspace, current evidence wins and conflict is reported.
- **Outputs/acceptance/failure:** Dated handover with done/in-progress/blocked/next and source references; pass when a new session can identify safe next action without repeating completed work. If storage unavailable, provide transient summary and disclose.
- **Security/example/evidence/maintenance:** Exclude secrets, PII, and private unrelated project data; retention/access must be authorized. Example: resume finds a formerly passing test now failing; state is refreshed, not blindly trusted. **Status:** partial-global-system stage reporting only; no project memory store. Review stale records on resume.

## Source mapping

- Candidate ID: `05`
- Source status at discovery: `partial-global-system stage reporting only; no project memory store`
- Mapping evidence: `| 05 | Project Memory & Handover | indirect | Traceability row 05: global-system stage guidance | `enterprise-ui-fullstack-skills/.github/skills/project-continuity-and-change-impact-management/SKILL.md`; `orchestration/WORKFLOW_PATTERNS.md` | Add authorized durable project state, privacy boundaries, and verified resume procedure. |`
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

