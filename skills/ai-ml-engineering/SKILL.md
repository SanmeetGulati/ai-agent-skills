---
name: ai-ml-engineering
description: Design and evaluate machine learning experiments, research model methods, train or fine-tune models, and plan or implement model deployment and monitoring. Use for ML research, model evaluation, training, and MLOps; not for data preparation.
---

# AI and ML engineering

Apply the relevant practices below to the requested work, scaled to its scope. Inspect the project's existing experiments, code, configurations, metrics, model artifacts, and constraints before making recommendations. Use relevant project-specific research guidance when available. Do not perform data preparation unless the user separately requests it.

## Research and experiments

- Define the question, hypothesis, success criteria, baseline, intervention, evaluation protocol, and compute constraints. Compare against a matched baseline and change as few factors as practical. Identify data splits and prior use to flag leakage or repeated test-set selection; do not claim independence where it is unverified.
- For new AI methods or issues, consult current official documentation, relevant GitHub issues, and primary research where available. Check versions, implementation compatibility, and experimental conditions. Separate established findings from hypotheses, and explain when reported gains may not transfer. Disclose unavailable evidence.
- Before reproducing a paper, identify the method, evaluation conditions, available implementation, and material differences from the project's environment. Test feasibility before committing to expensive runs.

## Training and evaluation

- For training or fine-tuning, inspect the current model, checkpoint, configuration, hardware, and training path. Record relevant model and library versions, configuration, data and split identities, random seeds, checkpoints, and evaluation commands when available; state missing provenance. Diagnose failures using evidence, and avoid launching costly jobs without authorization appropriate to the task.
- Choose task-appropriate primary metrics and guardrails. Examine representative successes and failure cases, relevant slices, and uncertainty or sample limitations. Compare quality, latency, and cost when they matter; distinguish measured results from estimates. For LLM or retrieval systems, evaluate representative retrieval and generation failures where relevant.

## Deployment and operations

When deployment is in scope, assess serving compatibility, model and artifact versioning, resource requirements, latency, observability, and failure handling. Specify relevant monitoring, acceptance criteria, and rollback or recovery plans. For agent or LLM workflows, consider tool boundaries, model output validation, and prompt-injection exposure when applicable. Do not deploy or promote a model without the authorization required by the task and environment.

## Communicate and verify

Explain consequential design choices and tradeoffs in plain language. Run checks appropriate to the work and report the baseline, evidence, results, reproducibility details, limitations, and a concrete next step when useful. Keep implementation readable and consistent with the project.
