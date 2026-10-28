# Source candidate specification

- **Purpose/problem; goal/outcome:** Typical examples miss boundary/combination defects; generate bounded, reproducible edge and property-based cases.
- **Behavior; activation/non-activation:** Identify invariants, boundary partitions, random seed and shrinking; not unbounded fuzzing or unauthorized target probing.
- **Inputs/tools/dependencies/handoff:** Contract/invariants, input bounds, safe harness; native property/fuzz test library if already present; depends 20/33–35; findings to 29/40.
- **Procedure/decision:** 1) Derive boundary classes and invariants. 2) Set sample/time/size caps and fixed seed. 3) Run, shrink failures, retain reproducer. 4) If complexity or side effects exceed limits, stop and refine harness.
- **Outputs/acceptance/failure:** Edge matrix, property tests, seeds/reproducers; pass when bounds are enforced and failures replay deterministically. No seed/output means report limitation.
- **Security/example/maintenance:** Avoid resource-exhaustion payloads outside sandbox/approval. Example: randomly generated valid fractions preserve normalization and zero-denominator rejection. **Status:** proposed new skill; generic QA mentions boundaries only. Monitor flaky/expensive cases.
