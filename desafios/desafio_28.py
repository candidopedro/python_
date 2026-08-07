def dobrar (num):
    return num * 2

def quadrado(num):
    return num ** 2

numero = int(input('Digite um número: '))
print(f'Resultado: {quadrado(dobrar(numero))}')