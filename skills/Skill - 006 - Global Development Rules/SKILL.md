description: 'Execute the evidence-based candidate contract for Global Development Rules.'
---
id: global-development-rules
name: Skill - 006 - Global Development Rules
candidateIds: ["02"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: foundation
---

# Skill - 006 - Global Development Rules

## Purpose

This canonical instruction package implements the approved candidate contract for
**Global Development Rules**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Conflicting or missing cross-project rules produce unsafe and inconsistent work; define universal engineering and communication principles while allowing explicit local exceptions.
- **Behavior; activation/non-activation:** Resolve applicable rules at task start and surface conflicts; do not overwrite project policy or claim compliance absent evidence.
- **Inputs/tools/dependencies/handoff:** Repository instructions, security policy, task constraints, supported tools; document search and policy comparison; depends 01/57; hands applicable rules to every workflow.
- **Procedure/decision:** 1) Inventory global and local rules. 2) Group by code, tests, security, docs, tools, approvals. 3) Identify contradictions and authority. 4) If a local rule conflicts with a non-negotiable safety rule, stop and request decision; otherwise scope the exception.
- **Outputs/acceptance/failure:** Versioned rule set, precedence map, exception record; pass when every rule has scope and no unresolved conflict is presented as settled. Missing policy remains unknown.
- **Security/example/evidence/maintenance:** Never weaken permission controls through a style exception. Example: local instructions require tests, but a test command may mutate shared data; ask for safe test scope before running. **Status:** partial-root SECURITY, CONTRIBUTING, and AUTHORING guides exist, no unified precedence contract. Review when policies change.

## Source mapping

- Candidate ID: `02`
- Source status at discovery: `partial-root SECURITY, CONTRIBUTING, and AUTHORING guides exist, no unified precedence contract`
- Mapping evidence: `| 02 | Global Development Rules | partial | Traceability row 02: `SECURITY.md`, `CONTRIBUTING.md`, `AUTHORING_GUIDE.md` | `skills/Skill - 177 - Engineering Governance/SKILL.md`; `docs/sdlc/RISK_AND_APPROVAL_POLICY.md`; `orchestration/MASTER_ORCHESTRATOR.md` | Define precedence and project exceptions; policy text is not an enforcement mechanism. |`
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

