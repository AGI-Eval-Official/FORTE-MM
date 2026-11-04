你是一名 SRE 工程师，需要熟悉当前监控平台的 Dashboard 结构。

**Grafana 地址**：http://MOCK_SYSTEM_IP:8418/（无需登录）
**时间范围**：`2026-04-27T09:45:00.000Z` 到 `2026-04-27T11:10:00.000Z`（UTC）

**任务**：
请打开 Grafana 首页，找到所有可用的 Dashboard，然后逐一打开截图。
将以下信息写入 `/workspace/input/answer/result.md`：
1. Grafana 中共有多少个 Dashboard？列出每个 Dashboard 的名称
2. 打开 **MLT Dashboard**，设置上述时间范围，截图保存到 `/workspace/input/answer/mlt_dashboard.png`
3. 观察 MLT Dashboard，列出所有面板（Panel）的标题和类型
4. 列出 Dashboard 顶部的所有筛选变量（Variable）名称

结果文件格式：
```
## Grafana Dashboard 概览

### Dashboard 列表
共 <N> 个 Dashboard：
- <Dashboard名称1>
- <Dashboard名称2>
- ...

### MLT Dashboard 面板列表
- <面板标题>：<面板类型>
- ...

### 筛选变量
- <变量名称1>
- <变量名称2>
- ...
```
