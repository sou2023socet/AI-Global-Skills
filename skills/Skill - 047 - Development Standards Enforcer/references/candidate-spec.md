# Source candidate specification

- **Purpose/problem; goal/outcome:** Inconsistent code practices cause defects and maintenance cost; check project standards and report actionable deviations.
- **Behavior; activation/non-activation:** Apply local conventions, linters, error/security rules; do not impose external style or rewrite unrelated code.
- **Inputs/tools/dependencies/handoff:** Repository rules, language/toolchain, changed files; configured linter/compiler and review checklist; depends 02/25/26; hands fixes to feature/refactor/review skills.
- **Procedure/decision:** 1) Discover authoritative rules/config. 2) Check changed scope for naming, modularity, errors, tests, security. 3) Run only approved existing checks. 4) If no rule exists, label recommendation rather than violation.
- **Outputs/acceptance/failure:** Findings with rule/source/severity and exceptions; pass when all scoped findings are fixed, accepted, or explicitly deferred. Tool unavailable is recorded.
- **Security/example/evidence/maintenance:** Never remove validation/auth checks for style. Example: a catch-all suppresses errors; report rule and expected surface behavior. **Status:** partial—clean-code and stack skills. Refresh rule set with project changes.
