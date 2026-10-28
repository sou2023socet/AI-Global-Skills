# Source candidate specification

- **Purpose/problem; goal/outcome:** Diagrams are missing or drifted; reconstruct architecture, sequences, deployments, data flow, and workflows from verified as-built evidence.
- **Behavior; activation/non-activation:** Model confirmed components and label inferred edges; do not design a replacement architecture unless asked.
- **Inputs/tools/dependencies/handoff:** Code/config/API/runtime evidence, audience and diagram type; repository search, Mermaid-capable Markdown; depends 08/10; hands to 19/26/43.
- **Procedure/decision:** 1) Identify components and evidence sources. 2) Trace each interaction/data boundary. 3) Render/validate syntax and reconcile contradictions. 4) If a connection is only inferred, annotate it or omit it.
- **Outputs/acceptance/failure:** Diagram plus legend/source notes; pass when all included edges have evidence and Mermaid renders. On unsupported renderer, provide source and mark rendering unverified.
- **Security/example/evidence/maintenance:** Redact topology/secrets where sensitive. Example: controller/service/database sequence diagram cites code entry points. **Status:** partial—architecture design and documentation skills provide diagram conventions but not reverse evidence. Revalidate after integration changes.
