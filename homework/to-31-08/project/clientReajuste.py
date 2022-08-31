import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.reajuste('João', 'operador', 1000))  # Returns 'João: 1200.0'
print(s.reajuste('João', 'programador', 1000))  # Returns 'João: 1000.0'
print(s.reajuste('João', 'outro', 1000))  # Returns 'João: 1000.0'
print(s.reajuste('João', 'outro', 1000))  # Returns 'João: 1000.0'

# Print list of available methods
print(s.system.listMethods())