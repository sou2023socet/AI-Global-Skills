description: 'Use this skill for Skill - 145 - Build and Test Approval Gate.'
---
name: Skill - 145 - Build and Test Approval Gate
---

# Skill - 145 - Build and Test Approval Gate

## Metadata
- Skill name and stable identifier: Build and Test Approval Gate (build-test-approval-gate)
- Version: 1.0.0
- Status: active
- Purpose and expected outcomes: Preserve user control over builds, tests, application runs, and generated artifacts by requiring clear, scoped approval before executing them and preventing unapproved repeat runs.
- Relevant project types and technology categories: All repositories and toolchains, including web, backend, mobile, desktop, data, cloud, and mixed-language projects.
- Trigger conditions: Use before any build, compile, test, package, install, application launch, benchmark, or other command that executes project code or generates build/test artifacts; use especially when the user says to wait, asks not to run, or limits repeated builds.
- Explicit non-trigger conditions: Read-only repository inspection, static file review, and preparing a proposed command list do not require this gate.
- Prerequisite skills: engineering-governance, project-discovery-audit
- Related skills: build-toolchain-manager, test-strategy-management, build-regression-verification, terminal-session-build-run-manager
- Required tools: Repository inspection tools and the project's normal build/test tools after approval.
- Optional tools: CI systems, static analysis, test reporting, and artifact inspection tools after approval.
- Risk classification: moderate
- Required permissions and approval conditions: Do not execute builds, tests, package/install commands, application runs, or artifact-producing verification unless the user explicitly approves the specific commands in the current task. A request to implement or inspect code is not approval to execute checks. Each approved command may run once; obtain fresh approval before any retry, rerun, additional build variant, or expanded test suite.

## Scope and boundaries
- Owns: The approval boundary and execution limits for build, test, run, package, and artifact-producing commands.
- Does not own: Choosing implementation details, deciding which tests are technically relevant, or authorizing production deployments.
- Read-only operations: Inspecting source, manifests, scripts, prior logs, and existing build outputs; drafting commands and estimated effects.
- Modifying operations: Creating or changing project source, tests, documentation, and configuration is governed by the user's implementation request and applicable project policies, not by build approval.
- Approval-required operations: Build, compile, test, package, install, run, benchmark, or otherwise execute project code or create generated build/test artifacts.
- Unverifiable operations: Any result that cannot be established without executing a command remains unverified and must be reported as such.

## Input discovery
- Identify the exact user request, any explicit execution restriction, and the current task's approval state.
- Determine which proposed commands compile, test, run, install, package, benchmark, or generate artifacts.
- Inspect existing scripts and prior outputs read-only to avoid proposing redundant checks.
- Define the minimum validation set that covers the requested change; group compatible checks into one proposed batch.
- State likely build outputs, side effects, required environment, and whether a failure would require a new approval to retry.

## Execution workflow
1. Inspect the project and determine the smallest useful validation set without executing it.
2. If execution was not explicitly requested, do not run any build, test, run, package, install, or artifact-generating command.
3. Present the exact commands, their order, expected artifact locations, and material side effects; request approval for this specific batch.
4. Treat approval as scoped to the named commands and one execution of each. Do not add commands, broaden coverage, or repeat a command under that approval.
5. Run only the approved commands, once each, and capture their actual results.
6. If a command fails, inspect its output and diagnose read-only; do not rerun or switch to another build/test command until separately approved.
7. Report completed, failed, skipped, and unverified checks separately, including any generated artifacts.

## Decision tables and conditional behavior
| Condition | Decision |
| --- | --- |
| User requests implementation but says nothing about running checks | Implement as requested; do not run checks. |
| User explicitly says not to run or to wait for approval | Do not execute build/test/run commands; continue only with permitted read-only work or edits. |
| User explicitly requests a named build/test command in this task | Treat that named command as approval for one run only. |
| User approves a proposed command batch | Run only the named commands, once each. |
| User approval is ambiguous or broad without a command scope | Ask which commands are approved; do not execute. |
| An approved command fails | Diagnose from output and request fresh approval before any retry or alternative validation command. |
| A second build, rerun, or broader suite is proposed | Request fresh, explicit approval even if a prior run was approved. |
| A result depends on a command that was not approved | Mark it unverified; do not imply the check passed. |

## Commands and examples
- Before an unrequested build, say: “I have not run a build or tests. I propose `<exact command>`; it will generate `<artifact path>`. May I run it once?”
- A clear approval such as “Run `npm run build` once” authorizes that command once in the current task.
- “Implement this” or “make the change” does not authorize builds, tests, package/install commands, or application launches.
- Do not trigger CI workflows or use another tool to execute a blocked build/test indirectly.
- Read-only checks of existing logs and artifacts are allowed; distinguish those from newly executed verification.

## Deliverables
- A precise proposed validation batch when approval is needed.
- The user's explicit approval scope, if granted, and the commands executed under it.
- Honest validation status and artifact locations; no success claims for skipped or unrun checks.

## Quality gates and acceptance criteria
- No execution occurred before explicit approval for the specific commands.
- Each approved command ran no more than once unless a later approval explicitly authorized a rerun.
- The batch was the smallest set sufficient for the stated validation goal.
- Build/test results and generated artifacts are reported accurately.
- Unrun verification is labeled as unverified, not passed.

## Failure handling and recovery
- If approval is missing or unclear, stop before execution and ask for precise approval.
- If execution is prohibited by the user, do not use an alternate runner, IDE task, CI workflow, or subagent to perform it.
- On failure, preserve the output and investigate it using read-only evidence.
- Before a retry, explain why it is needed, the exact command, and expected side effects; wait for fresh approval.
- If the environment starts a command unexpectedly, stop further execution when safe and report what ran and its status.

## Security and safety
- Do not expose secrets in command proposals, logs, or reports.
- Do not install dependencies or modify generated artifacts without the applicable approval.
- Do not bypass approval by launching builds through scripts, tasks, CI, agents, or indirect commands.
- Preserve existing user-generated artifacts and never clean them up unless separately approved.

## Inter-skill contracts
- Invoked by: master orchestrator and any skill that proposes builds, tests, runs, packages, installs, benchmarks, or generated validation artifacts.
- Must be consulted by: build-toolchain-manager, test-strategy-management, build-regression-verification, and terminal-session-build-run-manager before execution.
- Required input: task request, execution restrictions, project validation needs, and candidate commands.
- Expected output: an approved one-time execution scope or a clear no-execution decision.
- Return control to the invoking skill after approval is granted or execution is blocked.

## Reusability and maintenance
- Keep approval scoped to the current task and named commands; never carry it over to a later task.
- Adapt artifact paths and command examples to the repository without weakening the approval boundary.
- When build/test policies change, update this skill and the linked orchestrator and execution skills together.

## Completion report
Provide a concise report stating:
- whether builds/tests/runs were requested, approved, executed, or deliberately skipped,
- the exact commands run and their status, if any,
- any generated artifact locations,
- what remains unverified and whether fresh approval is needed.
