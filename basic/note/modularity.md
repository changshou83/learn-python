
## 1. 基本概念
- 一个 `.py` 文件 = 一个模块
- 一个文件夹（含 `__init__.py`）= 包（Python3.3+ 甚至可以没有 __init__.py）

顶层定义的东西自动可导出。

## 2. 定义模块
```python
# utils.py
def add(a, b):
    return a + b

PI = 3.14
```

## 3. 三种导入方式
```python
# 导入整个模块
import utils
utils.add(1,2)

# 按需导入
from utils import add
add(1,2)

# 起别名
from utils import add as plus
plus(1,2)
```

## 4. 文件夹包（多级）
结构：
```
main.py
tools/
  __init__.py // (1)作为桶文件批量导出模块内容（2）控制 * 导入的内容
  math.py
```
导入：
```python
from tools.math import add
```

## 5. 进阶技巧

### 入口判断
```python
if __name__ == '__main__':
    # 直接运行该文件时执行，被其他文件导入时不执行
    print(add(2,3))
```

### `__init__.py` 的作用

1. 作为桶文件批量导出模块内容
2. 控制 * 导入的内容：`__all__ = [<allow_import_member>];`

### 跨目录导入

所有导入都要用绝对路径。

### 相对导入

- `.` 代表当前目录
- `..` 代表上一级目录

### 模块私有化

以 _ 开头的函数 / 变量，默认不会被 import * 导入。

### 寻找模块的规则

1. 当前目录
2. 环境变量 PYTHONPATH 里的目录
3. Python 安装目录的标准库
4. site-packages（第三方库）

## 6. 现代项目目录结构

```plaintext
my_project/                # 项目根目录
├── main.py                # 项目唯一入口
├── .env                   # 环境变量
├── requirements.txt       # 依赖
└── app/                   # 主包（所有业务代码）
    ├── __init__.py
    ├── api/               # 接口层（路由/控制器）
    │   ├── __init__.py
    │   ├── user.py
    │   └── order.py
    ├── core/              # 核心配置、全局设置
    │   ├── __init__.py
    │   ├── config.py
    │   └── exceptions.py
    ├── db/                # 数据库相关
    │   ├── __init__.py
    │   ├── base.py        # 基类模型
    │   └── session.py     # 连接池
    ├── models/            # ORM 模型表结构
    │   ├── __init__.py
    │   ├── user.py
    │   └── order.py
    ├── schemas/           # Pydantic 校验、DTO
    │   ├── __init__.py
    │   ├── user.py
    │   └── order.py
    ├── services/          # 业务逻辑层
    │   ├── __init__.py
    │   ├── user_service.py
    │   └── order_service.py
    ├── utils/             # 工具函数
    │   ├── __init__.py
    │   ├── crypto.py
    │   ├── time_tools.py
    │   └── logger.py
    ├── middlewares/       # 中间件（鉴权、日志、跨域）
    ├── logs/              # 日志
    ├── static/            # 静态资源（可选）
    ├── constants/         # 常量、枚举（可选）
    └── tasks/             # 定时 / 异步任务（可选）
```
