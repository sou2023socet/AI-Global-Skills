description: 'Execute the evidence-based candidate contract for Deployment & Environment Engineer.'
---
id: deployment-and-environment-engineer
name: Skill - 092 - Deployment & Environment Engineer
candidateIds: ["47"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: delivery
---

# Skill - 092 - Deployment & Environment Engineer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Deployment & Environment Engineer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Deployment configuration is fragile or undocumented; prepare reproducible environment, configuration, health and rollback plans.
- **Behavior; activation/non-activation:** Design/validate deployment assets; do not deploy production unless separately authorized.
- **Inputs/tools/dependencies/handoff:** Target architecture, environment contracts, secrets mechanism, artifact, SLO; manifests/containers/infra validators; depends 23/25/30/38/39/42/46; hands plan to 48.
- **Procedure/decision:** 1) Map environment-specific config and dependencies. 2) Validate health/readiness/secrets/network boundaries. 3) Define migration order and rollback. 4) If target, credentials, or rollback are unverified, block execution.
- **Outputs/acceptance/failure:** Deployment plan/config and environment matrix; pass when config is reproducible, secrets externalized, health/rollback criteria explicit. Validation failures retain existing config.
- **Security/example/maintenance:** Least privilege, no secret logs, explicit production approval. Example: staging config uses secret references and restricted internal DB port. **Status:** partial-DevOps and deployment verification. Review config drift on release.

## Source mapping

- Candidate ID: `47`
- Source status at discovery: `partial-DevOps and deployment verification`
- Mapping evidence: `| 47 | Deployment & Environment Engineer | duplicate | Traceability row 47: DevOps and production verification | `skills/Skill - 200 - Hosting Platform Adapter/SKILL.md`; `skills/Skill - 149 - CI CD Infrastructure Automation/SKILL.md`; `skills/Skill - 164 - Deployment Live Service Verification/SKILL.md`; `skills/Skill - 218 - Production Environment Deployment Engineer/SKILL.md` | Separate deployment preparation from production execution and live verification. |`
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

