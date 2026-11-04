# Universal project artifact templates

These are optional starting points, not required files. Copy only artifacts
needed by the project, tailor fields to the project schema, preserve stable IDs,
and link to canonical information instead of duplicating it. Replace
`UNKNOWN`/`NOT_CHECKED` only with evidence.

## 1. Project manifest

```yaml
schemaVersion: "1.0"
project:
  id: "stable-project-id"
  name: "Project name"
  type: "software | ai-data | research | automation | other"
  purpose: "Evidence-backed short purpose"
  ownerRole: "UNKNOWN"
  lifecycle:
    model: "UNKNOWN"
    stage: "UNKNOWN"
    lastReviewed: "YYYY-MM-DD"
  technologies: []
  repositories:
    - id: "repo-id"
      canonicalPathOrRemote: "UNKNOWN"
      role: "source | infrastructure | docs | other"
      ownerRole: "UNKNOWN"
      lastVerified: "UNKNOWN"
  entryPoints:
    index: "PROJECT_INDEX.md"
    status: "PROJECT_STATUS.md"
    nextActions: "NEXT_ACTIONS.md"
  accessScope: "explicit"
  status: "UNKNOWN"
  lastChecked: "YYYY-MM-DDThh:mm:ssZ"
```

## 2. Project index

```markdown
# Project Index
Project ID: `...` | Owner role: `...` | Last checked: `...`

## Start here
- [Overview](00_PROJECT_CONTROL/PROJECT_OVERVIEW.md)
- [Current status](PROJECT_STATUS.md)
- [Next actions](NEXT_ACTIONS.md)
- [Manifest](project-manifest.yaml)

## Canonical artifact map
| Area | Canonical path/URL | Purpose | Owner role | Status/freshness |
|---|---|---|---|---|
| Requirements | `...` | `...` | `...` | `...` |

## Repositories and access
| Repository ID | Canonical path/remote | Role | Owner | Last verified |
|---|---|---|---|---|
```

## 3. Project overview

```markdown
# Project Overview
Project ID: `...` | Status: `...` | Updated: `...`

## Purpose and users
## Scope and exclusions
## Capabilities and system boundaries
## Repositories and owners
## Constraints and assumptions
## Lifecycle model and current stage
## Key risks and dependencies
## Entry points and canonical sources
## Evidence and open questions
```

## 4. Project status

```markdown
# Project Status
Project ID: `...` | Last checked (ISO 8601): `...` | Milestone/version: `...`

## Lifecycle stage
Stage: `...` | Evidence: `...` | Gate/decision owner: `...`

## Workstream status
| Item ID | Area | Implementation | Verification | Documentation | Release | Acceptance | Evidence |
|---|---|---|---|---|---|---|---|

## Current work and blockers
## Risks/dependencies
## Verification gaps and stale information
## Next status review
```

## 5. Requirements specification

```markdown
# Requirements
Version: `...` | Owner role: `...` | Status: `...`

## Problem and goals
## Scope and exclusions
## Constraints and assumptions
## Functional requirements
| ID | Requirement | Priority | Status | Source | Acceptance criteria | Owner |
|---|---|---|---|---|---|---|
## Non-functional requirements
## User stories/journeys
## Dependencies and conflicts
## Change history and approvals
```

## 6. Research report

```markdown
# Research: <question>
Research ID: `...` | Author: `...` | Date/accessed: `...`

## Question and decision needed
## Method and scope
## Sources and citations
## Findings and evidence
## Alternatives and comparison criteria
## Limitations, confidence, and unknowns
## Conclusion/status: PROPOSED | UNDER_REVIEW | APPROVED
## Links to requirements, decision, and plan
```

## 7. Technical feasibility report

```markdown
# Feasibility: <option>
ID: `...` | Evaluator: `...` | Date: `...`

## Objective and constraints
## Candidate options and baseline
## Technical/operational/security/privacy feasibility
## Dependencies, cost/capacity assumptions, and risks
## Prototype/experiment method and evidence
## Recommendation, confidence, and unresolved questions
## Decision owner and next action
```

## 8. Project roadmap

```markdown
# Roadmap
Version/date: `...` | Planning horizon: `...` | Status: `...`

| Milestone | Outcome | Status | Dependencies | Exit criteria | Risk | Target range | Evidence |
|---|---|---|---|---|---|---|---|

## Assumptions and capacity constraints
## Change/rebaseline history
```

## 9. Task and milestone tracker

```markdown
| ID | Task/outcome | Status | Owner role | Depends on | Acceptance/DoD | Risk/blocker | Evidence | Milestone |
|---|---|---|---|---|---|---|---|---|
```

