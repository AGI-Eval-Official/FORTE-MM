# Mock Systems in FORTE-MM

A defining characteristic of FORTE-MM is that a meaningful share of its tasks are **not** pure offline file-processing exercises. Many real-world office tasks require the agent to operate *systems* — monitoring dashboards, business backends, web applications — that cannot be shipped as plain workspace files. To keep the benchmark deterministic, reproducible, and safe to run anywhere (and to make sure no real internal service is ever touched during an evaluation run), these tasks are backed by **mock systems**: fully self-contained stand-ins for the real tools the corresponding profession uses day-to-day.

This document is a plain-language overview of the mock systems used across the dataset — what they emulate, which task families depend on them, and how they are exercised during grading. Deployment and implementation details are kept out of scope on purpose: from a benchmark user's perspective a mock system is simply "part of the task environment", like any other input file.

## Why mock systems

Traditional agent benchmarks hand the agent a folder of files and grade the files it produces back. That covers document drafting, data cleaning, and report writing, but it systematically under-tests the *interactive* half of office work: reading numbers off a dashboard, walking a web UI, triggering a page and observing the result. FORTE-MM includes these interaction skills by giving the agent, alongside its normal workspace, access to realistic mock targets:

- **Determinism.** Every mock serves fixed, curated state. Two runs of the same task present exactly the same screens and data, so rubrics can be graded objectively (e.g. "the screenshot shows time range X to Y").
- **Isolation.** No task touches a production or internal system. Everything the agent can see is fake data authored for the benchmark.
- **Accessibility.** A mock runs wherever the benchmark runs — no credentials, no VPN, no rate limits.

## The mock systems

### Monitoring dashboards (Grafana-style) — SRE tasks

The SRE subset (monitoring / fault diagnosis) asks the agent to operate a Grafana-like monitoring platform: browse the dashboard inventory, open a specific dashboard, set a time range, inspect panels and top-bar filter variables, and produce written summaries plus evidence screenshots. The mock platform ships a fixed inventory of dashboards and a fully-rendered flagship dashboard with typed panels (timeseries, gauge, stat, table, logs) and filter variables, all serving canned, deterministic time-series data. Grading checks the agent's `result.md` and the screenshots it captures against the known dashboard structure (e.g. correct dashboard count, panel titles and types, variable names, and the time range visible in the screenshot).

> **Address placeholder.** Task instructions that reference the mock
> monitoring platform use the placeholder `MOCK_SYSTEM_IP` (e.g.
> `http://MOCK_SYSTEM_IP:8418/`) instead of a real address. Evaluators should
> substitute `MOCK_SYSTEM_IP` with the host/port where their own mock
> dashboard instance is reachable before starting the agent.

### Web application targets — QA tasks

Several QA tasks (E2E testing, browser-based regression) require a real web page to drive a browser against. Each such task bundles a self-contained single-file web application (HTML/CSS/JS, no backend) inside its own `input/` tree — e.g. an e-commerce storefront with login, catalog, and checkout flows. The instruction asks the agent to serve the page locally, explore it with a browser tool, write and run automated tests against it, and record findings. The app is deliberately seeded with specific defects; rubrics check that the agent actually launched the app, exercised the required flows, and reported the seeded defects rather than hallucinating.

### Business backends & data interfaces — BA tasks

Business-analysis tasks that would otherwise require live SQL access are instead paired with queryable mock data interfaces: small, fixed relational datasets behind a simple query endpoint, described precisely in the instruction (schema, field semantics, enum values). The agent must discover the right joins and filters to pull the numbers the task demands, and the reference answers in the rubrics are computed offline against the same fixed dataset — so numeric claims in the agent's report are checkable to the digit.

### System screenshots as ground truth — every task family

Beyond live services, most professions' tasks make heavy use of **static mock artifacts**: mock screenshots of admin consoles, chat logs, approval flows, order pages, attendance systems, and mobile apps are shipped as images in the input tree. The agent must read real information *off the screen* (OCR, layout understanding, cross-image comparison) rather than off clean structured text — this is the multimodal core of the benchmark. The mock screenshots are authored alongside the rubrics so that every fact the agent is asked to extract is unambiguous in the image.

## How mock-based tasks are graded

Mock-based tasks use exactly the same LLM-judge pipeline as every other FORTE-MM task. The mock contributes to grading in two ways:

1. **Evidence artifacts.** The instruction requires the agent to leave behind observable evidence of the interaction — screenshots saved into the workspace, test scripts it wrote, reports citing specific values from the dashboard. The judge checks these workspace artifacts against rubric items; there is no live inspection of the mock during grading.
2. **Fixed ground truth.** Because the mock's state is frozen and known, the rubric author could write exact expected values (dashboard names, panel titles, seeded defect locations, query results) into the rubrics, keeping the judge's job factual rather than judgemental.

In short: mock systems widen what the benchmark can ask the agent to *do*, while the artifact-and-rubric design keeps what the benchmark *measures* identical across all 256 tasks.
