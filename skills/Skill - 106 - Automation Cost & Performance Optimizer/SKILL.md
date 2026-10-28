description: 'Execute the evidence-based candidate contract for Automation Cost & Performance Optimizer.'
---
id: automation-cost-and-performance-optimizer
name: Skill - 106 - Automation Cost & Performance Optimizer
candidateIds: ["67"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: maintenance
---

# Skill - 106 - Automation Cost & Performance Optimizer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Automation Cost & Performance Optimizer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Workflows waste calls, tokens, latency, or compute; measure and improve efficiency without weakening correctness/safety.
- **Behavior; activation/non-activation:** Analyze comparable metrics and bottlenecks; not optimize by dropping required validation or security checks.
- **Inputs/tools/dependencies/handoff:** Workflow traces, cost/latency baseline, quality outcomes; usage/telemetry tools; depends 06/39/53-59/66; hands changes to 52-55/70.
- **Procedure/decision:** 1) Define quality-preserving objective and baseline. 2) Find redundant waits/calls/context. 3) Pilot reversible optimization. 4) Reject changes that reduce evidence or safety even if cheaper.
- **Outputs/acceptance/failure:** Before/after measures with variance and quality results; pass when improvement is reproducible and quality non-regression holds. Missing telemetry is a limitation.
- **Security/example/maintenance:** Do not expose user prompts/secrets in traces. Example: cache stable metadata but recheck volatile Git status before editing. **Status:** partial-token efficiency/performance skills address different layers. Re-measure after tool changes.

## Source mapping

- Candidate ID: `67`
- Source status at discovery: `partial-token efficiency/performance skills address different layers`
- Mapping evidence: `| 67 | Automation Cost & Performance Optimizer | duplicate | Traceability row 67: token efficiency and profiling skills | `enterprise-ui-fullstack-skills/.github/skills/token-efficient-agent-workflows/SKILL.md`; `skills/Skill - 214 - Performance Scalability Engineering/SKILL.md`; `enterprise-ui-fullstack-skills/orchestration/TOKEN_EFFICIENCY_POLICY.md` | Define instrumentation/baselines for agent cost and latency; separate code performance from agent usage. |`
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

