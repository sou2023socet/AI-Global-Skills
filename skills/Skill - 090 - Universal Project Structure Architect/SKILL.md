description: 'Recommend a repository structure aligned to the selected SDLC model, project evidence, technology, scale, team ownership, and current conventions.'
---
id: universal-project-structure-architect
name: Skill - 090 - Universal Project Structure Architect
candidateIds: ["71"]
version: 0.1.0
status: implemented
verification: structurally-validated
lifecycleGroup: project-knowledge
---

# Skill - 090 - Universal Project Structure Architect

## Purpose

This canonical instruction package implements the approved candidate contract for
**Universal Project Structure Architect**. It is reusable guidance, not an autonomous runtime or
permission grant.

Use Universal Project Structure Governance (Skill 268) when the task needs the
shared lifecycle-to-artifact contract or gate evidence map. This skill owns
project-specific alternatives, module boundaries, and migration rationale.

## Activation

Use this skill when defining or revising a project's structure and the selected
SDLC model, delivery cadence, or stage-gate artifacts affect where work and
evidence belong. Resolve project identity and current lifecycle stage first.
Do not activate it for unrelated work, to bypass approvals, or to force a
universal folder template onto a working repository.

## Required procedure

1. Establish project identity, scope, lifecycle stage, team, stack, deployment
   shape, current repository conventions, and approved change boundary.
2. Resolve the project's SDLC model from its actual delivery needs and approved
   governance. If the model or gate policy is unclear, record the uncertainty;
   do not infer a process from directory names.
3. Inventory the current tree, manifests, module/build boundaries, CI/CD,
   tests, lifecycle documents, artifact ownership, and dependency directions.
   Distinguish observed evidence from assumptions.
4. Map lifecycle phases and required artifacts to stable, discoverable locations.
   Keep product code organized by domain, feature, or deployable boundary rather
   than duplicating source trees for each lifecycle phase.
5. Compare the proposed structure with model-specific needs, existing
   conventions, ownership, traceability, and migration risk. Prefer a minimal
   additive change; retain the current layout when benefits do not justify
   disruption.
6. Document the selected model, phase/gate map, folder responsibilities,
   ownership, dependencies, exceptions, and migration/rollback plan.
7. Validate that required artifacts have a source-of-truth location, references
   resolve, and stage transitions cannot be implied by folder presence alone.
   Hand off gate readiness and model decisions to the SDLC governance skills.

## SDLC-aligned structure rules

- **Sequential or V-model delivery:** make requirements, design, implementation,
  verification, and release evidence easy to trace in that order; define
  verification artifacts alongside the corresponding requirements/design.
- **Iterative or Agile delivery:** maintain stable product/domain boundaries and
  shared lifecycle evidence; keep iteration-specific plans and outcomes under
  a repeatable iteration convention only when the team needs them.
- **Spiral or risk-driven delivery:** give risk analysis, prototypes, and
  decision evidence explicit ownership; do not confuse exploratory artifacts
  with production source.
- **DevOps or continuous delivery:** keep application source and automated
  pipeline definitions near their operational ownership; make build, deploy,
  rollback, and observability artifacts versioned and reviewable.
- **Data/AI lifecycle:** add explicit data lineage, evaluation, model/version,
  and reproducibility boundaries only where those artifacts exist and have
  owners.

The model determines phase sequence, iteration, evidence, and gates; it does
not require a separate copy of the codebase per phase. Cross-cutting controls
such as security, accessibility, privacy, and operations apply throughout the
lifecycle.

## Candidate contract

- **Purpose/problem; goal/outcome:** Forced templates and ad hoc layouts hurt
  maintainability; recommend a structure aligned to the selected SDLC model,
  technology, scale, and current conventions.
- **Behavior; activation/non-activation:** Inventory the repository and
  lifecycle evidence before recommending incremental structure; do not
  restructure solely to match a universal folder template or lifecycle diagram.
- **Inputs/tools/dependencies/handoff:** Stack, SDLC model, gates, team/workflows,
  current tree, build/test/import constraints; repository inventory and
  dependency graph; coordinate with project discovery, SDLC model generation,
  planning/traceability, lifecycle management, and gate management.
- **Procedure/decision:** Map the model's phases and evidence; map source
  boundaries separately; compare alternatives against discoverability,
  coupling, traceability, tooling, ownership, and migration risk; retain a
  working layout when no material benefit justifies change.
- **Outputs/acceptance/failure:** Structure proposal, phase-to-artifact map,
  folder ownership, dependency rules, and migration plan; pass when rationale,
  gate evidence locations, and trade-offs are explicit. Missing model or code
  ownership blocks detailed design.
- **Security/example/maintenance:** Protect private repository topology and
  sensitive lifecycle artifacts; migration requires approval. Example: an
  iterative service may keep feature-oriented source while storing shared
  requirements, architecture decisions, and release evidence in stable
  documentation areas. Revisit the map when the SDLC model or delivery shape
  changes.

## Source mapping

- Candidate ID: `71`
- Source status at discovery: `partial-architecture/discovery skills`
- Mapping evidence: `| 71 | Universal Project Structure Architect | duplicate | Traceability row 71: architecture/discovery guidance | `skills/Skill - 227 - Project Structure Manager/SKILL.md`; `universal-project-setup/SKILL.md` | Reconcile structure design with scaffolding/setup; keep recommendations non-prescriptive and migration-safe. |`
- Canonical source of truth: `registry/registry.json`

## Safety and failure handling

- Read-only discovery is the default.
- Never copy credentials, private project data, or secrets into this package.
- Do not claim functional verification from the presence of this file.
- Stop and report an explicit blocker when identity, permissions, required inputs,
  or acceptance evidence are missing.
- Make changes only after the applicable project and tool approval rules allow
  them, and preserve a rollback reference for consequential changes.

## Acceptance criteria

- Project identity, current stage, and selected SDLC model are identified from
  evidence or explicitly marked unknown.
- Each lifecycle phase/gate has discoverable, owned artifacts without
  duplicating product source across phases.
- Module boundaries and dependency directions remain compatible with the
  project's stack and deployment topology.
- The proposal preserves working conventions unless migration benefit and risk
  are documented.
- Unknowns, blocked checks, approvals, and unverified assumptions are reported;
  no stronger verification status is claimed without evidence.
