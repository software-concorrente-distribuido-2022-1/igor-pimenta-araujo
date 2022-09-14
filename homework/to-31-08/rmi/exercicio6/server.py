import Pyro4
import json

@Pyro4.expose
class Server:
        
    def handle(self, data):
        request = json.loads(data)
        nome = request.get('nome')
        nivel = request.get('nivel')
        salario = request.get('salario')
        dependentes = request.get('dependentes')

        def salarioliquido(nome, nivel, salario, dependentes):
            if nivel == 'A':
                if dependentes == 0:
                    return json.dumps({"salario" : salario*0.97})
                else:
                    return json.dumps({"salario" : salario*0.93})
            elif nivel == 'B':
                if dependentes == 0:
                    return json.dumps({"salario" : salario*0.95})
                else:
                    return json.dumps({"salario" : salario*0.91})
            elif nivel == 'C':
                if dependentes == 0:
                    return json.dumps({"salario" : salario*0.93})
                else:
                    return json.dumps({"salario" : salario*0.89})
            elif nivel == 'D':
                if dependentes == 0:
                    return json.dumps({"salario" : salario*0.91})
                else:
                    return json.dumps({"salario" : salario*0.87})
            else:
                return json.dumps({"response" : "informe o nível"})

        return salarioliquido(nome, nivel, salario, dependentes)

Pyro4.Daemon.serveSimple({
    Server: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 