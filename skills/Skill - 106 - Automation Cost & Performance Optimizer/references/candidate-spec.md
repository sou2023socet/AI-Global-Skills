# Source candidate specification

- **Purpose/problem; goal/outcome:** Workflows waste calls, tokens, latency, or compute; measure and improve efficiency without weakening correctness/safety.
- **Behavior; activation/non-activation:** Analyze comparable metrics and bottlenecks; not optimize by dropping required validation or security checks.
- **Inputs/tools/dependencies/handoff:** Workflow traces, cost/latency baseline, quality outcomes; usage/telemetry tools; depends 06/39/53–59/66; hands changes to 52–55/70.
- **Procedure/decision:** 1) Define quality-preserving objective and baseline. 2) Find redundant waits/calls/context. 3) Pilot reversible optimization. 4) Reject changes that reduce evidence or safety even if cheaper.
- **Outputs/acceptance/failure:** Before/after measures with variance and quality results; pass when improvement is reproducible and quality non-regression holds. Missing telemetry is a limitation.
- **Security/example/maintenance:** Do not expose user prompts/secrets in traces. Example: cache stable metadata but recheck volatile Git status before editing. **Status:** partial—token efficiency/performance skills address different layers. Re-measure after tool changes.
