from funcoes import somar, saudacao, verificador_idade
saudacao('Pedro')
print(somar(2,6))

maior_de_idade = verificador_idade(int(input('Qual a sua idade? ')))
print(f'É maior de idade? {maior_de_idade}')