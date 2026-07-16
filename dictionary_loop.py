aluno = {'nome':'João', 'idade': 14, 'media': 'B', 'aprovacao': True}

for x in aluno.keys(): # <-- Por padrão vem apenas as chaves
    print(x)
print('\n')
for x in aluno.values():
    print(x)
print('\n')
for x in aluno.items():
    print(x)
print('\n')
for keys,values in aluno.items(): # <-- Uma forma de extrair as Keys and Values do dicionário
    print(keys, values)