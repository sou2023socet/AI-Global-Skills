description: 'Apply the source-derived Unit Test Engineering capability.'
---
id: unit-test-engineering
name: Skill - 071 - Unit Test Engineering
version: 1.0.0
status: structurally_validated
source: global-skills:skills\unit-test-engineering\SKILL.md
---

# Skill - 071 - Unit Test Engineering

## Purpose
Apply the reusable Unit Test Engineering capability to the named project task without
silently expanding scope or permissions.

## Activation
- Activate when the task explicitly requires Unit Test Engineering.
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

# Unit Test Engineering

## Purpose and Scope
Create focused, repeatable unit tests that verify one unit's behavior at its public boundary. Isolate external dependencies while exercising real domain logic. This skill implements unit tests; use `qa-test-automation-strategy` to select the broader test pyramid and coverage strategy.

## Trigger Conditions
- Add or improve tests for a class, function, component, reducer, or service without exercising the full application.
- Diagnose flaky, order-dependent, or misleading unit tests.
- Add a regression test for a reproducible defect.

## Non-Trigger Conditions
- Do not use as the primary workflow for browser journeys, multi-service integration, or acceptance testing.
- Do not change production behavior merely to satisfy a test without establishing the intended contract.
- Do not treat line coverage alone as proof of correctness.

## Prerequisites and Inputs
- Target symbol and intended behavior, inferred from requirements and existing callers/tests.
- Project-native test runner and dependencies, discovered from manifests and configuration.
- Known baseline status; distinguish new failures from pre-existing failures.

## Execution Workflow
1. Inspect the target unit, its callers, neighboring tests, fixtures, and test configuration.
2. Write down observable behavior and input partitions: normal, boundary, empty/null, invalid, and error paths as applicable.
3. Use Arrange-Act-Assert or Given-When-Then. Keep each test focused on one behavior and make assertions on externally visible outcomes.
4. Keep domain logic real. Mock or fake only external boundaries such as network, clock, filesystem, database, or nondeterministic provider.
5. Avoid shared mutable state, test-order assumptions, arbitrary sleeps, broad snapshots, and implementation-detail assertions.
6. Add a regression case that fails on the defect and passes with the intended behavior. Do not weaken unrelated assertions.
7. Inspect the exact test command and its effects, then obtain command-scoped user approval before running it. Run the smallest relevant selector first; capture exact commands and results.
8. Review the diff for unnecessary production changes and report failures honestly.

## Commands and Examples
Discover and use the configured runner; examples below are patterns, not commands to assume:

```powershell
# Java/JUnit
mvn -Dtest=TargetTest test
# Python
python -m pytest tests/test_target.py -q
# JavaScript/TypeScript
# Angular CLI example; use the runner configured in the project
npm test -- --watch=false
```

```bash
# Java/JUnit
mvn -Dtest=TargetTest test
# Python
python -m pytest tests/test_target.py -q
# JavaScript/TypeScript
# Angular CLI example; use the runner configured in the project
npm test -- --watch=false
```

Use the selector supported by the actual project; do not add dependencies unless required and approved.

## Deliverables and Outputs
- Focused unit tests using existing project conventions.
- Test-run command, pass/fail output, and any baseline failures.
- Short explanation of behavior and boundaries covered.

## Quality Gates and Acceptance Criteria
- Tests are deterministic, isolated, and assert behavior rather than incidental implementation.
- New tests pass using the repository's native runner.
- Regression coverage fails before the fix when a reproducible defect can be demonstrated.
- No test depends on production credentials, external services, or execution order.

## Security and Safety Rules
- Never use production data, credentials, or endpoints in fixtures.
- Do not make tests perform real payments, emails, notifications, account changes, or destructive filesystem/database operations.
- Keep secrets out of test output and fixtures; use synthetic values and dedicated test configuration.
- Do not suppress failures or convert exceptions to success-shaped defaults.
