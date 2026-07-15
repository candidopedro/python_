# Possui Key and Value
aluno = {'nome':'João', 'idade': 14, 'media': 'A', 'aprovacao': True} # 'nome' é a Key, 'João' é o value armazenado nela

print('==== Informações do aluno ====')
print(f' - Nome do aluno: {aluno['nome']}')
print(f' - Idade: {aluno['idade']}')
print(f' - Média: {aluno['media']}')
print(f' - Aprovado: {'Sim' if aluno['aprovacao'] == True else 'Não'}')


