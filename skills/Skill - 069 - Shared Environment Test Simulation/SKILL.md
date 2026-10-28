description: 'Apply the source-derived Shared Environment Test Simulation capability.'
---
id: shared-environment-test-simulation
name: Skill - 069 - Shared Environment Test Simulation
version: 1.0.0
status: structurally_validated
source: global-skills:skills\shared-environment-test-simulation\SKILL.md
---

# Skill - 069 - Shared Environment Test Simulation

## Purpose
Apply the reusable Shared Environment Test Simulation capability to the named project task without
silently expanding scope or permissions.

## Activation
- Activate when the task explicitly requires Shared Environment Test Simulation.
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

# Shared Environment Test Simulation

## Purpose and Scope
Plan and execute authorized test simulations in environments shared by multiple developers, testers, or services. Protect shared state, preserve running processes, isolate test data where possible, and make impact visible. This skill covers safe coordination and execution, not production deployment.

## Trigger Conditions
- Run a test or realistic simulation in a shared dev, QA, staging, preview, or classroom environment.
- Verify behavior while multiple users or services may be using the same app or database.
- Need to test failure, concurrency, or recovery paths without disrupting other users.

## Non-Trigger Conditions
- Do not use for production release verification; use `production-deployment-verification`.
- Do not use for designing the overall testing pyramid; use `qa-test-automation-strategy`.
- Do not run load or destructive failure simulations without explicit environment-owner approval.

## Prerequisites and Inputs
- Confirmed target URL/environment, ownership or authorization, and permitted test window.
- Known test identity, data boundaries, rate limits, and cleanup expectations.
- Read access to project setup, test scripts, and health checks.

## Execution Workflow
1. Inspect manifests, environment configuration, running services, and existing test scripts. Never assume a local URL points to an isolated environment.
2. Identify shared resources: database/schema, queues, storage buckets, accounts, rate limits, and long-running processes. Record what the test will touch.
3. Confirm environment ownership and allowed operations. Obtain command-scoped approval before running tests or any writes, load, fault injection, process restarts, or cleanup that affects shared resources.
4. Prefer a dedicated test tenant, namespace, unique test prefix, transaction rollback, or disposable fixture. Use read-only checks first.
5. Use unique run IDs and synthetic data. Keep concurrency low; avoid overlapping another known test run.
6. Execute one scenario at a time; monitor application health and error output. Stop when impact exceeds the approved scope or unrelated users are affected.
7. Clean up only records/resources created by this run and explicitly approved for cleanup. Do not reset shared databases or stop services.
8. Report environment, timestamps, scenarios, results, side effects, cleanup, and any blocked checks. Never describe an unrun scenario as passed.

## Commands and Examples
Discover project commands rather than assuming a framework or endpoint:

```powershell
Get-Content package.json
Get-ChildItem -Force
```

```bash
cat package.json
find . -maxdepth 2 -type f
```

After confirming an approved health endpoint, a low-impact check can be run with:

```powershell
Invoke-WebRequest -Method Get -Uri $env:TEST_BASE_URL
```

```bash
curl --fail --silent --show-error "$TEST_BASE_URL"
```

Do not put credentials in command history or use write requests as health checks.

## Deliverables and Outputs
- A bounded test plan with target environment, scope, test data, approval, and cleanup.
- Execution record listing steps, expected and actual outcomes, PASS/FAIL/BLOCKED, and evidence.
- Impact and cleanup summary, including any shared-environment incidents.

## Quality Gates and Acceptance Criteria
- Environment identity and permissions are confirmed before mutations.
- Each executed scenario has observed evidence; blocked scenarios are explicitly labeled.
- Shared resources remain healthy; only run-created test data is cleaned up.
- No unrelated processes, accounts, or shared datasets are altered.

## Security and Safety Rules
- Never treat staging or a local URL as safe solely based on its name.
- Never test with real user data or production credentials.
- Do not perform load, destructive, fault-injection, restart, or broad cleanup actions without explicit approval from the environment owner.
- Stop on unexpected impact; preserve logs safely and notify the owner.
