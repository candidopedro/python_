#Faça a atribuição de peças compartilhadas no grupo Volkswagen

class GrupWagen:
    def __init__(self, marca):
        self.marca = marca
        self.motor = 'EA825'

    def apresentar(self):
        print(f'Este carro é da {self.marca} e tem o motor {self.motor}\n')

class CaynneTurboGt(GrupWagen):
    pass

class RsQ8(GrupWagen):
    pass

class Bentayga(GrupWagen):
    pass

caynne = CaynneTurboGt('Porsche')
caynne.apresentar()

rsq8 = RsQ8('Audi')
rsq8.apresentar()

bentayga = Bentayga('Bentley')
bentayga.apresentar()

    