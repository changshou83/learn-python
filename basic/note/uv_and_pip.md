# pip
`pip` 是 Python **官方自带的包安装工具**。作用：安装、卸载、管理第三方库（requests、flask、pandas 等）。

## 常用命令
1. 安装包：`pip install <package-name>==<version>`，不指定版本，默认安装最新版本
2. 卸载包：`pip uninstall <package-name>`
3. 查看已安装包：`pip list`
4. 查看某个包信息：`pip show <package-name>`
5. 导出依赖（给别人复制环境用）：`pip freeze > requirements.txt`
6. 从文件安装环境：`pip install -r requirements.txt`
7. 升级包：`pip install --upgrade pip`
8. 安装本地开发包：`pip install .`

## pip 的痛点
- **慢**（依赖解析慢、下载慢）
- 没有**锁文件**，环境无法精准复现
- 不会自动创建**虚拟环境**
- 依赖冲突容易炸

# uv
uv 是用 Rust 写的、速度极快、兼容 pip 与 pyproject.toml、自带虚拟环境和 Python 版本管理的现代 Python 包与项目管理工具。

## 常用命令
使用：
1. 创建项目：`uv init <project-name>`，自动创建虚拟环境
2. 安装依赖：`uv add <package-name>==<version>`，自动加入配置文件中
3. 安装开发依赖：`uv add --dev <package-name>`
4. 安装项目所有依赖：`uv sync`
5. 卸载依赖：`uv remove <package-name>`
6. 运行脚本：`uv run <script-name>`，自动应用虚拟环境
7. 手动进入虚拟环境：`uv shell`

## uv 独有功能

1. 安装指定 Python 版本：`uv python install 3.12`
2. 全局安装工具（替代 pipx）：`uv tool install jupyterlab`
3. 极速打包发布：打包`uv build`和发布`uv publish`
