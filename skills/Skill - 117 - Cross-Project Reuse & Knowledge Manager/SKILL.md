description: 'Execute the evidence-based candidate contract for Cross-Project Reuse & Knowledge Manager.'
---
id: cross-project-reuse-and-knowledge-manager
name: Skill - 117 - Cross-Project Reuse & Knowledge Manager
candidateIds: ["60"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: automation
---

# Skill - 117 - Cross-Project Reuse & Knowledge Manager

## Purpose

This canonical instruction package implements the approved candidate contract for
**Cross-Project Reuse & Knowledge Manager**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Lessons/assets are duplicated or leak between projects; enable permission-aware reuse with provenance and isolation.
- **Behavior; activation/non-activation:** Search approved metadata/templates/patterns, classify reusable vs project-specific; do not export source/secrets by default.
- **Inputs/tools/dependencies/handoff:** Project identities, allowed knowledge sources, reuse goal, licenses; registry/index; depends 03/06/58/73/77; informs 18/19/28/53/68.
- **Procedure/decision:** 1) Verify source project and access. 2) Search metadata and approved reusable artifacts. 3) Check license, context assumptions and secret scan. 4) If transfer rights or sensitivity unclear, exclude and ask owner.
- **Outputs/acceptance/failure:** Reuse candidate report with provenance/constraints; pass when no unauthorized content crosses boundary. Failed access is not treated as no match.
- **Security/example/maintenance:** Enforce tenant/project isolation and consent. Example: share a generic test checklist, not a project's private API schema. **Status:** partial-principle in global system skill only. Revalidate permissions on each reuse.

## Phase H - Maintenance and continuous improvement

## Source mapping

- Candidate ID: `60`
- Source status at discovery: `partial-principle in global system skill only`
- Mapping evidence: `| 60 | Cross-Project Reuse & Knowledge Manager | partial | Traceability row 60: discovery and global-system guidance | `skills/Skill - 129 - AI Agent Skills Tool Governance/SKILL.md`; `skills/Skill - 178 - Engineering Orchestrator Continuous Improvement/SKILL.md` | Define provenance/search/consent and isolation; do not index private source or secrets without authorization. |`
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

