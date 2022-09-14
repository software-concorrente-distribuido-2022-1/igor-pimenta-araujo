from http import client
import json
import socket
import random

class BaseClient:

    def __init__(self, port, message_max_size):
        self.port = port
        self.message_max_size = message_max_size
        self.host = socket.gethostname()
        self.client_socket = socket.socket()

        self.client_socket.connect((self.host, self.port))
    
    def send_message(self, message):
        self.client_socket.send(message.encode())

        data = self.client_socket.recv(self.message_max_size).decode()
        if not data:
            return '-'
        return data
    
    def close_connection(self):
        self.client_socket.close() 

client = BaseClient(3001, 1024)

def carta():
    return client.send_message(json.dumps({ 'naipe': random.randrange(1, 5), 'valor': random.randrange(1, 14) }))

for i in range(10):
    print(carta())

