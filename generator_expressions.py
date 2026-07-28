from sys import getsizeof # <-- Importando a função para mostrar o quanto determinada váriavel está consumindo na memória
# Para reduzir a quantidade de memoria utilizada em listas

numeros = [x * 10 for x in range (100)] # <-- Lista convencional []
print(numeros)
print('\nbytes:', getsizeof(numeros)) # <-- Observer a diferença da quantidade de bytes armazenados em cada um

print('\n','='*100,'\n')

numeros = (x * 10 for x in range (100)) # <-- Generetor expression ()
print(list(numeros))
print('\nbytes:', getsizeof(numeros)) # <-- Observer a diferença da quantidade de bytes armazenados em cada um