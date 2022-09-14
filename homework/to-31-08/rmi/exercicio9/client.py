import Pyro4

import json

ipAddressServer = "0.0.0.0"

server = Pyro4.core.Proxy('PYRO:Server@' + ipAddressServer + ':9090')
print(server.handle(json.dumps({ 'naipe': 1, 'valor': 1 })))
print(server.handle(json.dumps({ 'naipe': 2, 'valor': 2 })))
print(server.handle(json.dumps({ 'naipe': 3, 'valor': 3 })))
print(server.handle(json.dumps({ 'naipe': 4, 'valor': 4 })))
