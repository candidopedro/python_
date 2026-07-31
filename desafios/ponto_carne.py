temperatura = int(input('Qual a temperatura da carne (°C)? '))

if temperatura < 48:
    print('- Carne precisa cozinhar por mais alguns minutos')
elif temperatura >= 48 and temperatura <= 53:     
    print('- Carne está selada')
elif temperatura >= 54 and temperatura <= 59:
    print('- Carne está ao ponto para o mal')
elif temperatura >= 60 and temperatura <= 64:
    print('- Carne está ao ponto para')
elif temperatura >= 65 and temperatura <= 70:
    print('- Carne está ao ponto para o bem')
elif temperatura >=71:
    print('- A carne está bem passada')

# Trabalhando com 'range' - MAIS PRÁTICO
if temperatura < 48:
    print('- Carne precisa cozinhar por mais alguns minutos')
elif temperatura in range(48, 53):     
    print('- Carne está selada')
elif temperatura in range(54, 59):
    print('- Carne está ao ponto para o mal')
elif temperatura in range(60, 64):
    print('- Carne está ao ponto')
elif temperatura in range(65, 70):
    print('- Carne está ao ponto para o bem')
elif temperatura >=71:
    print('- A carne está bem passada')