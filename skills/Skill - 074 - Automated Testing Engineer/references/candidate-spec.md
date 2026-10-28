# Source candidate specification

- **Purpose/problem; goal/outcome:** Manual checks are not repeatable; create or maintain reliable automated verification and authentic evidence.
- **Behavior; activation/non-activation:** Use native runners and stable fixtures; not only manual UAT or a one-off unit test.
- **Inputs/tools/dependencies/handoff:** Scenarios, test framework/config, safe environment/data; browser/API/device/native runner; depends 25/31/33/34; results to 40–42.
- **Procedure/decision:** 1) Inspect current runner and fixture lifecycle. 2) Implement assertions that prove user outcome. 3) Run bounded suite and capture diagnostics. 4) If flaky/external dependency fails, isolate/classify; do not rerun repeatedly to manufacture a pass.
- **Outputs/acceptance/failure:** Reusable tests, command/results, artifacts, cleanup record; pass when deterministic outcomes and no leaked test data/processes. Failed runner remains failure.
- **Security/example/maintenance:** No production credentials or external side effects. Example: automated login-to-calculation workflow asserts response and visible result. **Status:** partial—new automation/unit skills are instruction-only; no test artifacts. Keep suite versioned.
