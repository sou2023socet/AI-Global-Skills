description: 'Execute the evidence-based candidate contract for Parallel Agent Coordinator.'
---
id: parallel-agent-coordinator
name: Skill - 121 - Parallel Agent Coordinator
candidateIds: ["54"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: automation
---

# Skill - 121 - Parallel Agent Coordinator

## Purpose

This canonical instruction package implements the approved candidate contract for
**Parallel Agent Coordinator**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Parallel work can conflict on shared files or duplicated effort; divide independent tasks with isolated ownership and integration checks.
- **Behavior; activation/non-activation:** Delegate bounded independent tasks only; do not parallelize dependent traces or simultaneous edits to same files without coordination.
- **Inputs/tools/dependencies/handoff:** Task graph, files/resources, agent capabilities, shared-state constraints; task/agent system; depends 01/06/23/53/57; hands tasks via 55 and recovery via 56.
- **Procedure/decision:** 1) Identify independent work and shared resources. 2) Assign explicit scope, stop condition, output contract, and owner. 3) Integrate results and verify shared interfaces. 4) If conflict or agent failure occurs, pause dependent merges and preserve evidence.
- **Outputs/acceptance/failure:** Assignment map, results, conflict log; pass when no task overlap remains unresolved and combined result is validated. No agent capability â†’ serial fallback.
- **Security/example/maintenance:** Limit data/tool permissions per assignment. Example: one agent audits docs while another independently checks test config; code edits wait for integration owner. **Status:** proposed-no coordinator skill/runtime. Review conflict/quality metrics.

## Source mapping

- Candidate ID: `54`
- Source status at discovery: `proposed-no coordinator skill/runtime`
- Mapping evidence: `| 54 | Parallel Agent Coordinator | indirect | Traceability row 54: no dedicated parallel-coordination skill | `orchestration/MASTER_ORCHESTRATOR.md`; `orchestration/DEPENDENCY_GRAPH.md`; `skills/Skill - 178 - Engineering Orchestrator Continuous Improvement/SKILL.md` | Define ownership, conflict prevention, merge handoff, and verification only for supported agent platforms. |`
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

