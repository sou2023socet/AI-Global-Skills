description: 'Execute the evidence-based candidate contract for Project Registry.'
---
id: project-registry
name: Skill - 013 - Project Registry
candidateIds: ["03"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: foundation
---

# Skill - 013 - Project Registry

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Registry**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Similar project names and stale paths can direct work to the wrong repository; maintain canonical identities, locations, ownership, technology, status, and knowledge links.
- **Behavior; activation/non-activation:** Resolve a project before multi-repository work; do not copy source code or infer identity from a folder name alone.
- **Inputs/tools/dependencies/handoff:** User/project identifier, approved repository paths, ownership and freshness; filesystem/Git inspection and a registry schema; depends 01/02; feeds 04, 72, and 80.
- **Procedure/decision:** 1) Match supplied identity to canonical remote/path. 2) Check repository metadata and last-verified date. 3) Record aliases separately. 4) If multiple candidates match or access is denied, ask/stop rather than selecting silently.
- **Outputs/acceptance/failure:** Machine-readable project record and human index; pass when each entry has unique ID, canonical path, status source, and freshness. Registry write failures leave existing entries intact.
- **Security/example/evidence/maintenance:** Store no secrets or private source; access to private projects must be authorized. Example: "NexusMath" matches two worktrees; report both until owner selects canonical. **Status:** proposed-no registry file found. Revalidate path/ownership on change; propose, do not impose, storage.

## Source mapping

- Candidate ID: `03`
- Source status at discovery: `proposed-no registry file found`
- Mapping evidence: `| 03 | Project Registry | missing | Traceability row 03: no registry found | `skills/Skill - 227 - Project Structure Manager/SKILL.md` is adjacent, not a registry | Define canonical identity, owner, access, freshness, and source-of-truth before creating a registry service. |`
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

