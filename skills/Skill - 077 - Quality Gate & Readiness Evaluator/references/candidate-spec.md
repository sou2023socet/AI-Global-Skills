# Source candidate specification

- **Purpose/problem; goal/outcome:** Release decisions use incomplete or inconsistent evidence; provide ready/conditional/not-ready evaluation against agreed criteria.
- **Behavior; activation/non-activation:** Aggregate requirements/tests/security/docs/build/release evidence; do not waive criteria or release on behalf of owner.
- **Inputs/tools/dependencies/handoff:** Approved gates, status/evidence records, risks, release target; links to reports and CI results; depends 06/15/33–41/43; hands to 47–50.
- **Procedure/decision:** 1) Load gate criteria and evidence freshness. 2) Mark each pass/fail/blocked/missing/N/A. 3) Evaluate critical blockers and accepted risks. 4) Missing mandatory evidence means not-ready; conditional status requires named owner/expiry.
- **Outputs/acceptance/failure:** Gate report and recommendation; pass means all criterion results reconciled, not necessarily ready. Conflicting records are escalated.
- **Security/example/maintenance:** Private security findings remain access-controlled. Example: tests pass but migration rollback unverified → not ready for deployment. **Status:** partial—SDLC, security, deployment gates exist separately. Version thresholds with approved release policy.

## Phase F — Documentation and delivery