## 10. Architecture documentation

```markdown
# Architecture: <system>
Version/date: `...` | Status: `...` | Scope: `...`

## Context and users
## Containers/modules and ownership
## Data/API contracts and flows
## Deployment and trust boundaries
## Quality attributes and constraints
## Decisions/alternatives (link ADRs)
## Risks, assumptions, and unknowns
## Validation and source evidence
```

## 11. Test plan and test case

```markdown
# Test Plan: <scope>
Plan ID/version: `...` | Build/environment: `...` | Owner: `...`

## Requirements and risks covered
## Scope, exclusions, and test data policy
## Test levels, setup, and entry/exit criteria
## Cases and automation references
## Results (PASS/FAIL/BLOCKED/NOT_RUN) and evidence
## Defects, residual risk, and sign-off
```

```markdown
## Test Case TEST-001: <title>
Requirement: `REQ-...` | Priority: `...`
Preconditions/data: `...`
Steps: `...`
Expected: `...`
Actual/result: `NOT_RUN`
Build/environment/time: `...`
Evidence/defect: `...`
```

## 12. Bug report

```markdown
# BUG-001: <short title>
Status/severity: `...` | Version/environment: `...` | Owner role: `...`

## Summary and impact
## Preconditions and safe reproduction steps
## Expected vs actual behavior
## Evidence (redacted) and frequency
## Related requirement/component
## Workaround, fix link, and regression test
## Verification and closure evidence
```

## 13. Deployment guide

```markdown
# Deployment: <service/environment>
Version/owner: `...` | Classification: `...`

## Preconditions and approvals
## Artifact/source revision and provenance
## Configuration and secret references (values excluded)
## Deployment steps and verification
## Rollback/restore steps and decision owner
## Monitoring, smoke checks, and failure response
## Evidence, last verified date, and limitations
```

## 14. Operational incident report

```markdown
# INC-001: <summary>
Severity: `...` | Start/end (timezone): `...` | Service: `...`

## Impact and detection
## Timeline (evidence-linked)
## Containment and recovery
## Root cause and confidence
## Data/security/privacy considerations
## Follow-up actions, owners, and due criteria
## Redacted evidence and review
```

## 15. Decision record

```markdown
# ADR-001: <decision title>
Status: PROPOSED | UNDER_REVIEW | APPROVED | DEFERRED | SUPERSEDED
Date/owner: `...` | Requirements: `...`

## Context and constraints
## Decision and rationale
## Alternatives considered
## Consequences, risks, and reversibility
## Approval/evidence
## Supersedes/superseded by
```

## 16. Evidence register

```markdown
| Evidence ID | Claim/item | Source path/URL/hash | Captured at | Scope/version/environment | Owner | Sensitivity/retention | Result |
|---|---|---|---|---|---|---|---|
```

## 17. Release notes

```markdown
# Release <version>
Status: `...` | Commit/artifact: `...` | Target/date: `...`

## Approved scope and changes
## Compatibility, migrations, and known issues
## Verification/security/acceptance evidence
## Deployment and rollback references
## Approvals and user-acceptance status
```

## 18. Future-planning item

```markdown
# FUT-001: <idea or deferred work>
Status: PROPOSED | UNDER_REVIEW | APPROVED | DEFERRED | CANCELLED
Source/date/owner role: `...`

## Problem/opportunity and evidence
## Expected value and impact
## Dependencies, risks, and alternatives
## Decision/review trigger
## Next action (if authorized)
```

## 19. Next-actions report

```markdown
# Next Actions
As of (ISO 8601): `...` | Project/milestone: `...`

| Priority | ACT-ID / action | Reason/evidence | Status | Depends on/blocker | Owner role | Completion criteria |
|---|---|---|---|---|---|---|

## Decisions/approvals needed
## Verification not performed
```

## 20. Project handover report

```markdown
# Project Handover
Project ID: `...` | Prepared at: `...` | Recipient role: `...`

## Purpose and current lifecycle stage
## Canonical repositories, paths, and access
## Architecture and setup entry points
## Current status: implemented / tested / verified / released / accepted
## Known issues, risks, blockers, and dependencies
## Decisions and approvals pending
## Prioritized next actions and completion criteria
## Key evidence and documentation links
## Freshness, limitations, and sensitive-data handling
```

## Template validation

- Validate IDs, status vocabulary, timestamps, required fields, links, and
  project-specific schema before publishing.
- Mark unused fields `NOT_APPLICABLE` only when that is meaningful; otherwise
  use `UNKNOWN`, `MISSING`, or `NOT_CHECKED`.
- Never populate example values with real credentials, customer data, or
  unsupported completion claims.
