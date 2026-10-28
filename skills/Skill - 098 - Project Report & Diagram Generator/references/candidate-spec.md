# Source candidate specification

- **Purpose/problem; goal/outcome:** Reports/diagrams are inconsistent with templates and evidence; produce accurate, presentation-ready artifacts without fabricated project facts.
- **Behavior; activation/non-activation:** Populate specified templates and cite evidence; do not invent dates, approvals, counts, or progress values.
- **Inputs/tools/dependencies/handoff:** Template, project evidence, audience, required format; doc generation/diagram tooling; depends 06/11/13/33/43; output to 49/50/76.
- **Procedure/decision:** 1) Map each template field to evidence. 2) Fill confirmed values and mark missing/confirmation-needed. 3) Validate layout, links, math/diagram syntax. 4) If required data is absent, leave explicit placeholder rather than estimate.
- **Outputs/acceptance/failure:** Reports, diagrams, evidence note and missing-field list; pass when all claims trace to source and output opens. Conversion errors are reported.
- **Security/example/maintenance:** Redact PII/secrets. Example: weekly report has missing meeting dates; marks “not supplied,” not fabricated. **Status:** partial—docs skill supports reports/diagrams but no template engine. Validate each template revision.
