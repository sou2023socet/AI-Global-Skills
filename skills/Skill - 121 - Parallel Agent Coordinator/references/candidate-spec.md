# Source candidate specification

- **Purpose/problem; goal/outcome:** Parallel work can conflict on shared files or duplicated effort; divide independent tasks with isolated ownership and integration checks.
- **Behavior; activation/non-activation:** Delegate bounded independent tasks only; do not parallelize dependent traces or simultaneous edits to same files without coordination.
- **Inputs/tools/dependencies/handoff:** Task graph, files/resources, agent capabilities, shared-state constraints; task/agent system; depends 01/06/23/53/57; hands tasks via 55 and recovery via 56.
- **Procedure/decision:** 1) Identify independent work and shared resources. 2) Assign explicit scope, stop condition, output contract, and owner. 3) Integrate results and verify shared interfaces. 4) If conflict or agent failure occurs, pause dependent merges and preserve evidence.
- **Outputs/acceptance/failure:** Assignment map, results, conflict log; pass when no task overlap remains unresolved and combined result is validated. No agent capability → serial fallback.
- **Security/example/maintenance:** Limit data/tool permissions per assignment. Example: one agent audits docs while another independently checks test config; code edits wait for integration owner. **Status:** proposed—no coordinator skill/runtime. Review conflict/quality metrics.
