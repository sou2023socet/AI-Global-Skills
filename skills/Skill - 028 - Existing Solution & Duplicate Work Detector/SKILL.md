description: 'Execute the evidence-based candidate contract for Existing Solution & Duplicate Work Detector.'
---
id: existing-solution-and-duplicate-work-detector
name: Skill - 028 - Existing Solution & Duplicate Work Detector
candidateIds: ["18"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: research-planning
---

# Skill - 028 - Existing Solution & Duplicate Work Detector

## Purpose

This canonical instruction package implements the approved candidate contract for
**Existing Solution & Duplicate Work Detector**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Teams build capabilities already in code, tools, or another approved project; recommend reuse/build/retire with evidence.
- **Behavior; activation/non-activation:** Search current project and authorized reusable sources; do not copy code or assume another project's license/access.
- **Inputs/tools/dependencies/handoff:** Problem/requirements, canonical project registry, existing assets, reuse permissions; code search and registry; depends 03/04/17; hands decision to 19/22/28/60.
- **Procedure/decision:** 1) Search symbols, manifests, catalogs, and integrations. 2) Compare capability and constraints. 3) Verify ownership/license/maintenance. 4) Recommend reuse only if fit and rights are evidenced; otherwise mark candidate for evaluation.
- **Outputs/acceptance/failure:** Reuse-vs-build matrix with evidence and rationale; pass when search scope and exclusions are disclosed. Restricted projects are not searched.
- **Security/example/evidence/maintenance:** Keep project data isolated; no secret/code exfiltration. Example: existing CSV export covers format but lacks required access controls, so gap is explicit. **Status:** proposed workflow; discovery/search tools exist but no duplicate detector. Recheck before implementation.

## Source mapping

- Candidate ID: `18`
- Source status at discovery: `proposed workflow; discovery/search tools exist but no duplicate detector`
- Mapping evidence: `| 18 | Existing Solution & Duplicate Work Detector | partial | Traceability row 18: discovery and token-efficiency skills | `skills/Skill - 129 - AI Agent Skills Tool Governance/SKILL.md`; `orchestration/SKILL_ROUTING.md` | Add bounded cross-project search and evidence-backed reuse decisions; maintain project privacy. |`
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

