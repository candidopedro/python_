par_ou_impar = lambda num: 'Par' if num % 2 == 0 else 'Ímpar'
numero = int(input('Digite um número: '))
print(f' - O número {numero} é {par_ou_impar(numero)}')