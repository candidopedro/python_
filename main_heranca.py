class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie
    
    def apresentar(self):
        print(f'Eu sou o {self.especie} chamado na cor {self.cor}')

class Gato(Animal): #Utilizará os mesmos atributos da Class pai (ANIMAL)
    def emitir_som(self):
        print('Miau!\n')
    #pass #Dá as atribuições e passa direto

class Cachorro(Animal):
    def emitir_som(self):
        print('Au-Au!\n')
    
gato1 = Gato('Life', 'cinza', 'Ragdoll')
gato1.apresentar()
gato1.emitir_som()

cachorro1 = Cachorro('Clifford', 'Vermelho', 'Labrador')
cachorro1.apresentar()
cachorro1.emitir_som()