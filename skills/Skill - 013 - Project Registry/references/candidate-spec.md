# Source candidate specification

- **Purpose/problem; goal/outcome:** Similar project names and stale paths can direct work to the wrong repository; maintain canonical identities, locations, ownership, technology, status, and knowledge links.
- **Behavior; activation/non-activation:** Resolve a project before multi-repository work; do not copy source code or infer identity from a folder name alone.
- **Inputs/tools/dependencies/handoff:** User/project identifier, approved repository paths, ownership and freshness; filesystem/Git inspection and a registry schema; depends 01/02; feeds 04, 72, and 80.
- **Procedure/decision:** 1) Match supplied identity to canonical remote/path. 2) Check repository metadata and last-verified date. 3) Record aliases separately. 4) If multiple candidates match or access is denied, ask/stop rather than selecting silently.
- **Outputs/acceptance/failure:** Machine-readable project record and human index; pass when each entry has unique ID, canonical path, status source, and freshness. Registry write failures leave existing entries intact.
- **Security/example/evidence/maintenance:** Store no secrets or private source; access to private projects must be authorized. Example: “NexusMath” matches two worktrees; report both until owner selects canonical. **Status:** proposed—no registry file found. Revalidate path/ownership on change; propose, do not impose, storage.
