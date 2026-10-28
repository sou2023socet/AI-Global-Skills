description: 'Execute the evidence-based candidate contract for Existing Project Recovery.'
---
id: existing-project-recovery
name: Skill - 022 - Existing Project Recovery
candidateIds: ["07"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: recovery
---

# Skill - 022 - Existing Project Recovery

## Purpose

This canonical instruction package implements the approved candidate contract for
**Existing Project Recovery**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Abandoned, damaged, or poorly understood projects lack a safe recovery path; recover a working baseline, prioritize blockers, and define a controlled plan.
- **Behavior; activation/non-activation:** Triage recovery state and preserve working functionality; do not overwrite, delete, or "repair" before snapshot/scope approval.
- **Inputs/tools/dependencies/handoff:** Project identity, user goal, current Git state, backups/runtime evidence; discovery, logs, tests, backups if authorized; depends 04/06; hands technical unknowns to 08-15, fixes to 29.
- **Procedure/decision:** 1) Record current status and protect uncommitted changes. 2) Inventory breakage, backups, dependencies, and reproducibility. 3) Rank reversible recovery options. 4) If data loss/destructive action is possible, stop for explicit approval and backup confirmation.
- **Outputs/acceptance/failure:** Recovery report, preserved baseline, sequenced actions/rollback points; pass when critical unknowns and non-restorable data are explicit. If backup integrity is uncertain, block restoration.
- **Security/example/evidence/maintenance:** Least privilege; never copy credentials to reports. Example: missing build dependency but source intact yields a reproducible environment plan, not a clean/reset. **Status:** partial-discovery and RCA exist separately; no recovery workflow. Review after each checkpoint.

## Source mapping

- Candidate ID: `07`
- Source status at discovery: `partial-discovery and RCA exist separately; no recovery workflow`
- Mapping evidence: `| 07 | Existing Project Recovery | partial | Traceability row 07: discovery and diagnostic/RCA skills | `skills/Skill - 223 - Project Discovery Audit/SKILL.md`; `skills/Skill - 230 - Reliability Fault Recovery/SKILL.md`; `skills/Skill - 202 - Incident Response Root Cause/SKILL.md` | Compose a recovery workflow with preservation checkpoints, exit criteria, and handover. |`
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

