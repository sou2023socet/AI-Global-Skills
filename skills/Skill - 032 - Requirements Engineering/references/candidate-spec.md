# Source candidate specification

- **Purpose/problem; goal/outcome:** Vague requests produce incomplete work; create prioritized, testable functional/NFR requirements, constraints, and acceptance criteria.
- **Behavior; activation/non-activation:** Elicit and normalize requirements; do not implement or mark stakeholder approval without explicit authorization.
- **Inputs/tools/dependencies/handoff:** User needs, reconstructed evidence, constraints, stakeholders; requirements table/backlog; depends 10/16/19/24; hands to 22/23/26/33/49.
- **Procedure/decision:** 1) Identify actors/goals and boundaries. 2) Write atomic functional, quality, and constraint statements. 3) Add testable acceptance criteria and priority/dependency. 4) Resolve ambiguity with user; if unavailable, label assumption and block dependent commitment.
- **Outputs/acceptance/failure:** Versioned requirement set and traceability IDs; pass when each criterion is observable and scope is approved. Conflicts remain unresolved, not merged.
- **Security/example/evidence/maintenance:** Classify sensitive data/security requirements. Example: “calculator supports fractions” becomes accepted input, exact output, error case, and supported operations. **Status:** partial—SDLC provides traceability, not full elicitation. Change-controlled as user needs evolve.
