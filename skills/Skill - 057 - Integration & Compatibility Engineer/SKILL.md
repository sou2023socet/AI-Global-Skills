description: 'Execute the evidence-based candidate contract for Integration & Compatibility Engineer.'
---
id: integration-and-compatibility-engineer
name: Skill - 057 - Integration & Compatibility Engineer
candidateIds: ["31"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: development
---

# Skill - 057 - Integration & Compatibility Engineer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Integration & Compatibility Engineer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Individually working components fail across boundaries; verify contracts, versions, devices, services, and environments as a system.
- **Behavior; activation/non-activation:** Build compatibility matrix and test interactions; not a replacement for full architecture redesign.
- **Inputs/tools/dependencies/handoff:** Component versions, interfaces, deployment targets, test environment; API/browser/device/test tools; depends 09/25/26/30; hands defects to 29/35/40.
- **Procedure/decision:** 1) Identify component pairs and contract versions. 2) Prioritize supported combinations. 3) Execute bounded cross-boundary scenarios. 4) If target/tool is unavailable, mark combination unverified rather than infer compatibility.
- **Outputs/acceptance/failure:** Compatibility matrix and integration test results; pass only for tested combinations with evidence. Environment faults are classified separately.
- **Security/example/maintenance:** Authorized endpoints and synthetic data; external provider calls need approval/cost awareness. Example: Angular DTO + Spring endpoint + database path validated end-to-end. **Status:** partial-architecture/testing/mobile skills. Refresh on dependency or API version changes.

## Source mapping

- Candidate ID: `31`
- Source status at discovery: `partial-architecture/testing/mobile skills`
- Mapping evidence: `| 31 | Integration & Compatibility Engineer | duplicate | Traceability row 31: test, architecture, and platform skills | `skills/Skill - 203 - Integration Dependency Mapping/SKILL.md`; `skills/Skill - 132 - API Database Integration Testing/SKILL.md`; `skills/Skill - 208 - Migration Upgrade Compatibility/SKILL.md` | Compose integration tests and compatibility analysis with explicit platform/version matrix. |`
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

