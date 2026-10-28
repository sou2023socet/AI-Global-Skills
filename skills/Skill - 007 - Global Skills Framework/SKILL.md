description: 'Execute the evidence-based candidate contract for Global Skills Framework.'
---
id: global-skills-framework
name: Skill - 007 - Global Skills Framework
candidateIds: ["01"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: foundation
---

# Skill - 007 - Global Skills Framework

## Purpose

This canonical instruction package implements the approved candidate contract for
**Global Skills Framework**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Inconsistent skill structure and discovery impede reuse; define common metadata, lifecycle, invocation, versioning, documentation, and validation rules so skills are interoperable.
- **Behavior; activation/non-activation:** Establish the contract, examples, compatibility policy, and deprecation path when creating or changing the library; do not make project-specific feature decisions.
- **Inputs/tools/dependencies/handoff:** Platform conventions, current authoring rules, validator behavior, candidate requirements; Markdown/YAML, repository validator; depends 02 and 57; hands contracts to all skill authors and 53.
- **Procedure/decision:** 1) Compare platform requirements with repository format. 2) Inventory current fields and validator checks. 3) Propose a versioned schema and compatibility tests. 4) If platform constraints conflict, record the conflict and request review rather than silently changing the schema.
- **Outputs/acceptance/failure:** Schema, template, lifecycle/version rules, compatibility report; pass when fixtures cover required/invalid metadata and platform behavior. Preserve current format if validation fails; do not migrate skills automatically.
- **Security/example/evidence/maintenance:** Limit metadata to non-sensitive descriptions; approval required for breaking schema changes. Example: a skill author submits a missing description; validator rejects it with the field named. **Status:** partial-authoring guide and structural validator exist, but lifecycle/runtime compatibility evidence is absent. Recheck on platform schema changes.

## Source mapping

- Candidate ID: `01`
- Source status at discovery: `partial-authoring guide and structural validator exist, but lifecycle/runtime compatibility evidence is absent`
- Mapping evidence: `| 01 | Global Skills Framework | partial | Traceability row 01: global-system skill, authoring guide, validator | `skills/Skill - 129 - AI Agent Skills Tool Governance/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/skills-validation-versioning-and-release/SKILL.md`; `enterprise-ui-fullstack-skills/schemas/skill-metadata.schema.json` | Reconcile lifecycle, schema compatibility, and tested cross-platform conformance. |`
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

