# Source candidate specification

- **Purpose/problem; goal/outcome:** Agents invoke irrelevant or conflicting skills; route tasks to minimal compatible capabilities and coordinate handoffs.
- **Behavior; activation/non-activation:** Match intent, scope, dependencies, tools and risk; do not invent unavailable capabilities or override user instructions.
- **Inputs/tools/dependencies/handoff:** User request, registry/catalogue, project context, permissions; classifier/rules and status; depends 01/06/20/21/57; dispatches selected skills.
- **Procedure/decision:** 1) Classify task and exclusions. 2) Select smallest set that covers acceptance criteria. 3) Resolve ownership/dependencies and approval gates. 4) If conflict/uncertainty remains, ask or choose safe non-action; record routing reason.
- **Outputs/acceptance/failure:** Selection rationale, ordered calls, combined evidence; pass when every required task has owner and no duplicate side effects. Tool/capability mismatch blocks.
- **Security/example/maintenance:** Respect permissions and sensitive context boundaries. Example: a one-method test selects focused/unit testing, not full audit. **Status:** partial—global skill and token efficiency guide manual routing; no engine/tests. Evaluate with misroute/conflict cases.
