description: 'Execute the evidence-based candidate contract for Project Learning & Lessons Manager.'
---
id: project-learning-and-lessons-manager
name: Skill - 112 - Project Learning & Lessons Manager
candidateIds: ["68"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: maintenance
---

# Skill - 112 - Project Learning & Lessons Manager

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Learning & Lessons Manager**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Lessons are lost or overgeneralized; retain verified, reusable insights with scope and expiry.
- **Behavior; activation/non-activation:** Capture successful/failed approaches and applicability; do not store transient personal data or infer causality from one event.
- **Inputs/tools/dependencies/handoff:** Project outcome, evidence, owner consent, privacy/retention rules; lessons record/store; depends 06/58/63-67; informs 18/60/70/76.
- **Procedure/decision:** 1) Link lesson to evidence/outcome. 2) State context and limits. 3) Obtain approval for cross-project reuse and redact. 4) If evidence is anecdotal or sensitive, keep scoped or defer.
- **Outputs/acceptance/failure:** Searchable lesson record with provenance and review date; pass when lesson is actionable and scoped. Storage/consent failure prevents reuse.
- **Security/example/maintenance:** Project isolation, secret removal, retention limits. Example: a test fixture pattern generalized only after owner approves and removes project identifiers. **Status:** partial-handover principles only. Validate applicability before each reuse.

## Source mapping

- Candidate ID: `68`
- Source status at discovery: `partial-handover principles only`
- Mapping evidence: `| 68 | Project Learning & Lessons Manager | indirect | Traceability row 68: handover/planning guidance | `skills/Skill - 178 - Engineering Orchestrator Continuous Improvement/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/project-continuity-and-change-impact-management/SKILL.md` | Define opt-in verified lesson records, applicability, retention, privacy, and project isolation. |`
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

