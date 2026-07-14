# Somos donos de uma loja online, que possui vendedores tercerizados - assim com a shopee. Mas precisamos ter uma margem de lucro de 10% sobre cada produto postados por eles se maior que R$20
value_product = 0

print(f'{'='*15} AMAZON {'='*15}\n')

while value_product <= 20:
    value_product = float(input('Digite o valor do produto: R$')) 
print(f' - Lucro obtido por unidade: R${value_product-(value_product*0.10)}')
