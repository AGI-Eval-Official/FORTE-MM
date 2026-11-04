# Rubrics

> **通过标准：所有 rubric 均须满足，该任务才算通过。任一 rubric 不通过，则整体判定为 FAIL。**

## 文件读取路径

```path
/workspace/input/1.png
/workspace/input/2.png
/workspace/input/3.png
/workspace/input/4.png
/workspace/input/5.png
/workspace/input/answer/封面图打分报告.pdf
```

```json
[
  {
    "id": "01",
    "content": "输出了<file>/workspace/input/answer/封面图打分报告.pdf</file>。",
    "weight": 1
  },
  {
    "id": "02",
    "content": "输出的<file>/workspace/input/answer/封面图打分报告.pdf</file>文档中，至少包含'业务分析背景'、'评估标准'、'单图分析'、'综合评分表'、'优化建议'这5部分内容。",
    "weight": 1
  },
  {
    "id": "03",
    "content": "输出的<file>/workspace/input/answer/封面图打分报告.pdf</file>文档中，'单图分析'部分分别有对5张图的多维分析图文内容。",
    "weight": 1
  },
  {
    "id": "04",
    "content": "输出了<file>/workspace/input/answer/封面图打分报告.pdf</file>文档中，'单图分析'部分依次插入对应图片及文段，其中<file>/workspace/input/1.png</file>插入到对'1.png'的整体分析段落的上一行,<file>/workspace/input/2.png</file>插入到对'2.png'的整体分析段落的上一行,<file>/workspace/input/3.png</file>插入到对'3.png'的整体分析段落的上一行,<file>/workspace/input/4.png</file>插入到对'4.png'的整体分析段落的上一行,<file>/workspace/input/5.png</file>插入到对'5.png'的整体分析段落的上一行。",
    "weight": 1
  },
  {
    "id": "05",
    "content": "输出的<file>/workspace/input/answer/封面图打分报告.pdf</file>文档中，'综合评分表'至少有'图片命名'、'标题可读性'、'主体突出度'、'色彩对比'、'信息密度'、'点击钩子'、'创意和独特性'、'总得分'8个统计字段，5行统计数据。",
    "weight": 1
  },
  {
    "id": "06",
    "content": "输出的<file>/workspace/input/answer/封面图打分报告.pdf</file>文档中，'综合评分表'中'图片命名'列每行填入内容为'x.png'(x为1-5的整数)；'标题可读性'、'主体突出度'、'色彩对比'、'信息密度'、'点击钩子'、'创意和独特性'这6列每行填入内容均为对应图片的整数分数，范围均为1-10分；'总得分'列每行填入内容为该行前6个维度分数的总和，范围应在1-60分内。",
    "weight": 1
  },
  {
    "id": "07",
    "content": "输出的<file>/workspace/input/answer/封面图打分报告.pdf</file>文档中，'综合评分表'按'总得分'列降序排列。",
    "weight": 1
  }
]
```