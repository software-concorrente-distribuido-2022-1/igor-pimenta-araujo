import xmlrpc.client
import time

while True:
    time.sleep(1)
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        resposta = proxy.produce()
        if resposta < 10:
            print("Produzido! total: " + str(resposta))
        else:
            print("Não há espaço para produzir.")