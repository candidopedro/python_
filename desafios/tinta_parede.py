rendimento = int(input('Qual é o rendimento da lata? '))
altura = int(input('Qual a altura da parede em metros? '))
largura = int(input('Qual a largura? '))

def calcular_tinta():
    area = largura * altura
    total = area / rendimento
    return total

print (f'Você precisará de {calcular_tinta()} latas de tinta.')
