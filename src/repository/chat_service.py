from abc import ABC, abstractmethod

class ChatServiceInterface(ABC):
    @abstractmethod
    def send_message(self, message):
        pass
    
    @abstractmethod
    def send_private_message(self, message, user_id):
        pass

    @abstractmethod
    def reply_message(self, message, reply_to_id):
        pass