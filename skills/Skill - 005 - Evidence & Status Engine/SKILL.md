description: 'Execute the evidence-based candidate contract for Evidence & Status Engine.'
---
id: evidence-and-status-engine
name: Skill - 005 - Evidence & Status Engine
candidateIds: ["06"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: foundation
---

# Skill - 005 - Evidence & Status Engine

## Purpose

This canonical instruction package implements the approved candidate contract for
**Evidence & Status Engine**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Status language conflates proposed, implemented, verified, accepted, and released; define evidence-linked claims and controlled status transitions.
- **Behavior; activation/non-activation:** Attach source and timestamp to status claims; do not generate evidence or assign a passed state from documentation alone.
- **Inputs/tools/dependencies/handoff:** Claim, artifact/tool output, owner, time, status transition; repository references and shared schema; depends 01/02; feeds all audits, readiness, dashboard, handover.
- **Procedure/decision:** 1) Classify claim and required evidence. 2) Validate artifact/command result and scope. 3) Set the least-advanced supported status. 4) If evidence is missing or stale, mark unverified/blocked and name the next check.
- **Outputs/acceptance/failure:** Evidence record, status vocabulary, transition report; pass when every completion claim is traceable and state distinctions remain intact. Missing evidence is a failed gate, not a success default.
- **Security/example/evidence/maintenance:** Redact sensitive artifacts and restrict access. Example: a skill folder exists but has no scenario test; status stays "implemented, unverified" or "partial," not "verified." **Status:** partial-status vocabulary exists in blueprint; no engine/schema. Review transition rules and evidence retention.

## Phase B - Project recovery and understanding

## Source mapping

- Candidate ID: `06`
- Source status at discovery: `partial-status vocabulary exists in blueprint; no engine/schema`
- Mapping evidence: `| 06 | Evidence & Status Engine | partial | Traceability row 06: global-system and SDLC status guidance | `skills/Skill - 226 - Project Planning Traceability/SKILL.md`; `templates/sdlc/LIFECYCLE_AND_TRACEABILITY_TEMPLATE.md` | Standardize provenance, freshness, status transitions, and evidence retention; no engine is verified. |`
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

