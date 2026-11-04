---
id: skill-universal-project-structure-governance
name: Skill - 268 - Universal Project Structure & Governance
description: Establish and maintain an adaptable project structure, folder responsibilities, evidence-backed status, lifecycle workflows, and project knowledge standards for software, AI, research, and automation projects.
---

# Skill - 268 - Universal Project Structure & Governance

## Purpose

Create one discoverable, evidence-backed project information architecture for
software, AI/data, research, automation, and other technical projects. Define
where project information belongs, who owns it, how it changes through the
project lifecycle, and how people and agents find the authoritative version.

The numbered folder structure in this skill is a logical default, not a
mandatory physical layout. Adapt it to project size, technology, established
repositories, team practice, security requirements, and the selected SDLC
model. Preserve useful existing paths and link to canonical repositories;
never move or duplicate source solely to match this example.

## Activation

Use when initializing a project workspace, adapting an existing repository,
reconstructing project knowledge, creating a handover, or defining project
status and lifecycle governance. Use with the project-context, discovery,
recovery, planning, documentation, SDLC, and evidence skills named below when
their focused capability is needed.

Do not invoke for unrelated implementation, to impose all folders on a small
project, to infer missing facts, or to bypass project-specific access, security,
approval, retention, or release policy.

## Skill hierarchy and integration

This skill is the project information-architecture and governance parent. It
does not replace the Universal Global AI Skills Framework or specialized
skills.

| Layer | Responsibility | Repository capabilities to use |
|---|---|---|
| Global AI Skills Framework | Shared instructions, canonical skill registry, permissions, standards, orchestration, evaluation | Global Skills Framework (007), Skill Selection & Orchestration Engine (122), Approval & Permission Controller (115), Skill Evaluation & Improvement (114) |
| Project Intelligence | Resolve project identity/context; make index, evidence, documentation, and status discoverable | Project Context Analyzer (011), Project Registry (013), Project Artifact & Evidence Manager (084), Evidence & Status Engine (005), Project Health Dashboard (111), Documentation Generator (093), Documentation Synchronization (094) |
| Project Recovery | Reconstruct behavior, requirements, documentation, and architecture from evidence | Existing Project Recovery (022), Reverse Engineering & Code Archaeology (025), Requirements Reconstruction (024), Documentation Recovery (021), Architecture & Diagram Reconstruction (019) |
| Research & Planning | Evaluate options, feasibility, roadmap, milestones, risk, and traceability | Technical Research Agent (035), Feasibility & Technology Evaluator (029), Roadmap & Project Planner (034), Risk & Dependency Analyzer (033) |
| Development | Implement features, repair defects, evolve APIs, and maintain module boundaries | Feature Implementation Agent (049), Bug Diagnosis & Repair Agent (041), API & Database Specialist (037), Frontend Architecture and Project Structure (052), Spring Boot Backend Architecture (060), Universal Project Structure Architect (090) |
| Quality Engineering | Plan and execute testing, review, security, accessibility, and performance work | Automated Testing Engineer (074), Test Strategy Generator (082), Requirements-to-Test Traceability (079), Security Auditor (080), UI UX & Accessibility Tester (083), Performance Auditor (076) |
| Delivery & Operations | Build, deploy, release, and maintain delivery records | Build & Packaging Verifier (091), Deployment & Environment Engineer (092), Release & Version History Manager (102), Release & Rollback Manager (099); operational procedures remain owned under `09_OPERATIONS/` |
| Automation & Agents | Integrate MCP/tools, coordinate agents, and automate approved workflows | MCP Integration Specialist (120), Parallel Agent Coordinator (121), Automation Workflow Designer (116), Task Queue & Dependency Scheduler (123) |
| Project Lifecycle | Initialize, maintain, reassess, plan future work, close, and preserve knowledge | Project Lifecycle Reassessment (113), Project Learning & Lessons Manager (112), Project Memory & Handover (012), Roadmap & Future Feature Manager (103) |

### Capability distinctions

- **Parent skills** coordinate broad responsibilities and handoffs; this is
  such a skill.
- **Child/specialist skills** perform focused, reusable work such as
  requirements reconstruction or release verification.
- **Workflows** define ordered steps, conditions, approvals, and failure
  behavior; they are not folders or skills.
- **Templates** define optional repeatable artifact formats; use only when the
  project needs the artifact.
- **Tools/MCP integrations** enable an approved interaction; they do not
  define project policy or grant permission.
- **Automation services** trigger or coordinate work; record ownership,
  configuration, and operational behavior in their canonical locations.
- **Evaluations** measure reliability and quality; a skill's existence or
  structural validation is not functional verification.

Do not create a separate skill for each directory. Keep folder-specific rules
here unless a responsibility is genuinely distinct, reusable, and not already
owned by an existing skill.

## Required procedure

1. **Resolve context:** confirm project ID/name, canonical repository or
   workspace paths, owner, project type, scope, lifecycle stage, access
   boundaries, freshness, and the requested outcome. If identity is ambiguous,
   report candidates and ask before writing.
2. **Inspect before changing:** inventory the root, tracked/untracked files,
   manifests, source repositories, docs, CI, tests, generated outputs, and
   existing conventions. Do not copy secret-bearing files into reports.
3. **Map and classify:** map existing artifacts to the logical areas below;
   identify canonical locations, aliases, duplicates, missing information,
   stale material, and unknowns. Keep observations separate from inference.
4. **Adapt the structure:** preserve canonical source repositories and working
   paths. Propose only useful folders/files. Create no empty folders and do not
   move files unless explicitly in scope and approved.
5. **Establish project entry points:** define one primary `PROJECT_INDEX.md`
   (or an existing equivalent), root status/manifest/next-actions files where
   useful, and links to canonical content. Avoid mirrored copies.
6. **Apply lifecycle and status rules:** record project phase, item statuses,
   owners, dependencies, blockers, evidence, and next actions separately.
   Never promote a status beyond its evidence.
