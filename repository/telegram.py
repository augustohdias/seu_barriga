import os
import requests

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']
SERVER_URL = 'https://api.telegram.org/bot<token>/<method>'.replace('<token>', BOT_TOKEN)

def send_message(message):
    api_call = SERVER_URL.replace('<method>', 'sendMessage?chat_id=' + CHAT_ID + '&parse_mode=Markdown&text=' + message)
    print('[DEBUG] Sending message >' + message + '< to ' + CHAT_ID)
    response = requests.get(api_call)
    return response.json()

def get_updates(offset):
    api_call = SERVER_URL.replace('<method>', 'getUpdates?offset=' + offset)
    print('[DEBUG] Requesting updates.')
    response = requests.get(api_call)
    print('[DEBUG] Response ok? ' + response.json()['ok'])
    return response.json()['result'] if response.json()['ok'] else []
