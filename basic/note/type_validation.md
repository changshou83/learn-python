Python 是动态类型语言，变量不需要提前声明类型，但这会导致代码可读性差、IDE 无法智能提示、容易出现类型错误。
类型提示（Type Hints） 是 Python 3.5+ 引入的语法，用来标注变量、函数参数、返回值的类型，不影响代码运行，只做提示和校验。Python 3.9+ 可以直接用原生类型，不需要导入 typing 模块。

## 类型提示

语法：
```python
# 基础类型
name: str = 'changshou83'
age: int = 23
height: float = 1.75
is_student: bool = False
target: bytes = bytes('live', 'utf-8')
girl_friend: None = None

# 容器类型
pets: list[str] = ['tortoise', 'fish']
user: dict[str, int | str] = {"name": "ming", "age": 18}
s: set[int] = {1,2,3}
point: tuple[int, int] = (10,10)

# 函数类型
def add(a: int, b: int) -> int:
    return a = b

def print_info(msg: str) -> None:
    print(msg)

# 类类型
class Product:
    def __init__(self, name: str, price: float):
        self.name: str = name
        self.price: float = price

class Node:
    def __init__(self, value: int, next: "Node | None" = None):
        self.value: int = value
        self.next: Node | None = next

# 高级类型
# 可选类型
name: str | None = None
# 多选类型
data: str | int | bool = ''
from typing import Any, Callable
# 任意类型
value: Any = ''
# 函数类型
def execute(func: Callback[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
```

## 自定义类型

1. 类
2. 类型别名（相当于TS的type，鸭子类型）：`UserInfo: TypeAlias = dict[str, str | int | None]`
3. 新类型（类型符号，相当于JS的Symbol）：`UserId = NewType("UserId", int)`
4. 泛型：定义泛型，`T = TypeVar("T")`；使用泛型，`Callback[[T,T],T]`

## 元数据注解

Annotated = 类型 + 元数据（附加信息，例如备注，规则等）。语法：`Annotated[原始类型, 元数据1, 元数据2, ...]`。

## 类型校验方案：Pydantic

Pydantic 的核心是 `BaseModel`，自带：类型校验，自动类型转换，错误提示，IDE 智能提示。支持常见数据类型转换，例如类转字典或JSON字符串，以及从字典和JSON字符串加载类数据。

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    street: str

class User(BaseModel):
    name: str
    age: int
    email: str | None = None  # 可选类型
    address: Address | None = None  # 嵌套自定义类型

user1 = User(name="张三", age=20)
print(user1.name)

# 强制校验类型
user2 = User(name="张三", age="20")  # 会自动转 int
user3 = User(name="张三", age="abc") # 直接抛 ValidationError

# 常见数据类型转换
d = user1.model_dump()  # 转字典
j = user1.model_dump_json()  # 转JSON字符串
translated = User(**d) # 从字典/JSON字符串加载模型
```

还可以使用 `Annotated` 创造类型约束，例如：`Age = Annotated[int, Field(ge=16, le=22)]`。
