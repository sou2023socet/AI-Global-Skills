# Source candidate specification

- **Purpose/problem; goal/outcome:** Existing behavior and artifacts imply missing requirements; recover traceable functional/NFR candidates with fact/inference distinction.
- **Behavior; activation/non-activation:** Compare UI, API, schema, tests, docs, and runtime; do not invent stakeholder intent or silently convert inference to approved requirement.
- **Inputs/tools/dependencies/handoff:** Project context, artifacts, stakeholder notes, runtime evidence; source search and trace table; depends 04/08/09; hands candidates to 20 and validation links to 33.
- **Procedure/decision:** 1) Extract observable rules from each source. 2) Correlate duplicates/conflicts with source precedence. 3) Label observed/inferred/unknown and confidence. 4) Ask owner to resolve material conflicts before implementation.
- **Outputs/acceptance/failure:** Recovered requirements with source citations, assumptions, and questions; pass when each requirement is testable or explicitly unresolved. No stakeholder evidence means no approval claim.
- **Security/example/evidence/maintenance:** Exclude PII from recovered examples. Example: UI validates a required field, test confirms error, docs omit it; record fact and docs discrepancy. **Status:** partial—SDLC traceability only. Update when code or stakeholder evidence changes.
