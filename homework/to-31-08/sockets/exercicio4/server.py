import json
import socket
from threading import Thread

class BaseServer:

    def __init__(self, port, max_size, handler):
        self.port = port
        self.max_size = max_size
        self.handler = handler
    
    def start_server(self):
        host = '0.0.0.0'

        server_socket = socket.socket()
        server_socket.bind((host, self.port))

        print(f"Server started on port {self.port}")

        server_socket.listen(5)

        while True:
            connection, address = server_socket.accept()
            self.new_client(connection, address)

    def new_client(self, connection, address):
        while True:
            print(f"Incoming request from host {address}")
            data = connection.recv(self.max_size).decode()
            if not data:
                break
            message = self.handler(data)
            connection.send(message.encode())

        connection.close()

def handler(data):
    def pesoideal(altura, sexo):
        if sexo == 'masculino':
            pesoideal = (72.7 * altura - 58)
            return json.dumps({'pesoideal': pesoideal})
        elif sexo == 'feminino':
            pesoideal = (62.1 * altura - 44.7)
            return json.dumps({'pesoideal': pesoideal})
        else:
            return json.dumps({'response': "Sexo invalido"})


    request = json.loads(data)
    altura = request.get('altura')
    sexo = request.get('sexo')

    return pesoideal(altura, sexo)

server = BaseServer(3000, 1024, handler)
server.start_server()