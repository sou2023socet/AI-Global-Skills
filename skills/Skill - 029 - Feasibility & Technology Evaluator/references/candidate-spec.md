# Source candidate specification

- **Purpose/problem; goal/outcome:** Technology decisions omit constraints, cost, compatibility, or operational risk; compare viable options and recommend with uncertainty.
- **Behavior; activation/non-activation:** Score options against agreed criteria; do not choose a vendor/technology on unstated preferences.
- **Inputs/tools/dependencies/handoff:** Requirements, research sources, constraints, environment/cost model; official docs, compatibility data, architecture review; depends 17/18/23/25; hands to 20/22/26.
- **Procedure/decision:** 1) Establish must-haves and weights with owner. 2) Eliminate incompatible options using cited facts. 3) Compare lifecycle cost, security, operations, scale, lock-in. 4) If criteria/weights change ranking materially, present sensitivity and ask.
- **Outputs/acceptance/failure:** Decision matrix and recommendation, risks and assumptions; pass when recommendation is reproducible and ties to requirements. Missing cost/source becomes explicit unknown.
- **Security/example/evidence/maintenance:** Do not transmit secrets to vendors. Example: compare queue frameworks against deployment constraints and team capability, not popularity. **Status:** partial—architecture/discovery skills support portions; no evaluator or scoring evidence. Review on constraints/version change.
