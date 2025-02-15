import requests
import datetime
import json
import art

# Function to search for city adcode with precise and fuzzy matching
def search_city_adcode(city_name):
    # Load the JSON data from the file we saved earlier
    with open('./AMap_adcode_citycode.json', 'r', encoding='utf-8') as file:
        city_data = json.load(file)
    # Precise matching
    precise_matches = [entry for entry in city_data if entry['中文名'] == city_name]
    if precise_matches:
        return precise_matches[0]['adcode']

    # Fuzzy matching
    fuzzy_matches = [entry for entry in city_data if city_name in entry['中文名']]
    # Limit to top 6 closest matches based on the length of the city name in the entries
    fuzzy_matches_sorted = sorted(fuzzy_matches, key=lambda x: abs(len(x['中文名']) - len(city_name)))
    top_fuzzy_matches = fuzzy_matches_sorted[:6]

    return {entry['中文名']: entry['adcode'] for entry in top_fuzzy_matches}


def format_weather_report(weather_data):
    report = (
        f"省份：{weather_data['province']}\n"
        f"城市：{weather_data['city']}\n"
        f"地区代码：{weather_data['adcode']}\n"
        f"天气：{weather_data['weather']}\n"
        f"温度：{weather_data['temperature']}°C\n"
        f"风向：{weather_data['winddirection']}\n"
        f"风力：{weather_data['windpower']}\n"
        f"湿度：{weather_data['humidity']}%\n"
        f"报告时间：{weather_data['reporttime']}"
    )
    return report


def weather_api(city, key='ca24c25049bc8299bfc8add6f921672b'):
    """
    My Key: ca24c25049bc8299bfc8add6f921672b
    Docs: https://lbs.amap.com/api/webservice/guide/api/weatherinfo
    """
    # if isinstance(city_data, dict):
    #     city_data =
    url = "https://restapi.amap.com/v3/weather/weatherInfo?city={city}&key={key}".format(city=city, key=key)
    # print(url)
    html = requests.get(url).json()
    # print(*html['lives'])
    # print(len(html['lives']))
    return html['lives'][0]


def get_user_text():
    text = input('请输入的城市:>>>')
    city_data = search_city_adcode(text)
    print(city_data)
    # city_id = '110000'
    if isinstance(city_data, dict):
        city_id = input('请输入查询到的城市 ID:')
    else:
        city_id = city_data
        print(f'查询到城市{text}的 ID 为: {city_id}')
    return city_id


def chatbot_response(message):
    message = message.lower()
    if "hello" in message or "hi" in message or "你好" in message:
        return "Hello! How can I help you today?"
    elif "time" in message or "时间" in message:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."
    elif "date" in message or "日期" in message:
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}."
    elif "weather" in message or "天气" in message:
        # return "I'm not able to fetch real-time data yet, but it looks like a nice day!"
        city_id = get_user_text()
        data_dict = weather_api(city_id)
        return format_weather_report(data_dict)
    elif 'art' in message:
        print(art.text2art(message.replace('art', '')))
    else:
        return "I'm sorry, I didn't understand that. Can you try asking something else?"


def main():
    print("Welcome to ChatBot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")


if __name__ == '__main__':
    main()
