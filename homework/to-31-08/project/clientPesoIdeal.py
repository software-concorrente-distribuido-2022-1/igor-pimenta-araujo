import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.pesoideal(1.70, 'masculino'))  # Returns 'João: ideal'
print(s.pesoideal(1.70, 'feminino'))  # Returns 'João: ideal'
print(s.pesoideal(1.70, 'outro'))  # Returns 'João: informe o sexo'

# Print list of available methods
print(s.system.listMethods())