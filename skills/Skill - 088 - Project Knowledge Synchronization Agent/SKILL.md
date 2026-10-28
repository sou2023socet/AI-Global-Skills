description: 'Execute the evidence-based candidate contract for Project Knowledge Synchronization Agent.'
---
id: project-knowledge-synchronization-agent
name: Skill - 088 - Project Knowledge Synchronization Agent
candidateIds: ["75"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: project-knowledge
---

# Skill - 088 - Project Knowledge Synchronization Agent

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Knowledge Synchronization Agent**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Indexes/status/docs become stale after project changes; identify and reconcile records with canonical sources.
- **Behavior; activation/non-activation:** Compare records to source changes and update authorized derived fields; do not overwrite conflicts silently.
- **Inputs/tools/dependencies/handoff:** Canonical source map, Git changes, manifest/docs/status, sync permissions; link/hash checker; depends 06/44/58/72-73; feeds 61/76/80.
- **Procedure/decision:** 1) Detect changed sources and dependent records. 2) Mark stale/conflicting entries. 3) Regenerate derived content with source links. 4) Preserve manual decisions and request owner resolution on conflict.
- **Outputs/acceptance/failure:** Sync report and bounded update diff; pass when each affected record is updated, confirmed current, or flagged. Failed source read means stale/unknown.
- **Security/example/maintenance:** Propagate access/deletion restrictions; avoid copying secrets into indexes. Example: package version changed, manifest marked stale until verified. **Status:** partial-documentation drift exists, no project knowledge sync engine. Run on updates.

## Source mapping

- Candidate ID: `75`
- Source status at discovery: `partial-documentation drift exists, no project knowledge sync engine`
- Mapping evidence: `| 75 | Project Knowledge Synchronization Agent | indirect | Traceability row 75: documentation drift/discovery | `skills/Skill - 174 - Documentation Knowledge Management/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/project-continuity-and-change-impact-management/SKILL.md` | Define source-of-truth, index/manifest change detection, conflict resolution, and stale markers. |`
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

