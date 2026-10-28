description: 'Execute the evidence-based candidate contract for Project Lifecycle Reassessment.'
---
id: project-lifecycle-reassessment
name: Skill - 113 - Project Lifecycle Reassessment
candidateIds: ["69"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: maintenance
---

# Skill - 113 - Project Lifecycle Reassessment

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Lifecycle Reassessment**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Project maturity/needs change; reassess stage, maintenance obligations, and next-stage recommendation from current evidence.
- **Behavior; activation/non-activation:** Compare lifecycle criteria over time; not a certification or release authorization.
- **Inputs/tools/dependencies/handoff:** Current status, goals, risk, support needs, lifecycle criteria; project history and health metrics; depends 06/15/61-65/68; hands to 22/70/78-80.
- **Procedure/decision:** 1) Confirm lifecycle model and evidence date. 2) Compare current vs prior stage criteria. 3) Identify unmet/changed constraints. 4) Recommend stage/maintenance change; owner decides transition.
- **Outputs/acceptance/failure:** Reassessment with evidence and alternatives; pass when criteria and freshness are stated. Missing signals yield "insufficient data."
- **Security/example/maintenance:** Restrict business/operational records. Example: end-of-support runtime shifts project from feature growth to migration planning. **Status:** partial-SDLC/discovery contain stage concepts, no recurring reassessor. Set review trigger.

## Source mapping

- Candidate ID: `69`
- Source status at discovery: `partial-SDLC/discovery contain stage concepts, no recurring reassessor`
- Mapping evidence: `| 69 | Project Lifecycle Reassessment | indirect | Traceability row 69: planning/discovery skills | `skills/Skill - 239 - SDLC Lifecycle Manager/SKILL.md`; `skills/Skill - 178 - Engineering Orchestrator Continuous Improvement/SKILL.md` | Define periodic maturity criteria and evidence-based reassessment decisions. |`
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

