description: 'Execute the evidence-based candidate contract for Feasibility & Technology Evaluator.'
---
id: feasibility-and-technology-evaluator
name: Skill - 029 - Feasibility & Technology Evaluator
candidateIds: ["19"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: research-planning
---

# Skill - 029 - Feasibility & Technology Evaluator

## Purpose

This canonical instruction package implements the approved candidate contract for
**Feasibility & Technology Evaluator**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Technology decisions omit constraints, cost, compatibility, or operational risk; compare viable options and recommend with uncertainty.
- **Behavior; activation/non-activation:** Score options against agreed criteria; do not choose a vendor/technology on unstated preferences.
- **Inputs/tools/dependencies/handoff:** Requirements, research sources, constraints, environment/cost model; official docs, compatibility data, architecture review; depends 17/18/23/25; hands to 20/22/26.
- **Procedure/decision:** 1) Establish must-haves and weights with owner. 2) Eliminate incompatible options using cited facts. 3) Compare lifecycle cost, security, operations, scale, lock-in. 4) If criteria/weights change ranking materially, present sensitivity and ask.
- **Outputs/acceptance/failure:** Decision matrix and recommendation, risks and assumptions; pass when recommendation is reproducible and ties to requirements. Missing cost/source becomes explicit unknown.
- **Security/example/evidence/maintenance:** Do not transmit secrets to vendors. Example: compare queue frameworks against deployment constraints and team capability, not popularity. **Status:** partial-architecture/discovery skills support portions; no evaluator or scoring evidence. Review on constraints/version change.

## Source mapping

- Candidate ID: `19`
- Source status at discovery: `partial-architecture/discovery skills support portions; no evaluator or scoring evidence`
- Mapping evidence: `| 19 | Feasibility & Technology Evaluator | indirect | Traceability row 19: architecture and discovery skills | `skills/Skill - 136 - Architecture Design/SKILL.md`; `skills/Skill - 201 - Implementation Planner/SKILL.md` | Define comparable criteria, cost/constraints, scoring, and uncertainty; avoid implying a dedicated evaluator exists. |`
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

