age = int(input('Digite sua idade: '))

if age < 13:
    print('\n- Você é uma criança')
elif age in range(13, 19):
    print('\n- Você é um adolescente')
else:
    print('\n- Você é um adulto')
