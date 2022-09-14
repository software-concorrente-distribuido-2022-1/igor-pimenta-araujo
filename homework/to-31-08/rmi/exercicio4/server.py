import Pyro4
import json

@Pyro4.expose
class Server:
        
    def handle(self, data):

        def pesoideal(altura, sexo):
            if sexo == 'masculino':
                pesoideal = (72.7 * altura - 58)
                return json.dumps({'pesoideal': pesoideal})
            elif sexo == 'feminino':
                pesoideal = (62.1 * altura - 44.7)
                return json.dumps({'pesoideal': pesoideal})
            else:
                return json.dumps({'response': "Sexo invalido"})


        request = json.loads(data)
        altura = request.get('altura')
        sexo = request.get('sexo')

        return pesoideal(altura, sexo)

Pyro4.Daemon.serveSimple({
    Server: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 