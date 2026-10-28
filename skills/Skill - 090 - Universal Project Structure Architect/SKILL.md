description: 'Execute the evidence-based candidate contract for Universal Project Structure Architect.'
---
id: universal-project-structure-architect
name: Skill - 090 - Universal Project Structure Architect
candidateIds: ["71"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: project-knowledge
---

# Skill - 090 - Universal Project Structure Architect

## Purpose

This canonical instruction package implements the approved candidate contract for
**Universal Project Structure Architect**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Forced templates and ad hoc layouts hurt maintainability; recommend a structure suited to technology, scale, lifecycle, and existing conventions.
- **Behavior; activation/non-activation:** Inventory before recommending incremental structure; do not restructure solely to match a universal folder template.
- **Inputs/tools/dependencies/handoff:** Stack, team/workflows, current tree, build/test/import constraints; repository inventory and dependency graph; depends 04/08/19/20/25; hands to 26/72.
- **Procedure/decision:** 1) Map current modules and build boundaries. 2) Compare options against discoverability, coupling, tooling, team needs. 3) Identify migration risk and smallest change. 4) If no material benefit or migration risk dominates, recommend retain current layout.
- **Outputs/acceptance/failure:** Structure proposal/diagram and migration plan; pass when rationale and trade-offs are explicit. Missing code ownership blocks detailed design.
- **Security/example/maintenance:** Protect monorepo/private topology; migration requires approval. Example: preserve a small Angular app's current layout rather than introducing unnecessary packages. **Status:** partial-architecture/discovery skills. Revisit as scale changes.

## Source mapping

- Candidate ID: `71`
- Source status at discovery: `partial-architecture/discovery skills`
- Mapping evidence: `| 71 | Universal Project Structure Architect | duplicate | Traceability row 71: architecture/discovery guidance | `skills/Skill - 227 - Project Structure Manager/SKILL.md`; `universal-project-setup/SKILL.md` | Reconcile structure design with scaffolding/setup; keep recommendations non-prescriptive and migration-safe. |`
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

