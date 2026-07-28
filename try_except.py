# Para especificar cada um dos erros, evitado e ajudando quando houver uma quebra no código
try:
    letras = ['a','b','c']
    print(letras[3]) # <-- O erro está localizando aqui, pois não há nada no index [3] (0,1,2)
except:
    print('Index não existe')