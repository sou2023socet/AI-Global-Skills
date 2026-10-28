# Source candidate specification

- **Purpose/problem; goal/outcome:** Ambiguous prompts cause rework and unsafe assumptions; improve instructions for clarity, completeness, output, and controllable execution.
- **Behavior; activation/non-activation:** Diagnose intent, constraints, missing facts, and output shape; do not alter meaning, add permissions, or execute a prompt-only request.
- **Inputs/tools/dependencies/handoff:** Original prompt, audience/model/tool constraints, expected deliverable; prompt checklist and bounded examples; depends 02/20; hands improved prompt to 53 or user.
- **Procedure/decision:** 1) Extract goal, constraints, context, exclusions. 2) Identify ambiguity and ask only material questions. 3) Rewrite with acceptance criteria and output format. 4) Compare to original; if intent changes, show the delta and request confirmation.
- **Outputs/acceptance/failure:** Revised prompt plus assumptions/questions; pass when all original constraints remain and output is testable. Missing context is requested or marked.
- **Security/example/evidence/maintenance:** Redact private data before external model use. Example: “make app better” becomes scoped accessibility review with routes, target devices, and evidence output. **Status:** partial—token efficiency handles context, not prompt correctness. Review effectiveness using authorized scenarios.
