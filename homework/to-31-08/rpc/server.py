from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)

    # Register a function under a different name
    def adder_function(x, y):
        return x + y
    server.register_function(adder_function, 'add')

    """ 1 Faça um programa que leia o nome, o cargo e o salário de um funcionário e escreva
    seu salário reajustado. Se o cargo do funcionário for operador, ele deverá receber
    um reajuste de 20%, se for programador, ele deverá receber um reajuste de 18%. O
    programa deve escrever o nome do funcionário e seu salário reajustado. """
    def reajuste(nome, cargo, salario):
        if cargo == 'operador':
            return nome + ': ' + str(salario * 1.2)
        elif cargo == 'programador':
            return nome + ': ' + str(salario * 1.18)
        else:
            return nome + ': ' + str(salario)
    server.register_function(reajuste, 'reajuste')

    """ 2 Faça um programa que leia o nome, o sexo e a idade de uma pessoa e determine se
    a pessoa já atingiu a maioridade sabendo-se que: as pessoas do sexo masculino
    atingem a maioridade aos 18 anos e as pessoas do sexo feminino atingem a
    maioridade aos 21 anos. O programa deve escrever o resultado encontrado. """
    def maioridade(nome, sexo, idade):
        if sexo == 'masculino':
            if idade >= 18:
                return nome + ': já atingiu a maioridade'
            else:
                return nome + ': ainda não atingiu a maior idade'
        elif sexo == 'feminino':
            if idade >= 21:
                return nome + ': já atingiu a maioridade'
            else:
                return nome + ': ainda não atingiu a maior idade'
        else:
            return nome + ': informe o sexo'
    server.register_function(maioridade, 'maioridade')

    """ 3 Escreva um programa que leia as três notas (N1, N2 e N3) de um aluno de
    Faculdade e escreva se o mesmo foi aprovado ou reprovado. Considere as regras: se
    a média aritmética M, entre N1 e N2, for maior ou igual a 7,0, o aluno está
    aprovado; se a média aritmética M entre N1 e N2 for maior que 3,0 e menor que
    7,0, o aluno deve fazer a N3. O aluno é aprovado se a média aritmética entre M e
    N3 for maior ou igual a 5,0.  """
    def aprovado(n1, n2, n3):
        m = (n1 + n2) / 2
        if m >= 7:
            return 'aprovado'
        elif m >= 3 and m < 7:
            return 'fazer a N3'
        else:
            return 'reprovado'
    server.register_function(aprovado, 'aprovado')

    """ 4 Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
        programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
        - para homens: (72.7 * altura) – 58;
        - para mulheres (62.1 * altura) – 44.7.  """
    def pesoideal(altura, sexo):
        if sexo == 'masculino':
            return (72.7 * altura - 58)
        elif sexo == 'feminino':
            return (62.1 * altura - 44.7)
        else:
            return 'informe o sexo'
    server.register_function(pesoideal, 'pesoideal')

    """ Elabore um programa que leia a idade de um nadador e escreva em qual classificação
        o mesmo se enquadra, conforme as seguintes categorias:
        Categoria Idade
        infantil A 5 - 7 anos
        infantil B 8-10 anos
        juvenil A 11-13 anos
        juvenil B 14-17 anos
        adulto maiores de 18 anos """
    def nadador(idade):
        if idade >= 5 and idade <= 7:
            return 'infantil A'
        elif idade >= 8 and idade <= 10:
            return 'infantil B'
        elif idade >= 11 and idade <= 13:
            return 'juvenil A'
        elif idade >= 14 and idade <= 17:
            return 'juvenil B'
        else:
            return 'adulto'
    server.register_function(nadador, 'nadador')

    """ Faça um programa que leia o nome, nível, salário bruto e número de dependentes de
        um funcionário. A partir destes dados, o programa deve calcular e escrever o salário
        líquido do funcionário, juntamente com o seu nome e seu nível. Para o cálculo do
        salário líquido considere que:
         para o nível "A", o desconto é de 3% se o funcionário não tiver
        dependentes e 8% se o funcionário tiver dependentes;
         para o nível "B", o desconto é de 5% se o funcionário não tiver
        dependentes e 10% se o funcionário tiver dependentes;
         para o nível "C", o desconto é de 8% se o funcionário não tiver
        dependentes e 15% se o funcionário tiver dependentes;
         para o nível "D", o desconto é de 10% se o funcionário não tiver
        dependentes e 17% se o funcionário tiver dependentes. """
    def salarioliquido(nome, nivel, salario, dependentes):
        if nivel == 'A':
            if dependentes == 0:
                return nome + ': ' + str(salario * 0.97)
            else:
                return nome + ': ' + str(salario * 0.93)
        elif nivel == 'B':
            if dependentes == 0:
                return nome + ': ' + str(salario * 0.95)
            else:
                return nome + ': ' + str(salario * 0.91)
        elif nivel == 'C':
            if dependentes == 0:
                return nome + ': ' + str(salario * 0.93)
            else:
                return nome + ': ' + str(salario * 0.89)
        elif nivel == 'D':
            if dependentes == 0:
                return nome + ': ' + str(salario * 0.91)
            else:
                return nome + ': ' + str(salario * 0.87)
        else:
            return nome + ': informe o nível'
    server.register_function(salarioliquido, 'salarioliquido')

    """ Elabore um programa que escreva se um funcionário já pode se aposentar, a partir
    da leitura de sua idade e tempo de serviço. Considere que um funcionário só pode se
    aposentar se todas as condições abaixo forem satisfeitas:
    ter no mínimo 65 anos de idade;
    ter trabalhado, no mínimo, 30 anos;
    ter no mínimo 60 anos de idade e ter trabalhado no mínimo 25
    anos """
    def aposentadoria(idade, tempo):
        if idade >= 65 and tempo >= 30:
            return 'aposentar'
        elif idade >= 60 and tempo >= 25:
            return 'aposentar'
        else:
            return 'não aposentar'
    server.register_function(aposentadoria, 'aposentadoria')

    """ Um banco concederá um crédito especial aos seus clientes, variável com o saldo
    médio no último ano. Faça um programa que leia o saldo médio de um cliente e
    calcule o valor do crédito de acordo com a tabela abaixo. O programa deve mostrar
    uma mensagem informando o saldo médio e o valor do crédito.
    Saldo médio Percentual de Crédito
    de 0 a 200 nenhum crédito
    de 201 a 400 20% do valor do saldo médio
    de 401 a 600 30% do valor do saldo médio
    acima de 601 40% do valor do saldo médio """
    def credito(saldo):
        if saldo <= 200:
            return 'nenhum crédito'
        elif saldo <= 400:
            return '20% do valor do saldo médio'
        elif saldo <= 600:
            return '30% do valor do saldo médio'
        else:
            return '40% do valor do saldo médio'
    server.register_function(credito, 'credito')

    """ Escreva uma classe que encapsule uma carta de baralho, com um valor que
    represente o valor da carta, de um (ás) a treze (rei), e outro valor correspondente ao
    naipe (1 = ouros, 2 = paus, 3 = copas e 4 = espadas). Escreva nessa classe um
    método que imprima o nome da carta por extenso. Escreva ainda um programa em
    Java que instancie alguns objetos desta classe."""
    class CartaClass:
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
                return 'Naipe inválido'            

            if valor == 1:
                return 'Ás de ' + naipeStr
            elif valor == 2:
                return 'Dois de ' + naipeStr
            elif valor == 3:
                return 'Três de ' + naipeStr
            elif valor == 4:
                return 'Quatro de ' + naipeStr
            elif valor == 5:
                return 'Cinco de ' + naipeStr
            elif valor == 6:
                return 'Seis de ' + naipeStr
            elif valor == 7:
                return 'Sete de ' + naipeStr
            elif valor == 8:
                return 'Oito de ' + naipeStr
            elif valor == 9:
                return 'Nove de ' + naipeStr
            elif valor == 10:
                return 'Dez de ' + naipeStr
            elif valor == 11:
                return 'Valete de ' + naipeStr
            elif valor == 12:
                return 'Dama de ' + naipeStr
            elif valor == 13:
                return 'Rei de ' + naipeStr
            else:
                return 'Valor inválido'

    server.register_instance(CartaClass())

    # Run the server's main loop
    server.serve_forever()