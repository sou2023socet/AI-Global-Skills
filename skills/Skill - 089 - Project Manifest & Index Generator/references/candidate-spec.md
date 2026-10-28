# Source candidate specification

- **Purpose/problem; goal/outcome:** Project metadata and artifacts are hard to discover; generate consistent machine/human indexes with provenance.
- **Behavior; activation/non-activation:** Collect approved facts and update index; do not overwrite manually owned or stale fields without conflict policy.
- **Inputs/tools/dependencies/handoff:** Registry identity, repository manifests, artifact map, schema/owner; filesystem/Git and YAML/Markdown; depends 03/04/06/71; feeds 05/61/73–77/80.
- **Procedure/decision:** 1) Validate project identity/schema. 2) Extract only allowed facts and source references. 3) Compare generated vs existing fields. 4) Preserve manual fields or flag conflict until owner resolves.
- **Outputs/acceptance/failure:** Manifest and index with generated-at/source metadata; pass when schema validates and paths resolve. Missing field remains unknown.
- **Security/example/maintenance:** Exclude secrets/private user data. Example: index module directories and actual package versions with scan timestamp. **Status:** proposed shared template/service; no manifest found. Regenerate only by approved cadence.
