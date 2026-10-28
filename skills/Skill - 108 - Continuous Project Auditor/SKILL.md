description: 'Execute the evidence-based candidate contract for Continuous Project Auditor.'
---
id: continuous-project-auditor
name: Skill - 108 - Continuous Project Auditor
candidateIds: ["63"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: maintenance
---

# Skill - 108 - Continuous Project Auditor

## Purpose

This canonical instruction package implements the approved candidate contract for
**Continuous Project Auditor**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** One-off audits miss trends and recurring drift; periodically assess code/dependencies/docs/security/lifecycle against baseline.
- **Behavior; activation/non-activation:** Run bounded authorized checks at approved cadence; not constant surveillance or unrestricted scanner execution.
- **Inputs/tools/dependencies/handoff:** Audit scope/cadence, baseline, policies, permissions; existing validators/scanners; depends 04/06/23/38-39/57-59; findings to 62/64-70.
- **Procedure/decision:** 1) Confirm scope, schedule and tool impact. 2) Compare current evidence with baseline. 3) Deduplicate and identify new/resolved/regressed items. 4) Pause when auth/tool changes or scope drifts.
- **Outputs/acceptance/failure:** Trend report with dates, gaps, exceptions; pass when checks and omitted areas are explicit. Failed scanner does not equal clean audit.
- **Security/example/maintenance:** Protect findings; no production tests absent approval. Example: dependency drift discovered across two scheduled manifests, with advisory date linked. **Status:** partial workflow across audit skills, no scheduler/baseline. Review cadence and false positives.

## Source mapping

- Candidate ID: `63`
- Source status at discovery: `partial workflow across audit skills, no scheduler/baseline`
- Mapping evidence: `| 63 | Continuous Project Auditor | duplicate | Traceability row 63: discovery, appsec, and performance skills | `skills/Skill - 223 - Project Discovery Audit/SKILL.md`; `skills/Skill - 134 - Application Security DevSecOps/SKILL.md`; `skills/Skill - 214 - Performance Scalability Engineering/SKILL.md` | Compose audit dimensions with cadence/authorization, baseline, dedupe, and trend evidence. |`
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

