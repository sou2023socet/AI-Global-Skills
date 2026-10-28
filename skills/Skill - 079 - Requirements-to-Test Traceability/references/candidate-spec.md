# Source candidate specification

- **Purpose/problem; goal/outcome:** Requirements are mistaken for covered without tests; create bidirectional links from acceptance criteria to cases and results.
- **Behavior; activation/non-activation:** Maintain IDs/status and reveal gaps; do not equate line coverage with requirement verification.
- **Inputs/tools/dependencies/handoff:** Approved requirements, test inventory/results; spreadsheet/Markdown/test manager; depends 06/20/28–31; hands gaps to 34/35 and readiness to 42.
- **Procedure/decision:** 1) Assign stable IDs to criteria. 2) Link one or more tests and evidence. 3) Mark verified/failed/blocked/missing with run context. 4) If a criterion lacks an observable test, report uncovered rather than infer pass.
- **Outputs/acceptance/failure:** RTM with requirement↔test↔result; pass when every in-scope criterion has disposition. Preserve historical run results.
- **Security/example/maintenance:** Keep test data synthetic; redact reports. Example: role restriction maps to unauthorized and authorized cases with separate evidence. **Status:** partial—SDLC/QA mention traceability, no maintained mapping/test integration. Update with requirement changes.
