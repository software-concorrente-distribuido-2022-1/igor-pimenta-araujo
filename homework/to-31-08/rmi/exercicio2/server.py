import Pyro4
import json

import functools

@Pyro4.expose
class Server:
        
    def handle(self, data):
        request = json.loads(data)
        nome = request.get('nome')
        sexo = request.get('sexo')
        idade = request.get('idade')

        def maioridade(nome, sexo, idade):
            if sexo == 'masculino':
                if idade >= 18:
                    return json.dumps({ 'name': nome, 'isMaior': True })
                else:
                    return json.dumps({ 'name': nome, 'isMaior': False })
            elif sexo == 'feminino':
                if idade >= 21:
                    return json.dumps({ 'name': nome, 'isMaior': True })
                else:
                    return json.dumps({ 'name': nome, 'isMaior': False })
            else:
                return False

        return maioridade(nome, sexo, idade)

Pyro4.Daemon.serveSimple({
    Server: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 