description: 'Execute the evidence-based candidate contract for Project Manifest & Index Generator.'
---
id: project-manifest-and-index-generator
name: Skill - 089 - Project Manifest & Index Generator
candidateIds: ["72"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: project-knowledge
---

# Skill - 089 - Project Manifest & Index Generator

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Manifest & Index Generator**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Project metadata and artifacts are hard to discover; generate consistent machine/human indexes with provenance.
- **Behavior; activation/non-activation:** Collect approved facts and update index; do not overwrite manually owned or stale fields without conflict policy.
- **Inputs/tools/dependencies/handoff:** Registry identity, repository manifests, artifact map, schema/owner; filesystem/Git and YAML/Markdown; depends 03/04/06/71; feeds 05/61/73-77/80.
- **Procedure/decision:** 1) Validate project identity/schema. 2) Extract only allowed facts and source references. 3) Compare generated vs existing fields. 4) Preserve manual fields or flag conflict until owner resolves.
- **Outputs/acceptance/failure:** Manifest and index with generated-at/source metadata; pass when schema validates and paths resolve. Missing field remains unknown.
- **Security/example/maintenance:** Exclude secrets/private user data. Example: index module directories and actual package versions with scan timestamp. **Status:** proposed shared template/service; no manifest found. Regenerate only by approved cadence.

## Source mapping

- Candidate ID: `72`
- Source status at discovery: `proposed shared template/service; no manifest found`
- Mapping evidence: `| 72 | Project Manifest & Index Generator | indirect | Traceability row 72: no project manifest/index generator found globally | `skills/Skill - 227 - Project Structure Manager/SKILL.md`; `universal-project-setup/SKILL.md` | Define schema, source freshness, generated/manual ownership, and validation; no generator found in evidence reviewed. |`
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

