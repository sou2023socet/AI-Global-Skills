# Source candidate specification

- **Purpose/problem; goal/outcome:** Conflicting or missing cross-project rules produce unsafe and inconsistent work; define universal engineering and communication principles while allowing explicit local exceptions.
- **Behavior; activation/non-activation:** Resolve applicable rules at task start and surface conflicts; do not overwrite project policy or claim compliance absent evidence.
- **Inputs/tools/dependencies/handoff:** Repository instructions, security policy, task constraints, supported tools; document search and policy comparison; depends 01/57; hands applicable rules to every workflow.
- **Procedure/decision:** 1) Inventory global and local rules. 2) Group by code, tests, security, docs, tools, approvals. 3) Identify contradictions and authority. 4) If a local rule conflicts with a non-negotiable safety rule, stop and request decision; otherwise scope the exception.
- **Outputs/acceptance/failure:** Versioned rule set, precedence map, exception record; pass when every rule has scope and no unresolved conflict is presented as settled. Missing policy remains unknown.
- **Security/example/evidence/maintenance:** Never weaken permission controls through a style exception. Example: local instructions require tests, but a test command may mutate shared data; ask for safe test scope before running. **Status:** partial—root SECURITY, CONTRIBUTING, and AUTHORING guides exist, no unified precedence contract. Review when policies change.
