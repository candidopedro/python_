print (f'={'-'*10}= TABUADA ={'-'*10}=')

n = int(input('Deseja a tabuada de qual número? '))

lista = [1,2,3,4,5,6,7,8,9,10] # <-- Uma lista com os números que serão múltiplicados por 'n'

for cont in lista:
    lista2 = list(map(lambda x: n * x, lista)) # <-- Múltiplica cada item da lista pela número do input na váriavel 'n', e retorna em uma nova lista, chamada 'lista2'
    print(f'{n} x {cont} = {lista2[cont-1]}') # <-- Imprime 'n' o contador 'cont' e percorre a 'lista2' com 'cont'-1. O -1 foi uma "gambiarra" para alinhar os fatores na hora da impressão
