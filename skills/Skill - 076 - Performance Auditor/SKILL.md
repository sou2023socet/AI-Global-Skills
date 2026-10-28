description: 'Execute the evidence-based candidate contract for Performance Auditor.'
---
id: performance-auditor
name: Skill - 076 - Performance Auditor
candidateIds: ["39"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: quality
---

# Skill - 076 - Performance Auditor

## Purpose

This canonical instruction package implements the approved candidate contract for
**Performance Auditor**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Latency/resource issues lack reproducible measurement; locate bottlenecks and assess agreed targets.
- **Behavior; activation/non-activation:** Establish workload/baseline and profile; not a substitute for functional debugging or production load test approval.
- **Inputs/tools/dependencies/handoff:** SLO/target, workload, environment, baseline; profiler/metrics and safe load harness; depends 23/25/31/33/34; findings to 40/42/47.
- **Procedure/decision:** 1) Record environment and measurement noise. 2) Reproduce representative workload. 3) Profile bottleneck and compare target. 4) If no target/baseline exists, report measured facts and ask before optimizing to arbitrary threshold.
- **Outputs/acceptance/failure:** Reproducible report with workload, p50/p95/p99, resources and limits; pass against agreed threshold. Invalid/unstable measurements are inconclusive.
- **Security/example/maintenance:** No production load absent explicit approval; protect profiling data. Example: N+1 query measured locally and before/after counts attached. **Status:** partial-profiling skill, no actual benchmark evidence. Re-run after optimization.

## Source mapping

- Candidate ID: `39`
- Source status at discovery: `partial-profiling skill, no actual benchmark evidence`
- Mapping evidence: `| 39 | Performance Auditor | duplicate | Traceability row 39: profiling/scalability skill | `skills/Skill - 214 - Performance Scalability Engineering/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/frontend-performance-and-asset-optimization/SKILL.md` | Separate general profiling from frontend optimization; require workload, baseline, variance, and thresholds. |`
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

