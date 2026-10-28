---
name: Skill - 209 - MLOps and LLM Pipeline Engineering
description: Use when building machine learning pipelines, training or fine-tuning neural models, managing model weights/checkpoints, evaluating perplexity and loss, or integrating LLM providers.
---

# Skill - 209 - MLOps and LLM Pipeline Engineering

## Purpose and Scope
Architect, train, evaluate, checkpoint, and serve custom machine learning models and integrate external Large Language Model (LLM) providers. Enforces rigorous MLOps practices, including deterministic tokenizer vocabularies, dataset formatting and validation, baseline perplexity benchmarking, rollback mechanisms, and provider-neutral model abstractions.

## Trigger Conditions
- Training, retraining, or fine-tuning local neural models (e.g. `NumpyLM`, PyTorch GPT prototypes).
- Evaluating model checkpoints against unigram baselines or empirical evaluation sets.
- Implementing or configuring LLM provider adapters (OpenAI, Google AI Studio, Anthropic, Ollama, vLLM).
- Validating prompt/response training datasets (JSONL format, token distributions, deduplication).
- Managing model checkpoint lifecycles, versioning (`.npz`, `.pt`), and automated `.prev` rollback backups.

## Non-Trigger Conditions
- Do not trigger for purely symbolic or algebraic calculus calculation without neural models (use `neuro-symbolic-math-reasoning`).
- Do not trigger for standard frontend UI form design (use `frontend-spa-engineering`).
- Do not trigger for relational database migrations (use `database-architecture-migration`).

## Prerequisites and Inputs
- Python 3.12+ runtime with numerical computing libraries (NumPy, PyTorch, FastAPI).
- Training corpus or structured JSONL prompt/response dataset.
- Configured model hyperparameters (learning rate, batch size, embedding dimension, train steps).
- External LLM API credentials when integrating external providers.

## Execution Workflow
1. **Dataset Ingestion & Validation**:
   - Inspect and validate training datasets via `dataset_validate`: check for syntax errors, empty lines, and duplicates.
   - Enforce path traversal safety: confined strictly to authorized data directories (`AI_DATA_DIR`).
2. **Tokenizer & Vocabulary Management**:
   - Build or load vocabulary mapping: map special tokens (`<pad>=0`, `<unk>=1`) and sorted unique tokens.
   - Ensure lossless bidirectional encode/decode round-trip.
3. **Training Harness & Approval Gate**:
   - Gating: Model training is a resource-intensive side-effect requiring explicit user approval.
   - Checkpoint Backup: Automatically preserve previous model weights as `*.prev.npz` before initiating training.
   - Step Cap: Enforce hard execution caps (e.g. `MAX_TRAIN_STEPS = 5000`) to prevent thread exhaustion.
   - Optimization Step: Run forward pass, loss calculation (Cross-Entropy), analytical backpropagation, and Adam weight update.
4. **Empirical Evaluation & Acceptance Gate**:
   - Evaluate held-out validation split (10%).
   - Compute validation loss and perplexity ($PPL = \exp(\mathcal{L}_{CE})$).
   - Compare against an empirical unigram baseline: accept model update only if perplexity ratio improves ($PPL_{ratio} < 1.0$). If worse, roll back to `*.prev.npz`.
5. **Provider-Neutral Model Serving**:
   - Abstract models behind a unified `LLMProvider` interface returning `ChatResult(content, provider, model, tool_calls)`.

## Commands and Examples
```powershell
# Python: Validate training dataset format and check duplicates
python -c "from app.tools.builtin import dataset_validate; print(dataset_validate('sample_dataset.jsonl'))"

# Train custom neural model checkpoint (approval-gated)
python -m app.cli --provider custom /train 500

# Evaluate model validation perplexity against unigram baseline
python -c "from app.tools.builtin import evaluate_custom_model; print(evaluate_custom_model())"
```

```python
# LLM Provider Abstract Interface Pattern
class LLMProvider:
    name: str = "base"
    def chat(self, messages: list[dict], tools: list[dict] | None = None,
             temperature: float = 0.2, max_tokens: int = 1024) -> ChatResult:
        raise NotImplementedError
```

## Deliverables and Outputs
- Serialized model weight checkpoints (`*.npz`, `*.pt`).
- Automated `.report.json` detailing train steps, final loss, validation perplexity, and duration.
- Clean provider abstraction classes in `app/providers/`.

## Quality Gates and Acceptance Criteria
- Model training preserves the prior checkpoint as `.prev` before writing new weights.
- Training loss decreases monotonically across batches during convergence.
- Provider adapters gracefully handle HTTP 429 rate limits and 5xx errors via exponential backoff.

## Security and Safety Rules
- Model training must never run autonomously without explicit, user-confirmed approval.
- Training datasets must be scanned to ensure no credentials, API keys, or PII are ingested into model weights.
