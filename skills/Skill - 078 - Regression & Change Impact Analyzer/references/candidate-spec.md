# Source candidate specification

- **Purpose/problem; goal/outcome:** Changes break dependents that are not retested; map diff to affected behaviors and select regression coverage.
- **Behavior; activation/non-activation:** Analyze diff, callers, contracts and tests; do not claim full regression based on changed files only.
- **Inputs/tools/dependencies/handoff:** Base/head diff, dependency graph, requirements/tests; Git/search/LSP and test inventory; depends 06/28–33; hands tests to 35–39 and readiness to 42.
- **Procedure/decision:** 1) Identify changed symbols/contracts/data. 2) Trace downstream callers and user paths. 3) Rank tests by impact/risk. 4) If graph/tooling incomplete, add uncertainty and broaden or block test selection.
- **Outputs/acceptance/failure:** Change-impact map and regression plan/results; pass when changed public/data paths have rationale-backed coverage. Missing test is a gap.
- **Security/example/maintenance:** Avoid touching unrelated state. Example: DTO field change triggers API serialization and UI parsing tests. **Status:** partial—unit/refactor/test skills advise regressions, no impact engine. Keep test map current.
