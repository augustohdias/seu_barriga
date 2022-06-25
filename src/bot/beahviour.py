from abc import ABC, abstractmethod

class BehaviourInterface(ABC):
    @abstractmethod
    def valid_commands(self):
        pass
    
    @abstractmethod
    def perform(self, command, message={}):
        pass