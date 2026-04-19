读取环境变量：`os.getenv('VAR_NAME',default='xxx')`。
读取`.env`文件：`python-dotenv`包，`load_dotenv`方法将`.env`变量加载进环境变量，再使用`os`包读取。
推荐方案：`Pydantic Settings`，理由：自动加载`.env`文件，类型校验。
