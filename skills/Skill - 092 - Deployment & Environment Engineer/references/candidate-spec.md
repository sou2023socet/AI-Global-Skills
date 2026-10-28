# Source candidate specification

- **Purpose/problem; goal/outcome:** Deployment configuration is fragile or undocumented; prepare reproducible environment, configuration, health and rollback plans.
- **Behavior; activation/non-activation:** Design/validate deployment assets; do not deploy production unless separately authorized.
- **Inputs/tools/dependencies/handoff:** Target architecture, environment contracts, secrets mechanism, artifact, SLO; manifests/containers/infra validators; depends 23/25/30/38/39/42/46; hands plan to 48.
- **Procedure/decision:** 1) Map environment-specific config and dependencies. 2) Validate health/readiness/secrets/network boundaries. 3) Define migration order and rollback. 4) If target, credentials, or rollback are unverified, block execution.
- **Outputs/acceptance/failure:** Deployment plan/config and environment matrix; pass when config is reproducible, secrets externalized, health/rollback criteria explicit. Validation failures retain existing config.
- **Security/example/maintenance:** Least privilege, no secret logs, explicit production approval. Example: staging config uses secret references and restricted internal DB port. **Status:** partial—DevOps and deployment verification. Review config drift on release.
