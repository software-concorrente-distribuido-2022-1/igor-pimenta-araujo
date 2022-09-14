import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.aposentadoria(65,30))
print(s.aposentadoria(60,25))
print(s.aposentadoria(40,20))