# Source candidate specification

- **Purpose/problem; goal/outcome:** Failing tests are misattributed to code when caused by fixtures, environment, or flakiness; classify failure with evidence and safe recovery.
- **Behavior; activation/non-activation:** Analyze runner output and reproduction; do not rerun costly/destructive tests without approval.
- **Inputs/tools/dependencies/handoff:** Failure output, test/commit, environment, baseline; logs, runner, targeted reproduction; depends 06/35/40; hands code defects to 29, strategy issues to 34.
- **Procedure/decision:** 1) Preserve first failure/output. 2) Classify assertion/product, test, environment, dependency, flaky, unknown. 3) Compare baseline and isolate minimum case. 4) If rerun changes side effects/cost, ask; otherwise one bounded diagnostic rerun may be proposed.
- **Outputs/acceptance/failure:** Root-cause report with confidence and next action; pass when classification evidence and unresolved alternatives are explicit. Unknown remains unknown.
- **Security/example/maintenance:** Redact test data/secrets. Example: connection refused plus healthy unit tests maps to environment failure, not code fix. **Status:** partial—general diagnostic skill only. Track recurrent failure pattern.
