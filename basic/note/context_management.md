Python 上下文管理是**管理资源（文件、网络连接、数据库连接、锁）**的核心机制，核心作用是：**自动分配和释放资源**，避免资源泄漏，代码更简洁安全。

最常见的用法就是 `with` 语句，它是上下文管理的语法糖。


## 一、with 语句
`with` 会自动处理**进入**和**退出**上下文，无论代码正常执行还是抛出异常，都会**自动释放资源**。

### 经典例子：文件操作
```python
# 推荐写法：自动打开、自动关闭文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 出了 with 代码块，文件自动关闭，无需手动 f.close()
```

**对比传统写法（容易忘关文件）：**
```python
# 不推荐：必须手动关闭，异常时还可能关不掉
f = open("test.txt", "r")
content = f.read()
f.close()  # 容易遗漏
```

## 二、上下文管理的原理
一个对象要支持 `with`，必须实现**两个魔法方法**：
1. `__enter__()`：进入 `with` 块时执行（分配资源）
2. `__exit__()`：离开 `with` 块时执行（释放资源，无论是否异常）

### 手写一个上下文管理器
```python
class MyResource:
    # 初始化
    def __init__(self, name):
        self.name = name

    # 进入上下文
    def __enter__(self):
        print(f"[进入] 分配资源：{self.name}")
        return self  # 返回的值会被 as 接收

    # 退出上下文（自动处理异常）
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[退出] 释放资源：{self.name}")
        
        # 参数说明：
        # exc_type：异常类型
        # exc_val：异常对象
        # exc_tb：异常追踪信息
        return False  # False=不屏蔽异常，True=屏蔽异常

# 使用
with MyResource("数据库连接") as res:
    print(f"使用资源：{res.name}")
    # 这里抛异常也会自动执行 __exit__
```

**输出：**
```
[进入] 分配资源：数据库连接
使用资源：数据库连接
[退出] 释放资源：数据库连接
```


## 三、@contextmanager 装饰器

### 示例：自定义上下文管理器
```python
from contextlib import contextmanager

@contextmanager
def my_context(name):
    # ———— 上方：__enter__ 逻辑 ————
    print(f"[进入] 准备资源：{name}")
    
    try:
        # yield 之前 = 进入
        # yield 后面的值 = as 接收的值
        yield f"资源对象：{name}"
        
    finally:
        # ———— 下方：__exit__ 逻辑（一定会执行）————
        print(f"[退出] 清理资源：{name}")

# 使用
with my_context("测试资源") as res:
    print(res)
    print("执行业务逻辑")
```


## 四、常用内置上下文管理器
Python 很多内置对象天然支持 `with`：
1. **文件操作**：`with open(...) as f`
2. **数据库连接**（pymysql、sqlite3）
3. **网络请求**（requests 不直接支持，但可以封装）


## 五、高级用法
### 1. 嵌套多个上下文
```python
with open("a.txt") as f1, open("b.txt") as f2:
    # 同时管理两个文件，都自动关闭
    pass
```

### 2. 忽略异常（contextlib.suppress）
```python
from contextlib import suppress

# 忽略 FileNotFoundError 异常
with suppress(FileNotFoundError):
    open("不存在的文件.txt")
print("代码继续执行")
```

### 3. 临时重定向标准输出
```python
from contextlib import redirect_stdout

with open("log.txt", "w") as f:
    with redirect_stdout(f):
        print("这句话会写入文件，而不是控制台")
```
