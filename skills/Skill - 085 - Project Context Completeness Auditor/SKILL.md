description: 'Execute the evidence-based candidate contract for Project Context Completeness Auditor.'
---
id: project-context-completeness-auditor
name: Skill - 085 - Project Context Completeness Auditor
candidateIds: ["74"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: project-knowledge
---

# Skill - 085 - Project Context Completeness Auditor

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Context Completeness Auditor**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Agents act with insufficient context; determine whether evidence is adequate for a specific task and identify safe next steps.
- **Behavior; activation/non-activation:** Evaluate task-specific prerequisites and risk; not demand irrelevant exhaustive context.
- **Inputs/tools/dependencies/handoff:** Request, acceptance, repo state, evidence, tool availability, risk; context checklist; depends 04/06/72-73; gates 16-50/53/76.
- **Procedure/decision:** 1) Derive minimum facts needed for task. 2) Check each against current evidence/freshness. 3) Classify sufficient/partial/insufficient with safety-critical blockers. 4) If critical gap exists, ask or perform only safe discovery; do not execute consequential action.
- **Outputs/acceptance/failure:** Completeness report, missing facts, safe actions; pass when each gap has consequence and next action. Tool unavailable is explicit.
- **Security/example/maintenance:** Identify private data/permission gaps. Example: request to migrate DB without engine/version/backup confirmation is blocked. **Status:** proposed new skill; discovery notes unknowns but no task gate. Review checks for false blockers.

## Source mapping

- Candidate ID: `74`
- Source status at discovery: `proposed new skill; discovery notes unknowns but no task gate`
- Mapping evidence: `| 74 | Project Context Completeness Auditor | partial | Traceability row 74: discovery/unknown-reporting guidance | `skills/Skill - 223 - Project Discovery Audit/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/project-discovery-and-design-audit/SKILL.md` | Define task-specific sufficiency/confidence criteria and a safe next-action gate. |`
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

