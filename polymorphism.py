#Chamar as class e executar as def's de forma sequêncial através de um for (estrutura de repetição), criando uma lista para que seje possivel a execução em série

class Cachorro: 
    def emitir_som(self): # <--- Atente-se sempre para o (self)
        print('Au-Au-Au!')

class Gato:
    def emitir_som(self):
        print('Miau!')

animais = [Cachorro(), Gato()]

for a in animais:
    a.emitir_som()