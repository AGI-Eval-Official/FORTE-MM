# Rubrics

> **通过标准：所有 rubric 均须满足，该任务才算通过。任一 rubric 不通过，则该任务整体判定为不通过。**

## 文件读取路径

```path
/workspace/input/answer/售后反馈分析报告.docx
```

```json
[
  {
    "id": "01",
    "content": "<file>/workspace/input/answer/售后反馈分析报告.docx</file> 中至少需包含'问题类型数量统计'、'典型图片示例'、'归因结论与改进建议'这三个主要章节",
    "weight": 1
  },
  {
    "id": "02",
    "content": "<file>/workspace/input/answer/售后反馈分析报告.docx</file> 中存在一个包含问题类型数量统计的表格，该表格有且仅有'问题类型'和'数量'两列",
    "weight": 1
  },
  {
    "id": "03",
    "content": "<file>/workspace/input/answer/售后反馈分析报告.docx</file> 中的问题类型统计表格中，'问题类型'列从上至下所填内容依次为'包装破损'、'商品瑕疵'、'错发漏发'、'物流延迟'、'其他'；'数量'列从上至下所填内容依次为2，2，0，1，0",
    "weight": 1
  },
  {
    "id": "04",
    "content": "<file>/workspace/input/answer/售后反馈分析报告.docx</file> 中至少嵌入了3张不同的图片",
    "weight": 1
  }
]
```
