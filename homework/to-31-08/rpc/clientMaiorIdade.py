import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.maioridade('João', 'masculino', 18))  # Returns 'João: já atingiu a maioridade'
print(s.maioridade('João', 'masculino', 17))  # Returns 'João: ainda não atingiu a maior idade'
print(s.maioridade('João', 'feminino', 21))  # Returns 'João: já atingiu a maioridade'
print(s.maioridade('João', 'feminino', 20))  # Returns 'João: ainda não atingiu a maior idade'
print(s.maioridade('João', 'outro', 20))  # Returns 'João: informe o sexo'

# Print list of available methods
print(s.system.listMethods())