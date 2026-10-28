description: 'Execute the evidence-based candidate contract for Technical Research Agent.'
---
id: technical-research-agent
name: Skill - 035 - Technical Research Agent
candidateIds: ["17"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: research-planning
---

# Skill - 035 - Technical Research Agent

## Purpose

This canonical instruction package implements the approved candidate contract for
**Technical Research Agent**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Decisions rely on stale or unsupported technical claims; deliver cited, date/version-aware research and alternatives.
- **Behavior; activation/non-activation:** Search official docs and primary sources; do not invent citations or claim currentness without retrieval date.
- **Inputs/tools/dependencies/handoff:** Question, constraints, current versions, source access; web/docs retrieval if available; depends 16/19; hands evidence to 19/20/25/51.
- **Procedure/decision:** 1) Convert question into verifiable claims. 2) Search primary/vendor/spec sources first. 3) Compare versions, limitations, and alternatives. 4) If sources conflict or are inaccessible, state uncertainty and do not recommend as fact.
- **Outputs/acceptance/failure:** Cited research brief with date, trade-offs, unknowns; pass when each material recommendation traces to a source. No source access â†’ blocked or limited, not fabricated.
- **Security/example/evidence/maintenance:** Avoid transmitting confidential project data to external search. Example: compare supported runtime versions from official release docs and cite dates. **Status:** proposed; research behavior is not a dedicated repository skill. Refresh when versions change.

## Source mapping

- Candidate ID: `17`
- Source status at discovery: `proposed; research behavior is not a dedicated repository skill`
- Mapping evidence: `| 17 | Technical Research Agent | indirect | Traceability row 17: no direct research skill | `skills/Skill - 250 - Technology Watch Dependency Updates/SKILL.md` | Extend source-quality, citation, date/version, alternatives, and uncertainty requirements; dependency watch alone is not research. |`
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

