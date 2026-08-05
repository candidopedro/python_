locais = {
    'brasil': 'brasilia',
    'frança': 'paris',
    'japão': 'tóquio'
}

pais = input('Digite um pais: ')

if pais.lower() in locais:
    print(f'A capital de {pais.capitalize()} é {str(locais[pais]).capitalize()}')
else:
    print('Desculpe! Não temos informações sobre a capital deste pais')