description: 'Execute the evidence-based candidate contract for Feature Implementation Agent.'
---
id: feature-implementation-agent
name: Skill - 049 - Feature Implementation Agent
candidateIds: ["28"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: development
---

# Skill - 049 - Feature Implementation Agent

## Purpose

This canonical instruction package implements the approved candidate contract for
**Feature Implementation Agent**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Feature changes lack consistent requirement-to-test trace; implement approved functionality with documentation and verified evidence.
- **Behavior; activation/non-activation:** Plan, modify, test, document within authorized scope; not for unapproved scope or generic operation that existing domain skill owns fully.
- **Inputs/tools/dependencies/handoff:** Approved requirement/acceptance, baseline status, repo conventions; editor, native test/build; depends 20/24-27; hands defects to 29/41 and evidence to 33/42.
- **Procedure/decision:** 1) Inspect callers/interfaces/current changes. 2) Plan minimal files/tests. 3) Implement and run focused checks. 4) If acceptance is ambiguous or tests expose unrelated baseline failures, pause and report rather than expanding scope.
- **Outputs/acceptance/failure:** Scoped diff, tests, doc updates and evidence; pass when criteria map to passing checks and no unrelated edits. Failure preserves diff and records diagnostics.
- **Security/example/evidence/maintenance:** No secrets; approval for side-effecting commands per policy. Example: approved export feature adds endpoint/UI/tests and an API doc entry. **Status:** partial domain skills exist, no generic feature agent. Keep stack specifics delegated.

## Source mapping

- Candidate ID: `28`
- Source status at discovery: `partial domain skills exist, no generic feature agent`
- Mapping evidence: `| 28 | Feature Implementation Agent | indirect | Traceability row 28: domain implementation skills; generic loop absent | `skills/Skill - 201 - Implementation Planner/SKILL.md`; `skills/Skill - 190 - Frontend Engineering (Legacy Source Record)/SKILL.md`; `skills/Skill - 140 - Backend Engineering (Legacy Source Record)/SKILL.md` | Define generic acceptance-to-change workflow only if needed; delegate stack work to specialists. |`
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

