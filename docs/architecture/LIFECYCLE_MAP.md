# Lifecycle and Candidate Map

**Status:** Implemented lifecycle classification for the canonical catalogue. Candidate IDs and exact names come from `global-skills/SKILL_CANDIDATE_CATALOGUE.md`. The source-level coverage/evidence baseline is in `global-skills/SKILL_TO_80_CANDIDATE_MAPPING.md`.

Canonical skill display names use `Skill - NNN - Purpose`, where `NNN` is the
stable display sequence in lifecycle order. Stable directory IDs remain
unchanged so registry, dependency, and provenance links continue to resolve.
The authoritative sequence is generated in
[`registry/canonical-index.json`](../../registry/canonical-index.json).

| Execution order | Lifecycle group |
|---:|---|
| 10 | Foundation |
| 20 | Recovery and context restoration |
| 30 | Research and planning |
| 40 | Development |
| 50 | Testing |
| 60 | Security |
| 70 | Quality |
| 80 | Project knowledge |
| 90 | Delivery |
| 100 | Roadmap and release |
| 110 | Maintenance |
| 120 | Automation and orchestration |

## Lifecycle stages

| Stage | Candidate IDs | Main outputs | Current reusable evidence |
|---|---|---|---|
| Discovery and context | 03–09, 14, 18, 63, 74 | Project identity, context snapshot, as-built evidence, gaps and confidence | Discovery/audit skills in both sources; project-registry and formal evidence contracts remain gaps. |
| Research and feasibility | 16, 17, 19, 25, 64 | Source-verified options, feasibility/risk comparison, version-aware findings | Architecture and dependency-watch skills; general research and problem-analysis capabilities are not established. |
| Requirements and governance | 02, 10, 15, 20, 24, 33 | Approved requirements, gates, decisions, traceability | Existing requirements and SDLC skills/templates; common status and approval enforcement are not verified. |
| Planning and architecture | 11, 22, 23, 26, 71 | Architecture decisions, project structure, sequenced plan and risk register | Architecture, project-structure, and planning skills; compose them through workflows. |
| Development and integration | 27–32 | Standards mapping, bounded changes, code/API/data integration | Existing stack-specific skills are broad coverage; avoid one generic implementation mega-skill. |
| Verification and security | 09, 34–42 | Test strategy/results, review findings, security/performance evidence, readiness decision | Testing and security skills exist; runtime evidence is not established by this discovery. |
| Documentation and knowledge | 13, 43–45, 58, 60, 72, 73, 75, 77 | Source-linked docs, reports, project knowledge/artifact index | Documentation/logging skills and templates; knowledge ingestion and centralized evidence storage remain proposed. |
| Deployment and release | 46–50, 79 | Build/package evidence, deployment plan, rollback, acceptance/sign-off, release record | Build/deployment/release skills and templates; production authorization remains explicit and separate. |
| Maintenance and continuity | 05, 41, 56, 59, 61, 65, 68, 76 | Incident recovery, scheduled review, handover, trends, status and lessons | Scheduling, RCA, observability and continuity skills; durable state, trends and dashboard remain unverified. |
| Orchestration and continuous improvement | 01, 06, 21, 51–57, 62, 66, 67, 69, 70, 78, 80 | Skill routing, approval, workflow checkpoints, evaluation and prioritized improvement | Orchestration policy, skill governance, and token efficiency guidance exist; automated enforcement/services are not verified. |

## Per-candidate proposed disposition

`Existing skill` means reuse by source reference after review, not copied or verified. `Workflow` composes capabilities. `Shared component` means a contract/policy/template rather than an application service. `New skill candidate` is a proposal only. IDs are retained exactly and are not globally unique skill IDs.

