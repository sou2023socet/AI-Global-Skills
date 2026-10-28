description: 'Execute the evidence-based candidate contract for Dependency & Compatibility Monitor.'
---
id: dependency-and-compatibility-monitor
name: Skill - 109 - Dependency & Compatibility Monitor
candidateIds: ["64"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: maintenance
---

# Skill - 109 - Dependency & Compatibility Monitor

## Purpose

This canonical instruction package implements the approved candidate contract for
**Dependency & Compatibility Monitor**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Vulnerabilities/deprecations/compatibility breaks are found late; monitor dependencies and propose evidence-backed updates.
- **Behavior; activation/non-activation:** Compare lockfiles/versions to authoritative advisories/support matrices; do not auto-upgrade.
- **Inputs/tools/dependencies/handoff:** Manifests, allowed registries, runtime constraints, update policy; package audit/advisory feed if available; depends 17/25/57-59; hands risks to 19/22/25/63.
- **Procedure/decision:** 1) Inventory direct/transitive versions. 2) Check official advisories and compatibility. 3) Assess exploitability/upgrade path/test scope. 4) If feed stale, package unavailable, or major upgrade risky, label unknown and request decision.
- **Outputs/acceptance/failure:** Dated dependency report and staged recommendation; pass when each package is checked with source/date or explicit missing source. No auto-merge.
- **Security/example/maintenance:** Use trusted feeds; don't upload private lockfiles without authorization. Example: vulnerable transitive package requires compatible patch and regression plan. **Status:** proposed new monitor; discovery checks only. Refresh at approved cadence.

## Source mapping

- Candidate ID: `64`
- Source status at discovery: `proposed new monitor; discovery checks only`
- Mapping evidence: `| 64 | Dependency & Compatibility Monitor | duplicate | Traceability row 64: one-time discovery/configuration skills | `skills/Skill - 162 - Dependency Lifecycle Manager/SKILL.md`; `skills/Skill - 250 - Technology Watch Dependency Updates/SKILL.md`; `skills/Skill - 208 - Migration Upgrade Compatibility/SKILL.md` | Reconcile monitoring, upgrade planning, and compatibility checks; define source/advisory freshness. |`
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

