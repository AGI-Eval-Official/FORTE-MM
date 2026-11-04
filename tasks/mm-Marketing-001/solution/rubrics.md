# Rubrics

> **通过标准：所有 rubric 均须满足，该任务才算通过。任一 rubric 不通过，则整体判定为 FAIL。**

## 文件读取路径

```path
/workspace/input/answer/海报规范审核明细表.xlsx
/workspace/solution/《海报规范审核明细表》参考答案.xlsx
```

```json
[
  {
    "id": "01",
    "content": "输出的<file>/workspace/input/answer/海报规范审核明细表.xlsx</file>文件sheet1和sheet2与<file>/workspace/solution/《海报规范审核明细表》参考答案.xlsx</file>的sheet1和sheet2的A-K列的填写内容完全一致",
    "weight": 1
  } ,
  {
    "id": "02",
    "content": "输出的<file>/workspace/input/answer/海报规范审核明细表.xlsx</file>文件sheet1中，B3、C3、J3、K3、D5、E5、F5、I5、J5、K5单元格填充为标准红色，其它单元格均无填充；sheet2中，B2、C2、J2、K2、D3、E3、F3、I3、J3、K3单元格填充为标准红色，其它单元格均无填充；",
    "weight": 1
  },
  {
    "id": "03",
    "content": "输出的<file>/workspace/input/answer/海报规范审核明细表.xlsx</file>文件中，sheet1的L2、L4单元格内容填写为'无问题'",
    "weight": 1
  }
]
```