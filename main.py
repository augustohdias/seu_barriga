import os, queue
import server.app as app
from repository.telegram import TelegramAPI
import bot.seu_barriga as barriga
from concurrent.futures import ThreadPoolExecutor


def create_server(api):
    app_name = __name__
    port = os.getenv('PORT', '8000')
    return app.WebhookServer(app_name, int(port), api=api)
    
if __name__ == "__main__":
    api =  TelegramAPI()
    server = create_server(api)
    tasks = [server.run, barriga.notice_billing]
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        