7. **Generate/update artifacts:** use applicable templates in
   [`references/PROJECT_ARTIFACT_TEMPLATES.md`](references/PROJECT_ARTIFACT_TEMPLATES.md).
   Preserve existing formats where they already work.
8. **Validate and hand over:** check paths/links, manifest consistency,
   duplicate ownership, evidence freshness, secret handling, and the requested
   acceptance criteria. Report validation performed and not performed.

## Logical project structure

```text
MyProject/
|-- 00_PROJECT_CONTROL/
|-- 01_REQUIREMENTS/
|-- 02_RESEARCH/
|-- 03_PLANNING/
|-- 04_DESIGN/
|-- 05_SOURCE_CODE/
|-- 06_TESTING_QA/
|-- 07_DOCUMENTATION/
|-- 08_DEPLOYMENT/
|-- 09_OPERATIONS/
|-- 10_EVIDENCE_HISTORY/
|-- 11_AUTOMATION_AI/
|-- 12_ROADMAP_AND_FUTURE_PLANS/
|-- 13_RELEASES_AND_VERSIONS/
|-- 14_PROJECT_STATUS_AND_NEXT_STEPS/
|-- README.md
|-- PROJECT_INDEX.md
|-- PROJECT_STATUS.md
|-- project-manifest.yaml
`-- NEXT_ACTIONS.md
```

Treat this as a map, not a requirement to create 15 folders. On a small project,
keep a compact structure and map its existing paths to these logical areas in
the index. In a multi-repository system, keep source in its canonical
repositories and make this workspace a navigation/governance layer.

## Folder-wise operating guidelines

For each logical area, the rules below specify its purpose, ownership, content,
suggested layout, exclusions, metadata, relationships, skill handoffs, update
triggers, completion outputs, validation, maintenance, and duplicate controls.
Subfolders are optional and should be created only when they have real content
and an owner.

### `00_PROJECT_CONTROL/` — identity and governance

- **Owns / place here:** project charter/overview, approved scope, project ID,
  ownership and contact roles, governance rules, conventions, contribution
  guidance, access classifications, decision authority, and links to root
  entry files.
- **Suggested contents:** `PROJECT_OVERVIEW.md`, `GOVERNANCE.md`,
  `CONVENTIONS.md`, `OWNERS.md`, `access-classification.md`, and project-specific
  agent instructions. Root `project-manifest.yaml` and `PROJECT_INDEX.md`
  remain canonical; link to them rather than keeping copies here.
- **Do not store:** credentials, private keys, unapproved personal data,
  duplicated source, or stale snapshots of root control files.
- **Metadata and relationships:** project ID, owner role, scope/version,
  approval/effective date, review date, and source references. Governs all
  other areas; `01_REQUIREMENTS/` owns requirement detail.
- **Skills and update trigger:** Project Registry (013), Project Context
  Analyzer (011), Global Development Rules (006), and this parent skill use or
  update it when identity, ownership, policy, scope, or conventions change.
- **Output / acceptance:** a human and agent can identify the correct project,
  authority, repository, constraints, and source of truth without guessing.
  Validate IDs/paths, access boundaries, approvals, and links; review on
  ownership or governance changes. Never duplicate a policy owned globally.

### `01_REQUIREMENTS/` — needs and acceptance

- **Owns / place here:** problem statement, scope, functional/non-functional
  requirements, user stories/journeys, constraints, assumptions, acceptance
  criteria, deferred requirements, and change history.
- **Suggested contents:** `problem-statement.md`, `requirements/`,
  `user-stories/`, `constraints.md`, `acceptance-criteria.md`,
  `change-log.md`, and `REQUIREMENTS_TRACEABILITY.md`.
- **Do not store:** implementation plans masquerading as requirements,
  unapproved promises, secrets, or duplicate acceptance criteria maintained
  elsewhere.
- **Metadata and relationships:** stable requirement IDs, status, source,
  owner, priority, rationale, acceptance evidence link, dependencies, and
  change/version. Link to design in `04_DESIGN/` and test evidence in
  `06_TESTING_QA/`.
- **Skills and update trigger:** Requirements Engineering (032), Requirements
  Reconstruction (024), Requirements and User Journey Engineering (231), and
  Requirements-to-Test Traceability (079) update it when needs or scope change.
- **Output / acceptance:** every in-scope requirement has an owner, testable
  acceptance condition, and disposition. Validate uniqueness, traceability,
  approval, and orphan links; preserve superseded requirements as history and
  do not call a proposed requirement approved.

### `02_RESEARCH/` — evidence and alternatives

- **Owns / place here:** technical research, source links/citations,
  comparisons, feasibility studies, prototypes/experiments, assumptions,
  limitations, and research conclusions.
- **Suggested contents:** `references/`, `comparisons/`, `feasibility/`,
  `experiments/`, and dated reports named with topic and version.
- **Do not store:** unlicensed copied material, secrets, production data,
  unrepeatable claims presented as fact, or authoritative decisions whose
  source belongs in `04_DESIGN/` or `00_PROJECT_CONTROL/`.
- **Metadata and relationships:** question, method, sources and access date,
  project/stack version, criteria, evidence, confidence, conflicts, author,
  and conclusion status. Conclusions may inform `03_PLANNING/` and decision
  records in `04_DESIGN/`.
- **Skills and update trigger:** Technical Research Agent (035), Feasibility &
  Technology Evaluator (029), and Reverse Engineering & Code Archaeology (025)
  update it when a decision requires external or repository evidence.
- **Output / acceptance:** a reproducible, cited conclusion with alternatives
  and limitations. Check link freshness, source quality, and license; date
  volatile facts, archive superseded reports, and link rather than duplicate
  research.

### `03_PLANNING/` — approved work sequence

- **Owns / place here:** project plan, WBS, implementation sequence,
  dependencies, milestones, estimates/ranges, capacity assumptions, sprint or
  iteration plans, and risk/mitigation plans.
- **Suggested contents:** `SDLC_PLAN.md`, `milestones/`, `backlog/`,
  `dependencies/`, `estimates/`, `risk-register.md`, and iteration plans where
  used.
- **Do not store:** fabricated dates/owners/capacity, current status copied
  without evidence, detailed requirement source text, or release history
  duplicated in `13_RELEASES_AND_VERSIONS/`.
- **Metadata and relationships:** item/milestone ID, status, accountable role,
  estimate basis, prerequisites, risk, exit criteria, and source requirement.
  Link requirements to `01_REQUIREMENTS/`, acceptance evidence to QA, and
  gate definitions to the governing SDLC artifact.
- **Skills and update trigger:** SDLC Planning and Governance (241), Project
  Planning Traceability (226), Roadmap & Project Planner (034), and Risk &
  Dependency Analyzer (033) update at scope, dependency, capacity, or milestone
  changes.
- **Output / acceptance:** sequenced deliverables with measurable acceptance
  gates and explicit provisional assumptions. Validate dependency cycles,
  owners, dates/ranges, and requirement links; rebaseline with a recorded
  reason instead of rewriting history.

### `04_DESIGN/` — approved solution design

- **Owns / place here:** UI/UX and Figma references, design system, wireframes,
  prototypes, architecture diagrams, database models, API/interface contracts,
  and technical decision records.
- **Suggested contents:** `architecture/`, `decisions/`, `diagrams/`,
  `database/`, `api-contracts/`, `ux/`, `design-system/`, and prototype links.
- **Do not store:** production credentials, duplicate implementation source,
  unapproved designs presented as accepted, or test evidence whose source is
  `06_TESTING_QA/`.
- **Metadata and relationships:** design ID/version/status, author/owner,
  affected requirements, review/approval scope and date, alternatives,
  consequences, and implementation links. Keep ADRs immutable after acceptance;
  supersede with a new decision.
- **Skills and update trigger:** Architecture Design (136), Architecture &
  Diagram Reconstruction (019), API Contract and REST Design (130), and
  SDLC and Design Gate Manager (238) update when architecture/interface/UI
  decisions are proposed, reviewed, or changed.
- **Output / acceptance:** design has evidence, rationale, review disposition,
  and traceability to requirements and implementation. Validate diagrams,
  contract consistency, accessible design criteria, and links. Keep one
  canonical artifact and link from other sections.

### `05_SOURCE_CODE/` — canonical implementation pointers

- **Owns / place here:** canonical source repository references, module maps,
  repository inventory, local source when this project workspace is itself the
  canonical code repository, and source ownership rules.
- **Suggested contents:** `REPOSITORY_MAP.md`, `module-ownership.md`, and
  pointers to canonical repositories/submodules/workspaces. Code itself stays
  in its established repository and stack-native layout.
- **Do not store:** copied repositories, vendored/generated builds presented
  as source, build output, secrets, or a second canonical implementation.
- **Metadata and relationships:** repository ID/remote/path/access scope,
  branch or revision when relevant, owner, last verified timestamp, and
  source-of-truth link. Link design/requirements to modules and changes to
  release/evidence records.
- **Skills and update trigger:** Project Registry (013), Project Structure
  Manager (227), architecture, and development skills use/update when a repo,
  module boundary, ownership, or canonical path changes.
- **Output / acceptance:** each codebase has one verified canonical location
  and an owner. Check path/remote existence and avoid copying private source.
  Document vendoring exceptions and update references when repositories move.

### `06_TESTING_QA/` — verification and defects

- **Owns / place here:** test strategy/plans/cases, manual/automated test
  definitions, API/integration/UI/E2E/regression evidence, coverage reports,
  quality gates, bug reports, and test environment notes.
- **Suggested contents:** `strategy/`, `plans/`, `cases/`, `api/`, `integration/`,
  `ui-e2e/`, `regression/`, `bugs/`, `evidence/`, and `coverage/` where
  generated outputs are intentionally retained.
- **Do not store:** production secrets/data, test results without command,
  version, scope, and timestamp, or test plans copied into release history.
- **Metadata and relationships:** test/defect ID, requirement/design link,
  environment/build/version, steps and expected/actual result, status, evidence
  path, owner, and severity. Link source changes and release candidates.
- **Skills and update trigger:** Test Strategy Generator (082), Automated
  Testing Engineer (074), Focused Function Testing (183), Requirements-to-Test
  Traceability (079), and relevant security/performance skills update for scope,
  implementation, or quality gate changes.
- **Output / acceptance:** each claimed verification points to reproducible
  evidence with pass/fail/blocked/not-run outcome. Validate requirement
  coverage, artifact safety, test version, and reproducibility; do not infer
  coverage or success from a test file's existence.

### `07_DOCUMENTATION/` — maintained project guidance

- **Owns / place here:** technical docs, API reference, installation/setup,
  user/developer guides, architecture narrative, troubleshooting, and project
  reports not owned elsewhere.
- **Suggested contents:** `architecture/`, `api/`, `developer-guide/`,
  `user-guide/`, `operations/`, and `reports/`; the root README and project
  index remain at root.
- **Do not store:** duplicate status or requirements sources, credentials,
  unsupported commands, copied external content without permission, or
  unreviewed output treated as authoritative.
- **Metadata and relationships:** audience, scope/version, owner, last
  verified date, related source/requirement, and links. Link to canonical
  operational, research, and verification records instead of cloning.
- **Skills and update trigger:** Documentation Engineering (173),
  Documentation Knowledge Management (174), Documentation Recovery (021), and
  Documentation Synchronization (094) update on user-facing behavior, setup,
  interface, architecture, or release changes.
- **Output / acceptance:** reader can complete the stated task using current,
  internally consistent instructions. Validate relative links, commands
  against available evidence, and drift. Archive obsolete guidance with a
  supersession pointer.

### `08_DEPLOYMENT/` — delivery configuration and run steps

- **Owns / place here:** deployment architecture, hosting references,
  CI/CD configuration, environment schemas/templates, infrastructure-as-code
  references, release deployment steps, rollback, and environment promotion
  rules.
- **Suggested contents:** `pipelines/`, `environments/`, `infrastructure/`,
  `deployment-guides/`, and `rollback/`; executable definitions may remain
  alongside code or in the platform's canonical repository.
- **Do not store:** actual secrets, tokens, private keys, production dumps,
  unmanaged manual drift, or duplicate pipeline configuration.
- **Metadata and relationships:** environment identifier/classification,
  owner, source revision, approvals, deployment/rollback version, and secret
  reference name (never the value). Link releases to `13_RELEASES_AND_VERSIONS/`
  and operational runbooks to `09_OPERATIONS/`.
- **Skills and update trigger:** DevOps and Container Orchestration (170),
  CI/CD Infrastructure Automation (149), Deployment & Environment Engineer
  (092), and release skills update when delivery configuration or environment
  behavior changes.
- **Output / acceptance:** repeatable, reviewed deployment procedure and
  tested rollback path where applicable. Validate placeholders, access
  controls, environment separation, and source ownership; never state
  production success without live evidence.

### `09_OPERATIONS/` — running and supporting the project

- **Owns / place here:** monitoring/alerting references, logs policy, incidents,
  troubleshooting, maintenance, backups/restore, support records, operational
  procedures, and service objectives.
- **Suggested contents:** `runbooks/`, `monitoring/`, `incidents/`,
  `maintenance/`, `backup-recovery/`, and `support/`.
- **Do not store:** credentials, raw sensitive logs, unredacted personal data,
  duplicated deployment source, or an incident resolution without evidence.
- **Metadata and relationships:** service/environment, incident/change ID,
  timestamps/time zone, impact, owner, severity, evidence references, recovery
  actions, and follow-up. Link deployment to `08_DEPLOYMENT/`, fixes to source,
  and lessons to `12_ROADMAP_AND_FUTURE_PLANS/`.
- **Skills and update trigger:** Logging Monitoring and Incident Management
  (206), Incident Response Root Cause (202), Production Deployment and Live
  Verification (216), and project maintenance skills update after operational
  changes, incidents, or review cadence.
- **Output / acceptance:** an authorized operator can diagnose and recover
  safely. Validate redaction, procedure currency, backup restore evidence, and
  access scope; retain only records allowed by policy and link incident
  artifacts rather than duplicating logs.

### `10_EVIDENCE_HISTORY/` — provenance and durable decisions

- **Owns / place here:** approved screenshots/recordings, verification
  evidence, important decisions/approvals, audit trail, and significant
  change-history pointers.
- **Suggested contents:** `evidence-register.md`, `decisions/` only if no
  existing decision source is canonical, `approvals/`, and restricted
  `attachments/` when policy permits.
- **Do not store:** secrets, unnecessary personal data, unredacted customer
  content, bulk duplicate source, or the only copy of a document owned by
  another area.
- **Metadata and relationships:** evidence ID, claim supported, source path or
  immutable reference/hash where appropriate, capture time, actor/role,
  scope/version, sensitivity, retention, and integrity. Link to its owning
  requirement, test, gate, release, or incident.
- **Skills and update trigger:** Project Artifact & Evidence Manager (084),
  Evidence & Status Engine (005), Project Memory & Handover (012), and audit
  skills update when a material claim or approval needs durable evidence.
- **Output / acceptance:** evidence is discoverable, attributable, scoped,
  access-controlled, and retained per policy. Verify references and redact
  before sharing; do not duplicate authoritative records or use evidence
  existence to imply approval.

### `11_AUTOMATION_AI/` — agent and automation governance

- **Owns / place here:** AI-agent instructions, approved workflows, MCP/tool
  references, reusable prompts, integration documentation, automation
  configuration pointers, and handover instructions.
- **Suggested contents:** `agents/`, `workflows/`, `prompts/`, `integrations/`,
  `automation/`, and `handover/`; executable config may live in the
  automation's canonical source repo.
- **Do not store:** credentials/tokens, hidden policy overrides, uncontrolled
  autonomous actions, duplicate global skill sources, or prompts with private
  project data unnecessarily embedded.
- **Metadata and relationships:** owner, version, trigger, allowed tools,
  permission scope, inputs/outputs, failure behavior, data classification,
  and evaluation evidence. Link shared skills to the global registry and
  project-specific instructions to `00_PROJECT_CONTROL/`.
- **Skills and update trigger:** AI Agent Skill Governance and Routing (128),
  MCP Tool Integration (207), MCP Integration Specialist (120), Automation
  Workflow Designer (116), and orchestration skills update on tool, trigger,
  permission, or agent behavior changes.
- **Output / acceptance:** humans can understand what executes, when, with what
  permissions, and how it fails. Validate secret references, allowlists,
  approval gates, versioning, and test status; do not duplicate global
  instructions.

### `12_ROADMAP_AND_FUTURE_PLANS/` — proposed and deferred work

- **Owns / place here:** future ideas, proposed/approved future features,
  deferred requirements, technical debt, enhancement opportunities, and
  long-term direction.
- **Suggested contents:** `ideas/`, `approved/`, `deferred/`, `technical-debt/`,
  `themes/`, and `decision-log.md`.
- **Do not store:** unapproved commitments as planned work, active task status
  duplicated from `14_PROJECT_STATUS_AND_NEXT_STEPS/`, or released feature
  history duplicated from `13_RELEASES_AND_VERSIONS/`.
- **Metadata and relationships:** idea/issue ID, category, current status,
  rationale, value/risk, evidence, dependencies, owner role, review date, and
  next decision. Link approved work to `03_PLANNING/`.
- **Skills and update trigger:** Roadmap & Future Feature Manager (103),
  Continuous Improvement Planner (107), Project Lifecycle Reassessment (113),
  and Planning/Traceability skills update during roadmap review or discovery
  of new debt/opportunities.
- **Output / acceptance:** items remain clearly proposed, approved, deferred,
  or cancelled with a disposition reason. Validate duplicate issue links and
  stale priorities; promote to an executable plan only with authorization and
  capacity assumptions.

### `13_RELEASES_AND_VERSIONS/` — release record

- **Owns / place here:** version history, changelog, release notes, plans,
  release status, release evidence references, and rollback records.
- **Suggested contents:** `CHANGELOG.md`, `releases/<version>/`, `plans/`,
  `evidence-index/`, and `rollback/`.
- **Do not store:** credentials, duplicate build artifacts unless policy
  requires retention, unverified user acceptance, or current implementation
  status copied from another source.
- **Metadata and relationships:** version/tag/commit, scope, date, approver,
  deployment target, known issues, verification and acceptance evidence,
  rollback reference, and release status. Link to deployment and operations.
- **Skills and update trigger:** Release & Version History Manager (102),
  Release & Rollback Manager (099), Production Readiness Release Management
  (219), and deployment verification update for each candidate, release, or
  rollback.
- **Output / acceptance:** an immutable, traceable account of what was
  released where and with what evidence. Validate version uniqueness,
  artifact provenance, approval, and rollback notes; distinguish created,
  verified, deployed, and accepted states.

### `14_PROJECT_STATUS_AND_NEXT_STEPS/` — current state and action

- **Owns / place here:** current evidence-backed project status, active work,
  blockers, verification gaps, upcoming milestones, and prioritized next
  actions.
- **Suggested contents:** `status-history/`, `blockers.md`, `milestone-view.md`,
  and links to root `PROJECT_STATUS.md` and `NEXT_ACTIONS.md`. Root files are
  canonical and should not be copied here.
- **Do not store:** unsupported completion claims, secret-bearing logs,
  historical status overwriting, or duplicated detailed backlog.
- **Metadata and relationships:** status timestamp/time zone, project
  version/milestone, source evidence, accountable role, dependencies,
  blockers, next action, and freshness. Pull from requirements, implementation,
  testing, releases, and operations without conflating them.
- **Skills and update trigger:** Unified Project Status & Next-Step Generator
  (104), Project Health Dashboard (111), Evidence & Status Engine (005), and
  Project Memory & Handover (012) update after verified progress, blockers,
  release, or scheduled status review.
- **Output / acceptance:** a new contributor can identify current stage,
  verified/unverified capability, blocker owner, and safe next action.
  Validate every claim against fresh evidence; preserve snapshots/history and
  link details to their canonical area.

## Root-level entry files

Root entry files are the project's quick-start and discovery surface. For
multi-repository projects, choose one governed workspace root and point each
source repository back to it where practical. Do not keep competing root
indexes or duplicate their full contents under `00_PROJECT_CONTROL/`.

### `README.md` — project front door

- **Purpose/content:** explain project name and purpose, audience, key
  capabilities, project type, prerequisites, safe quick start, and links to
  `PROJECT_INDEX.md`, status, contribution, and setup guides.
- **Recommended order:** purpose; current maturity caveat; features; supported
  environments; prerequisites; quick start; configuration using placeholders;
  documentation/navigation links; support/ownership.
- **Update when:** purpose, install/setup, supported versions, main features,
  repository layout, or onboarding changes.
- **Validation:** compare commands and claims to current manifests and evidence;
  verify relative links and secret-free examples. README is an overview, not
  the canonical requirements, status, or deployment runbook.

### `PROJECT_INDEX.md` — primary human/agent navigation

- **Purpose/content:** canonical table of contents with project identity,
  repository map, owner/source of truth, freshness, and links to all important
  artifacts across the 15 logical areas.
- **Recommended fields:** area, canonical path/URL, purpose, owner role,
  status/freshness, access classification, and related artifacts. Mark absent
  areas `NOT_APPLICABLE` or `MISSING`, rather than linking to imaginary files.
- **Update when:** an authoritative path, owner, lifecycle artifact, repository,
  or access boundary changes.
- **Validation:** resolve each internal path/link; check no duplicate primary
  entry point, path alias confusion, or secret/private URL leakage. Keep it
  concise and link rather than copying documents.

### `PROJECT_STATUS.md` — current evidence-backed snapshot

- **Purpose/content:** project identity/model/stage, separate workstream
  statuses, verified outcomes, unverified gaps, blockers/risks, active
  milestone, last checked time, evidence references, and next review.
- **Update when:** status changes with evidence or the freshness interval
  expires. Record `NOT_CHECKED` rather than silently reusing stale state.
- **Validation:** every claim has an evidence reference and timestamp;
  implementation, verification, release, and acceptance states remain
  independent. Preserve history in the history area, not by bloating the
  current snapshot.

### `project-manifest.yaml` — machine-readable project identity

- **Purpose/content:** stable project ID/name/type, canonical repositories and
  paths, owner role, technologies, lifecycle model/stage, status source,
  access scope, freshness, and links to entry docs.
- **Recommended shape:** use the project schema/template in the reference
  material; represent unknown values explicitly as `unknown`/`null`, not
  guessed data. Keep secrets and private tokens out.
- **Update when:** identity, canonical remote/path, stack, owner, lifecycle
  model, or status source changes.
- **Validation:** parse as YAML with the project's available validator if
  authorized; check unique stable ID, required fields, valid references,
  allowed status values, and consistency with `PROJECT_INDEX.md`. Manifest
  describes identity, it does not prove runtime state.

### `NEXT_ACTIONS.md` — prioritized actionable handoff

- **Purpose/content:** short, prioritized next tasks, each with reason,
  completion criteria, dependencies/blocker, owner role if assigned, evidence,
  and target milestone where known.
- **Update when:** a task is completed, blocked, superseded, reprioritized, or
  new verified work appears.
- **Validation:** every action is specific and actionable; do not invent
  assignees/dates. Link to canonical backlog/roadmap, remove duplicates, and
  distinguish approved work from proposals.

## Status model and transitions

Maintain a **project lifecycle stage** separately from each item's status.
Project stage can be Initiation, Discovery, Requirements, Design, Implementation,
Verification, Release, Operations/Maintenance, or Closure; the selected SDLC
may iterate or combine these. The statuses below apply independently to
requirements, features, documentation, work, releases, ideas, risks, and
actions where appropriate.

### Status meanings

| Status | Meaning | Minimum evidence/guard |
|---|---|---|
| `PROPOSED` | Idea or request exists; not a commitment | Source/request and proposal owner or origin |
| `UNDER_REVIEW` | Authorized review/decision is in progress | Reviewer/decision owner, scope, and review date |
| `APPROVED` | Authorized party accepted scope/decision | Explicit approval record, approver role, version/scope |
| `PLANNED` | Approved or otherwise authorized work is sequenced | Plan/backlog reference, dependencies, exit criteria; approval remains a separate field |
| `IN_PROGRESS` | Work has started | Owner role and current work/evidence reference |
| `BLOCKED` | Progress cannot safely continue | Blocker, impact, responsible resolver, next action |
| `VERIFIED` | Declared acceptance/verification criteria passed for stated scope | Reproducible test/review/evidence, version, environment, date, reviewer as applicable |
| `RELEASED` | Identified version was made available/deployed to stated target | Version/commit, target, deployment/release evidence; user acceptance is separate |
| `DEFERRED` | Decision is to postpone without cancelling | Decision owner, rationale, review trigger/date if known |
| `CANCELLED` | Work is intentionally stopped | Authorized disposition and reason; preserve historical evidence |

`UNKNOWN`, `MISSING`, `OUTDATED`, `NOT_CHECKED`, and `NOT_APPLICABLE` are
information-quality markers, not lifecycle statuses. Use them as a separate
field when relevant. Do not map absence of evidence to a positive status.

### Status coverage by project area

Maintain these areas as independent facts in `PROJECT_STATUS.md` or a linked
status source. Each row points to its detailed canonical artifact; the status
snapshot must not become a duplicate document store.

| Status area | Canonical detail/source | What the status snapshot must say |
|---|---|---|
| Project identity | `project-manifest.yaml`, `00_PROJECT_CONTROL/` | Confirmed/verified identity or `UNKNOWN`, canonical repository, owner role, last-checked evidence |
| Requirements | `01_REQUIREMENTS/` | Requirement status, approval, acceptance criteria, traceability gaps |
| Implementation | `05_SOURCE_CODE/` and canonical source repository | Implemented scope/version separately from test and release status |
| Verification | `06_TESTING_QA/` | Tested/verified/not-run/blocked result, environment, evidence and uncovered scope |
| Documentation | `07_DOCUMENTATION/` and root README | Current/outdated/missing state, audience/scope, last-verified evidence |
| Current work | `03_PLANNING/` and active backlog | In-progress owner role, milestone, dependencies, blockers and next action |
| Releases | `13_RELEASES_AND_VERSIONS/` | Version, target, deployment evidence, release approval and user acceptance separately |
| Upcoming work | `03_PLANNING/` | Authorized planned items, dependencies, exit criteria; label unapproved work distinctly |
| Future ideas | `12_ROADMAP_AND_FUTURE_PLANS/` | Proposed/deferred/cancelled disposition and next review/decision |
| Risks and technical debt | `03_PLANNING/` risk register and linked issue source | Impact/likelihood, owner, mitigation, residual risk and decision/status |
| Dependencies and blockers | `03_PLANNING/`, `09_OPERATIONS/`, or canonical issue tracker | Dependency/blocker, effect, resolver role, evidence and condition to unblock |
| Next actions | `NEXT_ACTIONS.md` and canonical backlog | Priority, reason, prerequisite, owner if assigned and measurable completion criteria |

### Valid transition guidance

Typical path: `PROPOSED -> UNDER_REVIEW -> APPROVED -> PLANNED -> IN_PROGRESS
-> VERIFIED -> RELEASED`. This is not a mandatory linear workflow; a project's
approved SDLC may add iteration, review, or deployment steps.

- `PROPOSED -> UNDER_REVIEW`: assign review scope and decision owner.
- `UNDER_REVIEW -> APPROVED`: record explicit authorized approval and scope.
- `UNDER_REVIEW -> DEFERRED/CANCELLED`: record disposition authority and reason.
- `APPROVED -> PLANNED`: define tasks, dependencies, owner/capacity assumptions,
  and objective exit criteria. Approval does not mean work has started.
- `PLANNED -> IN_PROGRESS`: record start evidence and accountable role.
- `IN_PROGRESS -> BLOCKED`: record blocker, impact, resolver, and next action;
  resume only when blocker evidence is resolved.
- `IN_PROGRESS -> VERIFIED`: only after all named acceptance checks pass for
  the exact scope/version; partial results remain partial or in progress.
- `VERIFIED -> RELEASED`: require release authorization and deployment/version
  evidence. Verification is not deployment.
- `RELEASED -> VERIFIED` or `IN_PROGRESS`: only as a new version/scope or
  corrective cycle; do not rewrite history for the old release.
- `RELEASED -> user accepted`: track a separate acceptance field/state with
  user evidence. Release alone is not acceptance.
- Reopening `DEFERRED` or `CANCELLED` requires a new review/approval record and
  preserves the previous disposition.

### Record schema

For material status entries include: `itemId`, title, category, status,
`lastChecked` timestamp with time zone, evidence reference(s), owner role,
dependencies, blockers, next action, version/milestone, approval/acceptance
state where relevant, and confidence/limitations. Use stable IDs and link the
canonical artifact; do not repeat long descriptions in status summaries.

### Non-conflation rules

- Implemented does not mean tested; tested does not mean verified.
- Verified does not mean released; released does not mean user-accepted.
- Planned does not mean approved; proposed does not mean committed.
- Track implementation, verification, documentation, release, and acceptance
  independently for each important feature or deliverable.
- Mark stale or unavailable evidence explicitly and use the least-advanced
  status supported by current evidence.

## Lifecycle model guidelines

Select the actual model with the project governance owner and stakeholders. Do
not infer it from folder names. Store the model and tailoring decisions in
`00_PROJECT_CONTROL/` or `03_PLANNING/`, with a single canonical path in the
index.

| Model/pattern | Structure and evidence adaptation |
|---|---|
| Predictive/sequential or V-model | Baseline requirements/design and trace each to implementation and corresponding verification/acceptance evidence; gate exit evidence before transitions. |
| Agile/iterative/incremental | Keep stable product boundaries; record scoped increment goals, decisions, tests, review, and acceptance per iteration without cloning source trees. |
| Spiral/risk-driven | Make risk register, prototypes, experiment evidence, residual risk, and next-cycle decision discoverable. |
| DevOps/continuous delivery | Version pipeline, infrastructure, tests, deployment, rollback, observability, and promotion evidence; approvals remain explicit. |
| Research/AI/data lifecycle overlay | Add problem/hypothesis, provenance, datasets/model versions, evaluation/reproducibility, ethics/privacy, monitoring, and retirement artifacts where relevant. |
| Automation/system integration | Track workflow contract, triggers, permissions, dependencies, failure/recovery, owner, monitoring, and change approval with implementation and test evidence. |

At each stage gate, record entry criteria, exit criteria, accountable approver,
evidence links, result, date, exceptions, and next authorized stage. Gate
definitions belong to the approved SDLC governance artifact; this skill only
maps their evidence to discoverable locations. Do not represent a gate as
passed because its folder/template exists.

## Workflows

### A. New project initialization

1. Inspect requested scope, existing repositories, user-provided artifacts,
   team constraints, and project identity. Resolve canonical repositories
   rather than assuming the current directory is the only project root.
2. Classify project type, size/complexity, data sensitivity, deployment shape,
   lifecycle model, and required governance.
3. Discover existing source/docs and identify canonical locations and owners.
4. Map content to the logical areas and root entry files; note missing,
   unknown, and inapplicable areas.
5. Propose a minimal tree, ownership map, manifest fields, entry files, and
   lifecycle artifact locations. Ask before consequential/destructive changes,
   external actions, or decisions that require authority.
6. Create only approved/useful folders and templates. Keep source in its
   canonical repository; use placeholders for secrets.
7. Populate README, index, manifest, status, and next actions from evidence.
   Mark unavailable facts `UNKNOWN` or `NOT_CHECKED`.
8. Validate paths, relative links, manifest consistency, duplicate ownership,
   status evidence, and secret handling.
9. Record initial model/stage, validation results, open decisions, and
   prioritized next actions; hand off gate decisions to SDLC governance.

**Exit:** one usable entry point, resolved repository identity, minimal useful
structure, trustworthy initial status, and explicit unknowns. No unapproved
source movement or fabricated project fact.

### B. Existing project adaptation

1. Inspect the repository/worktree and instructions before edits; distinguish
   tracked source, generated output, and user changes.
2. Understand architecture, code conventions, current roots, canonical source
   locations, and existing governance.
3. Map existing files to logical areas; record path, owner, freshness, and
   canonical/duplicate status.
4. Preserve repositories and working paths. Use an index/reference for
   content held elsewhere; do not move or copy source to satisfy this standard.
5. Report missing, outdated, unknown, and unverified information distinctly.
6. Propose structural changes with reason, effect, alternatives, risk,
   dependencies, and migration/rollback plan.
7. Apply only scoped approved changes; validate links, consistency, and
   non-regression of established conventions.

**Exit:** evidence-backed current map and minimal adaptation plan; no
unrequested restructuring.

### C. Reverse engineering and project recovery

1. Inventory source, manifests, configs, APIs, schemas, tests, dependency
   declarations, and docs; protect secrets/private data.
2. Trace implemented features through source and available tests/configuration.
   Separate observed implementation from intended behavior.
3. Identify incomplete/unverified behavior, drift, dead/uncertain paths, and
   unavailable runtime evidence.
4. Reconstruct requirements and architecture with source/file/line references,
   confidence labels, and explicit unknowns.
5. Generate missing diagrams/docs only from supported evidence; avoid claiming
   runtime behavior from static source alone.
6. Update status, gaps, risks, roadmap candidates, and next actions without
   silently treating inferred items as approved work.
7. Have the relevant recovery/discovery/architecture skill review its domain
   deliverables and record the evidence references.

**Exit:** as-built map, evidence-linked requirements/architecture, confidence
and uncertainty, verification gaps, and actionable next steps.

### D. Ongoing project maintenance

1. Compare changed files, commits, releases, and approved task outcomes with
   the index and artifact map.
2. Identify affected docs, requirements, tests, statuses, decisions, risks,
   roadmap, deployment, and release history.
3. Update only status supported by new evidence; retain old state as history.
4. Record material decisions and change provenance at the canonical location.
5. Refresh roadmap and next actions; preserve deferred/cancelled items with
   rationale.
6. Add release history only for an identified release/version and evidence.
7. Detect misplaced/duplicate/stale docs; propose canonicalization rather than
   destructive cleanup.
8. Validate links, freshness, status transitions, secrets, and references.

**Exit:** current entry points match verified project changes, history is
preserved, and remaining gaps are visible.

### E. Project handover

1. Confirm recipient, scope, freshness, and access needs; redact sensitive
   details.
2. Summarize purpose, architecture, canonical repositories/paths, and setup
   instructions with evidence.
3. State current lifecycle stage and distinguish implemented, tested,
   verified, released, and accepted capabilities.
4. List known issues, blockers, dependencies, risks, and decisions pending.
5. Prioritize next steps with reasons, prerequisites, owner roles when known,
   and completion criteria.
6. Link the project index, key requirements/design/test/release/operations
   artifacts, and recent handover history.
7. Validate links, command freshness, evidence dates, access, and secrets.

**Exit:** a new owner can locate the source of truth and choose a safe, specific
next action without mistaking stale notes for current state.

## Documentation and naming standards

- Prefer human-readable, stable filenames; use consistent `UPPER_SNAKE_CASE`
  for root governance entries if the existing project follows that style.
  Preserve established framework conventions elsewhere.
- Use stable IDs such as `REQ-001`, `RISK-001`, `ADR-001`, `TEST-001`,
  `BUG-001`, `DEC-001`, `EVD-001`, `REL-1.2.0`, and `ACT-001`; do not
  renumber IDs after publication.
- Include title, purpose, owner role, status, created/updated timestamp with
  time zone, version/scope, evidence/source links, and sensitivity/retention
  fields where appropriate.
- Use relative links within a repository; use canonical remote/path references
  for other repositories. Validate anchor/path resolution.
- Distinguish facts, decisions, assumptions, proposals, and inferences.
- Keep current summaries concise and link to detailed canonical records.
- Record dates in ISO 8601 format; avoid timestamps without a time zone where
  event ordering matters.
- Put secrets in an approved secret manager, never in docs, sample manifests,
  prompts, logs, screenshots, or committed templates.

## Security, privacy, and change controls

- Use least privilege; verify repository identity and access scope before
  external or multi-repository operations.
- Treat evidence, logs, screenshots, agent prompts, and research notes as
  potentially sensitive. Redact before storing or sharing.
- Store secret names/references only when useful; never store secret values.
- Preserve user changes and history. No broad moves, deletes, rewrites, or
  external publication without explicit scope/approval.
- Require the applicable owner/approver for decisions, gates, deployments,
  external cost, data processing, retention, or production changes.
- If permission, identity, provenance, or evidence is missing, stop the gated
  action, mark the gap, and give the safe next step.

## Failure handling

- **Ambiguous project/repository:** list evidence-backed candidates and ask
  before writing.
- **Missing facts:** mark `MISSING`, `UNKNOWN`, `OUTDATED`, or `NOT_CHECKED`;
  do not infer a value to make a template look complete.
- **Conflicting records:** preserve both references, identify owners and
  consequences, request a decision; do not silently select a winner.
- **Unavailable tool/runtime:** complete safe static work if possible and
  label runtime/functional checks `NOT_TESTED`.
- **Validation failure:** report the exact path/check/error; do not mark
  success, hide the failure, or replace user data.
- **Partial work/interruption:** record completed/remaining steps, changed
  paths, rollback boundary, and evidence; resume from current workspace state.

## Evaluation and scenario checklist

Score each applicable item `PASS`, `FAIL`, or `NOT_TESTED`, with evidence:

- [ ] Skill ID/name/frontmatter/H1/path match repository conventions.
- [ ] Every one of the 15 logical areas has operational ownership, contents,
      exclusions, metadata, relationships, triggers, acceptance, and
      maintenance rules.
- [ ] Five root entry files have purpose, structure, update triggers, and
      validation.
- [ ] Initialization and existing-project adaptation preserve canonical source.
- [ ] Status definitions/transitions keep approval, implementation, verification,
      release, and user acceptance separate.
- [ ] Claims are backed by evidence; freshness and unknowns are explicit.
- [ ] Index links resolve and each artifact has one canonical home.
- [ ] Parent/child skills and workflows/templates/tools/evaluations are
      correctly distinguished.
- [ ] Reverse engineering, maintenance, and handover workflows are actionable.
- [ ] Secret handling and destructive/external approval boundaries are explicit.
- [ ] Templates are optional, internally consistent, and not forced on projects.
- [ ] No duplicate ID/name or unjustified overlapping skill is introduced.

Scenario execution record (update only after actually running a scenario):

| Scenario | Expected check | Status |
|---|---|---|
| New small software project | Minimal structure, useful entry files, no empty folders, evidence-backed initial status | `NOT_TESTED` |
| Existing large multi-repository application | Canonical repos preserved, index links and ownership map resolve, no source duplication | `NOT_TESTED` |
| Undocumented project requiring reverse engineering | Reconstructed map cites evidence and identifies uncertainty | `NOT_TESTED` |
| Incomplete testing and outdated docs | Verification and documentation states remain distinct; gaps become next actions | `NOT_TESTED` |
| Active development, releases, and future plans | Active/released/proposed/deferred work and version evidence remain separate | `NOT_TESTED` |

Structural validation confirms format and references only; it does not prove
functional quality, project adoption, or scenario behavior.

## Acceptance criteria

- A human/agent has one primary project index and a machine-readable identity
  manifest when appropriate.
- Every applicable logical area has one owner and a canonical information
  location, with links instead of redundant copies.
- Structure adapts to project size, type, architecture, and selected lifecycle.
- Project status separates lifecycle, approval, implementation, verification,
  documentation, release, and acceptance.
- Every material completion claim has fresh, scoped evidence.
- Initialization, adaptation, recovery, maintenance, and handover outputs meet
  their workflow exit criteria.
- Unknowns, stale facts, blockers, skipped checks, and untested scenarios are
  explicit.
- No secret exposure, invented fact, unapproved destructive change, or
  duplicate capability is introduced.

## Reusable templates

Optional templates for the manifest, index, overview, status, requirements,
research, feasibility, roadmap, milestone/task tracker, architecture, test
plan/case, bug, deployment, incident, decision, evidence, release, future
planning, next actions, and handover are in
[`references/PROJECT_ARTIFACT_TEMPLATES.md`](references/PROJECT_ARTIFACT_TEMPLATES.md).
Copy only the template a project needs, populate from evidence, and adapt it
to existing project standards.

## Maintenance

Review this skill when the repository registry/schema, global skill hierarchy,
project status policy, SDLC governance, or template references change. Keep the
stable ID and sequence; update name/path only through the repository's approved
registry workflow. Re-run structural validation after edits. Record scenario
results only when performed, and retain source-history/provenance separately
from current canonical guidance.
