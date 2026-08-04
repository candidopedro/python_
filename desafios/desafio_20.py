numeros  = [item for item in range(1,11)]

for numero in numeros:
    if numero % 2 == 0 :
        print(f'{numero} --> PAR')
    else:
        print(f'{numero} --> ÍMPAR')