description: 'Execute the evidence-based candidate contract for Security Auditor.'
---
id: security-auditor
name: Skill - 080 - Security Auditor
candidateIds: ["38"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: quality
---

# Skill - 080 - Security Auditor

## Purpose

This canonical instruction package implements the approved candidate contract for
**Security Auditor**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Security defects across code/config/dependencies are missed; perform authorized, evidence-based review with prioritized findings.
- **Behavior; activation/non-activation:** Review static and approved dynamic surfaces; not exploit third-party systems absent authorization or unbounded penetration testing.
- **Inputs/tools/dependencies/handoff:** Authorized scope, architecture, data classification, source/manifests; approved scanners and manual review; depends 02/23-25/31/33; findings to 29/32/42.
- **Procedure/decision:** 1) Confirm scope and exclusions. 2) Review auth, input, secrets, dependencies, data exposure and boundaries. 3) Validate safely and rate impact/confidence. 4) If proof needs risky access, stop and report unverified.
- **Outputs/acceptance/failure:** Private report with finding, evidence, impact, confidence, remediation; pass means review complete, not necessarily zero findings. Scanner errors disclosed.
- **Security/example/maintenance:** Never publish secrets/findings; follow disclosure policy and approvals. Example: source review finds missing owner check; report exact evidence without accessing another account. **Status:** partial-appsec skill and security policy exist; no scan results for candidate set. Reassess advisories.

## Source mapping

- Candidate ID: `38`
- Source status at discovery: `partial-appsec skill and security policy exist; no scan results for candidate set`
- Mapping evidence: `| 38 | Security Auditor | duplicate | Traceability row 38: appsec skill and root security policy | `skills/Skill - 134 - Application Security DevSecOps/SKILL.md`; `skills/Skill - 156 - Data Privacy Compliance/SKILL.md`; `enterprise-ui-fullstack-skills/.github/skills/security-privacy-and-data-governance/SKILL.md` | Preserve distinct threat/appsec/privacy roles; share safe findings/evidence and false-positive handling. |`
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

