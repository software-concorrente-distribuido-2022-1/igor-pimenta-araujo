import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.aprovado(7,8,9))  # Returns Aprovado
print(s.aprovado(7,6,4))  # Returns Fazer n3
print(s.aprovado(1,2,3))  # Returns Reprovado

# Print list of available methods
print(s.system.listMethods())