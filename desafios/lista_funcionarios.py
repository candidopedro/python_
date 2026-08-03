'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro
'''

funcionarios = set(['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'])
turno_dia = set(['Ana', 'Marcos', 'Alice', 'Melissa'])
turno_noite = set(['Pedro', 'Sophia', 'Bruno'])
tem_carro = set(['Marcos', 'Alice', 'Bruno', 'Melissa'])

lista1 = turno_noite & tem_carro
lista2 = turno_dia & tem_carro
lista3 = funcionarios - tem_carro

print(f'Funcionários que tem carro e trabalham a noite: {lista1}')
print(f'Funcionários que tem carro e trabalham durante o dia: {lista2}')
print(f'Funcionários que não tem carro: {lista3}')