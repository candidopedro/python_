from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento, cargo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
        self.cargo = cargo

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}\n'

    def calcular_idade(self):
        return int(datetime.now().year) - self.ano_nascimento

usuario1 = Funcionarios('João', 'Freitas', 2000, 'Gerente')
usuario2 = Funcionarios('Alex', 'Vieira', 1998, 'Assistênte')

# Nome + sobrenome
print(Funcionarios.nome_completo(usuario1))

# Calculando idade com base no ano de nascimento
print(f'Idade: {Funcionarios.calcular_idade(usuario1)}')