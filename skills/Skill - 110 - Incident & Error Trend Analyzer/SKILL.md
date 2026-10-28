description: 'Execute the evidence-based candidate contract for Incident & Error Trend Analyzer.'
---
id: incident-and-error-trend-analyzer
name: Skill - 110 - Incident & Error Trend Analyzer
candidateIds: ["65"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: maintenance
---

# Skill - 110 - Incident & Error Trend Analyzer

## Purpose

This canonical instruction package implements the approved candidate contract for
**Incident & Error Trend Analyzer**. It is reusable guidance, not an autonomous runtime or
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

- **Purpose/problem; goal/outcome:** Repeated incidents are handled individually; aggregate safe event data to identify recurring causes and prevention.
- **Behavior; activation/non-activation:** Normalize incidents/time windows and compare trends; not live incident response or surveillance.
- **Inputs/tools/dependencies/handoff:** Authorized incident/log data, taxonomy, retention, time range; approved log query/analysis; depends 06/41/58-59/63; hands root causes to 29/39/62/70.
- **Procedure/decision:** 1) Confirm access and redact identifiers. 2) Normalize categories and deduplicate events. 3) Compare rates/severity with baseline. 4) If sample size or logging is insufficient, report uncertainty, not trend.
- **Outputs/acceptance/failure:** Trend report with methods, sample limits, repeat patterns; pass when conclusions are reproducible and privacy-safe. Query errors or missing logs are visible.
- **Security/example/maintenance:** Minimize PII and restrict raw log access. Example: repeated timeout incidents cluster around one dependency after version change, hypothesis pending validation. **Status:** proposed; diagnostic skill handles individual RCA only. Reassess taxonomy.

## Source mapping

- Candidate ID: `65`
- Source status at discovery: `proposed; diagnostic skill handles individual RCA only`
- Mapping evidence: `| 65 | Incident & Error Trend Analyzer | indirect | Traceability row 65: single-incident diagnosis/profiling only | `skills/Skill - 205 - Logging Error Diagnostics/SKILL.md`; `skills/Skill - 212 - Observability Monitoring Alerting/SKILL.md`; `skills/Skill - 202 - Incident Response Root Cause/SKILL.md` | Add historical aggregation and privacy-preserving recurrence analysis; no trend engine found. |`
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

