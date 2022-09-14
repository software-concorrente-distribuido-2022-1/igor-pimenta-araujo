import Pyro4
import json

@Pyro4.expose
class Server:
        
    def handle(self, data):
        request = json.loads(data)

        if request.get('cargo') == 'operador':
            return json.dumps({'Novo salario': str(request.get('salario') * 1.2)})
        elif request.get('cargo') == 'programador':
            return json.dumps({'Novo salario': str(request.get('salario') * 1.18)})
        else:
            return json.dumps({'Novo salario': str(request.get('salario') * 1)})

Pyro4.Daemon.serveSimple({
    Server: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 