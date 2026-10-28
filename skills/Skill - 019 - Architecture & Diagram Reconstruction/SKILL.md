description: 'Execute the evidence-based candidate contract for Architecture & Diagram Reconstruction.'
---
id: architecture-and-diagram-reconstruction
name: Skill - 019 - Architecture & Diagram Reconstruction
candidateIds: ["11"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: recovery
---

# Skill - 019 - Architecture & Diagram Reconstruction

## Purpose

This canonical instruction package implements the approved candidate contract for
**Architecture & Diagram Reconstruction**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Diagrams are missing or drifted; reconstruct architecture, sequences, deployments, data flow, and workflows from verified as-built evidence.
- **Behavior; activation/non-activation:** Model confirmed components and label inferred edges; do not design a replacement architecture unless asked.
- **Inputs/tools/dependencies/handoff:** Code/config/API/runtime evidence, audience and diagram type; repository search, Mermaid-capable Markdown; depends 08/10; hands to 19/26/43.
- **Procedure/decision:** 1) Identify components and evidence sources. 2) Trace each interaction/data boundary. 3) Render/validate syntax and reconcile contradictions. 4) If a connection is only inferred, annotate it or omit it.
- **Outputs/acceptance/failure:** Diagram plus legend/source notes; pass when all included edges have evidence and Mermaid renders. On unsupported renderer, provide source and mark rendering unverified.
- **Security/example/evidence/maintenance:** Redact topology/secrets where sensitive. Example: controller/service/database sequence diagram cites code entry points. **Status:** partial-architecture design and documentation skills provide diagram conventions but not reverse evidence. Revalidate after integration changes.

## Source mapping

- Candidate ID: `11`
- Source status at discovery: `partial-architecture design and documentation skills provide diagram conventions but not reverse evidence`
- Mapping evidence: `| 11 | Architecture & Diagram Reconstruction | duplicate | Traceability row 11: architecture and documentation skills | `skills/Skill - 136 - Architecture Design/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/architecture-diagram-and-flow-documentation/SKILL.md` | Define reverse mapping from code to diagrams and diagram consistency validation. |`
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

