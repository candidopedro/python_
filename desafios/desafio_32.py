lista = [n for n in range(1,11)]
quadrado = lambda num: num ** 2

resultado = []
for numero in lista:
    print(f'{numero}² = {quadrado(numero)}')
    resultado.append(quadrado(numero))

print(f'\n{resultado}')