# Skill creation and registration

Use this process for every new active skill. It preserves existing skill
directories and assigns the next available sequence from the current
filesystem.

## Prerequisites

- Read the repository [AGENTS.md](../../AGENTS.md).
- Inspect comparable skills and search for overlapping responsibilities.
- Have a concise purpose, accurate description, lifecycle group, and real
  provenance repository/path. Do not invent source provenance.
- Confirm that the proposed skill is distinct rather than a duplicate.

## Create a skill

From the repository root, run:

```powershell
python scripts\create_skill.py `
  --purpose "Example Skill Purpose" `
  --description "Explain what the skill does and when to use it." `
  --lifecycle-group development `
  --provenance-repository example-repository `
  --provenance-path "path\to\source\SKILL.md"
```

The workflow:

1. Reads every existing skill directory and `registry/registry.json`.
2. Allocates the next free three-digit number without renumbering existing
   skills.
3. Rejects invalid titles, reserved filesystem characters, duplicate IDs, and
   duplicate purposes.
4. Creates the package from
   [`templates/skill-authoring/SKILL.md`](../../templates/skill-authoring/SKILL.md)
   using a staging directory.
5. Registers the skill and its declared provenance.
6. Regenerates the canonical index, dependency map, overlap report, and status
   matrix.
7. Runs structural registry validation and rolls back the new package and
   registry files if any step fails.

The workflow does not run tests, builds, integrations, or packaging commands.

## Required result

The final package must have:

- `skills/Skill - NNN - Skill Purpose/SKILL.md`
- matching `name` frontmatter and H1
- non-empty `description`
- Purpose, Activation, and Required procedure sections
- complete registry metadata and a resolving `path`
- declared provenance that can be audited

## Recovery and common mistakes

- If the purpose overlaps an existing skill, extend the existing skill or
  provide a genuinely distinct purpose before retrying.
- If provenance is unavailable, stop and obtain the real source reference; do
  not use a placeholder hash or fake repository.
- If validation fails, inspect the reported path and metadata error. The
  workflow is designed to remove its staged package and restore registry
  snapshots on failure.
- Never manually renumber existing directories to resolve a collision.
