#Desconto
valor = float(input('Digite o valor do produto: '))
desconto = int(input('Digite o percentual de desconto:'))

valor_com_desconto = valor - (valor * (desconto/100))
print (f'Valor final do produto: {valor_com_desconto}')