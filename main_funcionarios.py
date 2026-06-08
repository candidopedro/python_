#Atualizar cargos
class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
    
    def promover(self):
        self.cargo = input(f'Digite o novo cargo de {self.nome}: ')
        print(f'{self.nome} foi promovido(a) para a nova função de {self.cargo}!\n')

    def informacoes(self):
        print(f'- Nome: {self.nome}')
        print(f'- Idade: {self.idade}')
        print(f'- Cargo: {self.cargo}\n')

colaborador1 = Pessoa('Pedro Henrique', 23, 'Dev Junior')
colaborador2 = Pessoa('João Paulo', 43, 'Analista Pleno')


colaborador1.informacoes()
colaborador2.informacoes()

colaborador1.promover()
colaborador2.promover()

print('Dados atualizados: ')
colaborador1.informacoes()
colaborador2.informacoes()