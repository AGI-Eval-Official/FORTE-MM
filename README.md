# FORTE-MM: Multimodal Full-Cycle Office Real-World Task Evaluation

FORTE-MM (**FORTE**'s **M**ulti**M**odal counterpart) is an agent benchmark that measures how well AI agents handle **multimodal office work across 14 corporate professions**. Every task is a self-contained folder — the agent's instruction plus a multimodal working environment: images, screenshots, scans, office documents (xlsx / docx / pptx / pdf / csv), data files, and, where the task demands it, **mock systems** (monitoring dashboards, bundled web apps, queryable data interfaces) that the agent must operate. Outputs are scored by an **LLM judge** that inspects the agent's workspace artifacts against a set of expert-annotated rubrics.

Where text-only office benchmarks ask the agent to *read and write files*, FORTE-MM focuses on the multimodal skills real office work actually requires: reading data off screenshots, understanding charts and scanned forms, matching figures across images and text, counting objects in photos, and producing documents that cite what was seen. A README_zh.md is also available.

**Dataset**: the full benchmark contains **256 tasks**, spanning 14 professions: data/business analysis, algorithm engineering, development, QA, SRE, finance, legal, administration, operations, marketing, HR, sales, product management, and UI/UX design. Every task is annotated with its profession, task type, and a two-level task category. This repository ships the complete runner infrastructure and **one demo task per profession** (14 tasks, bundled with their input files and rubrics). The remaining task bundles will be released publicly when the benchmark is officially published.

**Leaderboard**: see docs/leaderboard.md (also inline below) for results of 9 models on the full 256-task benchmark.

For the mock systems used by the interactive tasks (monitoring dashboards, web app targets, data interfaces), see docs/mock-systems.md.

## Overview

| Dimension          | FORTE-MM |
|---|---|
| Task expression    | One folder per task: `task.yaml` metadata + `instruction.md` + `input/` + `solution/` |
| Modalities         | Images / screenshots / scans + xlsx + docx + pptx + pdf + csv + code + mock systems |
| Professions        | 14 corporate professions |
| Multimodal abilities | OCR, chart understanding, multi-image reasoning, image-text alignment, counting, arithmetic, domain knowledge, ... |
| Grading            | LLM-as-judge, all-or-nothing scoring (i.e. `score = 1` iff every rubric item passes) |
| Metrics            | Avg@3, Pass@3, Pass^3 |
| Agent runtime      | OpenClaw inside a single Docker image |
| Requirements       | Python 3.10+ stdlib + `docker` CLI |

## Leaderboard

Results on the full 256-task benchmark (3 runs per task, all-or-nothing scoring, macro-averaged across tasks; graded by the LLM judge; all models run with their default reasoning settings). Details and protocol notes: docs/leaderboard.md.

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

## Quickstart

Requirements:

- Docker
- Python 3.10+ (stdlib only)

1. Configure the gateway used by both the agent and judge:

```bash
cp openclaw_config/openclaw.json.example openclaw_config/openclaw.json
cp openclaw_config/.env.example          openclaw_config/.env
# Edit both files with your gateway URL and API key (secrets stay local).
```

2. (Optional but recommended) Install general-purpose office skills (`docx` / `pptx` / `xlsx` / `pdf`), which the runner stages into every agent container's skills dir:

```bash
bash scripts/install-anthropic-skills.sh   # SKILLS="docx xlsx" to pick a subset
```

3. Build the agent image (start Docker first — Docker Desktop on macOS/Windows, `systemctl start docker` on Linux):

```bash
bash docker/fetch-lo.sh
docker build -f docker/Dockerfile.agent -t mwork-agent:latest docker/
```

4. Run — the 14 demo tasks are already in the repo:

```bash
bash scripts/run.sh   # all tasks, default model from openclaw.json

# Or with explicit options:
python scripts/benchmark.py --model your-gateway/your-model --dataset ./tasks --runs 3 --concurrency 1

# Variants: TASK_ID=mm-ba-003, MODEL=..., RUNS=3 CONCURRENCY=2 bash scripts/run.sh
```

Each completed run lands the following files under `<output-dir>/<model_slug>/<task_id>[_run_N]/`:

| File                   | Notes                                                                 |
|---|---|
| `grading.json`         | score (0/1), per-rubric breakdown, anomalies                          |
| `openclaw_trace.json`  | raw agent event stream                                                |
| `openai_messages.json` | flattened OpenAI chat-completions view of the trace                   |
| `judge_prompt.json`    | exact judge inputs (system prompt + user prompt + image/pdf manifest) |
| `workspace/`           | snapshot of the agent's working directory after it finished           |

## Metrics

Each task is run 3 times. Per-run grading uses **all-or-nothing scoring**: a run scores 1 only if every rubric in `## Grading Criteria` passes; otherwise 0. The leaderboard reports three metrics, all computed per task and then macro averaged across tasks:

| Metric    | Meaning                                                       |
|---|---|
| `Avg@3`   | Mean score across the 3 runs.                                 |
| `Pass@3`  | 1 if at least one of the 3 runs scores 1, else 0.             |
| `Pass^3`  | 1 only if all 3 runs score 1, else 0 — a consistency measure. |

To aggregate results across all models in `./results/`:

```bash
python scripts/aggregate.py          # all models, all tasks, k=3
python scripts/aggregate.py --per-task   # per-(model, task) breakdown
python scripts/aggregate.py --json       # machine-readable output
```

## Acknowledgement

This repo is built on top of [FORTE](https://github.com/AGI-Eval-Official/FORTE) (Full-Cycle Office Real-World Task Evaluation), from which the runner architecture, the LLM-judge grading pipeline, and the evaluation methodology are derived. FORTE-MM (Multimodal Full-Cycle Office Real-World Task Evaluation) is its multimodal counterpart. The agent runtime is [OpenClaw](https://docs.openclaw.ai/). We thank the OpenClaw team for the excellent agent harness.

## Citation

If you find this repo helpful or relevant to your research, please kindly cite:

```bibtex
@misc{FORTE,
  title       = {{FORTE-MM}: Multimodal Full-Cycle Office Real-World Task Evaluation},
  author      = {{LongCat Team}},
  year        = {2026},
  month       = nov,
  url         = {https://github.com/AGI-Eval-Official/FORTE-MM},
  urldate     = {2026-11-02}
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

Maintainer: Shengyu Guo — `shengyu.guo@meituan.com`.

Contributors: Jiaxing Liu、Zeyang Hu、Shengyu Guo、Chen Chen、Fengjiao Chen、Yifan Yang、Xuezhi Cao、Ziwen Wang.