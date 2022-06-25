from requests import request
from flask import Flask, request, jsonify

class WebhookServer:
    __app = None
    __api = None 
    __port = 0
    
    def __init__(self, name, port, api):
        self.__app = Flask(name)
        self.__api = api
        self.__port = port
        
        @self.__app.route('/update', methods=['POST'])
        def update():
            data = request.get_json()
            print(str(data))
            # self.__api.send_message('Teste')
            return data
        
        @self.__app.route('/ping', methods=['GET'])
        def ping():
            return jsonify({'response': 'pong'})
    
    def run(self):
        self.__app.run(host='', port=int(self.__port))