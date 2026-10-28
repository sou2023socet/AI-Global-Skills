# Source candidate specification

- **Purpose/problem; goal/outcome:** Latency/resource issues lack reproducible measurement; locate bottlenecks and assess agreed targets.
- **Behavior; activation/non-activation:** Establish workload/baseline and profile; not a substitute for functional debugging or production load test approval.
- **Inputs/tools/dependencies/handoff:** SLO/target, workload, environment, baseline; profiler/metrics and safe load harness; depends 23/25/31/33/34; findings to 40/42/47.
- **Procedure/decision:** 1) Record environment and measurement noise. 2) Reproduce representative workload. 3) Profile bottleneck and compare target. 4) If no target/baseline exists, report measured facts and ask before optimizing to arbitrary threshold.
- **Outputs/acceptance/failure:** Reproducible report with workload, p50/p95/p99, resources and limits; pass against agreed threshold. Invalid/unstable measurements are inconclusive.
- **Security/example/maintenance:** No production load absent explicit approval; protect profiling data. Example: N+1 query measured locally and before/after counts attached. **Status:** partial—profiling skill, no actual benchmark evidence. Re-run after optimization.
