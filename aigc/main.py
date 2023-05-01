import requests
import fake_useragent

ua = fake_useragent.UserAgent(browsers=['chrome', "firefox", "opera", "safari", "edge", "internet explorer"])

def ask(question):
    headers = {
        'path': '/v1/chat/completions',
        'user-agent': ua.random,
    }

    json_data = {
        'messages': [
            {
                'role': 'user',
                'content': question,
            },
        ],
        'stream': True,
        'model': 'gpt-3.5-turbo',
        'temperature': .9,
        'presence_penalty': 0,
    }

    response = requests.post('https://c.aigc.it/api/chat-stream', headers=headers, json=json_data)
    
    return response.text
