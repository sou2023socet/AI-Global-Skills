description: 'Execute the evidence-based candidate contract for Skill Selection & Orchestration Engine.'
---
id: skill-selection-and-orchestration-engine
name: Skill - 122 - Skill Selection & Orchestration Engine
candidateIds: ["53"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: automation
---

# Skill - 122 - Skill Selection & Orchestration Engine

## Purpose

This canonical instruction package implements the approved candidate contract for
**Skill Selection & Orchestration Engine**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Agents invoke irrelevant or conflicting skills; route tasks to minimal compatible capabilities and coordinate handoffs.
- **Behavior; activation/non-activation:** Match intent, scope, dependencies, tools and risk; do not invent unavailable capabilities or override user instructions.
- **Inputs/tools/dependencies/handoff:** User request, registry/catalogue, project context, permissions; classifier/rules and status; depends 01/06/20/21/57; dispatches selected skills.
- **Procedure/decision:** 1) Classify task and exclusions. 2) Select smallest set that covers acceptance criteria. 3) Resolve ownership/dependencies and approval gates. 4) If conflict/uncertainty remains, ask or choose safe non-action; record routing reason.
- **Outputs/acceptance/failure:** Selection rationale, ordered calls, combined evidence; pass when every required task has owner and no duplicate side effects. Tool/capability mismatch blocks.
- **Security/example/maintenance:** Respect permissions and sensitive context boundaries. Example: a one-method test selects focused/unit testing, not full audit. **Status:** partial-global skill and token efficiency guide manual routing; no engine/tests. Evaluate with misroute/conflict cases.

## Source mapping

- Candidate ID: `53`
- Source status at discovery: `partial-global skill and token efficiency guide manual routing; no engine/tests`
- Mapping evidence: `| 53 | Skill Selection & Orchestration Engine | duplicate | Traceability row 53: global-system and token efficiency skills | `skills/Skill - 129 - AI Agent Skills Tool Governance/SKILL.md`; `skills/Skill - 178 - Engineering Orchestrator Continuous Improvement/SKILL.md`; `orchestration/SKILL_ROUTING.md` | Choose one routing contract and platform adapters; static routing docs are not a verified runtime engine. |`
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

