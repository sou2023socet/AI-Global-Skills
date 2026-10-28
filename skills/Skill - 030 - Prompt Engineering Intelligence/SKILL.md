description: 'Execute the evidence-based candidate contract for Prompt Engineering Intelligence.'
---
id: prompt-engineering-intelligence
name: Skill - 030 - Prompt Engineering Intelligence
candidateIds: ["21"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: research-planning
---

# Skill - 030 - Prompt Engineering Intelligence

## Purpose

This canonical instruction package implements the approved candidate contract for
**Prompt Engineering Intelligence**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Ambiguous prompts cause rework and unsafe assumptions; improve instructions for clarity, completeness, output, and controllable execution.
- **Behavior; activation/non-activation:** Diagnose intent, constraints, missing facts, and output shape; do not alter meaning, add permissions, or execute a prompt-only request.
- **Inputs/tools/dependencies/handoff:** Original prompt, audience/model/tool constraints, expected deliverable; prompt checklist and bounded examples; depends 02/20; hands improved prompt to 53 or user.
- **Procedure/decision:** 1) Extract goal, constraints, context, exclusions. 2) Identify ambiguity and ask only material questions. 3) Rewrite with acceptance criteria and output format. 4) Compare to original; if intent changes, show the delta and request confirmation.
- **Outputs/acceptance/failure:** Revised prompt plus assumptions/questions; pass when all original constraints remain and output is testable. Missing context is requested or marked.
- **Security/example/evidence/maintenance:** Redact private data before external model use. Example: "make app better" becomes scoped accessibility review with routes, target devices, and evidence output. **Status:** partial-token efficiency handles context, not prompt correctness. Review effectiveness using authorized scenarios.

## Source mapping

- Candidate ID: `21`
- Source status at discovery: `partial-token efficiency handles context, not prompt correctness`
- Mapping evidence: `| 21 | Prompt Engineering Intelligence | duplicate | Traceability row 21: token-efficient and global-system skills | `skills/Skill - 129 - AI Agent Skills Tool Governance/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/token-efficient-agent-workflows/SKILL.md`; `enterprise-ui-fullstack-skills/orchestration/TOKEN_EFFICIENCY_POLICY.md` | Compare similar token/prompt guidance; define prompt evaluation separately from context efficiency. |`
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

