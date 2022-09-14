import Pyro4

import json

ipAddressServer = "0.0.0.0"

server = Pyro4.core.Proxy('PYRO:Server@' + ipAddressServer + ':9090')
print(server.handle(json.dumps({ 'nome': 'Igor', 'salario': 6600.00, 'nivel': 'B', 'dependentes': 0 })))