Python 推导式（Comprehension）就是一行代码快速生成列表 / 字典 / 集合 / 生成器的简洁写法，比循环更短、更 Pythonic。

```python
# 列表推导式:[表达式 for 变量 in 可迭代对象 if 条件]
nums = [x for x in range(10)] # [0,1,2,...,9]
evens = [x for x in range(10) if x%2==0] # 偶数
squares = [x**2 for x in range(5)] # 平方
# 字典推导式:{键:值 for 变量 in 可迭代对象 if 条件}
d = {x: x**2 for x in range(5)} # {0:0,1:1,2:4,3:9,4:16}
# 集合推导式:{表达式 for 变量 in 可迭代对象 if 条件}
s = {x % 3 for x in range(10)} # {0,1,2}
# 生成器推导式:用 () 包裹，不一次性生成全部，适合大数据
g = (x for x in range(1000000))
```
