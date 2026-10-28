# Source candidate specification

- **Purpose/problem; goal/outcome:** Agents act with insufficient context; determine whether evidence is adequate for a specific task and identify safe next steps.
- **Behavior; activation/non-activation:** Evaluate task-specific prerequisites and risk; not demand irrelevant exhaustive context.
- **Inputs/tools/dependencies/handoff:** Request, acceptance, repo state, evidence, tool availability, risk; context checklist; depends 04/06/72–73; gates 16–50/53/76.
- **Procedure/decision:** 1) Derive minimum facts needed for task. 2) Check each against current evidence/freshness. 3) Classify sufficient/partial/insufficient with safety-critical blockers. 4) If critical gap exists, ask or perform only safe discovery; do not execute consequential action.
- **Outputs/acceptance/failure:** Completeness report, missing facts, safe actions; pass when each gap has consequence and next action. Tool unavailable is explicit.
- **Security/example/maintenance:** Identify private data/permission gaps. Example: request to migrate DB without engine/version/backup confirmation is blocked. **Status:** proposed new skill; discovery notes unknowns but no task gate. Review checks for false blockers.
