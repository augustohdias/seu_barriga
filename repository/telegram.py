import os, requests
from repository.chat_service import ChatServiceInterface

class TelegramAPI(ChatServiceInterface):
    __SERVER_URL = 'https://api.telegram.org/'
    __chat_id = ''
    __bot_token = ''
    
    def __init__(self):
        self.__chat_id = os.getenv('CHAT_ID', '')
        self.__bot_token = os.getenv('BOT_TOKEN', '')
    
    def send_message(self, message):
        send_message_url = ''.join([self.__SERVER_URL, 'bot', self.__bot_token, '/sendMessage?chat_id=', self.__chat_id, '&text=', message])
        print(send_message_url)
        response = requests.get(send_message_url)
        return response.json()
    
    def send_private_message(self, message, user_id):
        return super().send_private_message(message, user_id)
