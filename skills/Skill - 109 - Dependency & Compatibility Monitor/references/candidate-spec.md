# Source candidate specification

- **Purpose/problem; goal/outcome:** Vulnerabilities/deprecations/compatibility breaks are found late; monitor dependencies and propose evidence-backed updates.
- **Behavior; activation/non-activation:** Compare lockfiles/versions to authoritative advisories/support matrices; do not auto-upgrade.
- **Inputs/tools/dependencies/handoff:** Manifests, allowed registries, runtime constraints, update policy; package audit/advisory feed if available; depends 17/25/57–59; hands risks to 19/22/25/63.
- **Procedure/decision:** 1) Inventory direct/transitive versions. 2) Check official advisories and compatibility. 3) Assess exploitability/upgrade path/test scope. 4) If feed stale, package unavailable, or major upgrade risky, label unknown and request decision.
- **Outputs/acceptance/failure:** Dated dependency report and staged recommendation; pass when each package is checked with source/date or explicit missing source. No auto-merge.
- **Security/example/maintenance:** Use trusted feeds; don't upload private lockfiles without authorization. Example: vulnerable transitive package requires compatible patch and regression plan. **Status:** proposed new monitor; discovery checks only. Refresh at approved cadence.
