请打开

```
/workspace/input/校招岗位筛选标准.md
/workspace/input/简历材料/陈浩宇_简历.pdf
/workspace/input/简历材料/陈浩宇_成绩单.png
/workspace/input/简历材料/陈浩宇_英语证书.png
/workspace/input/简历材料/林晓雪_简历.pdf
/workspace/input/简历材料/林晓雪_成绩单.png
/workspace/input/简历材料/林晓雪_英语证书.png
/workspace/input/简历材料/张明远_简历.pdf
/workspace/input/简历材料/张明远_成绩单.png
/workspace/input/简历材料/张明远_英语证书.png
/workspace/input/简历材料/王思琪_简历.pdf
/workspace/input/简历材料/王思琪_成绩单.png
/workspace/input/简历材料/王思琪_英语证书.png
/workspace/input/简历材料/刘子豪_简历.pdf
/workspace/input/简历材料/刘子豪_成绩单.png
/workspace/input/简历材料/刘子豪_英语证书.png
/workspace/input/简历材料/赵雨桐_简历.pdf
/workspace/input/简历材料/赵雨桐_成绩单.png
/workspace/input/简历材料/赵雨桐_英语证书.png
/workspace/input/简历材料/孙浩然_简历.pdf
/workspace/input/简历材料/孙浩然_成绩单.png
/workspace/input/简历材料/孙浩然_英语证书.png
/workspace/input/简历材料/吴梦琳_简历.pdf
/workspace/input/简历材料/吴梦琳_成绩单.png
/workspace/input/简历材料/吴梦琳_英语证书.png
```
请根据《校招岗位筛选标准》对每份候选人简历进行多维度综合审核。**硬性条件未全部满足的候选人直接排除，不纳入输出结果。** 将硬性条件全部通过的候选人筛选结果输出至：

```
/workspace/input/answer/校招岗位筛选清单.csv
```

## 输出格式要求

将**硬性条件全部通过**的候选人审核结果汇总输出为 CSV 文件。**CSV 必须为标准横向表格格式：第一行为表头（字段名），后续每行对应一位候选人数据。** 包含以下字段（按此顺序排列）：

| 字段 | 说明 |
|------|------|
| 序号 | 候选人编号 |
| 姓名 | 候选人姓名 |
| 学校 | 毕业院校 |
| 专业 | 所学专业 |
| 学历 | 本科/硕士 |
| GPA | 绩点（提取成绩单中的综合GPA，填写格式为A/B，其中A为学生的综合绩点，B为满绩绩点） |
| 英语成绩 | CET-4/CET-6：分数 （此处不录入托福雅思分数，前面为具体的英语等级，填写英文简写，'分数'处填写具体的分数，填写阿拉伯数字） |
| 学历背景得分 | **仅填写纯数字**，档位对应：S=20 / A=16 / B=13 / C=9；硬性不通过记0 |
| 学业成绩得分 | **仅填写纯数字**，档位对应：S=20 / A=16 / B=13 / C=10；硬性不通过记0 |
| 英语能力得分 | **仅填写纯数字**，档位对应：S=10 / A=8 / B=6 / C=4；硬性不通过记0 |
| 项目实习得分 | **仅填写纯数字**，档位对应：S=30 / A=24 / B=19 / C=13；硬性不通过记0 |
| 竞赛科研得分 | **仅填写纯数字**，档位对应：S=20 / A=15 / B=10 / C=6 / 无经历=0；硬性不通过记0 |
| 总分 | 各维度得分之和 |
| 推荐档次 | A档推荐 / B档推荐 / C档待定 / 不通过 |

CSV 文件应按推荐档次排序（A档→B档→C档待定），同档次内按总分降序排列。

请直接执行操作，不要问我任何问题，也不要让我做出进一步决策。如果遇到任何问题和决策点，请你自行解决。
