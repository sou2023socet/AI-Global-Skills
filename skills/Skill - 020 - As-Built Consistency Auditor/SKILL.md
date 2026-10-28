description: 'Execute the evidence-based candidate contract for As-Built Consistency Auditor.'
---
id: as-built-consistency-auditor
name: Skill - 020 - As-Built Consistency Auditor
candidateIds: ["14"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: recovery
---

# Skill - 020 - As-Built Consistency Auditor

## Purpose

This canonical instruction package implements the approved candidate contract for
**As-Built Consistency Auditor**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Requirements, implementation, behavior, tests, diagrams, and docs may contradict; create a traceable discrepancy report.
- **Behavior; activation/non-activation:** Cross-check matched artifacts and classify mismatch; do not resolve architectural conflicts silently.
- **Inputs/tools/dependencies/handoff:** Requirements and context, code/runtime/tests/docs/diagrams; search, test output and link checker; depends 06/09-13; sends lifecycle gaps to 15 and changes to 40/62.
- **Procedure/decision:** 1) Build requirement-to-evidence rows. 2) Compare each artifact's claims. 3) Classify mismatch (code, test, docs, unknown) and impact. 4) Request decision where expected truth is ambiguous.
- **Outputs/acceptance/failure:** Discrepancy matrix with source and owner; pass when all in-scope claims are checked or labeled unverified. Missing artifact is a gap, not a pass.
- **Security/example/evidence/maintenance:** Redact evidence; read-only audit unless separately approved fixes. Example: docs claim CSV export but no route/UI/test is found; report "not evidenced," not definitively absent. **Status:** partial-discovery/documentation drift checks. Re-run after release.

## Source mapping

- Candidate ID: `14`
- Source status at discovery: `partial-discovery/documentation drift checks`
- Mapping evidence: `| 14 | As-Built Consistency Auditor | partial | Traceability row 14: discovery and documentation skills | `skills/Skill - 223 - Project Discovery Audit/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/project-discovery-and-design-audit/SKILL.md` | Compose cross-source discrepancy tracking, severity, trace links, and closure evidence. |`
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

