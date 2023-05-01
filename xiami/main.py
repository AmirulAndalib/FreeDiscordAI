import requests
import re
import fake_useragent

ua = fake_useragent.UserAgent(browsers=['chrome', "firefox", "opera", "safari", "edge", "internet explorer"])

def ask(question):
    headers = {
        'user-agent': ua.random
    }

    json_data = {
        'prompt': question,
        'options': {},
        'systemMessage': "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
        'temperature': 0.8,
        'top_p': 1,
    }



    response = requests.post('https://smart-chat.xiami.one/api/chat-process', headers=headers, json=json_data)
    last_line = response.text.splitlines()[-1]

    e = re.findall('"([^"]*)"', last_line)
    e[7] = e[7].replace("\\n", " ")
    return e[7]
