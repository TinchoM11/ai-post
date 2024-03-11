import os
from dotenv import load_dotenv

load_dotenv()

llm_config = {"config_list": [
    {"model": "gpt-4",
        "api_key": os.environ.get("OPENAI_API_KEY"), "temperature": 0.9},
]}
