import Pyro4

import json

ipAddressServer = "0.0.0.0"

server = Pyro4.core.Proxy('PYRO:Server@' + ipAddressServer + ':9090')
print(server.handle(json.dumps({ 'tempo': 20, 'idade': 40 })))
print(server.handle(json.dumps({ 'tempo': 30, 'idade': 65 })))