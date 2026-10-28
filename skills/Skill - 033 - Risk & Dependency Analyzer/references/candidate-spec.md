# Source candidate specification

- **Purpose/problem; goal/outcome:** Technical and schedule dependencies or risks surface late; make them visible with mitigation and ownership.
- **Behavior; activation/non-activation:** Trace technical, integration, security, operational, and schedule links; do not imply probability data where none exists.
- **Inputs/tools/dependencies/handoff:** Requirements, design, environment, schedule, external services; dependency graph and risk register; depends 11/17–20/25; hands to 22/26/42/47/48.
- **Procedure/decision:** 1) Identify dependency and risk events. 2) Record source, likelihood/impact basis, owner, mitigation, trigger. 3) Find critical path and single points. 4) Escalate intolerable/residual risk; do not approve it on behalf of owner.
- **Outputs/acceptance/failure:** Linked risk/dependency register; pass when material risks have evidence, owner, mitigation/status, or accepted decision. Unknowns remain open.
- **Security/example/evidence/maintenance:** Include data loss, secrets, availability and supply-chain risks. Example: provider availability blocks chatbot test; create contingency and evidence gate. **Status:** partial—SDLC and architecture mention risks; no register tool/evaluation tests. Reassess as dependencies change.
