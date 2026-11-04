你是电商平台的前端测试工程师，负责对一个已完成开发的电商 Web 应用进行 E2E 自动化测试。团队提供了用户交互流程图、功能需求文档、测试规范和覆盖率预算，你需要从流程图中解析关键测试路径，编写 Playwright 测试脚本，执行测试并截图留证，最终生成测试覆盖率报告。

## 可用资源

1. **用户交互流程图**：位于 `/workspace/input/user_flow_diagram.png`，标注了 8 条测试路径（PATH-01 ~ PATH-08）、操作节点、断言点和异常路径
2. **功能需求文档**：位于 `/workspace/input/app_requirements.md`，定义了页面路由、交互行为规范和测试路径说明
3. **测试规范文档**：位于 `/workspace/input/test_standards.md`，规定了 Playwright 脚本结构、选择器优先级、断言写法和截图命名规范
4. **覆盖率预算**：位于 `/workspace/input/coverage_budget.csv`，定义了 8 条路径的优先级、最少断言数和超时配置
5. **被测应用**：位于 `/workspace/input/ecommerce-app.html`，是一个可直接运行的单文件 HTML 电商应用

## 任务要求

### 第一步：理解测试目标

1. 读取 `/workspace/input/user_flow_diagram.png`，识别图中标注的 8 条测试路径（PATH-01 ~ PATH-08）、各路径的起止页面、操作步骤和断言点
2. 读取 `/workspace/input/app_requirements.md`，理解每条路径对应的功能需求和预期行为
3. 读取 `/workspace/input/test_standards.md`，掌握脚本编写规范
4. 读取 `/workspace/input/coverage_budget.csv`，了解各路径的优先级和断言要求

### 第二步：启动本地服务器

使用任意方式（如 Python `http.server`）在本地启动 HTTP 服务器，托管 `/workspace/input/ecommerce-app.html`，确认页面可正常访问。

### 第三步：编写 Playwright 测试脚本

编写 Python Playwright 测试脚本，覆盖 8 条测试路径：

1. **脚本要求**：
   - 使用 `playwright.sync_api` 的同步 API
   - 每条路径作为独立函数，函数名格式为 `test_path_XX`（如 `test_path_01`）
   - 选择器优先使用 `data-testid` 属性（参考需求文档中的 `data-testid` 值）
   - 每条路径执行完毕后截图，命名格式：`PATH-XX-{step}.png`
   - 脚本可通过 `python test_ecommerce.py` 独立执行

2. **必须覆盖的断言**（参考测试规范文档）：
   - PATH-01：登录成功后 URL 为 `/home`；`localStorage.auth_token` 存在
   - PATH-02：错误密码提示文案包含"用户名或密码错误"；第 3 次错误后显示锁定提示
   - PATH-03：搜索后 URL 包含 `q` 参数；搜索结果列表数量 > 0
   - PATH-04：加入购物车后购物车数量徽标 +1；跳转至 `/cart` 后商品存在
   - PATH-05：提交订单后 URL 跳转至 `/payment`；URL 包含 `orderId` 参数
   - PATH-06：支付成功后 URL 为 `/order/success`；订单号元素文本非空
   - PATH-07：支付失败后 URL 为 `/order/fail`；失败原因文案可见
   - PATH-08：购物车为空时点击结算，停留在 `/cart`；空购物车提示文案可见

3. **保存脚本**：将脚本保存至 `/workspace/input/answer/test_ecommerce.py`

### 第四步：执行测试并截图

执行测试脚本，将所有截图保存至 `/workspace/input/answer/screenshots/`，截图命名须符合规范。

### 第五步：生成测试覆盖率报告

生成 `/workspace/input/answer/test_report.md`，报告须包含：
- 8 条路径的逐项执行结果（通过/失败及原因）
- 截图文件清单（路径ID → 截图文件名）
- 总体通过率（通过路径数 / 8）
- 如有失败路径，说明失败原因及是否已修复

## 输出路径

| 文件 | 路径 |
|------|------|
| Playwright 测试脚本 | `/workspace/input/answer/test_ecommerce.py` |
| 测试截图目录 | `/workspace/input/answer/screenshots/` |
| 测试覆盖率报告 | `/workspace/input/answer/test_report.md` |

## 注意事项

- 测试脚本中的服务器端口须与实际启动的端口一致，不要硬编码为固定端口，应自动探测或使用随机可用端口
- 每条路径的截图必须在断言通过后拍摄，不得在页面加载中截图
- PATH-02（登录锁定）测试完成后须重置登录状态，避免影响后续路径
- PATH-04 和 PATH-05 存在依赖关系（需先加入购物车才能结算），脚本须保证执行顺序

请直接执行操作，不要问我任何问题，也不要让我做出进一步决策。如果遇到任何问题和决策点，请你自行解决。
