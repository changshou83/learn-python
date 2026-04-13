**数据类（Data Class）** 是 Python 3.7+ 自带的**专门用来存数据的类**，专门解决：**普通类写一堆样板代码（`__init__`、`__repr__`、`__eq__`）太麻烦**的问题。

## 一、普通类 vs 数据类
### 1. 普通类
```python
# 普通类：必须手写 __init__、__repr__...
class Person:
    def __init__(self, name: str, age: int, city: str = "北京"):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r}, city={self.city!r})"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return (self.name, self.age, self.city) == (other.name, other.age, other.city)
```

### 2. 数据类
```python
from dataclasses import dataclass

@dataclass  # 核心装饰器
class Person:
    name: str       # 类型注解 + 字段定义
    age: int
    city: str = "北京"  # 默认值
```


## 二、数据类核心功能
`@dataclass` **自动生成**这些方法，不用手写：
1. `__init__`：构造函数
2. `__repr__`：打印对象友好显示（不是内存地址）
3. `__eq__`：支持 `==` 比较（按字段值）
4. `__lt__`/`__le__`/`__gt__`/`__ge__`：排序比较（可选）

### 直接使用
```python
p1 = Person("张三", 20)
p2 = Person("李四", 25, "上海")
p3 = Person("张三", 20)

print(p1)        # Person(name='张三', age=20, city='北京')
print(p1 == p3)  # True（自动按值比较）
```


## 三、常用高级用法
### 1. 不可变数据类（只读）
```python
@dataclass(frozen=True)  # frozen=True = 不可修改
class Person:
    name: str
    age: int

p = Person("张三", 20)
# p.age = 21  # 报错：FrozenInstanceError
```

### 2. 支持排序（按字段排序）
```python
@dataclass(order=True)  # order=True = 支持排序
class Student:
    score: int  # 排序依据：写在前面的字段优先
    name: str

s1 = Student(90, "张三")
s2 = Student(80, "李四")
print(s1 > s2)  # True
```

### 3. 转字典 / 元组
```python
from dataclasses import asdict, astuple

p = Person("张三", 20)
print(asdict(p))  # {'name': '张三', 'age': 20, 'city': '北京'}
print(astuple(p)) # ('张三', 20, '北京')
```

### 4. 字段默认值（可变类型）
**注意**：列表/字典等可变类型，不能直接写默认值，要用 `field(default_factory=...)`
```python
from dataclasses import dataclass, field

@dataclass
class ClassRoom:
    name: str
    students: list[str] = field(default_factory=list)  # 正确写法
```


## 四、数据类 vs 普通字典
| 方式 | 优点 | 缺点 |
|------|------|------|
| 字典 | 简单、无需定义结构 | 无类型提示、容易写错键 |
| **数据类** | **类型安全、自动补全、代码清晰** | 需要提前定义结构 |

**开发首选数据类**：接口参数、返回值、配置项、数据载体。

