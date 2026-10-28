description: 'Execute the evidence-based candidate contract for Documentation Synchronization.'
---
id: documentation-synchronization
name: Skill - 094 - Documentation Synchronization
candidateIds: ["44"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: delivery
---

# Skill - 094 - Documentation Synchronization

## Purpose

This canonical instruction package implements the approved candidate contract for
**Documentation Synchronization**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Docs drift after source/config/API changes; detect impacted docs and synchronize canonical claims.
- **Behavior; activation/non-activation:** Compare source changes to linked docs; do not overwrite user-maintained content without review.
- **Inputs/tools/dependencies/handoff:** Diff, source-of-truth map, docs, owner rules; Git, links, API/schema extraction; depends 06/14/43/75; handoff updated docs to review.
- **Procedure/decision:** 1) Map changed interfaces to docs. 2) Locate stale statements/examples. 3) Update bounded references. 4) If sources conflict or content is intentionally historical, retain with date/context and seek owner decision.
- **Outputs/acceptance/failure:** Change-to-doc map, diff, link check; pass when each impacted doc is updated, confirmed unaffected, or explicitly deferred. Broken link means fail.
- **Security/example/maintenance:** Never copy secret config into examples. Example: renamed route updates API and client setup docs with contract test reference. **Status:** partial-documentation skill says drift checking but no synchronization workflow evidence. Run at release/change.

## Source mapping

- Candidate ID: `44`
- Source status at discovery: `partial-documentation skill says drift checking but no synchronization workflow evidence`
- Mapping evidence: `| 44 | Documentation Synchronization | duplicate | Traceability row 44: docs and discovery skills | `skills/Skill - 174 - Documentation Knowledge Management/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/project-continuity-and-change-impact-management/SKILL.md` | Add ownership, change detection, source-of-truth, and generated-doc review policy. |`
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

