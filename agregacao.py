# Criando classes que não dependem uma da outra
# Neste caso o motor pode existir sem o carro em si

class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia
    
class Carro:
    def __init__(self):
        self.motores = []

    def adicionar_motor(self, motor):
        self.motores.append(motor)

    def listar_motores(self):
        for motor in self.motores:
            print(f'Marca: {motor.marca} - Potencia: {motor.potencia}')

#Cadastro de motor
motor_v6 = Motor('Ford', 300)

#Adicionando motor
carro = Carro()
carro.adicionar_motor(motor_v6)

#Listar motor
carro.listar_motores()
