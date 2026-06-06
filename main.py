class Carro: #Sempre colocar a Primeira letra maiuscula, ex: CarroNovo
    def __init__(self, cor, ano, marca, ligado):
        self.cor = cor
        self.ano = ano 
        self.marca = marca
        self.ligado = bool(ligado)
    
    def informacoes_veiculo(self):
        print('Informações do veiculo:')
        print(f'Cor: {self.cor}')
        print(f'Ano: {self.ano}')
        print(f'Marca: {self.marca}')
        print(f'Está ligado: {self.ligado}')

carro1 = Carro('Vermelho', 2026, 'Ferrari', True) #Passando as informações para caracterizar objeto
carro1.informacoes_veiculo() #Imprimindo as informações atribuidas ao objeto