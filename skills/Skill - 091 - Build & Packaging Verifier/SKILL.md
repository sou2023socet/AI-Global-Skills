description: 'Execute the evidence-based candidate contract for Build & Packaging Verifier.'
---
id: build-and-packaging-verifier
name: Skill - 091 - Build & Packaging Verifier
candidateIds: ["46"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: delivery
---

# Skill - 091 - Build & Packaging Verifier

## Purpose

This canonical instruction package implements the approved candidate contract for
**Build & Packaging Verifier**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** A claimed build/package may be unreproducible or wrong artifact; verify native build, packaging, and install procedure.
- **Behavior; activation/non-activation:** Execute approved local checks and identify artifact; not live deployment.
- **Inputs/tools/dependencies/handoff:** Build manifest, runtime, commit, expected artifact; project-native tools; depends 25/28-31/35/42; hands artifact to 47/48/50.
- **Procedure/decision:** 1) Inspect scripts and working tree. 2) Confirm exact build command and side effects/approval. 3) Run and record exit code/artifact hash/path. 4) On failure preserve logs; do not retry with changed flags without explanation/approval.
- **Outputs/acceptance/failure:** Build/package report with environment and artifact identity; pass only if command succeeded and artifact is present/valid. Missing tool or environment is blocked.
- **Security/example/maintenance:** No secrets in artifact/logs; builds may execute project code, so review scope. Example: package JAR with verified commit SHA and test result. **Status:** partial-backend/frontend/DevOps examples, no generic evidence process. Revalidate on toolchain changes.

## Source mapping

- Candidate ID: `46`
- Source status at discovery: `partial-backend/frontend/DevOps examples, no generic evidence process`
- Mapping evidence: `| 46 | Build & Packaging Verifier | duplicate | Traceability row 46: stack-specific build examples | `skills/Skill - 148 - Build Toolchain Manager/SKILL.md`; `skills/Skill - 138 - Artifact Release Builder/SKILL.md`; `skills/Skill - 145 - Build and Test Approval Gate/SKILL.md` | Compose native build/package procedures; report artifact identity/reproducibility; do not infer execution. |`
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

