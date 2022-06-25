from requests import request
from flask import Flask, request, jsonify

class WebhookServer:
    __app = None
    __behaviour = None 
    __port = 0
    
    def __init__(self, name, port, behaviour):
        self.__app = Flask(name)
        self.__behaviour = behaviour
        self.__port = port
        self.__setup_routes()

    def __setup_routes(self):
        @self.__app.route('/update', methods=['POST'])
        def update():
            body = request.get_json()
            message_text = ''
            try:
                message_text = body['message']['text']
            except:
                print(body)
                return {'ok': True, 'message': 'Nao deveria entender isso.'}
            print(body)
            commands = []
            if 'seubarriga' in message_text.lower():
                commands = [c for c in message_text.lower().split(' ') if c in self.__behaviour.valid_commands()]
                return {'ok': False, 'message': 'Mensagem vazia.'} if commands == [] else self.__behaviour.perform(commands[0], message=body['message'])
            return {'ok': True, 'message': 'Nao falaram comigo ainda.'}
                
        @self.__app.route('/ping', methods=['GET'])
        def ping():
            return jsonify({'response': 'pong'})
        
    def run(self):
        self.__app.run(host='0.0.0.0', port=int(self.__port))