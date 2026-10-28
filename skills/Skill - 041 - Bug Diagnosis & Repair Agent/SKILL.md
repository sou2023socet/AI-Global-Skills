description: 'Execute the evidence-based candidate contract for Bug Diagnosis & Repair Agent.'
---
id: bug-diagnosis-and-repair-agent
name: Skill - 041 - Bug Diagnosis & Repair Agent
candidateIds: ["29"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: development
---

# Skill - 041 - Bug Diagnosis & Repair Agent

## Purpose

This canonical instruction package implements the approved candidate contract for
**Bug Diagnosis & Repair Agent**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Symptom-only patches hide root causes; reproduce, isolate, fix, and prevent recurrence.
- **Behavior; activation/non-activation:** Diagnose a reported defect; distinguish from new feature, security review, or optimization.
- **Inputs/tools/dependencies/handoff:** Reproduction, logs, expected/actual, source, environment; debugger/log/test tools; depends 06/09/24/25; hands test failure to 41 and fix evidence to 40/42.
- **Procedure/decision:** 1) Reproduce and establish baseline. 2) Trace failure to root cause and impacted callers. 3) Add regression case and minimal fix. 4) If not reproducible, report evidence and ask for missing conditions; do not suppress exception as a fix.
- **Outputs/acceptance/failure:** RCA, patch, regression test, verification result; pass when test reproduces pre-fix and passes post-fix where feasible. Preserve failing baseline info.
- **Security/example/evidence/maintenance:** Redact logs, preserve authorization behavior. Example: invalid state returns 500; regression proves expected 4xx and error envelope. **Status:** partial-diagnostic skill covers RCA. Reopen if recurrence.

## Source mapping

- Candidate ID: `29`
- Source status at discovery: `partial-diagnostic skill covers RCA`
- Mapping evidence: `| 29 | Bug Diagnosis & Repair Agent | duplicate | Traceability row 29: diagnostic/RCA skill | `skills/Skill - 205 - Logging Error Diagnostics/SKILL.md`; `skills/Skill - 202 - Incident Response Root Cause/SKILL.md`; `skills/Skill - 229 - Refactoring Maintenance/SKILL.md` | Distinguish diagnosis from authorized repair; include impact analysis, regression evidence, and rollback. |`
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

