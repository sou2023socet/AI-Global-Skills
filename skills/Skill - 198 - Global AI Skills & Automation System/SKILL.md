---
name: Skill - 198 - Global AI Skills & Automation System
description: 'Use when planning, designing, governing, or implementing a reusable global AI skills and automation system, including staged skill catalogues, workflows, shared contracts, project knowledge, orchestration, and validation.'
---

# Skill - 198 - Global AI Skills & Automation System

## Purpose and Scope
Guide the staged discovery, design, implementation, and validation of a reusable AI skills and automation system across projects. Use the bundled [system blueprint](./references/GLOBAL_AI_SKILLS_BLUEPRINT.md) as the detailed source for the 80 candidate capabilities, deliverables, and stage prompts.

This skill coordinates the work; it does not represent the implementation of the 80 candidates. Keep the existing repository's conventions and single sources of truth. Do not generate placeholder skills or claim planned capabilities are implemented.

## Trigger Conditions
- The user wants to create or evolve a reusable global skills library or AI automation framework.
- The task involves a staged catalogue of skills, cross-project workflows, shared skill contracts, governance, or handover.
- The user asks to resume a previously approved phase of the bundled blueprint.

## Non-Trigger Conditions
- Do not use for authoring or fixing one ordinary domain skill that does not involve the global system; follow the repository's skill authoring guide instead.
- Do not use for a project-specific application feature, routine code review, or deployment unrelated to global skills.
- Do not advance to a later stage merely because its requirements are present in the blueprint.

## Prerequisites and Inputs
- The target global-skills repository and its instructions, existing skills, catalogues, validation tools, and current changes.
- The requested stage or outcome, if specified.
- The blueprint and any prior approved discovery, decisions, architecture, specifications, or implementation evidence.
- Explicit user approval before crossing a stage gate that requires review or before performing consequential actions.

## Execution Workflow
1. **Establish scope and state.** Identify the requested stage, repository, existing work, local conventions, current changes, and approval boundaries. Treat verified facts, assumptions, unknowns, and proposals distinctly.
2. **Apply the initial gate.** If the user has not approved a later stage, perform Stage 1 (workspace discovery) only: inspect read-only, make no file changes, and report findings before stopping.
3. **Resume only the authorized stage.** Use the corresponding prompt in the bundled blueprint. Confirm the prerequisite outputs and approvals exist; if not, report the blocker rather than skipping the gate.
4. **Preserve traceability.** Keep candidate IDs 01–80 and their original names traceable. Record proposed consolidations or dispositions separately; do not silently omit, rename, merge, or invent candidates.
5. **Work within stage scope.** Make only changes authorized for the current stage. Preserve useful repository content, avoid duplicate authoritative documents, and keep project-specific information and secrets out of global assets.
6. **Validate the stage.** Run relevant repository checks and verify required outputs. Report actual results, failures, blocked or unverified work, and remaining gaps. Never present a proposal as an implemented, verified, approved, or released capability.
7. **Stop at the gate.** Summarize the stage and next proposed action, then wait for the required review or approval before continuing.

## Commands and Examples
Use read-only discovery commands for Stage 1. Adapt paths to the actual workspace and exclude generated/vendor directories where appropriate.

```powershell
# Windows PowerShell: inspect a repository's top-level entries and skill folders
Get-ChildItem -LiteralPath 'E:\path\to\global-skills' -Force
Get-ChildItem -LiteralPath 'E:\path\to\global-skills\skills' -Directory
```

```bash
# POSIX shell: inspect a repository's top-level entries and skill folders
find /path/to/global-skills -maxdepth 1 -mindepth 1 -print
find /path/to/global-skills/skills -mindepth 1 -maxdepth 1 -type d -print
```

## Deliverables and Outputs
- Stage 1: a read-only workspace discovery report with verified findings, assumptions, unknowns, existing conventions, reusable assets, conflicts, risks, and recommended next steps.
- Later stages: only the documents, catalogue, specifications, architecture, implementation, tests, or handover explicitly authorized by the corresponding blueprint stage.
- A stage summary that distinguishes completed, failed, blocked, unverified, approved, and deferred work, and identifies the next gate.

## Quality Gates and Acceptance Criteria
- The work stays within the specifically requested and approved stage.
- Stage 1 creates or changes no files and installs no dependencies.
- Every candidate remains traceable; candidate counts and identifiers are checked when the stage requires them.
- Artifacts follow the target repository's actual conventions and pass its applicable validation.
- Evidence supports each reported outcome; missing tools, failed checks, and unverified claims are stated explicitly.
- Work stops for review at every required approval gate.

## Security and Safety Rules
- Use least privilege and read-only inspection until changes are authorized.
- Never expose, copy, or commit credentials, private project data, or secrets into global skills.
- Obtain explicit authorization before destructive, external, production, paid-resource, or otherwise consequential actions.
- Do not execute every phase automatically or infer approval from the presence of the blueprint.
- Preserve existing user changes; inspect diffs before editing and never discard unrelated work.
