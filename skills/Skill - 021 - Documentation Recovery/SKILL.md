description: 'Execute the evidence-based candidate contract for Documentation Recovery.'
---
id: documentation-recovery
name: Skill - 021 - Documentation Recovery
candidateIds: ["13"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: recovery
---

# Skill - 021 - Documentation Recovery

## Purpose

This canonical instruction package implements the approved candidate contract for
**Documentation Recovery**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Useful documentation is missing, fragmented, or stale; reconstruct a sourced, usable baseline and uncertainty register.
- **Behavior; activation/non-activation:** Search docs/comments/manifests/tests and link claims to source; do not invent commands/features or rewrite authoritative content without scope.
- **Inputs/tools/dependencies/handoff:** Repository, existing doc locations, intended audience, available runtime evidence; file search, Markdown link check; depends 04/06/08; hands to 14/43-45.
- **Procedure/decision:** 1) Inventory canonical and orphan docs. 2) Compare statements to code/tests/runtime. 3) Draft missing sections with source citations and uncertainty labels. 4) If conflicts cannot be resolved, preserve both evidence and request owner decision.
- **Outputs/acceptance/failure:** Recovery index, proposed docs, discrepancy list; pass when links resolve and unsupported statements are removed or qualified. Tool failure becomes explicit gap.
- **Security/example/evidence/maintenance:** Remove secret values/PII. Example: reconstruct local setup only from manifest and verified scripts, marking missing environment variables. **Status:** partial-documentation engineering handles authoring/drift but no recovery provenance contract. Re-audit when code changes.

## Source mapping

- Candidate ID: `13`
- Source status at discovery: `partial-documentation engineering handles authoring/drift but no recovery provenance contract`
- Mapping evidence: `| 13 | Documentation Recovery | duplicate | Traceability row 13: documentation engineering | `skills/Skill - 174 - Documentation Knowledge Management/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/project-documentation-and-readme-engineering/SKILL.md` | Add fragmented-doc inventory, provenance, confidence, and completeness checks; preserve separate project adapters. |`
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

