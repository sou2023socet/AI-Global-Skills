# Source candidate specification

- **Purpose/problem; goal/outcome:** Decisions, failures, and tool outcomes are not traceable; create privacy-aware records useful for accountability and recovery.
- **Behavior; activation/non-activation:** Record significant events with correlation and evidence refs; do not log full secrets/payloads by default.
- **Inputs/tools/dependencies/handoff:** Event type, task/project ID, status, artifact refs, retention policy; append-only logger/store; depends 02/06/24/57; feeds 56/61–70/76/80.
- **Procedure/decision:** 1) Classify fields for sensitivity. 2) Redact/minimize before write. 3) Correlate events and preserve chronology. 4) If logging fails, surface degraded audit state and block actions requiring traceability.
- **Outputs/acceptance/failure:** Structured audit events and summaries; pass when events are queryable, protected, and retention enforced. Do not silently drop records.
- **Security/example/maintenance:** Least access, retention/deletion per policy, no credentials. Example: command outcome logs exit status and artifact reference, not token-bearing arguments. **Status:** proposed—no audit schema/store. Review privacy and retention.
