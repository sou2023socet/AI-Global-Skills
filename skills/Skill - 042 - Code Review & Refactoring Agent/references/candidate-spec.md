# Source candidate specification

- **Purpose/problem; goal/outcome:** Defects, risky changes, duplication, and unnecessary diffs escape review; deliver prioritized findings and optional safe refactor plan.
- **Behavior; activation/non-activation:** Inspect diff for correctness/security/maintainability; do not silently make changes during review-only request.
- **Inputs/tools/dependencies/handoff:** Base/head diff, requirements, local standards, tests; Git diff and static analysis; depends 06/20/27/28; findings to 29/38/40.
- **Procedure/decision:** 1) Read scope and surrounding code. 2) Check requirement, edge/error paths, security, compatibility. 3) Rank actionable findings with evidence/confidence. 4) If no high-confidence issue, state review boundary; do not invent findings.
- **Outputs/acceptance/failure:** Findings with file/line/severity, rationale and fix suggestion; pass when all changed scope reviewed or limitations named. No automatic refactor.
- **Security/example/maintenance:** Protect sensitive code/logs and avoid public disclosure. Example: review detects missing ownership check in newly changed repository lookup. **Status:** partial—clean-code refactoring and appsec guidance, not review protocol. Preserve independent reviewer role where required.

## Phase E — Quality assurance
