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
    valor = request.get('valor')
    naipe = request.get('naipe')

    def carta(valor, naipe):
        if naipe == 1:
            naipeStr = 'Ouros'
        elif naipe == 2:
            naipeStr = 'Paus'
        elif naipe == 3:
            naipeStr = 'Copas'
        elif naipe == 4:
            naipeStr = 'Espadas'
        else:
            return json.dumps({'carta': "naipe invalido" })           

        if valor == 1:
            carta = 'As de ' + naipeStr
        elif valor == 2:
            carta = 'Dois de ' + naipeStr
        elif valor == 3:
            carta = 'Tres de ' + naipeStr
        elif valor == 4:
            carta = 'Quatro de ' + naipeStr
        elif valor == 5:
            carta = 'Cinco de ' + naipeStr
        elif valor == 6:
            carta = 'Seis de ' + naipeStr
        elif valor == 7:
            carta = 'Sete de ' + naipeStr
        elif valor == 8:
            carta = 'Oito de ' + naipeStr
        elif valor == 9:
            carta = 'Nove de ' + naipeStr
        elif valor == 10:
            carta = 'Dez de ' + naipeStr
        elif valor == 11:
            carta = 'Valete de ' + naipeStr
        elif valor == 12:
            carta = 'Dama de ' + naipeStr
        elif valor == 13:
            carta = 'Rei de ' + naipeStr
        else:
            carta = 'Valor invalido'
        
        return json.dumps({'carta': carta})

    return carta(valor, naipe)

server = BaseServer(3001, 1024, handler)
server.start_server()