# Source candidate specification

- **Purpose/problem; goal/outcome:** Test level/environment choices are ad hoc; produce risk-based methods, data, priorities, and exit criteria.
- **Behavior; activation/non-activation:** Recommend coverage by risk and architecture; do not execute tests unless separately requested/approved.
- **Inputs/tools/dependencies/handoff:** Requirements, system boundaries, risk, toolchain, time constraints; test pyramid/checklist; depends 15/23/25/33; hands to 35–39.
- **Procedure/decision:** 1) Classify risks and testable behaviors. 2) Select unit/integration/system/security/performance levels. 3) Specify data/environment/isolation and evidence. 4) If required tool/environment is missing, propose fallback and mark coverage limitation.
- **Outputs/acceptance/failure:** Test strategy with priority, exit rules, owners; pass when high-risk acceptance has a planned method and safe target. No unsupported coverage promises.
- **Security/example/maintenance:** Production writes/load are excluded absent approval. Example: payment flow prioritizes deterministic unit/API tests with sandbox-only transaction. **Status:** partial—QA strategy skill. Review strategy after defects/architecture changes.
