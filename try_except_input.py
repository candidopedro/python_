while Exception: # <-- Enquanto a Exception for executada a estrutura será repetida, criando um loop, que o usuário só sairá quando um valor valido for atribuido a váriavel 'numero'
    try:
        numero = int(input('Digite um número: '))
    except ValueError:
           print('Digite um número, por favor')