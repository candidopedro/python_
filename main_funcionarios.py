class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
    
    def promover(self, novo_cargo):
        print(f'{self.nome} foi promovido(a) para a nova função de {novo_cargo}!')

    def informacoes(self):
        print(f'- Nome: {self.nome}')
        print(f'- Idade: {self.idade}')
        print(f'- Cargo: {self.cargo}\n')

colaborador1 = Pessoa('Pedro Henrique', 23, 'Dev Junior')
colaborador2 = Pessoa('João Paulo', 43, 'Analista Pleno')

colaborador1.promover('Dev Senior')

#colaborador1.informacoes()
#colaborador2.informacoes()