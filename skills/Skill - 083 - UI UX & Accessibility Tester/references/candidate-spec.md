# Source candidate specification

- **Purpose/problem; goal/outcome:** Visual/interaction defects and inaccessible flows block users; verify usability/accessibility against defined criteria.
- **Behavior; activation/non-activation:** Test keyboard, semantics, focus, contrast and viewport under supported tools; do not claim WCAG conformance without appropriate audit scope.
- **Inputs/tools/dependencies/handoff:** Screens, user flows, target devices, criteria; browser accessibility tree, keyboard, screen reader if available; depends 12/20/31/33/34; defects to 40/42/49.
- **Procedure/decision:** 1) Map key user journeys and roles. 2) Check keyboard/focus/form labels/error announcements. 3) Check responsive/contrast criteria using selected tools. 4) If assistive tech unavailable, label untested criteria and do not infer pass.
- **Outputs/acceptance/failure:** Reproducible findings with device/tool/criterion; pass only for checked criteria. Tool coverage is disclosed.
- **Security/example/maintenance:** Use synthetic identities and redact screenshots. Example: error message is visually shown but not announced; record screen-reader finding with reproduction. **Status:** partial—functional/frontend/mobile skills. Keep supported WCAG version explicit.
