import os, time
from bot.markdown import read_md_template
from datetime import date, datetime

class SeuBarriga:
    __dir_path = os.path.dirname(os.path.realpath(__file__))
    __billing_day = 27
    __api = None
    
    def __init__(self, billing_day, api):
        self.__billing_day = billing_day
        self.__api = api
    
    def task(self):
        pix = os.getenv('PIX', 'chavepixdementirinha')
        cobranca_msg = read_md_template(self.__dir_path, 'cobranca', params={'pix': pix})
        day = 23 * 3600
        while True:
            if datetime.now().day == 27 and datetime.now().hour == 10:
                self.__api.send_message(cobranca_msg)
                time.sleep(day)
        
    def __aluguel(self, message={}):
        today = date.today()
        days_to_payment = str(self.__billing_day - int(today.strftime('%d')))
        billing_date = str(self.__billing_day) + today.strftime('/%m/%Y')
        return self.__api.send_message(f'Vou cobrar o aluguel em {days_to_payment} dias ({billing_date}).')

    def __pix(self, message={}):
        pix = os.getenv('PIX', 'chavepixdementirinha')
        message_id = message['message_id']
        user = message['from']['username']
        user_id = message['from']['id']
        
        pix_msg = read_md_template(self.__dir_path, 'pix', params={'user': user, 'pix': pix, 'user_id': str(user_id)})
        
        return self.__api.reply_message(pix_msg, message_id)

    def __padrao(self, message={}):
        return self.__api.send_message('**Pague o aluguel!**')

    def __ajuda(self, message={}):
        ajuda_msg = read_md_template(self.__dir_path, 'ajuda')
        return self.__api.send_message(ajuda_msg)

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
