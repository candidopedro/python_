# Possui Key and Value
aluno = {'nome':'João', 'idade': 14, 'media': 'B', 'aprovacao': True} # 'nome' é a Key, 'João' é o value armazenado nela

aluno.update({'nome': 'Pedro', 'media':'A'}) # Atualizar/Alterar os itens

print(aluno.get('endereco', 'Este item não existe')) # Realiza a consulta e se o item não existir será retornado uma mensagem, que por padrão é NONE

print('==== Informações do aluno ====')
print(f' - Nome do aluno: {aluno['nome']}')
print(f' - Idade: {aluno['idade']}')
print(f' - Média: {aluno['media']}')
print(f' - Aprovado: {'Sim' if aluno['aprovacao'] == True else 'Não'}')

del aluno['aprovacao']



