FastAPI CLI 是官方提供的命令行工具，底层基于 Uvicorn，专为简化 开发运行、生产部署、配置管理 而生。

## 基础使用

### 开发模式

命令：`fastapi dev`或者`fastapi dev main.py`，推荐：`fastapi dev`，入口在配置文件里指定。

有热重载和自动文档。

参数：

```plaintext
Usage: fastapi dev [OPTIONS] FILE

Run a FastAPI app in development mode (with auto-reload).

Arguments:
  FILE    入口文件/模块路径  [required]

Options:
  --app TEXT                FastAPI 实例名 (默认: app)
  --app-dir DIR             添加到 sys.path
  --host TEXT               监听地址 (默认: 127.0.0.1)
  --port INTEGER            端口 (默认: 8000)
  --uds TEXT                绑定到 UNIX 套接字
  --fd INTEGER              绑定到文件描述符
  --log-level TEXT          日志级别
  --root-path TEXT          ASGI root_path
  --proxy-headers           启用代理头
  --help                    帮助

  --reload                  启用热重载 [默认开启]
  --reload-dir PATH         重载目录
  --reload-include TEXT     包含文件
  --reload-exclude TEXT     排除文件
  --reload-delay FLOAT      重载延迟 (默认: 0.25)
```

### 生产模式

命令：`fastapi run`或者`fastapi run main.py`，推荐：`fastapi run main.py --workers 4 --proxy-headers`，入口在配置文件里指定。

适合容器，服务器部署。

参数：

```plaintext
Usage: fastapi run [OPTIONS] FILE

Run a FastAPI app in production mode.

Arguments:
  FILE    入口文件/模块路径  [required]

Options:
  --app TEXT                FastAPI 实例名 (默认: app)
  --app-dir DIR             添加到 sys.path
  --host TEXT               监听地址 (默认: 0.0.0.0)
  --port INTEGER            端口 (默认: 8000)
  --uds TEXT                绑定到 UNIX 套接字
  --fd INTEGER              绑定到文件描述符
  --log-level TEXT          日志级别
  --root-path TEXT          ASGI root_path
  --proxy-headers           启用代理头
  --help                    帮助

  --workers INTEGER         工作进程数 (默认: 1)
```

## 进阶使用

1. 在`pyproject.toml`中配置应用位置：例如`[tool.fastapi]\nentrypoint = "main:app"`，其中main是模块名，app是fastapi实例对象名，例如可以改成`backend.main:api`，等价于`from backend.main import api`。
