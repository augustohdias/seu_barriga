import os, queue
import server.app as app
from repository.telegram import TelegramAPI
import bot.seu_barriga as barriga
from concurrent.futures import ThreadPoolExecutor


def create_server():
    api =  TelegramAPI()
    port = os.getenv('PORT', '8000')
    app_name = __name__
    return app.WebhookServer(app_name, int(port), api=api)
    
if __name__ == "__main__":
    server = create_server()
    tasks = [server.run]
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        