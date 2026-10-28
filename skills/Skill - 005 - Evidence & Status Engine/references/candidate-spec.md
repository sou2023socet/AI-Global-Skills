# Source candidate specification

- **Purpose/problem; goal/outcome:** Status language conflates proposed, implemented, verified, accepted, and released; define evidence-linked claims and controlled status transitions.
- **Behavior; activation/non-activation:** Attach source and timestamp to status claims; do not generate evidence or assign a passed state from documentation alone.
- **Inputs/tools/dependencies/handoff:** Claim, artifact/tool output, owner, time, status transition; repository references and shared schema; depends 01/02; feeds all audits, readiness, dashboard, handover.
- **Procedure/decision:** 1) Classify claim and required evidence. 2) Validate artifact/command result and scope. 3) Set the least-advanced supported status. 4) If evidence is missing or stale, mark unverified/blocked and name the next check.
- **Outputs/acceptance/failure:** Evidence record, status vocabulary, transition report; pass when every completion claim is traceable and state distinctions remain intact. Missing evidence is a failed gate, not a success default.
- **Security/example/evidence/maintenance:** Redact sensitive artifacts and restrict access. Example: a skill folder exists but has no scenario test; status stays “implemented, unverified” or “partial,” not “verified.” **Status:** partial—status vocabulary exists in blueprint; no engine/schema. Review transition rules and evidence retention.

## Phase B — Project recovery and understanding
