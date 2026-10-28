---
name: Skill - 213 - Performance Profiling and Scalability Engineering
description: Use when profiling application latency, diagnosing memory leaks, optimizing database connection pools, eliminating N+1 query bottlenecks, or analyzing Big-O algorithmic complexity.
---

# Skill - 213 - Performance Profiling and Scalability Engineering

## Purpose and Scope
Analyze, profile, benchmark, and optimize software system performance across compute, memory, database, and network dimensions. Eliminates algorithmic complexity bottlenecks ($O(n^2) \rightarrow O(n\log n)$), resolves memory leaks, optimizes database indexing and connection pooling, reduces API latency, and guarantees high-concurrency scalability.

## Trigger Conditions
- HTTP endpoints exhibiting high response latency (>500ms under load).
- High memory consumption, Java garbage collection pauses, or suspected memory leaks.
- Diagnosing database connection pool starvation under concurrent user load.
- Identifying and eliminating Hibernate N+1 select queries.
- Optimizing mathematical algorithms to meet formal $O(1)$ or $O(\log n)$ performance bounds.

## Non-Trigger Conditions
- Do not trigger for syntax error debugging (use `diagnostic-debugging-rootcause`).
- Do not trigger for security vulnerability scanning (use `appsec-devsecops-hardening`).
- Do not trigger for routine documentation writing (use `documentation-engineering`).

## Prerequisites and Inputs
- Reproducible benchmark or load generation scenario.
- Profiling tools (Java JProfiler/VisualVM, Python `cProfile`/`tracemalloc`, Chrome DevTools).
- Baseline performance metrics (response times, p95/p99 latency, heap memory footprint).

## Execution Workflow
1. **Empirical Baseline Measurement**:
   - Establish baseline metrics: Measure throughput (RPS), p50, p95, and p99 response times before touching code.
2. **CPU & Algorithmic Profiling**:
   - Profile CPU execution hotspots via sampling or instrumentation.
   - Analyze algorithmic complexity: Replace nested iteration loops ($O(n^2)$) with hash map lookups ($O(1)$) or balanced trees ($O(\log n)$).
3. **Memory & Garbage Collection Analysis**:
   - Inspect heap allocations and object lifecycles; identify uncollected memory retained in static maps or unbounded caches.
   - Java: Tune JVM heap flags (`-Xms`, `-Xmx`, G1GC configuration).
   - Python: Analyze object reference graphs with `tracemalloc`.
4. **Database Query & Pool Optimization**:
   - Enable Hibernate SQL logging with query execution timing.
   - Detect N+1 queries; replace iterative queries with `@EntityGraph` or `JOIN FETCH`.
   - Add database composite indexes covering frequent WHERE and ORDER BY clauses.
5. **Post-Optimization Verification**:
   - Rerun the identical benchmark scenario and verify latency and memory improvements.

## Commands and Examples
```powershell
# Python: Profile module execution time and top CPU functions
python -m cProfile -s tottime ai-service/app/custom_llm/train.py

# Trace Python memory allocations and find leaks
python -c "import tracemalloc; tracemalloc.start(); from app.custom_llm.model import NumpyLM; lm=NumpyLM(); current, peak = tracemalloc.get_traced_memory(); print(f'Peak memory: {peak / 1024 / 1024:.2f} MB')"

# Java: Profile Spring Boot memory and thread state via Actuator
Invoke-RestMethod -Uri "http://localhost:8080/actuator/metrics/jvm.memory.used"
```

## Deliverables and Outputs
- `docs/PERFORMANCE_REPORT.md`: Profiling report documenting before/after latency, memory savings, and flamegraphs.
- Optimized source code files with reduced algorithmic complexity.
- Targeted database index migration scripts.

## Quality Gates and Acceptance Criteria
- p99 response latency reduced significantly (e.g. >30% improvement).
- Algorithmic operations conform to declared Big-O bounds.
- Zero memory leaks detected during extended continuous execution.

## Security and Safety Rules
- Benchmarks must not run against live production databases.
- Diagnostic profiling endpoints (e.g. detailed Actuator thread dumps) must be restricted to administrators.
