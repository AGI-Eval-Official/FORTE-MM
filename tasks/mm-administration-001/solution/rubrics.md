# Rubrics

> **通过标准：所有 rubric 均须满足，该任务才算通过。任一 rubric 不通过，则该任务整体判定为不通过。**

## 文件读取路径

```path
/workspace/input/answer/翻新区域桌椅数量统计表.csv
/workspace/input/answer/办公椅参考品牌数据信息.csv
/workspace/solution/翻新区域桌椅数量统计表标准答案.csv
```

```json
[
  {
    "id": "01",
    "content": "输出了<file>/workspace/input/answer/翻新区域桌椅数量统计表.csv</file>，与<file>/workspace/solution/翻新区域桌椅数量统计表标准答案.csv</file>的文字内容完全一致",
    "weight": 1
  },
  {
    "id": "02",
    "content": "输出了<file>/workspace/input/answer/办公椅参考品牌数据信息.csv</file>，必须包含“品牌名称”“产品名称”“产品价格”“产品购买的网站链接”的对应内容（不要求字段与上述完全一致）",
    "weight": 1
  },
  {
    "id": "03",
    "content": "<file>/workspace/input/answer/办公椅参考品牌数据信息.csv</file>中的产品都是黑色椅子，且椅子价格不高于300元/把",
    "weight": 1
  },
  {
    "id": "04",
    "content": "<file>/workspace/input/answer/办公椅参考品牌数据信息.csv</file>中只有5个不同品牌，每个品牌只列出3个不同产品",
    "weight": 1
  }
]
```