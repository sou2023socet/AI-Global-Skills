description: 'Use this skill for Skill - 180 - Environment Readiness.'
---
name: Skill - 180 - Environment Readiness
---

# Skill - 180 - Environment Readiness

## Metadata
- Skill name and stable identifier: Environment Readiness (environment-readiness)
- Version: 1.0.0
- Status: active
- Purpose and expected outcomes: Inspect OS, SDKs, runtimes, compilers, tools, ports, storage, network access, environment variables, and required services.
- Relevant project types and technology categories: Web, backend, APIs, mobile, desktop, data, cloud, AI, distributed systems, and mixed-language repositories; adapt to the actual stack before acting.
- Trigger conditions: Use this skill when the task clearly requires this capability or a downstream skill depends on it.
- Explicit non-trigger conditions: Do not activate for unrelated tasks or work already owned by a more specific skill.
- Prerequisite skills: engineering-governance, project-discovery-audit
- Related skills: engineering-governance, project-discovery-audit, requirements-engineering
- Required tools: repository inspection tools, manifests, tests, build tools, shells, and runtime access when needed.
- Optional tools: static analysis, security scanners, API test tools, cloud CLIs, and CI/CD tooling.
- Risk classification: moderate
- Required permissions and approval conditions: Read access is the minimum baseline. Production changes, deployments, secret rotation, migrations, and external infrastructure changes require explicit approval and rollback planning.

## Scope and boundaries
- Owns: discovery, design, implementation, verification, and reporting for this skill's domain.
- Does not own: unrelated work, broad refactors outside the task scope, or operations best handled by more specialized skills.
- Delegates to other skills: project-discovery-audit, requirements-engineering, architecture-design, build-toolchain-manager, test-strategy-management, and deployment-live-service-verification as required.
- Read-only operations: repository inspection, environment checks, dependency review, and documentation review.
- Modifying operations: file edits, configuration updates, build changes, scripts, and operational actions with project impact.
- Approval-required operations: production changes, migration, infrastructure changes, secret rotation, and externally costed actions.
- Unverifiable operations: any step contingent on unavailable credentials, network access, or production environment access.

## Input discovery
- Inspect manifests, repository layout, build scripts, CI/CD definitions, and documentation to understand the actual stack and constraints.
- Study the source code and tests to identify current behavior, patterns, and missing evidence.
- Review existing architecture, deployment docs, and issue context to confirm scope, assumptions, and approval boundaries.
- Discover runtime requirements, available tools, environment variables, network paths, and security constraints before acting.
- Confirm functional and non-functional requirements, acceptance criteria, and user intent from repo evidence or user input.

## Execution workflow
1. Preconditions: confirm the task and project context, then verify permissions and available tools.
2. Discovery and inspection: inventory the repository, toolchain, environment, and relevant docs for this skill.
3. Analysis: identify current state, constraints, risks, dependencies, and missing evidence.
4. Decision-making: choose the minimal safe workflow and document assumptions explicitly.
5. Implementation or operational actions: make the necessary change or operational step in small increments.
6. Error handling: capture failures, isolate the root cause, and address it without masking symptoms.
7. Verification: run the smallest relevant checks and inspect outputs before claiming success.
8. Documentation: record the decision, file paths, logs, and any unresolved blockers.
9. Handoff to dependent skills: pass the verified state and any required downstream actions.
10. Final reporting: summarize the work, what was checked, and what remains unverified.

## Decision tables and conditional behavior
| Condition | Decision |
| --- | --- |
| New project | Create a clean baseline and choose simple, maintainable patterns. |
| Existing project | Preserve working conventions and avoid unnecessary rewrites. |
| Supported environment | Proceed with project-native commands and validation. |
| Unsupported environment | Stop or adapt and document the limitation clearly. |
| Safe change | Implement incrementally and verify immediately. |
| Risky change | Require additional review, rollback planning, and explicit approval. |
| Passing checks | Continue to the next stage. |
| Failing checks | Diagnose the root cause and re-run the smallest relevant validation. |

## Commands and examples
- Inspect the actual project stack before selecting commands.
- Windows PowerShell examples:
  - Get-ChildItem -Recurse
  - Get-Content .\README.md
  - Get-Command mvn, gradle, npm, dotnet
- Bash examples:
  - ls -la
  - grep -R "TODO\|FIXME" .
  - which java mvn gradle npm
- Replace placeholders with actual paths or commands. Use destructive commands only when necessary and approved.

## Deliverables
- Updated documentation, configuration, code, tests, scripts, or operational guidance relevant to this skill.
- Evidence log showing the checks performed and their outcomes.
- Handoff notes for downstream skills or approvers.
- Files stored in the repository conventions or a clearly documented default location.

## Quality gates and acceptance criteria
- The task matches the scope of the skill without unowned overlap.
- Discovery and verification steps are complete enough to support the decision.
- The work is traceable to a requirement, architecture decision, or validated root cause.
- Results are evidenced by logs, tests, file inspection, or clearly labeled limitations.
- Any unverified step is reported honestly and not treated as complete.

## Failure handling and recovery
- Missing prerequisites: document the gap and request the required access or dependency before continuing.
- Tool failures: determine whether the issue is environmental, configuration-driven, or code-related.
- Permission problems: stop and ask for the required authorization or delegated action.
- Dependency conflicts: isolate the conflict and apply the smallest compatible change.
- Interrupted execution: preserve partial work and resume from the last verified state.
- Unresolved blockers: return the issue to the orchestrator with the exact blocker and the safe next step.

## Security and safety
- Avoid exposing secrets, tokens, private keys, or internal infrastructure details in logs or generated docs.
- Use least-privilege access for tools and external systems.
- Validate user input and operational boundaries before connecting to external services or running destructive commands.
- Require explicit approval for production, migration, or externally costly changes.
- Maintain an audit trail of key decisions and verification evidence.

## Inter-skill contracts
- Invoked by: project-discovery-audit, requirements-engineering, architecture-design, implementation-planner, build-toolchain-manager, deployment-live-service-verification, production-readiness-release-management, and the orchestrator.
- May invoke: toolchain, testing, documentation, security, release, and deployment skills as needed.
- Required input: task context, project state, environment constraints, available tools, and desired outcome.
- Expected output: a verified result, evidence, and relevant handoff details for the next step.
- Return control to the orchestrator when the work is complete, blocked, or requires additional approval.

## Reusability and maintenance
- Adapt examples to the actual project and avoid hardcoded assumptions about frameworks, repositories, or deployment targets.
- Keep the skill versioned and update examples when the stack changes.
- Refresh validation scenarios when dependencies or toolchain versions change.
- Keep the skill aligned with actual repository conventions and platform requirements.

## Completion report
Provide a concise final report with:
- what was implemented or analyzed,
- which checks were run,
- the observed results,
- any remaining limitations,
- the next required action,
- and whether the work is complete, partial, or blocked.

Use evidence, not assumptions, in every status statement.
