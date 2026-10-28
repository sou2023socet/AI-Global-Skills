description: 'Execute the evidence-based candidate contract for Release & Version History Manager.'
---
id: release-and-version-history-manager
name: Skill - 102 - Release & Version History Manager
candidateIds: ["79"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: roadmap-release
---

# Skill - 102 - Release & Version History Manager

## Purpose

This canonical instruction package implements the approved candidate contract for
**Release & Version History Manager**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Release claims lack artifact/test/approval provenance; keep an accurate chronological record and rollback reference.
- **Behavior; activation/non-activation:** Record confirmed version facts; do not create a release entry from a planned tag or successful local build.
- **Inputs/tools/dependencies/handoff:** Release event, tag/artifact hashes, verification, approver, rollback, change notes; Git/release registry; depends 06/42/46-50/77; feeds 61/69/76/80.
- **Procedure/decision:** 1) Confirm release artifact and identity. 2) Link changes/tests/approval/deployment evidence. 3) Record status and known limitations. 4) If deployment is unverified, record as prepared/implemented-unverified, not released.
- **Outputs/acceptance/failure:** Append-only release record and version index; pass when chronology and artifacts reconcile. Missing tag/hash is explicit.
- **Security/example/maintenance:** Keep secrets and private deployment credentials out of notes. Example: version candidate passed staging but has no production approval, so history says "verified staging," not "released." **Status:** partial-deployment skill provides verification but no history ledger. Preserve immutable references.

## Source mapping

- Candidate ID: `79`
- Source status at discovery: `partial-deployment skill provides verification but no history ledger`
- Mapping evidence: `| 79 | Release & Version History Manager | duplicate | Traceability row 79: deployment/DevOps skills | `skills/Skill - 138 - Artifact Release Builder/SKILL.md`; `skills/Skill - 219 - Production Readiness Release Management/SKILL.md`; `CHANGELOG.md` | Define immutable release provenance/version history; do not infer active releases from policy. |`
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

