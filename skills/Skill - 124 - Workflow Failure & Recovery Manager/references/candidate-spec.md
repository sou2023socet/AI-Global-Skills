# Source candidate specification

- **Purpose/problem; goal/outcome:** Interrupted workflows repeat side effects or lose progress; classify state and resume from verified checkpoints safely.
- **Behavior; activation/non-activation:** Recover failed/interrupted tasks; do not retry non-idempotent action automatically or conceal original failure.
- **Inputs/tools/dependencies/handoff:** Workflow/task ID, last checkpoint, logs, side effects, approval; audit/task state; depends 06/52–55/57–58; returns to orchestrator/owner.
- **Procedure/decision:** 1) Freeze/reconcile current external state. 2) Identify last verified checkpoint and actions with uncertain completion. 3) Resume only idempotent/reconciled work; otherwise request owner action. 4) Bound retries and retain original diagnostics.
- **Outputs/acceptance/failure:** Recovery decision, checkpoint, retry/rollback record; pass when no duplicate irreversible action occurs and remaining state is explicit. Unknown side effect blocks.
- **Security/example/maintenance:** Require fresh approval for changed/repeated consequential commands. Example: timeout after account creation requires existence check before retry. **Status:** partial—RCA and worker error state only. Test interruption/idempotency paths.
