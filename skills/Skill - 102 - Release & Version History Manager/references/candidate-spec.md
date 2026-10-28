# Source candidate specification

- **Purpose/problem; goal/outcome:** Release claims lack artifact/test/approval provenance; keep an accurate chronological record and rollback reference.
- **Behavior; activation/non-activation:** Record confirmed version facts; do not create a release entry from a planned tag or successful local build.
- **Inputs/tools/dependencies/handoff:** Release event, tag/artifact hashes, verification, approver, rollback, change notes; Git/release registry; depends 06/42/46–50/77; feeds 61/69/76/80.
- **Procedure/decision:** 1) Confirm release artifact and identity. 2) Link changes/tests/approval/deployment evidence. 3) Record status and known limitations. 4) If deployment is unverified, record as prepared/implemented-unverified, not released.
- **Outputs/acceptance/failure:** Append-only release record and version index; pass when chronology and artifacts reconcile. Missing tag/hash is explicit.
- **Security/example/maintenance:** Keep secrets and private deployment credentials out of notes. Example: version candidate passed staging but has no production approval, so history says “verified staging,” not “released.” **Status:** partial—deployment skill provides verification but no history ledger. Preserve immutable references.
