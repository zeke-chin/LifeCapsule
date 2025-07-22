import os
from dotenv import load_dotenv

# 从 .env 文件加载环境变量
# 这行代码会查找当前目录或上级目录中的 .env 文件
load_dotenv()


class Config:
    """
    全局配置类
    从 .env 文件加载环境变量。
    """

    # OpenAI 配置
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    # 基础模型配置
    BASE_MODEL: str = os.getenv("BASE_MODEL")
    BASE_VLM_MODEL: str = os.getenv("BASE_VLM_MODEL")


# 创建一个 Config 类的全局实例，方便其他模块导入使用
config = Config()
