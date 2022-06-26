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
        send_message_url = f'{self.__SERVER_URL}bot{self.__bot_token}/sendMessage?chat_id={self.__chat_id}&parse_mode=Markdown&text={message}'
        print(send_message_url)
        return requests.get(send_message_url).json()
    
    def send_private_message(self, message, user_id):
        send_private_message_url = f'{self.__SERVER_URL}bot{self.__bot_token}/sendMessage?chat_id={user_id}&parse_mode=Markdown&text={message}'
        print(send_private_message_url)
        return requests.get(send_private_message_url).json()

    def reply_message(self, message, reply_to_id):
        send_message_url = f'{self.__SERVER_URL}bot{self.__bot_token}/sendMessage?chat_id={self.__chat_id}&parse_mode=Markdown&text={message}&reply_to_message_id={reply_to_id}'
        print(send_message_url)
        return requests.get(send_message_url).json()