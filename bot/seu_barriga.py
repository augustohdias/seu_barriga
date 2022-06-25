import time 
from repository.telegram import *
from datetime import date, datetime

BILLING_DAY = 27

# def read_updates():
#     print('reading updates')
#     offset = -1
#     while True:
#         updates = get_updates(str(offset))
#         if updates == []:
#             continue
#         print('[DEBUG] Updates size: ' + len(updates) + ' // Updates: ' + updates)
#         for text in [u['message']['text'] for u in updates if '@SeuBarriga' in u['message']['text']]:
#             valid_commands = [c for c in COMMANDS.keys() if c in text]
#             first_command = '' if len(valid_commands) == 0 else valid_commands[0]
#             COMMANDS.get(first_command, padrao)()
#         offset = updates[-1]['update_id'] + 1
        
def notice_billing():
    print('waiting to notice')
    while True:
        today = date.today()
        days_to_payment = BILLING_DAY - int(today.strftime('%d'))
        hour = datetime.now().hour
        if days_to_payment < 5 and hour >= 19:
            "Lembrem-se de pagar o aluguel!"
        time.sleep(5 * 3600)

def aluguel():
    today = date.today()
    days_to_payment = str(BILLING_DAY - int(today.strftime('%d')))
    billing_date = str(BILLING_DAY) + today.strftime('/%m/%Y')
    "Vou cobrar o aluguel em " + days_to_payment + " dias (" + billing_date + ")."

def padrao():
    '**Pague o aluguel!**'

COMMANDS = {
    'aluguel': aluguel,
}
