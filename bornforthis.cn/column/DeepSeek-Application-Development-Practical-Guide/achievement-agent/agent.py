import json
from llm import client
from prompt import REACT_PROMPT
from tools import get_score_by_name,generating_performance_reviews,tools
import re

def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-v3",
        messages=messages,
    )
    return response

if __name__ == "__main__":
    instructions = "你是一个员工绩效评价系统"

    query = "李四是个好同志，工作态度端正，请帮我给他写一段绩效评语"
    #query = "张三和李四的绩效谁好？"
    
    prompt = REACT_PROMPT.replace("{tools}", json.dumps(tools)).replace("{input}", query)
    messages = [{"role": "user", "content": prompt}]

    while True:
        response = send_messages(messages)
        response_text = response.choices[0].message.content

        print("大模型的回复：")
        print(response_text)

        final_answer_match = re.search(r'Final Answer:\s*(.*)', response_text)
        if final_answer_match:
            final_answer = final_answer_match.group(1)
            print("最终答案:", final_answer)
            break

        messages.append(response.choices[0].message)

        action_match = re.search(r'Action:\s*(\w+)', response_text)
        action_input_match = re.search(r'Action Input:\s*({.*?}|".*?")', response_text, re.DOTALL)

        if action_match and action_input_match:
            tool_name = action_match.group(1)
            params = json.loads(action_input_match.group(1))

            observation = ""
            if tool_name == "get_score_by_name":
                observation = get_score_by_name(params['name'])
                print("人类的回复：Observation:", observation)         
            elif tool_name == "generating_performance_reviews":
                observation = generating_performance_reviews(params['estimation'])
                print("人类的回复：Observation:", observation)

            messages.append({"role": "user", "content": f"Observation: {observation}"})
