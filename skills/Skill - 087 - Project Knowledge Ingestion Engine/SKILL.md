description: 'Execute the evidence-based candidate contract for Project Knowledge Ingestion Engine.'
---
id: project-knowledge-ingestion-engine
name: Skill - 087 - Project Knowledge Ingestion Engine
candidateIds: ["73"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: project-knowledge
---

# Skill - 087 - Project Knowledge Ingestion Engine

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Knowledge Ingestion Engine**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Relevant files/docs are scattered and unindexed; ingest authorized sources into searchable, source-linked knowledge with freshness.
- **Behavior; activation/non-activation:** Select, parse, redact and index allowed sources; not scrape arbitrary systems or train models on project data.
- **Inputs/tools/dependencies/handoff:** Project/source allowlist, permissions, formats, retention; file/API parsers and index; depends 02/03/57/72; hands context to 04/60/74-77.
- **Procedure/decision:** 1) Validate source authorization and sensitivity. 2) Extract text/metadata and provenance. 3) Redact/exclude restricted content and index. 4) If format/parser loses context or permission unclear, skip and report.
- **Outputs/acceptance/failure:** Source index with hash/path/date/access class; pass when retrieval returns citations and stale updates are detectable. Parser error is not silent omission.
- **Security/example/maintenance:** No credential ingestion; access control and deletion propagation required. Example: index Markdown and source paths, excluding `.env` and build outputs. **Status:** proposed new capability; project audit performs manual discovery. Review source allowlist and refresh.

## Source mapping

- Candidate ID: `73`
- Source status at discovery: `proposed new capability; project audit performs manual discovery`
- Mapping evidence: `| 73 | Project Knowledge Ingestion Engine | missing | Traceability row 73: discovery only, no ingestion/indexer | `skills/Skill - 223 - Project Discovery Audit/SKILL.md` is adjacent only | Specify authorized source adapters, provenance, redaction, indexing, refresh, and permission model first. |`
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

