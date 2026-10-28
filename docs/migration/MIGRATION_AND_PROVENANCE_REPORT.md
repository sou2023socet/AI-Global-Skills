# Migration and provenance report

## Scope

The source roots were inspected without modifying them:

- `E:\sumit@data\project\Git\global-skills`
- `E:\sumit@data\project\Git\enterprise-ai-engineering-skills`

The discovery baseline contains 443 curated resources and 143 `SKILL.md`
files. The complete row-level source inventory is preserved at
[`SOURCE_INVENTORY.csv`](./SOURCE_INVENTORY.csv).

## Disposition

All 80 approved candidates have a target-owned instruction package generated
from the authoritative candidate catalogue and a source-mapping record. These
packages are adaptations of candidate specifications, not claims that the
source implementations are functionally equivalent. Existing source skill
trees remain in place and are not overwritten or deleted.

The source catalogue and mapping hashes are recorded in each registry record.
No secrets, project code, or private runtime evidence was copied. The inventory
and mapping use reference-only provenance where capability-level migration has
not been independently verified.

## Status semantics

`implemented` means a canonical instruction package and registry record exist.
It does not mean functional or platform verification. Structural status is
updated only by the validator; functional status remains `not-run` until a
candidate-specific scenario has been executed and recorded.

## Limitations

Semantic overlap among the 143 source skills still requires owner review before
deprecating or merging source capabilities. External service integrations and
host-specific invocation behavior are not verified by this repository.
