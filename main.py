class Carro: #Sempre colocar a Primeira letra maiuscula, ex: CarroNovo
    def __init__(self, cor, ano, marca):
        self.cor = cor
        self.ano = ano 
        self.marca = marca
    
    def informacoes_veiculo(self):
        print('Informações do veiculo:')
        print(f'Cor: {self.cor}')
        print(f'Ano: {self.ano}')
        print(f'Marca: {self.marca}')

carro1 = Carro('Vermelho', 2026, 'Ferrari')
Carro.informacoes_veiculo()