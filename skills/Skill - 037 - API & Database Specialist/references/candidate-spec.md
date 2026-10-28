# Source candidate specification

- **Purpose/problem; goal/outcome:** API/schema changes can diverge or corrupt data; coordinate contracts, persistence, transactions, validation, and migration.
- **Behavior; activation/non-activation:** Review both data and API effects; do not run destructive migrations or broaden access without approval.
- **Inputs/tools/dependencies/handoff:** Requirements, current schema/API, DB/version, data constraints; OpenAPI/SQL/migration tools; depends 19/20/23–26; hands to integration/testing/build.
- **Procedure/decision:** 1) Map consumer/provider fields and persistence ownership. 2) Design backward-compatible DTO/schema and migration. 3) Test empty/current data and failure/rollback paths. 4) If migration loses data or changes public contract incompatibly, require explicit approval and rollout plan.
- **Outputs/acceptance/failure:** Contract, migration, DTO/repository changes, compatibility evidence; pass when schema and payload tests agree and migration/recovery are reviewed. Block on unknown production data.
- **Security/example/maintenance:** Validate inputs, enforce row ownership, protect PII/secrets. Example: adding optional profile field preserves existing clients and migration defaults. **Status:** partial—separate API/database skills exist. Coordinate contract version changes.
