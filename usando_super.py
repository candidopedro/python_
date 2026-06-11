#O objetivo é cirar a estrutura de uma escola com Aluno, Professor e Assistente do professor
#Cada aluno deve ter nome, idade matricula
#Cada professor deve ter nome, idade e materia

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def apresentar(self): # esta def existe na class Filho também - OBS
        print(f'É um teste {self.nome}! :)\n')  #Para mostrar que a class Filho sobrepoe a class Pai - OBS

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self): #Esta está sobrepondo a class Pai - OBS
        super().apresentar() # <------------ Este "apresentar" vem da class Pai "Pessoa" e aparecerá apenas para os Alunos
        print(f'Olá Aluno(a) {self.nome}!\n- Sua matrícula é: {self.matricula}\n')

class Professor(Pessoa):
    def __init__(self, nome, idade, materia):
        super().__init__(nome, idade)
        self.materia = materia
    
    def apresentar(self):
        print(f'Olá Professor(a) {self.nome}!\n- A(s) matéria(s) que você leciona: {self.materia}\n')

class Assistente(Pessoa):
    def __init__(self, nome, idade, bloco):
        super().__init__(nome, idade)
        self.bloco = bloco

    def apresentar(self):
        print(f'Olá Assistente {self.nome}!\n- Você está com o bloco: {self.bloco}\n')

aluno1 = Aluno('Pedro', 23, 14646789)
aluno1.apresentar()
aluno2 = Aluno('Isaque', 21, 43786322)
aluno2.apresentar()

professor1 = Professor('Mauro', 54, 'Matemática')
professor1.apresentar()
professor2 = Professor('Karla', 45, 'Biologia')
professor2.apresentar()

assistente1 = Assistente('Henrique', 25, 16)
assistente1.apresentar()
assistente2 = Assistente('Ana', 23, 18)
assistente2.apresentar()