# Rubrics

> **通过标准：所有 rubric 均须满足，该任务才算通过。任一 rubric 不通过，则该任务整体判定为不通过。**

## 文件读取路径

```path
/workspace/input/answer/2023年01月合同管理台账.xlsx
/workspace/solution/2023年01月合同管理台账-参考答案.xlsx
```

```json
[
  {
    "id": "01",
    "content": "<file>/workspace/input/answer/2023年01月合同管理台账.xlsx</file>中的sheet合同应收台账的A、B、C、L、O、R列的文本内容，与<file>/workspace/solution/2023年01月合同管理台账-参考答案.xlsx</file>的sheet合同应收台账的A、B、C、L、O、R列的文本内容完全一致",
    "weight": 1
  },
  {
    "id": "02",
    "content": "<file>/workspace/input/answer/2023年01月合同管理台账.xlsx</file>中的sheet合同应收台账中D、F、H、J、M、N、P、Q列的数值，与<file>/workspace/solution/2023年01月合同管理台账-参考答案.xlsx</file>的sheet合同应收台账中D、F、H、J、M、N、P、Q列的数值需要完全一致，保留两位小数",
    "weight": 1
  },
  {
    "id": "03",
    "content": "<file>/workspace/input/answer/2023年01月合同管理台账.xlsx</file>的sheet合同应收台账中E、I列、sheet非合同进账中D列的日期，与<file>/workspace/solution/2023年01月合同管理台账-参考答案.xlsx</file>的sheet合同应收台账中E、I列、sheet非合同进账中D列的日期完全一致，且显示的格式需要一致，如‘2025年01月01日’。",
    "weight": 1
  },
  {
    "id": "04",
    "content": "<file>/workspace/input/answer/2023年01月合同管理台账.xlsx</file>的sheet非合同进账中文本与数值内容，与<file>/workspace/solution/2023年01月合同管理台账-参考答案.xlsx</file>的sheet非合同进账中文本与数值内容需要完全一致",
    "weight": 1
  },
  {
    "id": "05",
    "content": "<file>/workspace/input/answer/2023年01月合同管理台账.xlsx</file>的sheet非合同进账中C列数值，与<file>/workspace/solution/2023年01月合同管理台账-参考答案.xlsx</file>的sheet非合同进账中C列数值需要完全一致，保留两位小数",
    "weight": 1
  },
  {
    "id": "06",
    "content": "<file>/workspace/input/answer/2023年01月合同管理台账.xlsx</file>中sheet合同应收台账中，O列的第2行数据的单元格填充为标准色黄色。；",
    "weight": 1
  }
]
```