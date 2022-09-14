import json
import socket

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
    if request.get('cargo') == 'operador':
        return json.dumps({'Novo salario': str(request.get('salario') * 1.2)})
    elif request.get('cargo') == 'programador':
        return json.dumps({'Novo salario': str(request.get('salario') * 1.18)})
    else:
        return json.dumps({'Novo salario': str(request.get('salario') * 1)})

server = BaseServer(3001, 1024, handler)
server.start_server()