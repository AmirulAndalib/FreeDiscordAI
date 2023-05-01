import requests
import fake_useragent
import re

def ask(question):

    ua = fake_useragent.UserAgent(browsers=['chrome', "firefox", "opera", "safari", "edge", "internet explorer"])


    headers = {
        'authority': 'komo.ai',
        'accept': 'text/event-stream',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'referer': 'https://komo.ai/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': ua.random,
    }

    params = {
        'query': f'Q: {question}\nA:',
        'FLAG_URLEXTRACT': 'false',
        'token': 'need to figure out how to generate',
    }



    response = requests.get('https://komo.ai/api/ask', params=params, headers=headers)

    def remove_text_inside_brackets(text, brackets="()[]{}"):
        count = [0] * (len(brackets) // 2) # count open/close brackets
        saved_chars = []
        for character in text:
            for i, b in enumerate(brackets):
                if character == b: # found bracket
                    kind, is_close = divmod(i, 2)
                    count[kind] += (-1)**is_close # `+1`: open, `-1`: close
                    if count[kind] < 0: # unbalanced bracket
                        count[kind] = 0  # keep it
                    else:  # found bracket to remove
                        break
            else: # character is not a [balanced] bracket
                if not any(count): # outside brackets
                    saved_chars.append(character)
        x = ''.join(saved_chars)
        x = x.replace("event: meta","")
        x = x.replace("event: line","")
        x = x.replace("data:","")
        x = x.replace("event:  ","")

        return x

    resp = []
    quoted = re.compile('"[^"]*"')
    for value in quoted.findall(remove_text_inside_brackets(response.text)):
        value = value.replace('"',"")
        resp.append(value)


    string = ''.join(str(e)for e in resp)
    return string
