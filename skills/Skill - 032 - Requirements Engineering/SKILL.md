description: 'Execute the evidence-based candidate contract for Requirements Engineering.'
---
id: requirements-engineering
name: Skill - 032 - Requirements Engineering
candidateIds: ["20"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: research-planning
---

# Skill - 032 - Requirements Engineering

## Purpose

This canonical instruction package implements the approved candidate contract for
**Requirements Engineering**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Vague requests produce incomplete work; create prioritized, testable functional/NFR requirements, constraints, and acceptance criteria.
- **Behavior; activation/non-activation:** Elicit and normalize requirements; do not implement or mark stakeholder approval without explicit authorization.
- **Inputs/tools/dependencies/handoff:** User needs, reconstructed evidence, constraints, stakeholders; requirements table/backlog; depends 10/16/19/24; hands to 22/23/26/33/49.
- **Procedure/decision:** 1) Identify actors/goals and boundaries. 2) Write atomic functional, quality, and constraint statements. 3) Add testable acceptance criteria and priority/dependency. 4) Resolve ambiguity with user; if unavailable, label assumption and block dependent commitment.
- **Outputs/acceptance/failure:** Versioned requirement set and traceability IDs; pass when each criterion is observable and scope is approved. Conflicts remain unresolved, not merged.
- **Security/example/evidence/maintenance:** Classify sensitive data/security requirements. Example: "calculator supports fractions" becomes accepted input, exact output, error case, and supported operations. **Status:** partial-SDLC provides traceability, not full elicitation. Change-controlled as user needs evolve.

## Source mapping

- Candidate ID: `20`
- Source status at discovery: `partial-SDLC provides traceability, not full elicitation`
- Mapping evidence: `| 20 | Requirements Engineering | duplicate | Traceability row 20: SDLC planning/traceability | `skills/Skill - 232 - Requirements Engineering (Legacy Source Record)/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/requirements-and-user-journey-engineering/SKILL.md` | Reconcile two direct requirements skills and retain recovery/user-journey specializations as modules. |`
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

