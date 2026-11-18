# Agent architecture design and review

Establish the job to be done, success criteria, users, data and action permissions, existing stack, constraints, and expected workload. Trace inputs through components to outputs and side effects. For a review, inspect the actual implementation and distinguish observed problems from potential risks.

Compare a deterministic workflow and a single agent before proposing multiple agents. Introduce delegation only when the task benefits from separate responsibilities or parallel work, and account for coordination cost, ownership, handoffs, shared state, and termination.

For the proposed design, specify the decisions that matter for implementation: component responsibilities, interfaces and data flow; model and tool boundaries; state, memory, context and persistence; authorization and trust boundaries; failure handling, retries, timeouts and stopping conditions; observability, latency and cost. Address human review or recovery where the action and risk justify it.

Define an evaluation using representative tasks and measurable acceptance criteria, including tool failures and unsafe or ambiguous inputs where relevant. Compare against an appropriate baseline. Do not present untested designs or maturity scores as measured performance. Include a compact flow diagram when it clarifies the design and a prioritized implementation or improvement sequence when useful.
