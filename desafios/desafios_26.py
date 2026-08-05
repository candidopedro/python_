def potencia(base, expo):
    return base**expo

num1 = int(input('Digite a base: '))
try:
    num2 = int(input('Digite o expoente (default 2): '))
except ValueError:
    num2 = 2

print(f'- Resultado: {potencia(num1,num2)}')