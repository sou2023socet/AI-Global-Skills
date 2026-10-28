# Source candidate specification

- **Purpose/problem; goal/outcome:** Approved architecture is not consistently reflected in implementation; translate decisions into module boundaries and contracts.
- **Behavior; activation/non-activation:** Preserve approved ADR/contracts and detect design gaps; do not redesign without review or treat proposal as approved.
- **Inputs/tools/dependencies/handoff:** Approved diagrams/ADRs, requirements, coding standards, environment; code search and native build/test tools; depends 11/19/20/22/24/25; hands to 27–33.
- **Procedure/decision:** 1) Map design elements to modules/interfaces. 2) Identify existing reusable components and violations. 3) Plan incremental changes with compatibility tests. 4) If code reality conflicts with approved design, stop for decision before structural rewrite.
- **Outputs/acceptance/failure:** Implementation map, bounded code changes, updated diagrams; pass when tests/contracts show intended boundaries. Preserve baseline if build fails.
- **Security/example/evidence/maintenance:** Approval for data/interface breaking changes. Example: add service interface behind approved bounded context; integration tests verify contract. **Status:** partial as workflow across architecture/backend/frontend skills, no generic trace loop. Maintain ADR links.
