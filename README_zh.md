# FORTE-MM：Multimodal Full-Cycle Office Real-World Task Evaluation

FORTE-MM（FORTE 的多模态版本）是一个评测 AI 智能体**多模态办公能力**的基准。每个任务是一个自包含的文件夹——智能体收到的指令，加上一个多模态的工作环境：图片、截图、扫描件、办公文档（xlsx / docx / pptx / pdf / csv）、数据文件；对于需要操作系统的任务，还配套**mock 系统**（监控看板、内置 Web 应用、可查询的数据接口），供智能体实际操作。产出物由 **LLM 裁判**依据专家标注的 rubric 对智能体工作区内的交付文件逐条核查打分。

纯文本办公基准考察的是智能体"读写文件"的能力，FORTE-MM 则聚焦真实办公所要求的多模态技能：从截图中读取数据、理解图表与扫描表单、跨图文对应信息、图片计数、以及产出引用所见内容的文档。英文版说明见 README.md。

**数据集**：完整基准共 **256 个任务**，覆盖 14 个职业工种：数据分析/商业分析/战略、算法、开发、测试、运维 SRE、财务、法务、行政、运营、市场、HR、商务销售、产品、UX/UI 设计。每个任务都带有工种、任务类型、一级/二级类目等标注。本仓库内置完整的评测基础设施，以及**每个工种一个 demo 任务**（共 14 题，随仓库附带输入文件与 rubrics）。其余任务包将在评测集正式发布时公开。

**榜单**：9 个模型在全部 256 题上的评测结果见 docs/leaderboard.md（下文也内联展示）。

交互类任务所依赖的 mock 系统（监控看板、Web 应用、数据接口）详见 docs/mock-systems.md。

## 总览

| 维度 | FORTE-MM |
|---|---|
| 任务表达 | 每任务一个文件夹：`task.yaml` 元数据 + `instruction.md` + `input/` + `solution/` |
| 模态 | 图片/截图/扫描件 + xlsx + docx + pptx + pdf + csv + 代码 + mock 系统 |
| 职业工种 | 14 个企业工种 |
| 多模态能力 | 文字识别、图表理解、多图理解、图文对应关系识别、数量识别、算术、领域知识等 |
| 评分方式 | LLM-as-judge，全对才得分（所有 rubric 均通过才计 1 分） |
| 指标 | Avg@3、Pass@3、Pass^3 |
| 智能体运行时 | OpenClaw，运行于单个 Docker 镜像内 |
| 依赖 | Python 3.10+ 标准库 + `docker` CLI |

## 榜单

以下为全部 256 题上的评测结果（每任务 3 次，全对才得分，按任务宏平均；由 LLM 裁判评分；所有模型均使用默认的推理设置）。协议细节见 docs/leaderboard.md。

| 排名 | 模型 | Avg@3 | Pass@3 | Pass^3 |
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

## 快速开始

依赖：

- Docker
- Python 3.10+（仅标准库）

1. 配置智能体与裁判共用的网关：

```bash
cp openclaw_config/openclaw.json.example openclaw_config/openclaw.json
cp openclaw_config/.env.example          openclaw_config/.env
# 在两个文件中填入网关地址与 API Key（密钥只保存在本地）。
```

2. （可选，建议）安装通用办公技能（`docx` / `pptx` / `xlsx` / `pdf`），运行器会自动注入每个智能体容器的技能目录：

```bash
bash scripts/install-anthropic-skills.sh   # SKILLS="docx xlsx" 可选装子集
```

3. 构建智能体镜像（先启动 Docker：macOS/Windows 用 Docker Desktop，Linux 用 `systemctl start docker`）：

```bash
bash docker/fetch-lo.sh
docker build -f docker/Dockerfile.agent -t mwork-agent:latest docker/
```

4. 运行——14 个 demo 任务已随仓库内置：

```bash
bash scripts/run.sh   # 跑全部任务，模型取自 openclaw.json

# 或显式指定参数：
python scripts/benchmark.py --model your-gateway/your-model --dataset ./tasks --runs 3 --concurrency 1

# 变体：TASK_ID=mm-ba-003、MODEL=...、RUNS=3 CONCURRENCY=2 bash scripts/run.sh
```

每次运行的结果落在 `<output-dir>/<model_slug>/<task_id>[_run_N]/` 下：

| 文件 | 说明 |
|---|---|
| `grading.json` | 得分（0/1）、逐 rubric 明细、异常标记 |
| `openclaw_trace.json` | 智能体原始事件流 |
| `openai_messages.json` | 展平后的 OpenAI chat-completions 视图 |
| `judge_prompt.json` | 裁判收到的完整输入（系统提示 + 用户提示 + 图片/PDF 清单） |
| `workspace/` | 智能体结束后的工作区快照 |

## 指标

每个任务运行 3 次。单次评分采用**全对才得分**：`## Grading Criteria` 中所有 rubric 全部通过该次运行才计 1 分，否则 0 分。榜单在任务粒度计算后按任务宏平均：

| 指标 | 含义 |
|---|---|
| `Avg@3` | 3 次运行的平均得分。 |
| `Pass@3` | 3 次中至少 1 次得 1 分则为 1，否则为 0。 |
| `Pass^3` | 仅当 3 次全部得 1 分才为 1 —— 衡量稳定性。 |

汇总 `./results/` 下所有模型的结果：

```bash
python scripts/aggregate.py          # 所有模型、所有任务，k=3
python scripts/aggregate.py --per-task   # 追加 (模型, 任务) 粒度明细
python scripts/aggregate.py --json       # 机器可读输出
```

## 致谢

本仓库基于 [FORTE](https://github.com/AGI-Eval-Official/FORTE)（Full-Cycle Office Real-World Task Evaluation）构建，评测运行器架构、LLM 裁判评分流程与评测方法论均源自该项目。FORTE-MM（Multimodal Full-Cycle Office Real-World Task Evaluation）是它的多模态版本。智能体运行时为 [OpenClaw](https://docs.openclaw.ai/)，感谢 OpenClaw 团队提供的优秀智能体框架。

## 引用

如果本仓库对你的研究有帮助，欢迎引用：

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

## 许可

本项目基于 MIT 许可发布，详见 LICENSE。

## 支持

维护者：Shengyu Guo — `shengyu.guo@meituan.com`。

参与建设：Jiaxing Liu、Zeyang Hu、Shengyu Guo、Chen Chen、Fengjiao Chen、Yifan Yang、Xuezhi Cao、Ziwen Wang。