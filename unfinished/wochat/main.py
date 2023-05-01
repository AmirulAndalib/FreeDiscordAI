import requests

cookies = {
    'XSRF-TOKEN': 'eyJpdiI6IjdhRHRXZHNXR0FEaUQxMXhlME4zZnc9PSIsInZhbHVlIjoidGZZSXJTTWdFa015emZCcUtCM3ZkMkRyMGNva3NKL1Q1YStUK0NtYTdlQ0c3Q0pwbmJIM2M4Q2pjTFJyMDNodnFxanQvMzBCa3ZIcEZnV2VNbmhPeUw1TFo2amtaSStMMmJUR01aQ25aaDhpMXB1Nkh3TVNwVXdvZTZMZkp4SjIiLCJtYWMiOiJkODM0YjYyMmYzNmVkMGZiMTg5MmJiNzVlNzI0YjllODgzZDE2MzI2MDhlNjJiN2VlOTY5Njg5NWIyNmViYzE4IiwidGFnIjoiIn0%3D',
    'wochat_session': 'eyJpdiI6Ik84cVFFTDVyWE1FdVlmVnkydXBZeXc9PSIsInZhbHVlIjoiNUY3M0p0VTV4b2FWK0FuMlRiQjVScHIrMnhZck11MDNZSnNaY0FtQUNnQms5aFo3ZCsvdXlNSUxtVEY0ZEFyNDlpL01aQjMyZHlDb0xnUWRiY1ZGbVlPUkoveWdSMDJWV3lRdUZ4dzVaWlVLZXdGZUNwRjFobXlPbUdFcnN6emIiLCJtYWMiOiJmMzgzNmIxN2U5MDJjMDc0ZjkwMzM3MjgyYWEwMTNhY2U2NGU1MDU2ZDJmMDBkNTkzMGQ4MDk1YmJjMjdiN2FmIiwidGFnIjoiIn0%3D',
}

headers = {
    'authority': 'chat.wobcw.com',
    'accept': 'text/event-stream',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'referer': 'https://chat.wobcw.com/',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

params = {
    'chat_id': 'bef55c20-617d-4f45-8722-81173e8d7339',
    'api_key': '',
}

response = requests.get('https://chat.wobcw.com/stream', params=params, cookies=cookies, headers=headers)