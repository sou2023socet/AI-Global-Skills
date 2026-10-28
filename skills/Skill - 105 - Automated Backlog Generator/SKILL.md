description: 'Execute the evidence-based candidate contract for Automated Backlog Generator.'
---
id: automated-backlog-generator
name: Skill - 105 - Automated Backlog Generator
candidateIds: ["62"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: maintenance
---

# Skill - 105 - Automated Backlog Generator

## Purpose

This canonical instruction package implements the approved candidate contract for
**Automated Backlog Generator**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Verified findings do not become actionable work; create deduplicated backlog candidates with acceptance and dependencies.
- **Behavior; activation/non-activation:** Transform issues/gaps/risks into proposed tasks; do not auto-approve, assign, or create external tickets without permission.
- **Inputs/tools/dependencies/handoff:** Evidence, severity, project backlog schema, priorities; issue/task API if authorized; depends 06/14/15/23/41/42/61/68; hands to 22/70/78.
- **Procedure/decision:** 1) Validate finding and source. 2) Search existing backlog duplicates. 3) Draft task with impact, acceptance, dependencies and owner suggestion. 4) Require review before publishing or committing priority.
- **Outputs/acceptance/failure:** Backlog candidates and traceability links; pass when each derives from verified evidence or is labeled idea. API unavailable leaves draft only.
- **Security/example/maintenance:** Remove sensitive reproduction details from broad tickets. Example: recurring failing contract test becomes a fix candidate linked to run ID. **Status:** partial-planning/RCA outputs, no backlog generator. Tune prioritization with owner feedback.

## Source mapping

- Candidate ID: `62`
- Source status at discovery: `partial-planning/RCA outputs, no backlog generator`
- Mapping evidence: `| 62 | Automated Backlog Generator | indirect | Traceability row 62: planning and RCA outputs | `skills/Skill - 201 - Implementation Planner/SKILL.md`; `skills/Skill - 249 - Technical Debt Management/SKILL.md` | Add verified finding-to-task conversion, deduplication, owner, priority, and evidence. |`
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

