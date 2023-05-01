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
    }

    response = requests.post('https://chatgpt.skybyte.me/api/chat-process', headers=headers, json=json_data)
    last_line = response.text.splitlines()[-1]

    e = re.findall('"([^"]*)"', last_line)
    e[9] = e[9].replace("\\n", " ")
    return e[9]

