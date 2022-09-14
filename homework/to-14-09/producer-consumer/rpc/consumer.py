import xmlrpc.client
import time

while True:
    time.sleep(2)
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        resposta = proxy.consume()
        if resposta > 0:
            print("Consumido! total: " + str(resposta))
        else:
            print("Não há itens para consumir.")