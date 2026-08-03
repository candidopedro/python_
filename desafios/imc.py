altura = float(input('- Qual sua altura(m)? '))
peso = float(input(' - Qual seu peso(Kg)? '))

imc = peso / (altura**2)

print('='*25)
if imc < 18.5:
    print(f'| IMC = {imc:.2f}\n| Magreza')
elif imc >= 18.5 and imc <= 24.9:
    print(f'| IMC = {imc:.2f}\n| Normal')
elif imc >= 25 and imc <= 29.9:
    print(f'| IMC = {imc:.2f}\n| Sobrepeso')
elif imc >= 30 and imc <= 39.9:
    print(f'| IMC = {imc:.2f} \n| Obesidade')
else:
    print(f'| IMC = {imc:.2f}\n| Obsidade Grave!')
print('='*25)