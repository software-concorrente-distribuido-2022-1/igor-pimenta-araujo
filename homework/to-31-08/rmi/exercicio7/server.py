import Pyro4
import json

@Pyro4.expose
class Server:
        
    def handle(self, data):
        request = json.loads(data)
        tempo = request.get('tempo')
        idade = request.get('idade')

        def aposentadoria(idade, tempo):
            if idade >= 65 and tempo >= 30:
                return json.dumps({ 'aposentadoria': 'sim'})
            elif idade >= 60 and tempo >= 25:
                return json.dumps({ 'aposentadoria': 'sim'})
            else:
                return json.dumps({ 'aposentadoria': 'nao'})

        return aposentadoria(idade, tempo)

Pyro4.Daemon.serveSimple({
    Server: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 