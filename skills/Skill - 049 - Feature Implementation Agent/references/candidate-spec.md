# Source candidate specification

- **Purpose/problem; goal/outcome:** Feature changes lack consistent requirement-to-test trace; implement approved functionality with documentation and verified evidence.
- **Behavior; activation/non-activation:** Plan, modify, test, document within authorized scope; not for unapproved scope or generic operation that existing domain skill owns fully.
- **Inputs/tools/dependencies/handoff:** Approved requirement/acceptance, baseline status, repo conventions; editor, native test/build; depends 20/24–27; hands defects to 29/41 and evidence to 33/42.
- **Procedure/decision:** 1) Inspect callers/interfaces/current changes. 2) Plan minimal files/tests. 3) Implement and run focused checks. 4) If acceptance is ambiguous or tests expose unrelated baseline failures, pause and report rather than expanding scope.
- **Outputs/acceptance/failure:** Scoped diff, tests, doc updates and evidence; pass when criteria map to passing checks and no unrelated edits. Failure preserves diff and records diagnostics.
- **Security/example/evidence/maintenance:** No secrets; approval for side-effecting commands per policy. Example: approved export feature adds endpoint/UI/tests and an API doc entry. **Status:** partial domain skills exist, no generic feature agent. Keep stack specifics delegated.