| ID | Candidate | Primary lifecycle | Proposed form | Reuse/gap decision |
|---:|---|---|---|---|
| 01 | Global Skills Framework | Orchestration | Shared contract | Reconcile authoring guides, schema, and validators; do not make a monolithic meta-skill. |
| 02 | Global Development Rules | Requirements and governance | Shared rules | Unify precedence and scoped exceptions from existing governance/security policies. |
| 03 | Project Registry | Discovery and context | Shared registry component | Missing canonical identity schema; start with static data contract, not a service. |
| 04 | Project Context Analyzer | Discovery and context | Existing skill | Reuse project-discovery-audit; enhance evidence freshness and bounded outputs. |
| 05 | Project Memory & Handover | Maintenance and continuity | Workflow | Compose existing continuity and status guidance; add project-isolated state contract. |
| 06 | Evidence & Status Engine | Orchestration | Shared evidence/status contracts | Existing status guidance is partial; no engine/service assumed. |
| 07 | Existing Project Recovery | Discovery and context | Workflow | Compose discovery, diagnostics, recovery, QA, and handover. |
| 08 | Reverse Engineering & Code Archaeology | Discovery and context | Workflow | Extend architecture/discovery procedures with reverse mapping and confidence labels. |
| 09 | Runtime Behavior Verification | Discovery and verification | Workflow | Compose focused, functional, API, and UI tests; require approval for execution. |
| 10 | Requirements Reconstruction | Requirements and governance | Workflow | Use discovery and requirements skills; distinguish observed from inferred requirements. |
| 11 | Architecture & Diagram Reconstruction | Planning and architecture | Workflow | Compose architecture and diagram/documentation resources; validate claims to evidence. |
| 12 | UI/UX Recovery | Discovery and context | Workflow | Compose UI research, accessibility, and functional verification; no duplicate broad skill. |
| 13 | Documentation Recovery | Documentation and knowledge | Workflow | Extend documentation engineering with provenance and completeness. |
| 14 | As-Built Consistency Auditor | Discovery and context | Workflow | Combine documentation, code, test, and runtime evidence without rewriting sources. |
| 15 | Lifecycle Gap Analyzer | Requirements and governance | Workflow | Compose lifecycle stage gates and risk evidence; no separate duplicate skill. |
| 16 | Real-World Problem Analyst | Research and feasibility | New skill candidate | No direct skill found; define user evidence, measurable value, hypotheses, and falsification. |
| 17 | Technical Research Agent | Research and feasibility | New skill candidate | No general research skill found; require dated primary-source citations and uncertainty. |
| 18 | Existing Solution & Duplicate Work Detector | Discovery and context | Workflow | Add reuse-before-build review with privacy and provenance boundaries. |
| 19 | Feasibility & Technology Evaluator | Research and feasibility | Workflow | Use architecture, research, dependency, and risk skills with a consistent comparison template. |
| 20 | Requirements Engineering | Requirements and governance | Existing skill | Reconcile existing requirements skills; retain clear user-journey specialization. |
| 21 | Prompt Engineering Intelligence | Orchestration | Shared evaluation workflow | Separate prompt quality/evaluation from token/context efficiency; compare source variants. |
| 22 | Roadmap & Project Planner | Planning and architecture | Existing skill | Reuse planning skills and add explicit dependency/capacity views where supported. |
| 23 | Risk & Dependency Analyzer | Planning and architecture | Shared template + workflow | Reuse dependency graph and risk policy; standardize ownership and mitigation state. |
| 24 | User Approval & Decision Manager | Requirements and governance | Shared approval/decision contract | Policy text exists; no controller or authorization service is claimed. |
| 25 | Environment & Dependency Manager | Research and feasibility | Workflow | Compose environment readiness, dependency lifecycle, and config/secret skills. |
| 26 | Architecture & Design Implementation | Planning and architecture | Workflow | Route approved design into existing frontend/backend/domain skills and verification. |
| 27 | Development Standards Enforcer | Development and integration | Shared rule + workflow | Reuse coding standards and repository policies; keep exceptions explicit. |
| 28 | Feature Implementation Agent | Development and integration | Workflow | Compose requirement, plan, domain implementation, review, test and docs; no generic mega-skill. |
| 29 | Bug Diagnosis & Repair Agent | Development and integration | Workflow | Compose RCA then approval-bounded fix, impact check, regression and recovery. |
| 30 | API & Database Specialist | Development and integration | Existing skills | Reuse API and database skills independently with shared integration contracts. |
| 31 | Integration & Compatibility Engineer | Development and integration | Workflow | Compose integration tests and compatibility skills using explicit version matrix. |
| 32 | Code Review & Refactoring Agent | Development and integration | Workflow | Separate review-only findings from approved refactoring work. |
| 33 | Requirements-to-Test Traceability | Requirements and governance | Shared traceability contract | Extend existing RTM guidance; require bidirectional IDs and result evidence. |
| 34 | Test Strategy Generator | Verification and security | Existing skill | Reuse QA/test-strategy skills; enhance risk-based selection and exit criteria. |
| 35 | Automated Testing Engineer | Verification and security | Existing skills | Compose unit/API/UI/automation skills; retain scope-specific modules. |
| 36 | Edge-Case & Randomized Testing | Verification and security | Workflow extension | Add seeded, bounded property/boundary test procedure; new skill only if distinct demand is proven. |
| 37 | UI/UX & Accessibility Tester | Verification and security | Existing skill | Reuse accessibility and functional-testing skills with explicit manual/automated evidence. |
| 38 | Security Auditor | Verification and security | Existing skill | Reuse appsec skill; keep privacy and identity work separately owned. |
| 39 | Performance Auditor | Verification and security | Existing skill | Reuse performance profiling; require comparable baseline/workload evidence. |
| 40 | Regression & Change Impact Analyzer | Verification and security | Workflow | Compose diff impact analysis and targeted verification. |
| 41 | Test Failure & Root-Cause Analyzer | Verification and security | Workflow | Compose test strategy with diagnostic RCA and flake/environment classification. |
| 42 | Quality Gate & Readiness Evaluator | Verification and security | Workflow | Aggregate existing evidence; return ready/conditional/not-ready, not release authority. |
| 43 | Documentation Generator | Documentation and knowledge | Existing skill | Reuse documentation engineering with source and uncertainty checks. |
| 44 | Documentation Synchronization | Documentation and knowledge | Workflow | Define source-of-truth, owner, update/review, and drift closure. |
| 45 | Project Report & Diagram Generator | Documentation and knowledge | Shared templates + workflow | Reuse documentation and diagram patterns; validate source links and output shape. |
| 46 | Build & Packaging Verifier | Deployment and release | Workflow | Compose project-native build/package skills under command approval policy. |
| 47 | Deployment & Environment Engineer | Deployment and release | Existing skills | Reuse DevOps/deployment skills; separate preparation, execution, and live verification. |
| 48 | Release & Rollback Manager | Deployment and release | Workflow | Reuse release/deployment skills and rollback templates; require explicit release gate. |
| 49 | User Acceptance & Sign-Off Manager | Deployment and release | Workflow | Compose acceptance testing with an authorized stakeholder decision record. |
| 50 | Final Project Completion Auditor | Deployment and release | Workflow | Aggregate requirement, quality, docs, release, and handover evidence. |
| 51 | MCP Integration Specialist | Orchestration | Existing skill | Reuse enterprise MCP skill after compatibility and permission review. |
| 52 | Automation Workflow Designer | Orchestration | Existing skill + shared workflow template | Reuse scheduling and orchestration references; require idempotency and recovery branches. |
| 53 | Skill Selection & Orchestration Engine | Orchestration | Shared policy/component | Start as static routing/dependency metadata; runtime engine remains deferred. |
| 54 | Parallel Agent Coordinator | Orchestration | Shared coordination policy | No runtime coordinator verified; constrain to ownership/conflict/handoff rules initially. |
| 55 | Task Queue & Dependency Scheduler | Orchestration | Shared task/dependency contract | Scheduling guidance exists; do not create queue service before a concrete requirement. |
| 56 | Workflow Failure & Recovery Manager | Orchestration | Workflow | Compose checkpoints, RCA, retries, and compensation rules; no automatic replay of side effects. |
| 57 | Approval & Permission Controller | Orchestration | Shared approval policy/contract | Begin with command/action scope policy; runtime enforcement is not established. |
| 58 | Logs, Audit Trail & Reporting | Documentation and knowledge | Shared evidence/audit contract | Reuse logging patterns; define privacy, retention, access, and redaction before storage. |
| 59 | Event & Scheduled Trigger Manager | Maintenance and continuity | Workflow | Reuse scheduler guidance; trigger registry/runtime is deferred. |
| 60 | Cross-Project Reuse & Knowledge Manager | Documentation and knowledge | Shared provenance policy + workflow | Search only authorized metadata; enforce project isolation and consent. |
| 61 | Project Health Dashboard | Maintenance and continuity | Static report/template | No dashboard service; begin with freshness-aware generated reports if approved. |
| 62 | Automated Backlog Generator | Planning and architecture | Workflow | Convert verified findings into deduplicated tasks; require owner/priority evidence. |
| 63 | Continuous Project Auditor | Discovery and context | Workflow | Compose discovery, security, and performance audits with authorized cadence. |
| 64 | Dependency & Compatibility Monitor | Research and feasibility | Workflow | Compose dependency watch, compatibility, and upgrade skills; freshness source required. |
| 65 | Incident & Error Trend Analyzer | Maintenance and continuity | Workflow extension | Requires authorized history and privacy-safe aggregation; no trend service verified. |
| 66 | Skill Evaluation & Improvement | Orchestration | Shared validation workflow | Extend static schema checks with scenario/effectiveness evidence. |
| 67 | Automation Cost & Performance Optimizer | Orchestration | Workflow/report | Reuse token and profiling guidance; instrument only with approved comparable measurements. |
| 68 | Project Learning & Lessons Manager | Maintenance and continuity | Shared template + workflow | Opt-in, evidence-backed lessons with scope, retention, and privacy controls. |
| 69 | Project Lifecycle Reassessment | Continuous improvement | Workflow | Compose lifecycle and discovery evidence with cadence and maturity criteria. |
| 70 | Continuous Improvement Planner | Continuous improvement | Workflow | Convert verified outcomes into owned, measurable actions and review dates. |
| 71 | Universal Project Structure Architect | Planning and architecture | Existing skill | Reuse structure and setup skills; keep recommendations technology- and scale-aware. |
| 72 | Project Manifest & Index Generator | Discovery and context | Shared schema + future generator | Define identity/provenance/freshness contract before any generator implementation. |
| 73 | Project Knowledge Ingestion Engine | Documentation and knowledge | Deferred integration/service capability | No ingestion engine found; require authorization, redaction, indexing and refresh design. |
| 74 | Project Context Completeness Auditor | Discovery and context | Shared preflight workflow | Reuse discovery; define task-specific sufficiency and safe-next-action criteria. |
| 75 | Project Knowledge Synchronization Agent | Documentation and knowledge | Workflow | Reuse docs/continuity guidance; add ownership and conflict-resolution protocol. |
| 76 | Project Handover & Session Recovery Agent | Maintenance and continuity | Workflow | Reuse continuity/token skills; require canonical, freshness-checked project state. |
| 77 | Project Artifact & Evidence Manager | Documentation and knowledge | Shared evidence contract | Define provenance, integrity, sensitivity, access, and retention; no store claimed. |
| 78 | Roadmap & Future Feature Manager | Continuous improvement | Existing planning skill + workflow | Reuse project planning; distinguish ideas, proposals, approved commitments, and deferrals. |
| 79 | Release & Version History Manager | Deployment and release | Shared release record + workflow | Reuse release engineering; no release ledger/service is verified. |
| 80 | Unified Project Status & Next-Step Generator | Continuous improvement | Shared status contract + workflow | Derive only from fresh evidence; expose blockers and unknowns rather than guessing. |

## Coverage and evidence caution

All 80 IDs have a primary lifecycle home and proposed resource form. This architecture classification is **not** a new coverage claim. The source mapping reports 0 full, 19 partial, 16 indirect, 41 duplicate/overlap, and 4 missing; those statuses remain a discovery snapshot. Candidate 16 and 17 are the only initial proposals for genuinely new standalone skills, still subject to owner approval and validation. Other gaps should first be handled by improving existing skills, shared contracts, templates, or workflows.
