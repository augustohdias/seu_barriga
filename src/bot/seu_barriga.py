import os
from datetime import date

class SeuBarriga:
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
        pix = os.getenv('PIX', 'chavepixdementirinha')
        message_id = message['message_id']
        user = message['from']['first_name']
        
        pix_msg = self.__read_md_template('pix', params={'user': user, 'pix': pix})
        
        return self.__api.reply_message(pix_msg, message_id)

    def __padrao(self, message={}):
        return self.__api.send_message('**Pague o aluguel!**')

    def __ajuda(self, message={}):
        ajuda_msg = self.__read_md_template('ajuda')
        return self.__api.send_message(ajuda_msg)

    def __read_md_template(self, template_name, params={}):
        template_str = open(f'{self.__dir_path}/messages/{template_name}.md', 'r').read()
        for param in params:
            template_str = template_str.replace(f'<{param}>', params[param])
        return template_str

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
