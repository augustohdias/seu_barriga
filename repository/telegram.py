import os
import requests

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']
SERVER_URL = 'https://api.telegram.org/bot<token>/<method>'.replace('<token>', BOT_TOKEN)

def send_message(message):
    api_call = SERVER_URL.replace('<method>', 'sendMessage?chat_id=' + CHAT_ID + '&parse_mode=Markdown&text=' + message)
    response = requests.get(api_call)
    return response.json()

def get_updates(offset):
    api_call = SERVER_URL.replace('<method>', 'getUpdates?allowed_updates=["message"]&offset=' + offset)
    response = requests.get(api_call)
    return response.json()['result'] if response.json()['ok'] else []