# Característica do FOR -> Cria-se uma váriavel dentro dele
for numero in range(1,5): #Partindo de 1 irá contar até 5, mas como ele conta sempre apartir do 0 é mostrado somente até o 4
    print(numero)

# Nested Loop
for numero1 in range(1,5):
    print(f'Produto {str(numero1)}')
    for numero2 in range (1,5):
        print(f'{numero2,numero1}')

# Uso do END - Space entre as letras
palavra = 'SUPER'

for space in palavra:
    print(f' {space}', end='') # Com o END ele só irá finalizar quando encontrar o que está entre os as áspas simples, que neste caso é vázio
print('\n')

# Retângulo 6x6

linha = 6
coluna = 6
simbulo = '@'

for l in range(linha):
    for c in range(coluna):
        print(f'{simbulo}', end='')
    print('')