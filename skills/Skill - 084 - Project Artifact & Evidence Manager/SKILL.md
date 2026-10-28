description: 'Execute the evidence-based candidate contract for Project Artifact & Evidence Manager.'
---
id: project-artifact-and-evidence-manager
name: Skill - 084 - Project Artifact & Evidence Manager
candidateIds: ["77"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: project-knowledge
---

# Skill - 084 - Project Artifact & Evidence Manager

## Purpose

This canonical instruction package implements the approved candidate contract for
**Project Artifact & Evidence Manager**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Reports, screenshots, builds and test logs are hard to trace or unsafe to retain; organize artifacts with provenance, access and lifecycle.
- **Behavior; activation/non-activation:** Register artifacts and references; do not copy/retain sensitive data without policy approval.
- **Inputs/tools/dependencies/handoff:** Artifact, owner, task, source, classification, retention; file store/index/hash; depends 02/06/57-58/72-73; serves 43-50/61/76/80.
- **Procedure/decision:** 1) Classify sensitivity and retention. 2) Record origin/hash/date/related claim. 3) Verify file/link/access. 4) If retention/access is unclear, keep only necessary reference or ask before copying.
- **Outputs/acceptance/failure:** Artifact index and integrity/access status; pass when links resolve and provenance is complete. Missing artifact is marked missing, not recreated fictitiously.
- **Security/example/maintenance:** Redact secrets/PII; enforce expiry and access control. Example: screenshot linked to test case with run date and redaction status. **Status:** proposed shared service; docs mention outputs without registry. Review retention and stale links.

## Phase J - Roadmap, releases, status, and next steps

## Source mapping

- Candidate ID: `77`
- Source status at discovery: `proposed shared service; docs mention outputs without registry`
- Mapping evidence: `| 77 | Project Artifact & Evidence Manager | indirect | Traceability row 77: documentation and global-system guidance | `skills/Skill - 174 - Documentation Knowledge Management/SKILL.md`; `templates/sdlc/LIFECYCLE_AND_TRACEABILITY_TEMPLATE.md` | Define artifact registry, provenance/integrity, access, retention, and project-specific boundaries. |`
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

