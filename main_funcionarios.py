#Atualizar cargos
class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = int(idade)
        self.cargo = cargo
    
    def promover(self,novo_cargo):
        print(f'{self.nome} foi promovido(a) para a nova função de {novo_cargo}!\n')

    def informacoes(self):
        print(f'- Nome: {self.nome}')
        print(f'- Idade: {self.idade}')
        print(f'- Cargo: {self.cargo}\n')

    def nova_idade(self, nova_idade):
        if nova_idade > self.idade:
            self.idade = nova_idade
            print(f'Idade de {self.nome} atualizada para {self.idade}')
        return
    
colaborador1 = Pessoa('Pedro Henrique', 23, 'Dev Junior')
colaborador2 = Pessoa('João Paulo', 43, 'Analista Pleno')

colaborador1.informacoes()
colaborador2.informacoes()

#Atualização: 

colaborador1.promover('Dev Pleno')
colaborador2.promover('Analista Sênior')

colaborador1.nova_idade(24)
colaborador2.nova_idade(44)

print('Dados atualizados: ')
colaborador1.informacoes()
colaborador2.informacoes()