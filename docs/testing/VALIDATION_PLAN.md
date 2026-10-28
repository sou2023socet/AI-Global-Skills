# Validation plan

## Structural checks

The structural validator checks:

- valid JSON and registry shape;
- 80 unique candidate IDs and skill IDs;
- one canonical `SKILL.md` for every registry record;
- required instruction sections;
- dependency references;
- no missing or extra candidate IDs.

Run it only with explicit approval for the exact command:

```powershell
python scripts\validate_registry.py
```

## Functional scenarios

Candidate-specific scenarios should use disposable fixture projects and record:
inputs, selected skill IDs, dependency order, permissions, outputs, failures,
and recovery checkpoints. No external service or production project should be
used as a fixture.

## Current evidence

Structural validation passed once on 2026-10-28 with command-scoped approval.
The focused unit suite passed once with 2 tests. Functional and platform
scenarios are not run. A passing structural validator must not be interpreted
as proof that a skill is effective on every host.
