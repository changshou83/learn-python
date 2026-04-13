# 现代Python开发的最佳实践

虚拟环境和标准配置文件，统一管理依赖，构建和工具配置。

## 虚拟环境

虚拟环境和核心作用是为每个项目创建独立、隔离的Python运行环境，防止不同项目的不同版本的依赖包相互冲突。
官方工具：venv（Python 3.3+内置）。
常用命令：

```bash
# 创建虚拟环境(项目根目录执行，推荐命名为 .venv)
python -m venv .venv

# 激活虚拟环境
.venv\Scripts\activate.bat
.venv\Scripts\Activate.ps1
source .venv/bin/activate

# 在当前虚拟环境中安装依赖
pip install requests flask

# 退出环境
deactivate

# 删除环境
rm -rf .venv
rmdir /s .venv
```

## pyproject.toml

PEP 518 & 621 定义的统一配置文件（替代 requirements.txt、setup.py 等），集中管理：
1. 项目元数据（名称、版本、作者）
2. 运行依赖 / 开发依赖
3. 构建系统（打包、发布）
4. 第三方工具配置（pytest, fastapi 等）

标准配置文件示例：
```toml
# ----------------------
# 1. 构建系统配置 (必填)
# ----------------------
[build-system]
requires = ["setuptools>=61.0", "wheel"]  # 构建所需工具
build-backend = "setuptools.build_meta"   # 构建后端

# ----------------------
# 2. 项目元数据与依赖 (PEP 621 标准)
# ----------------------
[project]
name = "my-awesome-project"
version = "0.1.0"
description = "一个用 pyproject.toml 管理的项目"
readme = "README.md"
requires-python = ">=3.8"  # 支持的Python版本
authors = [
    { name="John Doe", email="john@example.com" }
]

# 项目运行依赖
dependencies = [
    "requests>=2.31.0",
    "flask~=2.3.0"  # ~= 表示兼容版本
]

# 可选/开发依赖（分组管理）
[project.optional-dependencies]
dev = [
    "pytest>=7.0",    # 测试
]

# ----------------------
# 3. 第三方工具配置
# ----------------------
[tool.pytest.ini_options]
testpaths = ["tests"]
```

安装依赖：安装运行依赖`pip install`,安装开发依赖`pip install .[dev]`。

## 推荐工具：uv

理由：自动管理虚拟环境+`pyproject.toml`+`lock`文件锁定依赖。

使用：
1. 创建项目：`uv init <project-name>`，自动创建虚拟环境
2. 安装依赖：`uv add <package-name>`，自动加入配置文件中
3. 安装开发依赖：`uv add --dev <package-name>`
4. 安装项目所有依赖：`uv sync`（新项目），`uv pip install -r requirements.txt`（兼容旧项目）
5. 卸载依赖：`uv remove <package-name>`
6. 运行脚本：`uv run <script-name>`
7. 激活虚拟环境：`uv shell`
8. 导出 `requirements.txt`（兼容老项目）：`uv pip compile pyproject.toml -o requirements.txt`

对比 `poetry`:
1. uv安装依赖速度快一到两个数量级
2. 原生支持多版本`python`，命令`uv python install`
