# Rubrics

> **通过标准：所有 rubric 均须满足，该任务才算通过。任一 rubric 不通过，则该任务整体判定为不通过。**

## 文件读取路径

```path
/workspace/input/answer/answer.md
```

```json
[
  {
    "id": "01",
    "content": "正确识别架构图中红色框选区域对应的目标模块为DPT",
    "weight": 1
  },
  {
    "id": "02",
    "content": "正确指出DPT模块的核心实现文件为vggt/heads/dpt_head.py",
    "weight": 1
  },
  {
    "id": "03",
    "content": "正确说明DPT模块数据流的完整顺序，至少覆盖以下四个阶段并按顺序呈现：1，经 forward分块调度后进入 _forward_impl执行实际处理；2，遍历intermediate_layer_idx 提取多层 patch token 并投影为 2D 特征图（多尺度特征提取）；3，经 scratch_forward 中 refinenet 逐级融合多尺度特征；4，经 output_conv2 与 activate_head 输出预测值与置信度。若顺序混乱或缺少其中任意一个阶段，则不通过",
    "weight": 1
  },
  {
    "id": "04",
    "content": "在 dpt_head.py 中定位到DPTHead.forward 的入口，需覆盖第 115～172 行中的至少一行，并说明 forward 接收 aggregated_tokens_list 作为输入、按 frames_chunk_size 分块调度后调用 _forward_impl 执行实际处理。若只说forward接收输入而无行号，或给出的行号不在第 115～172 行范围内，则不通过",
    "weight": 1
  },
  {
    "id": "05",
    "content": "在 dpt_head.py 中定位到多尺度 token 提取与投影的实现（_forward_impl），需覆盖第 205～224 行中的至少一行，并说明该段代码的核心数据变换逻辑和代码解读。若只说明了数据变换逻辑而无行号，或给出的行号不在第 205～224 行范围内，则不通过",
    "weight": 1
  },
  {
    "id": "06",
    "content": "在 dpt_head.py 中定位到多尺度特征融合的实现（scratch_forward），需覆盖第 261～291 行中的至少一行，并说明该段代码的核心数据变换逻辑和代码解读。若只说有特征融合而无行号，或给出的行号不在第 261～291 行范围内，则不通过",
    "weight": 1
  },
  {
    "id": "07",
    "content": "在 dpt_head.py 中定位到最终输出生成的实现，需覆盖第 229～247 行中的至少一行，并说明该段代码的核心数据变换逻辑和代码解读。若只说输出了预测结果而无行号，或给出的行号不在第 229～247 行范围内，则不通过",
    "weight": 1
  },
  {
    "id": "08",
    "content": "回答须聚焦于DPT模块的结构与代码实现。若将 Aggregator、Global Attention、Frame Attention、Camera Head、Track Head 或训练策略等无关内容作为主答案大篇幅展开，则不通过",
    "weight": 1
  }
]
```
