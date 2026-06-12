#O objetivo é cirar a estrutura de uma escola com Aluno, Professor e Assistente do professor
#Cada aluno deve ter nome, idade matricula
#Cada professor deve ter nome, idade e materia

class Pessoa:
    def __init__(self, nome, idade, status):
        self.nome = nome 
        self.idade = idade
        self.status = status

    def status_pessoa(self):
        print(f'- Status: {"Ativo\n" if self.status == True else "Inativo\n"}') # <--- Aqui foi posto uma condicional em apenas uma linha

    def apresentar(self): # esta def existe na class Filho também - OBS
        print(f'- É um teste, {self.nome}! :)\n')  #Para mostrar que a class Filho sobrepoe a class Pai - OBS

class Aluno(Pessoa):
    def __init__(self, nome, idade, status, matricula):
        super().__init__(nome, idade, status)
        self.matricula = matricula

    def apresentar(self): #Esta está sobrepondo a class Pai - OBS
        print(f'Olá Aluno(a) {self.nome}!\n- Sua matrícula é: {self.matricula}\n')
        super().status_pessoa()
        super().apresentar() # <------------ Este "apresentar" vem da class Pai "Pessoa" e aparecerá apenas para os Alunos

class Professor(Pessoa):
    def __init__(self, nome, idade, status, materia):
        super().__init__(nome, idade, status)
        self.materia = materia
    
    def apresentar(self):
        print(f'Olá Professor(a) {self.nome}!\n- A(s) matéria(s) que você leciona: {self.materia}\n')
        super().status_pessoa()

class Assistente(Pessoa):
    def __init__(self, nome, idade, status, bloco):
        super().__init__(nome, idade, status)
        self.bloco = bloco

    def apresentar(self):
        print(f'Olá Assistente {self.nome}!\n- Você está com o bloco: {self.bloco}\n')
        super().status_pessoa()

#Alunos
aluno1 = Aluno(nome='Pedro', idade=23, status=True, matricula=14646789)# <---  Especificando os parâmetros para faciliar a LEITURA. Ex: nome='Pedro'
aluno1.apresentar()
aluno2 = Aluno(nome='Isaque', idade=21, status=False, matricula=43786322,)
aluno2.apresentar()

#Professores
professor1 = Professor(nome='Mauro', idade=54, status=False, materia='Matemática')
professor1.apresentar()
professor2 = Professor(nome='Karla', idade=45, status=True, materia='Biologia')
professor2.apresentar()

#Assistentes
assistente1 = Assistente(nome='Henrique', idade=25, status=True, bloco=16)
assistente1.apresentar()
assistente2 = Assistente(nome='Ana', idade=23, status=True, bloco=18)
assistente2.apresentar()