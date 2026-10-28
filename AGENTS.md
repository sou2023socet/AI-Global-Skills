# Skill repository rules

These rules apply to work in this repository. Read them before creating or
modifying a skill.

## Creating a skill

1. Inspect comparable packages under `skills/` and search for overlapping
   responsibilities before creating a new skill.
2. Use the repository workflow:
   `python scripts\create_skill.py --purpose "..." --description "..." --lifecycle-group ... --provenance-repository ... --provenance-path ...`
3. Never choose a permanent sequence number manually. The workflow derives the
   next number from the actual filesystem and registry and refuses collisions.
4. The directory must be named `Skill - NNN - Skill Purpose`, with a
   three-digit sequence, meaningful title capitalization, and no reserved
   filesystem characters.
5. `SKILL.md` must have `name` and `description` frontmatter. `name`, the
   primary H1, and the complete directory name must match exactly.
6. Preserve the established sections and domain knowledge: Purpose,
   Activation, Required procedure, scope, inputs, outputs, failure handling,
   acceptance criteria, and examples where applicable.
7. Every new skill must be registered in `registry/registry.json`. Update
   generated indexes and status matrices with the repository workflow; do not
   invent provenance or omit required registry fields.
8. Preserve existing skill directories and numbering. Do not create
   `legacy-`, `temp-`, or `old-` directories and do not create an unjustified
   duplicate.

## Validation and reporting

- Run only permitted structural validation; do not use this repository rule as
  authorization to run tests, builds, integrations, or archives.
- Validate the final filesystem, metadata, registry paths, and generated
  references before claiming success.
- If validation fails, report the exact error and do not claim the skill is
  complete.
- Keep source-history and provenance records distinct from active canonical
  packages.
