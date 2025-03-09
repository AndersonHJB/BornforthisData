import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AliDeep"),  
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def send_messages(messages):
    response = client.chat.completions.create(
        model="qwen-max",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    return response

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_closing_price",
            "description": "使用该工具获取指定股票的收盘价",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "股票名称",
                    }
                },
                "required": ["name"]
            },
        }
    },
]

def get_closing_price(name):
    if name == "青岛啤酒":
        return "67.92"
    elif name == "贵州茅台":
        return "1488.21"
    else:
        return "未搜到该股票"

if __name__ == "__main__":
    messages = [{"role": "user", "content": "青岛啤酒的收盘价是多少？"}]
    response = send_messages(messages)

    messages.append(response.choices[0].message)

    print("回复：")
    print(response.choices[0].message.content)

    print("工具选择：")
    print(response.choices[0].message.tool_calls)

    if response.choices[0].message.tool_calls != None:
        tool_call = response.choices[0].message.tool_calls[0]
        
        if tool_call.function.name == "get_closing_price":
            arguments_dict = json.loads(tool_call.function.arguments)
            price = get_closing_price(arguments_dict['name'])

            messages.append({
                "role": "tool",
                "content": price,
                "tool_call_id": tool_call.id
            })

    print("messages: ",messages)

    response = send_messages(messages)

    print("回复：")
    print(response.choices[0].message.content)