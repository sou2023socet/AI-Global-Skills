description: 'Execute the evidence-based candidate contract for Edge-Case & Randomized Testing.'
---
id: edge-case-and-randomized-testing
name: Skill - 075 - Edge-Case & Randomized Testing
candidateIds: ["36"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: quality
---

# Skill - 075 - Edge-Case & Randomized Testing

## Purpose

This canonical instruction package implements the approved candidate contract for
**Edge-Case & Randomized Testing**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Typical examples miss boundary/combination defects; generate bounded, reproducible edge and property-based cases.
- **Behavior; activation/non-activation:** Identify invariants, boundary partitions, random seed and shrinking; not unbounded fuzzing or unauthorized target probing.
- **Inputs/tools/dependencies/handoff:** Contract/invariants, input bounds, safe harness; native property/fuzz test library if already present; depends 20/33-35; findings to 29/40.
- **Procedure/decision:** 1) Derive boundary classes and invariants. 2) Set sample/time/size caps and fixed seed. 3) Run, shrink failures, retain reproducer. 4) If complexity or side effects exceed limits, stop and refine harness.
- **Outputs/acceptance/failure:** Edge matrix, property tests, seeds/reproducers; pass when bounds are enforced and failures replay deterministically. No seed/output means report limitation.
- **Security/example/maintenance:** Avoid resource-exhaustion payloads outside sandbox/approval. Example: randomly generated valid fractions preserve normalization and zero-denominator rejection. **Status:** proposed new skill; generic QA mentions boundaries only. Monitor flaky/expensive cases.

## Source mapping

- Candidate ID: `36`
- Source status at discovery: `proposed new skill; generic QA mentions boundaries only`
- Mapping evidence: `| 36 | Edge-Case & Randomized Testing | indirect | Traceability row 36: QA/unit boundary guidance | `skills/Skill - 256 - Test Strategy Management/SKILL.md`; `skills/Skill - 254 - Test Automation Engineering/SKILL.md` | Define seeded property-based testing, shrinking, replay, and bounded resource use; no dedicated capability found. |`
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

