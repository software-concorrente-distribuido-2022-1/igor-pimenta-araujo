from urllib import request
import Pyro4
import json

@Pyro4.expose
class Card:

    def handle(self, data):
        request = json.loads(data)
        valor = request.get('valor')
        naipe = request.get('naipe')

        def carta(self, valor, naipe):
            if naipe == 1:
                naipeStr = 'Ouros'
            elif naipe == 2:
                naipeStr = 'Paus'
            elif naipe == 3:
                naipeStr = 'Copas'
            elif naipe == 4:
                naipeStr = 'Espadas'
            else:
                return json.dumps({'carta': "naipe invalido" })           

            if valor == 1:
                carta = 'As de ' + naipeStr
            elif valor == 2:
                carta = 'Dois de ' + naipeStr
            elif valor == 3:
                carta = 'Tres de ' + naipeStr
            elif valor == 4:
                carta = 'Quatro de ' + naipeStr
            elif valor == 5:
                carta = 'Cinco de ' + naipeStr
            elif valor == 6:
                carta = 'Seis de ' + naipeStr
            elif valor == 7:
                carta = 'Sete de ' + naipeStr
            elif valor == 8:
                carta = 'Oito de ' + naipeStr
            elif valor == 9:
                carta = 'Nove de ' + naipeStr
            elif valor == 10:
                carta = 'Dez de ' + naipeStr
            elif valor == 11:
                carta = 'Valete de ' + naipeStr
            elif valor == 12:
                carta = 'Dama de ' + naipeStr
            elif valor == 13:
                carta = 'Rei de ' + naipeStr
            else:
                carta = 'Valor invalido'
            
            return json.dumps({'carta': carta})

        return carta(self, valor, naipe)

Pyro4.Daemon.serveSimple({
    Card: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 