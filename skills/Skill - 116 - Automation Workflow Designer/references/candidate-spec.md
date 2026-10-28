# Source candidate specification

- **Purpose/problem; goal/outcome:** Automation actions lack explicit triggers, checkpoints, and failure branches; design repeatable, bounded workflows.
- **Behavior; activation/non-activation:** Model trigger→conditions→actions→approvals→outputs; not a scheduler implementation or permission override.
- **Inputs/tools/dependencies/handoff:** Goal, events, actor, policies, dependencies, idempotency needs; workflow diagram/schema; depends 02/20/23/24/51/57; hands runtime to 53–59.
- **Procedure/decision:** 1) Define start condition and guards. 2) Specify action order, idempotency, timeout/retry, approval and compensation. 3) Model success/failure/disable paths. 4) If an action is unsafe to retry/compensate, require manual checkpoint.
- **Outputs/acceptance/failure:** Workflow spec/state diagram and test cases; pass when every transition has owner/result and duplicate-run behavior. Unavailable trigger is marked unsupported.
- **Security/example/maintenance:** Human approval for consequential external side effects. Example: nightly report runs only with fresh approved project manifest and emits a status artifact. **Status:** partial—workflow scheduling/global system skills cover pieces. Version and monitor workflow changes.
