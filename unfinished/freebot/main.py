import requests

import re
def ask(question):
    headers = {
        'authority': 'api.gptplus.one',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'http://chat.freebot.one',
        'referer': 'http://chat.freebot.one/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    json_data = {
        'prompt': 'whats your name?',
        'options': {},
        'systemMessage': "You are ChatGPT, the version is GPT3.5, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
        'temperature': 0.8,
        'top_p': 1,
        'secret': 'U2FsdGVkX19AtXtTE/ugQDXZRAb3C85Uc8SjUKRBH4U=', # need to get secret
    }

    response = requests.post('http://api.gptplus.one/chat-process', headers=headers, json=json_data)
    print(response.text)

    with open("temp.txt", 'w') as f:
        f.write(response.text)
    
    with open('temp.txt', 'r') as f:
        last_line = f.readlines()[-1]

    e = re.findall('"([^"]*)"', last_line)

    for i in e:
        print(i)

    return e

