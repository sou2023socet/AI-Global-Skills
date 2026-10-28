# Proposed Directory Map

**Status: proposal.** This map distinguishes the current foundation files from future directories; directory names do not imply implemented components.

```text
Project-Universal-Global-AI-Skills/
├── README.md
├── configs/
│   ├── defaults.yaml                 # Non-secret global policy defaults; proposed
│   └── platforms/                    # Host discovery/compatibility settings; proposed
├── catalogue/
│   ├── registry.json                 # Canonical records; intentionally not populated yet
│   ├── candidates-01-80.yaml         # Candidate IDs and disposition/status
│   ├── generated/                    # Search indexes and reports; generated, not hand-edited
│   └── provenance/                   # Source references and review records
├── schemas/
│   ├── skill-registry.schema.json    # Created in this proposal
│   ├── project-workspace.schema.json # Future project registry contract
│   ├── evidence.schema.json          # Future evidence contract
│   └── workflow.schema.json          # Future workflow contract
├── skills/
│   └── <stable-skill-id>/
│       ├── SKILL.md
│       ├── references/
│       └── templates/
├── workflows/
│   ├── lifecycle/                    # Discovery -> release -> maintenance workflows
│   ├── recovery/                     # Checkpointed failure/recovery procedures
│   └── validation/                   # Reusable validation plans, not validator code
├── shared/
│   ├── contracts/                    # Evidence, approval, status, and handoff contracts
│   ├── rules/                        # Global rules and precedence
│   ├── templates/                    # Cross-skill reusable artifact templates
│   └── references/                   # Shared technical reference material
├── orchestration/
│   ├── routing/                      # Intent/trigger routing and minimal skill selection
│   ├── dependencies/                 # Skill/workflow dependency maps
│   ├── policies/                    # Conflict, permission, retry, and ownership rules
│   └── adapters/                     # Platform-specific skill discovery/tool mappings
├── integrations/
│   ├── mcp/                          # MCP capability and permission declarations
│   ├── agent-platforms/              # Host-specific adapters and compatibility notes
│   └── automation/                   # Optional CI/event/scheduler adapters
├── projects/
│   └── <project-id>/
│       ├── project.yaml              # Non-secret canonical identity and access scope
│       ├── context/                  # Freshness-tagged project facts/instructions
│       ├── evidence/                 # Redacted evidence, findings, approvals
│       ├── decisions/
│       ├── status/
│       ├── outputs/
│       └── config/                   # Project-specific allowed policies/tools
├── validation/
│   ├── validators/                   # Static validators; proposed
│   ├── fixtures/                     # Valid/invalid metadata and workflow fixtures
│   ├── reports/                      # Versioned validation summaries
│   └── scenarios/                    # Safe behavior scenarios
├── tests/
│   ├── contract/
│   ├── registry/
│   ├── orchestration/
│   └── workflows/
├── docs/
│   ├── architecture/                 # This proposal and lifecycle map
│   ├── roadmap/
│   ├── governance/
│   ├── operations/
│   └── migration/
├── releases/
│   ├── CHANGELOG.md
│   └── compatibility-matrix.md
├── migrations/
│   └── <change-id>/                  # Source->target, hashes, approvals, validation, rollback
└── templates/
    ├── project-workspace/
    └── skill-authoring/
```

## Directory responsibilities

- **`catalogue/`** is the registry/catalogue source of truth. Generated indexes and dashboards/reports must be reproducible from it. Project evidence is not stored here.
- **`skills/`** contains reviewed, canonical, globally reusable skill packages. A folder is not accepted as a registered skill until it has a registry record and required validation status.
- **`workflows/`** composes skills into lifecycle procedures; workflows declare dependencies, approvals, outputs, failure branches, and recovery checkpoints.
- **`shared/`** owns reusable contracts, policies, templates, and references consumed across multiple skills.
- **`orchestration/`** owns selection/order/conflict/permission logic and platform adapters; adapters may translate discovery formats but cannot weaken policy.
- **`integrations/`** is opt-in. Tool capabilities, scopes, data handling, side effects, and fallbacks are documented before configuration.
- **`projects/<project-id>/`** isolates project-specific context and evidence. Prefer references to external repositories over copying project code.
- **`validation/` and `tests/`** separate static structural checks from behavior/scenario evidence. Reports identify exact version, scope, and environment.
- **`releases/` and `migrations/`** maintain compatibility, provenance, approval, change history, and rollback.

## Registration and execution path

1. Author proposes a stable-ID skill directory using `templates/skill-authoring/` and supplies source provenance.
2. Add a registry record conforming to `schemas/skill-registry.schema.json`; candidate links and dependencies must resolve.
3. Run static validation and review triggers, overlap, permissions, inputs/outputs, and failure handling.
4. Execute approved scenario tests in isolated fixtures; record results as evidence. Platform discovery is verified separately.
5. Publish the catalogue entry only with its actual lifecycle status and validation evidence.
6. At task time, resolve project context, select minimum matching skills, order dependencies, resolve conflicts, check permissions, and record a handoff.
7. Version the skill and contract under semantic compatibility rules; maintain migration/deprecation records for consumers.

## Actual files versus proposed paths

Created now: the README, architecture, directory map, lifecycle map, registry schema, roadmap, and migration strategy. Other paths shown above are proposed only; no runtime directories, scripts, catalogue registry entries, project workspaces, tests, integrations, or skill packages are claimed as implemented.
