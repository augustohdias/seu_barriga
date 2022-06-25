import os
from datetime import date
from bot.beahviour import BehaviourInterface

class SeuBarriga(BehaviourInterface):
    __dir_path = os.path.dirname(os.path.realpath(__file__))
    __billing_day = 27
    __api = None
    
    def __init__(self, billing_day, api):
        self.__billing_day = billing_day
        self.__api = api
        
    def __aluguel(self, message={}):
        today = date.today()
        days_to_payment = str(self.__billing_day - int(today.strftime('%d')))
        billing_date = str(self.__billing_day) + today.strftime('/%m/%Y')
        return self.__api.send_message(f'Vou cobrar o aluguel em {days_to_payment} dias ({billing_date}).')

    def __pix(self, message={}):
        return self.__api.send_private_message('', 0)

    def __padrao(self, message={}):
        return self.__api.send_message('**Pague o aluguel!**')

    def __ajuda(self, message={}):
        ajuda = open(f'{self.__dir_path}/messages/ajuda.md', 'r').read()
        return self.__api.send_message(ajuda)

    __COMMANDS = {
        'aluguel': __aluguel,
        'pix': __pix,
        'ajuda': __ajuda
    }
    
    def valid_commands(self):
        return self.__COMMANDS.keys()
    
    def perform(self, command, message={}):
        if command in self.valid_commands():
            print(command)
            return ('ok', self.__COMMANDS.get(command, self.__padrao)(self, message=message))
        return ('error', None)
