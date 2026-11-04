# FORTE-MM Leaderboard

Results of 9 models on the full **256-task** FORTE-MM benchmark. All numbers are macro-averaged across the 256 tasks.

## Evaluation protocol

- **Agent runtime**: each model runs as an OpenClaw agent inside the benchmark's Docker image, once per task, with the task's input tree as its workspace.
- **Runs**: every task is executed 3 times per model.
- **Scoring**: an LLM judge checks the agent's workspace artifacts against the task's expert-annotated rubrics. Scoring is **all-or-nothing** per run: a run scores 1 only if *every* rubric item passes, otherwise 0.
- **Metrics** (computed per task, then macro-averaged across tasks):
  - `Avg@3` — mean score across the 3 runs.
  - `Pass@3` — 1 if at least one of the 3 runs scores 1, else 0.
  - `Pass^3` — 1 only if all 3 runs score 1 (a consistency measure).

Reasoning-effort / thinking settings: all models were evaluated with their default reasoning settings and the benchmark's default agent configuration; none were tuned per-task.

## Results

| Rank | Model | Avg@3 | Pass@3 | Pass^3 |
|---|---|---|---|---|
| 1 | gemini-3.8-flash | **74.5** | **85.9** | 61.7 |
| 2 | gpt-5.6-sol | 73.2 | 82.4 | **62.9** |
| 3 | claude-5-opus | 73.1 | 81.2 | 62.0 |
| 4 | deepseek-4.1-flash | 72.8 | 83.2 | 60.9 |
| 5 | kimi-k3 | 70.7 | 80.1 | 60.2 |
| 6 | claude-4.8-opus | 69.9 | 80.5 | 57.8 |
| 7 | gemini-3.6-flash | 67.6 | 80.1 | 54.7 |
| 8 | gpt-5.5 | 63.5 | 75.4 | 51.2 |
| 9 | kimi-k2.6 | 53.6 | 69.1 | 36.3 |

## Observations

- **Headline scores are low.** The best model solves only ~75% of tasks on average, and no model passes all 3 runs on more than ~63% of tasks — multimodal office work remains far from solved.
- **Consistency lags peak ability.** `Pass@3` is 10–20 points above `Pass^3` for most models: agents that can solve a task once often fail to reproduce it, so reliability is the bigger gap.
- **Multimodal perception is a bottleneck.** Failure analysis of trajectories shows frequent errors in reading values off screenshots and scans, matching figures across images and text, and chart understanding — precisely the skills FORTE-MM is built to measure.

To reproduce these numbers, follow the [Quickstart](../README.md#quickstart) in the main README: configure the gateway, fetch the task bundles, build the agent image, and run `bash scripts/run.sh` or `scripts/benchmark.py` with the model of your choice, then aggregate with `scripts/aggregate.py`.