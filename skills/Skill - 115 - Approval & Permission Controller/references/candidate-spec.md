# Source candidate specification

- **Purpose/problem; goal/outcome:** Policy statements alone do not enforce least privilege; resolve authorization and gate actions with traceable scope.
- **Behavior; activation/non-activation:** Evaluate actor/action/resource/environment/approval; never infer permission from task context.
- **Inputs/tools/dependencies/handoff:** Identity, requested action, target, risk, approval record, policy; host auth/policy store; depends 02/24; gates 25–80.
- **Procedure/decision:** 1) Classify action and resource. 2) Verify actor permission and current approval conditions. 3) Allow only exact authorized scope and log outcome. 4) Deny/unknown/error defaults to blocked; request human resolution.
- **Outputs/acceptance/failure:** Allow/deny decision, scope, expiry, audit reference; pass when negative tests prove unauthorized actions are denied. Policy service outage fails closed.
- **Security/example/maintenance:** Protect identities and approvals; no privilege escalation. Example: staging approval cannot authorize production deploy. **Status:** partial—`SECURITY.md` mandates approvals, no enforcement controller found. Review policy and revocation tests.
