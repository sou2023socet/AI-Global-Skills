# Migration and provenance report

## Scope and evidence

The source inventory contains **443 resources**, including **143 source
`SKILL.md` files** from the two configured repositories. Every inventoried
resource has a row-level disposition in
[`SOURCE_MIGRATION_DECISIONS.csv`](./SOURCE_MIGRATION_DECISIONS.csv).

## Skill capability dispositions

| Disposition | Count |
|---|---:|
| Merged into an existing canonical capability | 102 |
| Promoted to a new canonical capability | 41 |
| Source skills inventoried | 143 |
| Active canonical skills after consolidation | 124 |

Every source skill has a SHA-256 hash, source repository/path, and
`canonicalSkillId` in [`registry/source-skills.json`](../registry/source-skills.json).
The legacy source-preserving folders remain available for auditability but are
not active canonical registry records.

## Non-skill resources

Supporting documentation, scripts, schemas, templates, and workflows remain
traceable in the source inventory. Their dispositions are `retain-as-reference`
or `defer-adaptation` where compatibility, licensing, or permission review is
still required.

No source repository was modified, and no credentials, project code, or private
runtime data was copied.

## Limitations

The inventory establishes provenance and disposition, not license ownership or
runtime effectiveness. Similarity analysis is reported separately for human
capability review.
