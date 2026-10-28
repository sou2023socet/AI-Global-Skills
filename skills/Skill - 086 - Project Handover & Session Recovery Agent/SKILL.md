description: 'Execute the evidence-based candidate contract for Project Handover & Session Recovery Agent.'
---
id: project-handover-and-session-recovery-agent
name: Skill - 086 - Project Handover & Session Recovery Agent
candidateIds: ["76"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: project-knowledge
---

# Skill - 086 - Project Handover & Session Recovery Agent

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Handover & Session Recovery Agent**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** New sessions repeat work or act on obsolete handover; reconstruct active state and verify it against workspace.
- **Behavior; activation/non-activation:** Read handovers, decisions, tasks, evidence; do not treat previous agent output as current truth.
- **Inputs/tools/dependencies/handoff:** Project identity, handover, task history, current Git/files, approvals; project memory and evidence; depends 05/06/58/72-77; hands to 04/74/80.
- **Procedure/decision:** 1) Load last authorized handover. 2) Compare status, files, tests and approvals to current source. 3) Reconcile stale/conflicting items. 4) If identity or change history is unclear, present uncertainty and stop risky continuation.
- **Outputs/acceptance/failure:** Resume brief with verified done/in-progress/blocked/next; pass when each active claim is current or labeled stale. Missing handover may be reconstructed with citations.
- **Security/example/maintenance:** Respect session/project privacy; do not expose prior unrelated chats. Example: previous note says no tests, current repository includes tests; update from current source. **Status:** partial-global skill gives stage handoff; no project recovery process. Revalidate every resume.

## Source mapping

- Candidate ID: `76`
- Source status at discovery: `partial-global skill gives stage handoff; no project recovery process`
- Mapping evidence: `| 76 | Project Handover & Session Recovery Agent | duplicate | Traceability row 76: global-system and token-efficient skills | `enterprise-ui-fullstack-skills/.github/skills/project-continuity-and-change-impact-management/SKILL.md`; `orchestration/WORKFLOW_PATTERNS.md` | Reconcile overlapping continuity guidance; define canonical state and verified resume behavior. |`
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

