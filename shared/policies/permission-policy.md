# Permission and isolation policy

- Global skills contain reusable instructions only; project code, credentials,
  logs, and private evidence remain in the project workspace.
- Read-only inspection is the default permission.
- File modification, code execution, external access, production impact, package
  installation, and artifact generation require the host's applicable approval.
- A skill may describe a tool without authorizing that tool.
- Sensitive values are redacted before evidence is persisted or reported.
- Cross-project search uses explicit project scope and must not expose unrelated
  private context.
- Unknown identity, scope, ownership, or permission is a blocker, not consent.
- Every consequential action records the actor, scope, time, command or change,
  result, and rollback or recovery path.
