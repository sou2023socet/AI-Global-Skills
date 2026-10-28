# Source candidate specification

- **Purpose/problem; goal/outcome:** Releases lack traceable versions and recovery; coordinate release criteria, artifact, rollout, and tested rollback.
- **Behavior; activation/non-activation:** Prepare/review release records and rollback; not independently approve or deploy.
- **Inputs/tools/dependencies/handoff:** Verified artifact, version policy, readiness, known risks, previous stable artifact; Git/release tooling; depends 06/23/42/46/47; handoff UAT and history to 49/79.
- **Procedure/decision:** 1) Validate version/artifact/test lineage. 2) Check release gate and rollback compatibility. 3) Present rollout/rollback steps and owner approvals. 4) If rollback is unavailable or critical gate fails, recommend hold.
- **Outputs/acceptance/failure:** Release checklist, version/changelog, rollback plan and outcome; pass only after authorized release evidence. Failed deployment records actual state and recovery.
- **Security/example/maintenance:** Production action requires explicit command-scoped approval. Example: previous container digest retained and restore smoke test verified before release. **Status:** partial—deployment-verification provides rollback goals, no release ledger. Preserve immutable release history.
