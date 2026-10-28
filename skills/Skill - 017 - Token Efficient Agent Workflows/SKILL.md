description: 'Apply the source-derived Token Efficient Agent Workflows capability.'
---
id: token-efficient-agent-workflows
name: Skill - 017 - Token Efficient Agent Workflows
version: 1.0.0
status: structurally_validated
source: global-skills:skills\token-efficient-agent-workflows\SKILL.md
---

# Skill - 017 - Token Efficient Agent Workflows

## Purpose
Apply the reusable Token Efficient Agent Workflows capability to the named project task without
silently expanding scope or permissions.

## Activation
- Activate when the task explicitly requires Token Efficient Agent Workflows.
- Confirm project identity, scope, required evidence, and permission boundaries first.
- Do not activate for unrelated work or when a more specific canonical skill owns the task.

## Required procedure
1. Inspect the project context, applicable contracts, and existing implementation before acting.
2. Follow the source capability contract below, adapting examples to the actual project.
3. Record inputs, decisions, outputs, evidence, failures, and unresolved limitations.
4. Validate the acceptance criteria with the smallest approved check; never claim an unrun check.

## Failure handling
Stop on missing prerequisites, unknown project identity, unsafe permissions, or contradictory
evidence. Preserve partial work, report the exact blocker, and return control to the
orchestrator rather than inventing a successful result.

## Permissions
Read-only inspection is the default. File changes require task scope; execution, external
access, persistent writes, production impact, and generated artifacts require explicit
command-scoped approval.

## Acceptance criteria
- The requested capability is applied to the identified project and scope.
- Outputs are actionable, traceable to evidence, and free of secrets.
- Failures and unverified steps are explicit.

## Source capability contract

The following source-preserving contract is the basis for this canonical package:

# Token-Efficient Agent Workflows

## Purpose and Scope
Optimize context window consumption, eliminate prompt bloat, reduce inference latency, and minimize API token expenditure during autonomous agent sessions. Enforces progressive disclosure, targeted file inspection, deduplication of context, output clamping, and concise evidence reporting.

## Trigger Conditions
- Long-running multi-turn agent conversations approaching context limits.
- Tasks involving large repositories with thousands of files or heavy vendor directories (`node_modules`).
- Preventing tool output bloat from overwhelming model prompts.
- Designing high-efficiency agent system prompts and slash commands.
- Compacting conversation transcripts or summarizing historical context.

## Non-Trigger Conditions
- Do not trigger when detailed, line-by-line debugging output is explicitly requested by the user.
- Do not trigger for raw model training or hyperparameter optimization (use `mlops-llm-pipeline-engineering`).
- Do not trigger for database index optimization (use `database-architecture-migration`).

## Prerequisites and Inputs
- Active agent session context or conversational transcript.
- Target task objectives and acceptable output granularity.
- Access to context compacting or truncation mechanisms.

## Execution Workflow
1. **Targeted Discovery Over Broad Dumps**:
   - Never run unconstrained recursive directory traversals across entire file systems.
   - Strictly filter out vendor and build directories (`node_modules`, `target`, `dist`, `.git`, `__pycache__`).
   - Use line range offsets (`StartLine`, `EndLine`) when reading files rather than dumping entire 5,000-line files.
2. **Progressive Disclosure**:
   - Step 1: Read only the high-level outline, manifest, or table of contents.
   - Step 2: Read only the specific method, class, or section required for the task.
3. **Tool Output Clamping & Summarization**:
   - Limit tool output returned to the LLM to a hard cap (e.g. 4,000 characters).
   - If a tool returns a massive array or log, return structured summaries (e.g. counts, top 5 records) rather than raw dumps.
4. **Eliminate Redundant Tool Calls**:
   - Cache static inspection results (e.g. directory layout, installed tool versions) in memory rather than querying repeatedly within the same turn.
5. **Concise User Reporting**:
   - Avoid echoing large artifacts in conversational replies.
   - Direct the user to the generated file path or artifact, highlighting only key decisions, status, and open questions.

## Commands and Examples
```powershell
# High-efficiency targeted search: Exclude heavy directories
Get-ChildItem -Path . -Recurse -File | Where-Object {
    $_.FullName -notmatch "node_modules|target|dist|__pycache__"
} | Select-Object -First 20 FullName

# Read targeted line slice rather than entire file
Get-Content .\backend\pom.xml | Select-Object -First 30
```

## Deliverables and Outputs
- Bounded, high-signal conversational turns.
- Compacted context representations and summarized diagnostic logs.
- Reduced session token consumption and faster response latency.

## Quality Gates and Acceptance Criteria
- Context window consumption remains within optimal operational limits throughout multi-turn sessions.
- No redundant identical tool calls executed within the same trajectory.
- File reads target specific line ranges rather than loading entire multi-megabyte files into memory.

## Security and Safety Rules
- Truncation and clamping must preserve error messages and security finding summaries.
- Never omit security warnings in the interest of saving tokens.
