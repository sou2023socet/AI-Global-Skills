---
name: Skill - 265 - Universal Project Setup and Run
description: Inspect, configure, verify, build, and when explicitly requested run software projects. Use for project setup, dependency or environment troubleshooting, build verification, and run requests across any technology stack.
---

# Skill - 265 - Universal Project Setup and Run

Prepare the current project safely, verify every claim, and reuse verified procedures. Inspect actual project files rather than inferring the stack from the folder name or README alone.

## Command intent

- **Setup project:** inspect, configure, install project dependencies, and build/verify. Never launch the application.
- **Run application:** verify setup, services, and ports; build if needed; start and verify one application instance.
- **Setup and run:** complete setup first, then run and verify.
- If the request is ambiguous, follow the closest intent above; do not start an app during setup-only work.

## Workflow

1. **Inspect before changing anything.** Identify the project name, OS/platform needs, languages, frameworks, runtime/SDK, build system, package manager, lockfiles, databases/services, APIs, environment variables, configuration, ports, and build/run/package commands. Read relevant manifests, scripts, configuration, and project documentation.
2. **Find existing skills.** Check applicable project skills, then personal skills. Prefer relevant verified project-specific guidance, followed by environment-specific and general guidance. Confirm that versions, paths, and assumptions still match; update rather than duplicate a skill.
3. **Audit only relevant tools.** Check required tool versions and configuration, then compare them with the project's declared requirements and compatibility constraints. Classify tools as compatible, outdated but compatible, misconfigured, incompatible, or missing. Do not upgrade working dependencies blindly.
4. **Plan the smallest safe changes.** Use the project's existing package manager and respect lockfiles. Prefer official sources for missing tools. Do not invent credentials, secrets, or environment-specific values. Never overwrite unrelated settings or kill unrelated processes.
5. **Execute changes sequentially per project/environment.** Allow parallel read-only inspection and research, but maintain one active project-changing operation at a time: no concurrent installs, configuration edits, cleans, migrations, builds, or app/service starts for the same project/environment. Check whether an operation is already running or has already succeeded before starting it. Wait for completion, inspect its result, and verify before the next operation.
6. **Build and diagnose.** Use the project's actual build/test command when appropriate. On failure, inspect the relevant error, identify the cause, make a targeted fix, then run only the necessary next command. Never repeat an unchanged failed command or report success without a successful result.
7. **Run only when requested.** Check required services and ports first. Reuse the correct running instance; do not start duplicates or terminate unrelated processes. Do not run against an incomplete or failed build unless the project's documented development workflow allows it. Verify startup with an appropriate health check, response, or process/log evidence.
8. **Save reusable learning.** After a verified setup or meaningful fix, update an existing relevant skill or create a concise new one only when the procedure is reusable. Keep project-specific facts in a project skill where possible; do not pollute this universal skill with one-project assumptions. Never mark an untested procedure verified.

## Inspection and compatibility guide

Look for the files that apply to the detected stack, for example:

- `README*`, `.env.example`, Docker/Compose files, and service configuration
- Node manifests and lockfiles; Python dependency/project files
- Maven/Gradle files and wrappers; Go modules; Cargo manifests
- `.sln`/`.csproj`, CMake files, platform SDK manifests
- Framework/build configuration, scripts, and CI workflows

Check only relevant categories: language runtime, compiler/SDK, package manager/build tool, framework, database or external service, required CLI tools, and platform-specific tooling. Verify compatibility across the actual declared versions (for example runtime ↔ framework ↔ build tool), not just whether a command exists. Prefer project wrappers and pinned versions when provided.

If a required tool is missing and installation is permitted, determine the required version and platform, use the official source, configure only necessary environment variables, and verify the installed version. If download/install is unavailable, state exactly what is missing, the required version, and the official manual action. Continue other work that can be completed safely.

For unavailable required credentials or external services, identify the blocker, configure and verify everything else possible, and request only the missing user-specific information. Never print secrets in reports.

## Skill quality and format

Before adding a skill, search for an existing one that covers the procedure. Keep each skill concise and include, as relevant:

- purpose and when to use
- detection method and required inputs/tools
- compatibility requirements
- setup and verification steps
- verified build/run commands
- common failures and tested fixes
- known project/environment details and last verification status

Use exactly one status for procedures: `VERIFIED`, `PARTIALLY VERIFIED`, or `UNVERIFIED`. Discovery does not guarantee automatic invocation; apply the skill when relevant and re-check changeable environment assumptions.

## Reports

For setup, report the project and detected stack; what was configured; any attention items or missing requirements; build result; and:

> Application: NOT STARTED

For a run request, report setup/dependency/service/build status, whether the application is actually running, the verified URL if available, and the command used. If blocked, report `NOT RUNNING`, the root cause, what was fixed, and the specific remaining action. Keep logs summarized and distinguish verified facts from unverified assumptions.

## Safety invariants

- Correctness and safety take priority over speed or token savings.
- Setup prepares the project; it does not start the application.
- Never claim a tool, dependency, build, service, or application is ready without checking it.
- Parallelize analysis; serialize changes and execution for a given project/environment.
- Do not repeat work unless a relevant condition changed or verification requires it.
- Preserve user files and existing working configuration; use the smallest safe fix.
