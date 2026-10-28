description: 'Execute the evidence-based candidate contract for Real-World Problem Analyst.'
---
id: real-world-problem-analyst
name: Skill - 031 - Real-World Problem Analyst
candidateIds: ["16"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: research-planning
---

# Skill - 031 - Real-World Problem Analyst

## Purpose

This canonical instruction package implements the approved candidate contract for
**Real-World Problem Analyst**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Solutions are sometimes selected before user pain is understood; produce a falsifiable problem statement and measurable value hypothesis.
- **Behavior; activation/non-activation:** Ask/derive who is affected, workflow, frequency, impact, constraints, alternatives; do not present speculation as user research.
- **Inputs/tools/dependencies/handoff:** User statements, observations, domain evidence, stakeholders; interview notes and evidence table; depends 03/04; hands validated problem to 17/19/20/22.
- **Procedure/decision:** 1) Define users and current workflow. 2) Separate observed pain from assumptions. 3) Identify alternatives and measurable baseline. 4) If no evidence of a real problem/value, recommend discovery rather than implementation.
- **Outputs/acceptance/failure:** Problem brief, evidence/confidence, success measures, open questions; pass when affected user and falsifiable measure are stated. Missing stakeholder access is a limitation.
- **Security/example/evidence/maintenance:** Minimize personal data in research notes. Example: repeated manual report reconciliation becomes a time/error hypothesis with baseline still to measure. **Status:** proposed; no dedicated skill. Review assumptions with users before roadmap approval.

## Source mapping

- Candidate ID: `16`
- Source status at discovery: `proposed; no dedicated skill`
- Mapping evidence: `| 16 | Real-World Problem Analyst | missing | Traceability row 16: no direct skill | `skills/Skill - 232 - Requirements Engineering (Legacy Source Record)/SKILL.md` is adjacent only | Define user/problem evidence, value measures, falsification, and uncertainty before proposing a distinct skill. |`
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

