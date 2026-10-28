description: 'Execute the evidence-based candidate contract for Reverse Engineering & Code Archaeology.'
---
id: reverse-engineering-and-code-archaeology
name: Skill - 025 - Reverse Engineering & Code Archaeology
candidateIds: ["08"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: recovery
---

# Skill - 025 - Reverse Engineering & Code Archaeology

## Purpose

This canonical instruction package implements the approved candidate contract for
**Reverse Engineering & Code Archaeology**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Architecture and behavior are undocumented; reconstruct modules, call/data flows, dependencies, and likely design intent with confidence labels.
- **Behavior; activation/non-activation:** Trace symbols, config, tests, and runtime evidence; do not present naming-based inference as fact or modify code.
- **Inputs/tools/dependencies/handoff:** Repository, manifests, entry points, tests/logs, target question; search/LSP/call graph where available; depends 04/09; hands requirements/diagrams to 10/11.
- **Procedure/decision:** 1) Start at entry points and dependency manifests. 2) Trace callers/data/contracts in both directions. 3) Compare test/runtime evidence to inferred intent. 4) If tooling cannot resolve dynamic behavior, mark the trace incomplete and request runtime evidence.
- **Outputs/acceptance/failure:** As-built map, symbol/file citations, confidence and unknowns; pass when cited paths support each important edge. Missing LSP/index is recorded, not simulated.
- **Security/example/evidence/maintenance:** Avoid exposing secret config; inspect redacted examples. Example: controllerâ†’serviceâ†’repository path is documented, while untested external callback stays unknown. **Status:** partial-project discovery and architecture design help but no archaeology protocol. Refresh after structural changes.

## Source mapping

- Candidate ID: `08`
- Source status at discovery: `partial-project discovery and architecture design help but no archaeology protocol`
- Mapping evidence: `| 08 | Reverse Engineering & Code Archaeology | partial | Traceability row 08: discovery and architecture skills | `skills/Skill - 223 - Project Discovery Audit/SKILL.md`; `skills/Skill - 136 - Architecture Design/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/architecture-diagram-and-flow-documentation/SKILL.md` | Add static/dynamic tracing, evidence confidence, unknown tracking, and as-built outputs. |`
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

