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
    request = json.loads(data)
    nome = request.get('nome')
    nivel = request.get('nivel')
    salario = request.get('salario')
    dependentes = request.get('dependentes')

    def salarioliquido(nome, nivel, salario, dependentes):
        if nivel == 'A':
            if dependentes == 0:
                return json.dumps({"salario" : salario*0.97})
            else:
                return json.dumps({"salario" : salario*0.93})
        elif nivel == 'B':
            if dependentes == 0:
                return json.dumps({"salario" : salario*0.95})
            else:
                return json.dumps({"salario" : salario*0.91})
        elif nivel == 'C':
            if dependentes == 0:
                return json.dumps({"salario" : salario*0.93})
            else:
                return json.dumps({"salario" : salario*0.89})
        elif nivel == 'D':
            if dependentes == 0:
                return json.dumps({"salario" : salario*0.91})
            else:
                return json.dumps({"salario" : salario*0.87})
        else:
            return json.dumps({"response" : "informe o nível"})

    return salarioliquido(nome, nivel, salario, dependentes)

server = BaseServer(3000, 1024, handler)
server.start_server()