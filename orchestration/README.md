# Deterministic orchestration

The canonical registry is descriptive metadata. It is not an autonomous agent
runner and it does not grant tool permissions.

## Selection order

1. Establish a project identity and a current task scope.
2. Match explicit task intent to registry triggers.
3. Select the smallest set of skills that covers the requested outputs.
4. Resolve required dependencies and reject unknown IDs or cycles.
5. Apply project policy and the build/test approval boundary.
6. Execute one skill at a time, recording inputs, outputs, evidence, and failures.
7. Resume only from the last durable checkpoint after a failure.

Selection must fail closed when project identity, permissions, required inputs, or
dependency integrity is unknown. A registry record never authorizes external
access, code execution, production impact, or secret handling by itself.

See [workflow contract](../workflows/lifecycle/workflow-contract.json) and
[permission policy](../shared/policies/permission-policy.md).
