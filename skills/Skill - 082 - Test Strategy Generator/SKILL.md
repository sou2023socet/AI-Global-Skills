description: 'Execute the evidence-based candidate contract for Test Strategy Generator.'
---
id: test-strategy-generator
name: Skill - 082 - Test Strategy Generator
candidateIds: ["34"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: quality
---

# Skill - 082 - Test Strategy Generator

## Purpose

This canonical instruction package implements the approved candidate contract for
**Test Strategy Generator**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Test level/environment choices are ad hoc; produce risk-based methods, data, priorities, and exit criteria.
- **Behavior; activation/non-activation:** Recommend coverage by risk and architecture; do not execute tests unless separately requested/approved.
- **Inputs/tools/dependencies/handoff:** Requirements, system boundaries, risk, toolchain, time constraints; test pyramid/checklist; depends 15/23/25/33; hands to 35-39.
- **Procedure/decision:** 1) Classify risks and testable behaviors. 2) Select unit/integration/system/security/performance levels. 3) Specify data/environment/isolation and evidence. 4) If required tool/environment is missing, propose fallback and mark coverage limitation.
- **Outputs/acceptance/failure:** Test strategy with priority, exit rules, owners; pass when high-risk acceptance has a planned method and safe target. No unsupported coverage promises.
- **Security/example/maintenance:** Production writes/load are excluded absent approval. Example: payment flow prioritizes deterministic unit/API tests with sandbox-only transaction. **Status:** partial-QA strategy skill. Review strategy after defects/architecture changes.

## Source mapping

- Candidate ID: `34`
- Source status at discovery: `partial-QA strategy skill`
- Mapping evidence: `| 34 | Test Strategy Generator | duplicate | Traceability row 34: QA strategy skill | `skills/Skill - 256 - Test Strategy Management/SKILL.md`; `docs/sdlc/TEST_AND_QUALITY_POLICY.md` | Reconcile test strategy guidance; add risk-based selection and exit evidence. |`
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

