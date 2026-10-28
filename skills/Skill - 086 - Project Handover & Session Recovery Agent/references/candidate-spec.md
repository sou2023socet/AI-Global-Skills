# Source candidate specification

- **Purpose/problem; goal/outcome:** New sessions repeat work or act on obsolete handover; reconstruct active state and verify it against workspace.
- **Behavior; activation/non-activation:** Read handovers, decisions, tasks, evidence; do not treat previous agent output as current truth.
- **Inputs/tools/dependencies/handoff:** Project identity, handover, task history, current Git/files, approvals; project memory and evidence; depends 05/06/58/72–77; hands to 04/74/80.
- **Procedure/decision:** 1) Load last authorized handover. 2) Compare status, files, tests and approvals to current source. 3) Reconcile stale/conflicting items. 4) If identity or change history is unclear, present uncertainty and stop risky continuation.
- **Outputs/acceptance/failure:** Resume brief with verified done/in-progress/blocked/next; pass when each active claim is current or labeled stale. Missing handover may be reconstructed with citations.
- **Security/example/maintenance:** Respect session/project privacy; do not expose prior unrelated chats. Example: previous note says no tests, current repository includes tests; update from current source. **Status:** partial—global skill gives stage handoff; no project recovery process. Revalidate every resume.
