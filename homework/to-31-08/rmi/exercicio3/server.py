import Pyro4
import json

@Pyro4.expose
class Server:
        
    def handle(self, data):
        request = json.loads(data)
        n1 = request.get('n1')
        n2 = request.get('n2')
        n3 = request.get('n3')

        def aprovado(n1, n2, n3):
            m = (n1 + n2) / 2
            if m >= 7:
                return json.dumps({'response': "Aprovado"})
            elif m >= 3 and m < 7:
                return json.dumps({'response': "fazer a N3"})
            else:
                return json.dumps({'response': "reprovado"})

        return aprovado(n1, n2, n3)

Pyro4.Daemon.serveSimple({
    Server: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 