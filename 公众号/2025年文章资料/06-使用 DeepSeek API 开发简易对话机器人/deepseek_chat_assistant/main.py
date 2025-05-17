# main.py

from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL

# 初始化客户端
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 初始上下文
messages = [
    {"role": "system", "content": "你是一个乐于助人的中文 AI 助手。"}
]

def chat():
    print("🤖 DeepSeek 聊天助手已启动（输入 exit 退出）")
    while True:
        user_input = input("🧑 你：")
        if user_input.lower() in ["exit", "退出", "bye"]:
            print("👋 再见！")
            break

        # 添加用户输入
        messages.append({"role": "user", "content": user_input})

        try:
            # 生成回复
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                stream=False
            )
            reply = response.choices[0].message.content.strip()

            # 打印助手回复
            print("🤖 助手：" + reply)

            # 添加助手回复
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"❌ 出错了: {e}")
            break

if __name__ == "__main__":
    chat()