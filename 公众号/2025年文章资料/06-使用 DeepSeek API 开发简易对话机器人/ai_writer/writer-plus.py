# writer.py

from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL
import datetime
import threading
import time
import sys

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

styles = {
    "1": "日常风格",
    "2": "科幻风格",
    "3": "技术说明风格"
}

def get_style_prompt(style_choice):
    if style_choice == "1":
        return "请用日常生活化的语气续写下文："
    elif style_choice == "2":
        return "请用科幻小说风格续写下文："
    elif style_choice == "3":
        return "请用专业技术文档风格续写下文："
    else:
        return "请续写下文："

def show_loading(stop_event):
    i = 0
    dots = ['.', '..', '...', '....']
    while not stop_event.is_set():
        sys.stdout.write('\r⏳ AI 正在写作中' + dots[i % len(dots)])
        sys.stdout.flush()
        i += 1
        time.sleep(0.5)
    sys.stdout.write('\r' + ' ' * 40 + '\r')  # 清空行

def generate_writing(style_prompt, user_input):
    messages = [
        {"role": "system", "content": "你是一个专业写作助手，擅长多种文风写作。"},
        {"role": "user", "content": f"{style_prompt}\n\n{user_input}"}
    ]

    stop_event = threading.Event()
    t = threading.Thread(target=show_loading, args=(stop_event,))
    t.start()

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=False
    )

    stop_event.set()
    t.join()

    return response.choices[0].message.content.strip()

def save_output(content):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{timestamp}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ 写作内容已保存至：{filename}")

def main():
    print("✍️ AI 写作助手启动")
    print("请选择写作风格：")
    for k, v in styles.items():
        print(f"{k}. {v}")

    style_choice = input("请输入数字选择风格：").strip()
    user_input = input("请输入你想写的主题或段落开头：\n").strip()

    style_prompt = get_style_prompt(style_choice)
    result = generate_writing(style_prompt, user_input)

    print("\n📝 生成内容：\n")
    print(result)

    save_output(result)

if __name__ == "__main__":
    main()
