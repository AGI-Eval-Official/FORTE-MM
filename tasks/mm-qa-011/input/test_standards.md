# E2E 测试规范文档

## 测试框架规范

本项目 E2E 测试使用 **Playwright（Python 版）** 编写，测试脚本须满足以下规范：

### 脚本结构规范

```python
# 标准测试用例结构
from playwright.sync_api import sync_playwright, expect

def test_case_name(page):
    # 1. 导航到目标页面
    page.goto("http://localhost:PORT/path")
    
    # 2. 执行用户操作（填写表单、点击按钮等）
    page.fill("selector", "value")
    page.click("selector")
    
    # 3. 等待页面响应
    page.wait_for_url("**/target-path**")
    # 或
    page.wait_for_selector("selector")
    
    # 4. 断言验证
    expect(page.locator("selector")).to_be_visible()
    expect(page).to_have_url(re.compile(r"/target"))
```

### 选择器规范

优先级（从高到低）：
1. `data-testid` 属性：`[data-testid="login-btn"]`
2. ARIA 角色：`role=button[name="登录"]`
3. 文本内容：`text=登录`
4. CSS 类（最低优先级，避免使用）

### 断言规范

| 断言场景 | 推荐写法 |
|----------|----------|
| 元素可见 | `expect(locator).to_be_visible()` |
| URL 匹配 | `expect(page).to_have_url(re.compile(r"pattern"))` |
| 文本内容 | `expect(locator).to_have_text("text")` |
| 元素数量 | `expect(locator).to_have_count(n)` |
| 属性值 | `expect(locator).to_have_attribute("attr", "value")` |
| LocalStorage | 通过 `page.evaluate()` 读取并断言 |

### 截图规范

- 每个测试用例执行完毕后必须截图留证
- 截图命名格式：`{PATH_ID}-{step_name}.png`，如 `PATH-01-login-success.png`
- 截图保存路径：`/workspace/input/answer/screenshots/`
- 失败用例截图命名加 `-FAIL` 后缀

### 超时配置

| 操作类型 | 超时时间 |
|----------|----------|
| 页面导航 | 10000ms |
| 元素等待 | 5000ms |
| 网络请求 | 8000ms |

## 测试覆盖要求

E2E 测试脚本必须覆盖以下 8 条测试路径（对应需求文档中的 PATH-01 ~ PATH-08）：

| 路径ID | 必须包含的断言 |
|--------|--------------|
| PATH-01 | URL跳转至/home；LocalStorage中auth_token存在 |
| PATH-02 | 错误提示文案可见；第3次错误后锁定提示可见 |
| PATH-03 | URL包含q参数；搜索结果列表数量>0 |
| PATH-04 | 购物车数量徽标+1；跳转至/cart后商品存在 |
| PATH-05 | URL跳转至/payment；URL包含orderId参数 |
| PATH-06 | URL跳转至/order/success；订单号元素非空 |
| PATH-07 | URL跳转至/order/fail；失败原因文案可见 |
| PATH-08 | 停留在/cart；空购物车提示文案可见 |

## 测试报告规范

测试执行完毕后须生成测试报告，包含：
- 每条路径的执行结果（通过/失败）
- 失败原因（如有）
- 截图文件清单
- 总体通过率
