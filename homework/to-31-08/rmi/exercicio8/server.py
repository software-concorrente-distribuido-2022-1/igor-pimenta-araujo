import Pyro4
import json

@Pyro4.expose
class Server:
        
    def handle(self, data):
        request = json.loads(data)
        saldo = request.get('saldo')

        def credito(saldo):
            if saldo <= 200:
                return json.dumps({ 'credito': '0'})
            elif saldo <= 400:
                return json.dumps({ 'credito': '20%'})
            elif saldo <= 600:
                return json.dumps({ 'credito': '30%'})
            else:
                return json.dumps({ 'credito': '40%'})

        return credito(saldo)

Pyro4.Daemon.serveSimple({
    Server: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 