description: 'Execute the evidence-based candidate contract for Project Context Analyzer.'
---
id: project-context-analyzer
name: Skill - 011 - Project Context Analyzer
candidateIds: ["04"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: foundation
---

# Skill - 011 - Project Context Analyzer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Context Analyzer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Work begins with incomplete assumptions about code, dependencies, configuration, and docs; produce a bounded, evidence-linked project context baseline.
- **Behavior; activation/non-activation:** Analyze requested project scope and confidence; do not edit files or run unsafe commands during discovery-only use.
- **Inputs/tools/dependencies/handoff:** Canonical project path, task intent, relevant constraints; file/Git search, manifests, optional safe runtime facts; depends 03/73; hands evidence to 07-25.
- **Procedure/decision:** 1) Inspect instructions/status/manifests. 2) Map modules and relevant files. 3) Compare docs with code and record unknowns. 4) If scope is too large, narrow by task and disclose omissions; if identity is ambiguous, stop.
- **Outputs/acceptance/failure:** Context summary with citations, stack/modules, current changes, limitations; pass when each material claim has source evidence and secret values are redacted. Tool errors are explicit, not treated as absence.
- **Security/example/evidence/maintenance:** Read-only by default; never print secrets. Example: unfamiliar Angular repo yields package/runtime facts and unknown backend contract, not guessed routes. **Status:** partial-`project-discovery-audit` covers discovery but not normalized context freshness contract. Reassess sources as repo changes.

## Source mapping

- Candidate ID: `04`
- Source status at discovery: `partial-`project-discovery-audit` covers discovery but not normalized context freshness contract`
- Mapping evidence: `| 04 | Project Context Analyzer | duplicate | Traceability row 04: `skills/project-discovery-audit/SKILL.md` | `skills/Skill - 223 - Project Discovery Audit/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/project-discovery-and-design-audit/SKILL.md` | Compare overlapping discovery contracts; unify evidence/freshness model and keep design-specific adapters. |`
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

