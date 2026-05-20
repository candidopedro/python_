#Quantos dias um produto duraria se a pessoa usar X porções por dia

print('Teste de duração')
total_porcoes = int(input('Quantas porções o produto tem?'))
porcoes_por_dia = int(input('Quantas porções você consome por dia?'))

dias = total_porcoes/porcoes_por_dia

print(f'Vai durar {int(dias)} dias')