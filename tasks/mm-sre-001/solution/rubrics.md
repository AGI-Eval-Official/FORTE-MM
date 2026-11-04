# Rubrics
> **每个 rubric 独立评分，满分 5 分。**
>
> 参考答案：
> - Grafana 中共有 4 个 Dashboard：MLT Dashboard、MLT Erroring Endpoints、Official k6 Test Result、Traces in Dashboards
> - MLT Dashboard 有 8 个面板：Request Rate（timeseries）、Overall Error %age（gauge）、Error Percentages by Target（stat）、HTTP Status codes by Endpoint（table）、Top 10 Highest Endpoint Latencies Over Last Minute（table）、All Endpoint Latencies in ms (Last 10 mins)（timeseries）、95th Percentile Response Latencies (ms)（timeseries）、Autologged Errors（logs）
> - 筛选变量有 3 个：HTTP Status、HTTP Endpoint、Service Version

## 文件读取路径
```path
/workspace/input/answer/result.md
/workspace/input/answer/时间设置截图.png
```

```json
[
  {
    "id": "MM-SRE-001-1",
    "content": "<file>/workspace/input/answer/result.md</file> 中列出了 4 个 Dashboard 名称，MLT Dashboard、MLT Erroring Endpoints、Official k6 Test Result、Traces in Dashboards",
    "weight": 1
  },
  {
    "id": "MM-SRE-001-2",
    "content": "<file>/workspace/input/answer/result.md</file> 中列出了 MLT Dashboard 8个面板标题，Request Rate（timeseries）、Overall Error %age（gauge）、Error Percentages by Target（stat）、HTTP Status codes by Endpoint（table）、Top 10 Highest Endpoint Latencies Over Last Minute（table）、All Endpoint Latencies in ms (Last 10 mins)（timeseries）、95th Percentile Response Latencies (ms)（timeseries）、Autologged Errors（logs）",
    "weight": 1
  },
  {
    "id": "MM-SRE-001-3",
    "content": "<file>/workspace/input/answer/result.md</file> 中列出了 3 个筛选变量：HTTP Status、HTTP Endpoint、Service Version",
    "weight": 1
  },
  {
    "id": "MM-SRE-001-4",
    "content": "<file>/workspace/input/answer/时间设置截图.png</file>存在，且正确显示时间范围`2026-04-27T09:50:00.000Z` 到 `2026-04-27T10:10:00.000Z`（UTC）",
    "weight": 1
  }
]
```
