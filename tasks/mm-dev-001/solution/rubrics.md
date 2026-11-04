# Rubrics

> **通过标准：所有 rubric 均须满足，该任务才算通过。任一 rubric 不通过，则整体判定为不通过。**

## 文件读取路径

```path
/workspace/input/answer/PostgreSQL.md
```

```json
[
    {
    "id": "01",
    "content": "输出了<file>/workspace/input/answer/PostgreSQL.md</file>文件",
    "weight": 1
  },
  {
    "id": "02",
    "content": "准确识别设计图中的物理实现问题。在建表时，必须消除这些冗余属性，强制使用外键引用替代重复存储的数据，确保数据的一致性。若直接照搬图中所有线条导致字段重复，或未处理逻辑陷阱，则不通过。",
    "weight": 1
  },
  {
    "id": "03",
    "content": "正确识别图中实体间的关系，并在物理实现中通过外键约束体现。对于中间关联实体，必须建立正确的外键约束，分别指向其关联的两个父级实体。若外键关系建立错误、缺失或未体现双向约束，则不通过",
    "weight": 1
  },
  {
    "id": "04",
    "content": "为每张表正确识别并设置主键，且主键数据类型符合规范。根据字段含义合理映射数据类型，确保数据的准确性和完整性。若主键缺失、定义错误，或数据类型映射不合理（如金额使用字符串），则不通过",
    "weight": 1
  },
  {
    "id": "05",
    "content": "生成的SQL代码必须符合标准的PostgreSQL语法规范，若输出其他数据库的语法，则不通过。",
    "weight": 1
  },
    {
    "id": "06",
    "content": "生成的PostgreSQL DDL脚本中要包含建表语句、表关系定义语句和数据约束语句，若缺少，则不通过。",
    "weight": 1
  },
    {
  "id": "07",
  "content": "必须完整映射ER图中的所有实体。若有遗漏图中的实体未生成建表语句，则不通过。",
  "weight": 1
},
    {
  "id": "08",
  "content": "<file>/workspace/input/answer/PostgreSQL.md</file>要包含分析说明、实体关系映射和PostgreSQL DDL，若缺少，则不通过。",
  "weight": 1
}
]
```

