# Rubrics

> **通过标准：所有 rubric 均须满足，该任务才算通过。任一 rubric 不通过，则该任务整体判定为不通过。**

## 文件读取路径

```path
/workspace/input/answer/test_ecommerce.py
/workspace/input/answer/screenshots/*
/workspace/input/answer/test_report.md
```

```json
[
  {
    "id": "01",
    "content": "输出了<file>/workspace/input/answer/test_ecommerce.py</file>和<file>/workspace/input/answer/test_report.md</file>两个文件，且<file>/workspace/input/answer/screenshots/</file>目录下至少存在8张截图文件（每条路径至少1张），且截图文件命名包含对应的PATH-XX标识。若缺少任意一项，则不通过。",
    "weight": 1
  },
  {
    "id": "02",
    "content": "读取<file>/workspace/input/answer/test_ecommerce.py</file>，脚本满足以下全部条件：（1）使用playwright.sync_api的同步API；（2）包含8个独立测试函数，函数名格式为test_path_XX；（3）选择器优先使用data-testid属性；（4）每个测试函数内包含截图调用。缺少任意一项不得分。",
    "weight": 1
  },
  {
    "id": "03",
    "content": "读取<file>/workspace/input/answer/test_ecommerce.py</file>，脚本中PATH-01和PATH-02的断言完整：（1）PATH-01包含对URL跳转至/home的断言（expect(page).to_have_url或等效写法）；（2）PATH-01包含对localStorage中auth_token存在的断言（通过page.evaluate读取）；（3）PATH-02包含对错误提示文案的断言（文案包含'用户名或密码错误'）；（4）PATH-02包含对第3次错误后锁定提示的断言（文案包含'锁定'或'locked'）。缺少任意一项不得分。",
    "weight": 1
  },
  {
    "id": "04",
    "content": "读取<file>/workspace/input/answer/test_ecommerce.py</file>，脚本中PATH-03至PATH-05的断言完整：（1）PATH-03包含对URL中q参数存在的断言；（2）PATH-03包含对搜索结果列表数量大于0的断言；（3）PATH-04包含对购物车数量徽标+1的断言；（4）PATH-05包含对URL跳转至/payment的断言；（5）PATH-05包含对URL中orderId参数存在的断言。缺少任意一项不得分。",
    "weight": 1
  },
  {
    "id": "05",
    "content": "读取<file>/workspace/input/answer/test_ecommerce.py</file>，脚本中PATH-06至PATH-08的断言完整：（1）PATH-06包含对URL跳转至/order/success的断言；（2）PATH-06包含对订单号元素文本非空的断言（data-testid='success-order-id'）；（3）PATH-07包含对URL跳转至/order/fail的断言；（4）PATH-07包含对失败原因文案可见的断言（data-testid='fail-reason'）；（5）PATH-08包含对停留在/cart的断言；（6）PATH-08包含对空购物车提示文案可见的断言（data-testid='cart-empty-msg'）。缺少任意一项不得分。",
    "weight": 1
  },
  {
    "id": "06",
    "content": "读取<file>/workspace/input/answer/test_report.md</file>，报告满足以下条件：（1）包含8条路径的逐项执行结果，每条路径明确标注通过/失败及原因；（2）包含截图文件清单，列出每条路径对应的截图文件名；（3）包含总体通过率。缺少任意一项不得分。",
    "weight": 1
  },
  {
    "id": "07",
    "content": "读取<file>/workspace/input/answer/test_report.md</file>，报告中确认：（1）PATH-01（正常登录）通过，且说明auth_token已验证；（2）PATH-02（登录锁定）通过，且说明锁定提示已验证；（3）PATH-06（支付成功）通过，且说明订单号非空已验证；（4）PATH-08（空购物车）通过，且说明空购物车提示已验证。缺少任意一项不得分。",
    "weight": 1
  }
]
```
