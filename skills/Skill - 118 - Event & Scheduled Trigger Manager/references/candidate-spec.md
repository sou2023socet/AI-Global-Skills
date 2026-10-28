# Source candidate specification

- **Purpose/problem; goal/outcome:** Scheduled/event runs may duplicate or violate permissions; register triggers and execution constraints safely.
- **Behavior; activation/non-activation:** Configure supported triggers, deduplication, pause/disable, windows; not an assumption that host can schedule jobs.
- **Inputs/tools/dependencies/handoff:** Trigger source, schedule, timezone, task, permission, dedup key; platform scheduler/event API; depends 52/55/57/58; failures to 56.
- **Procedure/decision:** 1) Verify platform trigger capability and identity. 2) Define schedule/window, condition and idempotency key. 3) Test disabled/read-only path. 4) Unsupported capability, ambiguous timezone, or missing permission means do not activate.
- **Outputs/acceptance/failure:** Trigger registry, run ledger, disable instructions; pass when duplicate events produce at most one authorized run per key. Missed run must be visible.
- **Security/example/maintenance:** Do not schedule production mutations without explicit approval; protect tokens. Example: daily audit starts only if registry freshness check succeeds. **Status:** partial—workflow scheduling has cron examples, no trigger manager. Monitor drift/timezone.
