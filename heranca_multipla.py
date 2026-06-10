#Aqui vemos uma dependencia das classe abaixo da classe "AVÔ" uma passa a informação para a outra de modo que uma complemente a outra

#Classe Avô
class Animal:
    def __init__(self, nome):
        self.nome = nome
        
#Classes Pai
class Predador(Animal):
    def cacando(self):
        print(f'- {self.nome} está caçando!\n')

class Presa(Animal):
    def fugindo(self):
        print(f'- {self.nome} está sendo fugindo!\n')

#Classes filho
class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Presa, Predador):
    pass

coelho1 = Coelho('Bunny')

tigre1 = Tigre('Kenny')

golfinho1 = Golfinho('Teodor')

coelho1.fugindo()

tigre1.cacando()

golfinho1.cacando()
golfinho1.fugindo()