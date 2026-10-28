# Source candidate specification

- **Purpose/problem; goal/outcome:** Architecture and behavior are undocumented; reconstruct modules, call/data flows, dependencies, and likely design intent with confidence labels.
- **Behavior; activation/non-activation:** Trace symbols, config, tests, and runtime evidence; do not present naming-based inference as fact or modify code.
- **Inputs/tools/dependencies/handoff:** Repository, manifests, entry points, tests/logs, target question; search/LSP/call graph where available; depends 04/09; hands requirements/diagrams to 10/11.
- **Procedure/decision:** 1) Start at entry points and dependency manifests. 2) Trace callers/data/contracts in both directions. 3) Compare test/runtime evidence to inferred intent. 4) If tooling cannot resolve dynamic behavior, mark the trace incomplete and request runtime evidence.
- **Outputs/acceptance/failure:** As-built map, symbol/file citations, confidence and unknowns; pass when cited paths support each important edge. Missing LSP/index is recorded, not simulated.
- **Security/example/evidence/maintenance:** Avoid exposing secret config; inspect redacted examples. Example: controller→service→repository path is documented, while untested external callback stays unknown. **Status:** partial—project discovery and architecture design help but no archaeology protocol. Refresh after structural changes.
