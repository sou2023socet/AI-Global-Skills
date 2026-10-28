# Source candidate specification

- **Purpose/problem; goal/outcome:** Symptom-only patches hide root causes; reproduce, isolate, fix, and prevent recurrence.
- **Behavior; activation/non-activation:** Diagnose a reported defect; distinguish from new feature, security review, or optimization.
- **Inputs/tools/dependencies/handoff:** Reproduction, logs, expected/actual, source, environment; debugger/log/test tools; depends 06/09/24/25; hands test failure to 41 and fix evidence to 40/42.
- **Procedure/decision:** 1) Reproduce and establish baseline. 2) Trace failure to root cause and impacted callers. 3) Add regression case and minimal fix. 4) If not reproducible, report evidence and ask for missing conditions; do not suppress exception as a fix.
- **Outputs/acceptance/failure:** RCA, patch, regression test, verification result; pass when test reproduces pre-fix and passes post-fix where feasible. Preserve failing baseline info.
- **Security/example/evidence/maintenance:** Redact logs, preserve authorization behavior. Example: invalid state returns 500; regression proves expected 4xx and error envelope. **Status:** partial—diagnostic skill covers RCA. Reopen if recurrence.
