import os
import server.app as app
import bot.seu_barriga as barriga
from concurrent.futures import ThreadPoolExecutor

def create_server():
    app_name = __name__
    port = os.getenv('PORT', '8000')
    return app.WebhookServer(app_name, int(port))
    
if __name__ == "__main__":
    server = create_server()
    tasks = [server.run, barriga.notice_billing]
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        