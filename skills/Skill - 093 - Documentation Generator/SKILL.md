description: 'Execute the evidence-based candidate contract for Documentation Generator.'
---
id: documentation-generator
name: Skill - 093 - Documentation Generator
candidateIds: ["43"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: delivery
---

# Skill - 093 - Documentation Generator

## Purpose

This canonical instruction package implements the approved candidate contract for
**Documentation Generator**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Technical docs are incomplete or inconsistent; create audience-specific, sourced artifacts from verified code and decisions.
- **Behavior; activation/non-activation:** Generate requested docs and examples; do not create phantom endpoints, setup steps, or compliance claims.
- **Inputs/tools/dependencies/handoff:** Audience, requirements, source code, actual commands, templates; Markdown/Mermaid/link checker; depends 06/10-13/20; hands to 44/45/50.
- **Procedure/decision:** 1) Identify canonical sources and audience. 2) Build outline against requirements. 3) Draft with source links and uncertainty labels. 4) If an example cannot be executed/verified, label it illustrative or omit it.
- **Outputs/acceptance/failure:** README/API/runbook/architecture docs per request; pass when links resolve, claims are evidenced, and secrets are absent. Renderer failure is recorded.
- **Security/example/maintenance:** Redact secrets/internal details. Example: endpoint docs include schema only after matching controller and tests. **Status:** partial-documentation-engineering skill exists; no generated artifact validation evidence. Regenerate on source changes.

## Source mapping

- Candidate ID: `43`
- Source status at discovery: `partial-documentation-engineering skill exists; no generated artifact validation evidence`
- Mapping evidence: `| 43 | Documentation Generator | duplicate | Traceability row 43: documentation engineering | `skills/Skill - 174 - Documentation Knowledge Management/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/project-documentation-and-readme-engineering/SKILL.md` | Define audience/source mapping and factuality checks; retain project-specific templates. |`
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

