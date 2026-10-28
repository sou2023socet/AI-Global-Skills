# Source candidate specification

- **Purpose/problem; goal/outcome:** Indexes/status/docs become stale after project changes; identify and reconcile records with canonical sources.
- **Behavior; activation/non-activation:** Compare records to source changes and update authorized derived fields; do not overwrite conflicts silently.
- **Inputs/tools/dependencies/handoff:** Canonical source map, Git changes, manifest/docs/status, sync permissions; link/hash checker; depends 06/44/58/72–73; feeds 61/76/80.
- **Procedure/decision:** 1) Detect changed sources and dependent records. 2) Mark stale/conflicting entries. 3) Regenerate derived content with source links. 4) Preserve manual decisions and request owner resolution on conflict.
- **Outputs/acceptance/failure:** Sync report and bounded update diff; pass when each affected record is updated, confirmed current, or flagged. Failed source read means stale/unknown.
- **Security/example/maintenance:** Propagate access/deletion restrictions; avoid copying secrets into indexes. Example: package version changed, manifest marked stale until verified. **Status:** partial—documentation drift exists, no project knowledge sync engine. Run on updates.
