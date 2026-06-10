class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade) #Puxa as informações da Class Pai
        self.cargo = cargo

class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo

    def comprar(self, valor_produto):
        if self.saldo >= valor_produto:
            print(f'Parabéns {self.nome}!')
            print(f'Item de {valor_produto} adquirido!')
        else:
            print(f'Saldo insuficiente!{self.nome}')

#Cadastro de funcionários
funcionario1 = Funcionario('João', 27, 'Gerente')
funcionario1.apresentar()

#Cadastro e dados dos clientes
cliente1 = Cliente('Pedro', 23, 300)
cliente1.comprar(301)