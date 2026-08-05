cidades = ('SÃOPAULO', 'RIODEJANEIRO', 'SALVADOR')

cidade = input('Digite o nome da cidade: ')

if cidade.upper().replace(' ', '') in cidades:
    print(f'{cidade} está na lista de cidades')
else:
    print(f'{cidade} não está na lista de cidades')
