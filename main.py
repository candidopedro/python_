class Carro: #Sempre colocar a Primeira letra maiuscula, ex: CarroNovo
    def __init__(self, cor, ano, marca):
        self.cor = cor
        self.ano = ano 
        self.marca = marca
        self.ligado = True
    
    def informacoes_veiculo(self):
        print('Informações do veiculo:')
        print(f'Cor: {self.cor}')
        print(f'Ano: {self.ano}')
        print(f'Marca: {self.marca}')
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('O carro foi ligado')
        else:
            print('O carro já está ligado')


carro1 = Carro('Vermelho', 2026, 'Ferrari') #Passando as informações para caracterizar objeto
carro1.informacoes_veiculo() #Imprimindo as informações atribuidas ao objeto
carro1.ligar()