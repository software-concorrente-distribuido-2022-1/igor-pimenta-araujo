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
    n1 = request.get('n1')
    n2 = request.get('n2')
    n3 = request.get('n3')

    def aprovado(n1, n2, n3):
        m = (n1 + n2) / 2
        if m >= 7:
            return json.dumps({'response': "Aprovado"})
        elif m >= 3 and m < 7:
            return json.dumps({'response': "fazer a N3"})
        else:
            return json.dumps({'response': "reprovado"})

    return aprovado(n1, n2, n3)

server = BaseServer(3001, 1024, handler)
server.start_server()