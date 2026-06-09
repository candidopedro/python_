class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.name} e tenho {self.idade} anos')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade) #Puxa as informações da Class Pai
        self.cargo = cargo

class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo

    def comprar(self,valor_produto):
        if self.saldo >= valor_produto:
            print(f'Parabéns {self.nome}!')
            print(f'Item de {valor_produto} adquirido!')
        else:
            print('Saldo insuficiente!')
    
cliente1 = Cliente.comprar('')