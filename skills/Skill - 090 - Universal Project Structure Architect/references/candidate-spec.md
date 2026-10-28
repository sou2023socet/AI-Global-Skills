# Source candidate specification

- **Purpose/problem; goal/outcome:** Forced templates and ad hoc layouts hurt maintainability; recommend a structure suited to technology, scale, lifecycle, and existing conventions.
- **Behavior; activation/non-activation:** Inventory before recommending incremental structure; do not restructure solely to match a universal folder template.
- **Inputs/tools/dependencies/handoff:** Stack, team/workflows, current tree, build/test/import constraints; repository inventory and dependency graph; depends 04/08/19/20/25; hands to 26/72.
- **Procedure/decision:** 1) Map current modules and build boundaries. 2) Compare options against discoverability, coupling, tooling, team needs. 3) Identify migration risk and smallest change. 4) If no material benefit or migration risk dominates, recommend retain current layout.
- **Outputs/acceptance/failure:** Structure proposal/diagram and migration plan; pass when rationale and trade-offs are explicit. Missing code ownership blocks detailed design.
- **Security/example/maintenance:** Protect monorepo/private topology; migration requires approval. Example: preserve a small Angular app’s current layout rather than introducing unnecessary packages. **Status:** partial—architecture/discovery skills. Revisit as scale changes.
