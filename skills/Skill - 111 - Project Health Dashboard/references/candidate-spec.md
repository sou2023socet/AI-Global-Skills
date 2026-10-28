# Source candidate specification

- **Purpose/problem; goal/outcome:** Status is fragmented or stale; summarize progress, blockers, risk, quality, and release state with source freshness.
- **Behavior; activation/non-activation:** Aggregate verified metrics and missing data; do not estimate project health from file count or stale status text.
- **Inputs/tools/dependencies/handoff:** Registry, evidence/status, test/release/risk data and timestamps; report/dashboard renderer; depends 03/06/58/72–75/79–80; informs 62/69/70.
- **Procedure/decision:** 1) Load allowed sources and freshness thresholds. 2) Reconcile conflicting states. 3) Show metric source and missingness. 4) If critical source stale/unavailable, mark dashboard partial and do not score as healthy.
- **Outputs/acceptance/failure:** Timestamped status view and source links; pass when each metric has definition/source/freshness. Aggregation failure visible.
- **Security/example/maintenance:** Role-based access; no sensitive details in broad dashboards. Example: tests green last month → stale, not current green. **Status:** proposed new capability; no dashboard service. Review metric definitions.
