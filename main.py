import os
import bot.seu_barriga
import concurrent.futures

def main():
    from http.server import BaseHTTPRequestHandler, HTTPServer

    class handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            message = "Pong"
            self.wfile.write(bytes(message, "utf8"))
            
    def start_http():
        with HTTPServer(('', int(os.environ['PORT'])), handler) as server:
            print('Starting ping...')
            server.serve_forever()    
            
    tasks = [bot.seu_barriga.notice_billing, bot.seu_barriga.read_updates, start_http]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
    


if __name__ == "__main__":
    main()
