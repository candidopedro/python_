#Classes com o mesmo nome mas em arquivos diferente
# Ainda não identifiquei o por que -->   ---

class Computador:
    def __init__(self, modelo, modelo_gpu, vram, marca_cpu, modelo_cpu, nucleos_cpu):
        self.modelo = modelo
        self.gpu = self.GPU(modelo_gpu, vram) # Importa as informações da Class GPU e atribui a um objeto
        self.cpu = self.CPU(marca_cpu, modelo_cpu, nucleos_cpu) # Importa as informações da Class GPU e atribui a um objeto
    
    def mostrar_configuracoes(self):
        print(f'Computador: {self.modelo}')
        self.gpu.mostrar_gpu()
        self.cpu.mostar_cpu()

    class GPU: # Nested class - Uma classe dentro da outra 
        def __init__(self, modelo_gpu, vram):
            self.modelo_gpu = modelo_gpu
            self.vram = vram    
        
        def mostrar_gpu(self):
            print(f'Placa de vídeo: {self.modelo_gpu}')
            print(f'Quantidade de VRAM: {self.vram}GB')

    class CPU: # Nested class - Uma classe dentro da outra 
        def __init__(self, marca_cpu, modelo_cpu, nucleos_cpu):
            self.marca_cpu = marca_cpu
            self.modelo_cpu = modelo_cpu
            self.nucleos_cpu = nucleos_cpu
        
        def mostar_cpu(self):
            print(f'CPU: {self.marca_cpu} {self.modelo_cpu}')
            print(f' - Quantidade de núcleos: {self.nucleos_cpu}')

computador_1 = Computador('DELL XPS', 'RTX 5090', 12, 'Intel', 'i7-4790', 8)
Computador.mostrar_configuracoes(computador_1)
