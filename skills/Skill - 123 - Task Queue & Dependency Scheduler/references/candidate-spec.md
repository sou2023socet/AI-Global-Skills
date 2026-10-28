# Source candidate specification

- **Purpose/problem; goal/outcome:** Tasks start before prerequisites or become orphaned; maintain dependency-aware queue and readiness states.
- **Behavior; activation/non-activation:** Order tasks by approved priority, dependencies and constraints; do not schedule blocked or unapproved mutations.
- **Inputs/tools/dependencies/handoff:** Task IDs, priorities, dependencies, owners, status, deadlines; task store/graph; depends 06/22/23/53–54; dispatches eligible work, failures to 56.
- **Procedure/decision:** 1) Validate unique task/dependency IDs and cycles. 2) Compute ready vs blocked states. 3) Select by approved priority/fairness rule. 4) Cycle/unknown dependency prevents dispatch until resolved.
- **Outputs/acceptance/failure:** Queue snapshot, dependency graph, ready/block reasons; pass when every task has valid state and no dependency is bypassed. Store failure blocks autonomous scheduling.
- **Security/example/maintenance:** Access scoped to project; record approval prerequisites. Example: integration test waits for API contract and service implementation. **Status:** partial—SDLC/task scheduling instructions, no common scheduler schema. Reconcile statuses periodically.
