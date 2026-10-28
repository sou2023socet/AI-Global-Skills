# Source candidate specification

- **Purpose/problem; goal/outcome:** Source text does not prove actual behavior; safely compare expected/documented behavior with observed execution.
- **Behavior; activation/non-activation:** Execute only bounded, authorized scenarios; do not claim runtime verification from static inspection.
- **Inputs/tools/dependencies/handoff:** Expected behavior, target/environment identity, inputs, side-effect scope; native test runner/browser/API/log tools; depends 04/06; hands discrepancies to 14/29/33–42.
- **Procedure/decision:** 1) Confirm target, environment, and side effects. 2) Select smallest discriminating scenario and baseline. 3) Run and capture output/evidence. 4) If target safety or expected result is unclear, stop as BLOCKED rather than probing broadly.
- **Outputs/acceptance/failure:** Case-level expected/actual/status and environment; pass only on observed assertion success. Infrastructure/tool failure is BLOCKED/FAILED, not product pass.
- **Security/example/evidence/maintenance:** Synthetic data and redaction; production activity requires explicit scope. Example: documented `/health` is called on approved local service and HTTP result recorded. **Status:** partial—focused, functional, automation test instructions; no unified runtime protocol or skill tests. Preserve runner/version for replay.
