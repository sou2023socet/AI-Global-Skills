description: 'Apply the source-derived Safe Demo Data Seeding capability.'
---
id: safe-demo-data-seeding
name: Skill - 014 - Safe Demo Data Seeding
version: 1.0.0
status: structurally_validated
source: global-skills:skills\safe-demo-data-seeding\SKILL.md
---

# Skill - 014 - Safe Demo Data Seeding

## Purpose
Apply the reusable Safe Demo Data Seeding capability to the named project task without
silently expanding scope or permissions.

## Activation
- Activate when the task explicitly requires Safe Demo Data Seeding.
- Confirm project identity, scope, required evidence, and permission boundaries first.
- Do not activate for unrelated work or when a more specific canonical skill owns the task.

## Required procedure
1. Inspect the project context, applicable contracts, and existing implementation before acting.
2. Follow the source capability contract below, adapting examples to the actual project.
3. Record inputs, decisions, outputs, evidence, failures, and unresolved limitations.
4. Validate the acceptance criteria with the smallest approved check; never claim an unrun check.

## Failure handling
Stop on missing prerequisites, unknown project identity, unsafe permissions, or contradictory
evidence. Preserve partial work, report the exact blocker, and return control to the
orchestrator rather than inventing a successful result.

## Permissions
Read-only inspection is the default. File changes require task scope; execution, external
access, persistent writes, production impact, and generated artifacts require explicit
command-scoped approval.

## Acceptance criteria
- The requested capability is applied to the identified project and scope.
- Outputs are actionable, traceable to evidence, and free of secrets.
- Failures and unverified steps are explicit.

## Source capability contract

The following source-preserving contract is the basis for this canonical package:

# Safe Demo Data Seeding

## Purpose and Scope
Create realistic but synthetic, reproducible data that exercises a requested application flow. Keep data scoped to authorized non-production fixtures, support traceable cleanup, and preserve the application's validation and authorization rules.

## Trigger Conditions
- Populate a demo/test form, workflow, database fixture, or API request with representative values.
- Generate datasets for positive, negative, boundary, or end-to-end feature scenarios.
- Add test-only seed data or a reusable fixture builder.

## Non-Trigger Conditions
- Do not use for creating user identities or credentials; use `test-account-provisioning`.
- Do not use for production imports, migrations, or bulk customer-data operations.
- Do not use for arbitrary synthetic population without a defined feature or test purpose.

## Prerequisites and Inputs
- Feature contract, field constraints, relationships, and expected scenario outcomes.
- Confirmed non-production target and approved write/cleanup scope.
- Existing fixture, factory, seeder, or validation conventions.

## Execution Workflow
1. Inspect schemas, form validators, API DTOs, enums, relationships, and existing fixtures before choosing values.
2. Define datasets by purpose: valid typical, minimum/maximum boundary, optional-field omission, invalid/rejected, and relationship/state variations as relevant.
3. Use unmistakably synthetic values and unique run identifiers. Keep values internally consistent with domain rules; do not copy real users' data.
4. Prefer in-memory fixtures or transaction rollback. For persistent seeding, obtain command-scoped approval, then use a dedicated test profile/schema/namespace and an idempotent, run-scoped seed mechanism.
5. Validate generated data through the normal application validation layer; do not bypass constraints merely to force seed success.
6. Execute only the requested flow and record inputs without secrets or personal information.
7. Clean up only records created by the current run, using recorded IDs/run labels. Verify cleanup and do not use broad deletes.
8. Document the fixture schema, scenario mapping, execution result, and any uncleaned records or blocked cleanup.

## Commands and Examples
Inspect existing fixture conventions and schema definitions first:

```powershell
Get-ChildItem -Recurse -Include *Fixture*,*Factory*,*Seeder*,*Data.sql,*.json
```

```bash
find . -type f \( -iname '*fixture*' -o -iname '*factory*' -o -iname '*seeder*' -o -iname '*data.sql' -o -iname '*.json' \)
```

Use the project's documented test profile and seed command; never construct a production database command from these discovery examples.

## Deliverables and Outputs
- Synthetic fixture/data values and scenario-to-purpose mapping.
- Seed/run instructions and explicit target environment.
- Execution result plus run-scoped cleanup record.

## Quality Gates and Acceptance Criteria
- Data is synthetic, constraint-aware, and sufficient for the named feature scenarios.
- Setup is repeatable and isolated; rerunning does not create uncontrolled duplicates.
- Cleanup targets only resources created for the current run.
- Results and evidence do not contain sensitive user data or secrets.

## Security and Safety Rules
- Never seed production, public shared storage, or real customer accounts without explicit authorization and an approved import plan.
- Never include passwords, tokens, payment details, personal information, or real identifiers in demo fixtures.
- Require explicit approval before persistent writes or deletes in any shared environment.
- Avoid broad cleanup statements; verify target IDs/run labels before deleting.
