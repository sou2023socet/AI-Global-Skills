description: 'Execute the evidence-based candidate contract for API & Database Specialist.'
---
id: api-and-database-specialist
name: Skill - 037 - API & Database Specialist
candidateIds: ["30"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: development
---

# Skill - 037 - API & Database Specialist

## Purpose

This canonical instruction package implements the approved candidate contract for
**API & Database Specialist**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** API/schema changes can diverge or corrupt data; coordinate contracts, persistence, transactions, validation, and migration.
- **Behavior; activation/non-activation:** Review both data and API effects; do not run destructive migrations or broaden access without approval.
- **Inputs/tools/dependencies/handoff:** Requirements, current schema/API, DB/version, data constraints; OpenAPI/SQL/migration tools; depends 19/20/23-26; hands to integration/testing/build.
- **Procedure/decision:** 1) Map consumer/provider fields and persistence ownership. 2) Design backward-compatible DTO/schema and migration. 3) Test empty/current data and failure/rollback paths. 4) If migration loses data or changes public contract incompatibly, require explicit approval and rollout plan.
- **Outputs/acceptance/failure:** Contract, migration, DTO/repository changes, compatibility evidence; pass when schema and payload tests agree and migration/recovery are reviewed. Block on unknown production data.
- **Security/example/maintenance:** Validate inputs, enforce row ownership, protect PII/secrets. Example: adding optional profile field preserves existing clients and migration defaults. **Status:** partial-separate API/database skills exist. Coordinate contract version changes.

## Source mapping

- Candidate ID: `30`
- Source status at discovery: `partial-separate API/database skills exist`
- Mapping evidence: `| 30 | API & Database Specialist | duplicate | Traceability row 30: API and database skills | `skills/Skill - 131 - API Contract Design/SKILL.md`; `skills/Skill - 159 - Database Data Architecture/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/rest-api-controller-and-contract-engineering/SKILL.md` | Preserve separate API/data ownership and add cross-layer transaction/compatibility contracts. |`
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

