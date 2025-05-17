# main.py

from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL
import threading
import time
import sys

# 初始化客户端
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 初始上下文
messages = [
    {"role": "system", "content": "你是一个乐于助人的中文 AI 助手。"}
]

def show_loading(stop_event):
    i = 0
    loading_chars = ['.', '..', '...', '....']
    while not stop_event.is_set():
        sys.stdout.write('\r🤖 助手正在思考中' + loading_chars[i % len(loading_chars)])
        sys.stdout.flush()
        i += 1
        time.sleep(0.5)
    sys.stdout.write('\r' + ' ' * 40 + '\r')  # 清空行

def chat():
    print("🤖 DeepSeek 聊天助手已启动（输入 exit 退出）")
    while True:
        user_input = input("🧑 你：")
        if user_input.lower() in ["exit", "退出", "bye"]:
            print("👋 再见！")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            stop_event = threading.Event()
            loading_thread = threading.Thread(target=show_loading, args=(stop_event,))
            loading_thread.start()

            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                stream=False
            )

            stop_event.set()
            loading_thread.join()

            reply = response.choices[0].message.content.strip()
            print("🤖 助手：" + reply)

            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            stop_event.set()
            loading_thread.join()
            print(f"\n❌ 出错了: {e}")
            break

if __name__ == "__main__":
    chat()
