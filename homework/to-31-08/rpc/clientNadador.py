import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.nadador(6))
print(s.nadador(9))
print(s.nadador(12))
print(s.nadador(15))
print(s.nadador(18))

# Print list of available methods
print(s.system.listMethods())