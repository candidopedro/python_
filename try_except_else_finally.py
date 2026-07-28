try:
    numero = int(input('Digite um número: '))
except ValueError:
    print('\nDigite um número!')
else: # <-- Será executado QUANDO TRY for verdadeiro (true)
    print('Número válido')
finally: # <-- SEMPRE será executado após o try e o except
    print('Fim do script')