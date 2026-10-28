# Source candidate specification

- **Purpose/problem; goal/outcome:** Decisions and blockers are repeatedly rediscovered; preserve concise, verified, project-scoped state so future work resumes without assuming stale notes are true.
- **Behavior; activation/non-activation:** Capture/restore task state with provenance; do not store credentials, unrelated project context, or speculative facts as decisions.
- **Inputs/tools/dependencies/handoff:** Approved project ID, current task, decisions, changed files, tests, blockers; canonical docs/session storage; depends 06/72/77; hands verified resume brief to 76/80.
- **Procedure/decision:** 1) Gather current Git/status and task evidence. 2) Separate decisions, facts, assumptions, and pending approvals. 3) Write/update only the authorized handover location. 4) On resume, recheck volatile facts; if notes contradict workspace, current evidence wins and conflict is reported.
- **Outputs/acceptance/failure:** Dated handover with done/in-progress/blocked/next and source references; pass when a new session can identify safe next action without repeating completed work. If storage unavailable, provide transient summary and disclose.
- **Security/example/evidence/maintenance:** Exclude secrets, PII, and private unrelated project data; retention/access must be authorized. Example: resume finds a formerly passing test now failing; state is refreshed, not blindly trusted. **Status:** partial—global-system stage reporting only; no project memory store. Review stale records on resume.
