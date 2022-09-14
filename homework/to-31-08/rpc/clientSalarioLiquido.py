import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.salarioliquido('Igor', "A" , 1000, 3))
print(s.salarioliquido('Igor', "A" , 1000, 0))
print(s.salarioliquido('Igor', "B", 1000, 3))
print(s.salarioliquido('Igor', "B", 1000, 0))
print(s.salarioliquido('Igor', "C", 1000, 3))
print(s.salarioliquido('Igor', "C", 1000, 0))
print(s.salarioliquido('Igor', "D", 1000, 3))
print(s.salarioliquido('Igor', "D", 1000, 0))

# Print list of available methods
print(s.system.listMethods())