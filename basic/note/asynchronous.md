异步编程是 Python 处理高并发、IO 密集型任务（网络请求、文件读写、数据库操作）的核心技术。
使用官方库`asyncio`以及`async/await`关键字实现异步编程。

```python
import asyncio

# 1. 定义异步任务
async def do_something():
    await asyncio.sleep(1)
    return "完成"

# 2. 主函数
async def main():
    results = await do_something()
    print(results)

# 3. 运行
asyncio.run(main())
```

## 并发

用 asyncio.gather()。

```python
import asyncio
import time

# 定义异步函数
async def task(name, delay):
    print(f"任务 {name} 开始，等待 {delay}s")
    # 异步等待（不会阻塞整个程序）
    await asyncio.sleep(delay)
    print(f"任务 {name} 完成")

async def main():
    # 创建多个异步任务
    t1 = task("A", 2)
    t2 = task("B", 1)

    # 并发执行
    await asyncio.gather(t1, t2)

if __name__ == "__main__":
    start = time.time()
    # 运行异步主函数
    asyncio.run(main())
    print(f"总耗时：{time.time() - start:.2f}s")

'''
任务 A 开始，等待 2s
任务 B 开始，等待 1s
任务 B 完成
任务 A 完成
总耗时：2.01s
'''
```

## 网络请求

用 aiohttp，不能用 requests。

```python
import asyncio
import aiohttp  # 异步HTTP库（必须用异步请求，否则没效果）

async def fetch_url(session, url):
    async with session.get(url) as resp:
        print(f"请求 {url} 状态：{resp.status}")
        return await resp.text()

async def main():
    urls = [
        "https://www.baidu.com",
        "https://www.bing.com",
        "https://github.com"
    ]

    # 创建异步会话
    async with aiohttp.ClientSession() as session:
        # 批量创建任务
        tasks = [fetch_url(session, url) for url in urls]
        # 并发执行
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
```

## 多线程缺点

Python 有 GIL（全局解释器锁），同一时刻只有一个线程在真正执行。遇到 IO 等待才切换，效率一般。线程多了之后，切换开销大，容易混乱。
