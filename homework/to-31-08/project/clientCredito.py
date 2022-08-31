import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.credito(200))
print(s.credito(400))
print(s.credito(600))
print(s.credito(800))