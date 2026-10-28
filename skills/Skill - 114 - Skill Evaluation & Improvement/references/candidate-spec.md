# Source candidate specification

- **Purpose/problem; goal/outcome:** Skill quality is assumed from metadata; evaluate correctness, usefulness, reliability, cost and failures on controlled scenarios.
- **Behavior; activation/non-activation:** Maintain versioned fixtures and compare outcomes; do not use automated judge as sole release authority.
- **Inputs/tools/dependencies/handoff:** Skill versions, trigger/output contracts, representative and adversarial cases; validator, test harness, human review; depends 01/06/33–42/53/58; feedback to skill owner.
- **Procedure/decision:** 1) Separate static schema checks from behavior tests. 2) Execute safe scenarios including negative/ambiguous inputs. 3) Score required outputs, safety and regressions. 4) Failure blocks “verified”; propose targeted change and rerun same baseline.
- **Outputs/acceptance/failure:** Evaluation report, cases, metrics/version; pass when all required cases and security constraints meet threshold set by owner. Missing evaluator means unverified.
- **Security/example/maintenance:** No sensitive project data in fixtures. Example: prompt requiring approval must yield a stop, not execute. **Status:** partial—static validator only, no evaluation corpus. Review after skill edits/tool changes.
