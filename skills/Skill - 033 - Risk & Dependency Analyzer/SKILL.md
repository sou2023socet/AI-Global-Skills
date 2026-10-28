description: 'Execute the evidence-based candidate contract for Risk & Dependency Analyzer.'
---
id: risk-and-dependency-analyzer
name: Skill - 033 - Risk & Dependency Analyzer
candidateIds: ["23"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: research-planning
---

# Skill - 033 - Risk & Dependency Analyzer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Risk & Dependency Analyzer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Technical and schedule dependencies or risks surface late; make them visible with mitigation and ownership.
- **Behavior; activation/non-activation:** Trace technical, integration, security, operational, and schedule links; do not imply probability data where none exists.
- **Inputs/tools/dependencies/handoff:** Requirements, design, environment, schedule, external services; dependency graph and risk register; depends 11/17-20/25; hands to 22/26/42/47/48.
- **Procedure/decision:** 1) Identify dependency and risk events. 2) Record source, likelihood/impact basis, owner, mitigation, trigger. 3) Find critical path and single points. 4) Escalate intolerable/residual risk; do not approve it on behalf of owner.
- **Outputs/acceptance/failure:** Linked risk/dependency register; pass when material risks have evidence, owner, mitigation/status, or accepted decision. Unknowns remain open.
- **Security/example/evidence/maintenance:** Include data loss, secrets, availability and supply-chain risks. Example: provider availability blocks chatbot test; create contingency and evidence gate. **Status:** partial-SDLC and architecture mention risks; no register tool/evaluation tests. Reassess as dependencies change.

## Source mapping

- Candidate ID: `23`
- Source status at discovery: `partial-SDLC and architecture mention risks; no register tool/evaluation tests`
- Mapping evidence: `| 23 | Risk & Dependency Analyzer | duplicate | Traceability row 23: planning and architecture skills | `skills/Skill - 203 - Integration Dependency Mapping/SKILL.md`; `orchestration/DEPENDENCY_GRAPH.md`; `docs/sdlc/RISK_AND_APPROVAL_POLICY.md` | Share risk/dependency IDs, owners, confidence, and mitigation lifecycle across separate analyses. |`
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

