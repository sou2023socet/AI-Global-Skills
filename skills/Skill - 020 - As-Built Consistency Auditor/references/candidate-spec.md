# Source candidate specification

- **Purpose/problem; goal/outcome:** Requirements, implementation, behavior, tests, diagrams, and docs may contradict; create a traceable discrepancy report.
- **Behavior; activation/non-activation:** Cross-check matched artifacts and classify mismatch; do not resolve architectural conflicts silently.
- **Inputs/tools/dependencies/handoff:** Requirements and context, code/runtime/tests/docs/diagrams; search, test output and link checker; depends 06/09–13; sends lifecycle gaps to 15 and changes to 40/62.
- **Procedure/decision:** 1) Build requirement-to-evidence rows. 2) Compare each artifact’s claims. 3) Classify mismatch (code, test, docs, unknown) and impact. 4) Request decision where expected truth is ambiguous.
- **Outputs/acceptance/failure:** Discrepancy matrix with source and owner; pass when all in-scope claims are checked or labeled unverified. Missing artifact is a gap, not a pass.
- **Security/example/evidence/maintenance:** Redact evidence; read-only audit unless separately approved fixes. Example: docs claim CSV export but no route/UI/test is found; report “not evidenced,” not definitively absent. **Status:** partial—discovery/documentation drift checks. Re-run after release.
