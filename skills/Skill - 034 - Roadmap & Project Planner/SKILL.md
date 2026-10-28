description: 'Execute the evidence-based candidate contract for Roadmap & Project Planner.'
---
id: roadmap-and-project-planner
name: Skill - 034 - Roadmap & Project Planner
candidateIds: ["22"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: research-planning
---

# Skill - 034 - Roadmap & Project Planner

## Purpose

This canonical instruction package implements the approved candidate contract for
**Roadmap & Project Planner**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Approved goals lack executable sequence; create milestones, dependencies, estimates, deliverables, and stage gates.
- **Behavior; activation/non-activation:** Plan approved scope and show uncertain estimates; do not commit dates/owners/capacity without authority.
- **Inputs/tools/dependencies/handoff:** Approved requirements, constraints, capacity, risks, milestones; task/backlog format; depends 20/23/24; hands to 25-50/62/70/78.
- **Procedure/decision:** 1) Decompose outcomes into verifiable deliverables. 2) Connect prerequisites and critical path. 3) Estimate range with assumptions and risk. 4) If dependencies/authority/capacity are unknown, mark plan provisional and request owner confirmation.
- **Outputs/acceptance/failure:** Roadmap with milestones, acceptance, dependencies, risks, dates as ranges if uncertain; pass when every milestone has exit criteria. No hidden commitments.
- **Security/example/evidence/maintenance:** Keep private staffing/cost details restricted. Example: API contract precedes client integration and contract tests. **Status:** partial-SDLC roadmap/gates exist, detailed estimating and dependencies incomplete. Rebaseline on scope change.

## Source mapping

- Candidate ID: `22`
- Source status at discovery: `partial-SDLC roadmap/gates exist, detailed estimating and dependencies incomplete`
- Mapping evidence: `| 22 | Roadmap & Project Planner | duplicate | Traceability row 22: SDLC planning/governance | `skills/Skill - 226 - Project Planning Traceability/SKILL.md`; `skills/Skill - 201 - Implementation Planner/SKILL.md` | Separate roadmap, estimation, dependency critical path, and implementation planning with shared records. |`
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

