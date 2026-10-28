description: 'Execute the evidence-based candidate contract for Continuous Improvement Planner.'
---
id: continuous-improvement-planner
name: Skill - 107 - Continuous Improvement Planner
candidateIds: ["70"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: maintenance
---

# Skill - 107 - Continuous Improvement Planner

## Purpose

This canonical instruction package implements the approved candidate contract for
**Continuous Improvement Planner**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Audits/feedback lack follow-through; convert verified outcomes into prioritized, measurable improvement plan.
- **Behavior; activation/non-activation:** Consolidate evidence-backed recommendations; do not turn ideas into approved commitments automatically.
- **Inputs/tools/dependencies/handoff:** Audit/incident/test/lesson results, objectives, capacity, owners; backlog/roadmap; depends 22/23/62-69; hands approved work to 22/78/80.
- **Procedure/decision:** 1) Deduplicate recommendations and trace evidence. 2) Rank by impact, effort, risk/dependencies. 3) Define owner, measure, target date and review. 4) If capacity/authority absent, mark proposed/deferred with reason.
- **Outputs/acceptance/failure:** Improvement roadmap and follow-up measures; pass when each item has evidence, metric and status. Unmeasurable item is returned for refinement.
- **Security/example/maintenance:** Aggregate sensitive incidents before planning. Example: reduce flaky test rate using baseline and target rather than broad "improve QA." **Status:** partial-SDLC/performance planning; no continuous loop. Reassess at agreed cadence.

## Phase I - Project structure and knowledge

## Source mapping

- Candidate ID: `70`
- Source status at discovery: `partial-SDLC/performance planning; no continuous loop`
- Mapping evidence: `| 70 | Continuous Improvement Planner | partial | Traceability row 70: planning/profiling skills | `skills/Skill - 178 - Engineering Orchestrator Continuous Improvement/SKILL.md`; `skills/Skill - 226 - Project Planning Traceability/SKILL.md` | Connect verified outcomes to owners, measurable improvement actions, and review dates. |`
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

