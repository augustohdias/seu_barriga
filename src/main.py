import os
import server.app as app
from bot.seu_barriga import SeuBarriga
from repository.telegram import TelegramAPI
from concurrent.futures import ThreadPoolExecutor

def create_server():
    bot = SeuBarriga(27, TelegramAPI())
    port = os.getenv('PORT', '8000')
    app_name = __name__
    return app.WebhookServer(app_name, int(port), bot)
    
if __name__ == "__main__":
    server = create_server()
    tasks = [server.run]
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        