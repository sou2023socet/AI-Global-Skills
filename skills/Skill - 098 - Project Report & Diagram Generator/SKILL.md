description: 'Execute the evidence-based candidate contract for Project Report & Diagram Generator.'
---
id: project-report-and-diagram-generator
name: Skill - 098 - Project Report & Diagram Generator
candidateIds: ["45"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: delivery
---

# Skill - 098 - Project Report & Diagram Generator

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Report & Diagram Generator**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Reports/diagrams are inconsistent with templates and evidence; produce accurate, presentation-ready artifacts without fabricated project facts.
- **Behavior; activation/non-activation:** Populate specified templates and cite evidence; do not invent dates, approvals, counts, or progress values.
- **Inputs/tools/dependencies/handoff:** Template, project evidence, audience, required format; doc generation/diagram tooling; depends 06/11/13/33/43; output to 49/50/76.
- **Procedure/decision:** 1) Map each template field to evidence. 2) Fill confirmed values and mark missing/confirmation-needed. 3) Validate layout, links, math/diagram syntax. 4) If required data is absent, leave explicit placeholder rather than estimate.
- **Outputs/acceptance/failure:** Reports, diagrams, evidence note and missing-field list; pass when all claims trace to source and output opens. Conversion errors are reported.
- **Security/example/maintenance:** Redact PII/secrets. Example: weekly report has missing meeting dates; marks "not supplied," not fabricated. **Status:** partial-docs skill supports reports/diagrams but no template engine. Validate each template revision.

## Source mapping

- Candidate ID: `45`
- Source status at discovery: `partial-docs skill supports reports/diagrams but no template engine`
- Mapping evidence: `| 45 | Project Report & Diagram Generator | partial | Traceability row 45: documentation and SDLC guidance | `enterprise-ui-fullstack-skills/.github/skills/architecture-diagram-and-flow-documentation/SKILL.md`; `templates/sdlc/LIFECYCLE_AND_TRACEABILITY_TEMPLATE.md` | Define report/diagram output contracts, evidence links, and renderer validation. |`
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

