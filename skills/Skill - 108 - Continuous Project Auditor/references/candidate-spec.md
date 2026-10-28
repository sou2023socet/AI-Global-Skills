# Source candidate specification

- **Purpose/problem; goal/outcome:** One-off audits miss trends and recurring drift; periodically assess code/dependencies/docs/security/lifecycle against baseline.
- **Behavior; activation/non-activation:** Run bounded authorized checks at approved cadence; not constant surveillance or unrestricted scanner execution.
- **Inputs/tools/dependencies/handoff:** Audit scope/cadence, baseline, policies, permissions; existing validators/scanners; depends 04/06/23/38–39/57–59; findings to 62/64–70.
- **Procedure/decision:** 1) Confirm scope, schedule and tool impact. 2) Compare current evidence with baseline. 3) Deduplicate and identify new/resolved/regressed items. 4) Pause when auth/tool changes or scope drifts.
- **Outputs/acceptance/failure:** Trend report with dates, gaps, exceptions; pass when checks and omitted areas are explicit. Failed scanner does not equal clean audit.
- **Security/example/maintenance:** Protect findings; no production tests absent approval. Example: dependency drift discovered across two scheduled manifests, with advisory date linked. **Status:** partial workflow across audit skills, no scheduler/baseline. Review cadence and false positives.
