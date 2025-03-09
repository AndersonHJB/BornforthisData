import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AliDeep"),  
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)