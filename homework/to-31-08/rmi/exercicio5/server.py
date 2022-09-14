import Pyro4
import json

@Pyro4.expose
class Server:
        
    def handle(self, data):
        request = json.loads(data)
        idade = request.get('idade')

        def nadador(idade):
            if idade >= 5 and idade <= 7:
                return json.dumps({ 'categoria': 'infantil A'})
            elif idade >= 8 and idade <= 10:
                return json.dumps({ 'categoria': 'infantil B'})
            elif idade >= 11 and idade <= 13:
                return json.dumps({ 'categoria': 'juvenil A'})
            elif idade >= 14 and idade <= 17:
                return json.dumps({ 'categoria': 'juvenil B'})
            else:
                return json.dumps({ 'categoria': 'adulto'})

        return nadador(idade)

Pyro4.Daemon.serveSimple({
    Server: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 