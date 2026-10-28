description: 'Execute the evidence-based candidate contract for Environment & Dependency Manager.'
---
id: environment-and-dependency-manager
name: Skill - 048 - Environment & Dependency Manager
candidateIds: ["25"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: development
---

# Skill - 048 - Environment & Dependency Manager

## Purpose

This canonical instruction package implements the approved candidate contract for
**Environment & Dependency Manager**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Inconsistent runtimes/configuration prevent reproducible work; inventory environment and compatibility, then propose safe changes.
- **Behavior; activation/non-activation:** Inspect manifests, runtimes, env templates, and supported dependencies; do not install/update packages without explicit scope.
- **Inputs/tools/dependencies/handoff:** Project manifest, lockfiles, runtime requirements, target platform; version commands/package managers; depends 04/17/24; hands compatibility to 26-31/34-47.
- **Procedure/decision:** 1) Read manifests/lockfiles and installed tool versions. 2) Compare declared vs available requirements. 3) Trace incompatible/transitive constraints. 4) If remediation requires upgrade/install, present diff/risk/rollback and wait for approval.
- **Outputs/acceptance/failure:** Environment matrix and reproducibility plan; pass when required vs installed versions are distinguished. Missing tool is a blocker, not silently installed.
- **Security/example/evidence/maintenance:** Do not print secret env values; report variable names only. Example: expected Java 21 but runtime 17 results in blocked build recommendation. **Status:** partial-project discovery/DevOps/database instructions. Recheck on lockfile/runtime changes.

## Source mapping

- Candidate ID: `25`
- Source status at discovery: `partial-project discovery/DevOps/database instructions`
- Mapping evidence: `| 25 | Environment & Dependency Manager | duplicate | Traceability row 25: discovery, DevOps, and database skills | `skills/Skill - 180 - Environment Readiness/SKILL.md`; `skills/Skill - 162 - Dependency Lifecycle Manager/SKILL.md`; `skills/Skill - 153 - Configuration Secrets Manager/SKILL.md` | Separate environment readiness, dependency lifecycle, and secret/configuration management; share manifests. |`
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

