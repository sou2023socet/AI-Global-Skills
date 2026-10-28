# Source candidate specification

- **Purpose/problem; goal/outcome:** Decisions and approvals are implicit or lost; capture who authorized what, scope, conditions, and expiry.
- **Behavior; activation/non-activation:** Identify decision gates and record explicit response; do not infer consent from silence or prior unrelated approval.
- **Inputs/tools/dependencies/handoff:** Proposed action/options, risk, affected target, user/owner response; approval record; depends 02/57; gates 20/22/26/47–50.
- **Procedure/decision:** 1) Classify reversible/destructive/external/production/paid action. 2) Present exact action, target, impact, rollback, alternatives. 3) Obtain explicit scoped approval/denial. 4) If scope changes or approval expires, re-request; never proceed on ambiguity.
- **Outputs/acceptance/failure:** Decision record and gated task state; pass when action matches approval exactly. Missing owner/response marks BLOCKED.
- **Security/example/evidence/maintenance:** Least privilege and auditable, privacy-aware records. Example: approval for a staging migration does not authorize production. **Status:** partial—policy and text gates exist; no decision ledger/enforcement. Review approvals before execution.

## Phase D — Development
