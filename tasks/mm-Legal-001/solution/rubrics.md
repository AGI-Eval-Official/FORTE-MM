# Rubrics

> **通过标准：所有 rubric 均须满足，该任务才算通过。任一 rubric 不通过，则该任务整体判定为不通过。**

## 文件读取路径

```path
/workspace/input/answer/用印合规审查表.csv
/workspace/solution/用印合规审查表-参考答案.csv
```

```json
[
  {
    "id": "01",
    "content": "输出的<file>/workspace/input/answer/用印合规审查表.csv</file>中'申请单链接'之外的其他列文字内容与参考答案<file>/workspace/solution/用印合规审查表-参考答案.csv</file>完全一致。",
    "weight": 1
  },
  {
    "id": "02",
    "content": "输出的<file>/workspace/input/answer/用印合规审查表.csv</file>中的'申请单链接'列的第 2–6 行的 5 个单元格内数据，由上到下其值分别以 `申请单1.png`、`申请单2.png`、`申请单4.png`、`申请单3.png`、`申请单5.png` 结尾。",
    "weight": 1
  }
]
```
