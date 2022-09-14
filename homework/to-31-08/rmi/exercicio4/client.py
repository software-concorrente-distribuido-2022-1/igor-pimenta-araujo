import Pyro4

import json

ipAddressServer = "0.0.0.0"

server = Pyro4.core.Proxy('PYRO:Server@' + ipAddressServer + ':9090')
print(server.handle(json.dumps({ 'altura': 1.80, 'sexo': 'feminino'})))
print(server.handle(json.dumps({ 'altura': 1.80, 'sexo': 'masculino'})))