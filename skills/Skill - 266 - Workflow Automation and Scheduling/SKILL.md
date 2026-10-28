---
name: Skill - 266 - Workflow Automation and Scheduling
description: Use when designing background worker queues, scheduling recurring cron automation, implementing asynchronous task decoupling, or preventing HTTP thread exhaustion.
---

# Skill - 266 - Workflow Automation and Scheduling

## Purpose and Scope
Design, implement, configure, and monitor automated workflow execution, scheduled cron jobs, asynchronous task queues, and background worker threads. Decouples heavy compute workloads (model training, matrix factorizations, batch evaluations, reporting) from synchronous web request threads, preventing HTTP gateway timeouts (504) and thread exhaustion.

## Trigger Conditions
- Decoupling synchronous long-running operations (e.g. `train_tiny_lm`) into background tasks.
- Designing recurring cron jobs or automated maintenance tasks.
- Implementing asynchronous task status polling endpoints (`GET /tasks/{id}/status`).
- Orchestrating multi-step workflow pipelines where downstream tasks depend on upstream artifacts.

## Non-Trigger Conditions
- Do not trigger for synchronous, low-latency (<50ms) in-memory data lookups.
- Do not trigger for live real-time bidirectional audio/video streaming.
- Do not trigger for manual, one-off terminal executions.

## Prerequisites and Inputs
- Target workflow task definition and input arguments.
- Asynchronous task framework (Spring `@Async` / `ThreadPoolTaskExecutor`, Python `asyncio` / Celery / Redis queue).
- Task status persistence store (PostgreSQL `task_runs` table or in-memory thread registry).

## Execution Workflow
1. **Workload Profiling & Decoupling**:
   - Identify operations exceeding 500ms execution times under load.
   - Separate the synchronous HTTP request from asynchronous computation:
     - Client calls `POST /tasks/execute` $\rightarrow$ Server assigns UUID, launches background worker, and returns `202 ACCEPTED` with `{"taskId": "..."}` immediately.
2. **Thread Pool & Concurrency Management**:
   - Configure bounded thread pools (`corePoolSize: 4`, `maxPoolSize: 8`, `queueCapacity: 50`) to prevent out-of-memory crashes under burst traffic.
3. **Status Polling & Event Streaming**:
   - Provide status endpoint (`GET /tasks/{id}`) returning `PENDING`, `RUNNING`, `SUCCESS`, or `FAILED` with percentage progress.
   - Stream real-time progress events to client via Server-Sent Events (SSE).
4. **Retry & Failure Recovery**:
   - Implement exponential backoff retry for transient network operations.
   - Enforce task execution deadlines (timeouts) to kill hanging threads cleanly.
5. **Audit & Execution Logging**:
   - Persist execution records: start time, finish time, exit status, and error traces.

## Commands and Examples
```java
// Spring Boot Asynchronous Task Pattern
@Service
public class ModelTrainingWorker {
    @Async("taskExecutor")
    public CompletableFuture<TrainingResult> executeTrainingAsync(String taskId, int steps) {
        updateTaskStatus(taskId, "RUNNING");
        try {
            TrainingResult result = runTraining(steps);
            updateTaskStatus(taskId, "SUCCESS", result);
            return CompletableFuture.completedFuture(result);
        } catch (Exception ex) {
            updateTaskStatus(taskId, "FAILED", ex.getMessage());
            return CompletableFuture.failedFuture(ex);
        }
    }
}
```

```powershell
# Query task progress via PowerShell REST invoke
Invoke-RestMethod -Uri "http://localhost:8080/api/tasks/task-123/status" -Headers @{Authorization="Bearer $TOKEN"}
```

## Deliverables and Outputs
- Asynchronous service worker implementations and thread pool configuration beans.
- REST endpoints for task submission (`202 ACCEPTED`) and status polling.
- Persistent task execution audit records in database.

## Quality Gates and Acceptance Criteria
- Synchronous HTTP endpoints return within 200ms without blocking on background compute.
- Thread pools strictly bound maximum concurrent execution and prevent thread starvation.
- Unhandled task worker exceptions are cleanly caught and reflected as `FAILED` status without crashing the server process.

## Security and Safety Rules
- Enforce strict caller ownership on task status endpoints to prevent unauthorized inspection of other users' background jobs.
- Heavy background compute tasks must be bounded by memory and time limits.
