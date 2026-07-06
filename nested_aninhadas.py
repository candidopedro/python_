#Classes com o mesmo nome mas em arquivos diferente

# Ainda não identifiquei o por que -->   ---

class Computador:
    def __init__(self, modelo, gpu_nome, modelo_gpu, vram):
        self.modelo = modelo
        self.gpu_nome = gpu_nome # ---
        self.gpu = self.GPU(modelo_gpu, vram) # ---
    
    def mostrar_configuracoes_(self):
        print(f'Computador: {self.modelo}')

    class GPU: # Nested class - Uma classe dentro da outra 
        def __init__(self, modelo_gpu, vram):
            self.modelo_gpu = modelo_gpu
            self.vram = vram    
        
        def mostrar_gpu(self):
            print(f'')