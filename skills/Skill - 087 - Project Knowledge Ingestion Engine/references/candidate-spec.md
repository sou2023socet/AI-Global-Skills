# Source candidate specification

- **Purpose/problem; goal/outcome:** Relevant files/docs are scattered and unindexed; ingest authorized sources into searchable, source-linked knowledge with freshness.
- **Behavior; activation/non-activation:** Select, parse, redact and index allowed sources; not scrape arbitrary systems or train models on project data.
- **Inputs/tools/dependencies/handoff:** Project/source allowlist, permissions, formats, retention; file/API parsers and index; depends 02/03/57/72; hands context to 04/60/74–77.
- **Procedure/decision:** 1) Validate source authorization and sensitivity. 2) Extract text/metadata and provenance. 3) Redact/exclude restricted content and index. 4) If format/parser loses context or permission unclear, skip and report.
- **Outputs/acceptance/failure:** Source index with hash/path/date/access class; pass when retrieval returns citations and stale updates are detectable. Parser error is not silent omission.
- **Security/example/maintenance:** No credential ingestion; access control and deletion propagation required. Example: index Markdown and source paths, excluding `.env` and build outputs. **Status:** proposed new capability; project audit performs manual discovery. Review source allowlist and refresh.
